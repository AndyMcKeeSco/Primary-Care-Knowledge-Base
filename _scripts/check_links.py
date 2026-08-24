#!/usr/bin/env python3
"""Check relative file links in Markdown; URLs and anchors are V1 out of scope."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")


def main() -> int:
    errors: list[str] = []
    checked = 0
    for source in sorted(ROOT.rglob("*.md")):
        if ".git" in source.parts:
            continue
        for raw in LINK_RE.findall(source.read_text(encoding="utf-8")):
            destination = raw.strip().split(maxsplit=1)[0].strip("<>")
            if not destination or destination.startswith(("#", "http://", "https://", "mailto:")):
                continue
            checked += 1
            file_part = unquote(destination.split("#", 1)[0])
            target = (source.parent / file_part).resolve()
            try:
                target.relative_to(ROOT)
            except ValueError:
                errors.append(f"{source.relative_to(ROOT)}: link escapes repository: {destination}")
                continue
            if not target.exists():
                errors.append(f"{source.relative_to(ROOT)}: missing target: {destination}")
    if errors:
        print(f"Link check failed with {len(errors)} broken link(s):")
        for error in errors:
            print(f"  - {error}")
        return 1
    print(f"Link check passed: {checked} internal file link(s) checked.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
