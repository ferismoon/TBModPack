package com.moonie.blahajfix.mixin;

import com.moonie.blahajfix.access.ForgingScreenHandlerAccess;
import hibi.blahaj.block.CuddlyItem;
import net.minecraft.item.ItemStack;
import net.minecraft.screen.AnvilScreenHandler;
import net.minecraft.nbt.NbtString;
import org.spongepowered.asm.mixin.Final;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.Shadow;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;
import org.spongepowered.asm.mixin.injection.callback.LocalCapture;

@Mixin(AnvilScreenHandler.class)
public abstract class AnvilScreenHandlerMixin {
    @Inject(
            method = "updateResult",
            at = {
                    @At(value = "INVOKE", target = "Lnet/minecraft/item/ItemStack;removeCustomName()V"),
                    @At(value = "INVOKE", target = "Lnet/minecraft/item/ItemStack;setCustomName(Lnet/minecraft/text/Text;)Lnet/minecraft/item/ItemStack;")
            },
            locals = LocalCapture.CAPTURE_FAILHARD,
            expect = 2,
            require = 2
    )
    private void blahajFix$setOwner(
            CallbackInfo info,
            ItemStack firstInput,
            int firstCost,
            int secondCost,
            int levelCost,
            ItemStack result,
            ItemStack secondInput
    ) {
        if (result.getItem() instanceof CuddlyItem) {
            result.getOrCreateNbt().put("Owner", NbtString.of(
                    ((ForgingScreenHandlerAccess) (Object) this).blahajFix$getPlayer().getName().getString()
            ));
        }
    }
}
