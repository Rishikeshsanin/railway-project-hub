# App 02 — ReturnReview

## Identity
- App number: 02
- Slug: return_review
- Repository: https://github.com/Rishikeshsanin/ReturnReview
- Canonical Railway project: ReturnReview
- Railway project ID: 3b5a435b-a0ca-43c0-85c0-9783073a8cd4
- Environment: production
- Environment ID: c587f082-f4c9-4b2a-96e8-946f9929d7ce
- Status: active

## Canonical services

### returnreview-api
- Service ID: 15b5ade1-912a-44bf-ae07-e0d21f2278e1
- Source: Rishikeshsanin/ReturnReview
- Branch: main
- Domain: https://returnreview-api-production.up.railway.app
- Health path: /health
- Outbound IPv6: enabled (ReturnReview API only; verified 2026-09-23)

Registered custom variable names:
- RETURNREVIEW_ALLOWED_ORIGINS
- RETURNREVIEW_CV_MODEL_VERSION
- RETURNREVIEW_DATABASE_URL
- RETURNREVIEW_GEMINI_MODEL
- RETURNREVIEW_DATABASE_SCHEMA
- RETURNREVIEW_DEMO_MODE
- RETURNREVIEW_ENV
- RETURNREVIEW_LLM_ENABLED
- RETURNREVIEW_MAX_UPLOAD_MB
- RETURNREVIEW_STORAGE_DIR

### returnreview-web
- Service ID: 445fd60b-8e72-49fe-86fb-bf9eeb276546
- Source: Rishikeshsanin/ReturnReview
- Branch: main
- Root directory: /frontend
- Domain: https://returnreview-web-production.up.railway.app
- Health path: /

Registered custom variable names:
- NEXT_PUBLIC_API_BASE_URL

## Persistence
Canonical Railway Postgres is now provisioned inside the isolated ReturnReview project.

- Database service: `Postgres`
- Service ID: `02cc5aaf-b427-48d8-bfdd-488a1d714daf`
- Private network endpoint: `postgres`
- Public domain: none
- Volume: `postgres-volume`
- Volume ID: `6114b26f-88d5-40d9-ad53-b1de917bc703`
- Mount path: `/var/lib/postgresql/data`

Production activation is now verified. `returnreview-api` connects to the canonical Railway Postgres through a Railway service-reference URL; startup reports `database_backend=postgresql` and `durable_persistence=True`, and both `/health` and `/readiness` return HTTP 200. Final proof still requires a real case + evidence to survive an API redeploy.

An accidental Postgres service was separately created inside the governance-only Railway Project Hub. It is non-canonical, has no application dependency, and is explicitly approved for removal.

## API registry
Gemini is intended for the ReturnReview API.

The credential name is RETURNREVIEW_GEMINI_API_KEY, but the last verified Railway inventory did not show that variable present.

Never store its value in this Hub.

## Isolation boundary
ReturnReview may modify only the ReturnReview Railway project and its registered canonical resources.

MotionLab and future apps are out of scope.

## Required app-side documents
The ReturnReview repository contains:
- README.md
- AGENTS.md
- RAILWAY_HUB_RULES.md
- SUPABASE_HUB_RULES.md

## Migration cleanup state
The non-canonical app01-motionlab duplicate service was safely removed on 2026-09-23 after audit and explicit approval.

ReturnReview canonical runtime resources are:
- returnreview-api
- returnreview-web
- Postgres
- postgres-volume

The three earlier project-level Hub metadata flags were safely removed on 2026-09-23 after confirming that canonical governance lives in the independent Railway Project Hub repository and ReturnReview runtime does not depend on those flags.

ReturnReview is now cleanly isolated with only its canonical runtime services and no embedded Hub metadata.
