# App 01 — MotionLab

## Identity
- App number: 01
- Slug: motionlab
- Repository: https://github.com/Rishikeshsanin/animation-website
- Canonical Railway project: MotionLab
- Railway project ID: 917d84ff-5ef4-4d64-9629-b731ab79d67b
- Environment: production
- Environment ID: bca2ecae-b4dd-4047-87da-428b96be0270
- Status: active

## Canonical service
- Service: motionlab
- Service ID: 048331c3-43df-4bbb-a1a5-1cea4adcfc5d
- Source: Rishikeshsanin/animation-website
- Branch: main
- Domain: https://motionlab-production-2310.up.railway.app

## Architecture
MotionLab is frontend-only.

It currently requires:
- no Railway database
- no Railway volume
- no Supabase project
- no cross-app runtime dependency
- no custom application secrets

## Isolation boundary
MotionLab may modify only its own Railway project and registered resources.

ReturnReview and all future apps are out of scope during MotionLab work.

## Required app-side documents
The MotionLab repository contains:
- README.md
- AGENTS.md
- RAILWAY_HUB_RULES.md

These must be read before Railway writes.

## Known duplicate
A duplicate service named app01-motionlab exists inside the ReturnReview Railway project from an earlier experiment.

It is not canonical.

Do not delete or repurpose it until the cleanup procedure in docs/recovery.md has been approved and completed.

## Recovery source
The standalone MotionLab Railway project is the canonical deployment and must remain healthy before any duplicate cleanup.
