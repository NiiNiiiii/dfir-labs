#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

FAIL_TYPES = {"Delete"}
WARN_TYPES = {"Ignore", "Unsupported"}


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: evaluate_whatif.py <whatif-json-path>")
        return 2

    path = Path(sys.argv[1]).resolve()
    if not path.exists():
        print(f"what-if output not found: {path}")
        return 1

    data = json.loads(path.read_text(encoding="utf-8"))
    changes = data.get("changes", []) if isinstance(data, dict) else []

    fail = []
    warn = []
    for change in changes:
        change_type = change.get("changeType")
        resource_id = change.get("resourceId", "unknown-resource")
        if change_type in FAIL_TYPES:
            fail.append({"resourceId": resource_id, "changeType": change_type})
        elif change_type in WARN_TYPES:
            warn.append({"resourceId": resource_id, "changeType": change_type})

    print(json.dumps({"fail": fail, "warn": warn, "count": len(changes)}, indent=2))

    if fail:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
