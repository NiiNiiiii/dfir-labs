#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

PLACEHOLDER_MARKERS = [
    "TODO",
    "TBD",
    "FILL IN",
    "CHANGEME",
    "REPLACE_ME",
    "<placeholder>",
    "<todo>",
]

EXPECTED = [
    {
        "doc": "detections/docs/01_failed_signin_burst_by_ip.md",
        "kql": "kql/analytics/failed_signin_burst_by_ip.kql",
        "export": "detections/exports/analytics/rule_failed_signin_burst.json",
        "table": "SigninLogs",
    },
    {
        "doc": "detections/docs/02_directory_role_assignment_change.md",
        "kql": "kql/analytics/directory_role_assignment_change.kql",
        "export": "detections/exports/analytics/rule_role_assignment_change.json",
        "table": "AuditLogs",
    },
    {
        "doc": "detections/docs/03_service_principal_credential_addition.md",
        "kql": "kql/analytics/service_principal_credential_addition.kql",
        "export": "detections/exports/analytics/rule_sp_credential_addition.json",
        "table": "AuditLogs",
    },
]


def rel(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_detection_metadata.py <lab_dir>")
        return 2

    lab_dir = Path(sys.argv[1]).resolve()
    repo_root = lab_dir.parents[1]
    errors: list[dict[str, str]] = []

    for item in EXPECTED:
        for key in ["doc", "kql", "export"]:
            path = lab_dir / item[key]
            if not path.exists() or path.stat().st_size == 0:
                errors.append({"path": rel(path, repo_root), "message": f"Required detection {key} file is missing or empty."})

        kql_path = lab_dir / item["kql"]
        if kql_path.exists():
            kql_text = kql_path.read_text(encoding="utf-8", errors="ignore")
            if item["table"] not in kql_text:
                errors.append({"path": rel(kql_path, repo_root), "message": f"Expected table name {item['table']} not found in KQL."})
            for marker in PLACEHOLDER_MARKERS:
                if marker in kql_text:
                    errors.append({"path": rel(kql_path, repo_root), "message": f"Unresolved placeholder marker found: {marker}"})

        doc_path = lab_dir / item["doc"]
        if doc_path.exists():
            doc_text = doc_path.read_text(encoding="utf-8", errors="ignore")
            for marker in PLACEHOLDER_MARKERS:
                if marker in doc_text:
                    errors.append({"path": rel(doc_path, repo_root), "message": f"Unresolved placeholder marker found: {marker}"})

    param_path = lab_dir / "pipeline" / "parameters" / "test.parameters.json"
    if param_path.exists():
        text = param_path.read_text(encoding="utf-8", errors="ignore")
        for marker in PLACEHOLDER_MARKERS + ["OperationNameHere", "operation-name-here", "fill-me"]:
            if marker in text:
                errors.append({"path": rel(param_path, repo_root), "message": f"Unresolved parameter placeholder found: {marker}"})

    if errors:
        print("Detection metadata validation failed.")
        print(json.dumps({"errors": errors}, indent=2))
        return 1

    print("Detection metadata validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
