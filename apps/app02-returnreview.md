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
- RETURNREVIEW_CV_IMAGE_SIZE
- RETURNREVIEW_CATEGORY_PROBABILITY_THRESHOLD
- RETURNREVIEW_CATEGORY_MODEL_PATH
- RETURNREVIEW_DATABASE_URL
- RETURNREVIEW_GEMINI_API_KEY
- RETURNREVIEW_GEMINI_FALLBACK_MODEL
- RETURNREVIEW_GEMINI_MODEL
- RETURNREVIEW_DATABASE_SCHEMA
- RETURNREVIEW_DEMO_MODE
- RETURNREVIEW_ENV
- RETURNREVIEW_LLM_ENABLED
- RETURNREVIEW_LLM_EVAL_MODEL
- RETURNREVIEW_MAX_UPLOAD_MB
- RETURNREVIEW_RUN_LLM_EVAL_ON_START
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

Production persistence is fully verified. `returnreview-api` connects to the canonical Railway Postgres through a Railway service-reference URL; startup reports `database_backend=postgresql` and `durable_persistence=True`, and both `/health` and `/readiness` return HTTP 200. Case `PERSISTENCE-PROOF-01`, its two uploaded evidence images, and its audit timeline remained available after redeploying only `returnreview-api`.

The accidental Postgres service previously created inside the governance-only Railway Project Hub has been removed and verified. The Hub now contains only the non-running `app02-returnreview` marker for ReturnReview.

## API registry
Gemini is intended for the ReturnReview API.

The credential name is `RETURNREVIEW_GEMINI_API_KEY`; it is present only on `returnreview-api` and its value remains private/redacted. Production primary model is `gemini-3.8-flash`; transient-capacity fallback is `gemini-3.5-flash`. The controlled six-case evaluation completed using the explicitly recorded evaluation model `gemini-3.5-flash`, and `RETURNREVIEW_RUN_LLM_EVAL_ON_START` was restored to false after the run.

Never store secret values in this Hub.

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


## Lightweight CV production candidate — declared 2026-09-25

The existing `returnreview-api` remains the intended deployment target. No new Railway service is declared.

Planned backend-only CV settings:
- `RETURNREVIEW_CV_IMAGE_SIZE`
- `RETURNREVIEW_CATEGORY_MODEL_PATH`
- `RETURNREVIEW_CATEGORY_PROBABILITY_THRESHOLD`

The candidate architecture uses multiclass YOLO segmentation plus a MobileNetV3-Small category verifier so production does not require OpenCLIP. Runtime activation is not yet approved; the existing production service must remain unchanged until the candidate passes the recorded 1 GB memory gate and explicit production approval is obtained.
