# Secrets and Environment Variables

## Core rule

This repository never stores secret values.

It may store:
- variable name
- owning app
- owning service
- provider
- purpose
- expected status

## App isolation

A secret belonging to App A must not be copied into App B for convenience.

Project-level/account-level secrets must not be given to ordinary applications unless explicitly designed and approved for that scope.

## Frontend safety

Anything intentionally exposed to browsers is not a secret.

Review public-prefixed frontend variables carefully.

Never place server credentials in client-side variables.

## Debugging

Never paste secret values into:
- GitHub
- README/docs
- issues/PRs
- logs
- screenshots
- URLs
- ChatGPT messages

Redact values when investigating.

## Rotation

Before rotating a production credential:
- identify every consumer
- confirm app ownership
- plan rollback
- update the minimum scoped services
- verify
- never rotate an account-wide/shared credential for one app without impact review

## Registry

Use registry/api-registry.json for external API credential ownership.

Use registry/resources.json for service custom variable names where useful.

Store names only.
