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
        SimpleInventory temporary = new SimpleInventory(54);
        table.supplyInventory(temporary, context, seed);
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
        for (int slot = 0; slot < inventory.size(); slot++) inventory.setStack(slot, slot < temporary.size() ? temporary.getStack(slot).copy() : ItemStack.EMPTY);
        inventory.markDirty();
        LootrHookTest.LOGGER.info("Lootr pre-insert hook fired: table={}, slots={}, mergedItems={}", table, inventory.size(), merged);
    }
}
