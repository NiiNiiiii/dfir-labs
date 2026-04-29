# DFIR / Detection Engineering Portfolio

DFIR and detection engineering portfolio with seven completed labs across Microsoft Sentinel, Microsoft Entra ID, Windows forensics, and AWS cloud security. The labs turn telemetry into investigations, detections, automation, and publish-safe deployment artifacts, including a gated Sentinel content deployment pipeline.

## Portfolio snapshot
- 7 completed labs
- 2 planned labs
- Publish-safe: screenshots, queries, exports, templates, manifests, and sanitized IOC material only — no raw evidence
- Reusable outputs: KQL, analytics exports, automation, workbooks, timelines, IOC packs, Terraform, Athena SQL, Lambda code, and evidence manifests

## What this portfolio shows
- Detection engineering, investigation, and response workflows across endpoint, identity, SIEM, and cloud
- Publish-safe, recruiter-reviewable lab documentation with reusable technical artifacts

## Start here
- [06 — Entra ID Detection Engineering + Gated Content Pipeline](labs/06-entra-id-detection-engineering-gated-content-pipeline/)  
  Validate Entra telemetry, build identity detections and triage content, and prove a gated GitHub OIDC validation/package/test-deploy path into a separate Sentinel workspace.

- [07 — AWS GuardDuty Detection + Response](labs/07-aws-guardduty-detection-response/)  
  Build AWS-native alerting, finding retention, Athena triage, and a Security Hub-driven response workflow.

- [04 — Endpoint Forensics Casework](labs/04-endpoint-forensics-casework/)  
  Triage MFT and EVTX artifacts, build a timeline, package IOCs, and uplift findings into Sentinel content.

- [05 — Windows Memory Forensics + Cloud SecOps Loop](labs/05-memory-forensics-cloud-secops-loop/)  
  Document Azure memory-acquisition constraints, pivot to process-memory proof, and complete the Sentinel hunt-to-response loop.

## All completed labs
| Lab | Focus | Status |
|---|---|---|
| [01 — Telemetry + SIEM Validation](labs/01-telemetry-siem-validation/) | Validate AMA/DCR onboarding and prove Heartbeat, Sysmon, and Security event ingestion in Sentinel | ✅ Done |
| [02 — Multi-Host Incident Reconstruction](labs/02-incident-reconstruction/) | Correlate cross-host activity into a timeline and operationalize the result as detection, automation, and workbook content | ✅ Done |
| [03 — Controls-to-Telemetry Audit](labs/03-controls-to-telemetry-audit/) | Test which security controls are observable and document gaps with validation queries and a coverage matrix | ✅ Done |
| [04 — Endpoint Forensics Casework](labs/04-endpoint-forensics-casework/) | Triage MFT and EVTX artifacts, build a timeline, package IOCs, and uplift findings into Sentinel content | ✅ Done |
| [05 — Windows Memory Forensics + Cloud SecOps Loop](labs/05-memory-forensics-cloud-secops-loop/) | Document Azure memory-acquisition constraints, pivot to process-memory proof, and complete the Sentinel hunt-to-response loop | ✅ Done |
| [06 — Entra ID Detection Engineering + Gated Content Pipeline](labs/06-entra-id-detection-engineering-gated-content-pipeline/) | Validate Entra telemetry, build identity detections and triage content, and prove a gated GitHub OIDC validation/package/test-deploy path into a separate Sentinel workspace | ✅ Done |
| [07 — AWS GuardDuty Detection + Response](labs/07-aws-guardduty-detection-response/) | Build AWS-native alerting, finding retention, Athena triage, and a Security Hub-driven response workflow | ✅ Done |

## Planned
| Lab | Focus | Status |
|---|---|---|
| 08 — Secure EKS AI Platform | Planned flagship lab for GitHub OIDC deployment, EKS Pod Identity, signed-image enforcement, platform hardening, runtime detection, AI abuse telemetry, and Security Hub response | 📋 Planned |
| 09 — AWS IAM + S3 Misconfiguration Response | Planned posture and remediation lab focused on unintended access, attribution, and control validation | 📋 Planned |

## Core stack

- **Microsoft security:** Microsoft Sentinel, Log Analytics, Microsoft Entra ID, AMA/DCR, KQL
- **Windows DFIR:** Sysmon, Windows Security Events, KAPE, MFTECmd, EvtxECmd, Timeline Explorer, Volatility 3
- **AWS security:** GuardDuty, Security Hub, IAM Access Analyzer, AWS Config, CloudTrail
- **Automation and deployment:** GitHub Actions, GitHub OIDC, Azure Bicep, Terraform, EventBridge, SNS, Lambda
- **Cloud investigation:** S3, Athena

## Notes
- Labs that create billable cloud services include teardown or cleanup guidance.

_Last updated: 2026-03-18_
