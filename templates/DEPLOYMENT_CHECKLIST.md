# Railway Deployment Checklist

## Before deployment
- [ ] Read Hub README, AGENTS.md, and RAILWAY_HUB_RULES.md
- [ ] Identify exact app
- [ ] Verify registry ownership
- [ ] Read app-side README, AGENTS.md, and RAILWAY_HUB_RULES.md
- [ ] Confirm repository and branch
- [ ] Confirm Railway project
- [ ] Confirm environment
- [ ] Confirm target service
- [ ] Confirm build/root/Dockerfile configuration
- [ ] Confirm variable names and ownership
- [ ] Confirm no secret values will be exposed
- [ ] Inspect current deployment health
- [ ] Identify previous known-good deployment
- [ ] Review rollback
- [ ] Review database migration impact separately

## Deployment
- [ ] Prefer preview/staging for major changes
- [ ] Deploy only the intended service
- [ ] Do not change another app's resources
- [ ] Do not change shared/account-wide settings without explicit approval

## After deployment
- [ ] Deployment status is successful
- [ ] Health check passes
- [ ] Startup logs checked
- [ ] Error logs checked
- [ ] Public endpoint/domain checked
- [ ] Main user flow checked
- [ ] Database/storage behavior checked if relevant
- [ ] No unrelated service was redeployed or modified
- [ ] Changelog updated for meaningful infrastructure changes

A build succeeding is not enough. Production verification is required.
