# Lab 06 redaction log

## Purpose

This file records what I reviewed before publishing Lab 06 and what I chose to redact, keep, or leave visible.

## Files reviewed

- `detections/exports/analytics/rule_failed_signin_burst.json`
- `detections/exports/analytics/rule_role_assignment_change.json`
- `detections/exports/analytics/rule_sp_credential_addition.json`
- `automation/exports/identity-triage-automation.export.json`
- `workbooks/exports/identity_dashboard.json`
- `notes/scenario-execution.md`
- `notes/oidc-setup.md`
- `README.md`
- `executive-summary.md`

## What I redacted

- tenant-specific user principal names where they were not needed in the public write-up
- the public source IP used during sign-in testing
- correlation identifiers that were only useful during local validation
- incidental identity detail that did not change the detection story

## What I intentionally kept

- rule names and detection descriptions
- exact `OperationName` values needed to explain the audit-based detection logic
- MITRE mappings
- rule schedules, thresholds, and entity mappings
- workbook section names and publish-safe query content
- scenario timestamps and sequence details needed to explain how the validation was performed
- OIDC setup values and resource identifiers that still appear in `notes/oidc-setup.md` and deployment-related artifacts as part of the execution record

## Verification notes

- I reviewed the exported analytics and automation content for live secrets, credentials, and user-specific ownership fields.
- I reviewed the workbook export and deployable JSON separately because they can carry workspace-specific references.
- This repo copy still contains some environment identifiers in the OIDC note, workbook export, and deployment artifacts. They are not secrets, but they are more specific than the narrative sections need.
- If I decide to scrub those values later, that should be treated as an approval-required documentation change so the evidence trail stays explicit.

## Result

The public write-up hides incidental user and source-IP detail, but this repo copy still retains some environment-specific identifiers in the setup and deployment record. That tradeoff should be treated as visible and intentional, not implied away.
