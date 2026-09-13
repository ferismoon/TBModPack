# Forced Relocation loot workshop

Editable sources for the 1.3 loot update. This folder belongs in Git and is excluded from Packwiz. Only `config/openloader/data/forced-relocation-loot.zip` is installed. OpenLoader already supports ZIP datapacks in that directory.

## Current state

The foundation builds three shared tables and previews seven ocean mappings. **Every chest mapping starts disabled.** The installed datapack therefore defines new shared tables but changes no chest rewards. Loot Integrations and existing KubeJS loot hooks still run unchanged. Activation is the next migration step, not a completed balance overhaul.

The sample 10% supply / 25% treasure chance and 75:23:2 equipment/collectible/jackpot weights demonstrate the configuration. They are proposed starting values, not measured existing rates or final approved balance. All choices share one bonus draw; they do not each trigger independent rolls. Blacklisted Beachparty rubber rings are deliberately excluded.

## What to edit

| Folder/file | Purpose |
| --- | --- |
| `pools/` | Item IDs and relative weights within each shared reward set |
| `profiles/` | Overall bonus chance and relative selection between shared sets |
| `mappings/ocean.json` | Exact destination IDs, profile, enabled flag and integration review notes |
| `preserved-tables/` | Unmodified baseline JSON, retaining original counts, functions, conditions and special loot |
| `catalog.json` | Reviewed item evidence and baseline provenance/hashes |
| `reports/` | Generated local build report and preview ZIP; ignored by Git and Packwiz |

The current generator supports adding exactly one shared bonus pool to a preserved table. It does not yet rewrite filler weights, remove original pools, or control Java injections. Extend that behaviour deliberately when migrating the first chest family. Item entries support ID and positive integer weight; quantities/NBT remain untouched in baselines. New custom reward functions need explicit schema validation before being added to shared entries.

## Build and preview

Requires Python 3.11+ with no third-party packages. Run from MCWork:

```powershell
python loot-workshop/build.py
python loot-workshop/build.py --check
python loot-workshop/build.py --preview
python loot-workshop/test_build.py
```

`build` writes the installed ZIP deterministically. `--check` validates sources and checks that output is current, without writing. `--preview` generates all mapped chest overrides into `loot-workshop/reports/preview.zip` only; it never updates the installed pack. Do not install preview.zip alongside the generated datapack.

After an intentional installed-output change, run `packwiz refresh` and include both index/pack metadata and the generated ZIP in the same eventual commit. Previewing alone needs no Packwiz refresh.

## Bringing a chest family live

1. Check active table IDs and other injectors on the test server. The saved loot audit in `docs/quest-planning/loot-audit` provides background evidence.
2. Migrate overlapping `misc.js` additions and account for Beachparty's Java injection. Do not add duplicate swimwear pools. Remove/reconfigure Loot Integrations only as part of that migration, with its lost coverage tracked.
3. Compare the preserved baseline with current mod resources after updates. `import_sources.py` is an explicit re-import tool, never an automatic part of a build.
4. Set `integration_reviewed` and `enabled` to true for the reviewed mapping. The build rejects enabled mappings without the review flag.
5. Build, refresh Packwiz and test fresh loot. Check old Lootr containers separately; generated changes do not directly rewrite saved inventories.

The review flag records a human/code review decision; it cannot automatically prove that all runtime injections are safe. Local item-model evidence is also not a live registry or drop test. A mod can still modify tables after datapack loading.

## Source updates

`import_sources.py --minecraft-jar PATH --moogs-jar PATH --beachparty-jar PATH` explicitly refreshes the seven mapped baselines and item catalog from installed archives. Review its diff before rebuilding. The generated datapack needs no local jar paths or Python at runtime.

Deleting a mapping removes that override from the next generated ZIP automatically. The builder replaces only its own named ZIP and does not recursively delete directories or modify other datapacks. Do not edit the generated ZIP manually.
