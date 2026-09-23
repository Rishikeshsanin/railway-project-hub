# Railway Project Hub Architecture

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

## Current applications

App 01: MotionLab
- canonical Railway Project: MotionLab

App 02: ReturnReview
- canonical Railway Project: ReturnReview

## Current non-canonical residue

The ReturnReview project contains a duplicate MotionLab service and older Hub metadata from an abandoned architecture.

They are tracked in registry/resources.json as migration residue.

They are not evidence that shared runtime is an accepted architecture.
