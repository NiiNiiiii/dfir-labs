# Executive Summary

This lab covers Microsoft Sentinel detection engineering around Microsoft Entra ID from connector validation through scheduled analytics, automation, workbook content, and a gated test deployment path for the exported content.

I built three identity-focused detections in Sentinel. The first looks for a failed sign-in burst from one IP across multiple users. The second tracks directory role assignment changes. The third watches for service principal credential additions. I also added a small identity workbook and a lightweight automation rule that tags new Lab 06 incidents with `lab06-identity`, so the lab shows a usable triage flow instead of stopping at query output.

I exported the analytics, automation rule, and workbook as repo-safe JSON and used GitHub OIDC into Azure to validate, package, preview with ARM `what-if`, approve, and deploy the content into a separate test workspace. That keeps the claim honest: this lab proves a portfolio-scale gated content pipeline, not a full enterprise multi-environment release platform.

The scope stays narrow on purpose. This is not an identity governance program, a broad XDR engineering project, or a finished Sentinel release platform. It is a focused lab built to show real Entra telemetry validation, real identity detections, clean supporting evidence, and a believable deployment story without padding the result.
