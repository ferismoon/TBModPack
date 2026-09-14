# Loot Tidy 0.2.0 testing

Install the 0.2.0 jar together with `config/forced-relocation-rewards.json` and both regenerated KubeJS files. The two scripts are intentionally inert: the mod now owns structure and plushie reward rolls. Keep the existing OpenLoader pack for its independent table and modifier fixes.

The mod loads the config on server start (including singleplayer). Restart after config changes. Workshop edits are compiled by `build.py`; its `--check` mode checks the runtime config as well as other outputs.

Lootr chest, barrel and shulker generation share the hook; trapped chests inherit the chest implementation. This does not re-roll saved inventories. Prefilled inventory behavior and other generation paths must be checked separately.

Test a fresh Moog house chest and barrel. Look for CONFIG loaded, GENERATE original items, REWARDS profile and additions, then packing. Village/easy/medium/water routes guarantee one resource selection; plushies have a separate 10% roll on their configured targets. Unmapped tables are explicitly reported. Unknown item IDs disable the reward config with an error, while original loot continues.

Build and workshop checks are not gameplay proof. Structure matches are bounding-box matches and can overlap. The existing intermediary-mapping compiler warning remains; confirm the new barrel/shulker mixins during client startup.
