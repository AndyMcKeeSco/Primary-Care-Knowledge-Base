#!/usr/bin/env python3
"""Validate the lightweight Markdown/YAML knowledge graph."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ENTITY_ROOTS = [
    *(ROOT / f"{n:02d}-{name}" for n, name in [
        (1, "system"), (2, "care-settings"), (3, "personas"),
        (4, "journeys"), (5, "workflows"), (6, "decisions"),
        (7, "interfaces"), (8, "problems"), (9, "claims"),
        (10, "evidence"), (11, "observations"), (12, "constraints"),
        (13, "solutions"), (14, "hypotheses"), (15, "opportunities"),
        (16, "experiments"), (17, "questions"),
    ]),
    ROOT / "_sources" / "catalogue",
    ROOT / "examples",
]
PREFIX_TYPES = {
    "ORG": "organisation", "CS": "care_setting", "SVC": "service",
    "PER": "persona", "JRN": "journey", "WFL": "workflow",
    "DEC": "decision", "INT": "interface", "PRB": "problem",
    "CLM": "claim", "EVD": "evidence", "OBS": "observation",
    "CON": "constraint", "SOL": "solution", "HYP": "hypothesis",
    "OPP": "opportunity", "EXP": "experiment", "QUE": "question",
    "SRC": "source",
}
REQUIRED = {"id", "type", "title", "status", "created", "updated", "tags", "relationships", "confidence", "provenance"}
CONFIDENCE = {"unknown", "low", "medium", "high"}
ID_RE = re.compile(r"^(%s)-\d{4,}$" % "|".join(PREFIX_TYPES))
REFERENCE_RE = re.compile(r"\b(?:%s)-\d{4,}\b" % "|".join(PREFIX_TYPES))


def entity_files() -> list[Path]:
    return sorted(
        path for root in ENTITY_ROOTS if root.exists()
        for path in root.rglob("*.md") if path.name != "README.md"
        and path not in {ROOT / "17-questions/research-backlog.md", ROOT / "17-questions/contradictions.md"}
    )


def front_matter(path: Path) -> tuple[dict[str, str], str] | None:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*(?:\n|$)", text, re.DOTALL)
    if not match:
        return None
    values: dict[str, str] = {}
    for line in match.group(1).splitlines():
        item = re.match(r"^([A-Za-z_][\w-]*):(?:\s*(.*))?$", line)
        if item:
            values[item.group(1)] = (item.group(2) or "").strip().strip("'\"")
    return values, match.group(1)


def main() -> int:
    errors: list[str] = []
    records: dict[str, Path] = {}
    references: list[tuple[Path, str]] = []
    files = entity_files()
    for path in files:
        relative = path.relative_to(ROOT)
        parsed = front_matter(path)
        if parsed is None:
            errors.append(f"{relative}: missing opening/closing YAML front matter")
            continue
        values, yaml = parsed
        missing = sorted(REQUIRED - values.keys())
        if missing:
            errors.append(f"{relative}: missing required fields: {', '.join(missing)}")
        entity_id = values.get("id", "")
        match = ID_RE.fullmatch(entity_id)
        if not match:
            errors.append(f"{relative}: invalid id {entity_id!r}")
        else:
            expected = PREFIX_TYPES[match.group(1)]
            if values.get("type") != expected:
                errors.append(f"{relative}: type {values.get('type')!r} does not agree with {match.group(1)} (expected {expected!r})")
            if entity_id in records:
                errors.append(f"{relative}: duplicate id {entity_id}; first seen in {records[entity_id].relative_to(ROOT)}")
            else:
                records[entity_id] = path
        if values.get("confidence") not in CONFIDENCE:
            errors.append(f"{relative}: invalid confidence {values.get('confidence')!r}")
        # IDs in front matter, excluding the entity's own ID, are graph references.
        for reference in REFERENCE_RE.findall(yaml):
            if reference != entity_id:
                references.append((path, reference))
    for path, reference in references:
        if reference not in records:
            errors.append(f"{path.relative_to(ROOT)}: referenced entity {reference} does not exist")
    if errors:
        print(f"Validation failed with {len(errors)} error(s):")
        for error in errors:
            print(f"  - {error}")
        return 1
    print(f"Validation passed: {len(records)} entities across {len(files)} Markdown files; all references resolve.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
