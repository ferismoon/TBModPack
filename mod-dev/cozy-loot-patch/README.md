# Cozy Core loot registration patch

REVERTED: Do not distribute a patched Cozy Core JAR. The user identified a
redistribution restriction. The patched artifact was deleted and the original
pinned CurseForge entry restored. KubeJS replacements remain in use; the
original redundant handler's warning is accepted. The notes below describe
the abandoned patch, not the current pack configuration.

Base: CozyStudios Core 2.1 for Minecraft 1.20.1, CurseForge file 8795699.
Original SHA-1: ecbb9ee316b274befda319331c55179294bf204e.

PatchCozy.java removes the single call to LootTableFixes.register() in
CozyStudiosCore.class. It verifies every other JAR entry remains identical.
The original reflection lookup fails with "LootManager Gson not found".

All eight bundled replacements were compared structurally against KubeJS data
overrides in McWork, the test client, and server: all match. These cover five
Beachparty ocean chest tables and three Incendium castle tables. Existing
KubeJS scripts add their extra pools separately.

The patched JAR is distributed directly through Packwiz to preserve the patch.
This development folder is excluded by .packwizignore. Rollback: restore the
original cozystudios-core.pw.toml from Git, remove the patched JAR and refresh.
Do not load both JARs together.

Validation: archive comparison and bytecode inspection. Fresh startup and
loot generation still need runtime verification.
