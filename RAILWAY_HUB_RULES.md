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

## 4. Read-first gate

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

## 5. No cross-app assumptions

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

## 6. New project hard gate

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

## 7. Production safety

Production is not a sandbox.

Before a production change:
- identify the current known-good deployment
- inspect health
- inspect dependencies
- understand rollback
- prefer preview/staging for major changes
- deploy the minimum scoped change
- verify health, logs, endpoint behavior, and main user flow

## 8. Never delete first

Use:
inspect -> document -> verify dependencies -> confirm replacement/backup -> disable when practical -> verify -> explicit destructive approval -> delete -> audit

## 9. Secrets

Secret values must remain in the owning app's secure Railway configuration or approved secret store.

The Hub may record:
- variable name
- owning app
- owning service
- purpose
- provider
- status

The Hub must never record the secret value.

## 10. Databases and persistent storage

Prefer application-specific databases/storage.

If a shared database is ever intentionally used:
- namespace isolation is mandatory
- credentials must be scoped
- cross-app access must be impossible by default
- ownership and dependency must be registered before use

## 11. Naming

Use deterministic names that include the application identity when ambiguity is possible.

Avoid names such as backend, server, database, test, new, final, or final2.

See docs/naming.md.

## 12. Source control

Every Railway service must be traceable:
GitHub repository -> branch -> Railway project -> environment -> service

Connecting a different repository to an existing production service requires explicit review.

## 13. Change history

Meaningful infrastructure changes must be recorded in changes/CHANGELOG.md with:
- date
- application
- resource
- change
- reason
- risk
- rollback
- result

## 14. Incident rule

If another app is unexpectedly affected:
- stop all modifications
- identify affected project/service
- record what changed
- record what has not changed
- restore only within authorized scope
- do not silently repair unrelated applications

Use templates/INCIDENT_TEMPLATE.md.

## 15. Supabase relationship

Supabase is not a dependency of this Hub.

Supabase Project Hub patterns may inform governance, but Railway uses Railway-native boundaries: projects, environments, services, variables, domains, deployments, networking, volumes, databases, and source connections.

## 16. Historical migration residue

An earlier shared-runtime experiment temporarily placed a duplicate MotionLab service and Hub metadata inside ReturnReview.

That experiment has been fully cleaned up. The removed resources remain recorded in registry/resources.json and changes/CHANGELOG.md as historical `removed_verified` entries.

Historical residue must never be treated as an active resource or reused as a shortcut for a future application.

## 17. Final rule

Protect every existing application as if it belongs to a different customer.
