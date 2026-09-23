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

Registered custom variable names:
- RETURNREVIEW_ALLOWED_ORIGINS
- RETURNREVIEW_CV_MODEL_VERSION
- RETURNREVIEW_DATABASE_URL
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
No active Railway volume is registered.

Hosted SQLite/uploads are currently ephemeral and must not be described as durable persistence.

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

ReturnReview now contains only its canonical runtime services:
- returnreview-api
- returnreview-web

Three earlier Hub metadata signals still remain inside the ReturnReview project. They are not ReturnReview application architecture and must not be touched during ordinary ReturnReview development. Their cleanup is governed separately by the Hub recovery process.
