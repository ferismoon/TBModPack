package com.moonie.blahajfix.mixin;

import com.moonie.blahajfix.access.ForgingScreenHandlerAccess;
import net.minecraft.entity.player.PlayerEntity;
import net.minecraft.screen.ForgingScreenHandler;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.Shadow;

@Mixin(ForgingScreenHandler.class)
public abstract class ForgingScreenHandlerAccessor implements ForgingScreenHandlerAccess {
    @Shadow protected final PlayerEntity player = null;

    @Override
    public PlayerEntity blahajFix$getPlayer() {
        return player;
    }
}
