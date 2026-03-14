#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

MARKDOWN_LINK_RE = re.compile(r'!?\[[^\]]*\]\(([^)]+)\)')


def rel(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_readme_evidence.py <lab_dir>")
        return 2

    lab_dir = Path(sys.argv[1]).resolve()
    repo_root = lab_dir.parents[1]
    readme = lab_dir / "README.md"
    errors: list[dict[str, str]] = []

    if not readme.exists():
        print(json.dumps({"errors": [{"path": rel(readme, repo_root), "message": "README.md is missing."}]}, indent=2))
        return 1

    text = readme.read_text(encoding="utf-8", errors="ignore")
    referenced_paths: list[Path] = []
    image_count = 0

    for match in MARKDOWN_LINK_RE.finditer(text):
        target = match.group(1).strip()
        if target.startswith("http://") or target.startswith("https://") or target.startswith("mailto:"):
            continue
        clean = target.split("#", 1)[0]
        if not clean:
            continue
        path = (readme.parent / clean).resolve()
        referenced_paths.append(path)
        if target.lower().startswith("screenshots/"):
            image_count += 1

    for path in referenced_paths:
        if not path.exists():
            errors.append({"path": rel(path, repo_root), "message": "README link target does not exist."})

    if image_count == 0:
        errors.append({"path": rel(readme, repo_root), "message": "README should reference at least one local screenshot for recruiter-facing proof."})

    screenshots_dir = lab_dir / "screenshots"
    if not screenshots_dir.exists() or not any(screenshots_dir.iterdir()):
        errors.append({"path": rel(screenshots_dir, repo_root), "message": "screenshots directory is missing or empty."})

    if errors:
        print("README evidence validation failed.")
        print(json.dumps({"errors": errors}, indent=2))
        return 1

    print("README evidence validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
