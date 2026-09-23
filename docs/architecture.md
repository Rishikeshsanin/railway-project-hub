# Railway Project Hub Architecture

**Governance version: v1.0 — FROZEN**

## Principle

The Hub is a governance/control layer, not a shared runtime.

Canonical model:

~~~text
Railway account
│
├── Railway Project Hub
│   └── governance-only Railway project; no app runtime
│
├── ReturnReview Railway Project
│   └── ReturnReview resources
│
└── Future active App Railway Project
    └── that app's resources

Archived source
└── MotionLab
    └── GitHub source + restore snapshot; no active Railway runtime
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

A dedicated Railway project now exists for governance visibility in the Railway dashboard. It is named `Railway Project Hub` and must remain empty of application runtime resources.

Canonical governance still lives in this GitHub repository. The Railway Hub project is a governance-only container and must not host app services, databases, volumes, buckets, or shared application secrets.

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
├── Railway Project Hub → governance-only; 0 app services
├── ReturnReview        → isolated active app project
├── App 03              → isolated future app project
└── App NN              → isolated future app project

Archived
└── MotionLab            → source preserved; no active Railway project
~~~

New apps extend the registry; they do not redesign this structure.

## Current applications

App 01: MotionLab
- status: archived
- active Railway Project: none
- source/restore state: preserved

App 02: ReturnReview
- status: active
- canonical Railway Project: ReturnReview

Governance project:
- Railway Project Hub
- project ID: `917d84ff-5ef4-4d64-9629-b731ab79d67b`
- app runtime services: 0

The governance project reuses the former MotionLab project container after verified retirement. This lifecycle transition is recorded explicitly and is not a cross-app runtime dependency.

## Historical migration residue

An abandoned shared-runtime experiment temporarily created a duplicate MotionLab service and embedded Hub metadata inside ReturnReview.

Those resources were audited, safely removed, and remain permanently recorded in registry/resources.json with removed_verified status and in changes/CHANGELOG.md.

Historical residue is evidence for recovery/audit only and must never be treated as active architecture.
