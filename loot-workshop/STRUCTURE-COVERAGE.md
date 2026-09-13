# Modded structure reward rollout

The workshop now generates `kubejs/server_scripts/generated_structure_rewards.js`. This adds one optional weighted bundle to each of 297 installed table targets; it never replaces their original pools. Plushies retain their separate 10% roll. No Beachparty equipment is duplicated by these profiles.

| Profile | Chance of one additional bundle | Targets |
| --- | ---: | ---: |
| Village | 50% | 84 |
| Easy | 50% | 120 |
| Medium | 65% | 18 |
| Hard | 80% | 1 |
| Water | 60% | 13 |
| Nether | 65% | 52 |
| End | 75% | 9 |

These are initial balancing values, not the old Loot Integrations probabilities. Bundles contain modest amounts of Create resources, Farmer's Delight provisions and materials, Nether's Delight ingredients, and End-themed materials/food. Precision mechanisms are restricted to low-weight hard/End rewards.

Coverage includes CTOV (11), Moog's Voyager (32), Missing Villages (10), Nether (24), End (8), Temples (34), Structory (31), Towers (25), Dungeons and Taverns (50 nova_structures tables and 17 minecraft-namespaced custom tables), YUNG's structures (43 including Extras), and Immersive Structures (12).

## Evidence and limitations

`structure-routes.json` records each target, its installed source jar, selected profile, and any recovered Loot Integrations mapping. The five archived add-on jars in the local server mods directory are read only as reference; they are not reinstalled. Current table names/theme supply additional coverage beyond the archived mappings.

262 archived target IDs were absent from the installed resource tables. They are listed under `missing_legacy_targets`; some belong to uninstalled mods or different mod versions. 56 referenced helper or empty tables are excluded. Structures using vanilla tables keep those tables' existing rewards; this pass does not blindly map every vanilla chest to a modded profile. Runtime-generated table IDs may require follow-up after gameplay testing.

Item model evidence was checked for every reward against installed jars. This is static validation, not a live item-registry or natural-structure test. Check fresh representative chests from each family and use Loot Tidy's table ID log when a chest appears uncovered.

## Maintaining the sources

Edit probabilities/items/counts/weights in `structure-rewards.json`. Edit route assignments in `structure-routes.json`. Run `build.py`, `build.py --check`, then Packwiz refresh; distribute both generated KubeJS scripts and the datapack with the pack. No Loot Tidy rebuild is required.

`import_structure_routes.py` explicitly regenerates route evidence from the current test client and archived add-ons. It overwrites manual route assignments, so review its diff when deliberately refreshing after mod updates. Other legacy food/resource additions in misc.js are still active pending their separate migration; this change does not claim that migration is complete.
