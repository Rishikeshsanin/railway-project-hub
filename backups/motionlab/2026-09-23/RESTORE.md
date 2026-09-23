# MotionLab Railway Restore Guide

This snapshot was created **before retiring the standalone MotionLab Railway project** to free one Railway project slot for the governance-only Railway Project Hub.

## Source preservation

- Repository: `Rishikeshsanin/animation-website`
- Preserved main commit: `85e64bd1dd67148893290c5862a1187567b7e54e`
- Permanent archive branch: `archive/pre-railway-retirement-2026-09-23`

The GitHub repository is the canonical source. Deleting the Railway project does **not** delete the code.

## Railway state at backup time

- Project: `MotionLab`
- Project ID: `917d84ff-5ef4-4d64-9629-b731ab79d67b`
- Environment: `production`
- Environment ID: `bca2ecae-b4dd-4047-87da-428b96be0270`
- Service: `motionlab`
- Service ID: `048331c3-43df-4bbb-a1a5-1cea4adcfc5d`
- Railway domain: `motionlab-production-2310.up.railway.app`
- Builder: Railpack V3
- Runtime: V2
- Region: sfo
- Replicas: 1

## Data-loss assessment

Verified before retirement:

- no custom application variables/secrets
- no Railway database
- no Railway volume
- no bucket
- no cron
- no custom domain
- no persistent Railway-only application data

Only Railway runtime/deployment metadata and the generated Railway domain are removed when the project is retired. The source code and exact archive commit remain preserved in GitHub.

## Restore procedure

If MotionLab needs Railway hosting again:

1. Read the frozen Railway Project Hub governance first.
2. Confirm account capacity for a separate MotionLab project.
3. Create a new isolated Railway project named `MotionLab`.
4. Deploy `Rishikeshsanin/animation-website` from the intended archived/current commit.
5. Use Railpack unless the repository has deliberately changed its deployment model.
6. Generate a new Railway service domain.
7. Verify build, production page, and main interactive flows.
8. Update the Hub registry with the **new** project/environment/service/domain IDs.
9. Never reuse the retired IDs as if they were active.

The old generated Railway domain is not guaranteed to be recoverable after project deletion.
