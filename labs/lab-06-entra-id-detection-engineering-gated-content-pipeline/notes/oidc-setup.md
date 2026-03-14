# Lab 06 OIDC setup record

## GitHub
- Org: Abdullah0417
- Repo: dfir-labs
- Environment: sentinel-test

## Azure app registration
- Display name: dfir-lab06-gh-oidc-test-20260313
- App ID / client ID: b342fac8-4e08-4869-97b9-6aaaa24a9075
- App object ID: bc380db1-f5fe-49c3-90f5-bf409e6794ba
- Service principal object ID: 3c96eb90-0fed-4385-aa83-6ba7a6e9eb0a

## Federated credential
- Name: github-sentinel-test
- Issuer: https://token.actions.githubusercontent.com
- Subject: repo:Abdullah0417/dfir-labs:environment:sentinel-test
- Audience: api://AzureADTokenExchange

## Azure RBAC
- Role: Contributor
- Scope: /subscriptions/d4c995f0-0cba-4d52-8272-4c568d44b677/resourceGroups/rg-dfir-lab06-test

## GitHub environment protection
- Required reviewers: enabled
- Reviewer listed: Abdullah0417
- Prevent self-review: disabled
- Deployment branches: protected branches only (`main`)

## Verification
- App verification command completed: YES
- Federated credential verification completed: YES
- RBAC verification completed: YES
- GitHub environment secrets configured: YES
- GitHub environment variables configured: YES
- Smoke-test workflow run ID: