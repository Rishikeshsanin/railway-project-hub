# Application Lifecycle

## Planned

An app may be listed as planned before Railway infrastructure exists.

Requirements:
- repo exists
- README exists
- AGENTS.md exists
- RAILWAY_HUB_RULES.md exists
- app number/slug prepared
- proposed resources documented

## Provisioning

Only after documentation review:
- create isolated Railway Project
- create registered services
- configure app-only secrets
- configure health/domain
- deploy and verify

## Active

An active app must have:
- canonical Railway project
- registered services/resources
- app-side safety files
- healthy known-good deployment
- current Hub records

## Changing

Meaningful infrastructure changes require:
- read-first gate
- exact scope
- rollback
- verification
- changelog update

## Deprecated

Before deprecation:
- document replacement
- stop new dependencies
- preserve recovery/data
- communicate domain/API changes

## Retired

Retirement is not deletion-by-assumption.

Before destructive cleanup:
- inspect dependencies
- backup/export if needed
- disable where practical
- verify no consumers
- explicit destructive approval
- delete scoped resources
- final audit
- keep historical registry/changelog record

App numbers are never reused.
