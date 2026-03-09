Hands-on DFIR and cloud SecOps labs covering enterprise telemetry, threat hunting, incident reconstruction, endpoint casework, memory triage, and AWS detection/response.

## What this proves
- I can build and validate end-to-end telemetry pipelines across Windows, Azure, and AWS.
- I can move from findings to hunts, detections, automation, and analyst-facing investigation views.
- I can perform publish-safe forensic casework: artifact triage, hashing, chain-of-custody, IOC packaging, and memory-triage pivots without committing raw evidence.
- I can ship operational artifacts as code: KQL, ARM/JSON exports, Athena SQL, Lambda response logic, and Terraform.

## Skills demonstrated
- Microsoft Sentinel (Log Analytics) investigation workflow: incidents, entities, timelines
- Azure Monitor Agent (AMA) + Data Collection Rules (DCR) telemetry onboarding
- Windows telemetry: Sysmon + Security Event Logs (authentication, admin, and persistence signals)
- KQL authoring, validation, joins, decoding, and charting
- Detection engineering: scheduled analytic rules, tuning notes, and MITRE mapping
- SOAR-lite automation: incident tagging, severity updates, and triage actions
- Endpoint forensics: KAPE, EVTX export, MFT parsing, artifact correlation, and publish-safe IOC packaging
- Memory triage under cloud constraints, including process-memory validation and strings-based proof
- AWS detection and response with GuardDuty, Security Hub, EventBridge, SNS, Lambda, Athena, S3, and Terraform
- DFIR discipline: reproducible artifacts in GitHub, raw evidence retained outside the repo

## Labs
| Lab | Focus | Status |
|---|---|---|
| [01 — Telemetry + SIEM Validation](labs/01-telemetry-siem-validation/) | Confirm ingestion and baseline Windows telemetry in Sentinel | ✅ Done |
| [02 — Multi-Host Incident Reconstruction](labs/02-incident-reconstruction/) | Reconstruct a cross-host intrusion timeline and operationalize detection | ✅ Done |
| [03 — Controls-to-Telemetry Audit](labs/03-controls-to-telemetry-audit/) | Prove which security controls are observable and where blind spots remain | ✅ Done |
| [04 — Endpoint Forensics Casework](labs/04-endpoint-forensics-casework/) | Triage disk and log artifacts, build a timeline, and uplift findings into detection content | ✅ Done |
| [05 — Windows Memory Forensics + Cloud SecOps Loop](labs/05-memory-forensics-cloud-secops-loop/) | Handle memory-triage constraints in Azure and complete the Sentinel detection-to-workbook loop | ✅ Done |
| 06 — Capstone Report | Package Labs 02, 04, and 05 into a consulting-style deliverable | 📋 Planned |
| [07 — AWS GuardDuty Detection + Response](labs/07-aws-guardduty-detection-response/) | Build AWS-native alerting, findings enrichment, and response workflow | ✅ Done |
| 08 — AWS IAM + S3 Misconfiguration Response | Detect and remediate unintended access with attribution and compliance validation | 📋 Planned |

Each completed lab includes a `README.md`, proof screenshots, and lab-specific artifacts such as KQL, detections, automation exports, workbooks, IOC packs, Athena queries, Lambda code, or Terraform where applicable.

_Last updated: 2026-03-09_

## Tooling / Stack
- Microsoft Sentinel + Log Analytics Workspace
- Azure Monitor Agent (AMA) + Data Collection Rules (DCR)
- Sysmon + Windows Security Event Logs
- Endpoint triage tooling: KAPE, MFTECmd, EvtxECmd, Timeline Explorer
- Volatility 3 and process-memory triage workflow
- AWS CLI, Terraform, Amazon GuardDuty, AWS Security Hub, Amazon EventBridge, Amazon SNS, AWS Lambda, Amazon Athena, Amazon S3, AWS CloudTrail, IAM Access Analyzer, AWS Config

## How to use this repo
- Start at any lab folder and read its `README.md` first.
- Use the screenshots to verify expected results and analyst-facing outputs.
- Review the artifact folders for reusable content such as queries, detections, automation, workbooks, Terraform, notes, and IOC packs.
- Treat each lab as a scoped case study with its own evidence, validation, and documentation trail.

## Notes / Safety
- Raw evidence is never published. No EVTX, MFT, memory dumps, binaries, or secrets are committed.
- The repo contains reproducible queries, exports, templates, screenshots, notes, and hash-based manifests only.
- Cloud cost and cleanup discipline matter. Labs that create billable resources are documented with teardown and cleanup notes.
- Access is kept narrow where possible. Avoid exposing management services directly to the public Internet.
