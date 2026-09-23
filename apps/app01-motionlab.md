# App 01 — MotionLab

## Identity
- App number: 01
- Slug: `motionlab`
- Repository: https://github.com/Rishikeshsanin/animation-website
- Status: **archived**
- Active Railway project: **none**

App 01 remains permanently reserved for MotionLab. Its number and slug must never be reused.

## Archive state

MotionLab's Railway runtime was safely retired on 2026-09-23 after:
- verifying the source repository,
- creating a permanent source archive branch,
- exporting a downloadable source snapshot,
- capturing non-secret Railway configuration and deployment metadata,
- verifying no database, volume, bucket, cron, custom domain, custom application secret, or unique Railway-persistent data existed.

Preserved source:
- main commit: `85e64bd1dd67148893290c5862a1187567b7e54e`
- archive branch: `archive/pre-railway-retirement-2026-09-23`

Restore documentation:
- `backups/motionlab/2026-09-23/README.md`
- `backups/motionlab/2026-09-23/RAILWAY_SNAPSHOT.json`
- `backups/motionlab/2026-09-23/RESTORE.md`

## Historical Railway identity

Former project:
- name: `MotionLab`
- project ID: `917d84ff-5ef4-4d64-9629-b731ab79d67b`
- environment ID: `bca2ecae-b4dd-4047-87da-428b96be0270`

Former service:
- name: `motionlab`
- service ID: `048331c3-43df-4bbb-a1a5-1cea4adcfc5d`
- former Railway domain: `motionlab-production-2310.up.railway.app`

The service was deleted with explicit authorization after backup verification.

## Project-ID repurposing warning

The former MotionLab **project container was not deleted**. After the MotionLab service was removed, the empty container was renamed to **Railway Project Hub**.

Therefore project ID:

`917d84ff-5ef4-4d64-9629-b731ab79d67b`

is **not an active MotionLab resource anymore**.

Its current role is the governance-only Railway Project Hub project. Never infer MotionLab ownership from historical ID references.

## Restore rule

If MotionLab is deployed to Railway again:
1. read the Hub governance first,
2. use the preserved source/restore snapshot,
3. create a **new isolated MotionLab Railway project**,
4. never place MotionLab runtime services inside Railway Project Hub,
5. verify the new live IDs,
6. update the Hub registry and changelog.

ReturnReview and every other application remain out of scope during a MotionLab restore.
