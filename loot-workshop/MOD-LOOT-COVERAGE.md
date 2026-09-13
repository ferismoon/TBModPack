# Mod loot coverage and injection plan

This is the working reference for the 1.3 loot branch. The detailed machine-readable results are in [`mod-coverage-audit/MOD-BY-MOD.md`](mod-coverage-audit/MOD-BY-MOD.md), [`mod-coverage-audit/mod-coverage.csv`](mod-coverage-audit/mod-coverage.csv), and [`mod-coverage-audit/evidence.json`](mod-coverage-audit/evidence.json).

The audit scans the current MS Test Client jars, the generated OpenLoader loot pack, and the KubeJS data. It records native loot tables, likely loot-table hooks, item-model namespaces, existing workshop routes, and structure references. It is evidence for planning; an item model does not prove that an item is registered, and the absence of a table does not prove that a mod never adds loot.

## Current coverage

The pack now has three deliberate loot layers:

1. Native tables supplied by the mod that owns a structure or chest.
2. The workshop structure reward profiles, applied to the 297 active structure routes.
3. Shared player-plushie and collectible pools, applied centrally so modded structures receive them as well.

The audit shows native coverage is already present for several content mods, including AlcoCraft+, Beachparty, Beautify, BetterEnd, Oh The Biomes We've Gone, Bosses of Mass Destruction, Brewery, and other structure or adventure content. Create has workshop rewards but no native chest-table item references in the scanned evidence, so its useful resources are currently represented by the workshop layer rather than assumed to be supplied by Create.

## Injection priorities

These are the next review groups, ordered by value rather than by the number of installed files:

- **Major progression resources:** Create and its add-ons, Farmer's Delight and food add-ons, Brewery, BetterEnd/End's Delight, Nether's Delight, and other processing or material mods. Add a small number of useful starter resources to themed structure profiles, keeping rare materials rare.
- **Exploration rewards:** BetterEnd, Biomes We've Gone, Better Dungeons/Temples/Fortresses/Strongholds, Structory, YUNG's structures, CTOV, and other structure providers. Keep their native special loot where it works, then use the workshop profiles for consistent supplies and collectibles.
- **Collectibles:** player plushies and the central Perfect Plushies replacement pool. Native Perfect Plushies global modifier routes remain disabled because their serializer is broken in this environment; the shared pool is the supported route.
- **Cosmetic and utility items:** hats, beach items, decorative items, trinkets, and equipment. These should be added only after confirming a real registered item and a suitable chest tier; visual-only and library namespaces should not be given loot automatically.
- **No injection by default:** libraries, APIs, client-only utilities, world-generation-only mods, and mods whose items are not sensible exploration rewards.

## How to use this report

For each candidate namespace, check the detailed entry and classify it as **native**, **workshop**, **both**, or **review**. Only items confirmed in the registry and suitable for a chest tier should be added to `structure_rewards.py` or a pool. After a change, regenerate the OpenLoader zip, run the builder checks, and validate in a newly generated world; existing Lootr inventories do not regenerate.

The audit itself changes no gameplay files and is intentionally kept under `loot-workshop`, which is excluded from Packwiz.
