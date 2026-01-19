# Week 01 — Governance Baseline + Evidence Automation (Free Tier / $0)

## Goals
- Build governance habits: RG scoping, tags, policy guardrails, audit trail.
- Build evidence habits: repeatable CLI collection, JSON artifacts, hash manifest.

## Alignment
- Job skills: governance, auditing, basic security operations evidence.
- SC-900: governance + auditing fundamentals.
- AZ-500: Policy + monitoring fundamentals.

---

## A) Portal tasks (rg-azsec-week01-portal)
1) Create `rg-azsec-week01-portal`
2) Add tags: Owner, Purpose, Week
3) Assign Policy: “Require a tag on resources” (Tag Name = Owner)
4) Review RG Activity Log (confirm create/tag/policy events)

Portal evidence saved locally: `reports/week01/portal/`
- RG list screenshot
- Tags screenshot
- Policy assignment screenshot
- Activity log screenshot

---

## B) CLI tasks (rg-azsec-week01-cli)
- az login
- az account show
- az group create --name rg-azsec-week01-cli --location eastus
- az group update --name rg-azsec-week01-cli --set tags.Owner=name tags.Purpose=azsec-lab tags.Week=01
- az policy definition list ... (find “Require a tag on resources” ID)
- az policy assignment create ... (scope = RG)
- az monitor activity-log list --resource-group rg-azsec-week01-cli --max-events 20 -o table

---

## D) Python automation (azsec)
Run (local-only outputs):
- azsec inventory --rg rg-azsec-week01-cli --out reports/week01/cli
- azsec activitylog --rg rg-azsec-week01-cli --out reports/week01/cli

Expected local files:
- reports/week01/cli/account.show.json
- reports/week01/cli/group.list.json
- reports/week01/cli/group.show.rg-azsec-week01-cli.json
- reports/week01/cli/activitylog.rg-azsec-week01-cli.json
- reports/week01/cli/manifest.json

---

## Commit checklist (what goes to GitHub)
Commit:
- README.md
- .gitignore
- pyproject.toml
- src/**
- docs/90-weekly-notes/week-01.md
- docs/91-call-chains/week-01.md

Do NOT commit:
- reports/**
- .venv/**
