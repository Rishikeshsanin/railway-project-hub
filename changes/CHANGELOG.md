# Railway Project Hub Changelog

## 2026-09-24 — ReturnReview Railway Postgres activated

Application: ReturnReview (App 02)

Change:
- configured `returnreview-api` to use the canonical ReturnReview Railway Postgres through service-reference variables
- corrected the SQLAlchemy driver form to `postgresql+psycopg` for the installed Psycopg 3 driver
- verified production deployment `58933dd2-3255-46ae-960c-33a738690b75` succeeded
- verified startup reports `database_backend=postgresql` and `durable_persistence=True`
- verified `/health` and `/readiness` return HTTP 200
- ReturnReview web remained healthy and unchanged

Remaining persistence proof:
A real case plus evidence images must survive an API redeploy before the persistence checklist is fully complete.

Accidental Hub Postgres cleanup:
- only service `0e2a45db-b528-462b-b85b-ee56f9d960de` and volume `49d2eca8-6585-4ca5-ad6f-7f245eca5f78` are staged for removal
- Railway requires dashboard 2FA to commit that destructive change, so final removal is pending one manual confirmation
- no other resource is staged for deletion

## 2026-09-24 — ReturnReview Railway Postgres reconciled before cleanup

Application: ReturnReview (App 02) / Hub governance

Observed and registered:
- canonical ReturnReview Postgres service `02cc5aaf-b427-48d8-bfdd-488a1d714daf` exists inside the isolated ReturnReview Railway project
- canonical volume `6114b26f-88d5-40d9-ad53-b1de917bc703` is attached only to that database
- database has no public domain and uses Railway private networking
- ReturnReview API/web remain healthy and unchanged

Accidental Hub resource identified:
- governance-only Railway Project Hub service `Postgres`
- service ID `0e2a45db-b528-462b-b85b-ee56f9d960de`
- attached volume ID `49d2eca8-6585-4ca5-ad6f-7f245eca5f78`
- no public domain
- no ReturnReview API reference
- no marker-service reference
- no intentional application data

User authorization:
Explicitly approved deletion of only the accidental Hub Postgres and instructed that nothing else be deleted.

Plan:
Delete only the accidental Hub Postgres service and its attached volume, verify the Hub returns to marker-only state, then connect ReturnReview API only to the canonical ReturnReview Postgres.

## 2026-09-23 — ReturnReview API outbound IPv6 enabled

Application: ReturnReview (App 02)

Change:
- enabled outbound IPv6 only on canonical service `returnreview-api`
- verified API redeployment succeeded
- verified `returnreview-web` remained healthy and unchanged
- reconciled the App 02 resource registry with current non-secret variable names
- recorded `RETURNREVIEW_DATABASE_SCHEMA` and `RETURNREVIEW_GEMINI_MODEL`
- confirmed `RETURNREVIEW_GEMINI_API_KEY` is not currently registered/present

Reason:
Allow ReturnReview API to reach the IPv6 Supabase direct Postgres endpoint while preserving project/service isolation.

Current persistence state:
Network connectivity is prepared, but the live API remains on SQLite until the dedicated `return_review_backend` credential and PostgreSQL URL are configured privately.

Result:
ReturnReview API/web healthy; no cross-app resource changed.

## 2026-09-23 — ReturnReview marker added to Railway Project Hub

Application: ReturnReview / Hub governance

Created:
- empty marker service: `app02-returnreview`
- marker service ID: `4dabbfb9-e1be-4247-8287-abc78f32ad71`

Verified marker constraints:
- no source attached
- no deployment
- no domain
- no custom variables/secrets
- no volume
- no cron
- no application runtime role

Real ReturnReview runtime remains isolated in project `3b5a435b-a0ca-43c0-85c0-9783073a8cd4` with `returnreview-api` and `returnreview-web`, both verified healthy.

Result:
ReturnReview is now visually represented inside Railway Project Hub without duplicating or moving its runtime.

## 2026-09-23 — Non-running Hub marker policy added

Application: Hub governance / ReturnReview

Change:
- clarified that the Hub may contain explicitly registered empty marker services for visual app cataloging
- marker services are forbidden from having sources, deployments, domains, variables/secrets, persistence, or runtime dependencies
- planned `app02-returnreview` marker registered before creation

Reason:
Allow ReturnReview to appear visually inside the Railway Project Hub without duplicating or moving its real runtime.

Governance impact:
This does not weaken the invariant that the Hub must not host application runtime services. Governance remains v1.0 with a clarification-only implementation update.

## 2026-09-23 — MotionLab archived; Railway Project Hub provisioned

Applications: MotionLab / Hub governance / ReturnReview verification

Completed actions:
- verified MotionLab backup and permanent source archive
- removed only the `motionlab` Railway service after explicit authorization
- verified the former MotionLab project container became empty
- renamed the empty project container to `Railway Project Hub`
- preserved the same project/environment IDs while changing their lifecycle role
- kept the Railway Project Hub governance-only with 0 app services, 0 buckets, and 0 project feature flags
- verified ReturnReview API and web services remained healthy

Current state:
- App 01 MotionLab: archived; no active Railway project
- App 02 ReturnReview: active; isolated Railway project
- Railway Project Hub: governance-only project
- App 03: next application number

Important identity note:
Project ID `917d84ff-5ef4-4d64-9629-b731ab79d67b` historically belonged to MotionLab and now belongs to the governance-only Railway Project Hub role. Historical records remain intact; current ownership must be determined by lifecycle state and live verification.

Governance impact:
No immutable invariant was weakened and governance version remains v1.0. This provisions an optional governance-only Railway project already permitted by the frozen architecture; it does not introduce shared application runtime.

## 2026-09-23 — MotionLab pre-retirement backup prepared

Application: MotionLab

Change:
- created permanent source archive branch at commit `85e64bd1dd67148893290c5862a1187567b7e54e`
- captured non-secret Railway project/service/environment/domain/deployment metadata
- documented a restore procedure
- verified no custom app secrets, database, volume, bucket, cron, custom domain, or unique Railway-persistent data

Reason:
Preserve MotionLab before retiring its Railway project to free account capacity for a governance-only Railway Project Hub project.

Result:
Backup prepared. MotionLab Railway project remains active until the separately authorized retirement step.

## 2026-09-23 — v1.0 final consistency clarification

Application: Hub governance

Change:
- replaced ambiguous "machine-readable source of truth" wording with "canonical declared application registry"
- explicitly tied registry declarations to the reconciliation STOP rule
- aligned the app template and agent contract with the already-required app governance CI gate

Reason:
Remove ambiguity without changing the frozen v1.0 architecture or immutable invariants.

Result:
Hub validation passed. This was a clarification-only patch; the frozen v1.0 architecture and immutable invariants were unchanged.

## 2026-09-23 — Railway Project Hub Governance v1.0 frozen

Application: Hub governance

Change:
- added Immutable Safety Invariants as constitutional rules
- added explicit declared-state/live-Railway reconciliation hierarchy
- defined registry/live mismatch as a STOP condition
- added governance version metadata and freeze status
- updated architecture to remove stale "current residue" wording
- added versioning policy
- strengthened Hub validator to enforce v1.0 invariants and frozen status

Reason:
Finalize the governance architecture so future applications use a stable, scalable model rather than redesigning the Hub during normal development.

Result:
Hub validation passed and the v1.0 freeze was squash-merged to main as commit `d2a6284e1ad3ed2d52bd54b92f147c388a8cd26c`. Historical MotionLab/ReturnReview cleanup records remain unchanged.

## 2026-09-23 — Legacy ReturnReview Hub metadata cleanup completed

Application: ReturnReview / Hub governance

Removed project-scoped flags:
- `hub.apps`
- `hub.architecture_version`
- `hub.read_me_first`

Pre-removal verification:
- canonical Railway governance is stored in `Rishikeshsanin/railway-project-hub`
- ReturnReview runtime consists only of `returnreview-api` and `returnreview-web`
- the old flags were created by the abandoned shared-runtime experiment
- `hub.apps` contained stale references to the already-removed duplicate MotionLab service
- no application service relied on these feature flags for runtime configuration

Post-removal verification:
- ReturnReview project has zero project-scoped Hub feature flags
- `returnreview-api` remains healthy
- `returnreview-web` remains healthy
- standalone MotionLab remains healthy
- ReturnReview has no pending changes

Result:
The abandoned Railway shared-runtime/embedded-Hub experiment is fully cleaned up. Canonical governance remains independently in the Railway Project Hub repository.

## 2026-09-23 — MotionLab duplicate cleanup completed

Applications: MotionLab, ReturnReview

Completed action:
- deleted only the non-canonical `app01-motionlab` service
- deleted service ID: `25cc6232-ed7e-42fd-94e8-d180e641607f`

Post-deletion verification:
- standalone MotionLab service `motionlab` remains present and healthy
- ReturnReview `returnreview-api` remains present and healthy
- ReturnReview `returnreview-web` remains present and healthy
- ReturnReview now contains only its two canonical services
- no pending Railway changes remain

Data-loss assessment:
- no custom secret/variable values were stored by the deleted duplicate
- no volume, database, bucket, custom domain, cron, or persistent data was attached
- canonical source remains in `Rishikeshsanin/animation-website`
- historical duplicate identity/configuration is retained in `registry/resources.json`

Not changed:
- canonical standalone MotionLab project
- ReturnReview API/web
- three old project-level Hub metadata entries inside ReturnReview

Result:
Duplicate runtime cleanup completed safely. The remaining old Hub metadata requires a separate review and authorization before removal.

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
