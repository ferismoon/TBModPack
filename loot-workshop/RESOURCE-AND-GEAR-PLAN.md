# Resource and gear loot plan

The intended rule is **equivalent value, appropriate location**. A chest should still feel like vanilla exploration loot, but its resource rolls may come from the pack's other progression systems.

## Resource bands

| Band | Vanilla baseline | Cross-mod examples | Suitable profiles |
| --- | --- | --- | --- |
| Early | coal, copper, iron, food, sticks | Create copper sheets, zinc, Farmer's Delight ingredients, rope | village, easy, water |
| Mid | gold, redstone, lapis, emeralds, iron equipment | Create brass, andesite alloy, experience nuggets, Brewery ingredients, farming supplies | medium, village, water |
| Late | diamonds, quartz, netherite-adjacent materials | BetterEnd crystals, End's Delight, Create mechanisms, advanced food | hard, nether, end |
| Jackpot | enchanted or high-tier equipment | Advanced Netherite gear, rare Create components, special mod equipment | hard and end only, very low weight |

The implementation should add one small resource or gear pool to a profile rather than replacing the source table. This keeps native mod loot intact and prevents every chest from becoming a general-purpose shopping chest.

## Gear rules

- Early structures may contain damaged or low-tier mod tools and utility items.
- Mid-tier structures may contain one tool, weapon, or armour piece from a relevant mod, with low weight.
- Nether and End structures may contain higher-tier equipment, but never a complete matching set.
- Create machinery belongs in technical or difficult structures, not village starter chests.
- Food and farming items belong in village, farm, and supply profiles.
- Cosmetic and collectible items remain in their existing shared pools.

Before adding an item, confirm that it is a real registered item and that its normal crafting or progression tier matches the profile. The audit report provides the candidate item evidence; it does not automatically promote every registered item into loot.

## First implementation pass

The first pass should add confirmed resource equivalents and a very small number of representative tools to the existing `village`, `easy`, `medium`, `water`, `nether`, and `end` profiles. We should then test fresh structures and tune weights from actual chest results before expanding the catalogue.

## Content families that must be covered

- **Food and farming:** Farmer's Delight, Expanded Delight, Ocean's Delight, Nether's Delight, End's Delight, Nature's Delight, Farm & Charm, Candlelight, and the other Let's Do food modules. Their ingredients, seeds, meals, kitchen supplies, and farming tools should appear in village, farm, supply, and biome-appropriate chests.
- **Brewing and drinks:** Brewery and HerbalBrews. Ingredients and lower-tier drinks can appear in villages and taverns; stronger or unusual drinks belong in medium and hard exploration profiles.
- **Magic and natural resources:** Hexalia. Herbs, plants, crystals, reagents, and low-tier magical tools should be considered for village, forest, swamp, and difficult exploration tables. Rare combat or progression items should remain hard or jackpot rewards.
- **Technical resources:** Create and its add-ons. Sheets, alloys, zinc, nuggets, experience items, and selected components should be distributed by tier; complex mechanisms and machines should stay rare.
- **Nether and End resources:** BetterEnd, BetterEndDelight, Nether's Delight, and End's Delight. Their materials and foods should be present in the corresponding dimension profiles rather than only in generic structure loot.

The detailed audit already confirms these namespaces are installed and records their available item evidence. The reward compiler will continue to reject unconfirmed item IDs, so additions will be based on the evidence file rather than guessed names.
