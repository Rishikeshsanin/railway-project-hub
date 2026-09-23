# Railway Project Hub Agent Contract

This repository governs Railway infrastructure for multiple independent applications.

## Mandatory read order

Before any Railway write:
1. Read README.md.
2. Read RAILWAY_HUB_RULES.md.
3. Read registry/apps.json and registry/resources.json.
4. Identify the exact app number and slug.
5. Read apps/appNN-<slug>.md.
6. Read that application's own README.md, AGENTS.md, and RAILWAY_HUB_RULES.md.
7. Inspect the target Railway project/environment/service read-only.
8. Verify scope before changing anything.

If any required document is missing, stop before creating or changing Railway infrastructure.

## Scope rule

Treat every registered application as a separate customer.

Authorization to work on App 01 does not authorize work on App 02, App 03, or Hub-wide infrastructure.

## Destructive changes

Deleting projects, services, domains, databases, volumes, or persistent data; changing production networking; rotating critical secrets; or removing migration residue requires:
- dependency inspection
- rollback/recovery plan
- explicit user confirmation immediately before execution
- post-change verification
- changelog update

## Secrets

Never print, commit, log, screenshot, document, or copy secret values.

The Hub stores secret names, ownership, and purpose only.

## New applications

No new Railway application project may be created until:
- app README exists
- app AGENTS.md exists
- app RAILWAY_HUB_RULES.md exists
- Hub registry entry is prepared
- expected Railway resources are documented
- architecture/resource review is complete

## Change discipline

Use:
read -> identify -> verify -> plan -> change -> test -> verify -> document

When uncertain:
- do nothing destructive
- inspect read-only
- ask the user if ambiguity remains
