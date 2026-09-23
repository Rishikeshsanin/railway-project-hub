# Railway Project Hub

> **Railway Project Hub Governance v1.0 — FROZEN**
>
> **READ THIS BEFORE ANY RAILWAY WRITE.**

This repository is the canonical governance, registry, safety, and recovery source of truth for Railway applications owned by this account.

The Railway Project Hub is **not** a shared application runtime. Every real application must remain independently deployable and, by default, must have its **own isolated Railway Project**.

## Golden rule

> **Treat every registered application as if it belongs to a different customer.**

Working on one app does **not** authorize changes to another app, even when both are owned by the same person and exist in the same Railway account.

## Safety priority

~~~text
Isolation
  >
Security
  >
Recoverability
  >
Maintainability
  >
Convenience
~~~

## Immutable Safety Invariants

The following rules are constitutional. They must never be weakened for convenience:

1. Every production application has one canonical Railway Project.
2. An application must never silently share another application's runtime resources.
3. The Hub itself must not host application runtime services.
4. Application credentials are scoped to the minimum required application/resource.
5. No agent may infer ownership from naming alone; ownership must be verified from IDs, registry records, app documentation, and live Railway state.
6. No destructive operation may be performed without verifying ownership, dependencies, and rollback/recovery options.
7. Existing application data must be preserved unless explicit destructive authorization is given.
8. Registry state must never claim a resource belongs to an application until the Railway resource has been verified.
9. Removed resources remain historically recorded with a removed/verified status.
10. When documentation and live Railway state disagree, stop all writes and reconcile the discrepancy before making changes.

These invariants outrank convenience and normal application-development requests.

## Declared State vs Live Railway — Reconciliation Rule

> **No single artifact automatically overrides another when declared state and observed infrastructure disagree. A mismatch creates a STOP condition requiring read-only investigation and reconciliation.**

The information model is:

~~~text
README.md
   ↓ governance / constitutional policy

AGENTS.md + RAILWAY_HUB_RULES.md
   ↓ operational behavior

registry/apps.json
   ↓ declared application identity / ownership

registry/resources.json
   ↓ declared resource ownership / lifecycle

apps/appNN-<slug>.md
   ↓ application-specific operational context

Live Railway state
   ↓ observed infrastructure reality

Git history / deployment history / changelog
   ↓ evidence for reconciliation

RECONCILED STATE
~~~

This is a hierarchy of **information roles**, not an automatic winner order.

If any mismatch is detected:

~~~text
STOP WRITES
   ↓
INSPECT READ-ONLY
   ↓
VERIFY PROJECT / ENVIRONMENT / SERVICE IDs
   ↓
VERIFY REPOSITORY / DOMAIN / DEPLOYMENT HISTORY
   ↓
DETERMINE CORRECT STATE
   ↓
RECONCILE REGISTRY / DOCUMENTATION
   ↓
VERIFY AGAIN
   ↓
ONLY THEN CONTINUE
~~~

Neither stale documentation nor live infrastructure is allowed to overwrite the other silently.

## Mandatory read-first gate

Before creating, modifying, deploying, deleting, reconnecting, renaming, or reconfiguring any Railway resource:

~~~text
READ THIS README
      ↓
READ AGENTS.md
      ↓
READ RAILWAY_HUB_RULES.md
      ↓
IDENTIFY THE EXACT APPLICATION
      ↓
VERIFY registry/apps.json
      ↓
READ apps/appNN-<slug>.md
      ↓
READ THAT APP'S OWN README + AGENTS.md + RAILWAY_HUB_RULES.md
      ↓
INSPECT RAILWAY READ-ONLY
      ↓
VERIFY PROJECT / ENVIRONMENT / SERVICE / RESOURCE
      ↓
PLAN + ROLLBACK
      ↓
ONLY THEN WRITE
      ↓
TEST + VERIFY + UPDATE CHANGELOG
~~~

If any required documentation is missing, **do not create the Railway project/resource**.

If scope is ambiguous, **stop and ask the user**.

## Canonical architecture

~~~text
Railway account
│
├── Railway Project Hub
│   └── governance / registry / safety documentation only
│
├── MotionLab
│   └── isolated Railway project
│
├── ReturnReview
│   └── isolated Railway project
│
└── Future applications
    └── one isolated Railway project each by default
~~~

The Hub must never become a dumping ground for unrelated application services, data, databases, secrets, or runtime code.

## Current registered applications

| App | Slug | Repository | Canonical Railway Project | Status |
|---|---|---|---|---|
| App 01 | motionlab | Rishikeshsanin/animation-website | MotionLab | active |
| App 02 | return_review | Rishikeshsanin/ReturnReview | ReturnReview | active |

The machine-readable source of truth is registry/apps.json.

## Migration cleanup status

An earlier Hub experiment created an extra app01-motionlab service inside the ReturnReview Railway project plus project-level Hub metadata there.

The duplicate app01-motionlab service was audited, documented, explicitly approved for deletion, removed, and post-verified on 2026-09-23. Its historical identity remains in registry/resources.json with status removed_verified.

The three old project-level Hub metadata entries inside ReturnReview were also reviewed and removed on 2026-09-23 after confirming that canonical governance lives in this repository and the application runtime does not depend on those flags.

The abandoned shared-runtime experiment is now fully cleaned up. Historical identities remain preserved in registry/resources.json and changes/CHANGELOG.md.

See docs/recovery.md and changes/CHANGELOG.md.

## New application hard gate

For every future app:

~~~text
Hub rules
   ↓
App README
   ↓
App AGENTS.md
   ↓
App RAILWAY_HUB_RULES.md
   ↓
Hub registry entry
   ↓
Architecture/resource review
   ↓
Create isolated Railway Project
   ↓
Create services
   ↓
Configure app-only secrets
   ↓
Deploy
   ↓
Verify
   ↓
Update registry + changelog
~~~

No documentation = no Railway project creation.

## What one app may never do to another

Without explicit cross-app authorization and Hub documentation, an app/operator/agent must never:

- delete, rename, redeploy, reconnect, or reconfigure another app's Railway project
- modify another app's services, environments, variables, secrets, domains, volumes, databases, networking, or GitHub source
- copy credentials between apps
- point one app at another app's database or storage
- create cross-app dependencies
- change project-wide or account-wide settings for convenience
- assume an apparently unused resource is safe to delete

## Secrets

Never commit or expose:

- API keys
- database passwords
- access tokens
- service-role keys
- Railway tokens
- OAuth secrets
- private user data

The Hub records **secret names and ownership only**, never secret values.

## Repository map

~~~text
railway-project-hub/
├── README.md
├── AGENTS.md
├── RAILWAY_HUB_RULES.md
├── registry/
│   ├── apps.json
│   ├── resources.json
│   └── api-registry.json
├── apps/
│   ├── app01-motionlab.md
│   ├── app02-returnreview.md
│   └── TEMPLATE.md
├── changes/
│   └── CHANGELOG.md
├── templates/
│   ├── NEW_APP_CHECKLIST.md
│   ├── DEPLOYMENT_CHECKLIST.md
│   ├── RESOURCE_REGISTRATION.md
│   └── INCIDENT_TEMPLATE.md
└── docs/
    ├── architecture.md
    ├── naming.md
    ├── recovery.md
    ├── secrets.md
    └── lifecycle.md
~~~

## Governance Freeze and Versioning

**Current governance version: v1.0 — frozen.**

The architecture and immutable invariants are not redesigned during normal application development.

Future applications (App 03, App 04, and beyond) must use this governance model as-is.

A governance change is allowed only when there is a genuine security, safety, recoverability, or platform-model reason. Any such change must:
- be deliberate and documented,
- preserve historical records,
- update the governance version,
- pass Hub CI,
- and be reviewed before becoming canonical.

Small clarifications that do not weaken invariants may become v1.0.x documentation patches. Material policy changes require v1.1 or v2.0.

## Relationship to Supabase

The Supabase Project Hub is a **reference model for governance philosophy only**.

This Railway Hub is independent. It does not require Supabase to function and uses Railway-native isolation concepts: projects, environments, services, variables, domains, volumes, databases, networking, deployments, and source connections.

## Default behavior when uncertain

~~~text
DO NOTHING DESTRUCTIVE.
INSPECT READ-ONLY.
ASK THE USER IF STILL UNCERTAIN.
~~~

---

**Canonical repository:** Rishikeshsanin/railway-project-hub
