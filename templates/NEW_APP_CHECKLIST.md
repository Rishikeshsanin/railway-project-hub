# New Railway Application Checklist

Use this checklist before creating any new Railway application project.

## Phase 1 — Identity
- [ ] Application name chosen
- [ ] Snake_case Hub slug chosen
- [ ] Next app number verified in registry/apps.json
- [ ] GitHub repository exists
- [ ] Repository ownership verified
- [ ] Purpose documented

## Phase 2 — App-side safety contract
The application repository must already contain:
- [ ] README.md
- [ ] AGENTS.md
- [ ] RAILWAY_HUB_RULES.md

The files must explicitly identify:
- app number and slug
- repository
- intended Railway project
- allowed scope
- forbidden cross-app scope
- secret policy
- destructive-change policy

## Phase 3 — Hub registration
Before Railway creation:
- [ ] apps/appNN-<slug>.md prepared
- [ ] registry/apps.json entry prepared
- [ ] expected resources prepared for registry/resources.json
- [ ] expected APIs prepared for registry/api-registry.json
- [ ] no secret values stored

## Phase 4 — Architecture review
- [ ] Separate Railway Project is the default
- [ ] Service names are unambiguous
- [ ] Environments are documented
- [ ] Database/storage strategy documented
- [ ] Cross-app dependencies are none by default
- [ ] Shared resources, if any, have explicit approval
- [ ] Health checks documented
- [ ] Rollback path documented
- [ ] Production is not the first test environment for a major change

## Phase 5 — Creation
Only after Phases 1–4:
- [ ] Create isolated Railway Project
- [ ] Create only registered services
- [ ] Set app-only variables/secrets
- [ ] Connect the verified GitHub repository/branch
- [ ] Configure health checks
- [ ] Configure domains
- [ ] Deploy
- [ ] Verify logs and health
- [ ] Test main user flow

## Phase 6 — Closeout
- [ ] Capture actual Railway project ID
- [ ] Capture environment ID
- [ ] Capture service IDs
- [ ] Update registry/apps.json
- [ ] Update registry/resources.json
- [ ] Update API registry if relevant
- [ ] Update app record
- [ ] Add changelog entry
- [ ] Verify no unrelated app changed

If any mandatory phase is incomplete, stop before creating more infrastructure.
