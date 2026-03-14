#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path


def rel(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def load_json(path: Path) -> tuple[dict | list | None, str | None]:
    try:
        return json.loads(path.read_text(encoding="utf-8")), None
    except Exception as exc:
        return None, str(exc)


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_deployable_json.py <lab_dir>")
        return 2

    lab_dir = Path(sys.argv[1]).resolve()
    repo_root = lab_dir.parents[1]
    manifest_path = lab_dir / "pipeline" / "manifests" / "content-manifest.json"
    workbook_path = lab_dir / "pipeline" / "deploy" / "workbook.serialized.json"
    errors: list[dict[str, str]] = []

    manifest, err = load_json(manifest_path)
    if err:
        errors.append({"path": rel(manifest_path, repo_root), "message": f"Invalid JSON: {err}"})
    if manifest is None:
        print(json.dumps({"errors": errors}, indent=2))
        return 1

    for key in ["labId", "packageVersion", "deployables", "packageIncludes"]:
        if key not in manifest:
            errors.append({"path": rel(manifest_path, repo_root), "message": f"Manifest missing required key: {key}"})

    deployables = manifest.get("deployables", {}) if isinstance(manifest, dict) else {}
    analytics = deployables.get("analytics", []) if isinstance(deployables, dict) else []
    automation = deployables.get("automation", []) if isinstance(deployables, dict) else []
    workbook = deployables.get("workbook", {}) if isinstance(deployables, dict) else {}

    referenced_files: list[Path] = []
    for item in analytics + automation:
        if isinstance(item, dict) and "path" in item:
            referenced_files.append(lab_dir / item["path"])
    if isinstance(workbook, dict):
        for key in ["deployPath", "evidenceExportPath"]:
            if key in workbook:
                referenced_files.append(lab_dir / workbook[key])

    for path in referenced_files:
        if not path.exists():
            errors.append({"path": rel(path, repo_root), "message": "Referenced file is missing."})
            continue
        _, err = load_json(path)
        if err:
            errors.append({"path": rel(path, repo_root), "message": f"Invalid JSON: {err}"})

    workbook_obj, err = load_json(workbook_path)
    if err:
        errors.append({"path": rel(workbook_path, repo_root), "message": f"Invalid JSON: {err}"})
    elif isinstance(workbook_obj, dict):
        for key in ["displayName", "category", "version", "serializedData"]:
            if key not in workbook_obj:
                errors.append({"path": rel(workbook_path, repo_root), "message": f"Workbook deploy JSON missing key: {key}"})
        serialized = workbook_obj.get("serializedData")
        if not isinstance(serialized, dict) or not serialized.get("items"):
            errors.append({"path": rel(workbook_path, repo_root), "message": "serializedData must be an object with at least one workbook item."})

    if errors:
        print("Deployable JSON validation failed.")
        print(json.dumps({"errors": errors}, indent=2))
        return 1

    print("Deployable JSON validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
