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

## Current MotionLab duplicate cleanup

Known residue:
- app01-motionlab service inside ReturnReview
- its generated public domain
- earlier project-level Hub metadata inside ReturnReview

Do not clean these during ordinary MotionLab or ReturnReview work.

Required cleanup sequence:
1. Confirm standalone MotionLab project/service is healthy.
2. Confirm the duplicate contains no unique variables, volumes, data, custom domains, or dependencies.
3. Confirm ReturnReview does not reference the duplicate.
4. Confirm the duplicate does not reference ReturnReview.
5. Record the proposed deletion in the changelog.
6. Obtain explicit user confirmation immediately before deletion.
7. Delete only the duplicate service.
8. Verify standalone MotionLab remains healthy.
9. Verify ReturnReview API/web remain healthy.
10. Separately review the three misplaced Hub metadata entries.
11. Obtain explicit confirmation before deleting that metadata.
12. Run final inventory and update registry.

## Database rollback

Code rollback and database rollback are separate decisions.

Never assume rolling back code safely rolls back schema/data.

Prefer additive migrations and verified backups before destructive database changes.
