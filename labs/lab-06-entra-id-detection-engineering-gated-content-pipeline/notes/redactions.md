# Lab 06 redaction log

## Purpose

This file records what I reviewed before publishing Lab 06 and what I chose to redact, keep, or leave local.

## Files reviewed

- `detections/exports/analytics/rule_failed_signin_burst.json`
- `detections/exports/analytics/rule_role_assignment_change.json`
- `detections/exports/analytics/rule_sp_credential_addition.json`
- `automation/exports/identity-triage-automation.export.json`
- `workbooks/exports/identity_dashboard.json`
- `pipeline/deploy/workbook.serialized.json`
- supporting markdown notes used to explain the lab

## What I redacted in the public write-up

- the public source IP used during sign-in testing
- exact actor identities where a role label or generic description was enough
- full tenant-specific UPN values where a placeholder or sanitized alias was enough
- correlation identifiers that were only needed during validation
- exact app, object, and service principal IDs from the OIDC setup notes
- full subscription-scope resource IDs from the public OIDC notes

## What I intentionally kept

- rule names and detection descriptions
- `OperationName` values needed to explain the detection logic
- rule schedules, thresholds, and entity mappings
- workbook section names and the query logic needed to explain the analyst view
- scenario timestamps and sequence details needed to explain the validation flow
- the GitHub org, repo name, and environment name because they are part of the public repo story

## What stayed local or still needs a deliberate push decision

- `notes/lab06-values.env` stays local and should not be tracked
- `notes/federated-credential.local.json` is a local helper file and should not be tracked
- `artifacts/` contains runtime workflow output and deployment result files; keep it out of the public push unless you intentionally want those raw runtime artifacts public
- `dist/` contains generated package files; it is build output, not the source of truth

## Verification notes

- I reviewed the exported analytics and automation content for secrets, credentials, and user-specific ownership fields.
- I reviewed the workbook export more closely because workbook JSON can retain workspace-specific references as part of the export format.
- The narrower deployable workbook wrapper used for the gated deployment proof is `pipeline/deploy/workbook.serialized.json`.
- The fuller workbook evidence export under `workbooks/exports/identity_dashboard.json` still carries workspace-specific resource references. That is not a secret by itself, but it is extra environment detail and should be a deliberate publish decision.

## Result

The documentation layer is publish-safe after redaction. The remaining publish-safety judgment calls are the local-only helper files, the raw runtime files under `artifacts/`, and whether the full workbook export stays public in addition to the narrower deploy wrapper.
