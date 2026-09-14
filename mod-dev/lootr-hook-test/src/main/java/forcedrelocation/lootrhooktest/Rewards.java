package forcedrelocation.lootrhooktest;

import com.google.gson.*;
import java.nio.file.*;
import java.util.*;
import net.minecraft.item.ItemStack;
import net.minecraft.registry.Registries;
import net.minecraft.util.Identifier;

/** External, server-owned configuration. Reloaded on server start. */
public final class Rewards {
    private static JsonObject config;
    public static void load() {
        config = null;
        Path path = net.fabricmc.loader.api.FabricLoader.getInstance().getConfigDir().resolve("forced-relocation-rewards.json");
        try (var reader = Files.newBufferedReader(path)) {
            JsonObject candidate = JsonParser.parseReader(reader).getAsJsonObject();
            for (var profile : candidate.getAsJsonObject("profiles").entrySet()) {
                double chance = profile.getValue().getAsJsonObject().get("chance").getAsDouble();
                if (chance < 0 || chance > 1) throw new IllegalArgumentException("Invalid chance");
                for (var row : profile.getValue().getAsJsonObject().getAsJsonArray("items")) {
                    var entry = row.getAsJsonObject();
                    verify(entry.get("item").getAsString());
                    if (entry.get("weight").getAsInt() <= 0 || entry.get("count").getAsInt() < 1 || entry.get("count").getAsInt() > 64)
                        throw new IllegalArgumentException("Invalid reward weight/count");
                }
            }
            for (var item : candidate.getAsJsonObject("plushies").getAsJsonArray("items")) verify(item.getAsString());
            for (var route : candidate.getAsJsonObject("routes").entrySet())
                if (!candidate.getAsJsonObject("profiles").has(route.getValue().getAsString())) throw new IllegalArgumentException("Unknown profile " + route);
            config = candidate;
            LootrHookTest.LOGGER.info("[LootDiag CONFIG] loaded {} reward routes", config.getAsJsonObject("routes").size());
        } catch (Exception e) { LootrHookTest.LOGGER.error("[LootDiag CONFIG] Rewards disabled: cannot load " + path, e); }
    }
    private static void verify(String id) {
        if (!Registries.ITEM.containsId(new Identifier(id)) || id.equals("minecraft:air")) throw new IllegalArgumentException("Unknown reward item: " + id);
    }
    public static void add(List<ItemStack> output, Identifier table, long seed) {
        if (config == null) return;
        Random random = new Random(seed ^ 0x46524c4f4f54L);
        var added = new ArrayList<String>();
        var route = config.getAsJsonObject("routes").get(table.toString());
        if (route != null) {
            var profile = config.getAsJsonObject("profiles").getAsJsonObject(route.getAsString());
            if (random.nextDouble() < profile.get("chance").getAsDouble()) {
                var entries = profile.getAsJsonArray("items");
                int total = 0;
                for (var e : entries) total += e.getAsJsonObject().get("weight").getAsInt();
                int roll = random.nextInt(total);
                for (var e : entries) {
                    var row = e.getAsJsonObject();
                    roll -= row.get("weight").getAsInt();
                    if (roll < 0) { put(output, added, row.get("item").getAsString(), row.get("count").getAsInt()); break; }
                }
            }
        }
        var plush = config.getAsJsonObject("plushies");
        boolean eligible = false;
        for (var target : plush.getAsJsonArray("targets")) if (target.getAsString().equals(table.toString())) { eligible = true; break; }
        if (eligible && random.nextDouble() < plush.get("chance").getAsDouble()) {
            var items = plush.getAsJsonArray("items");
            put(output, added, items.get(random.nextInt(items.size())).getAsString(), 1);
        }
        LootrHookTest.LOGGER.info("[LootDiag REWARDS] table={} profile={} added={}", table, route == null ? "unmapped" : route.getAsString(), added);
    }
    private static void put(List<ItemStack> output, List<String> added, String id, int count) {
        output.add(new ItemStack(Registries.ITEM.get(new Identifier(id)), count));
        added.add(id + " x" + count);
    }
}
