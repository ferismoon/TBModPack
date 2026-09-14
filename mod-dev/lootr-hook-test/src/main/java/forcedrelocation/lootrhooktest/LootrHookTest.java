package forcedrelocation.lootrhooktest;

import net.fabricmc.api.ModInitializer;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public final class LootrHookTest implements ModInitializer {
    public static final Logger LOGGER = LoggerFactory.getLogger("Lootr Hook Test");
    @Override public void onInitialize() {
        LOGGER.info("Loot Tidy diagnostics 0.1.2 loaded; server-side container interactions enabled");
        net.fabricmc.fabric.api.event.player.UseBlockCallback.EVENT.register((player, world, hand, hit) -> {
            if (!(world instanceof net.minecraft.server.world.ServerWorld server)
                    || hand != net.minecraft.util.Hand.MAIN_HAND) return net.minecraft.util.ActionResult.PASS;
            var pos = hit.getBlockPos();
            var entity = world.getBlockEntity(pos);
            if (entity == null || (!(entity instanceof net.minecraft.inventory.Inventory)
                    && !net.minecraft.registry.Registries.BLOCK_ENTITY_TYPE.getId(entity.getType()).toString().contains("lootr")))
                return net.minecraft.util.ActionResult.PASS;
            try {
                var nbt = entity.createNbt();
                var tableFields = new java.util.TreeMap<String, String>();
                for (String key : nbt.getKeys()) {
                    String lower = key.toLowerCase(java.util.Locale.ROOT);
                    if (lower.contains("loot") || lower.contains("table") || lower.contains("seed"))
                        tableFields.put(key, String.valueOf(nbt.get(key)));
                }
                var structures = new java.util.ArrayList<String>();
                var registry = server.getRegistryManager().get(net.minecraft.registry.RegistryKeys.STRUCTURE);
                for (var start : server.getStructureAccessor().getStructureStarts(new net.minecraft.util.math.ChunkPos(pos), structure -> true)) {
                    if (start.hasChildren() && start.getBoundingBox().contains(pos))
                        structures.add(String.valueOf(registry.getId(start.getStructure())));
                }
                LOGGER.info("[LootDiag INTERACT] dimension={} pos={} block={} entityType={} class={} structures={} tableFields={} note=interaction_attempt_not_proof_of_generation",
                    world.getRegistryKey().getValue(), pos.toShortString(),
                    net.minecraft.registry.Registries.BLOCK.getId(world.getBlockState(pos).getBlock()),
                    net.minecraft.registry.Registries.BLOCK_ENTITY_TYPE.getId(entity.getType()),
                    entity.getClass().getName(), structures, tableFields);
            } catch (Exception error) {
                LOGGER.warn("[LootDiag] Unable to inspect container at {}", pos, error);
            }
            return net.minecraft.util.ActionResult.PASS;
        });
    }
}
