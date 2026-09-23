# Railway Project Hub Changelog

## 2026-09-23 — Canonical Hub v1 established

Application: Hub governance

Change:
- created canonical GitHub governance repository
- made README.md the first Hub commit
- added read-first agent contract and Hub rules
- registered MotionLab as App 01
- registered ReturnReview as App 02
- added Railway-native resource registry
- added API ownership registry
- added lifecycle, naming, secrets, recovery, deployment, and incident procedures

Reason:
Create a scalable governance model where each application remains isolated in its own Railway Project.

Risk:
Documentation/registry only. No Railway runtime change in this Hub setup.

Rollback:
Git history.

Result:
Pending merge/verification of governance v1 branch.

## 2026-09-23 — Shared-runtime experiment documented

Applications: MotionLab, ReturnReview

Observed state:
- canonical standalone MotionLab project still exists and is healthy
- canonical ReturnReview project still exists and is healthy
- duplicate app01-motionlab service exists inside ReturnReview
- three earlier Hub metadata entries exist inside ReturnReview

Decision:
Do not delete or modify the residue yet.

Reason:
Cleanup must follow inspect -> verify -> disable where practical -> explicit confirmation -> delete -> final audit.

## 2026-09-23 — App-side safety contracts installed

Applications: MotionLab, ReturnReview

Change:
- MotionLab README linked to Hub governance
- MotionLab AGENTS.md added
- MotionLab RAILWAY_HUB_RULES.md added
- ReturnReview README linked to Hub governance
- ReturnReview AGENTS.md extended for Railway
- ReturnReview RAILWAY_HUB_RULES.md added

Result:
Merged to each app's main branch.
