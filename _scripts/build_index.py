#!/usr/bin/env python3
"""Generate Markdown indexes from valid entity front matter."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "_indexes"
SKIP = {"_templates", "_indexes", ".git"}


def records() -> list[dict[str, str]]:
    found = []
    for path in sorted(ROOT.rglob("*.md")):
        if any(part in SKIP for part in path.parts) or path.name == "README.md":
            continue
        text = path.read_text(encoding="utf-8")
        match = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
        if not match:
            continue
        values = {}
        for line in match.group(1).splitlines():
            field = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
            if field:
                values[field.group(1)] = field.group(2).strip().strip("'\"")
        if values.get("id") and values.get("type"):
            values["path"] = path.relative_to(ROOT).as_posix()
            found.append(values)
    return sorted(found, key=lambda item: item["id"])


def write_index(filename: str, title: str, selected: list[dict[str, str]]) -> None:
    lines = [f"# {title}", "", "> This file is generated. Do not edit manually.", "", "| ID | Title | Status | Confidence | Link |", "|---|---|---|---|---|"]
    for item in selected:
        link = "../" + item["path"]
        title_text = item.get("title", "").replace("|", "\\|")
        lines.append(f"| {item['id']} | {title_text} | {item.get('status', '')} | {item.get('confidence', '')} | [Open]({link}) |")
    if not selected:
        lines.append("| — | No entities yet | — | — | — |")
    (OUTPUT / filename).write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    all_records = records()
    OUTPUT.mkdir(exist_ok=True)
    write_index("entities.md", "All Entities", all_records)
    for filename, title, entity_type in [("problems.md", "Problems", "problem"), ("opportunities.md", "Opportunities", "opportunity"), ("questions.md", "Questions", "question")]:
        write_index(filename, title, [item for item in all_records if item["type"] == entity_type])
    print(f"Built 4 indexes from {len(all_records)} entities in {OUTPUT.relative_to(ROOT)}/.")


if __name__ == "__main__":
    main()
