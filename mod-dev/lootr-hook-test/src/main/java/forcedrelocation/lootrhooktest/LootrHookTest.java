package forcedrelocation.lootrhooktest;

import net.fabricmc.api.ModInitializer;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public final class LootrHookTest implements ModInitializer {
    public static final Logger LOGGER = LoggerFactory.getLogger("Lootr Hook Test");
    @Override public void onInitialize() { LOGGER.info("Lootr hook test loaded"); }
}
