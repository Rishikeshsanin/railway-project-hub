# Naming Standard

## Application identity

Every app receives:
- immutable app number once registered
- stable snake_case slug
- human display name

Examples:
- App 01 / motionlab / MotionLab
- App 02 / return_review / ReturnReview

App numbers are not reused after retirement.

## Railway projects

Default project name: application display name.

Examples:
- MotionLab
- ReturnReview

Do not create one generic runtime project for unrelated apps.

## Services

Prefer:
- appname-web
- appname-api
- appname-worker
- appname-db

A single-service app may use the app name when unambiguous.

Avoid:
- backend
- server
- database
- test
- new
- final
- final2

## Variables

Prefer app-specific names when the variable could be confused across projects.

Examples:
- RETURNREVIEW_GEMINI_API_KEY
- RETURNREVIEW_DATABASE_URL

Never use naming as a substitute for real project-level isolation.

## Domains

Record every production domain in registry/resources.json.

Do not transfer/repoint production domains between apps without explicit review.

## Branches/environments

Use explicit names:
- main
- development
- staging
- production

Do not assume a generic DATABASE_URL or API_URL points to the intended environment. Verify ownership.
