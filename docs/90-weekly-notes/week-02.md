# Week 02 — RBAC + Policy Compliance Evidence (Free Tier / $0)

## Goals
- Learn Azure RBAC scope and role assignment auditing (subscription + RG).
- Export role definitions for core roles (Reader/Contributor/Owner).
- Export Azure Policy assignments + compliance summary at RG scope.
- Produce repeatable evidence artifacts with azsec-kit.

## Alignment
- Job skills: identity & access governance, least privilege, compliance visibility.
- SC-900: identity/access + compliance fundamentals.
- AZ-500: RBAC + policy/governance awareness.

---

## A) Portal tasks
### Subscription RBAC
- Subscriptions → <your subscription> → Access control (IAM) → Role assignments
- Screenshot: role assignments list

### RG RBAC
- Resource groups → rg-azsec-week01-cli → Access control (IAM) → Role assignments
- Screenshot: role assignments list

### Policy Compliance
- Policy → Compliance → scope to rg-azsec-week01-cli (or portal RG)
- Confirm Week 1 policy assignment visible
- Screenshot: compliance view

Save screenshots locally (DO NOT COMMIT):
- reports/week02/portal/

---

## B) CLI tasks
- Export subscription ID and RG ID
- az role assignment list at subscription scope
- az role assignment list at RG scope
- az role definition list for Reader/Contributor/Owner
- az policy assignment list at RG scope
- az policy state summarize for the RG

---

## D) Python automation
Run (LOCAL ONLY outputs):
- azsec rbac --rg rg-azsec-week01-cli --out reports/week02/cli
- azsec policy --rg rg-azsec-week01-cli --out reports/week02/cli

Expected local files (DO NOT COMMIT):
- reports/week02/cli/rbac.role-assignments.subscription.<subId(optional)>.json
- reports/week02/cli/rbac.role-assignments.rg.rg-azsec-week01-cli.json
- reports/week02/cli/rbac.role-definition.Reader.json
- reports/week02/cli/rbac.role-definition.Contributor.json
- reports/week02/cli/rbac.role-definition.Owner.json
- reports/week02/cli/policy.assignments.rg.rg-azsec-week01-cli.json
- reports/week02/cli/policy.state-summarize.rg.rg-azsec-week01-cli.json
- reports/week02/cli/manifest.json

---

## Commit checklist
Commit:
- README.md
- src/**
- docs/90-weekly-notes/week-02.md
- docs/91-call-chains/week-02.md

Do NOT commit:
- reports/**
- .venv/**
