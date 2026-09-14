package forcedrelocation.lootrhooktest.mixin;

import net.minecraft.entity.player.PlayerEntity;
import net.minecraft.inventory.Inventory;
import net.minecraft.inventory.SimpleInventory;
import net.minecraft.item.ItemStack;
import net.minecraft.loot.LootTable;
import net.minecraft.loot.context.LootContextParameterSet;
import net.minecraft.util.Identifier;
import net.zestyblaze.lootr.block.entities.LootrChestBlockEntity;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;
import forcedrelocation.lootrhooktest.LootrHookTest;

@Mixin(LootrChestBlockEntity.class)
public abstract class LootrChestBlockEntityMixin {
    @org.spongepowered.asm.mixin.injection.Redirect(method = "unpackLootTable", at = @At(value = "INVOKE", target = "Lnet/minecraft/class_52;method_329(Lnet/minecraft/class_1263;Lnet/minecraft/class_8567;J)V"))
    private void forcedrelocation$compactBeforeInsert(LootTable table, Inventory inventory, LootContextParameterSet context, long seed) {
        // Generate without a container limit: supplyInventory can discard overflow.
        java.util.List<ItemStack> generated = table.generateLoot(context, seed);
        LootrChestBlockEntity chest = (LootrChestBlockEntity)(Object)this;
        LootrHookTest.LOGGER.info("[LootDiag GENERATE] pos={} table={} seed={} items={}",
            chest.getPos().toShortString(), chest.getTable(), seed,
            generated.stream().map(stack -> net.minecraft.registry.Registries.ITEM.getId(stack.getItem()) + " x" + stack.getCount()).toList());
        SimpleInventory temporary = new SimpleInventory(generated.size());
        for (int i = 0; i < generated.size(); i++) temporary.setStack(i, generated.get(i).copy());
        int merged = 0;
        for (int first = 0; first < temporary.size(); first++) {
            ItemStack destination = temporary.getStack(first);
            if (destination.isEmpty()) continue;
            for (int second = first + 1; second < temporary.size(); second++) {
                ItemStack source = temporary.getStack(second);
                if (source.isEmpty() || !ItemStack.canCombine(destination, source)) continue;
                int room = destination.getMaxCount() - destination.getCount();
                if (room <= 0) continue;
                int moved = Math.min(room, source.getCount());
                destination.increment(moved);
                source.decrement(moved);
                if (source.isEmpty()) temporary.setStack(second, ItemStack.EMPTY);
                merged += moved;
            }
        }
        int slot = 0;
        int overflow = 0;
        for (int i = 0; i < temporary.size(); i++) {
            ItemStack stack = temporary.getStack(i);
            if (stack.isEmpty()) continue;
            if (slot < inventory.size()) inventory.setStack(slot++, stack.copy());
            else {
                overflow++;
                LootrHookTest.LOGGER.error("Loot Tidy capacity exceeded: unable to fit {}", stack);
            }
        }
        while (slot < inventory.size()) inventory.setStack(slot++, ItemStack.EMPTY);
        inventory.markDirty();
        LootrHookTest.LOGGER.info("Loot Tidy packing v0.1.1: table={}, generatedStacks={}, slots={}, mergedItems={}, overflowStacks={}", ((LootrChestBlockEntity)(Object)this).getTable(), generated.size(), inventory.size(), merged, overflow);
    }
}
