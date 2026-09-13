# Player plushie rollout

`player-plushies.json` controls a 10% chance for one item from 27 populated player slots, three Homestead creatures, and 47 Perfect Plushies designs. Empty slots 28–50 and the generic player model are excluded. All 77 entries have equal weight.

The current manifest covers 528 candidate root chest tables from the installed mods and vanilla resources. Referenced helper tables and Beachparty donor tables are excluded to reduce duplicate nested rolls. This is broad coverage, not every container or every runtime-injected table. The chance applies to this custom pool; independent plushie additions from other mods are not capped by it.

`build.py` generates `kubejs/server_scripts/generated_player_plushies.js` alongside the datapack. Deploy both outputs and the edited `misc.js` together. The old Homestead plushie handler and guaranteed shipwreck test have been removed. Other legacy loot additions still remain in misc.js pending migration.

The generated script uses the existing KubeJS chest-loot API; no mod rebuild is required. Restart after updating. Newly generated loot must be tested in-game to verify runtime coverage.

The datapack replaces the global modifier route list using `global-modifier-routes.json`: 66 broken Perfect Plushie API routes are omitted, and the installed pack's 59 other modifier routes are retained. Re-run `import_perfect_plushies.py` and review that list when adding or updating mods with global loot modifiers. This is a pack-specific snapshot. It disables the broken routes without altering the item mod. The independent cat/frog village entries were removed from misc.js to avoid overlapping custom plushie rolls. Native archaeology routes are disabled too; this replacement is chest-only.
