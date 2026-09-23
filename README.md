# Railway Project Hub

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

Three old project-level Hub metadata entries remain inside ReturnReview. They are **not canonical** and must not be deleted casually. Their cleanup requires a separate review and explicit approval.

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
