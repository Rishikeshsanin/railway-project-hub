# Recovery and Cleanup

## General recovery rule

Do not improvise destructive fixes.

Use:
inspect -> identify previous known-good state -> contain -> plan rollback -> recover -> verify -> document

## Deletion gate

Before deleting a project, service, domain, database, volume, or other persistent resource:
1. Verify exact owner in the Hub registry.
2. Inspect all dependencies.
3. Determine whether it stores unique data.
4. Identify canonical replacement/recovery source.
5. Verify replacement is healthy.
6. Prefer disabling/detaching first when practical.
7. Verify no user flow depends on the resource.
8. Obtain explicit user confirmation immediately before destructive deletion.
9. Delete only the registered target.
10. Audit all applications after deletion.
11. Update registry and changelog.

## MotionLab duplicate cleanup — completed

The non-canonical app01-motionlab service inside ReturnReview was safely removed on 2026-09-23.

Completed checks:
1. standalone MotionLab project/service verified healthy
2. duplicate verified to contain no unique variables, volumes, data, custom domains, or dependencies
3. ReturnReview verified not to reference the duplicate
4. duplicate verified not to reference ReturnReview
5. proposed deletion recorded in changelog
6. explicit user confirmation obtained
7. only the duplicate service deleted
8. standalone MotionLab verified healthy afterward
9. ReturnReview API/web verified healthy afterward
10. registry/changelog updated

Still pending separately:
- review the three misplaced Hub metadata entries inside ReturnReview
- obtain explicit confirmation before deleting any of that metadata
- run a final metadata cleanup audit afterward

## Database rollback

Code rollback and database rollback are separate decisions.

Never assume rolling back code safely rolls back schema/data.

Prefer additive migrations and verified backups before destructive database changes.
