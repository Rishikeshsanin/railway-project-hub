# Railway Project Hub Architecture

**Governance version: v1.0 — FROZEN**

## Principle

The Hub is a governance/control layer, not a shared runtime.

Canonical model:

~~~text
Railway account
│
├── Governance: Rishikeshsanin/railway-project-hub
│
├── MotionLab Railway Project
│   └── MotionLab resources
│
├── ReturnReview Railway Project
│   └── ReturnReview resources
│
└── Future App Railway Project
    └── that app's resources
~~~

## Isolation boundary

The default isolation boundary is the Railway Project.

Each application should be independently:
- deployable
- configurable
- observable
- recoverable
- removable

without requiring changes to another application.

## Hub implementation

The canonical Hub is this GitHub repository.

A dedicated Railway runtime project is not required for governance. If one is ever created, it must remain governance-only and must not become a container for unrelated application runtimes.

## Registry model

registry/apps.json owns application identity.

registry/resources.json owns Railway resource identity.

registry/api-registry.json owns external API/credential-name relationships.

Human-readable app records live in apps/.

## Governance / Reconciliation Model

~~~text
README.md
   ↓ constitutional governance

AGENTS.md + RAILWAY_HUB_RULES.md
   ↓ operational rules

registry/apps.json
   ↓ declared app identity / ownership

registry/resources.json
   ↓ declared Railway resource ownership / lifecycle

apps/appNN-<slug>.md
   ↓ app-specific operational context

Live Railway state
   ↓ observed infrastructure

Git history / deployment history / changelog
   ↓ reconciliation evidence

RECONCILED STATE
~~~

No artifact automatically wins a disagreement. A mismatch stops writes until read-only investigation establishes and records the reconciled state.

## Shared infrastructure

Shared infrastructure is exceptional, not default.

Before a resource becomes shared, document:
- owner
- consumers
- access boundaries
- failure boundary
- secret model
- data boundary
- rollback
- removal plan

## Frozen v1.0 architecture

The v1.0 architecture is intentionally frozen:

~~~text
Railway governance
└── railway-project-hub
    ├── README / rules / agent contract
    ├── app + resource registries
    ├── per-app governance records
    ├── CI validation
    └── immutable history

Railway runtime
├── MotionLab       → isolated project
├── ReturnReview    → isolated project
├── App 03          → isolated project
└── App NN          → isolated project
~~~

New apps extend the registry; they do not redesign this structure.

## Current applications

App 01: MotionLab
- canonical Railway Project: MotionLab

App 02: ReturnReview
- canonical Railway Project: ReturnReview

## Historical migration residue

An abandoned shared-runtime experiment temporarily created a duplicate MotionLab service and embedded Hub metadata inside ReturnReview.

Those resources were audited, safely removed, and remain permanently recorded in registry/resources.json with removed_verified status and in changes/CHANGELOG.md.

Historical residue is evidence for recovery/audit only and must never be treated as active architecture.
