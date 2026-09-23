# Railway Project Hub Rules

## 1. Purpose

The Railway Project Hub is the canonical governance and resource registry for Railway applications owned by this account.

It is not a shared application runtime.

## 2. Isolation model

Each application is an independent tenant and, by default, receives its own isolated Railway Project.

An application may access only:
- its registered Railway project
- its registered environments
- its registered services
- its own variables and secrets
- its own domains
- its own volumes/databases/storage
- explicitly approved shared infrastructure

Everything else is out of scope.

## 3. Safety priority

Isolation > Security > Recoverability > Maintainability > Convenience

## 4. Immutable Safety Invariants

The following rules are constitutional and must not be weakened for convenience:

1. Every production application has one canonical Railway Project.
2. Applications do not silently share runtime resources.
3. The Hub does not host application runtime services.
4. Credentials use minimum required scope.
5. Ownership is never inferred from naming alone.
6. Destructive operations require ownership, dependency, and recovery verification.
7. Existing data is preserved unless explicit destructive authorization is given.
8. Registry ownership is recorded only after verification against Railway.
9. Removed resources remain historically recorded as removed/verified.
10. Declared/live-state mismatches stop all writes until reconciled.

## 4A. Non-running registry markers

The governance-only Railway Project Hub may contain empty marker services solely to make registered applications visible on its canvas.

Markers are permitted only when they are explicitly registered as governance metadata and verified to have:
- no source
- no image
- no deployment
- no domain
- no custom variables/secrets
- no persistence
- no runtime dependency

A marker is never a canonical application service and must not appear in an application's `canonical_services` list.

## 5. Read-first gate

Before any write:
1. Read README.md.
2. Read AGENTS.md.
3. Verify the app in registry/apps.json.
4. Verify target resources in registry/resources.json.
5. Read the app record in apps/.
6. Read the app repository's README.md, AGENTS.md, and RAILWAY_HUB_RULES.md.
7. Inspect Railway read-only.
8. Establish exact target project, environment, service, and resource.
9. Review rollback.
10. Only then make the scoped change.

## 6. No cross-app assumptions

Never reuse, modify, connect, copy, or delete another application's:
- project
- service
- environment
- variable
- secret
- database
- volume
- storage
- domain
- networking
- GitHub connection
- deployment

Cross-app dependencies require explicit user authorization and Hub documentation.

## 7. New project hard gate

Documentation and registration come before infrastructure.

No new application Railway project may be created until:
- application identity is documented
- app README.md exists
- app AGENTS.md exists
- app RAILWAY_HUB_RULES.md exists
- Hub app number and slug are reserved
- repository ownership is verified
- expected project/environment/service names are documented
- secret ownership is documented by name only
- database/storage strategy is documented
- architecture review is complete

## 8. Production safety

Production is not a sandbox.

Before a production change:
- identify the current known-good deployment
- inspect health
- inspect dependencies
- understand rollback
- prefer preview/staging for major changes
- deploy the minimum scoped change
- verify health, logs, endpoint behavior, and main user flow

## 9. Never delete first

Use:
inspect -> document -> verify dependencies -> confirm replacement/backup -> disable when practical -> verify -> explicit destructive approval -> delete -> audit

## 10. Secrets

Secret values must remain in the owning app's secure Railway configuration or approved secret store.

The Hub may record:
- variable name
- owning app
- owning service
- purpose
- provider
- status

The Hub must never record the secret value.

## 11. Databases and persistent storage

Prefer application-specific databases/storage.

If a shared database is ever intentionally used:
- namespace isolation is mandatory
- credentials must be scoped
- cross-app access must be impossible by default
- ownership and dependency must be registered before use

## 12. Naming

Use deterministic names that include the application identity when ambiguity is possible.

Avoid names such as backend, server, database, test, new, final, or final2.

See docs/naming.md.

## 13. Source control

Every Railway service must be traceable:
GitHub repository -> branch -> Railway project -> environment -> service

Connecting a different repository to an existing production service requires explicit review.

## 14. Change history

Meaningful infrastructure changes must be recorded in changes/CHANGELOG.md with:
- date
- application
- resource
- change
- reason
- risk
- rollback
- result

## 15. Incident rule

If another app is unexpectedly affected:
- stop all modifications
- identify affected project/service
- record what changed
- record what has not changed
- restore only within authorized scope
- do not silently repair unrelated applications

Use templates/INCIDENT_TEMPLATE.md.

## 16. Supabase relationship

Supabase is not a dependency of this Hub.

Supabase Project Hub patterns may inform governance, but Railway uses Railway-native boundaries: projects, environments, services, variables, domains, deployments, networking, volumes, databases, and source connections.

## 17. Historical migration residue

An earlier shared-runtime experiment temporarily placed a duplicate MotionLab service and Hub metadata inside ReturnReview.

That experiment has been fully cleaned up. The removed resources remain recorded in registry/resources.json and changes/CHANGELOG.md as historical `removed_verified` entries.

Historical residue must never be treated as an active resource or reused as a shortcut for a future application.

## 18. Reconciliation Rule

No single artifact automatically overrides another when declared state and observed Railway infrastructure disagree.

A mismatch is a STOP condition:
- stop writes,
- inspect read-only,
- verify resource IDs and ownership,
- use repository, domain, deployment, and changelog history as evidence,
- reconcile the discrepancy,
- update the appropriate record only after verification,
- verify again before continuing.

The hierarchy defines information roles, not an automatic winner:
README → AGENTS/RULES → app registry → resource registry → app docs → live Railway → history/evidence → reconciled state.

## 19. Governance Freeze

Railway Project Hub Governance v1.0 is frozen.

Normal app development must use the existing model instead of redesigning it.

Constitutional/security changes must be deliberate, versioned, documented, CI-validated, and historically recorded. Historical cleanup records must not be rewritten.

## 20. Final rule

Protect every existing application as if it belongs to a different customer.
