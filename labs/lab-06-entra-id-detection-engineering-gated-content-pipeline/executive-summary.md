# Executive Summary

This lab shows practical Microsoft Sentinel detection engineering built around Microsoft Entra ID telemetry. The point was not to make a flashy “platform” claim. The point was to show a clean workflow: validate the data, build the hunts, promote the strongest logic into scheduled analytics, and package the results in a way that is reviewable and safe to publish.

I built three identity-focused detections in Sentinel. The first looks for a failed sign-in burst from one IP across multiple users. The second tracks directory role assignment changes. The third watches for service principal credential additions. I also added a small identity workbook so the results are easier to review, and a lightweight automation rule so the lab shows a basic investigation and response flow instead of stopping at query output.

From a hiring perspective, this lab demonstrates a few things that matter. I can validate Entra telemetry before I write detections. I can use KQL against real identity activity instead of canned sample data. I can turn hunt logic into scheduled analytics with usable mappings and incident creation. And I can export the content as code rather than presenting the work as screenshots alone.

The scope is intentionally narrow. This is not a full identity governance program, a complete multi-environment deployment pipeline, or a broad XDR engineering project. It is a focused portfolio lab built to show real telemetry validation, real Entra detections, usable Sentinel content, and disciplined documentation without overstating what was built.
