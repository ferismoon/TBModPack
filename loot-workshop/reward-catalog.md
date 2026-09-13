# Loot reward catalogue

Working catalogue for the 1.3 exploration loot pass. Items are reviewed here before they are added to a pool. The catalogue is intentionally separate from the generated datapack.

## Collectibles and plushies

- `phomesteadplushies:homestead_player_1` through `homestead_player_50` are installed. The populated player entries currently include server/community names such as `homestead_player_22` (JadedStar) and `homestead_player_27` (madmooncrow); the later empty slots should remain excluded until they are assigned.
- `phomesteadplushies:mushling_plushie`
- `phomesteadplushies:mystical_elk_plushie`
- `phomesteadplushies:fernling_plushie`
- Server-created player plushies use the same `phomesteadplushies:homestead_player_N` entries, rather than a separate namespace.
- `perfectplushies:*`: review separately; the broken global-loot serializer must not be used.

## Major reward families

### Create and engineering

`create-fabric`, `createaddition`, `createdeco`, `create_connected`, `create_jetpack`, `create_enchantment_industry`, `create_vibrant_vaults`, `create-dragons-plus`, `cratedelight`, and `create_oxidized`.

Candidate rewards: low-tier components, copper parts, zinc, and decorative Create materials. Avoid machines, progression gates, and high-value automation parts.

### Food, farming, and cooking

`FarmersDelight`, `NethersDelight`, `Ocean's Delight`, `Expanded Delight`, `Chef's Delight`, `Nature's Delight`, `BetterEndDelight`, `farm_and_charm`, and `smarterfarmers`.

Candidate rewards: seeds, ingredients, preserved food, modest prepared meals, and cooking supplies.

### Brewing and drinks

`Brewery`, `HerbalBrews`, `Vinery`, `Candlelight`, `AlcoCraftPlus`, and `BeachParty`.

Candidate rewards: bottles, ingredients, drinks, music discs, and themed beach items. BeachParty's own chest table remains untouched.

### Building and decoration

`Chipped`, `Handcrafted`, `Beautify`, `Supplementaries`, `Amendments`, `Clutter`, `Cluttered`, `Immersive Furniture`, `Decorative Lamps`, `Dusty Decorations`, and `Natures Spirit`.

Candidate rewards: decorative blocks, furniture components, lamps, pottery, and small building bundles.

### Exploration and collectibles

`Perfect Plushies`, `Homestead Plushies`, `Simple Hats`, `Go Fish`, `Squish`, and `Spelunkery`.

Candidate rewards: plushies, hats, novelty items, maps, fishing items, and low-tier cave finds.

### World and structure content

`BetterEnd`, `Regions Unexplored`, `Incendium`, `Moog's structures`, `Structory`, `Structory Towers`, `Dungeons and Taverns`, and YUNG's structures.

These primarily define locations and difficulty. Their structure loot should receive themed pools rather than a single universal reward list.

## Review rules

- Prefer items that introduce a mod without bypassing its progression.
- Keep common supplies stackable and modest.
- Put collectibles and rare equipment in low-weight entries.
- Never reintroduce the BeachParty rubber rings.
- Confirm every item exists in the installed registry before adding it to a generated pool.
