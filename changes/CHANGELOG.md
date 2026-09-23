# Railway Project Hub Changelog

## 2026-09-23 — MotionLab duplicate cleanup approved

Applications: MotionLab, ReturnReview

Target:
- non-canonical service: `app01-motionlab`
- service ID: `25cc6232-ed7e-42fd-94e8-d180e641607f`
- project: ReturnReview

Pre-deletion verification:
- canonical standalone MotionLab project exists and is healthy
- canonical MotionLab service ID: `048331c3-43df-4bbb-a1a5-1cea4adcfc5d`
- both services deploy from `Rishikeshsanin/animation-website`
- duplicate has no custom variables/secrets
- duplicate has no volume, database, bucket, cron, or custom domain
- duplicate has no unique persistent data
- ReturnReview API/web have no explicit dependency on the duplicate
- duplicate has no explicit dependency on ReturnReview
- duplicate configuration/domain/deployment identity is already captured in `registry/resources.json`

User authorization:
Explicitly approved deletion after confirming it is a duplicate and that the canonical/original copy is preserved.

Planned action:
Delete only the non-canonical `app01-motionlab` service, then verify standalone MotionLab and ReturnReview API/web remain healthy. Misplaced Hub metadata is **not** part of this deletion.

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
Governance v1 validation passed in GitHub Actions and PR #1 was squash-merged to main as commit 71bc5ac4264eb2c13afb2c073043c59f7ac4d102.

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
