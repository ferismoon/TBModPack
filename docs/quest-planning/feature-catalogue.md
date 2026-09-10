# Forced Relocation — feature and path catalogue

Audit date: 9 September 2026. Source pack: `I:/McWork`, Minecraft 1.20.1 / Fabric, pack metadata version 1.2.1. The pack metadata still calls itself “True Bastard ModPack”; this document uses the current Forced Relocation name.

This is a planning catalogue, not a new quest book. Every one of the 423 top-level files in the canonical mods folder is accounted for, including the six directly supplied jars. Matching jar filenames were found locally for all 423, allowing inspection of installed-version metadata and assets. These totals count distributed mod files, not Fabric's larger count of nested libraries/modules. The server and client can legitimately load different subsets.

The catalogue combines a manually categorized feature description for each gameplay mod with an exhaustive file inventory and an expandable list of names extracted from installed item, block, entity, biome, effect and enchantment language assets. It also lists packaged biome and structure definitions. Project links come from the pack's own metadata; 82 Modrinth project records were fetched for additional context, and selected official project/wiki pages were checked. Local version evidence takes priority over newer website features.

The file inventory is complete. The feature descriptions are a planning audit, not an exhaustive reverse-engineering of every mechanic. Asset names can include compatibility content, creative-only objects, disabled items and unused translations; they are not a verified survival registry or proof of acquisition. Raw recipe-file counts are not counts of active recipes. The catalogue marks known pack exceptions, but does not claim that every recipe, spawn or interaction has been tested in-game. Existing quest files and resource-pack pictures are not evidence that an absent mod is installed.

## The paths

Keep the eight original identities. Six further paths have identifiable content, but these are proposed organizational choices, not commitments to fourteen top-level chapters. People should be able to follow several paths; one mod can serve several interests. A primary home prevents duplicate accounting, while crossover tags preserve its wider features.

| Path | Feature groups to organize around | Boundary and possible chapter families |
| --- | --- | --- |
| The Mechanic | Create power, processing, machinery, moving contraptions, farms, fluids, electricity, trains, signals, industrial enchanting | Power a workshop; process materials; automate a useful product; build transport. Railways can be a substantial branch within this path. |
| The Farmer | Crops, wild seed gathering, soil, fertilizer, irrigation, harvesting, orchards, vineyards, garden propagation, forestry, carts | Supply ingredients and timber. Keep making meals with Cook, drinks with Brewer and animal care with Rancher. Forestry can stay here unless it later deserves its own identity. |
| The Cook | Farmer's Delight and its addons, Farm & Charm cooking, Candlelight dining, Meadow cheese, regional and dimensional foods | Ingredient preparation; working kitchens; baking and meals; dairy; seafood; Nether/End cuisine; host a meal. Several cooking systems are alternatives or complements, not necessarily one upgrade ladder. |
| The Brewer | Brewery, AlcoCraft+, Vinery, HerbalBrews and Beachparty drinks | Hops and grain; keg beer; brewing stations; spirits; grape/fruit drinks and wine cellars; tea and coffee; cocktails. HerbalBrews can be a Witch crossover without moving all ordinary drinks into magic. |
| The Witch | Hexalia herbology, processing, brewing, rituals, living plants, silk garments, magical equipment, Things and enchanting | Magical garden; first brew; rituals and elemental materials; practical enchanted plants; clothing and trinkets; enchantment management. This is not evidence for absent magic mods such as Botania or Bewitchment. |
| The Builder | Architectural palettes, furniture, glass, lighting, gardens, industrial decoration, custom shapes, seasonal decor, paintings, posed displays | Build places: cottage, kitchen, greenhouse, workshop, station, tavern, market, gallery. Use material families and finished builds rather than thousands of compulsory colour variants. |
| The Collector | Perfect Plushies, Homestead plushies, Blåhaj, hats, photographs, paintings, special equipment, living variants | Separate crafted, found, earned and photographed collections. The long installed-name lists are candidate checklists; establish obtainability before declaring any collection mandatory. |
| The Explorer | Overworld biomes/terrain, caves, settlements, ruins, Nether, End, Otherside, navigation, camping and travel | Discover places, bring back materials and establish routes. Keep combat victories in Adventurer so exploration is not defined only by killing things. |
| The Angler — proposed | Go Fish rods, lures, fish, crates; regional/dimensional fishing; seafood connections; aquatic animal discoveries | There is a clear fishing loop. Could instead be a substantial Farmer or Explorer branch if fewer identities are preferred. Aquarium keeping overlaps Rancher. |
| The Rancher — proposed | Feeding, breeding, pets, ducks, wildlife, bees, axolotls, Ribbits, taming addons, silk moths, dairy animals | Keep and understand creatures. Broad enough for its own path; could be folded into Farmer. “The Naturalist” is an alternative name if observation matters more than production. |
| The Blacksmith — proposed | Mining tools, ore/gem processing, obsidian and Netherite smithing, Mythic Upgrades, repair, recycling, specialist tools | Equip the other paths. Mining can live here or become “The Miner” later; current catalogue keeps extraction and equipment together to avoid too many small identities. |
| The Adventurer — proposed | Bosses, modified Dragon fight, illagers/caravans, regional hostile mobs, archery, combat equipment and survival preparation | Encounters and combat mastery, distinct from peaceful exploration. A natural place for difficult optional accomplishments. |
| The Merchant — proposed | VillagersPlus, Chef's Delight professions, trade cycling, village guards, Spud's Shops, trading settlements | Villager markets and player shops. Needs a later decision about the server economy; no currency policy is implied by the mod list. Can be a community/settlement branch instead. |
| The Quartermaster — proposed | Chests, drawers, storage networks, upgraded containers, backpacks, labels, portable crafting and moving goods | A well-supported storage/logistics branch. Can sit inside Mechanic and Explorer if a separate identity feels too administrative. |

## Shared foundations

A short shared starting area can explain recipes, map use, food, death recovery, claims/parties, quest teams and starting supplies. These features affect everyone; they do not need to become professions. REI, Jade, AppleSkin, breeding/profession viewers, maps and the supporting controls are included in the full inventory. Libraries, rendering, sound and performance mods are also accounted for without presenting them as quest trees.

## Pack-specific features and exceptions

The following findings are grounded in the canonical configuration and scripts. A script expresses configured intent; checking the final recipe viewer and gameplay remains necessary before writing recipe-specific tasks.

| Feature | What this pack changes | Paths and design consequence | Local evidence |
| --- | --- | --- | --- |
| Beer inputs | Six Brewery beer recipes use the shared hops tag, another ingredient and Farm & Charm yeast. Grain beers use dried grain inputs. | Farmer → Brewer is a real supply connection. Do not copy default beer recipes blindly. | `kubejs/server_scripts/hops_based_beer.js` |
| AlcoCraft keg | Custom keg recipe uses wood slabs, iron and shared hops. | AlcoCraft is a second method within Brewer. | `scripts/mods/AlcoCraft+/keg_test.zs` |
| Shared ingredients | Tags connect crops, hops, eggs, flour and other ingredients across food mods. Bater Wucket is added to several water-input tags. | Cook, Farmer, Brewer and Witch overlap through ingredients, without requiring four duplicate farms. | `scripts/mods/Compat/mod_compat.zs`, `bater_wucket.zs`, `flour.zs` |
| Manual flour | Hexalia and Expanded Delight pestles can produce four Create flour from wheat-tag input; the pestle is damaged. Flour conversions and dough changes also exist. | A manual route can precede Create food automation. | `kubejs/server_scripts/flour.js`, `kubejs/startup_scripts/mortar.js`, `scripts/mods/Compat/flour.zs` |
| Hexalia resin | Athame cutting-board recipes use dark oak or cottonwood logs to produce tree resin. | Witch tools connect to Cook's preparation station and forestry. | `kubejs/server_scripts/resin.js` |
| Smithing | Custom smithing makes Obsidian equipment the base for the listed vanilla Netherite equipment recipes; custom Obsidian template crafting and duplication are present. | Blacksmith is pack-specific progression, not the standard diamond-to-Netherite tutorial. | `scripts/mods/Custom/custom_smithing.zs`, `template.zs`; `kubejs/startup_scripts/obsidian_template.js` |
| Mythic equipment | Dedicated armor-crafting and attribute scripts; crystal block/shard/cluster conversions for seven named gems. | Check the effective recipes and stats before designing the final equipment tree. | `scripts/mods/Mythic Upgrades/`, `kubejs/server_scripts/cluster_recipes.js` |
| Area tools | Nine Toolshed hammer recipes are removed and the items hidden from the recipe viewer; existing items are retained. JustHammers' impact core has a custom recipe. | Use JustHammers for the hammer branch; keep Toolshed excavators, scythes, axes and utility tools. | `kubejs/server_scripts/retire_toolshed_hammers.js`, `kubejs/client_scripts/retire_toolshed_hammers.js`, `scripts/mods/Compat/hammer_changes.zs` |
| Unusable items | Blacklist includes Wilder Nature bounty board; Spelunkery iron pick on a stick and charcoal lump; Clutter red/yellow polypores; five Beachparty rings. | Omit these from required collections. Bounty-board progression is not currently a usable Rancher foundation. | `config/item_obliterator.json5` |
| Plushie loot | Custom pool contains 30 Homestead plushies: 27 player entries and three creatures. Applied to selected vanilla chest tables with 0.5 buried-treasure probability and 0.1 for several other targets. These are pool conditions, not measured world-wide drop rates. | Separate locating suitable loot from finishing the collection. Replaced ocean loot tables mean actual destinations need checking. | `kubejs/server_scripts/misc.js`; `scripts/mods/Custom/plushies.zs` |
| Village and ocean loot | Adds profession-themed village supplies and restores useful vanilla rewards alongside Beachparty loot. Loot Integrations patches also feed modded structure loot. | Explorer can supply cooks, farmers, builders and mechanics through expeditions. | `kubejs/server_scripts/misc.js`, `kubejs/data/beachparty/`, Loot Integrations addons |
| Hat bags | Four lower bags make a higher rarity bag; epic bags plus themed ingredients make seasonal bags. | Collector has a conversion route, not only random acquisition. | `kubejs/server_scripts/hats.js` |
| Storage upgrades | Revised metal-tier recipes and conversions between Backpack and Storage stack upgrades. A vanilla barrel plus redstone torch can make the Sophisticated barrel. | Quartermaster needs the pack recipes for tiers and cross-system conversions. | `scripts/mods/Compat/stack_upgrade_balance.zs`, `kubejs/server_scripts/misc.js` |
| Create processing | Revised raw iron/gold/copper/zinc/silver processing, ancient debris processing, and a Netherite-sheet/compacting route. Other scripts add renewable processing via compacting, crushing, deploying, haunting, mixing, pressing, washing and polishing. | Mechanic supports Blacksmith and Builder through genuinely pack-specific production chains. | `scripts/mods/Create/ore_processing/`, `scripts/mods/Create/renewables/` |
| Renewable materials | Examples include heated dye/cobblestone mixing into Create stones, shroomlight/dye froglights, water/lava obsidian, superheated gilded blackstone, and haunting charcoal into coal or cobbled deepslate into netherrack. | Building supplies and progression ingredients may have factory alternatives to exploration. | `scripts/mods/Create/renewables/renewables_mixing.zs`, `kubejs/server_scripts/charcoal_haunting.js` |
| Recycling and unification | Listed iron equipment recycles into one ingot through smelting/blasting; Clutter/Spelunkery copper nuggets convert to Create nuggets. White wool can provide string. | Material efficiency and compatibility belong in production notes. | `kubejs/server_scripts/iron_recycling.js`, `copper_nugget.js`, `misc.js` |
| Miscellaneous craftables | Pack scripts cover elytra, saddles, name tags, shiitake mushroom soup, custom computer-themed items, logo and named custom content. | These are additional pack features, not evidence for computer/technology mods. The script appendix preserves every file for later acquisition review. | `scripts/mods/Custom/`, `kubejs/startup_scripts/` |
| Decorative recipes | Coloured presents, daub-frame slabs/stairs, butterfly wings, stone/tuff and related material recipes have pack changes. | Builder and Collector must use actual recipes. | `kubejs/server_scripts/supplementaries_presents.js`, `suppsquared_daub.js`, `scripts/mods/Compat/butterfly_wings.zs`, `stone.zs`, `scripts/mods/Custom/tuff.zs` |
| Explorer's Compass | Custom crafting uses cobwebs and gilded blackstone. | Do not assume the default early-game acquisition route. The pack also has a Create route to gilded blackstone. | `scripts/mods/Compat/explorers_compass.zs` |
| Biome availability | Eroded Borealis and Shattered Glacier are false in canonical BWG world-generation config; Lush Stacks is true. | Use this checkout's settings, not older notes from another profile. New generation and already-generated world terrain can differ. | `config/biomeswevegone/world_generation.json` |
| Structure spacing | Sparse Structures is configured to a 1.2 general factor with a mansion override of 2; KubeJS also has individual structure-set overrides. | Exploration frequency differs from mod defaults; do not promise a fixed search distance. | `config/sparsestructures.json5`, `kubejs/data/*/worldgen/structure_set/` |
| Mob-biome bridges | Tags/modifiers extend selected caravan, creeper, Enderman and other variant spawn contexts into the combined biome pack. | Discovery goals should account for this mixed world; static tag presence is not natural-spawn proof. | `kubejs/data/classic_caravans/`, `creeperoverhaul/`, `endermanoverhaul/`, `variantsandventures/`, `forced_relocation/` |
| Starting roles | Welcome kit exists; Witch, Lumberjack, Archer and Default kit files are in an inactive folder. | Proposed quest identities should not be mistaken for active restricted classes. | `config/starterkit/kits/` |

## How to use the catalogue

First decide which identities deserve top-level paths. Then choose feature families inside each path. Only after that choose actual activities, item requirements and rewards. A mod's primary category is bookkeeping, not a rule that every feature must stay in one chapter.

Examples of crossover projects: a Farmer supplies hops to a Brewer; a Builder makes their tavern; a Mechanic automates ingredient preparation; a Quartermaster organizes stock; a Merchant sells drinks. An Explorer brings home herbs for a Witch, saplings for a Builder and ingredients for a Cook. Those are opportunities for cooperation, not mandatory dependencies that force every player to become a mechanic.

The strongest additional identities are Rancher, Blacksmith and Adventurer because they cover interests that the original eight only partly express. Angler has a clear standalone loop. Merchant and Quartermaster can remain branches until their size and appeal are clearer. A separate Beekeeper, Archaeologist or Photographer would currently be better represented as a branch or collection theme.

## Sources and traceability

Every mod entry retains its exact Packwiz filename, local jar/version, project link when supplied, primary category and crossover paths. The adjacent evidence file preserves the metadata and extracted names. The installed-content appendix exposes all extracted candidate names and biome/structure definitions without silently treating them as obtainable items.

Additional primary sources checked: [Hexalia project](https://www.curseforge.com/minecraft/mc-mods/hexalia), [Tokimi's Toolshed project](https://www.curseforge.com/minecraft/mc-mods/tokimistoolshed), [Create: Dragons Plus project](https://www.curseforge.com/minecraft/mc-mods/create-dragons-plus), [Brewery official wiki](https://team-let-s-do.github.io/Lets-Do-Wiki/docs/brewery/). These supply project context; local assets and scripts determine installed-version scope. Minecraft Guides was checked as an index, but the catalogue does not treat third-party listings as proof of installed features.



## Coverage by primary home

| Home | Mod files |
| --- | ---: |
| Mechanic | 15 |
| Farmer | 12 |
| Cook | 9 |
| Brewer | 4 |
| Witch | 6 |
| Builder | 40 |
| Collector | 5 |
| Explorer | 50 |
| Angler | 1 |
| Rancher | 16 |
| Blacksmith | 12 |
| Adventurer | 13 |
| Merchant | 5 |
| Quartermaster | 13 |
| Shared foundations | 8 |
| Pack customization | 2 |
| Performance and fixes | 31 |
| Visuals and sound | 34 |
| Interface and controls | 40 |
| Compatibility and integrations | 12 |
| Pack and admin tools | 19 |
| Libraries and APIs | 76 |

A mod appears once in the sections below. Crossover references are part of its record and searchable in the HTML catalogue.


## The Mechanic


### Copper Age Backport

**Feature family:** Copper content. **Also serves:** Builder, Blacksmith, Quartermaster, Rancher.

Copper golem and copper chests; copper tools/armor; shelves, lights, chains, bars, bulbs, grates and decorative copper families with oxidation/waxing variants. Divide golem/storage utility, equipment and building palettes by use; verify overlap with the pack's other copper mods in recipes.

**Installed-name examples:** Acacia Shelf, Bamboo Shelf, Birch Shelf, Cherry Shelf, Chiseled Copper, Copper Bars, Copper Bulb, Copper Button, Copper Chain, Copper Chest, Copper Door, Copper Golem Statue, Copper Grate, Copper Lantern, Copper Torch, Copper Trapdoor, Crimson Shelf, Dark Oak Shelf, Exposed Chiseled Copper, Exposed Copper Bars, Exposed Copper Bulb, Exposed Copper Button, Exposed Copper Chain, Exposed Copper Chest, Exposed Copper Door, Exposed Copper Golem Statue, Exposed Copper Grate, Exposed Copper Lantern, Exposed Copper Trapdoor, Exposed Lightning Rod, Jungle Shelf, Mangrove Shelf, Oak Shelf, Oxidized Chiseled Copper, Oxidized Copper Bars, Oxidized Copper Bulb. Full extracted list in the HTML catalogue.

**Version:** 0.1.4. **File:** `mods/backport-copper-age.pw.toml`. [Project page](https://modrinth.com/mod/backport-copper-age).


### Create Cobblestone

**Feature family:** Bulk materials. **Also serves:** Builder.

A rotational-power cobblestone generator provides a compact source for stone-processing lines; connect it to storage and downstream material production.

**Installed-name examples:** Mechanical Generator.

**Version:** 1.5.0+fabric-1.20.1-154. **File:** `mods/create-cobblestone.pw.toml`. [Project page](https://modrinth.com/mod/create-cobblestone).


### Create Crafts & Additions

**Feature family:** Electricity and fuels. **Also serves:** Farmer, Cook.

Connect rotational power to electricity with alternators and motors; distribute and store energy with connectors and accumulators; roll rods and wires. Installed assets also include seed oil, biofuel-related materials, biomass, a Tesla coil and additional food/decorative components. This is an extension of Create, not evidence of a separate large electrical mod ecosystem.

**Installed-name examples:** Accumulator, Alternator, Barbed Wire, Bioethanol, Biomass Pallet, Blaze Burner with Straw, Chocolate Cake, Creative Generator, Digital Adapter, Electric Motor, Electrum Block, Honey Cake, Large Connector, Portable Energy Interface, Redstone Relay, Rolling Mill, Seed Oil, Small Connector, Small Connector With Light, Tesla Coil, Shocked, Baked Cake Base, Biomass, Biomass Pellet, Brass Figurine, Brass Rod, Bronze Rod, Bucket of Biofuel, Bucket of Seed Oil, Cake Base, Capacitor, Copper Goblet, Copper Rod, Copper Spool, Copper Spool with Festive Lights, Copper Wire. Full extracted list in the HTML catalogue.

**Version:** 1.3.4. **File:** `mods/createaddition.pw.toml`. [Project page](https://www.curseforge.com/projects/439890).


### Create Fabric

**Feature family:** Power and production. **Also serves:** Farmer, Cook, Builder, Quartermaster.

Generate and distribute rotational power; manage speed, direction and stress; use shafts, gears, belts and gearboxes. Build presses, mills, crushing wheels, mixers, fans and mechanical crafters; handle items and fluids; assemble moving contraptions and farms; progress into steam power and trains. The pack also adds its own ore processing and renewable-material recipes.

**Installed-name examples:** Acacia Window, Acacia Window Pane, Adjustable Chain Gearshift, Analog Lever, Andesite Bars, Andesite Belt Funnel, Andesite Casing, Andesite Door, Andesite Encased Cogwheel, Andesite Encased Large Cogwheel, Andesite Encased Shaft, Andesite Funnel, Andesite Ladder, Andesite Pillar, Andesite Scaffolding, Andesite Table Cover, Andesite Tunnel, Asurine, Asurine Pillar, Bamboo Window, Bamboo Window Pane, Basin, Belt, Birch Window, Birch Window Pane, Black Nixie Tube, Black Postbox, Black Sail, Black Seat, Black Table Cloth, Black Toolbox, Black Valve Handle, Blaze Burner, Block of Andesite Alloy, Block of Brass, Block of Cardboard. Full extracted list in the HTML catalogue.

**Version:** 6.0.8.1+build.1744-mc1.20.1. **File:** `mods/create-fabric.pw.toml`. [Project page](https://modrinth.com/mod/create-fabric).


### Create Jetpack

**Feature family:** Personal flight. **Also serves:** Explorer.

Craft and use Create-themed jetpack equipment; treat fuel/air requirements and progression as part of transport engineering, with exact installed recipes deciding its entry point.

**Installed-name examples:** Jetpack, Netherite Jetpack, Jetpack Placeable, Netherite Jetpack Placeable.

**Version:** 4.4.2-fabric. **File:** `mods/create-jetpack.pw.toml`. [Project page](https://www.curseforge.com/projects/655608).


### Create Slice & Dice

**Feature family:** Food automation. **Also serves:** Cook, Farmer.

Automate Farmer's Delight ingredient preparation using Create-powered machinery. Teach a working food-production line after players understand the manual kitchen process.

**Installed-name examples:** Fertilizer, Slicer, Sprinkler, Wet Air, Bucket of Liquid Fertilizer.

**Version:** 3.5.2-fabric. **File:** `mods/slice-and-dice.pw.toml`. [Project page](https://www.curseforge.com/projects/659674).


### Create: Bells & Whistles

**Feature family:** Railway fittings. **Also serves:** Builder.

Additional railway and factory decorations and utility fittings; furnish platforms, signals and industrial buildings. A natural extension of a working rail network.

**Installed-name examples:** Andesite Door Step, Andesite Grab Bars, Andesite Pilot, Andesite Steps, Brass Door Step, Brass Grab Bars, Brass Pilot, Brass Steps, Copper Door Step, Copper Grab Bars, Copper Pilot, Copper Steps, Corrugated Metro Casing, Corrugated Metro Panel, Headlight, Metal Pilot, Metro Casing, Metro Panel, Metro Trapdoor, Metro Window, Ornate Iron Trapdoor, Polished Andesite Pilot, Polished Asurine Pilot, Polished Calcite Pilot, Polished Crimsite Pilot, Polished Deepslate Pilot, Polished Diorite Pilot, Polished Dripstone Pilot, Polished Granite Pilot, Polished Limestone Pilot, Polished Ochrum Pilot, Polished Scorchia Pilot, Polished Scoria Pilot, Polished Tuff Pilot, Polished Veridium Pilot, Station Platform.

**Version:** 0.4.5. **File:** `mods/bellsandwhistles.pw.toml`. [Project page](https://www.curseforge.com/projects/905040).


### Create: Connected Fabric

**Feature family:** Machine controls. **Also serves:** Builder, Quartermaster.

Additional gearboxes, cross connectors, brakes, clutches and kinetic batteries; linked buttons and levers; fan catalysts; inventory bridges, access ports, silos and fluid vessels. Copycat parts also support factory construction. Treat these as refinements to practical machines.

**Installed-name examples:** 6-way Gearbox, Andesite Encased Cross Connector, Brake, Brass Encased Cross Connector, Brass Gearbox, Centrifugal Clutch, Copycat Beam, Copycat Block, Copycat Board, Copycat Fence, Copycat Fence Gate, Copycat Slab, Copycat Stairs, Copycat Vertical Step, Copycat Wall, Crank Wheel, Creative Fluid Vessel, Cross Connector, Empty Fan Catalyst, Encased Chain Cogwheel, Fan Blasting Catalyst, Fan Ending Catalyst with Dragon Head, Fan Ending Catalyst with Dragon's Breath, Fan Enriched Catalyst, Fan Freezing Catalyst, Fan Haunting Catalyst, Fan Sanding Catalyst, Fan Seething Catalyst, Fan Smoking Catalyst, Fan Washing Catalyst, Fan Withering Catalyst, Fluid Vessel, Freewheel Clutch, Inventory Access Port, Inventory Bridge, Inverted Clutch. Full extracted list in the HTML catalogue.

**Version:** 1.1.13+patch.1-mc1.20.1. **File:** `mods/create-connected-fabric.pw.toml`. [Project page](https://modrinth.com/mod/create-connected-fabric).


### Create: Curios Jetpack & Backtank

**Feature family:** Wearable integration. **Also serves:** Explorer.

Allows jetpacks and backtanks in an accessory slot. This changes loadout choices but is not a separate machine progression.

**Version:** 1.2.0. **File:** `mods/create-curios-jetpack.pw.toml`. [Project page](https://www.curseforge.com/projects/1057194).


### Create: Dragons Plus

**Feature family:** Create shared features. **Also serves:** Witch, Builder.

A shared library for Dragons Plus addons with player-facing fluid/dye and dragon-breath-related assets, including a fluid hatch. It is not a dragon creature or boss mod. Compatibility dye entries may refer to absent mods; inspect actual recipes before making tasks from them.

**Installed-name examples:** Arts And Crafts Bleached Dye, Black Dye, Blue Dye, Brown Dye, Cyan Dye, Dragon's Breath, Dragon's Breath Cauldron, Dye Depot Amber Dye, Dye Depot Aqua Dye, Dye Depot Beige Dye, Dye Depot Coral Dye, Dye Depot Forest Dye, Dye Depot Ginger Dye, Dye Depot Indigo Dye, Dye Depot Maroon Dye, Dye Depot Mint Dye, Dye Depot Navy Dye, Dye Depot Olive Dye, Dye Depot Rose Dye, Dye Depot Slate Dye, Dye Depot Tan Dye, Dye Depot Teal Dye, Dye Depot Verdant Dye, Fluid Hatch, Gray Dye, Green Dye, Light Blue Dye, Light Gray Dye, Lime Dye, Magenta Dye, Orange Dye, Pink Dye, Purple Dye, Red Dye, White Dye, Yellow Dye. Full extracted list in the HTML catalogue.

**Version:** 1.11.8. **File:** `mods/create-dragons-plus.pw.toml`. [Project page](https://www.curseforge.com/projects/1216624).


### Create: Enchantment Industry

**Feature family:** Experience processing. **Also serves:** Witch, Blacksmith.

Automate experience handling and enchanting-related production with Create. Connect the workshop to equipment upgrading; use the installed disenchanting and printing/enchanting machinery as a distinct factory branch.

**Installed-name examples:** Affix Augmentor, Apotheotic Essence, Blaze Composer, Blaze Enchanter, Blaze Forger, Block of Super Experience, Brass Bookshelf, Classic Blaze Enchanter, Creative Bookshelf, Crystal Essence, Ender Woven Bag, Experience Hatch, Experience Lantern, Gem Cutter, Grindstone Drain, Infused Dragon's Breath, Infuser, Liquid Experience, Mechanical Grindstone, Printer, Apotheotic Affix Template, Apotheotic Essence Bucket, Blaze's Enchanting Handbook, Brass Affix Template, Bucket o' Enchanting, Cake Base o' Enchanting, Cake o' Enchanting, Cake Slice o' Enchanting, Crystal Affix Template, Crystal Essence Bucket, Enchanting Template, Incomplete Apotheotic Affix Template, Incomplete Brass Affix Template, Incomplete Brass Bookshelf, Incomplete Crystal Affix Template, Infused Dragon's Breath Bucket. Full extracted list in the HTML catalogue.

**Version:** 2.5.2-g. **File:** `mods/create-enchantment-industry.pw.toml`. [Project page](https://www.curseforge.com/projects/688768).


### Create: Oxidized

**Feature family:** Copper processing. **Also serves:** Builder.

Adds Create oxidizing recipes, linking copper ageing to repeatable production of building materials.

**Version:** 0.1.1+1.20.1. **File:** `mods/create_oxidized.pw.toml`. [Project page](https://modrinth.com/mod/create_oxidized).


### Create: Steam 'n' Rails

**Feature family:** Railways. **Also serves:** Builder, Explorer.

Expand Create rail construction and train customization; build a railway serving farms, workshops and settlements. Use the installed track and train parts for stations, routes and rolling stock rather than requiring every decorative variant.

**Installed-name examples:** Acacia Train Track, Andesite Track Switch, Ash Train Track, Ashen Train Track, Aspen Train Track, Azalea Train Track, Bamboo Train Track, Baobab Train Track, Big Buffer, Birch Train Track, Black Brass Wrapped Locometal, Black Brass Wrapped Locometal Boiler, Black Brass Wrapped Locometal Smokebox, Black Copper Wrapped Locometal, Black Copper Wrapped Locometal Boiler, Black Copper Wrapped Locometal Smokebox, Black Folding Locometal Door, Black Four Pane Locometal Window, Black Hinged Locometal Door, Black Iron Wrapped Locometal, Black Iron Wrapped Locometal Boiler, Black Iron Wrapped Locometal Smokebox, Black Locometal Boiler, Black Locometal End Ladder, Black Locometal Flywheel, Black Locometal Pillar, Black Locometal Rung Ladder, Black Locometal Smokebox, Black Locometal Trapdoor, Black Locometal Vent, Black on Black Chevron, Black on Black Hazard Stripes, Black on White Chevron, Black on White Hazard Stripes, Black Riveted Locometal, Black Round Pane Locometal Window. Full extracted list in the HTML catalogue.

**Version:** 1.7.3+fabric-mc1.20.1. **File:** `mods/create-steam-n-rails.pw.toml`. [Project page](https://www.curseforge.com/projects/688231).


### Simple Copper Pipes

**Feature family:** Pipes and utilities. **Also serves:** Farmer, Builder.

Copper pipe and fitting systems provide additional physical utility mechanics. Use the installed pipe variants and in-game documentation to establish transport and environmental applications before selecting specific tasks.

**Installed-name examples:** Copper Fitting, Copper Pipe, Exposed Copper Fitting, Exposed Copper Pipe, Oxidized Copper Fitting, Oxidized Copper Pipe, Waxed Copper Fitting, Waxed Copper Pipe, Waxed Exposed Copper Fitting, Waxed Exposed Copper Pipe, Waxed Oxidized Copper Fitting, Waxed Oxidized Copper Pipe, Waxed Weathered Copper Fitting, Waxed Weathered Copper Pipe, Weathered Copper Fitting, Weathered Copper Pipe.

**Version:** 2.0.3. **File:** `mods/simple-copper-pipes.pw.toml`. [Project page](https://www.curseforge.com/projects/571336).


### Wireless Redstone

**Feature family:** Signals. **Also serves:** Builder.

Transmit redstone signals without continuous wiring; create remote controls for doors, farms and machinery.

**Installed-name examples:** P2P Redstone Receiver, P2P Redstone Transmitter, Redstone Receiver, Redstone Transmitter, Circuit, Frequency Sniffer, Frequency Tool, Linker, Remote.

**Version:** 1.2.2+1.20.1. **File:** `mods/wirelessredstone.pw.toml`. [Project page](https://www.curseforge.com/projects/409660).


## The Farmer


### [Let's Do] Farm & Charm

**Feature family:** Working farms. **Also serves:** Cook, Rancher, Builder.

Wild crops and cultivated barley, oat, corn, lettuce, onion, tomato and strawberry; fertilized soil/farmland, compost and fertilizer; sprinklers, silos, scarecrows and farm tools. Also adds troughs, coops, nests, pet feed, carts and plows. Cooking uses a mincer, roaster, cooking pot, pan, stove and crafting bowl, with flour, yeast, pasta and substantial meals.

**Installed-name examples:** Bag of Beetroots, Bag of Carrots, Bag of Corn, Bag of Flour, Bag of Lettuce, Bag of Onions, Bag of Potatoes, Bag of Strawberries, Bag of Tomatoes, Baked Lamb Ham, Barley Bale, Barley Crop, Cat Food Bag, Chicken Coop, Chicken Nest, Cooking Pan, Cooking Pot, Copper Silo, Corn Crop, Crafting Bowl, Dog Food Bag, Farmers Bread, Farmers Breakfast, Feeding Trough, Fertilized Farmland, Fertilized Soil, Grandma's Strawberry Cake, Lettuce Crop, Mincer, Nettle Tea, Oat Bale, Oat Crop, Oat Pancake, Onion Crop, Pet Bowl, Potato with Roast Meat. Full extracted list in the HTML catalogue.

**Version:** 1.0.14. **File:** `mods/lets-do-farm-charm.pw.toml`. [Project page](https://www.curseforge.com/projects/1038103).


### Accelerated Decay

**Feature family:** Forestry support. **Also serves:** Builder.

Leaves decay faster after tree cutting, making timber harvesting and clearing more convenient.

**Version:** 3.0.1+mc1.20.1. **File:** `mods/accelerated-decay.pw.toml`. [Project page](https://www.curseforge.com/projects/699872).


### Crops Love Rain

**Feature family:** Crop growth. **Also serves:** —.

Rain improves crop growth. A farm-management rule to explain alongside watering rather than a separate collectible system.

**Version:** 1.4.0. **File:** `mods/crops-love-rain.pw.toml`. [Project page](https://www.curseforge.com/projects/580294).


### Flower Tweaks

**Feature family:** Plant recipes. **Also serves:** Builder.

Additional crafting routes for flowers and grass; check pack recipes for the exact conversions available.

**Version:** 1. **File:** `mods/flower-tweaks-mod.pw.toml`. [Project page](https://www.curseforge.com/projects/1010566).


### Grass Seeds

**Feature family:** Ground cover. **Also serves:** Builder.

Use wheat seeds to turn dirt into grass and create grass growth; useful for restoring farmyards and landscaping.

**Version:** 3.4. **File:** `mods/grass-seeds.pw.toml`. [Project page](https://www.curseforge.com/projects/345981).


### Harvestable Flowers

**Feature family:** Flower propagation. **Also serves:** Builder, Collector.

Use bone meal on flowers to obtain more flowers; supports dye production and garden collections.

**Version:** 1.1.0+1.20.1. **File:** `mods/harvestable-flowers.pw.toml`. [Project page](https://modrinth.com/mod/harvestable-flowers).


### NiftyCarts

**Feature family:** Farm transport. **Also serves:** Rancher, Explorer, Quartermaster.

Carts support carrying goods, travel and farming; compare them with Farm & Charm's carts so players understand alternative equipment rather than treating the two systems as identical.

**Installed-name examples:** Animal Cart, Hand Cart, Plow, Reaper, Seed Drill, Supply Cart, Wagon, Acacia Animal Cart, Acacia Hand Cart, Acacia Plow, Acacia Reaper, Acacia Seed Drill, Acacia Supply Cart, Acacia Wagon, Add 5 carpets as roof, add chests for storage, Bamboo Animal Cart, Bamboo Hand Cart, Bamboo Plow, Bamboo Reaper, Bamboo Seed Drill, Bamboo Supply Cart, Bamboo Wagon, Birch Animal Cart, Birch Hand Cart, Birch Plow, Birch Reaper, Birch Seed Drill, Birch Supply Cart, Birch Wagon, Can be also controlled from the front seat, Can till the ground, make dirt paths or strip logs, Cherry Animal Cart, Cherry Hand Cart, Cherry Plow, Cherry Reaper, Cherry Seed Drill. Full extracted list in the HTML catalogue.

**Version:** 20.1.5. **File:** `mods/niftycarts.pw.toml`. [Project page](https://www.curseforge.com/projects/900093).


### Panda's Falling Trees

**Feature family:** Forestry. **Also serves:** Builder.

Trees fall when harvested; make forestry a Farmer sub-branch with timber supply, replanting and a sawmill/workshop connection.

**Version:** 0.13.2. **File:** `mods/pandas-falling-trees.pw.toml`. [Project page](https://www.curseforge.com/projects/880630).


### RightClickHarvest

**Feature family:** Harvesting. **Also serves:** —.

Right-click crop harvesting streamlines repeat harvests; teach the configured interaction as part of farm setup.

**Version:** 4.6.1+1.20.1. **File:** `mods/rightclickharvest.pw.toml`. [Project page](https://www.curseforge.com/projects/452834).


### Secure Crops

**Feature family:** Farmland protection. **Also serves:** —.

Prevents trampling of crops/farmland; makes paths and busy farmyards easier to maintain.

**Version:** 2.0.0. **File:** `mods/secure-crops.pw.toml`. [Project page](https://modrinth.com/mod/secure-crops).


### Smarter Farmers (farmers replant)

**Feature family:** Villager farming. **Also serves:** Merchant.

Improved farmer-villager planting/replanting behaviour supports village agriculture and crop supply.

**Version:** 1.20-2.1.2. **File:** `mods/smarter-farmers-farmers-replant.pw.toml`. [Project page](https://www.curseforge.com/projects/491290).


### Universal Bone Meal

**Feature family:** Plant propagation. **Also serves:** Builder.

Extends bone-meal use to additional plants; supports resource renewal, flower gardens and landscaping.

**Version:** 8.0.1. **File:** `mods/universal-bone-meal.pw.toml`. [Project page](https://www.curseforge.com/projects/594013).


## The Cook


### [Let's Do] Candlelight - Farm&Charm Compat

**Feature family:** Dining and hospitality. **Also serves:** Builder, Merchant.

A Farm & Charm-compatible cooking and dining mod, not merely an invisible patch. Prepare additional meals and furnish dining rooms and restaurants with its tableware and furniture.

**Installed-name examples:** Acacia Big Table, Acacia Cabinet, Acacia Chair, Acacia Drawer, Acacia Shelf, Acacia Table, Bamboo Big Table, Bamboo Cabinet, Bamboo Chair, Bamboo Counter, Bamboo Drawer, Bamboo Shelf, Bamboo Sink, Bamboo Stove, Bamboo Table, Basalt Counter, Basalt Sink, Basalt Stove, Beef Wellington, Birch Big Table, Birch Cabinet, Birch Chair, Birch Drawer, Birch Shelf, Birch Table, Bowl, Cabinet, Chair, Cherry Big Table, Cherry Cabinet, Cherry Chair, Cherry Drawer, Cherry Shelf, Cherry Table, Chocolate Box, Cobblestone Counter. Full extracted list in the HTML catalogue.

**Version:** 2.0.5. **File:** `mods/lets-do-candlelight-farm-charm-compat.pw.toml`. [Project page](https://www.curseforge.com/projects/1038117).


### BetterEndDelight

**Feature family:** BetterEnd cuisine. **Also serves:** Explorer, Builder, Farmer.

Use BetterEnd berries, roots, mushrooms, plants and fish in prepared foods; examples include berry juices and cheesecakes, mushroom rice and End fish meals. Adds themed knives, cabinets, crates, bags and petal carpets as supporting kitchen/decor content.

**Installed-name examples:** Amber Root Bag, Black Hydralux Petal Carpet, Blossom Berry Cheesecake, Blossom Berry Crate, Blue Hydralux Petal Carpet, Brown Hydralux Petal Carpet, Chorus Mushroom Bag, Cyan Hydralux Petal Carpet, Dragon Tree Cabinet, End Aloe Vera, End Lotus Cabinet, Gray Hydralux Petal Carpet, Green Hydralux Petal Carpet, Helix Tree Cabinet, Hydralux Petal Carpet, HydraluxPetal Bag, Jellyshroom Cabinet, Lacugrove Cabinet, Light Blue Hydralux Petal Carpet, Light Gray Hydralux Petal Carpet, Lime Hydralux Petal Carpet, Lucernia Cabinet, Lumecorn Rod Crate, Magenta Hydralux Petal Carpet, Mossy Glowshroom Cabinet, Orange Hydralux Petal Carpet, Pink Hydralux Petal Carpet, Purple Hydralux Petal Carpet, Pythadendron Cabinet, Red Hydralux Petal Carpet, Shadow Berry Cheesecake, Shadow Berry Crate, Tenanea Cabinet, Umbrella Tree Cabinet, White Hydralux Petal Carpet, Yellow Hydralux Petal Carpet. Full extracted list in the HTML catalogue.

**Version:** 0.4.0-alpha. **File:** `mods/betterenddelight.pw.toml`. [Project page](https://modrinth.com/mod/betterenddelight).


### End's Delight

**Feature family:** End cuisine. **Also serves:** Explorer, Adventurer.

End-themed ingredients, preparation and meals built around Farmer's Delight. Connect End expeditions with a new culinary branch rather than requiring combat for the first kitchen chapter.

**Installed-name examples:** Chorus Fruit Crate, Chorus Fruit Pie, Chorus Succulent, Dragon Leg with Sauce, Dragon Meat Stew, End Stove, Grilled Shulker, Steamed Dragon Egg, Assorted Salad, Bowl of Dragon Meat Stew, Bowl of Steamed Dragon Egg, Bubble Tea, Chorus Cookie, Chorus Flower Pie, Chorus Flower Tea, Chorus Fruit Grain, Chorus Fruit Milk Tea, Chorus Fruit Popsicle, Chorus Fruit Wine, Chorus Sauce, Dragon Egg Shell, Dragon Egg Shell Knife, Dragon Leg, Dragon Tooth, Dragon Tooth Knife, Dragon's Breath and Chorus Soup, Dragon's Breath Soda, Dried Chorus Flower, Dried Endermite Meat, End Barbecue Stick, End Mixed Salad, End Stone Knife, Ender Bamboo Rice, Ender Congee, Ender Noodle, Ender Pearl Grain. Full extracted list in the HTML catalogue.

**Version:** refabricated-1.20.1-2.5. **File:** `mods/ends-delight.pw.toml`. [Project page](https://www.curseforge.com/projects/662675).


### Expanded Delight

**Feature family:** Expanded ingredients. **Also serves:** Farmer.

Additional crops, ingredients and prepared foods extend Farmer's Delight. The installed mortar and pestle is also a pack-defined manual route to Create flour; it has a configured durability change.

**Installed-name examples:** Asparagus, Asparagus Crate, Chili Pepper Crate, Chili Peppers, Cinnamon Log, Cinnamon Sapling, Deepslate Salt Ore, Juicer, Mortar and Pestle, Peanuts, Salt Ore, Sweet Potato Crate, Sweet Potatoes, Wild Asparagus, Wild Chili Pepper, Wild Peanuts, Wild Sweet Potatoes, Apple Juice, Asparagus Seeds, Asparagus Soup, Baked Sweet Potato, Berry Sweet Roll, Cheese Sandwich, Cheese Slice, Cheese Wheel, Cheesy Asparagus and Bacon, Chili Pepper, Chili Pepper Seeds, Chocolate Cookie, Cinnamon, Cinnamon Apples, Cinnamon Rice, Cinnamon Stick, Creamy Asparagus Soup, Glass Jar, Glow Berry Jelly. Full extracted list in the HTML catalogue.

**Version:** 0.3.2. **File:** `mods/expanded-delight.pw.toml`. [Project page](https://modrinth.com/mod/expanded-delight).


### Farmer's Delight Refabricated

**Feature family:** Kitchen foundations. **Also serves:** Farmer, Builder.

Grow cabbage, tomatoes and onions; gather straw; prepare ingredients with knives and a cutting board; cook meals using the cooking pot and stove. Include dough/pasta, soups, stews, plated meals, feasts, storage and rustic kitchen furnishings. Organic compost and rich soil bridge to farming.

**Installed-name examples:** Acacia Cabinet, Apple Pie, Bag of Rice, Bamboo Cabinet, Basket, Beetroot Crate, Birch Cabinet, Black Canvas Sign, Black Canvas Wall Sign, Black Hanging Canvas Sign, Black Wall Hanging Canvas Sign, Blue Canvas Sign, Blue Canvas Wall Sign, Blue Hanging Canvas Sign, Blue Wall Hanging Canvas Sign, Brown Canvas Sign, Brown Canvas Wall Sign, Brown Hanging Canvas Sign, Brown Mushroom Colony, Brown Wall Hanging Canvas Sign, Budding Tomato Vine, Cabbage, Cabbage Crate, Canvas Rug, Canvas Sign, Canvas Wall Sign, Carrot Crate, Cherry Cabinet, Chocolate Pie, Cooking Pot, Crimson Cabinet, Cutting Board, Cyan Canvas Sign, Cyan Canvas Wall Sign, Cyan Hanging Canvas Sign, Cyan Wall Hanging Canvas Sign. Full extracted list in the HTML catalogue.

**Version:** 1.20.1-2.4.1+refabricated. **File:** `mods/farmers-delight-refabricated.pw.toml`. [Project page](https://www.curseforge.com/projects/993166).


### Farmer's Knives

**Feature family:** Kitchen tools. **Also serves:** Blacksmith.

Adds Farmer's Delight knives in materials from other mods; compare available knife recipes with the actual material progression rather than making every knife mandatory.

**Installed-name examples:** Adamantite Knife, Adamantium Knife, Aeternium Knife, Amethyst Knife, Aquarium Knife, Banglum Knife, Bronze Knife, Carmot Knife, Celestium Knife, Chitin Knife, Cincinnasite Knife, Cincinnasite-Diamond Knife, Copper Knife, Cryomarble Knife, Dragon Knife, Durasteel Knife, Elementium Knife, Emerald Knife, End Knife, Enderite Knife, Fiery Knife, Gilded Netherite Knife, Gobber Knife, Hallowed Knife, Ironwood Knife, Knightmetal Knife, Kyber Knife, Legendary Banglum Knife, Manasteel Knife, Metallurgium Knife, Mythril Knife, Nether Brick Knife, Nether Knife, Nether Ruby Knife, Netherite-Diamond Knife, Netherite-Emerald Knife. Full extracted list in the HTML catalogue.

**Version:** 3.2. **File:** `mods/farmers-knives.pw.toml`. [Project page](https://www.curseforge.com/projects/628972).


### Nature's Delight

**Feature family:** Regional cuisine. **Also serves:** Farmer, Explorer.

Farmer's Delight integration for Nature's Spirit materials and ingredients. Treat it as the culinary use of that world-generation mod's resources.

**Installed-name examples:** Aspen Cabinet, Cedar Cabinet, Coconut Cabinet, Cypress Cabinet, Desert Turnip Crate, Fir Cabinet, Ghaf Cabinet, Joshua Cabinet, Larch Cabinet, Mahogany Cabinet, Manakish, Maple Cabinet, Olive Cabinet, Palo Verde Cabinet, Redwood Cabinet, Saxaul Cabinet, Shiitake Mushroom Colony, Sugi Cabinet, Willow Cabinet, Wisteria Cabinet, Alfredo Pasta, Cocada, Coconut Bread, Coconut Pancakes, Coconut Sauce, Fafaru, Slice of Manakish, Sweet And Savory Saute, Turnip Tagine.

**Version:** 1.12-1.20.1. **File:** `mods/natures-delight.pw.toml`. [Project page](https://www.curseforge.com/projects/1082132).


### Nether's Delight Refabricated

**Feature family:** Nether cuisine. **Also serves:** Farmer, Explorer, Adventurer.

Gather Nether ingredients and prepare themed dishes with Farmer's Delight; include hoglin-related food and Nether plant resources. Acquisition belongs to exploration, cooking the resulting meals belongs here.

**Installed-name examples:** Blackstone Blast Furnace, Blackstone Furnace, Blackstone Stove, Crimson Fungus Colony, Hoglin Trophy, Mimicarnation, Nether Brick Smoker, Propelplant Cane, Propelplant Torch, Rich Soul Soil, Soul Compost, Stuffed Hoglin, Warped Fungus Colony, Diamond Machete, Golden Machete, Grilled Strider, Ground Strider, Hoglin Ear, Hoglin Hide, Hoglin Loin, Hoglin Sirloin, Iron Machete, Magma Gelatin, Nether Skewer, Netherite Machete, Plate of Stuffed Hoglin Ham, Plate of Stuffed Hoglin Roast, Plate of Stuffed Hoglin Snout, Propelpearl, Raw Stuffed Hoglin, Strider Moss Stew, Strider Slice, Warped Moldy Meat.

**Version:** 1.20.1-4.1.1. **File:** `mods/nethers-delight-refabricated.pw.toml`. [Project page](https://www.curseforge.com/projects/998782).


### Ocean's Delight

**Feature family:** Seafood. **Also serves:** Angler.

Prepare foods from ocean creatures; a seafood branch linking fishing and underwater gathering to the kitchen.

**Installed-name examples:** Guardian Soup, Baked Tentacle on a Stick, Bowl of Guardian Soup, Braised Sea Pickle, Cabbage Wrapped Elder Guardian, Cooked Guardian Tail, Cooked Slice of Elder Guardian, Cooked Stuffed Cod, Cut Tentacles, Fugu Roll, Fugu Slice, Guardian, Guardian Tail, Honey Fried Kelp, Roll of Elder Guardian, Seagrass Salad, Slab of Elder Guardian, Slice of Elder Guardian, Squid Rings, Stuffed Cod, Tentacle on a Stick, Tentacles.

**Version:** fdrf-fabric-1.0.2-1.20. **File:** `mods/oceans-delight.pw.toml`. [Project page](https://www.curseforge.com/projects/841262).


## The Brewer


### [Let's Do] Brewery - Farm&Charm Compat

**Feature family:** Beer and spirits. **Also serves:** Farmer, Cook, Builder.

Grow hops and supply grains; dry ingredients; brew beers using wooden, copper and netherite brewing-station assets. The installed version includes named whiskey drinks, beer effects, festival clothing and tavern furniture, plus pub foods. Six beer recipes are explicitly replaced by pack scripts to require the shared hops tag and yeast.

**Installed-name examples:** AK Reserve, Bar Counter, Barley Beer, Beer Mug, Bench, Big Barrel, Brewery Banner, Brewingstation, Cabinet, Carrasconlabel Heritage, Copper Brewingstation, CristelWalker Original, Drawer, Dried Barley, Dried Corn, Dried Oat, Dried Wheat, Dumplings, Fried Chicken, Gingerbread, Haley Beer, Half Chicken, Highland Hearth Signature, Hops Beer, Jameson Malt Whiskey, JoJannik Select, Lilitu Single Malt, MaggoAllan, Aged, Mashed Potatoes, Netherite Brewingstation, Nettle Beer, Oat Beer, Patterned Carpet, Patterned Wool, Pork Knuckle, Potato Salad. Full extracted list in the HTML catalogue.

**Version:** 2.0.6. **File:** `mods/lets-do-brewery-farm-charm-compat.pw.toml`. [Project page](https://www.curseforge.com/projects/1038106).


### [Let's Do] HerbalBrews

**Feature family:** Tea and coffee. **Also serves:** Witch, Farmer, Cook, Builder.

Grow or gather tea, coffee, rooibos, yerba mate, hibiscus and lavender; process tea leaves and brew drinks using kettles and the brewing cauldron. Black, green and oolong teas, floral teas, coffee and milk coffee supply a non-alcoholic drinks branch. Herbal infusions and drink effects cross into the Witch path.

**Installed-name examples:** Bag of Tea Leaves, Black Tea, Black Tea Leaf Block, Brewing Cauldron, Coffee, Coffee Beans, Completionist Banner: Herbal Brews, Copper Tea Kettle, Dried Green Tea Leaf Block, Green Tea, Green Tea Leaf Block, Hibiscus, Hibiscus Tea, Jug, Lavender, Lavender Tea, Milk Coffee, Mixed Tea Leaf Block, Oolong Tea, Oolong Tea Leaf Block, Potted Hibiscus, Potted Lavender, Potted Wild Coffee, Potted Wild Rooibos, Potted Wild Yerba Mate, Rooibos Leaf, Rooibos Tea, Stove, Tea Blossom, Tea Kettle, Wild Coffee, Wild Rooibos, Wild Yerba Mate, Yerba Mate Leaf, Yerba Mate Tea, Balanced. Full extracted list in the HTML catalogue.

**Version:** 1.0.12. **File:** `mods/lets-do-herbal-brews.pw.toml`. [Project page](https://www.curseforge.com/projects/951221).


### [Let's Do] Vinery

**Feature family:** Vineyards and cellars. **Also serves:** Farmer, Builder, Collector.

Collect and cultivate regional red/white grapes; tend fruit trees; press juice and use fermentation barrels to make wines and cider. Wine variants, ageing/storage and a cellar fit here. Racks, bottle storage, latticework, dark-cherry furniture, bags and baskets support vineyards and tasting rooms.

**Installed-name examples:** A Bottle of 'Creepers Crush', A Bottle of 'Mojang Noir', A Bottle of 'Villagers Fright', Acacia Lattice, Acacia Wine Rack, Aegis Wine, Apple Bag, Apple Juice, Apple Leaves, Apple Log, Apple Press, Apple Tree Sapling, Apple Wine, Apple Wood, Bamboo Lattice, Bamboo Wine Rack, Basket, Big Acacia Wine Bottle Storage, Big Bamboo Wine Bottle Storage, Big Birch Wine Bottle Storage, Big Cherry Wine Bottle Storage, Big Dark Cherry Table, Big Dark Cherry Wine Rack, Big Dark Oak Wine Bottle Storage, Big Flower Pot, Big Jungle Wine Bottle Storage, Big Mangrove Wine Bottle Storage, Big Oak Wine Bottle Storage, Big Spruce Wine Bottle Storage, Birch Lattice, Birch Wine Rack, Bolvar Wine, Chenet Wine, Cherry Bag, Cherry Lattice, Cherry Wine. Full extracted list in the HTML catalogue.

**Version:** 1.4.41. **File:** `mods/lets-do-vinery.pw.toml`. [Project page](https://www.curseforge.com/projects/704465).


### AlcoCraft+

**Feature family:** Keg brewing. **Also serves:** Farmer, Builder.

An additional beer system using hops and a keg, separate from Let's Do Brewery. The pack replaces the keg recipe and connects its hops to shared ingredient tags; catalogue its beer varieties as their own brewing method.

**Installed-name examples:** Empty mug, Keg, Mug of Chorus Ale, Mug of Digger Bitter, Mug of Drowned Ale, Mug of Ice Beer, Mug of Kvass, Mug of Leprechaun Cider, Mug of Magnet Pilsner, Mug of Nether Porter, Mug of Nether Star Lager, Mug of Night Rauch, Mug of Sun Pale Ale, Mug of Wither Stout, Frost, Magnetism, Phantomism, Power of Wither, Dry seeds, Hop, Hop seeds.

**Version:** 2.1.1. **File:** `mods/alcocraft.pw.toml`. [Project page](https://modrinth.com/mod/alcocraft).


## The Witch


### Easy Disenchanting

**Feature family:** Enchantment transfer. **Also serves:** Blacksmith.

Transfer enchantments from equipment to books using an anvil; overlaps with other installed enchantment-recovery systems, so explain alternatives.

**Version:** 1.0.1. **File:** `mods/easy-disenchanting.pw.toml`. [Project page](https://www.curseforge.com/projects/1266689).


### Easy Magic

**Feature family:** Enchanting workflow. **Also serves:** Blacksmith.

Enchanting-table interaction improvements, retained items and rerolling; part of learning enchantment choices.

**Version:** 8.0.1. **File:** `mods/easy-magic.pw.toml`. [Project page](https://www.curseforge.com/projects/456239).


### Enchanter Fix

**Feature family:** Enchanting-room construction. **Also serves:** Builder.

Corrects enchantment-power transmission behaviour so decorative table surrounds can function properly.

**Version:** 1.8. **File:** `mods/enchanter-fix.pw.toml`. [Project page](https://modrinth.com/mod/enchanter-fix).


### Grind enchantments

**Feature family:** Grindstone processing. **Also serves:** Blacksmith.

Adds grindstone enchantment operations; compare its available recipes to anvil transfer and Create automation before selecting a preferred learning route.

**Version:** 3.1.4+1.20.1. **File:** `mods/grind-enchantments.pw.toml`. [Project page](https://www.curseforge.com/projects/379680).


### Hexalia

**Feature family:** Herbal witchcraft. **Also serves:** Farmer, Rancher, Cook, Explorer, Blacksmith, Builder.

Gather magical herbs and cultivate special crops; refine ingredients with a mortar and pestle; use the small cauldron and ladle for brews and salves. Ritual tables/braziers, elemental nodes, infused farmland and enchanted plants form a deeper ritual branch. Silk moths and silkworms supply fibres for garments; idols, pendants, magical tools, weapons, a censer and dreamcatcher provide practical rewards. The pack adds athame cutting-board recipes for tree resin.

**Installed-name examples:** Aegiflora, Astrylis, Begonia, Candle Skull, Celestial Bloom, Celestial Crystal Block, Censer, Chillberry Bush, Cottonwood Button, Cottonwood Catkin, Cottonwood Door, Cottonwood Fence, Cottonwood Fence Gate, Cottonwood Hanging Sign, Cottonwood Leaves, Cottonwood Log, Cottonwood Planks, Cottonwood Pressure Plate, Cottonwood Sapling, Cottonwood Sign, Cottonwood Slab, Cottonwood Stairs, Cottonwood Trapdoor, Cottonwood Wood, Dahlia, Dreamcatcher, Dreamshroom, Egg Cluster, Galeberries Vine, Galeberries Vine Plant, Ghost Fern, Grimshade, Infused Dirt, Infused Farmland, Lavender, Lotus Flower. Full extracted list in the HTML catalogue.

**Version:** 1.3.5-1.20.1+fabric. **File:** `mods/hexalia.pw.toml`. [Project page](https://www.curseforge.com/projects/962878).


### Things [Fabric]

**Feature family:** Trinkets and utilities. **Also serves:** Collector, Explorer, Blacksmith, Quartermaster.

Craft utility accessories and magical equipment, including mining/movement aids, item magnets, recall/displacement tools, ender storage and the Bater Wucket. The Things Almanac is the learning entry point. Pack tags integrate the Bater Wucket into several food and drink systems.

**Installed-name examples:** Deepslate Gleaming Ore, Deepslate Glowstone Fixture, Diamond Pressure Plate, Gleaming Ore, Quartz Glowstone Fixture, Stone Glowstone Fixture, Momentum, Retribution, Agglomeration, Arm Extender, Bater Wucket, Broken Watch, Container Key, Displacement Page, Displacement Tome, Empty Agglomeration, Enchanted Wax Gland, Ender Pouch, Gleaming Compound, Gleaming Powder, Hades Crystal, Hardening Catalyst, Infernal Scepter, Item Magnet, Luck of the Irish, Mining Glove, Monocle, Mossy Necklace, Placebo, Rabbit Foot Charm, Recall Potion, Riot Gauntlet, Shock Absorber, Socks, Things Almanac.

**Version:** 0.3.3+1.20. **File:** `mods/things-fabric.pw.toml`. [Project page](https://www.curseforge.com/projects/456151).


## The Builder


### [Let's Do] Beachparty

**Feature family:** Beach leisure. **Also serves:** Brewer, Explorer, Collector.

Beach furniture, sandcastles, cocktails and seaside leisure items. Drinks belong to Brewer; creating a beach resort belongs to Builder. The pack disables five rubber-ring items and customizes ocean loot, so avoid a blanket collect-every-item objective.

**Installed-name examples:**  Palm Chair, Beach Chair, Beach Goal, Beach Parasol, Beach Sun Lounger, Beach Towel, Cocoa Cocktail, Coconut, Coconut Cocktail, Completionist Banner: Beachparty, Empty Sand Bucket, Filled Sand Bucket, Hanging Coconut, Honey Cocktail, Hooded Beach Chair, Melon Cocktail, Message in a Bottle, Mini Fridge, Palm Bar, Palm Bar Stool, Palm Button, Palm Cabinet, Palm Door, Palm Fence, Palm Fence Gate, Palm Floorboard, Palm Glass, Palm Glass Pane, Palm Hanging Sign, Palm Leaves, Palm Log, Palm Planks, Palm Pressure Plate, Palm Sign, Palm Slab, Palm Sprout. Full extracted list in the HTML catalogue.

**Version:** 2.0.3. **File:** `mods/lets-do-beachparty.pw.toml`. [Project page](https://www.curseforge.com/projects/858691).


### Amendments

**Feature family:** Vanilla block interactions. **Also serves:** Cook, Mechanic.

Additional practical and decorative interactions for familiar blocks. Include as building and household tips; use installed interactions rather than assuming all features from newer releases.

**Installed-name examples:** Carpet Slab, Carpet Stairs, Directional Cake, Double Cake, Dye Cauldron, Hanging Flower Pot, Liquid Cauldron, Skull Pile, Tool Hook, Wall Lantern, Dragon Fireball, Fireball, Dragon Charge, Dye Bottle.

**Version:** 1.20-2.2.6. **File:** `mods/amendments.pw.toml`. [Project page](https://www.curseforge.com/projects/896746).


### Armor Statues

**Feature family:** Display figures. **Also serves:** Collector.

Pose and customize armor stands for displays, shops, storytelling and equipment galleries.

**Version:** 8.0.6. **File:** `mods/armor-statues.pw.toml`. [Project page](https://www.curseforge.com/projects/682566).


### Beautify: Refabricated

**Feature family:** Interior decoration. **Also serves:** Farmer.

House and garden decorations, including hanging pots and decorative fittings, extend room and garden design.

**Installed-name examples:** Acacia Blinds, Acacia Lattice, Acacia Picture Frame, Bamboo Lamp, Birch Blinds, Birch Lattice, Birch Picture Frame, Black Candelabra, Blue Candelabra, Bookstack, Botanist Workbench, Brown Candelabra, Candelabra, Cherry Blinds, Cherry Lattice, Cherry Picture Frame, Crimson Blinds, Crimson Lattice, Crimson Picture Frame, Cyan Candelabra, Dark Oak Blinds, Dark Oak Lattice, Dark Oak Picture Frame, Glowstone Essence Lamp, Gray Candelabra, Green Candelabra, Hanging Pot, Iron Blinds, Jungle Blinds, Jungle Lattice, Jungle Picture Frame, Light Blue Candelabra, Light Bulb, Light Gray Candelabra, Lime Candelabra, Magenta Candelabra. Full extracted list in the HTML catalogue.

**Version:** 2.0.0+1.20.1. **File:** `mods/beautify-refabricated.pw.toml`. [Project page](https://www.curseforge.com/projects/809311).


### Chipped

**Feature family:** Block palettes. **Also serves:** —.

Large families of decorative block variants organized through themed workstations. Use masonry, carpentry, glass, textiles and other palette projects as chapters; requiring every recolour would overwhelm the Builder path.

**Installed-name examples:** Acacia Barrel, Acacia Crate, Acacia Planks Mosaic, Acacia Planks Panel, Acacia Planks Shavings, Acacia Torch, Ad Astra Ochre Froglight, Ad Astra Pearlescent Froglight, Ad Astra Verdant Froglight, Airy Birch Trapdoor, Airy Crimson Trapdoor, Airy Dark Oak Trapdoor, Airy Jungle Trapdoor, Airy Mangrove Trapdoor, Airy Oak Trapdoor, Airy Spruce Trapdoor, Airy Warped Trapdoor, Alchemy Bench, Amethyst Block Bricks, Amethyst Block Mini Tiles, Amethyst Block Pillar, Amethyst Block Pillar Top, Amethyst Block Scales, Ancient Cubed Oak Bookshelf, Ancient Debris Bricks, Ancient Debris Mini Tiles, Ancient Debris Pillar, Ancient Debris Pillar Top, Ancient Debris Scales, Ancient Diamond Block, Ancient Emerald Block, Ancient Gold Block, Ancient Iron Block, Ancient Oak Bookshelf, Ancient Oak Large Bookshelf, Ancient Ochre Froglight. Full extracted list in the HTML catalogue.

**Version:** 3.0.7. **File:** `mods/chipped.pw.toml`. [Project page](https://www.curseforge.com/projects/456956).


### Clutter

**Feature family:** Mixed homestead content. **Also serves:** Rancher, Farmer, Brewer, Collector, Explorer, Blacksmith.

A broad content mod: furniture, lighting, shelves, benches, chimneys, decorative metals and corals; plants and hops; creatures including Mossbloom; wearable/collectible items and other materials. Its mixed scope should be split by feature. Red/yellow polypores are disabled; copper nuggets are unified with Create; butterfly wings have a pack recipe.

**Installed-name examples:** Giant Redwood Forest, Lupine Fields, Acacia Bench, Acacia Chair, Acacia Cupboard, Acacia Mosaic, Acacia Mosaic Slab, Acacia Mosaic Stairs, Acacia Shelf, Acacia Short Bench, Acacia Table, Acacia Trellis, Acacia Wall Bookshelf, Acacia Wall Cupboard, Acacia Window Sill, Anchor, Anchor Coral, Anchor Coral Block, Anchor Coral Fan, Andesite Chimney, Apple Food Box, Aquatic Torch, Bamboo Bench, Bamboo Chair, Bamboo Cupboard, Bamboo Shelf, Bamboo Short Bench, Bamboo Table, Bamboo Trellis, Bamboo Wall Bookshelf, Bamboo Wall Cupboard, Bamboo Window Sill, Basalt Sulphur Ore, Beetroot Food Box, Birch Bench, Birch Chair. Full extracted list in the HTML catalogue.

**Version:** 1.20-0.6.2. **File:** `mods/clutter.pw.toml`. [Project page](https://www.curseforge.com/projects/826060).


### Cluttered

**Feature family:** Decorative objects. **Also serves:** Collector.

A distinct decoration mod from Clutter, providing decorative household objects and furniture. Keep its item list separate so similarly named mods are not accidentally merged.

**Installed-name examples:** Amethyst Endtable, Analog Kitchen Scale, Anchor Wallpaper, Anchor Wallpaper Wainscoting, Ancient Codex, Angry Bee Lamp, Antique Book Stand, Antique Lamp, Antique Library Books, Antique Map, Antique Sewing Machine, Apple Chair, Art Academy Box Of Paint, Assorted Jam Jars, Baking Set A, Bamboo Bookshelf, Basic Lovely Love Seat, Bee Balm, Bee Lamp, Berry Cake, Black Armchair, Black Cabinet, Black Cat Armchair, Black Cat Garland, Black Cat Plant Pot, Black Cat Purple Bookshelf, Black Counter, Black Endtable, Black Glass Cabinet, Black Inner Corner Cabinet, Black Inner Corner Counter, Black Left Outer Corner Counter, Black Lovely Love Seat, Black Mini Cabinet, Black Outer Corner Cabinet, Black Retro Fridge. Full extracted list in the HTML catalogue.

**Version:** 2.1.0+1.20.1. **File:** `mods/cluttered.pw.toml`. [Project page](https://www.curseforge.com/projects/826308).


### Construction Wand (Fabric)

**Feature family:** Building tools. **Also serves:** —.

Wands place groups of blocks to extend structures; a practical construction-tool progression using available wand upgrades.

**Installed-name examples:** Angel Wand Core, Destruction Wand Core, Diamond Wand, Infinity Wand, Iron Wand, Stone Wand.

**Version:** 2.1.3. **File:** `mods/construction-wand-fabric.pw.toml`. [Project page](https://www.curseforge.com/projects/1035665).


### Create Deco Fabric

**Feature family:** Industrial architecture. **Also serves:** Mechanic.

Factory-themed building blocks and decorative details for workshops, rail yards and streets.

**Installed-name examples:** Andesite Bars, Andesite Bars Overlay, Andesite Catwalk, Andesite Catwalk Railing, Andesite Catwalk Stairs, Andesite Door, Andesite Facade, Andesite Mesh Fence, Andesite Sheet Metal, Andesite Support, Andesite Support Wedge, Andesite Train Hull, Andesite Trapdoor, Andesite Window, Andesite Window Pane, Black Placard, Black Shipping Container, Blue Andesite Cage Lamp, Blue Brass Cage Lamp, Blue Brick Slab, Blue Brick Stairs, Blue Brick Wall, Blue Bricks, Blue Copper Cage Lamp, Blue Industrial Iron Cage Lamp, Blue Iron Cage Lamp, Blue Placard, Blue Shipping Container, Blue Zinc Cage Lamp, Brass Bars, Brass Bars Overlay, Brass Catwalk, Brass Catwalk Railing, Brass Catwalk Stairs, Brass Door, Brass Facade. Full extracted list in the HTML catalogue.

**Version:** 2.1.1-1.20.1-fabric. **File:** `mods/create-deco-fabric.pw.toml`. [Project page](https://www.curseforge.com/projects/739872).


### Create: Copycats+

**Feature family:** Custom shapes. **Also serves:** Mechanic.

Apply building materials to copycat shapes: slopes, layers, beams, panels, stairs, walls, fences, doors and industrial parts. Build detailed structures and disguise machinery. Pack files also contain Copycats recipe-advancement fixes.

**Installed-name examples:** Copycat Base, Copycat Beam, Copycat Block, Copycat Board, Copycat Byte, Copycat Byte Panel, Copycat Cogwheel, Copycat Corner Slice, Copycat Door, Copycat Fence, Copycat Fence Gate, Copycat Flat Pane, Copycat Fluid Pipe, Copycat Folding Door, Copycat Ghost Block, Copycat Glass Fluid Pipe, Copycat Half Layer, Copycat Half Panel, Copycat Heavy Weighted Pressure Plate, Copycat Iron Door, Copycat Iron Trapdoor, Copycat Ladder, Copycat Large Cogwheel, Copycat Layer, Copycat Light Weighted Pressure Plate, Copycat Pane, Copycat Shaft, Copycat Slab, Copycat Slice, Copycat Sliding Door, Copycat Slope, Copycat Slope Layer, Copycat Stacked Half Layer, Copycat Stairs, Copycat Stone Button, Copycat Stone Pressure Plate. Full extracted list in the HTML catalogue.

**Version:** 3.0.8+mc.1.20.1-fabric. **File:** `mods/copycats.pw.toml`. [Project page](https://www.curseforge.com/projects/968398).


### Create: Interiors

**Feature family:** Vehicle interiors. **Also serves:** Mechanic.

Furniture intended to fit Create builds and contraptions; furnish passenger carriages and usable vehicle interiors.

**Installed-name examples:** Black Chair, Black Cushion, Black Floor Chair, Blue Chair, Blue Cushion, Blue Floor Chair, Brown Chair, Brown Cushion, Brown Floor Chair, Cyan Chair, Cyan Cushion, Cyan Floor Chair, Gray Chair, Gray Cushion, Gray Floor Chair, Green Chair, Green Cushion, Green Floor Chair, Kelp Chair, Kelp Floor Chair, Kelp Seat, Light Blue Chair, Light Blue Cushion, Light Blue Floor Chair, Light Gray Chair, Light Gray Cushion, Light Gray Floor Chair, Lime Chair, Lime Cushion, Lime Floor Chair, Magenta Chair, Magenta Cushion, Magenta Floor Chair, Orange Chair, Orange Cushion, Orange Floor Chair. Full extracted list in the HTML catalogue.

**Version:** 0.6.0. **File:** `mods/interiors.pw.toml`. [Project page](https://www.curseforge.com/projects/906239).


### Dark Paintings

**Feature family:** Art displays. **Also serves:** Collector.

Additional painting designs extend galleries and wall decoration.

**Version:** 17.0.6. **File:** `mods/dark-paintings.pw.toml`. [Project page](https://www.curseforge.com/projects/377281).


### Decorative Lamps

**Feature family:** Lighting. **Also serves:** —.

Additional decorative lamps for interior and exterior lighting schemes.

**Installed-name examples:** Black Ceiling Lamp, Black Ceiling Lamp (Wide Cap), Black Ceiling Lamp (Wide), Black Floor Lamp, Black Lattice Wall Lamp, Black Night Light, Black Paper Lantern, Black Pendant Lamp, Black Umbrella Lamp, Black Umbrella Wall Lamp, Blue Ceiling Lamp, Blue Ceiling Lamp (Wide Cap), Blue Ceiling Lamp (Wide), Blue Floor Lamp, Blue Lattice Wall Lamp, Blue Night Light, Blue Paper Lantern, Blue Pendant Lamp, Blue Umbrella Lamp, Blue Umbrella Wall Lamp, Brown Ceiling Lamp, Brown Ceiling Lamp (Wide Cap), Brown Ceiling Lamp (Wide), Brown Floor Lamp, Brown Lattice Wall Lamp, Brown Night Light, Brown Paper Lantern, Brown Pendant Lamp, Brown Umbrella Lamp, Brown Umbrella Wall Lamp, Copper Candle Holder, Copper Chandelier, Cyan Ceiling Lamp, Cyan Ceiling Lamp (Wide Cap), Cyan Ceiling Lamp (Wide), Cyan Floor Lamp. Full extracted list in the HTML catalogue.

**Version:** 1.20.1-1.7.4. **File:** `mods/decorative-lamps.pw.toml`. [Project page](https://modrinth.com/mod/decorative-lamps).


### Diagonal Walls

**Feature family:** Building connections. **Also serves:** —.

Walls connect diagonally, improving angled boundaries and architectural shapes.

**Version:** 8.0.4. **File:** `mods/diagonal-walls.pw.toml`. [Project page](https://www.curseforge.com/projects/969422).


### Diagonal Windows

**Feature family:** Building connections. **Also serves:** —.

Window connections work diagonally, supporting angled glass structures.

**Version:** 8.1.5. **File:** `mods/diagonal-windows.pw.toml`. [Project page](https://www.curseforge.com/projects/891328).


### Double Doors

**Feature family:** Door behaviour. **Also serves:** —.

Paired doors, trapdoors and gates can open together; a convenience rule for entrances and barns.

**Version:** 7.2. **File:** `mods/double-doors.pw.toml`. [Project page](https://www.curseforge.com/projects/348831).


### Dusty Decorations

**Feature family:** Lived-in details. **Also serves:** Cook, Collector.

Decorative props for detailed rooms and workshops. The pack fixes the cooking-pot block's drop; its kitchen appearance alone should not be treated as proof of a functional cooking system.

**Installed-name examples:** Acacia Chair, Acacia Shelf, Anchor, Apple Barrel, Bamboo Chair, Bamboo Shelf, Beetroot Barrel, Big Bowl, Birch Chair, Birch Shelf, Black Wool Awning, Blue Wool Awning, Book Stack, Books, Brown Wool Awning, Carrot Barrel, Cherry Chair, Cherry Shelf, Cluttered Shelf, Cod Barrel, Coiled Rope, Cooking Pot, Corrugated Metal, Corrugated Metal Awning, Crimson Chair, Crimson Shelf, Cutting Board, Cyan Wool Awning, Dark Oak Chair, Dark Oak Shelf, Empty Barrel, Frying Pan, Glass Buoy, Globe, Glow Berries Barrel, Gray Wool Awning. Full extracted list in the HTML catalogue.

**Version:** 1.1-1.20.1+1.20.2. **File:** `mods/dusty-decorations.pw.toml`. [Project page](https://www.curseforge.com/projects/843344).


### Fairy Lights (Fabric)

**Feature family:** String lights. **Also serves:** —.

Decorative string-light layouts for gardens, festivals, taverns and homes.

**Installed-name examples:** Candle Lantern, Candle Lantern Light, Connection Fastener, Fairy Light, Flower Light, Ghost Light, Heart Light, Icicle Lights, Incandescent Light, Jack o'Lantern, Meteor Light, Moon Light, Oil Lantern, Oil Lantern Light, Orb Lantern, Paper Lantern, Skull Light, Snowflake Light, Spider Light, Star Light, Witch Light, Fastener, Black String, Hanging Lights, Letter Bunting, Pennant Bunting, Spearhead Pennant, Square Pennant, Swallowtail Pennant, Tinsel Garland, Triangle Pennant, Twinkles, Vine Garland, White String.

**Version:** 1.1.5_fabric. **File:** `mods/fairy-lights-fabric.pw.toml`. [Project page](https://www.curseforge.com/projects/1510773).


### Fetzi's Asian Decoration

**Feature family:** Themed architecture. **Also serves:** —.

Asian-inspired decorative blocks and details support a distinct architectural style branch.

**Installed-name examples:** Acacia Fence, Acacia Fence Extension, Acacia Fence Gate, Acacia Handrail, Acacia Katana Stand, Acacia Panel, Acacia Shoji Door (2x5), Acacia Shoji Door (3x5), Acacia Shoji Door (4x5), Acacia Shoji Trapdoor (2x3), Acacia Shoji Trapdoor (3x3), Acacia Shoji Trapdoor (4x3), Acacia Shoji Wall (2x3), Acacia Shoji Wall (3x3), Acacia Shoji Wall (4x3), Andesite Handrail, Bamboo Fence, Bamboo Fence Extension, Bamboo Fence Gate, Bamboo Handrail, Bamboo Katana Stand, Bamboo Panel, Bamboo Shoji Door (2x5), Bamboo Shoji Door (3x5), Bamboo Shoji Door (4x5), Bamboo Shoji Trapdoor (2x3), Bamboo Shoji Trapdoor (3x3), Bamboo Shoji Trapdoor (4x3), Bamboo Shoji Wall (2x3), Bamboo Shoji Wall (3x3), Bamboo Shoji Wall (4x3), Birch Fence, Birch Fence Extension, Birch Fence Gate, Birch Handrail, Birch Katana Stand. Full extracted list in the HTML catalogue.

**Version:** 1.8.2. **File:** `mods/fetzis-asian-decoration.pw.toml`. [Project page](https://www.curseforge.com/projects/678856).


### FroglightsReimagined

**Feature family:** Lighting materials. **Also serves:** Rancher.

Additional froglight colours, shapes and crafting uses; connect the material source to animal-related gameplay where appropriate.

**Installed-name examples:** Alabaster Froglight, Alabaster Froglight Lantern, Ametrine Froglight, Ametrine Froglight Lantern, Ashen Froglight, Ashen Froglight Lantern, Aureate Froglight, Aureate Froglight Lantern, Azure Froglight, Azure Froglight Lantern, Carmine Froglight, Carmine Froglight Lantern, Cerulean Froglight, Cerulean Froglight Lantern, Citrine Froglight, Citrine Froglight Lantern, Emberglow Froglight, Emberglow Froglight Lantern, Frostveil Froglight, Frostveil Froglight Lantern, Fuchsia Froglight, Fuchsia Froglight Lantern, Obsidian Froglight, Obsidian Froglight Lantern, Pewter Froglight, Pewter Froglight Lantern, Roseate Froglight, Roseate Froglight Lantern, Sylvan Froglight, Sylvan Froglight Lantern, Umber Froglight, Umber Froglight Lantern.

**Version:** 0.3-1.20.1. **File:** `mods/froglightsreimagined.pw.toml`. [Project page](https://www.curseforge.com/projects/1361021).


### Handcrafted

**Feature family:** Home interiors. **Also serves:** —.

Furniture and household decorations for furnished bedrooms, living rooms, kitchens and workspaces; make room-building projects rather than a furniture checklist alone.

**Installed-name examples:** Acacia Bench, Acacia Chair, Acacia Corner Trim, Acacia Couch, Acacia Counter, Acacia Cupboard, Acacia Desk, Acacia Dining Bench, Acacia Drawer, Acacia Fancy Bed, Acacia Nightstand, Acacia Pillar Trim, Acacia Shelf, Acacia Side Table, Acacia Table, Andesite Corner Trim, Andesite Pillar Trim, Bamboo Bench, Bamboo Chair, Bamboo Corner Trim, Bamboo Couch, Bamboo Counter, Bamboo Cupboard, Bamboo Desk, Bamboo Dining Bench, Bamboo Drawer, Bamboo Fancy Bed, Bamboo Nightstand, Bamboo Pillar Trim, Bamboo Shelf, Bamboo Side Table, Bamboo Table, Bear Trophy, Bench, Berry Jam Jar, Birch Bench. Full extracted list in the HTML catalogue.

**Version:** 3.0.6. **File:** `mods/handcrafted.pw.toml`. [Project page](https://www.curseforge.com/projects/538214).


### Hearth & Home

**Feature family:** Architectural materials. **Also serves:** —.

Additional warm domestic building materials, including glass and structural finishes, for houses and settlements.

**Installed-name examples:** Acacia Lattice, Acacia Parquet, Acacia Sanded Wood, Acacia Trim, Acacia Vertical Trim, Andesite Chimney, Bamboo Lattice, Bamboo Mat, Bamboo Parquet, Bamboo Sanded Wood, Bamboo Trim, Bamboo Vertical Trim, Barred Glass, Barred Glass Pane, Birch Lattice, Birch Parquet, Birch Sanded Wood, Birch Trim, Birch Vertical Trim, Black Paper Lantern, Black Shingle Slab, Black Shingle Stairs, Black Shingles, Black Stained Barred Glass, Black Stained Barred Glass Pane, Black Terracotta Brick Slab, Black Terracotta Brick Stairs, Black Terracotta Bricks, Black Terracotta Mosaic, Black Tile Slab, Black Tiles, Blackstone Chimney, Blue Paper Lantern, Blue Shingle Slab, Blue Shingle Stairs, Blue Shingles. Full extracted list in the HTML catalogue.

**Version:** 1.20.1-2.0.3. **File:** `mods/hearth-and-home.pw.toml`. [Project page](https://www.curseforge.com/projects/849364).


### Immersive Furniture

**Feature family:** Custom furniture. **Also serves:** —.

Create custom furniture and objects in-game or use designs from its library; supports bespoke interiors beyond fixed crafting variants.

**Installed-name examples:** Artisan's Workstation, Crafting Material.

**Version:** 0.3.3+1.20.1. **File:** `mods/immersive-furniture.pw.toml`. [Project page](https://www.curseforge.com/projects/1283531).


### Just Outdoor Stuffs

**Feature family:** Outdoor furniture. **Also serves:** Farmer.

Furniture and decorative objects for gardens, patios and outdoor spaces.

**Installed-name examples:** Bags of Fertilizers, BBQ Grill, Bird Bath, Black Modern Patio Planter, Checkers Set, Garden Bench, Garden Chair, Garden Flamingo, Garden Gnome, Garden Gnome with Pitchfork, Garden Gnome with Shovel, Garden Hoes, Garden Hose, Garden Pitchforks, Garden Planter, Garden Rakes, Garden Shovels, Garden Spades, Garden Stool, Gardening Tools, Gardening Tools in a Bucket, Glass Patio Coffee Table, Iron Patio Bench, Iron Patio Chair, Iron Patio Planter, Iron Patio Rocking Chair, Iron Patio Stool, Large Garden Table, Large Iron Patio Table, Lawn Mower, Patio Armchair, Patio Bench, Patio Coffee Table, Patio Lounge Chair, Patio Side Table, Patio Sofa Chaise Section. Full extracted list in the HTML catalogue.

**Version:** 1.0.2. **File:** `mods/just-outdoor-stuffs.pw.toml`. [Project page](https://www.curseforge.com/projects/896219).


### Macaw's Holidays

**Feature family:** Seasonal decorations. **Also serves:** Collector.

Christmas and Halloween decorations for themed builds and seasonal display collections.

**Installed-name examples:** Awakened Bat, Bat Doormat, Bat Wall Deco, Bat Wall Deco 2, Bat Wall Deco 3, Bell Wall Deco 1, Bell Wall Deco 2, Bell Wall Deco 3, Bell Wall Deco 4, Bells Wall Deco 1, Bells Wall Deco 2, Big Blue Present, Big Cyan Present, Big Dark Blue Present, Big Green Present, Big Magenta Present, Big Purple Present, Big Red Present, Big Yellow Present, Black Balloon, Blue Candy Cane Block, Blue Candy Cane Slab, Blue Candy Cane Slim, Blue Candy Cane Stairs, Blue Cube String Lights, Blue Decorated Christmas Tree Base, Blue Decorated Christmas Tree Bottom, Blue Decorated Christmas Tree Middle, Blue Decorated Christmas Tree Top, Blue Garland Wall Deco 1, Blue Garland Wall Deco 2, Blue Ornament, Blue Ornament Wall Deco 1, Blue Ornament Wall Deco 2, Blue Present, Blue Stocking. Full extracted list in the HTML catalogue.

**Version:** 1.1.2. **File:** `mods/macaws-holidays.pw.toml`. [Project page](https://www.curseforge.com/projects/930232).


### Macaw's Paintings

**Feature family:** Art displays. **Also serves:** Collector.

Additional paintings for galleries and interiors; collection completion is optional, decorating with them is the core building activity.

**Version:** 1.1.0. **File:** `mods/macaws-paintings.pw.toml`. [Project page](https://www.curseforge.com/projects/438116).


### Macaw's Paths and Pavings

**Feature family:** Roads and paving. **Also serves:** Explorer.

Additional path and paving materials for gardens, settlements and roads linking player bases.

**Installed-name examples:** Acacia Planks Path, Andesite Basket Weave Paving, Andesite Clover Paving, Andesite Crystal Floor, Andesite Crystal Floor Path, Andesite Crystal Floor Slab, Andesite Crystal Floor Stairs, Andesite Diamond Paving, Andesite Dumble Paving, Andesite Flagstone, Andesite Flagstone Path, Andesite Flagstone Slab, Andesite Flagstone Stairs, Andesite Honeycomb Paving, Andesite Running Bond, Andesite Running Bond Path, Andesite Running Bond Slab, Andesite Running Bond Stairs, Andesite Square Paving, Andesite Strewn Rocky Path, Andesite Windmill Weave, Andesite Windmill Weave Path, Andesite Windmill Weave Slab, Andesite Windmill Weave Stairs, Bamboo Planks Path, Birch Planks Path, Blackstone Basket Weave Paving, Blackstone Clover Paving, Blackstone Crystal Floor, Blackstone Crystal Floor Path, Blackstone Crystal Floor Slab, Blackstone Crystal Floor Stairs, Blackstone Diamond Paving, Blackstone Dumble Paving, Blackstone Flagstone, Blackstone Flagstone Path. Full extracted list in the HTML catalogue.

**Version:** 1.1.2. **File:** `mods/macaws-paths-and-pavings.pw.toml`. [Project page](https://www.curseforge.com/projects/629153).


### Macaw's Windows

**Feature family:** Windows and glazing. **Also serves:** —.

Window styles, mosaic glass, blinds and arrow slits for architectural detailing.

**Installed-name examples:** Acacia Blinds, Acacia Curtain Rod, Acacia Four Pane Window, Acacia Louvered Shutter, Acacia Pane Window, Acacia Parapet, Acacia Planks Four Pane Window, Acacia Planks Pane Window, Acacia Planks Parapet, Acacia Shutter, Andesite Four Pane Window, Andesite Louvered Shutter, Andesite Pane Window, Andesite Parapet, Bamboo Shutter, Birch Blinds, Birch Curtain Rod, Birch Four Pane Window, Birch Louvered Shutter, Birch Pane Window, Birch Parapet, Birch Planks Four Pane Window, Birch Planks Pane Window, Birch Planks Parapet, Birch Shutter, Black Curtain, Black Mosaic Glass, Black Mosaic Glass Pane, Blackstone Brick Arrow Slit, Blackstone Four Pane Window, Blackstone Gothic Window, Blackstone Pane Window, Blackstone Parapet, Blue Curtain, Blue Mosaic Glass, Blue Mosaic Glass Pane. Full extracted list in the HTML catalogue.

**Version:** 2.4.2. **File:** `mods/macaws-windows.pw.toml`. [Project page](https://www.curseforge.com/projects/363569).


### MasterCutter

**Feature family:** Material conversion. **Also serves:** Blacksmith.

Expands stonecutter recipes, including woodcutting, recycling and reverse conversions; supports efficient material preparation.

**Version:** 1.1. **File:** `mods/mastercutter.pw.toml`. [Project page](https://modrinth.com/mod/mastercutter).


### Mo Glass

**Feature family:** Glass shapes. **Also serves:** —.

Glass stairs and slabs provide additional transparent building shapes.

**Installed-name examples:** Black Stained Glass Slab, Black Stained Glass Stairs, Blue Stained Glass Slab, Blue Stained Glass Stairs, Brown Stained Glass Slab, Brown Stained Glass Stairs, Cyan Stained Glass Slab, Cyan Stained Glass Stairs, Glass Slab, Glass Stairs, Gray Stained Glass Slab, Gray Stained Glass Stairs, Green Stained Glass Slab, Green Stained Glass Stairs, Light Blue Stained Glass Slab, Light Blue Stained Glass Stairs, Light Gray Stained Glass Slab, Light Gray Stained Glass Stairs, Lime Stained Glass Slab, Lime Stained Glass Stairs, Magenta Stained Glass Slab, Magenta Stained Glass Stairs, Orange Stained Glass Slab, Orange Stained Glass Stairs, Pink Stained Glass Slab, Pink Stained Glass Stairs, Purple Stained Glass Slab, Purple Stained Glass Stairs, Red Stained Glass Slab, Red Stained Glass Stairs, Tinted Glass Slab, Tinted Glass Stairs, White Stained Glass Slab, White Stained Glass Stairs, Yellow Stained Glass Slab, Yellow Stained Glass Stairs.

**Version:** 1.7-MC1.20.1. **File:** `mods/mo-glass.pw.toml`. [Project page](https://www.curseforge.com/projects/353426).


### Pumpkins Accelerated

**Feature family:** Carved pumpkins. **Also serves:** Farmer, Collector.

Additional carved-pumpkin faces and soul jack-o-lantern variants; decorative and seasonal collection potential, rather than a new crop-production system.

**Installed-name examples:** Carved Pumpkin Check, Carved Pumpkin Creeper, Carved Pumpkin Derp, Carved Pumpkin Evil, Carved Pumpkin Heart, Carved Pumpkin Herobrine, Carved Pumpkin Shout, Carved Pumpkin Smile, Carved Pumpkin X, Jack o'Lantern Check, Jack o'Lantern Creeper, Jack o'Lantern Derp, Jack o'Lantern Evil, Jack o'Lantern Heart, Jack o'Lantern Herobrine, Jack o'Lantern Shout, Jack o'Lantern Smile, Jack o'Lantern X, Soul Jack o'Lantern Check, Soul Jack o'Lantern Creeper, Soul Jack o'Lantern Derp, Soul Jack o'Lantern Evil, Soul Jack o'Lantern Heart, Soul Jack o'Lantern Herobrine, Soul Jack o'Lantern Normal, Soul Jack o'Lantern Shout, Soul Jack o'Lantern Smile, Soul Jack o'Lantern X.

**Version:** 1.0.0. **File:** `mods/more-pumpkins!.pw.toml`. [Project page](https://modrinth.com/mod/more-pumpkins!).


### Round's Invisible Frames

**Feature family:** Item displays. **Also serves:** Collector, Merchant.

Toggle item-frame visibility for clean displays, shop presentation and collection rooms.

**Version:** 1.1.0. **File:** `mods/rounds-invisible-frames.pw.toml`. [Project page](https://www.curseforge.com/projects/1295518).


### Sawmill

**Feature family:** Timber processing. **Also serves:** Farmer.

Dedicated wood-processing workstation for turning timber into construction components.

**Installed-name examples:** Saw.

**Version:** 1.20-1.4.11. **File:** `mods/sawmill.pw.toml`. [Project page](https://www.curseforge.com/projects/964817).


### Serene Shrubbery Refabricated

**Feature family:** Flower gardens. **Also serves:** Farmer, Collector.

Decorative flowers provide more garden palettes and plant-collection goals.

**Installed-name examples:** Blanketflower, Bloom Basket, Bloom Basket Blue Orchids, Bloom Basket Frost Pansies, Bloom Basket Halloween Pansies, Bloom Basket Orange Crown Cacti, Bloom Basket Orange Pansies, Bloom Basket Panola Pansies, Bloom Basket Pink Crown Cacti, Bloom Basket Pink Pansies, Bloom Basket Purple Pansies, Bloom Basket Red Pansies, Bloom Basket Sunrise Pansies, Bloom Basket Twinflowers, Bloom Basket White Pansies, Bloom Basket Yellow Pansies, Blue Frost Pansies, Blue Hydrangea, Blue Liverwort, Candy Mountain Foxglove, Fireweed, Golden Lupine, Green Hydrangea, Halloween Foxglove, Halloween Hydrangea, Halloween Pansies, Indigo Butterfly Bush, Lavender Foxglove, Manhattan Lights Lupine, Orange Crown Cactus, Orange Pansies, Panola Pink Pansies, Peachy Foxglove, Pink Butterfly Bush, Pink Crown Cactus, Pink Hydrangea. Full extracted list in the HTML catalogue.

**Version:** 1.2.1. **File:** `mods/serene-shrubbery-fabric.pw.toml`. [Project page](https://www.curseforge.com/projects/1446593).


### SignCopy

**Feature family:** Signs. **Also serves:** Merchant.

Local SignCopy jar provides sign-copying utility; verify its exact interaction in-game before writing instructional text.

**Version:** 1.1.1. **File:** `mods/SignCopy-Fabric-1.20.1-1.1.1.jar`. [Project page](https://modrinth.com/mod/cK4nxndh).


### Sit (Fabric)

**Feature family:** Furniture interaction. **Also serves:** —.

Sit on suitable slabs and stairs; supports usable seating made from ordinary blocks.

**Version:** 1.20.1-27. **File:** `mods/sit-fabric.pw.toml`. [Project page](https://www.curseforge.com/projects/328163).


### Sooty Chimneys

**Feature family:** Chimneys. **Also serves:** —.

Chimneys and smoke effects provide working visual detail for cottages, kitchens and workshops.

**Installed-name examples:** Brick Chimney, Cobblestone Chimney, Copper Chimney, Dirty Brick Chimney, Dirty Cobblestone Chimney, Dirty Copper Chimney, Dirty Iron Chimney, Dirty Mud Brick Chimney, Dirty Stone Brick Chimney, Dirty Terracotta Chimney, Iron Chimney, Mud Brick Chimney, Stone Brick Chimney, Terracotta Chimney.

**Version:** 1.3.4. **File:** `mods/sooty-chimneys.pw.toml`. [Project page](https://www.curseforge.com/projects/634005).


### Supplementaries

**Feature family:** Functional decoration. **Also serves:** Mechanic, Quartermaster, Farmer, Collector, Merchant.

A broad set of functional blocks and props: storage and displays, signs and notices, ropes and utility fittings, lighting and redstone-related interactions. Treat practical household and workshop features separately from material palettes. Pack scripts change coloured presents and related crafting.

**Installed-name examples:** 0, Ash, Ash Brick Slab, Ash Brick Stairs, Ash Brick Vertical Slab, Ash Brick Wall, Ash Bricks, Awning, Bamboo Spikes, Basalt, Bellows, Black Awning, Black Candle Holder, Black Flag, Black Present, Blackboard, Blackstone Lamp, Blackstone Tile Slab, Blackstone Tile Stairs, Blackstone Tile Vertical Slab, Blackstone Tile Wall, Blackstone Tiles, Blaze Rod, Block of Flint, Blue Awning, Blue Candle Holder, Blue Flag, Blue Present, Boat in a Jar, Book Pile, Brass Lantern, Brown Awning, Brown Candle Holder, Brown Flag, Brown Present, Bubble Block. Full extracted list in the HTML catalogue.

**Version:** 1.20-3.1.43. **File:** `mods/supplementaries.pw.toml`. [Project page](https://www.curseforge.com/projects/412082).


### Supplementaries Squared

**Feature family:** Supplementaries materials. **Also serves:** —.

Extends Supplementaries building options; the pack supplies corrected daub-frame slab and stair recipes.

**Installed-name examples:** %s Item Shelf, Black Sack, Blue Sack, Brass Lantern, Brown Sack, Copper Lantern, Copper Plaque, Crimson Lantern, Cyan Sack, Daub Slab, Daub Stairs, Daub Vertical Slab, Gold Black Candle Holder, Gold Blue Candle Holder, Gold Brown Candle Holder, Gold Candle Holder, Gold Cupric Candle Holder, Gold Cyan Candle Holder, Gold Ender Candle Holder, Gold Gray Candle Holder, Gold Green Candle Holder, Gold Lantern, Gold Light Blue Candle Holder, Gold Light Gray Candle Holder, Gold Lime Candle Holder, Gold Magenta Candle Holder, Gold Orange Candle Holder, Gold Pink Candle Holder, Gold Plaque, Gold Purple Candle Holder, Gold Red Candle Holder, Gold Soul Candle Holder, Gold Spectacle Candle Holder, Gold White Candle Holder, Gold Yellow Candle Holder, Gray Sack. Full extracted list in the HTML catalogue.

**Version:** 1.20-1.1.29. **File:** `mods/supplementaries-squared.pw.toml`. [Project page](https://www.curseforge.com/projects/838411).


### Twigs

**Feature family:** Natural building materials. **Also serves:** Explorer.

New materials and decorative variants expand stone, timber and natural-detail palettes.

**Installed-name examples:** Acacia Table, Azalea Flowers, Bamboo Leaves, Bamboo Mat, Bamboo Table, Bamboo Thatch, Bamboo Thatch Slab, Bamboo Thatch Stairs, Birch Table, Black Packed Silt, Black Silt Pot, Black Silt Shingle Slab, Black Silt Shingle Stairs, Black Silt Shingle Wall, Black Silt Shingles, Blackstone Column, Bloodstone, Bloodstone Slab, Bloodstone Stairs, Bloodstone Wall, Blue Packed Silt, Blue Silt Pot, Blue Silt Shingle Slab, Blue Silt Shingle Stairs, Blue Silt Shingle Wall, Blue Silt Shingles, Bronzed Seashell, Brown Packed Silt, Brown Silt Pot, Brown Silt Shingle Slab, Brown Silt Shingle Stairs, Brown Silt Shingle Wall, Brown Silt Shingles, Calcite Slab, Calcite Stairs, Calcite Wall. Full extracted list in the HTML catalogue.

**Version:** 3.1.0. **File:** `mods/twigs.pw.toml`. [Project page](https://www.curseforge.com/projects/496913).


## The Collector


### Blåhaj

**Feature family:** Soft toys. **Also serves:** Builder.

Blåhaj soft-toy content offers an additional plushie/display collection separate from the Perfect Plushies mods.

**Installed-name examples:** Bread Pillow, Gray Toy Shark, Soft Toy Shark.

**Version:** 0.3.2. **File:** `mods/blahaj-fabric-1.20.0-0.3.2.jar`. [Project page](https://github.com/DaFuqs/Blahaj).


### Camerapture

**Feature family:** Photography. **Also serves:** Explorer, Builder.

Take in-game photos and display pictures; supports a travel journal, wildlife album and gallery without making every collection an item checklist.

**Installed-name examples:** Picture Frame, Album, Camera, Picture.

**Version:** 1.10.12. **File:** `mods/camerapture.pw.toml`. [Project page](https://www.curseforge.com/projects/1051342).


### Perfect Homestead Plushies

**Feature family:** Homestead plushies. **Also serves:** Builder, Explorer.

Homestead-specific player and creature plushies. The custom chest-loot pool explicitly lists 27 player plushies plus Mushling, Mystical Elk and Fernling: 30 entries. This is a pool count, not proof that those are every registered plushie in the mod.

**Installed-name examples:** Fernling Plushie, Homestead Player 1, Homestead Player 10, Homestead Player 11, Homestead Player 12, Homestead Player 13, Homestead Player 14, Homestead Player 15, Homestead Player 16, Homestead Player 17, Homestead Player 18, Homestead Player 19, Homestead Player 2, Homestead Player 20, Homestead Player 21, Homestead Player 22, Homestead Player 23, Homestead Player 24, Homestead Player 25, Homestead Player 26, Homestead Player 27, Homestead Player 28, Homestead Player 29, Homestead Player 3, Homestead Player 30, Homestead Player 31, Homestead Player 32, Homestead Player 33, Homestead Player 34, Homestead Player 35, Homestead Player 36, Homestead Player 37, Homestead Player 38, Homestead Player 39, Homestead Player 4, Homestead Player 40. Full extracted list in the HTML catalogue.

**Version:** 1.1.0. **File:** `mods/perfect-homestead-plushies.pw.toml`. [Project page](https://www.curseforge.com/projects/1286189).


### Perfect Plushies

**Feature family:** Plushies. **Also serves:** Builder, Explorer.

Collect and display decorative plushies and Easter-egg variants. The pack supplies additional acquisition routes; use recipe/loot availability rather than assuming every plushie is a chest drop.

**Installed-name examples:** Aye Aye Plushie, Bear Plushie, Brown Rabbit Plushie, Capybara Plushie, Cat Plushie, Daniel Plushie, Doe Plushie, Dog Plushie, Dolphin Plushie, Duck Plushie, Dumbo Blob Plushie, Elephant Plushie, Fennec Fox Plushie, Frog Plushie, GamerPotion Plushie, Geode Plushie, Goose Plushie, Hedgehog Plushie, Hippo Plushie, Hummingbird Plushie, Joosh Plushie, June Plushie, Koala Plushie, Lion Cub Plushie, Monkey Plushie, Mouse Plushie, Nyf Plushie, Panda Plushie, Quokka Plushie, Raccoon Plushie, Red Fox Plushie, Red Panda Plushie, Red Ruffed Lemur Plushie, Reindeer Plushie, Robin Plushie, RoCris Plushie. Full extracted list in the HTML catalogue.

**Version:** 1.13.3. **File:** `mods/perfect-plushies.pw.toml`. [Project page](https://www.curseforge.com/projects/867232).


### Simple Hats

**Feature family:** Cosmetic hats. **Also serves:** Explorer, Builder.

Collect wearable cosmetic hats and hat bags. Pack recipes upgrade four lower-rarity bags into the next tier and convert epic bags into seasonal bags with themed ingredients.

**Installed-name examples:** Hat Stand, Acorn Cap, Aegis, Alhoon, Alien Antennae, Amalgalich, Angel and Devil, Angled Shades, Antlers, Apple, Armor Helm, Artsy, Artsy Doll, Astronaut, Axolotl Friend, Azumanga's Hat, Baby Bottle Head, Baby Crewmate, Baby Dolphin, Baby Penguin, Baby Snowman, Baby Turtle, Bandana, Baseball Cap, Bat Wing Hat, Beanie, Bee Friend, Bee Hat, Beeholder, Beetle Friend, Beret Ribbon, Bicorne, Big Brain, Big Crown, Big Eyes, Big Ribbon. Full extracted list in the HTML catalogue.

**Version:** 0.4.0a. **File:** `mods/simplehats.pw.toml`. [Project page](https://www.curseforge.com/projects/631990).


## The Explorer


### [Let's Do Addon] Structures

**Feature family:** Homestead structures. **Also serves:** Brewer, Farmer, Builder, Merchant.

Let's Do-themed world structures tie exploration to vineyards, farming and domestic architecture; the pack overrides selected structure sets and loot.

**Version:** 1.7.2. **File:** `mods/lets-do-addon-structures.pw.toml`. [Project page](https://www.curseforge.com/projects/967867).


### Better Climbing

**Feature family:** Traversal rules. **Also serves:** Blacksmith.

Improved climbing interactions make caving and vertical travel easier; include as a travel tip.

**Version:** 3. **File:** `mods/better-climbing.pw.toml`. [Project page](https://www.curseforge.com/projects/655619).


### BetterEnd

**Feature family:** End ecosystems. **Also serves:** Builder, Cook, Farmer, Blacksmith, Witch, Collector.

New End biomes, vegetation, creatures and building resources; resource processing and ritual-related content broaden End progression. Link its materials to BetterEndDelight and equipment rather than treating the dimension as a single visit.

**Installed-name examples:** Amber Land, Blossoming Spires, Chorus Forest, Crystal Mountains, Dragon Graveyards, Dry Shrubland, Dust Wastelands, Empty Aurora Cave, Empty End Cave, Empty Smaragdant Cave, Eterial Grove, Foggy Mushroomland, Glowing Grasslands, Ice Starfield, Jade Cave, Lantern Woods, Lush Aurora Cave, Lush Smaragdant Cave, Megalake, Megalake Grove, Neon Oasis, Nightshade Redwoods, Old Bulbis Gardens, Painted Mountains, Shadow Forest, Sulfur Springs, Umbra Valley, Umbrella Jungle, Aeridium, Aeternium Anvil, Aeternium Block, Amaranita Cap, Amaranita Fur, Amaranita Hymenophore, Amaranita Hyphae, Amaranita Lantern. Full extracted list in the HTML catalogue.

**Version:** 4.0.11. **File:** `mods/betterend.pw.toml`. [Project page](https://modrinth.com/mod/betterend).


### Block Runner

**Feature family:** Road travel. **Also serves:** Builder.

Certain surface blocks increase movement speed, giving player-built roads a practical purpose.

**Installed-name examples:** Speed Multiplier: %s.

**Version:** 8.0.4. **File:** `mods/block-runner.pw.toml`. [Project page](https://www.curseforge.com/projects/442842).


### ChoiceTheorem's Overhauled Village

**Feature family:** Villages and outposts. **Also serves:** Merchant, Builder, Adventurer.

Rebuilt and biome-appropriate villages and pillager outposts; discover settlements and study their architecture or trading opportunities.

**Version:** 3.4.14. **File:** `mods/choicetheorems-overhauled-village.pw.toml`. [Project page](https://www.curseforge.com/projects/623908).


### Comforts

**Feature family:** Camping. **Also serves:** Builder.

Sleeping bags and hammocks provide portable rest with distinct time/spawn behaviour, supporting camps and expeditions.

**Installed-name examples:** Black Hammock Cloth, Black Sleeping Bag, Blue Hammock Cloth, Blue Sleeping Bag, Brown Hammock Cloth, Brown Sleeping Bag, Cyan Hammock Cloth, Cyan Sleeping Bag, Gray Hammock Cloth, Gray Sleeping Bag, Green Hammock Cloth, Green Sleeping Bag, Light Blue Hammock Cloth, Light Blue Sleeping Bag, Light Gray Hammock Cloth, Light Gray Sleeping Bag, Lime Hammock Cloth, Lime Sleeping Bag, Magenta Hammock Cloth, Magenta Sleeping Bag, Orange Hammock Cloth, Orange Sleeping Bag, Pink Hammock Cloth, Pink Sleeping Bag, Purple Hammock Cloth, Purple Sleeping Bag, Red Hammock Cloth, Red Sleeping Bag, Rope and Nail, This is decorative, you cannot sleep here, White Hammock Cloth, White Sleeping Bag, Yellow Hammock Cloth, Yellow Sleeping Bag.

**Version:** 6.4.0+1.20.1. **File:** `mods/comforts.pw.toml`. [Project page](https://www.curseforge.com/projects/276951).


### Deeper and Darker

**Feature family:** Deep Dark and Otherside. **Also serves:** Adventurer, Blacksmith, Builder, Collector.

Expands Deep Dark-themed blocks, equipment and mysteries with another exploration destination. Separate access/preparation, biome discovery, encounters and material uses.

**Installed-name examples:** Blooming Caverns, Deeplands, Echoing Forest, Overcast Columns, Ancient Vase, Bloom Button, Bloom Door, Bloom Fence, Bloom Fence Gate, Bloom Hanging Sign, Bloom Planks, Bloom Pressure Plate, Bloom Sign, Bloom Slab, Bloom Stairs, Bloom Trapdoor, Bloom Wall Hanging Sign, Bloom Wall Sign, Blooming Moss Block, Blooming Sculk Stone, Blooming Stem, Cannot link to block, Chiseled Gloomslate, Chiseled Sculk Stone, Cobbled Gloomslate, Cobbled Gloomslate Slab, Cobbled Gloomslate Stairs, Cobbled Gloomslate Wall, Cobbled Sculk Stone, Cobbled Sculk Stone Slab, Cobbled Sculk Stone Stairs, Cobbled Sculk Stone Wall, Crystallized Amber, Cut Gloomslate, Cut Gloomslate Slab, Cut Gloomslate Stairs. Full extracted list in the HTML catalogue.

**Version:** 1.3.3-plus-b. **File:** `mods/deeperdarker.pw.toml`. [Project page](https://www.curseforge.com/projects/659011).


### Dungeons and Taverns

**Feature family:** Dungeons and roadside stops. **Also serves:** Adventurer, Merchant, Builder.

Dungeons, taverns and other exploration structures supply encounters, loot and world detail.

**Version:** 3.0.3.f. **File:** `mods/dungeon-and-taverns.pw.toml`. [Project page](https://www.curseforge.com/projects/853794).


### Elytra Slot

**Feature family:** Flight loadouts. **Also serves:** Adventurer.

Wear elytra in an accessory slot alongside chest armor, changing exploration and combat loadouts.

**Version:** 6.4.4+1.20.1. **File:** `mods/elytra-slot.pw.toml`. [Project page](https://www.curseforge.com/projects/317716).


### Explorer's Compass

**Feature family:** Structure navigation. **Also serves:** Adventurer.

Locate structures. The pack replaces its recipe with one using cobwebs and gilded blackstone, so do not present it as the default cheap early-game compass.

**Installed-name examples:** Explorer's Compass.

**Version:** 1.20.1-2.6.0-fabric. **File:** `mods/explorers-compass.pw.toml`. [Project page](https://www.curseforge.com/projects/491794).


### Geophilic – Vanilla Biome Overhauls

**Feature family:** Vanilla landscape detail. **Also serves:** Builder.

Overhauls the appearance and detail of vanilla Overworld biomes; a scenery layer supporting exploration and site selection.

**Version:** 3.5. **File:** `mods/geophilic.pw.toml`. [Project page](https://www.curseforge.com/projects/711216).


### Gliders

**Feature family:** Aerial travel. **Also serves:** Builder.

Gliding equipment helps cross terrain and manage falls; a transport option alongside jetpacks and later flight.

**Installed-name examples:** Basic Paraglider, Copper Upgrade, Diamond Paraglider, Gold Paraglider, Iron Paraglider, Nether Upgrade, Netherite Paraglider, Re-Enforced Paper, Re-Enforced Paper (Diamond), Re-Enforced Paper (Gold), Re-Enforced Paper (Iron), Re-Enforced Paper (Netherite).

**Version:** 1.2.0. **File:** `mods/gliders.pw.toml`. [Project page](https://www.curseforge.com/projects/828331).


### Immersive structures

**Feature family:** World structures. **Also serves:** Builder, Adventurer.

Additional structures built into the landscape; use distinct structure families as exploration targets.

**Version:** 2.1.0. **File:** `mods/immersive-structures.pw.toml`. [Project page](https://modrinth.com/mod/immersive-structures).


### Incendium

**Feature family:** Nether overhaul. **Also serves:** Adventurer, Collector, Builder.

Nether biome and terrain content, challenging structures and distinctive loot/equipment. Because it uses substantial vanilla-style data content, a new-item registry alone would miss many features.

**Installed-name examples:** Ash Barrens, Infernal Dunes, Inverted Forest, Quartz Flats, Toxic Heap, Volcanic Deltas, Weeping Valley, Withered Forest.

**Version:** 5.3.5. **File:** `mods/incendium.pw.toml`. [Project page](https://www.curseforge.com/projects/591388).


### Jump Over Fences

**Feature family:** Traversal rules. **Also serves:** Rancher.

Fence-jumping convenience affects movement through farmyards and settlements.

**Version:** 1.3.1. **File:** `mods/jump-over-fences-forge.pw.toml`. [Project page](https://www.curseforge.com/projects/423421).


### Lootr (Fabric)

**Feature family:** Shared exploration. **Also serves:** Adventurer, Collector.

Personalised loot access supports exploring together without one player emptying the rewards for everyone.

**Installed-name examples:** Centennial Trophy, Loot Barrel, Loot Chest, Loot Shulker, Minecart with Chest.

**Version:** 0.7.35.86. **File:** `mods/lootr-fabric.pw.toml`. [Project page](https://www.curseforge.com/projects/615106).


### MES - Moog's End Structures

**Feature family:** End structures. **Also serves:** Adventurer, Builder.

Additional End structures and loot destinations complement BetterEnd.

**Version:** 2.0.3. **File:** `mods/moogs-end-structures.pw.toml`. [Project page](https://www.curseforge.com/projects/892382).


### MMV - Moog's Missing Villages

**Feature family:** Missing village biomes. **Also serves:** Merchant, Builder.

Jungle and swamp village additions fill gaps in vanilla settlement coverage.

**Version:** 2.1.1. **File:** `mods/mmv-moogs-missing-villages.pw.toml`. [Project page](https://www.curseforge.com/projects/1153951).


### MNS - Moog's Nether Structures

**Feature family:** Nether structures. **Also serves:** Adventurer, Builder.

Additional Nether structures with encounters and loot expand the dimension's routes.

**Version:** 3.0.0. **File:** `mods/mns-moogs-nether-structures.pw.toml`. [Project page](https://www.curseforge.com/projects/967466).


### MTR - Moog's Temples Reimagined

**Feature family:** Temples. **Also serves:** Adventurer, Builder.

Reimagined temple structures add further expedition targets. Confirm which replacements generate alongside YUNG's structure mods before creating exact-location requirements.

**Version:** 2.0.3. **File:** `mods/mtr-moogs-temples-reimagined.pw.toml`. [Project page](https://www.curseforge.com/projects/1339737).


### MVS - Moog's Voyager Structures

**Feature family:** Overworld structures. **Also serves:** Adventurer, Builder.

A broad collection of Overworld structures and ruins with loot, mobs and villager encounters; group by structure family rather than every template variant.

**Version:** 5.1.1. **File:** `mods/moogs-voyager-structures.pw.toml`. [Project page](https://www.curseforge.com/projects/656977).


### Nature's Compass

**Feature family:** Biome navigation. **Also serves:** Farmer.

Find biomes and read biome information; a practical tool for locating regional resources and homes.

**Installed-name examples:** Nature's Compass.

**Version:** 1.20.1-2.6.0-fabric. **File:** `mods/natures-compass.pw.toml`. [Project page](https://www.curseforge.com/projects/252848).


### Nature's Spirit

**Feature family:** Biomes and materials. **Also serves:** Builder, Farmer, Cook, Collector.

New landscapes, plants and building materials; Nature's Delight supplies a food-processing connection.

**Installed-name examples:** Alpine Clearings, Alpine Highlands, Arid Highlands, Arid Savanna, Aspen Forest, Bamboo Wetlands, Blooming Dunes, Blooming Highlands, Blooming Sugi Forest, Boreal Taiga, Carnation Fields, Cedar Thicket, Chaparral, Coniferous Covert, Cypress Fields, Drylands, Dusty Slopes, Fir Forest, Floral Ridges, Flowering Shrubland, Golden Wilds, Heather Fields, Lavender Fields, Lively Dunes, Maple Woodlands, Marigold Meadows, Marsh, Oak Savanna, Prairie, Red Peaks, Redwood Forest, Scorched Dunes, Shrubby Highlands, Shrubland, Sleeted Slopes, Snowcapped Red Peaks. Full extracted list in the HTML catalogue.

**Version:** 2.2.5-1.20.1. **File:** `mods/natures-spirit.pw.toml`. [Project page](https://www.curseforge.com/projects/1044992).


### Oh The Biomes We've Gone

**Feature family:** Biomes and materials. **Also serves:** Builder, Farmer, Collector.

Large biome, tree and plant expansion. The canonical configuration disables Eroded Borealis and Shattered Glacier; Lush Stacks is enabled here. Avoid tasks requiring disabled biomes and do not reuse settings from an older instance.

**Installed-name examples:** Allium Shrubland, Amaranth Grassland, Araucaria Savanna, Aspen Boreal, Atacama Outback, Baobab Savanna, Basalt Barrera, Bayou, Black Forest, Canadian Shield, Cika Woods, Coconino Meadow, Coniferous Forest, Crag Gardens, Crimson Tundra, Cypress Swamplands, Cypress Wetlands, Dacite Ridges, Dacite Shore, Dead Sea, Ebony Woods, Enchanted Tangle, Eroded Borealis, Firecracker Chaparral, Forgotten Forest, Fragment Jungle, Frosted Coniferous Forest, Frosted Taiga, Howling Peaks, Ironwood Gour, Jacaranda Jungle, Lush Stacks, Maple Taiga, Mojave Desert, Orchard, Overgrowth Woodlands. Full extracted list in the HTML catalogue.

**Version:** 1.8.0. **File:** `mods/oh-the-biomes-weve-gone.pw.toml`. [Project page](https://www.curseforge.com/projects/1070751).


### Regions Unexplored

**Feature family:** Biomes and materials. **Also serves:** Builder, Farmer, Collector.

Additional regional landscapes, vegetation and material palettes. Discovery, tree/plant collections and construction uses are separate goals; use installed biome assets rather than a marketing biome count.

**Installed-name examples:** Alpha Grove, Ancient Delta, Arid Mountains, Ashen Woodland, Autumnal Maple Forest, Bamboo Forest, Baobab Savanna, Barley Fields, Bayou, Bioshroom Caves, Blackstone Basin, Blackwood Taiga, Boreal Taiga, Chalk Cliffs, Clover Plains, Cold Boreal Taiga, Cold Deciduous Forest, Cold River, Deciduous Forest, Dry Bushland, Eucalyptus Forest, Fen, Flower Fields, Frozen Pine Taiga, Frozen Tundra, Fungal Fen, Glistering Meadow, Golden Boreal Taiga, Grassland, Grassy Beach, Gravel Beach, Highland Fields, Hyacinth Deeps, Icy Heights, Infernal Holt, Joshua Desert. Full extracted list in the HTML catalogue.

**Version:** 0.5.6+1.20.1. **File:** `mods/regions-unexplored.pw.toml`. [Project page](https://www.curseforge.com/projects/659110).


### Repurposed Structures (Fabric)

**Feature family:** Structure variants. **Also serves:** Adventurer, Merchant, Builder.

Biome/dimension variants of familiar structures; a discovery catalogue of structure families across environments.

**Version:** 7.1.25+1.20.1-fabric. **File:** `mods/repurposed-structures-fabric.pw.toml`. [Project page](https://www.curseforge.com/projects/391366).


### Shulker Drops Two

**Feature family:** Shulker rewards. **Also serves:** Quartermaster, Adventurer.

Adjusts shulker shell drops, affecting portable-storage acquisition; verify configured values before stating a guaranteed yield.

**Version:** 3.5. **File:** `mods/shulker-drops-two.pw.toml`. [Project page](https://www.curseforge.com/projects/302548).


### Structory

**Feature family:** Ruins and environmental stories. **Also serves:** Builder, Adventurer.

Atmospheric structures and themed ruins add smaller destinations and architectural details.

**Version:** 1.3.5. **File:** `mods/structory.pw.toml`. [Project page](https://modrinth.com/mod/structory).


### Structory: Towers

**Feature family:** Towers. **Also serves:** Builder, Adventurer.

Biome-themed towers add landmarks and expedition sites; pack structure-set overrides affect placement.

**Version:** 1.0.7. **File:** `mods/structory-towers.pw.toml`. [Project page](https://modrinth.com/mod/structory-towers).


### Tectonic

**Feature family:** Landforms. **Also serves:** Builder.

Changes large-scale terrain and landforms; exploration and choosing a home site are the activities, rather than collecting mod-specific machines or gear.

**Version:** 3.0.17. **File:** `mods/tectonic.pw.toml`. [Project page](https://www.curseforge.com/projects/686836).


### Tidal Towns

**Feature family:** Ocean settlements. **Also serves:** Merchant, Builder.

Floating driftwood-style villages provide maritime destinations and architectural inspiration.

**Version:** 1.3.4. **File:** `mods/tidal-towns.pw.toml`. [Project page](https://www.curseforge.com/projects/891880).


### Towns and Towers

**Feature family:** Settlements and ships. **Also serves:** Merchant, Builder, Adventurer.

Additional village, outpost and ship structures; separate peaceful settlement discovery from hostile sites.

**Version:** 1.12. **File:** `mods/towns-and-towers.pw.toml`. [Project page](https://www.curseforge.com/projects/626761).


### Umbrellas

**Feature family:** Weather equipment. **Also serves:** Collector, Builder.

Umbrellas offer shelter-themed utility and cosmetic equipment for outdoor travel.

**Installed-name examples:** Acacia Umbrella Stand, Bamboo Umbrella Stand, Birch Umbrella Stand, Cherry Umbrella Stand, Crimson Umbrella Stand, Dark Oak Umbrella Stand, Jungle Umbrella Stand, Mangrove Umbrella Stand, Oak Umbrella Stand, Spruce Umbrella Stand, Warped Umbrella Stand, Billowing, Gliding, Animals Umbrella, Azalea Umbrella, Black Umbrella, Blue Umbrella, Bordure Indented Umbrella Pattern, Brown Umbrella, Creeper Umbrella Pattern, Cyan Umbrella, Field Masoned Umbrella Pattern, Flower Umbrella Pattern, Galactic Umbrella, Globe Umbrella Pattern, Gothic Umbrella, Gray Umbrella, Green Umbrella, Jellyfish Umbrella, Light Blue Umbrella, Light Gray Umbrella, Lime Umbrella, Magenta Umbrella, Orange Umbrella, Pink Umbrella, Pride Umbrella Pattern. Full extracted list in the HTML catalogue.

**Version:** 1.4.2. **File:** `mods/pneumono_umbrellas.pw.toml`. [Project page](https://modrinth.com/mod/pneumono_umbrellas).


### Universal Graves

**Feature family:** Death recovery. **Also serves:** Adventurer.

Graves preserve/recover dropped possessions according to server configuration; explain this in shared onboarding before dangerous paths.

**Installed-name examples:** Emptied Grave, Grave, Gravestone, Grave Compass.

**Version:** 3.0.3+1.20.1. **File:** `mods/universal-graves.pw.toml`. [Project page](https://www.curseforge.com/projects/497175).


### Vanilla Backport

**Feature family:** Newer vanilla content. **Also serves:** Builder, Rancher, Adventurer, Quartermaster, Collector.

The installed jar includes Pale Garden/pale oak, Creaking-related content and resin; armadillos and wolf armor; Happy Ghast, dried ghast and harness assets; bundles, ambient plants and Sulfur Caves-related assets. These are installed-version candidates, not a claim that every feature is enabled or every language entry spawns. Split them across exploration, animal care, transport and building.

**Installed-name examples:** Pale Garden, Sulfur Caves, Block of Resin, Bush, Cactus Flower, Chiseled Cinnabar, Chiseled Resin Bricks, Chiseled Sulfur, Cinnabar, Cinnabar Brick Slab, Cinnabar Brick Stairs, Cinnabar Brick Wall, Cinnabar Bricks, Cinnabar Slab, Cinnabar Stairs, Cinnabar Wall, Closed Eyeblossom, Creaking Heart, Dried Ghast, Firefly Bush, Leaf Litter, Open Eyeblossom, Pale Hanging Moss, Pale Moss Block, Pale Moss Carpet, Pale Oak Button, Pale Oak Door, Pale Oak Fence, Pale Oak Fence Gate, Pale Oak Hanging Sign, Pale Oak Leaves, Pale Oak Log, Pale Oak Planks, Pale Oak Pressure Plate, Pale Oak Sapling, Pale Oak Sign. Full extracted list in the HTML catalogue.

**Version:** 1.1.7.10. **File:** `mods/vanillabackport.pw.toml`. [Project page](https://www.curseforge.com/projects/417430).


### Villages&Pillages

**Feature family:** Hostile settlements. **Also serves:** Adventurer, Merchant.

Hostile village-like structures give settlement exploration a combat branch.

**Version:** 1.0.2. **File:** `mods/villages-and-pillages.pw.toml`. [Project page](https://www.curseforge.com/projects/915531).


### Waystones

**Feature family:** Travel network. **Also serves:** Merchant, Builder.

Activate waystones and build a network between bases, settlements and expedition sites; costs and permissions follow current configuration.

**Installed-name examples:** Black Sharestone, Black Waystone, Blue Sharestone, Brown Sharestone, Cyan Sharestone, Deepslate Waystone, Ender Waystone, Gray Sharestone, Green Sharestone, Light Blue Sharestone, Light Gray Sharestone, Lime Sharestone, Magenta Sharestone, Mossy Waystone, Orange Sharestone, Pink Sharestone, Portstone, Purple Sharestone, Red Sharestone, Sandy Waystone, Sharestone, Warp Plate, Waystone, White Sharestone, Yellow Sharestone, Attuned Shard, Bound Scroll, Crumbling Attuned Shard, Return Scroll, Warp Dust, Warp Scroll, Warp Scroll (Bound), Warp Stone.

**Version:** 14.1.20. **File:** `mods/waystones.pw.toml`. [Project page](https://www.curseforge.com/projects/245755).


### Wearable lanterns

**Feature family:** Wearable lighting. **Also serves:** Blacksmith.

Wearable lantern and soul-lantern items, with waterproof variants, supply light while adventuring and caving. Local jar metadata calls this Wearable lanterns; its source contact is an example repository, so use local assets as evidence instead of that placeholder link.

**Installed-name examples:** Wearable Lantern, Wearable Soul Lantern, Wearable Waterproof Lantern, Wearable Waterproof Soul Lantern.

**Version:** 1.0.1. **File:** `mods/trinketlantern-1.0.1.jar`. Source: local jar metadata/assets; no trusted project URL supplied.


### YUNG's Better Caves (Fabric)

**Feature family:** Cave layout. **Also serves:** Blacksmith.

Overhauled cave generation is an underground exploration layer; evaluate its actual effect with the other terrain mods when checking generation.

**Version:** 1.20.1-Fabric-2.0.7. **File:** `mods/yungs-better-caves-fabric.pw.toml`. [Project page](https://www.curseforge.com/projects/408465).


### YUNG's Better Desert Temples (Fabric)

**Feature family:** Desert temples. **Also serves:** Adventurer.

Expanded desert-temple exploration, traps and loot; a specific expedition family.

**Version:** 1.20-Fabric-3.0.3. **File:** `mods/yungs-better-desert-temples-fabric.pw.toml`. [Project page](https://www.curseforge.com/projects/631020).


### YUNG's Better Dungeons (Fabric)

**Feature family:** Dungeons. **Also serves:** Adventurer.

Expanded dungeon structures provide underground combat and treasure destinations.

**Version:** 1.20-Fabric-4.0.4. **File:** `mods/yungs-better-dungeons-fabric.pw.toml`. [Project page](https://www.curseforge.com/projects/525586).


### YUNG's Better Jungle Temples (Fabric)

**Feature family:** Jungle temples. **Also serves:** Adventurer.

Rebuilt jungle temples provide a separate temple expedition family.

**Version:** 1.20-Fabric-2.0.5. **File:** `mods/yungs-better-jungle-temples-fabric.pw.toml`. [Project page](https://www.curseforge.com/projects/897678).


### YUNG's Better Mineshafts (Fabric)

**Feature family:** Mineshafts. **Also serves:** Blacksmith, Adventurer.

Reworked abandoned mines support underground navigation, resource trips and encounters.

**Version:** 1.20-Fabric-4.0.4. **File:** `mods/yungs-better-mineshafts-fabric.pw.toml`. [Project page](https://www.curseforge.com/projects/373591).


### YUNG's Better Nether Fortresses (Fabric)

**Feature family:** Nether fortresses. **Also serves:** Adventurer.

Expanded fortress structures affect how players approach Nether progression resources and combat.

**Version:** 1.20-Fabric-2.0.6. **File:** `mods/yungs-better-nether-fortresses-fabric.pw.toml`. [Project page](https://www.curseforge.com/projects/817666).


### YUNG's Better Ocean Monuments (Fabric)

**Feature family:** Ocean monuments. **Also serves:** Angler, Adventurer.

Expanded ocean monuments provide an underwater expedition branch with preparation and combat.

**Version:** 1.20-Fabric-3.0.4. **File:** `mods/yungs-better-ocean-monuments-fabric.pw.toml`. [Project page](https://www.curseforge.com/projects/689252).


### YUNG's Better Strongholds (Fabric)

**Feature family:** Strongholds. **Also serves:** Adventurer.

Expanded strongholds change the journey to the End portal; use discovery and navigation goals.

**Version:** 1.20-Fabric-4.0.3. **File:** `mods/yungs-better-strongholds-fabric.pw.toml`. [Project page](https://www.curseforge.com/projects/480684).


### YUNG's Better Witch Huts (Fabric)

**Feature family:** Witch huts. **Also serves:** Witch, Builder.

Rebuilt swamp witch huts provide a witch-themed destination and architectural inspiration, not a separate magic system.

**Version:** 1.20-Fabric-3.0.3. **File:** `mods/yungs-better-witch-huts-fabric.pw.toml`. [Project page](https://www.curseforge.com/projects/631403).


### YUNG's Bridges (Fabric)

**Feature family:** Bridges. **Also serves:** Builder.

Naturally generated bridges add travel landmarks and examples of landscape-spanning construction.

**Version:** 1.20-Fabric-4.0.3. **File:** `mods/yungs-bridges-fabric.pw.toml`. [Project page](https://www.curseforge.com/projects/590988).


### YUNG's Cave Biomes (Fabric)

**Feature family:** Cave ecosystems. **Also serves:** Builder, Blacksmith.

New cave biomes and underground content supply subterranean destinations and material palettes.

**Installed-name examples:** Frosted Caves, Lost Caves, Marble Caves, Ancient Sand, Ancient Sandstone, Ancient Sandstone Slab, Ancient Sandstone Stairs, Ancient Sandstone Wall, Brittle Ancient Sandstone, Brittle Red Sandstone, Brittle Sandstone, Chiseled Ancient Sandstone, Creeping Ice, Cut Ancient Sandstone, Cut Ancient Sandstone Slab, Enchanted Ice, Frost Lily, Icicle, Layered Ancient Sandstone, Layered Red Sandstone, Layered Sandstone, Marble, Prickly Peach Cactus, Prickly Vines, Smooth Ancient Sandstone, Smooth Ancient Sandstone Slab, Smooth Ancient Sandstone Stairs, Suspicious Ancient Sand, Travertine, Buffeted, Frost, Ice Cube, Sand Snapper, Clock Pottery Sherd, Hourglass Pottery Sherd, Ice Cube Spawn Egg. Full extracted list in the HTML catalogue.

**Version:** 1.20.1-Fabric-2.0.5. **File:** `mods/yungs-cave-biomes-fabric.pw.toml`. [Project page](https://www.curseforge.com/projects/1112347).


### YUNG's Extras (Fabric)

**Feature family:** Small world details. **Also serves:** Builder.

Additional small structures and vanilla-style world details support incidental exploration.

**Version:** 1.20-Fabric-4.0.3. **File:** `mods/yungs-extras-fabric.pw.toml`. [Project page](https://www.curseforge.com/projects/590993).


## The Angler


### Go Fish

**Feature family:** Fishing progression. **Also serves:** Cook, Collector, Explorer.

Catch fish across environments and conditions; collect fishing crates; craft specialised rods and lures. Installed content includes overworld, Nether, End and celestial-themed fish, rods and meals. Catch-condition tasks need the installed loot rules; item names alone do not prove the required weather or biome.

**Installed-name examples:** Astral Crate, Diamond Crate, End Crate, Fiery Crate, Frosted Crate, Gilded Blackstone Crate, Golden Crate, Iron Crate, Slimey Crate, Soul Crate, Supply Crate, Wooden Crate, Deepfry, Aquatic Astral Stew, Baked Carrot Carp, Baked Endfish, Baked Seaweed, Basalt Bass, Blackstone Trout, Blackstone Trout Deluxe, Blaze Rod, Blizzard Bass, Bonefish, Carrot Carp, Celestial Rod, Charfish, Chorus Cod, Cloudy Crab, Diamond Reinforced Rod, Dragonfish, Ender Eel, Endfish, Endfish n' Chorus, Eye of Fishing, Frosted Rod, Galaxy Starfish. Full extracted list in the HTML catalogue.

**Version:** 1.6.3+1.20.1. **File:** `mods/go-fish.pw.toml`. [Project page](https://www.curseforge.com/projects/431135).


## The Rancher


### [Let's Do] Meadow

**Feature family:** Alpine homesteading. **Also serves:** Cook, Farmer, Explorer, Builder.

Alpine pasture landscapes and livestock-related resources; milk and multiple cheese wheels, cheese press and racks, fondue and cakes. Pine and limestone construction, patterned wool, barn fittings, watering can and wheelbarrow support the farmstead. Split dairy cooking, animal keeping and alpine architecture across paths.

**Installed-name examples:** Alpine Birch Log, Alpine Coal Ore, Alpine Copper Ore, Alpine Diamond Ore, Alpine Emerald Ore, Alpine Gold Ore, Alpine Iron Ore, Alpine Lapis Lazuli Ore, Alpine Poppy, Alpine Redstone Ore, Alpine Salt Ore, Amethyst Cheese Wheel, Big Wooden Flower Pot, Buffalo Cheese Wheel, Camera, Can, Cheese Press, Cheese Rack, Cheese Tart, Cheese Wheel, Cheesecake, Chiseled Limestone, Climbing Rope, Cobbled Limestone, Cobbled Limestone Slab, Cobbled Limestone Stairs, Cobbled Limestone Wall, Completionist Banner: Meadow, Cooking Cauldron, Cracked Limestone Bricks, Delphinium, Doormat, Enzian, Eriophorum, Fire Lily, Fire Log. Full extracted list in the HTML catalogue.

**Version:** 1.3.25. **File:** `mods/lets-do-meadow.pw.toml`. [Project page](https://www.curseforge.com/projects/821483).


### [Let's Do] WilderNature

**Feature family:** Wild animals. **Also serves:** Explorer, Cook, Adventurer, Collector.

Bison, boar, deer, minisheep, wolves, dogs, birds and smaller wildlife; meat, fur, trophies, an animal compendium and hunting equipment. The bounty board is blacklisted in this pack: do not build the path around contracts, bounty progression or its reward economy until alternative acquisition is verified.

**Installed-name examples:** Bison Trophy, Bounty Board, Bunny-Stalker Banner, Cod-Catcher Banner, Deer Trophy, Hazelnut Bush, Red Wolf Trophy, Wolf-Trapper Banner, Bison, Boar, Cassowary, Deer, Dog, Flamingo, Hedgehog, Minisheep, Owl, Pelican, Penguin, Raccoon, Red Wolf, Squirrel, Turkey, Animal Compendium, Bison Horn, Bison Meat, Bison Spawn Egg, Blunderbuss, Boar Spawn Egg, Cassowary Meat, Cassowary Spawn Egg, Common Contract, Cooked Bison Meat, Cooked Cassowary Meat, Cooked Pelican Meat, Cooked Turkey Meat. Full extracted list in the HTML catalogue.

**Version:** 1.0.6. **File:** `mods/lets-do-wildernature.pw.toml`. [Project page](https://www.curseforge.com/projects/1071657).


### Animal Feeding Trough [Fabric | Forge | Quilt | NeoForge]

**Feature family:** Animal husbandry. **Also serves:** Farmer.

Feed nearby animals using a trough, reducing repeated hand-feeding and supporting organized pens and breeding.

**Installed-name examples:** Feeding Trough.

**Version:** 1.1.0+1.20.1. **File:** `mods/animal-feeding-trough.pw.toml`. [Project page](https://www.curseforge.com/projects/445838).


### Convenient Name Tags

**Feature family:** Naming animals. **Also serves:** Collector.

Rename name tags directly through their interaction; helps organize pets and animal collections.

**Version:** 1.1.0. **File:** `mods/convenient-name-tags.pw.toml`. [Project page](https://modrinth.com/mod/convenient-name-tags).


### Duckling

**Feature family:** Waterfowl. **Also serves:** Cook, Explorer.

Ducks and duck-related resources, including eggs; the pack's food tags integrate duck eggs into recipes.

**Installed-name examples:** Holiday Fruit Cake, Duck, Duck Egg, Quackling, Cooked Duck Meat, Duck Spawn Egg, Quackling Spawn Egg, Raw Duck Meat.

**Version:** 4.0.0. **File:** `mods/duckling.pw.toml`. [Project page](https://www.curseforge.com/projects/597248).


### Friends For Life

**Feature family:** Companions. **Also serves:** Explorer, Adventurer.

Pet-related quality-of-life features encourage taking companions on adventures. Explain current configuration before promising any particular recovery or protection behaviour.

**Installed-name examples:** Black Ocarina, Blue Ocarina, Brown Ocarina, Collar, Cyan Ocarina, Gray Ocarina, Green Ocarina, Light Blue Ocarina, Light Gray Ocarina, Lime Ocarina, Magenta Ocarina, Ocarina, Orange Ocarina, Pet Roster, Pink Ocarina, Purple Ocarina, Red Ocarina, White Ocarina, Yellow Ocarina.

**Version:** 1.2.0. **File:** `mods/friends-for-life.pw.toml`. [Project page](https://www.curseforge.com/projects/1388097).


### Friends&Foes (Fabric/Quilt)

**Feature family:** Additional mobs. **Also serves:** Adventurer, Explorer, Collector, Mechanic.

Introduces mob-vote creatures and their associated behaviours, including helpful and hostile mobs. Split animal/companion discoveries from combat encounters and any utility-golem features.

**Installed-name examples:** Acacia Beehive, Bamboo Beehive, Birch Beehive, Buttercup, Cherry Beehive, Copper Button, Crab Egg, Crimson Beehive, Dark Oak Beehive, Exposed Copper Button, Exposed Lightning Rod, Jungle Beehive, Mangrove Beehive, Oak Beehive, Oxidized Copper Button, Oxidized Lightning Rod, Potted Buttercup, Spruce Beehive, Warped Beehive, Waxed Copper Button, Waxed Exposed Copper Button, Waxed Exposed Lightning Rod, Waxed Lightning Rod, Waxed Oxidized Copper Button, Waxed Oxidized Lightning Rod, Waxed Weathered Copper Button, Waxed Weathered Lightning Rod, Weathered Copper Button, Weathered Lightning Rod, Reach, Copper Golem, Crab, Glare, Iceologer, Mauler, Moobloom. Full extracted list in the HTML catalogue.

**Version:** 3.0.9. **File:** `mods/friends-and-foes.pw.toml`. [Project page](https://www.curseforge.com/projects/551364).


### More Axolotl Variants Mod

**Feature family:** Axolotl variants. **Also serves:** Collector, Explorer.

Additional axolotl appearances support aquarium, breeding and living-collection goals.

**Version:** 1.2.6. **File:** `mods/mavm.pw.toml`. [Project page](https://www.curseforge.com/projects/498797).


### No Animal Tempt Delay

**Feature family:** Animal handling. **Also serves:** —.

Removes the wait between attempts to attract animals with food; a handling convenience.

**Version:** 1.2. **File:** `mods/no-animal-tempt-delay.pw.toml`. [Project page](https://www.curseforge.com/projects/952356).


### Realistic Bees

**Feature family:** Beekeeping. **Also serves:** Farmer.

Changes bee size, spawns and hive capacity; teach beekeeping with the pack's actual rules.

**Version:** 4.2. **File:** `mods/realistic-bees.pw.toml`. [Project page](https://www.curseforge.com/projects/410743).


### Ribbits

**Feature family:** Frog communities. **Also serves:** Explorer, Merchant, Builder.

Frog inhabitants and their settlements provide discovery and interaction goals. Use the installed Ribbits content and its taming addon for a companion/community branch.

**Installed-name examples:** Brown Toadstool Block, Lush Lily Pad, Mossy Oak Door, Mossy Oak Fence, Mossy Oak Fence Gate, Mossy Oak Planks, Mossy Oak Slab, Mossy Oak Stairs, Red Toadstool Block, Swamp Daisy, Swamp Lantern, Toadstool, Toadstool Stem, Umbrella Leaf, Ribbit, Fisherman Ribbit Spawn Egg, Gardener Ribbit Spawn Egg, Maraca, Merchant Ribbit Spawn Egg, Nitwit Ribbit Spawn Egg, Sorcerer Ribbit Spawn Egg.

**Version:** 1.20.1-Fabric-3.0.5. **File:** `mods/ribbits.pw.toml`. [Project page](https://www.curseforge.com/projects/622967).


### Spawn

**Feature family:** Wildlife niches. **Also serves:** Angler, Farmer, Cook, Explorer, Builder, Collector.

Adds angler fish, tuna, seahorses, snails, hamsters and ants, with related food and decorative resources. Ant gardens/anthills, rotten wood, snail-shell materials, sunflowers, music and pottery collectibles broaden its scope beyond animals alone.

**Installed-name examples:** Ant Gardens, Ant Farm, Ant Mound, Anthill, Big Snail Shell, Cracked Rotten Planks, Fallen Leaves, Ghostly Mucus Block, Mucus, Mucus Block, Potted Sweet Berries, Rotten Door, Rotten Fence, Rotten Fence Gate, Rotten Log, Rotten Log Anthill, Rotten Planks, Rotten Slab, Rotten Stairs, Rotten Trapdoor, Rotten Wood, Snail Eggs, Snail Shell Tile Slab, Snail Shell Tile Stairs, Snail Shell Tiles, Stripped Rotten Log, Stripped Rotten Wood, Sunflower, Angler Fish, Ant, Hamster, Seahorse, Snail, Tuna, Angler Fish Spawn Egg, Ant Pupa. Full extracted list in the HTML catalogue.

**Version:** 1.0.3-fabric. **File:** `mods/spawn-mod.pw.toml`. [Project page](https://modrinth.com/mod/spawn-mod).


### Squish

**Feature family:** Baby animals. **Also serves:** Collector.

A sugar-themed item/mechanic keeps supported mobs as babies; a cosmetic animal-care branch whose species support needs checking in-game.

**Installed-name examples:** Hardened Sugar, Melted Sugar, Waxed Melted Sugar, Sugar Rush, Baby Creeper, Baby Enderman, Baby Iron Golem, Baby Skeleton, Bitter Candy, Bitter Sugar Shard, Ender Candy, Ender Essence, Explosive Candy, Explosive Essence, Hardened Sugar Shard, Lollipop, Poppy Candy, Poppy Essence, Skelly Candy, Skelly Essence, Squish Candy, Squish Essence, Squish Guidebook.

**Version:** 0.4-SNAPSHOT. **File:** `mods/squish.pw.toml`. [Project page](https://www.curseforge.com/projects/1383770).


### Tameable Ribbits

**Feature family:** Taming addon. **Also serves:** —.

The local mod metadata explicitly adds taming and sitting for Ribbits using slime balls.

**Version:** 1.0.0. **File:** `mods/tameableribbits-1.0.0.jar`. Source: local jar metadata/assets; no trusted project URL supplied.


### TameableMinisheep

**Feature family:** Taming addon. **Also serves:** —.

Makes Wilder Nature's minisheep tameable; belongs with minisheep care rather than a separate chapter.

**Version:** 1.0. **File:** `mods/tameableminisheep.pw.toml`. [Project page](https://www.curseforge.com/projects/1332726).


### TameableMossbloom

**Feature family:** Taming addon. **Also serves:** —.

Makes Clutter's Mossbloom tameable; connects that mixed-content mod to animal keeping.

**Version:** 1.0. **File:** `mods/tameablemossbloom.pw.toml`. [Project page](https://www.curseforge.com/projects/1332717).


## The Blacksmith


### Advanced Netherite (Fabric)

**Feature family:** Equipment tiers. **Also serves:** Adventurer.

Additional Netherite upgrade tiers provide late equipment goals. Coordinate with Mythic Upgrades and the pack's custom smithing recipes rather than assuming one universal linear upgrade tree.

**Installed-name examples:** Block of Netherite-Diamond, Block of Netherite-Emerald, Block of Netherite-Gold, Block of Netherite-Iron, Netherite-Diamond Axe, Netherite-Diamond Boots, Netherite-Diamond Chestplate, Netherite-Diamond Helmet, Netherite-Diamond Hoe, Netherite-Diamond Ingot, Netherite-Diamond Leggings, Netherite-Diamond Pickaxe, Netherite-Diamond Shovel, Netherite-Diamond Sword, Netherite-Emerald Axe, Netherite-Emerald Boots, Netherite-Emerald Chestplate, Netherite-Emerald Helmet, Netherite-Emerald Hoe, Netherite-Emerald Ingot, Netherite-Emerald Leggings, Netherite-Emerald Pickaxe, Netherite-Emerald Shovel, Netherite-Emerald Sword, Netherite-Gold Axe, Netherite-Gold Boots, Netherite-Gold Chestplate, Netherite-Gold Helmet, Netherite-Gold Hoe, Netherite-Gold Ingot, Netherite-Gold Leggings, Netherite-Gold Pickaxe, Netherite-Gold Shovel, Netherite-Gold Sword, Netherite-Iron Axe, Netherite-Iron Boots. Full extracted list in the HTML catalogue.

**Version:** 2.1.3-1.20.1. **File:** `mods/advanced-netherite-fabric.pw.toml`. [Project page](https://www.curseforge.com/projects/547881).


### Better Crossbows

**Feature family:** Crossbow equipment. **Also serves:** Adventurer.

Copper, gold, diamond and Netherite crossbows provide ranged equipment alternatives.

**Installed-name examples:** Copper Crossbow, Diamond Crossbow, Gold Crossbow, Netherite Crossbow.

**Version:** 1.0.1. **File:** `mods/better-crossbows.pw.toml`. [Project page](https://www.curseforge.com/projects/1402632).


### Better Than Mending

**Feature family:** Equipment repair. **Also serves:** Witch.

Changes Mending use/repair interaction; include as an equipment-maintenance rule, not a new magic school.

**Version:** 1.3.0. **File:** `mods/better-than-mending.pw.toml`. [Project page](https://www.curseforge.com/projects/264738).


### DarkSmelting - RPG Smelt Armor, Tools, Weapons

**Feature family:** Equipment recycling. **Also serves:** Mechanic.

Smelt equipment back into materials; consider it alongside the custom iron recycling rules when explaining recovery yields.

**Version:** 1.0.6. **File:** `mods/darksmelting.pw.toml`. [Project page](https://www.curseforge.com/projects/908418).


### Easy Anvils

**Feature family:** Repair and naming. **Also serves:** Witch, Builder.

Improved anvils with retained items and naming-related features; use for an equipment-maintenance workshop.

**Version:** 8.0.2. **File:** `mods/easy-anvils.pw.toml`. [Project page](https://www.curseforge.com/projects/682567).


### JustHammers

**Feature family:** Area mining. **Also serves:** Builder.

Hammer tool progression for breaking larger areas; the pack changes the impact-core recipe and retires competing Toolshed hammers.

**Installed-name examples:** Destruction Core, Diamond Destructor Hammer, Diamond Hammer, Diamond Impact Hammer, Diamond Reinforced Hammer, Diamond Reinforced Impact Hammer, Gold Destructor Hammer, Gold Hammer, Gold Impact Hammer, Gold Reinforced Hammer, Gold Reinforced Impact Hammer, Impact Core, Iron Destructor Hammer, Iron Hammer, Iron Impact Hammer, Iron Reinforced Hammer, Iron Reinforced Impact Hammer, Netherite Destructor Hammer, Netherite Hammer, Netherite Impact Hammer, Netherite Reinforced Hammer, Netherite Reinforced Impact Hammer, Reinforced Core, Reinforced Impact Core, Stone Destructor Hammer, Stone Hammer, Stone Impact Hammer, Stone Reinforced Hammer, Stone Reinforced Impact Hammer.

**Version:** 20.1.5+mc1.20.1. **File:** `mods/justhammers.pw.toml`. [Project page](https://www.curseforge.com/projects/681606).


### Mythic Upgrades

**Feature family:** Gem equipment. **Also serves:** Explorer, Adventurer, Collector.

Discover gem materials and craft specialised upgraded equipment. The pack names ruby, topaz, peridot, jade, aquamarine, sapphire and ametrine; it changes crafting and armor attributes and adds crystal block/shard/cluster conversions.

**Installed-name examples:** Ametrine Crystal Cluster, Ametrine Ore, Aquamarine Crystal Cluster, Aquamarine Ore, Block of Ametrine, Block of Ametrine Crystal, Block of Aquamarine, Block of Aquamarine Crystal, Block of Jade, Block of Jade Crystal, Block of Necoium, Block of Peridot, Block of Peridot Crystal, Block of Raw Necoium, Block of Ruby, Block of Ruby Crystal, Block of Sapphire, Block of Sapphire Crystal, Block of Topaz, Block of Topaz Crystal, Deepslate Aquamarine Ore, Deepslate Peridot Ore, Deepslate Sapphire Ore, Deepslate Topaz Ore, Jade Crystal Cluster, Jade Ore, Necoium Ore, Peridot Crystal Cluster, Peridot Ore, Ruby Crystal Cluster, Ruby Ore, Sapphire Crystal Cluster, Sapphire Ore, Topaz Crystal Cluster, Topaz Ore, Arcane Aura. Full extracted list in the HTML catalogue.

**Version:** 4.2.0+mc1.20.1. **File:** `mods/mythic-upgrades.pw.toml`. [Project page](https://www.curseforge.com/projects/663567).


### Obsidian Equipment Reworked

**Feature family:** Obsidian equipment. **Also serves:** Adventurer.

Adds an alternative equipment material family; the pack creates an Obsidian Upgrade Smithing Template and custom smithing rules.

**Installed-name examples:** Obsidian Axe, Obsidian Boots, Obsidian Chestplate, Obsidian Helmet, Obsidian Hoe, Obsidian Horse Armor, Obsidian Ingot, Obsidian Leggings, Obsidian Nautilus Armor, Obsidian Pickaxe, Obsidian Shovel, Obsidian Spear, Obsidian Sword, Obsidian Upgrade.

**Version:** 1.0. **File:** `mods/obsidian-equipment-reworked.pw.toml`. [Project page](https://www.curseforge.com/projects/1468750).


### Spelunkery

**Feature family:** Mining and mineral processing. **Also serves:** Explorer, Mechanic, Builder, Collector, Witch.

Rough gems and nuggets, diamond grindstone and polishing, salt/sulfur-related resources and underground materials; magnets, compaction, depth/navigation tools and mining devices. Ropes, rails, glowsticks and a parachute support caving; dimensional-tears and nephrite tools cross into utility/magic. The iron pick on a stick and charcoal lump are blacklisted, and compatibility ores in language files are not proof they generate.

**Installed-name examples:** Andesite Coal Ore, Andesite Copper Ore, Andesite Diamond Ore, Andesite Emerald Ore, Andesite Gold Ore, Andesite Iron Ore, Andesite Jade Ore, Andesite Lapis Lazuli Ore, Andesite Lead Ore, Andesite Redstone Ore, Andesite Silver Ore, Andesite Zinc Ore, Black Glowstick, Block of Cinnabar, Block of Dust, Block of Raw Magnetite, Block of Rough Cinnabar, Block of Rough Diamond, Block of Rough Emerald, Block of Rough Lazurite, Block of Rough Quartz, Block of Salt, Block of Saltpeter, Block of Sulfur, Blue Glowstick, Bramble of Tangle Roots, Brown Glowstick, Bunny Ears, Button Mushroom, Calcite Redstone Ore, Carved Nephrite, Cave Mushroom Stem, Compression Blast Miner, Conk Fungus, Conk Fungus Block, Crimini. Full extracted list in the HTML catalogue.

**Version:** 1.20.1-0.3.16. **File:** `mods/spelunkery.pw.toml`. [Project page](https://www.curseforge.com/projects/790530).


### Tokimi's Toolshed

**Feature family:** Specialist hand tools. **Also serves:** Farmer, Builder.

Excavators, scythes, lumber axes, clippers, trowel, abacus, chisels and copper buckets support earthworks, forestry, crops, detail work and measuring. The nine hammer recipes are removed and hidden by pack scripts; use JustHammers for that role. Other tool families remain relevant.

**Installed-name examples:** Abacus, Clippers, Copper Bucket, Copper Excavator, Copper Hammer, Copper Lava Bucket, Copper Lumber Axe, Copper Milk Bucket, Copper Powder Snow Bucket, Copper Scythe, Copper Water Bucket, Diamond Chisel, Diamond Excavator, Diamond Hammer, Diamond Lumber Axe, Diamond Scythe, Golden Excavator, Golden Hammer, Golden Lumber Axe, Golden Scythe, Iron Chisel, Iron Excavator, Iron Hammer, Iron Lumber Axe, Iron Scythe, Netherite Excavator, Netherite Hammer, Netherite Lumber Axe, Netherite Scythe, Obsidian Excavator, Obsidian Hammer, Obsidian Lumber Axe, Obsidian Scythe, Rose Gold Excavator, Rose Gold Hammer, Rose Gold Lumber Axe. Full extracted list in the HTML catalogue.

**Version:** 1.7. **File:** `mods/tokimistoolshed.pw.toml`. [Project page](https://www.curseforge.com/projects/1366151).


### Too Cheap!

**Feature family:** Anvil limits. **Also serves:** Witch.

Removes the anvil Too Expensive level-cost restriction, affecting long-term equipment maintenance.

**Version:** 1.4.0+mc1.20. **File:** `mods/too-cheap.pw.toml`. [Project page](https://modrinth.com/mod/too-cheap).


### Vein Mining (Fabric/Forge/Quilt)

**Feature family:** Mining enchantment. **Also serves:** Witch.

A configurable enchantment for mining connected groups of blocks; connect it to mining efficiency and enchanting.

**Installed-name examples:** Vein Mining.

**Version:** 1.5.0+1.20.1. **File:** `mods/vein-mining.pw.toml`. [Project page](https://www.curseforge.com/projects/431611).


## The Adventurer


### Bosses of Mass Destruction

**Feature family:** Boss encounters. **Also serves:** Explorer, Collector.

Dedicated boss content with unique encounters and rewards; build separate preparation and victory branches. Use the installed boss list and summon/acquisition requirements when drafting tasks.

**Installed-name examples:** Ancient Carved Blackstone, Blast Amplifier, Bramble Wall, Chiseled Stone Altar, Obsidian Altar, Obsidian Rune, Sealed Blackstone Bricks, Staff of Suppression, Table of Elevation, Void Blossom, Void Blossom Boss Spawner, Void Lily, Blue Fireball, Comet, Nether Gauntlet, Night Lich, Obsidilith, Petal Blade, Soul Star, Spore, Ancient Anima, Blazing Eye, Brimstone Nectar, Charged Ender Pearl, Crystal Fruit, Earthdive Spear, Obsidian Heart, Void Thorn.

**Version:** 1.7.5-1.20.1. **File:** `mods/bosses-of-mass-destruction.pw.toml`. [Project page](https://modrinth.com/mod/bosses-of-mass-destruction).


### Creeper Overhaul

**Feature family:** Creeper variants. **Also serves:** Explorer, Collector.

Biome-specific creepers expand encounter variety. Pack biome tags/modifiers extend selected spawn contexts; finding a variant is distinct from defeating it.

**Installed-name examples:** Potted Tiny Cactus, Tiny Cactus, Badlands Creeper, Bamboo Creeper, Beach Creeper, Cave Creeper, Dark Oak Creeper, Desert Creeper, Dripstone Creeper, Hills Creeper, Jungle Creeper, Mushroom Creeper, Ocean Creeper, Savannah Creeper, Snowy Creeper, Spruce Creeper, Swamp Creeper, Badlands Creeper Spawn Egg, Bamboo Creeper Spawn Egg, Beach Creeper Spawn Egg, Cave Creeper Spawn Egg, Dark Oak Creeper Spawn Egg, Desert Creeper Spawn Egg, Dripstone Creeper Spawn Egg, Hills Creeper Spawn Egg, Jungle Creeper Spawn Egg, Mushroom Creeper Spawn Egg, Ocean Creeper Spawn Egg, Savannah Creeper Spawn Egg, Snowy Creeper Spawn Egg, Spruce Creeper Spawn Egg, Swamp Creeper Spawn Egg.

**Version:** 3.0.2. **File:** `mods/creeper-overhaul.pw.toml`. [Project page](https://modrinth.com/mod/creeper-overhaul).


### Crossbow Enchants

**Feature family:** Crossbow enchantments. **Also serves:** Witch, Blacksmith.

Expands crossbow enchantment choices to support a dedicated ranged loadout.

**Version:** 1.4.0+1.20-1.20.4. **File:** `mods/crossbow-enchants.pw.toml`. [Project page](https://modrinth.com/mod/crossbow-enchants).


### Enderman Overhaul

**Feature family:** Enderman variants. **Also serves:** Explorer, Collector, Witch.

Biome-specific Endermen and distinct pearl-related content expand encounters and utility rewards; pack tags extend selected spawn contexts.

**Installed-name examples:** Tiny Skull, Ancient Pearl, Axolotl Pet Enderman, Badlands Enderman, Bubble Pearl, Cave Enderman, Coral Enderman, Corrupted Pearl, Crimson Forest Enderman, Crimson Pearl, Dark Oak Enderman, Desert Enderman, End Enderman, End Islands Enderman, Ender Bullet, Flower Fields Enderman, Hammerhead Pet Enderman, Ice Spikes Enderman, Icy Pearl, Mushroom Fields Enderman, Nether Wastes Enderman, Pet Enderman, Savanna Enderman, Scarab, Snowy Enderman, Soul Pearl, Soulsand Valley Enderman, Spirit, Summoner Pearl, Swamp Enderman, Warped Forest Enderman, Warped Pearl, Windswept Hills Enderman, Badlands Enderman Spawn Egg, Badlands Hood, Cave Enderman Spawn Egg. Full extracted list in the HTML catalogue.

**Version:** 1.0.4. **File:** `mods/enderman-overhaul.pw.toml`. [Project page](https://modrinth.com/mod/enderman-overhaul).


### Illager Invasion

**Feature family:** Illager threats. **Also serves:** Explorer, Merchant.

Additional illager enemies and structures/encounters; connect combat goals to protecting settlements and exploring hostile sites.

**Installed-name examples:** Imbuing Table, Magic Fire, Alchemist, Archivist, Basher, Firecaller, Inquisitor, Invoker, Marauder, Necromancer, Provoker, Sorcerer, Surrendered, Alchemist Spawn Egg, Archivist Spawn Egg, Basher Spawn Egg, Firecaller Spawn Egg, Hallowed Gem, Horn of Sight, Illusionary Dust, Illusioner Spawn Egg, Inquisitor Spawn Egg, Invoker Spawn Egg, Lost Candle, Magical Fire Charge, Marauder Spawn Egg, Necromancer Spawn Egg, Platinum Chunk, Platinum Infused Hatchet, Platinum Sheet, Primal Essence, Provoker Spawn Egg, Sorcerer Spawn Egg, Surrendered Spawn Egg, Unusual Dust.

**Version:** 8.0.7. **File:** `mods/illager-invasion.pw.toml`. [Project page](https://www.curseforge.com/projects/891324).


### Inventory Totem

**Feature family:** Survival rule. **Also serves:** —.

Totems can activate from the inventory, changing how players prepare for dangerous trips.

**Version:** 3.4. **File:** `mods/inventory-totem.pw.toml`. [Project page](https://www.curseforge.com/projects/349071).


### MmmMmmMmmMmm (Target Dummy)

**Feature family:** Equipment testing. **Also serves:** Blacksmith, Builder.

Target dummy for comparing weapons and damage; useful as a training-yard fixture and learning tool.

**Installed-name examples:** Target Dummy.

**Version:** 1.20-2.0.12. **File:** `mods/mmmmmmmmmmmm.pw.toml`. [Project page](https://www.curseforge.com/projects/225738).


### More Bows and Arrows | Major Update Available!

**Feature family:** Archery. **Also serves:** Blacksmith, Collector, Witch.

Material and special bows, diverse arrow types and related enchantments; installed examples include explosive, teleport-related and elemental/material arrows. Let players choose a useful ranged kit rather than craft every wood variant.

**Installed-name examples:** Anti-Gravity, Bonus Shot, Defensive Shot, Fluid Movement, Monster Hunter, Quick Pull, Tempo Thief, Amethyst Arrow, Bamboo Arrow, Blaze Rod Arrow, Bone Arrow, Cactus Arrow, Coal Arrow, Copper Arrow, Diamond Arrow, Emerald Arrow, Ender Pearl Arrow, Flint And Steel Arrow, Flint Arrow, Gold Arrow, Iron Arrow, Lapis Arrow, Moss Arrow, Netherite Arrow, Obsidian Arrow, Paper Arrow, REALLY Big Arrow, TNT Arrow, Acacia Bow, Amethyst Bow, Bamboo Bow, Birch Bow, Blaze Bow, Bone Bow, Cherry Bow, Coal Bow. Full extracted list in the HTML catalogue.

**Version:** 5.0.1. **File:** `mods/more-bows-and-arrows.pw.toml`. [Project page](https://www.curseforge.com/projects/888468).


### Pillager Caravans

**Feature family:** Roaming encounters. **Also serves:** Explorer, Merchant.

Biome-themed pillager convoys with guards and loot. The pack adds biome-tag bridges for caravans, so road encounters belong in exploration and defence rather than a stationary dungeon-only checklist.

**Version:** 3.0.0. **File:** `mods/pillager-caravans.pw.toml`. [Project page](https://modrinth.com/mod/pillager-caravans).


### Respect My Trims

**Feature family:** Armor-trim utility. **Also serves:** Blacksmith, Builder.

Gold armor trims pacify piglins, giving decorative equipment choices a practical Nether use.

**Version:** 1.0.0+mc1.20. **File:** `mods/respect-my-trims.pw.toml`. [Project page](https://www.curseforge.com/projects/1264714).


### Savage Ender Dragon

**Feature family:** Dragon encounter. **Also serves:** Explorer.

Changes the Ender Dragon fight with additional difficulty/mechanics. Treat the vanilla dragon milestone as a modified encounter in this pack.

**Version:** 1.20.1-4.7. **File:** `mods/savage-ender-dragon.pw.toml`. [Project page](https://www.curseforge.com/projects/523327).


### SwingThrough

**Feature family:** Combat controls. **Also serves:** —.

Target living entities through transparent blocks; explain as a combat convenience.

**Version:** 1.0.6+1.20. **File:** `mods/swingthrough.pw.toml`. [Project page](https://modrinth.com/mod/swingthrough).


### Variants&Ventures

**Feature family:** Regional enemies. **Also serves:** Explorer.

Additional regional hostile-mob variants; the pack provides spawn-biome tags for several named variants.

**Installed-name examples:** Gelid, Murk, Thicket, Verdant, Gelid Spawn Egg, Murk Spawn Egg, Thicket Spawn Egg, Verdant Spawn Egg.

**Version:** 1.0.26. **File:** `mods/variants-and-ventures.pw.toml`. [Project page](https://modrinth.com/mod/variants-and-ventures).


## The Merchant


### Chef's Delight [Fabric] - Farmer's Delight Villagers

**Feature family:** Food professions. **Also serves:** Cook.

Adds Cook and Chef villager professions; link kitchen production to trading and restaurant/market builds.

**Version:** 1.0.4-fabric-1.20.1. **File:** `mods/chefs-delight-fabric.pw.toml`. [Project page](https://www.curseforge.com/projects/736986).


### Guard Villagers (Fabric/Quilt)

**Feature family:** Village defence. **Also serves:** Adventurer, Rancher.

Village guards support settlement protection and equipment/defence planning.

**Installed-name examples:** Guard, Guard Spawn Egg.

**Version:** 2.0.9-1.20.1. **File:** `mods/guard-villagers-fabric.pw.toml`. [Project page](https://www.curseforge.com/projects/571503).


### Spud's shops

**Feature family:** Player shops. **Also serves:** Builder, Quartermaster.

Decorative shop blocks support player trading. Define the server's chosen currency and trade expectations separately; the mod's presence does not establish an economy policy.

**Installed-name examples:** Acacia Shelf Shop, Acacia Shop, Amethyst Windowsill Shop, Andesite Windowsill Shop, Bamboo Shelf Shop, Bamboo Shop, Birch Shelf Shop, Birch Shop, Blackstone Windowsill Shop, Calcite Windowsill Shop, Cherry Shelf Shop, Cherry Shop, Crimson Shelf Shop, Crimson Shop, Dark Oak Shelf Shop, Dark oak Shop, Deepslate Windowsill Shop, Dripstone Windowsill Shop, End Stone Windowsill Shop, Granite Windowsill Shop, Hook Shop, Jungle Shelf Shop, Jungle Shop, Mangrove Shelf Shop, Mangrove Shop, Merchant's Crate, Oak Shelf Shop, Oak Shop, Rug Shop Black, Rug Shop Blue, Rug Shop Brown, Rug Shop Cyan, Rug Shop Gray, Rug Shop Green, Rug Shop Light Blue, Rug Shop Light Gray. Full extracted list in the HTML catalogue.

**Version:** 1.9.0. **File:** `mods/spuds-shops.pw.toml`. [Project page](https://modrinth.com/mod/spuds-shops).


### Trade Cycling

**Feature family:** Trade selection. **Also serves:** —.

Cycle eligible villager trade offers through the mod's interaction; a trading convenience to explain once.

**Version:** 1.20.1-1.0.18. **File:** `mods/trade-cycling.pw.toml`. [Project page](https://www.curseforge.com/projects/570431).


### VillagersPlus (Fabric/Neoforge)

**Feature family:** Professions and trades. **Also serves:** Builder, Farmer.

New villagers/professions, trades and workstations; organize a functional market or village around what each profession supplies.

**Installed-name examples:** Acacia Flower Tub, Alchemist Table, Aquarium, Bamboo Flower Tub, Birch Flower Tub, Cherry Flower Tub, Crimson Flower Tub, Dark Oak Flower Tub, Enchanted Basin, Jungle Flower Tub, Mangrove Flower Tub, Oak Flower Tub, Spruce Flower Tub, Warped Flower Tub.

**Version:** 3.1. **File:** `mods/villagersplus.pw.toml`. [Project page](https://www.curseforge.com/projects/809542).


## The Quartermaster


### Carry On

**Feature family:** Moving objects. **Also serves:** Rancher, Builder.

Carry eligible containers/block entities and supported creatures using direct interaction; useful for moving house, organizing farms and arranging workshops.

**Version:** 2.1.2.7. **File:** `mods/carry-on.pw.toml`. [Project page](https://www.curseforge.com/projects/274259).


### CraftingPad (Fabric)

**Feature family:** Portable crafting. **Also serves:** Explorer.

A carried crafting-table item provides crafting access away from the base.

**Installed-name examples:** Crafting Pad.

**Version:** 1.0.12. **File:** `mods/craftingpad-fabric.pw.toml`. [Project page](https://www.curseforge.com/projects/308976).


### Crate Delight (Fabric)

**Feature family:** Produce storage. **Also serves:** Farmer, Cook, Builder.

Crates and bags for storing and displaying food resources; useful for pantries, farm stores and market stalls.

**Installed-name examples:** Apple Crate, Bag of Cocoa Beans, Bag of Ground Cinnamon, Bag of Gunpowder, Bag of Salt, Bag of Sugar, Banana Crate, Beetroot Crate, Beetroot Seeds Bag, Berry Crate, Blue Egg Crate, Blueberry Crate, Bread Bag, Brown Egg Crate, Brown Mushroom Crate, Caiman Egg Crate, Carrot Crate, Cinder Flour Bag, Cookie Bag, Crocodile Egg Crate, Duck Egg Crate, Egg Crate, Emu Egg Crate, Ender Dust Bag, Glow Berry Crate, Golden Apple Crate, Golden Carrot Crate, Kiwi Egg Crate, Kiwifruit Crate, Leaf Litter Bag, Melon Seeds Bag, Peanut Crate, Platypus Egg Crate, Poisonous Potato Crate, Potato Crate, Powdered Obsidian Bag. Full extracted list in the HTML catalogue.

**Version:** 26.07.01-1.20-fabric. **File:** `mods/crate-delight-fabric.pw.toml`. [Project page](https://www.curseforge.com/projects/957811).


### Create Contraption Terminals

**Feature family:** Mobile storage access. **Also serves:** Mechanic.

Use Tom's Simple Storage terminals on Create contraptions; connect mobile workshops and transport to storage access.

**Version:** 1.2.0. **File:** `mods/create-contraption-terminals.pw.toml`. [Project page](https://www.curseforge.com/projects/1059879).


### Create: Vibrant Vaults

**Feature family:** Warehouse styling. **Also serves:** Mechanic, Builder.

Additional Create item-vault appearances and variants for identifying and decorating factory storage.

**Installed-name examples:** Basic Shipping Container, Black Basic Shipping Container, Black Item Vault, Black Package Frogport, Black Packager, Black Redstone Requester, Black Shipping Container, Black Stock Link, Black Vertical Basic Shipping Container, Black Vertical Item Vault, Black Vertical Shipping Container, Blue Basic Shipping Container, Blue Item Vault, Blue Package Frogport, Blue Packager, Blue Redstone Requester, Blue Shipping Container, Blue Stock Link, Blue Vertical Basic Shipping Container, Blue Vertical Item Vault, Blue Vertical Shipping Container, Brown Basic Shipping Container, Brown Item Vault, Brown Package Frogport, Brown Packager, Brown Redstone Requester, Brown Shipping Container, Brown Stock Link, Brown Vertical Basic Shipping Container, Brown Vertical Item Vault, Brown Vertical Shipping Container, Cyan Basic Shipping Container, Cyan Item Vault, Cyan Package Frogport, Cyan Packager, Cyan Redstone Requester. Full extracted list in the HTML catalogue.

**Version:** 0.3.2+1.20.1. **File:** `mods/create-vibrant-vaults.pw.toml`. [Project page](https://modrinth.com/mod/create-vibrant-vaults).


### Iron Chests: Restocked

**Feature family:** Container tiers. **Also serves:** Builder.

Upgraded chest families expand storage capacity and organization beyond vanilla containers.

**Installed-name examples:** Copper Barrel, Copper Chest, Crystal Barrel, Crystal Chest, Diamond Barrel, Diamond Chest, Dirt Chest, Gold Barrel, Gold Chest, Iron Barrel, Iron Chest, Netherite Barrel, Netherite Chest, Obsidian Barrel, Obsidian Chest, %s : [X=%d, Y=%d, Z=%d], Blank Chest Upgrade, Chest Name: , Chest Position: [X=%d, Y=%d, Z=%d], Chest: %s, Copper Chest Upgrade, Crystal Chest Upgrade, Diamond Chest Upgrade, Diamond Dolly, Gold Chest Upgrade, Iron Chest Upgrade, Iron Dolly, Key, Key Ring, Lock, Netherite Chest Upgrade, Obsidian Chest Upgrade.

**Version:** 5.0.2. **File:** `mods/ironchests.pw.toml`. [Project page](https://www.curseforge.com/projects/498794).


### Sophisticated Backpacks (Unofficial Fabric port)

**Feature family:** Portable storage. **Also serves:** Explorer, Farmer.

Upgradeable backpacks provide capacity and functional inventory upgrades for travel, gathering and work.

**Installed-name examples:** Backpack, Copper Backpack, Diamond Backpack, Gold Backpack, Iron Backpack, Netherite Backpack, Advanced Compacting Upgrade, Advanced Deposit Upgrade, Advanced Feeding upgrade, Advanced Filter Upgrade, Advanced Jukebox Upgrade, Advanced Magnet Upgrade, Advanced Pickup Upgrade, Advanced Pump Upgrade, Advanced Refill Upgrade, Advanced Restock Upgrade, Advanced Tool Swapper Upgrade, Advanced Void Upgrade, Anvil Upgrade, Auto-blasting Upgrade, Auto-smelting Upgrade, Auto-smoking Upgrade, Battery Upgrade, Blasting Upgrade, Compacting Upgrade, Crafting Upgrade, Deposit Upgrade, Everlasting Upgrade, Experience Pump Upgrade, Feeding Upgrade, Filter Upgrade, Inception Upgrade, Infinity Upgrade (Admin), Jukebox Upgrade, Magnet Upgrade, Pickup Upgrade. Full extracted list in the HTML catalogue.

**Version:** 1.20.1-3.23.4.5.110. **File:** `mods/sophisticated-backpacks-unofficial-fabric-port.pw.toml`. [Project page](https://www.curseforge.com/projects/979322).


### Sophisticated Storage (Unofficial Fabric port)

**Feature family:** Upgraded containers. **Also serves:** Mechanic, Builder.

Upgradeable storage containers with capacity and functional upgrades support sorting and processing. The pack adds a barrel conversion and changes stack-upgrade balance.

**Installed-name examples:** %s%sBarrel, %s%sChest, %s%sCopper Barrel, %s%sCopper Chest, %s%sDiamond Barrel, %s%sDiamond Chest, %s%sGold Barrel, %s%sGold Chest, %s%sIron Barrel, %s%sIron Chest, %s%sNetherite Barrel, %s%sNetherite Chest, Copper Shulker Box, Decoration Table, Diamond Shulker Box, Gold Shulker Box, Iron Shulker Box, Limited %s%sBarrel I, Limited %s%sBarrel II, Limited %s%sBarrel III, Limited %s%sBarrel IV, Limited %s%sCopper Barrel I, Limited %s%sCopper Barrel II, Limited %s%sCopper Barrel III, Limited %s%sCopper Barrel IV, Limited %s%sDiamond Barrel I, Limited %s%sDiamond Barrel II, Limited %s%sDiamond Barrel III, Limited %s%sDiamond Barrel IV, Limited %s%sGold Barrel I, Limited %s%sGold Barrel II, Limited %s%sGold Barrel III, Limited %s%sGold Barrel IV, Limited %s%sIron Barrel I, Limited %s%sIron Barrel II, Limited %s%sIron Barrel III. Full extracted list in the HTML catalogue.

**Version:** 1.20.1-1.3.5.11.142. **File:** `mods/sophisticated-storage-unofficial-fabric-port.pw.toml`. [Project page](https://www.curseforge.com/projects/979326).


### Storage Drawers

**Feature family:** Bulk storage. **Also serves:** Mechanic, Farmer, Builder.

Compartment drawers, upgrades and connected storage organization suit bulk crops, mining materials and factory outputs.

**Installed-name examples:** Compacting Drawers (2-Tier), Compacting Drawers (3-Tier), Compacting Half Drawers (2-Tier), Compacting Half Drawers (3-Tier), Concealment Key Button, Drawer Controller, Drawer Controller IO, Drawer Key Button, Framed Compacting Drawers (2-Tier), Framed Compacting Drawers (3-Tier), Framed Compacting Half Drawers (2-Tier), Framed Compacting Half Drawers (3-Tier), Framed Drawer Controller, Framed Drawer Controller IO, Framing Table, Personal Key Button, Quantify Key Button, Balanced Fill Upgrade, Concealment Key, Conversion Upgrade, Creative Storage Upgrade, Creative Vending Upgrade, Detached Drawer, Drawer Key, Drawer Puller, Fill Level Upgrade, Hopper Upgrade, Illumination Upgrade, Keyring, Magnet Upgrade (I), Magnet Upgrade (II), Magnet Upgrade (III), Max Redstone Upgrade, Min Redstone Upgrade, Pause Key, Personal Key. Full extracted list in the HTML catalogue.

**Version:** 12.14.3. **File:** `mods/storagedrawers.pw.toml`. [Project page](https://modrinth.com/mod/storagedrawers).


### Storage Labels

**Feature family:** Storage labels. **Also serves:** Builder, Merchant.

Label containers and storage areas so shared workshops and warehouses are readable.

**Installed-name examples:** Label.

**Version:** 1.20-2.0.0. **File:** `mods/labels.pw.toml`. [Project page](https://www.curseforge.com/projects/688223).


### Tom's Simple Storage Mod (Fabric)

**Feature family:** Storage networks. **Also serves:** Mechanic, Builder.

Link containers into a searchable storage/crafting network; use connectors and terminals to make a central storeroom or workshop.

**Version:** 1.7.1. **File:** `mods/toms-storage-fabric.pw.toml`. [Project page](https://www.curseforge.com/projects/396826).


### Trash Cans

**Feature family:** Overflow disposal. **Also serves:** Mechanic.

Dedicated disposal blocks for unwanted resources; connect to storage overflow once players understand what is being discarded.

**Version:** 1.0.18. **File:** `mods/trash-cans.pw.toml`. [Project page](https://www.curseforge.com/projects/394535).


### Traveler's Backpack [Fabric]

**Feature family:** Travel backpacks. **Also serves:** Explorer, Collector.

A separate backpack system with distinctive variants, upgrades and utility features; show it as an alternative to Sophisticated Backpacks rather than making both mandatory.

**Installed-name examples:** Bat Traveler's Backpack, Bee Traveler's Backpack, Black Sleeping bag, Blaze Traveler's Backpack, Blue Sleeping bag, Bookshelf Traveler's Backpack, Brown Sleeping bag, Cactus Traveler's Backpack, Cake Traveler's Backpack, Chicken Traveler's Backpack, Coal Traveler's Backpack, Cow Traveler's Backpack, Creeper Traveler's Backpack, Cyan Sleeping bag, Diamond Traveler's Backpack, Dragon Traveler's Backpack, Emerald Traveler's Backpack, End Traveler's Backpack, Enderman Traveler's Backpack, Fox Traveler's Backpack, Ghast Traveler's Backpack, Gold Traveler's Backpack, Gray Sleeping bag, Green Sleeping bag, Hay Traveler's Backpack, Horse Traveler's Backpack, Iron Golem Traveler's Backpack, Iron Traveler's Backpack, Lapis Traveler's Backpack, Light Blue Sleeping bag, Light Gray Sleeping bag, Lime Sleeping bag, Magenta Sleeping bag, Magma Cube Traveler's Backpack, Melon Traveler's Backpack, Nether Traveler's Backpack. Full extracted list in the HTML catalogue.

**Version:** 9.1.55. **File:** `mods/travelers-backpack-fabric.pw.toml`. [Project page](https://www.curseforge.com/projects/541171).


## Shared foundations


### FTB Essentials (Forge & Fabric)

**Feature family:** Server conveniences. **Also serves:** Explorer, Merchant.

Utility commands depend on server configuration and permissions; include only the commands the server actually enables.

**Version:** 2001.2.3. **File:** `mods/ftb-essentials.pw.toml`. [Project page](https://www.curseforge.com/projects/410811).


### FTB Quests (Fabric)

**Feature family:** Quest framework. **Also serves:** —.

The chapter/task/reward framework being planned. Existing chapters are evidence of prior pack design, not a complete authority for the currently installed content.

**Installed-name examples:** Loot Crate Opener, Loot Crate Storage, Progress Screen, Quest Barrier, Quest Chest, Quest Detector, Quest Progress Detector, Stage Barrier, Task Screen, Task Screen (1x1), Task Screen (3x3), Task Screen (5x5), Task Screen (7x7), Custom Icon, Loot Crate, Missing Item, Quest Book, Task Screen Configurator.

**Version:** 2001.4.13. **File:** `mods/ftb-quests-fabric.pw.toml`. [Project page](https://www.curseforge.com/projects/438496).


### FTB Teams (Fabric)

**Feature family:** Quest teams. **Also serves:** —.

Team membership can support shared quest progress; decide the intended team experience when designing the chapters.

**Version:** 2001.3.1. **File:** `mods/ftb-teams-fabric.pw.toml`. [Project page](https://www.curseforge.com/projects/438497).


### Mob Explosion Griefing Gamerule

**Feature family:** World protection rules. **Also serves:** Builder, Adventurer.

Controls mob explosion damage independently from other mob griefing; record the server's chosen behaviour in onboarding.

**Version:** 2.1.0+1.20-1.20.2. **File:** `mods/mobexplosiongriefinggamerule.pw.toml`. [Project page](https://modrinth.com/mod/mobexplosiongriefinggamerule).


### Open Parties and Claims

**Feature family:** Teams and land. **Also serves:** Merchant, Builder.

Party creation, claims and configurable chunk-forceloading protect shared bases and support cooperation; explain allowed server settings in onboarding.

**Version:** 0.30.3. **File:** `mods/open-parties-and-claims.pw.toml`. [Project page](https://www.curseforge.com/projects/636608).


### Peaceful Hunger | UPDATED

**Feature family:** Food rules. **Also serves:** Cook, Farmer.

Keeps hunger relevant in Peaceful; food production can remain meaningful even without hostile combat.

**Version:** 2.2.0. **File:** `mods/peaceful-hunger.pw.toml`. [Project page](https://www.curseforge.com/projects/1034453).


### Preferred Gamerules

**Feature family:** World defaults. **Also serves:** —.

Provides default gamerule configuration; affects the environment of every path rather than adding a quest-content tree.

**Version:** 1.1.1+1.19.4. **File:** `mods/preferred-gamerules.pw.toml`. [Project page](https://modrinth.com/mod/preferred-gamerules).


### Starter Kit

**Feature family:** Starting supplies. **Also serves:** —.

Supplies configurable first-join gear. The pack has a Welcome kit and inactive role-kit files; their presence does not make the proposed paths preselected classes.

**Version:** 8.0. **File:** `mods/starter-kit.pw.toml`. [Project page](https://www.curseforge.com/projects/390717).


## Pack customization


### CozyStudios Core

**Feature family:** Inherited pack core. **Also serves:** —.

Shared support for CozyStudios pack features. Treat individually verified custom recipes/items as pack features; the core's presence does not imply a full additional gameplay system.

**Installed-name examples:** Arborist Table, Diamond Tranquil Lantern, Golden Tranquil Lantern, Kiln, Netherite Tranquil Lantern, Tranquil Lantern, Fernling, Mushling, Mystical Elk, Mystical Trader, AT Original Soundtrack Music Disc, Cozy Crumbs, Dayspring Music Disc, Fernling Spawn Egg, Golden Leaf, Homeward Music Disc, Jungle Horn, Mushling Spawn Egg, Mystical Berries, Mystical Elk Spawn Egg, Mystical Trader Spawn Egg, Windswept Music Disc.

**Version:** 2.1-1.20.1. **File:** `mods/cozystudios-core.pw.toml`. [Project page](https://www.curseforge.com/projects/1371145).


### Modrinth Logo Mod

**Feature family:** Pack branding. **Also serves:** Collector.

An item-based logo mod renamed by KubeJS to Homestead Logo Mod. Branding/quest display content is not a separate survival feature or profession.

**Installed-name examples:** Modrinth Logo.

**Version:** 1.3.4. **File:** `mods/modrinth-logo-mod.pw.toml`. [Project page](https://modrinth.com/mod/modrinth-logo-mod).


## Performance and fixes


### Clumps

**Feature family:** Performance and fixes. **Also serves:** —.

Improves runtime efficiency or corrects behaviour; not a separate activity or collection tree.

Short installed-metadata excerpt: “Clumps xp orbs together.”.

**Version:** 12.0.0.4. **File:** `mods/clumps.pw.toml`. [Project page](https://modrinth.com/mod/clumps).


### Concurrent Chunk Management Engine

**Feature family:** Performance and fixes. **Also serves:** —.

Improves runtime efficiency or corrects behaviour; not a separate activity or collection tree.

Short installed-metadata excerpt: “A Fabric mod designed to improve the chunk performance of Minecraft.”.

**Version:** 0.2.0+alpha.11.18. **File:** `mods/c2me.pw.toml`. [Project page](https://www.curseforge.com/projects/533097).


### CreateBetterFps

**Feature family:** Performance and fixes. **Also serves:** —.

Improves runtime efficiency or corrects behaviour; not a separate activity or collection tree.

Short installed-metadata excerpt: “Improve your Create FPS when shaderpack is on, up to 50%”.

**Version:** 1.1.2. **File:** `mods/createbetterfps.pw.toml`. [Project page](https://modrinth.com/mod/createbetterfps).


### Debugify

**Feature family:** Performance and fixes. **Also serves:** —.

Improves runtime efficiency or corrects behaviour; not a separate activity or collection tree.

Short installed-metadata excerpt: “Fixes Minecraft bugs found on the bug tracker License stuff: j-Tai's TieFix - Code used licensed under LGPLv3 FlashyReese's Sodium Extra -”.

**Version:** 1.20.1+2.0. **File:** `mods/debugify.pw.toml`. [Project page](https://www.curseforge.com/projects/596224).


### Enhanced Block Entities

**Feature family:** Performance and fixes. **Also serves:** —.

Improves runtime efficiency or corrects behaviour; not a separate activity or collection tree.

Short installed-metadata excerpt: “Optimize and customize block entity rendering with a more modern approach.”.

**Version:** 0.9+1.20. **File:** `mods/enhanced-block-entities.pw.toml`. [Project page](https://www.curseforge.com/projects/452046).


### Entity Culling

**Feature family:** Performance and fixes. **Also serves:** —.

Improves runtime efficiency or corrects behaviour; not a separate activity or collection tree.

Short installed-metadata excerpt: “This mod uses async path-tracing to hide Tiles/Entities that are not visible.”.

**Version:** 1.10.5. **File:** `mods/entityculling.pw.toml`. [Project page](https://modrinth.com/mod/entityculling).


### FastBoot

**Feature family:** Performance and fixes. **Also serves:** —.

Improves runtime efficiency or corrects behaviour; not a separate activity or collection tree.

Short installed-metadata excerpt: “FastBoot is a mod that made to reduce game loading time, by using mixins overwrites on game loading stage”.

**Version:** 1.2-fabric. **File:** `mods/fastboot.pw.toml`. [Project page](https://www.curseforge.com/projects/1030285).


### Faster Random

**Feature family:** Performance and fixes. **Also serves:** —.

Improves runtime efficiency or corrects behaviour; not a separate activity or collection tree.

Short installed-metadata excerpt: “Makes your game randomly faster!”.

**Version:** 5.1.0. **File:** `mods/faster-random.pw.toml`. [Project page](https://modrinth.com/mod/faster-random).


### FastQuit

**Feature family:** Performance and fixes. **Also serves:** —.

Improves runtime efficiency or corrects behaviour; not a separate activity or collection tree.

Short installed-metadata excerpt: “This mod lets you return to the Title Screen early while your world is still saving in the background.”.

**Version:** 3.0.0+1.20+. **File:** `mods/fastquit.pw.toml`. [Project page](https://www.curseforge.com/projects/708967).


### FerriteCore (Fabric)

**Feature family:** Performance and fixes. **Also serves:** —.

Improves runtime efficiency or corrects behaviour; not a separate activity or collection tree.

Short installed-metadata excerpt: “Reduces memory usage”.

**Version:** 6.0.1. **File:** `mods/ferritecore-fabric.pw.toml`. [Project page](https://www.curseforge.com/projects/459857).


### Icterine

**Feature family:** Performance and fixes. **Also serves:** —.

Improves runtime efficiency or corrects behaviour; not a separate activity or collection tree.

Short installed-metadata excerpt: “Optimize advancements that require obtaining items.”.

**Version:** 1.3.0. **File:** `mods/icterine.pw.toml`. [Project page](https://www.curseforge.com/projects/974774).


### ImmediatelyFast

**Feature family:** Performance and fixes. **Also serves:** —.

Improves runtime efficiency or corrects behaviour; not a separate activity or collection tree.

Short installed-metadata excerpt: “Speed up and optimize immediate mode rendering in Minecraft”.

**Version:** 1.5.5+1.20.4. **File:** `mods/immediatelyfast.pw.toml`. [Project page](https://www.curseforge.com/projects/686911).


### kennytvs-epic-force-close-loading-screen-mod-for-fabric

**Feature family:** Performance and fixes. **Also serves:** —.

Improves runtime efficiency or corrects behaviour; not a separate activity or collection tree.

Short installed-metadata excerpt: “Force closes the level receiving and resource pack loading screen instead of having to wait for the chunks you're in to be”.

**Version:** 2.1.1. **File:** `mods/forcecloseworldloadingscreen.pw.toml`. [Project page](https://modrinth.com/mod/forcecloseworldloadingscreen).


### Keybind Fix

**Feature family:** Performance and fixes. **Also serves:** —.

Improves runtime efficiency or corrects behaviour; not a separate activity or collection tree.

Short installed-metadata excerpt: “Fixes keybindings overwriting each other when set as a conflict, allowing both bindings to function (in game effects may still conflict)”.

**Version:** 1.0.0. **File:** `mods/keybind-fix.pw.toml`. [Project page](https://modrinth.com/mod/keybind-fix).


### Ksyxis

**Feature family:** Performance and fixes. **Also serves:** —.

Improves runtime efficiency or corrects behaviour; not a separate activity or collection tree.

Short installed-metadata excerpt: “Speed up your world loading by removing unneeded chunks.”.

**Version:** 1.4.3. **File:** `mods/ksyxis.pw.toml`. [Project page](https://www.curseforge.com/projects/537533).


### Let Me Despawn

**Feature family:** Performance and fixes. **Also serves:** —.

Improves runtime efficiency or corrects behaviour; not a separate activity or collection tree.

Short installed-metadata excerpt: “Tweaks mob despawn rules to prevent accidental persistent mobs to increase performance.”.

**Version:** 1.5.0. **File:** `mods/let-me-despawn.pw.toml`. [Project page](https://www.curseforge.com/projects/663477).


### Lithium (Fabric/NeoForge)

**Feature family:** Performance and fixes. **Also serves:** —.

Improves runtime efficiency or corrects behaviour; not a separate activity or collection tree.

Short installed-metadata excerpt: “Lithium is a free and open-source optimization mod for Minecraft which makes a wide range of performance improvements to the game.”.

**Version:** 0.11.4. **File:** `mods/lithium.pw.toml`. [Project page](https://www.curseforge.com/projects/360438).


### Load My F***ing Tags

**Feature family:** Performance and fixes. **Also serves:** —.

Improves runtime efficiency or corrects behaviour; not a separate activity or collection tree.

Short installed-metadata excerpt: “Simple mod that makes Tag Loading less of a Pain”.

**Version:** 1.1.1+1.21.9. **File:** `mods/lmft.pw.toml`. [Project page](https://www.curseforge.com/projects/656346).


### Memory Leak Fix

**Feature family:** Performance and fixes. **Also serves:** —.

Improves runtime efficiency or corrects behaviour; not a separate activity or collection tree.

Short installed-metadata excerpt: “A mod which fixes multiple memory leaks, both client-side & server-side”.

**Version:** 1.1.5. **File:** `mods/memoryleakfix.pw.toml`. [Project page](https://modrinth.com/mod/memoryleakfix).


### ModernFix

**Feature family:** Performance and fixes. **Also serves:** —.

Improves runtime efficiency or corrects behaviour; not a separate activity or collection tree.

Short installed-metadata excerpt: “Egregious, yet effective performance improvements for modern Minecraft”.

**Version:** 5.25.2+mc1.20.1. **File:** `mods/modernfix.pw.toml`. [Project page](https://www.curseforge.com/projects/790626).


### MoreCulling

**Feature family:** Performance and fixes. **Also serves:** —.

Improves runtime efficiency or corrects behaviour; not a separate activity or collection tree.

Short installed-metadata excerpt: “A mod that changes how multiple types of culling are handled in order to improve performance”.

**Version:** 1.20.1-0.24.5. **File:** `mods/moreculling.pw.toml`. [Project page](https://www.curseforge.com/projects/630104).


### Neruina - Ticking Entity Fixer

**Feature family:** Performance and fixes. **Also serves:** —.

Improves runtime efficiency or corrects behaviour; not a separate activity or collection tree.

Short installed-metadata excerpt: “This is a mod that prevents ticking entity and ticking block entity / tile entity crashes from bricking worlds.”.

**Version:** 3.3.3. **File:** `mods/neruina.pw.toml`. [Project page](https://www.curseforge.com/projects/851046).


### Not Enough Crashes (Fabric)

**Feature family:** Performance and fixes. **Also serves:** —.

Improves runtime efficiency or corrects behaviour; not a separate activity or collection tree.

Short installed-metadata excerpt: “Improves crashes in Minecraft - allows returning to title screen, blaming causing mods, and more.”.

**Version:** 4.4.9+1.20.1. **File:** `mods/not-enough-crashes.pw.toml`. [Project page](https://www.curseforge.com/projects/353890).


### Not Enough Recipe Book [NERB]

**Feature family:** Performance and fixes. **Also serves:** —.

Improves runtime efficiency or corrects behaviour; not a separate activity or collection tree.

Short installed-metadata excerpt: “Optimization tool that removes Minecraft's recipe book”.

**Version:** 0.4.1. **File:** `mods/notenoughrecipebook.pw.toml`. [Project page](https://www.curseforge.com/projects/738663).


### Packet Fixer

**Feature family:** Performance and fixes. **Also serves:** —.

Improves runtime efficiency or corrects behaviour; not a separate activity or collection tree.

Short installed-metadata excerpt: “A simple mod to solve various problems with packets/NBT's.”.

**Version:** 3.3.2. **File:** `mods/packet-fixer.pw.toml`. [Project page](https://www.curseforge.com/projects/689467).


### Remove Reloading Screen

**Feature family:** Performance and fixes. **Also serves:** —.

Improves runtime efficiency or corrects behaviour; not a separate activity or collection tree.

Short installed-metadata excerpt: “Makes resource packs load in the background, allowing you to do other things while waiting!”.

**Version:** 4.0.6.1+mc1.20.1-fabric. **File:** `mods/rrls.pw.toml`. [Project page](https://www.curseforge.com/projects/833233).


### Riding Mouse Fix

**Feature family:** Performance and fixes. **Also serves:** —.

Improves runtime efficiency or corrects behaviour; not a separate activity or collection tree.

Short installed-metadata excerpt: “Fixes the sluggishness of the mouse when riding on entities.”.

**Version:** 1.0.0. **File:** `mods/ridingmousefix.pw.toml`. [Project page](https://modrinth.com/mod/ridingmousefix).


### Sodium

**Feature family:** Performance and fixes. **Also serves:** —.

Improves runtime efficiency or corrects behaviour; not a separate activity or collection tree.

Short installed-metadata excerpt: “Sodium is a powerful rendering engine for Minecraft which greatly improves frame rates and micro-stutter, while fixing many graphical issues”.

**Version:** 0.5.13+mc1.20.1. **File:** `mods/sodium.pw.toml`. [Project page](https://www.curseforge.com/projects/394468).


### Structure Essentials

**Feature family:** Performance and fixes. **Also serves:** —.

Improves runtime efficiency or corrects behaviour; not a separate activity or collection tree.

Short installed-metadata excerpt: “Essential utilities for structures”.

**Version:** 1.20.1-5.0. **File:** `mods/structure-essentials-forge-fabric.pw.toml`. [Project page](https://www.curseforge.com/projects/832882).


### Structure Layout Optimizer

**Feature family:** Performance and fixes. **Also serves:** —.

Improves runtime efficiency or corrects behaviour; not a separate activity or collection tree.

Short installed-metadata excerpt: “An attempt at optimizing jigsaw generation”.

**Version:** 1.0.10. **File:** `mods/structure-layout-optimizer.pw.toml`. [Project page](https://www.curseforge.com/projects/1087831).


### StutterFix

**Feature family:** Performance and fixes. **Also serves:** —.

Improves runtime efficiency or corrects behaviour; not a separate activity or collection tree.

Short installed-metadata excerpt: “This mod limits the number of threads available for chunk generation in order to reduce stuttering.”.

**Version:** mc1.20.1-0.2.0. **File:** `mods/stutterfix.pw.toml`. [Project page](https://www.curseforge.com/projects/1409618).


## Visuals and sound


### 3D Skin Layers

**Feature family:** Visuals and sound. **Also serves:** —.

Changes presentation, animation, lighting, weather or audio; supports the experience without supplying its own profession.

Short installed-metadata excerpt: “Renders the player skin layer in 3d”.

**Version:** 1.11.2. **File:** `mods/3dskinlayers.pw.toml`. [Project page](https://modrinth.com/mod/3dskinlayers).


### [EMF] Entity Model Features

**Feature family:** Visuals and sound. **Also serves:** —.

Changes presentation, animation, lighting, weather or audio; supports the experience without supplying its own profession.

Short installed-metadata excerpt: “This is an expansion of the ETF mod, it adds support for OptiFine format Custom Entity Model (CEM) resource packs. While still”.

**Version:** 3.3.5. **File:** `mods/entity-model-features.pw.toml`. [Project page](https://modrinth.com/mod/entity-model-features).


### [ETF] Entity Texture Features

**Feature family:** Visuals and sound. **Also serves:** —.

Changes presentation, animation, lighting, weather or audio; supports the experience without supplying its own profession.

Short installed-metadata excerpt: “Adds support for resource-pack driven features for entity textures including some OptiFine features Supports OptiFine: - Random & Custom textures - Emissive”.

**Version:** 7.2.1. **File:** `mods/entitytexturefeatures.pw.toml`. [Project page](https://modrinth.com/mod/entitytexturefeatures).


### Advancement Plaques [Fabric]

**Feature family:** Visuals and sound. **Also serves:** —.

Changes presentation, animation, lighting, weather or audio; supports the experience without supplying its own profession.

Short installed-metadata excerpt: “Replaces standard advancement toasts with fancy plaques.”.

**Version:** 1.6.7. **File:** `mods/advancement-plaques-fabric.pw.toml`. [Project page](https://www.curseforge.com/projects/514882).


### AmbientSounds 6

**Feature family:** Visuals and sound. **Also serves:** —.

Changes presentation, animation, lighting, weather or audio; supports the experience without supplying its own profession.

Short installed-metadata excerpt: “Expands minecraft's ambient sounds.”.

**Version:** 6.3.8. **File:** `mods/ambientsounds.pw.toml`. [Project page](https://www.curseforge.com/projects/254284).


### Boat Item View

**Feature family:** Visuals and sound. **Also serves:** —.

Changes presentation, animation, lighting, weather or audio; supports the experience without supplying its own profession.

Short installed-metadata excerpt: “The Boat Item View mod allows you to view your held items whilst sitting in a moving boat.”.

**Version:** 0.0.5. **File:** `mods/boat-item-view.pw.toml`. [Project page](https://www.curseforge.com/projects/482160).


### Chat Heads

**Feature family:** Visuals and sound. **Also serves:** —.

Changes presentation, animation, lighting, weather or audio; supports the experience without supplying its own profession.

Short installed-metadata excerpt: “See who are you chatting with! This mod adds player heads next to their chat messages.”.

**Version:** 0.15.7. **File:** `mods/chat-heads.pw.toml`. [Project page](https://www.curseforge.com/projects/407206).


### CIT Resewn

**Feature family:** Visuals and sound. **Also serves:** —.

Changes presentation, animation, lighting, weather or audio; supports the experience without supplying its own profession.

Short installed-metadata excerpt: “Re-implements MCPatcher's CIT”.

**Version:** 1.2.2+1.20.1. **File:** `mods/cit-resewn.pw.toml`. [Project page](https://www.curseforge.com/projects/521427).


### Colorwheel

**Feature family:** Visuals and sound. **Also serves:** —.

Changes presentation, animation, lighting, weather or audio; supports the experience without supplying its own profession.

Short installed-metadata excerpt: “Allows you to use Iris Shaders with Flywheel”.

**Version:** 1.2.9+mc1.20.1. **File:** `mods/colorwheel.pw.toml`. [Project page](https://www.curseforge.com/projects/1254143).


### Colorwheel Patcher

**Feature family:** Visuals and sound. **Also serves:** —.

Changes presentation, animation, lighting, weather or audio; supports the experience without supplying its own profession.

Short installed-metadata excerpt: “Autopatch supported shaders to be compatible with Colorwheel”.

**Version:** 1.0.5+mc1.20.1. **File:** `mods/colorwheel-patcher.pw.toml`. [Project page](https://www.curseforge.com/projects/1285475).


### Continuity

**Feature family:** Visuals and sound. **Also serves:** —.

Changes presentation, animation, lighting, weather or audio; supports the experience without supplying its own profession.

Short installed-metadata excerpt: “Continuity is a Fabric mod that allows resource packs that use the OptiFine connected textures format, OptiFine emissive textures format (only for”.

**Version:** 3.0.0+1.20.1. **File:** `mods/continuity.pw.toml`. [Project page](https://www.curseforge.com/projects/531351).


### Cool Rain

**Feature family:** Visuals and sound. **Also serves:** —.

Changes presentation, animation, lighting, weather or audio; supports the experience without supplying its own profession.

Short installed-metadata excerpt: “Cool as hell local rain sounds”.

**Version:** 1.4.0-1.20.1. **File:** `mods/coolrain.pw.toml`. [Project page](https://modrinth.com/mod/coolrain).


### Drippy Loading Screen

**Feature family:** Visuals and sound. **Also serves:** —.

Changes presentation, animation, lighting, weather or audio; supports the experience without supplying its own profession.

Short installed-metadata excerpt: “Addon for FancyMenu to customize the loading screen.”.

**Version:** 3.1.0. **File:** `mods/drippy-loading-screen.pw.toml`. [Project page](https://www.curseforge.com/projects/511770).


### Eating Animation [Fabric]

**Feature family:** Visuals and sound. **Also serves:** —.

Changes presentation, animation, lighting, weather or audio; supports the experience without supplying its own profession.

Short installed-metadata excerpt: “This mod adds simple sprite animation when you eat or drink something.”.

**Version:** 1.20+1.9.61. **File:** `mods/eating-animation-fabric.pw.toml`. [Project page](https://www.curseforge.com/projects/527023).


### Euphoria Patches

**Feature family:** Visuals and sound. **Also serves:** —.

Shader customization/compatibility support; affects presentation rather than adding a survival content progression.

Short installed-metadata excerpt: “A mod that applies the Euphoria Patches add-on to Complementary Shaders. Enable and Change Euphoria Patches Settings in the shaderpack settings menu”.

**Version:** 1.8.6-r5.7.1-fabric. **File:** `mods/euphoria-patches.pw.toml`. [Project page](https://www.curseforge.com/projects/915902).


### Fadeless

**Feature family:** Visuals and sound. **Also serves:** —.

Changes presentation, animation, lighting, weather or audio; supports the experience without supplying its own profession.

Short installed-metadata excerpt: “Remove fade out animations”.

**Version:** 1.0.1. **File:** `mods/fadeless.pw.toml`. [Project page](https://www.curseforge.com/projects/861310).


### FancyMenu

**Feature family:** Visuals and sound. **Also serves:** —.

Changes presentation, animation, lighting, weather or audio; supports the experience without supplying its own profession.

Short installed-metadata excerpt: “Customize Minecraft's menus with ease!”.

**Version:** 3.8.1. **File:** `mods/fancymenu.pw.toml`. [Project page](https://www.curseforge.com/projects/367706).


### IllagerBlabber

**Feature family:** Visuals and sound. **Also serves:** —.

Changes presentation, animation, lighting, weather or audio; supports the experience without supplying its own profession.

Short installed-metadata excerpt: “Adds dynamically yapping Illagers! Why? Glad you asked!”.

**Version:** 1.0.0. **File:** `mods/illagerblabber.pw.toml`. [Project page](https://modrinth.com/mod/illagerblabber).


### Iris Shaders

**Feature family:** Visuals and sound. **Also serves:** —.

Changes presentation, animation, lighting, weather or audio; supports the experience without supplying its own profession.

Short installed-metadata excerpt: “A modern shaders mod for Minecraft intended to be compatible with existing OptiFine shader packs”.

**Version:** 1.7.6+mc1.20.1. **File:** `mods/irisshaders.pw.toml`. [Project page](https://www.curseforge.com/projects/455508).


### LambDynamicLights - Dynamic Lights

**Feature family:** Visuals and sound. **Also serves:** Explorer.

Changes presentation, animation, lighting, weather or audio; supports the experience without supplying its own profession.

Short installed-metadata excerpt: “The most feature-complete dynamic lighting mod for Fabric.”.

**Version:** 4.0.2+1.20.1. **File:** `mods/lambdynamiclights.pw.toml`. [Project page](https://modrinth.com/mod/lambdynamiclights).


### Not Enough Animations

**Feature family:** Visuals and sound. **Also serves:** —.

Changes presentation, animation, lighting, weather or audio; supports the experience without supplying its own profession.

Short installed-metadata excerpt: “Adding and improving animations in Third-Person.”.

**Version:** 1.12.4. **File:** `mods/not-enough-animations.pw.toml`. [Project page](https://modrinth.com/mod/not-enough-animations).


### Nuit

**Feature family:** Visuals and sound. **Also serves:** —.

Changes presentation, animation, lighting, weather or audio; supports the experience without supplying its own profession.

Short installed-metadata excerpt: “Adds custom skybox support to MC”.

**Version:** 0.7.3+mc1.20.1. **File:** `mods/nuit.pw.toml`. [Project page](https://modrinth.com/mod/nuit).


### Nuit Interop

**Feature family:** Visuals and sound. **Also serves:** —.

Changes presentation, animation, lighting, weather or audio; supports the experience without supplying its own profession.

Short installed-metadata excerpt: “FabricSkyBoxes Interoperability for MCPatcher/OptiFine Skies”.

**Version:** 1.3.6+mc1.20.1-build.50. **File:** `mods/nuit-interop.pw.toml`. [Project page](https://modrinth.com/mod/nuit-interop).


### Particle Rain

**Feature family:** Visuals and sound. **Also serves:** —.

Changes presentation, animation, lighting, weather or audio; supports the experience without supplying its own profession.

Short installed-metadata excerpt: “Replaces weather with prettier particle effects”.

**Version:** 4.0.0-beta.11. **File:** `mods/particle-rain.pw.toml`. [Project page](https://www.curseforge.com/projects/421897).


### Presence Footsteps

**Feature family:** Visuals and sound. **Also serves:** —.

Changes presentation, animation, lighting, weather or audio; supports the experience without supplying its own profession.

Short installed-metadata excerpt: “An overly complicated sound mod.”.

**Version:** 1.10.1+1.20.1. **File:** `mods/presence-footsteps.pw.toml`. [Project page](https://www.curseforge.com/projects/334259).


### Show Me Your Skin! (Hide armor)

**Feature family:** Visuals and sound. **Also serves:** —.

Changes presentation, animation, lighting, weather or audio; supports the experience without supplying its own profession.

Short installed-metadata excerpt: “A mod to hide or customize armor rendering.”.

**Version:** 1.9.0+1.20. **File:** `mods/show-me-your-skin.pw.toml`. [Project page](https://www.curseforge.com/projects/622010).


### Sound Physics Remastered

**Feature family:** Visuals and sound. **Also serves:** —.

Changes presentation, animation, lighting, weather or audio; supports the experience without supplying its own profession.

Short installed-metadata excerpt: “Provides realistic sound attenuation, reverberation, and absorption through blocks.”.

**Version:** 1.20.1-1.5.1. **File:** `mods/sound-physics-remastered.pw.toml`. [Project page](https://www.curseforge.com/projects/535489).


### Subtle Effects

**Feature family:** Visuals and sound. **Also serves:** —.

Changes presentation, animation, lighting, weather or audio; supports the experience without supplying its own profession.

Short installed-metadata excerpt: “Adding many new subtle details through particles and a few sounds”.

**Version:** 1.14.3. **File:** `mods/subtle-effects.pw.toml`. [Project page](https://modrinth.com/mod/subtle-effects).


### Sun and Moon Celestial Configuration

**Feature family:** Visuals and sound. **Also serves:** —.

Changes presentation, animation, lighting, weather or audio; supports the experience without supplying its own profession.

Short installed-metadata excerpt: “Celestial Configuration is a mod that allows one to change the size of the sun and moon to whatever size you wish!”.

**Version:** 1.1.2. **File:** `mods/sun-and-moon-celestial-configuration.pw.toml`. [Project page](https://www.curseforge.com/projects/656398).


### Tiny Item Animations

**Feature family:** Visuals and sound. **Also serves:** —.

Changes presentation, animation, lighting, weather or audio; supports the experience without supplying its own profession.

Short installed-metadata excerpt: “Adds a cute little animation when picking up items with your mouse.”.

**Version:** 1.20-1.1. **File:** `mods/tiny-item-animations.pw.toml`. [Project page](https://modrinth.com/mod/tiny-item-animations).


### Traveler's Titles (Fabric)

**Feature family:** Visuals and sound. **Also serves:** —.

Changes presentation, animation, lighting, weather or audio; supports the experience without supplying its own profession.

Short installed-metadata excerpt: “Epic, RPG-like titles when entering biomes & dimensions”.

**Version:** 1.20-Fabric-4.0.2. **File:** `mods/travelers-titles-fabric.pw.toml`. [Project page](https://www.curseforge.com/projects/590990).


### Typewriter Day Counter

**Feature family:** Visuals and sound. **Also serves:** —.

Changes presentation, animation, lighting, weather or audio; supports the experience without supplying its own profession.

Short installed-metadata excerpt: “Adds a daycounter, displaying at the start of each day”.

**Version:** 1.0. **File:** `mods/typewriter-daycounter.pw.toml`. [Project page](https://modrinth.com/mod/typewriter-daycounter).


### Visuality

**Feature family:** Visuals and sound. **Also serves:** —.

Changes presentation, animation, lighting, weather or audio; supports the experience without supplying its own profession.

Short installed-metadata excerpt: “Little visual improvements by adding a bunch of new particles.”.

**Version:** 0.7.1+1.20. **File:** `mods/visuality.pw.toml`. [Project page](https://www.curseforge.com/projects/521126).


### What Are They Up To (Watut)

**Feature family:** Visuals and sound. **Also serves:** —.

Changes presentation, animation, lighting, weather or audio; supports the experience without supplying its own profession.

Short installed-metadata excerpt: “Lets you see if players are typing, in a GUI, idle, with cool ingame visuals”.

**Version:** 1.20.1-1.2.3. **File:** `mods/what-are-they-up-to.pw.toml`. [Project page](https://www.curseforge.com/projects/945479).


## Interface and controls


### AdvancementInfo

**Feature family:** Interface and controls. **Also serves:** —.

Improves information, configuration, controls or inventory interaction; explain useful controls in shared onboarding.

Short installed-metadata excerpt: “Make it easier to see which advancements you have and what's missing.”.

**Version:** 1.20-fabric0.83.0-1.4. **File:** `mods/advancementinfo.pw.toml`. [Project page](https://www.curseforge.com/projects/403815).


### AppleSkin

**Feature family:** Interface and controls. **Also serves:** Cook, Farmer.

Shows additional hunger/saturation information for choosing meals and understanding food value.

Short installed-metadata excerpt: “Adds various food-related HUD improvements”.

**Version:** 2.5.2+mc1.20.1. **File:** `mods/appleskin.pw.toml`. [Project page](https://www.curseforge.com/projects/248787).


### Better Mount HUD

**Feature family:** Interface and controls. **Also serves:** —.

Improves information, configuration, controls or inventory interaction; explain useful controls in shared onboarding.

Short installed-metadata excerpt: “Improves the ingame HUD while riding a mount”.

**Version:** 1.2.2. **File:** `mods/better-mount-hud.pw.toml`. [Project page](https://www.curseforge.com/projects/475358).


### Bridging Mod

**Feature family:** Interface and controls. **Also serves:** Builder.

Improves information, configuration, controls or inventory interaction; explain useful controls in shared onboarding.

Short installed-metadata excerpt: “Adds bridging assist similar to Bedrock & Quark's building mechanics”.

**Version:** 2.5.1+1.20.1. **File:** `mods/bridging-mod.pw.toml`. [Project page](https://www.curseforge.com/projects/533942).


### Configured

**Feature family:** Interface and controls. **Also serves:** —.

Improves information, configuration, controls or inventory interaction; explain useful controls in shared onboarding.

Short installed-metadata excerpt: “Take control over minecraft's features.”.

**Version:** 1.3.1. **File:** `mods/configured.pw.toml`. [Project page](https://modrinth.com/mod/configured).


### Controlling

**Feature family:** Interface and controls. **Also serves:** —.

Improves information, configuration, controls or inventory interaction; explain useful controls in shared onboarding.

Short installed-metadata excerpt: “Adds the ability to search for keybinds using their name in the KeyBinding menu, this allows players to easily find a key”.

**Version:** 12.0.2. **File:** `mods/controlling.pw.toml`. [Project page](https://www.curseforge.com/projects/250398).


### Cubes Without Borders

**Feature family:** Interface and controls. **Also serves:** —.

Improves information, configuration, controls or inventory interaction; explain useful controls in shared onboarding.

Short installed-metadata excerpt: “Allows you to play Minecraft in a borderless fullscreen window.”.

**Version:** 3.0.0+mc1.20. **File:** `mods/cubes-without-borders.pw.toml`. [Project page](https://www.curseforge.com/projects/975120).


### Detail Armor Bar [Fabric]

**Feature family:** Interface and controls. **Also serves:** —.

Improves information, configuration, controls or inventory interaction; explain useful controls in shared onboarding.

Short installed-metadata excerpt: “Show more details of armors in Armor bar!”.

**Version:** 2.6.3+1.20.1-fabric. **File:** `mods/detail-armor-bar.pw.toml`. [Project page](https://www.curseforge.com/projects/506898).


### Enchantment Descriptions

**Feature family:** Interface and controls. **Also serves:** Witch, Blacksmith.

Improves information, configuration, controls or inventory interaction; explain useful controls in shared onboarding.

Short installed-metadata excerpt: “Adds descriptions of enchantments to their tooltip.”.

**Version:** 17.1.21. **File:** `mods/enchantment-descriptions.pw.toml`. [Project page](https://www.curseforge.com/projects/250419).


### Extreme sound muffler - Fabric

**Feature family:** Interface and controls. **Also serves:** —.

Improves information, configuration, controls or inventory interaction; explain useful controls in shared onboarding.

Short installed-metadata excerpt: “This mod allows you to muffle (almost) any sound selectively, allowing you to choose the volume of the sound you want between”.

**Version:** 3.51. **File:** `mods/extreme-sound-muffler-fabric-official.pw.toml`. [Project page](https://www.curseforge.com/projects/566140).


### Inventory HUD+

**Feature family:** Interface and controls. **Also serves:** —.

Improves information, configuration, controls or inventory interaction; explain useful controls in shared onboarding.

Short installed-metadata excerpt: “This mod will show you your inventory while playing. Enjoy!”.

**Version:** 3.4.26. **File:** `mods/inventory-hud-forge.pw.toml`. [Project page](https://www.curseforge.com/projects/357540).


### Jade Addons (Fabric)

**Feature family:** Interface and controls. **Also serves:** —.

Extends Jade information for supported modded blocks and systems.

Short installed-metadata excerpt: “Jade's additional mod supports for Fabric.”.

**Version:** 5.5.2+fabric. **File:** `mods/jade-addons-fabric.pw.toml`. [Project page](https://www.curseforge.com/projects/656665).


### Jade 🔍

**Feature family:** Interface and controls. **Also serves:** Shared foundations.

Identifies targeted blocks/entities and exposes supported information; helps newcomers understand unfamiliar content.

Short installed-metadata excerpt: “Minecraft mod shows what you are looking at. (Hwyla fork)”.

**Version:** 11.13.3+fabric. **File:** `mods/jade.pw.toml`. [Project page](https://www.curseforge.com/projects/324717).


### Just Enough Breeding (JEBr)

**Feature family:** Interface and controls. **Also serves:** Rancher.

Shows supported animal breeding information in the recipe viewer; a Rancher reference rather than an animal-content mod.

Short installed-metadata excerpt: “JEI/REI/EMI plugin that displays breeding information”.

**Version:** 3.0.1. **File:** `mods/justenoughbreeding.pw.toml`. [Project page](https://modrinth.com/mod/justenoughbreeding).


### Mod Menu

**Feature family:** Interface and controls. **Also serves:** —.

Improves information, configuration, controls or inventory interaction; explain useful controls in shared onboarding.

Short installed-metadata excerpt: “Adds a mod menu to view the list of mods you have installed.”.

**Version:** 7.2.2. **File:** `mods/modmenu.pw.toml`. [Project page](https://www.curseforge.com/projects/308702).


### Modern World Creation

**Feature family:** Interface and controls. **Also serves:** —.

Improves information, configuration, controls or inventory interaction; explain useful controls in shared onboarding.

Short installed-metadata excerpt: “Gives the Create World screen a makeover!”.

**Version:** 2.0.1. **File:** `mods/modernworldcreation.pw.toml`. [Project page](https://www.curseforge.com/projects/485245).


### More Enchantment Info

**Feature family:** Interface and controls. **Also serves:** Witch, Blacksmith.

Improves information, configuration, controls or inventory interaction; explain useful controls in shared onboarding.

Short installed-metadata excerpt: “Providing enchantment info to recipe viewer”.

**Version:** 0.2.0. **File:** `mods/more-enchantment-info.pw.toml`. [Project page](https://www.curseforge.com/projects/1166503).


### Mouse Tweaks

**Feature family:** Interface and controls. **Also serves:** —.

Improves information, configuration, controls or inventory interaction; explain useful controls in shared onboarding.

Short installed-metadata excerpt: “A mod that enhances the inventory management by adding various additional functions to the usual mouse buttons.”.

**Version:** 2.26. **File:** `mods/mouse-tweaks.pw.toml`. [Project page](https://www.curseforge.com/projects/60089).


### No Chat Reports

**Feature family:** Interface and controls. **Also serves:** —.

Improves information, configuration, controls or inventory interaction; explain useful controls in shared onboarding.

Short installed-metadata excerpt: “Strips cryptographic signatures from player messages, making it impossible to track and associate them with your Mojang/Microsoft account, as well as use”.

**Version:** 1.20.1-v2.2.3. **File:** `mods/no-chat-reports.pw.toml`. [Project page](https://www.curseforge.com/projects/634062).


### No Chat Restrictions

**Feature family:** Interface and controls. **Also serves:** —.

Improves information, configuration, controls or inventory interaction; explain useful controls in shared onboarding.

Short installed-metadata excerpt: “A mod dedicated to removing restrictions around the use of multiplayer features, including in-game chat.”.

**Version:** Fabric-MC1.20.1-v1.0.0. **File:** `mods/no-chat-restrictions.pw.toml`. [Project page](https://modrinth.com/mod/no-chat-restrictions).


### No Resource Pack Warnings

**Feature family:** Interface and controls. **Also serves:** —.

Improves information, configuration, controls or inventory interaction; explain useful controls in shared onboarding.

Short installed-metadata excerpt: “Disable warnings for outdated resource packs”.

**Version:** 1.3.1. **File:** `mods/no-resource-pack-warnings.pw.toml`. [Project page](https://www.curseforge.com/projects/627242).


### Puzzle

**Feature family:** Interface and controls. **Also serves:** —.

Improves information, configuration, controls or inventory interaction; explain useful controls in shared onboarding.

Short installed-metadata excerpt: “Unites optifine replacement mods in a clean & vanilla-style gui”.

**Version:** 2.2.0. **File:** `mods/puzzle.pw.toml`. [Project page](https://www.curseforge.com/projects/563977).


### Reese's Sodium Options

**Feature family:** Interface and controls. **Also serves:** —.

Improves information, configuration, controls or inventory interaction; explain useful controls in shared onboarding.

Short installed-metadata excerpt: “Replaces Sodium's Options Screen”.

**Version:** 1.7.2+mc1.20.1-build.101. **File:** `mods/reeses-sodium-options.pw.toml`. [Project page](https://www.curseforge.com/projects/511319).


### Roughly Enough Items (REI)

**Feature family:** Interface and controls. **Also serves:** Shared foundations.

Recipe and usage lookup across the pack; the first tool for checking effective crafting after custom scripts load.

Short installed-metadata excerpt: “Clean and Customizable.”.

**Version:** 12.1.785. **File:** `mods/rei.pw.toml`. [Project page](https://modrinth.com/mod/rei).


### Roughly Enough Professions (REP)

**Feature family:** Interface and controls. **Also serves:** Merchant.

Shows profession information in REI; useful when planning villager workstations and trades.

Short installed-metadata excerpt: “Adds info about professions to REI”.

**Version:** 2.0.2. **File:** `mods/roughly-enough-professions-rep.pw.toml`. [Project page](https://modrinth.com/mod/roughly-enough-professions-rep).


### Screenshot Viewer

**Feature family:** Interface and controls. **Also serves:** —.

Improves information, configuration, controls or inventory interaction; explain useful controls in shared onboarding.

Short installed-metadata excerpt: “A mod that allows you to see and manage (through right-clicking) your screenshots in game!”.

**Version:** 1.3.1-fabric-mc1.20. **File:** `mods/screenshot-viewer.pw.toml`. [Project page](https://www.curseforge.com/projects/693961).


### ScreenshotToClipboard

**Feature family:** Interface and controls. **Also serves:** —.

Improves information, configuration, controls or inventory interaction; explain useful controls in shared onboarding.

Short installed-metadata excerpt: “:)”.

**Version:** 1182~1204-1.1.0. **File:** `mods/screenshottoclipboard.pw.toml`. [Project page](https://www.curseforge.com/projects/1445937).


### Show Me What You Got

**Feature family:** Interface and controls. **Also serves:** —.

Improves information, configuration, controls or inventory interaction; explain useful controls in shared onboarding.

Short installed-metadata excerpt: “Allows displaying your items to other players in chat.”.

**Version:** 1.1.1. **File:** `mods/show-me-what-you-got.pw.toml`. [Project page](https://www.curseforge.com/projects/564941).


### Smooth Scrolling

**Feature family:** Interface and controls. **Also serves:** —.

Improves information, configuration, controls or inventory interaction; explain useful controls in shared onboarding.

Short installed-metadata excerpt: “Makes scrolling much more smooth”.

**Version:** 2.2.3.1. **File:** `mods/smooth-scroll.pw.toml`. [Project page](https://modrinth.com/mod/smooth-scroll).


### Sodium Extra

**Feature family:** Interface and controls. **Also serves:** —.

Improves information, configuration, controls or inventory interaction; explain useful controls in shared onboarding.

Short installed-metadata excerpt: “Features that shouldn't be in Sodium.”.

**Version:** 0.5.9+mc1.20.1. **File:** `mods/sodium-extra.pw.toml`. [Project page](https://www.curseforge.com/projects/447673).


### Sodium/Embeddium Extras

**Feature family:** Interface and controls. **Also serves:** —.

Improves information, configuration, controls or inventory interaction; explain useful controls in shared onboarding.

Short installed-metadata excerpt: “Collection of performance improvements and QOL features for Sodium”.

**Version:** 1.0.6. **File:** `mods/magnesium-extras.pw.toml`. [Project page](https://www.curseforge.com/projects/558905).


### Sort It Out!

**Feature family:** Interface and controls. **Also serves:** —.

Improves information, configuration, controls or inventory interaction; explain useful controls in shared onboarding.

Short installed-metadata excerpt: “A capable inventory sorting mod that works either client-side or server-side”.

**Version:** 1.5.0+1.20.1. **File:** `mods/sort-it-out.pw.toml`. [Project page](https://modrinth.com/mod/sort-it-out).


### Stack Refill

**Feature family:** Interface and controls. **Also serves:** —.

Improves information, configuration, controls or inventory interaction; explain useful controls in shared onboarding.

Short installed-metadata excerpt: “A quality of life mod which automatically refills the item in the hand of the player when using the final item if”.

**Version:** 4.9. **File:** `mods/stack-refill.pw.toml`. [Project page](https://www.curseforge.com/projects/411813).


### Stfu

**Feature family:** Interface and controls. **Also serves:** —.

A local convenience/fix mod. Metadata describes minor annoyance fixes; exact toggles were not independently verified, so no standalone gameplay claims are made.

Short installed-metadata excerpt: “A mod that fixes some minor annoyances!”.

**Version:** 1.2.3. **File:** `mods/Stfu-1.2.3.jar`. Source: local jar metadata/assets; no trusted project URL supplied.


### Tool Stats

**Feature family:** Interface and controls. **Also serves:** Blacksmith.

Improves information, configuration, controls or inventory interaction; explain useful controls in shared onboarding.

Short installed-metadata excerpt: “Adds tool stats to item tooltips.”.

**Version:** 16.0.10. **File:** `mods/tool-stats.pw.toml`. [Project page](https://www.curseforge.com/projects/377109).


### Tooltip Overhaul

**Feature family:** Interface and controls. **Also serves:** —.

Improves information, configuration, controls or inventory interaction; explain useful controls in shared onboarding.

Short installed-metadata excerpt: “Every tooltip, more modern, sharper, clearer”.

**Version:** 1.5.2. **File:** `mods/tooltip-overhaul.pw.toml`. [Project page](https://www.curseforge.com/projects/1327508).


### TrashSlot

**Feature family:** Interface and controls. **Also serves:** —.

Improves information, configuration, controls or inventory interaction; explain useful controls in shared onboarding.

Short installed-metadata excerpt: “Adds a trash slot to the inventory screen that allows deletion of unwanted items.”.

**Version:** 15.1.5. **File:** `mods/trashslot.pw.toml`. [Project page](https://www.curseforge.com/projects/235577).


### Xaero's Minimap

**Feature family:** Interface and controls. **Also serves:** Explorer.

Local minimap and navigation interface for finding the way around explored areas.

Short installed-metadata excerpt: “The most vanilla-looking minimap for Minecraft.”.

**Version:** 26.4.2. **File:** `mods/xaeros-minimap.pw.toml`. [Project page](https://www.curseforge.com/projects/263420).


### Xaero's World Map

**Feature family:** Interface and controls. **Also serves:** Explorer.

Exploration map for reviewing discovered terrain and planning routes.

Short installed-metadata excerpt: “A self-writing fullscreen map which also works as an add-on to Xaero's Minimap.”.

**Version:** 1.45.0. **File:** `mods/xaeros-world-map.pw.toml`. [Project page](https://www.curseforge.com/projects/317780).


### Zoomify

**Feature family:** Interface and controls. **Also serves:** —.

Improves information, configuration, controls or inventory interaction; explain useful controls in shared onboarding.

Short installed-metadata excerpt: “A zoom mod with infinite customizability.”.

**Version:** 2.15.1+1.20.1. **File:** `mods/zoomify.pw.toml`. [Project page](https://www.curseforge.com/projects/574741).


## Compatibility and integrations


### [Let's Do Addon] Compat

**Feature family:** Compatibility and integrations. **Also serves:** Farmer, Cook, Brewer.

Connects supported mods or resolves interactions; feature ownership remains with the participating content mods.

Short installed-metadata excerpt: “Adds compatibility between Let's Do and a plethora of mods sos you don't have to !”.

**Version:** 2.2.4. **File:** `mods/lets-do-addon-compat.pw.toml`. [Project page](https://www.curseforge.com/projects/992333).


### FTB XMod Compat

**Feature family:** Compatibility and integrations. **Also serves:** —.

Connects supported mods or resolves interactions; feature ownership remains with the participating content mods.

Short installed-metadata excerpt: “Provides cross-mod compatibility/integration for all main FTB mods”.

**Version:** 2.1.3. **File:** `mods/ftb-xmod-compat.pw.toml`. [Project page](https://www.curseforge.com/projects/889915).


### Indium

**Feature family:** Compatibility and integrations. **Also serves:** —.

Connects supported mods or resolves interactions; feature ownership remains with the participating content mods.

Short installed-metadata excerpt: “Sodium addon providing support for the Fabric Rendering API, based on Indigo”.

**Version:** 1.0.36+mc1.20.1. **File:** `mods/indium.pw.toml`. [Project page](https://www.curseforge.com/projects/459496).


### Loot Integrations

**Feature family:** Compatibility and integrations. **Also serves:** —.

Connects supported mods or resolves interactions; feature ownership remains with the participating content mods.

Short installed-metadata excerpt: “Integrates loot into loottables”.

**Version:** 1.20.1-4.7. **File:** `mods/loot-integrations.pw.toml`. [Project page](https://www.curseforge.com/projects/580689).


### Loot Integrations: ChoiceTheorem's Overhauled Village & Immersive Structures

**Feature family:** Compatibility and integrations. **Also serves:** —.

Connects additional loot to CTOV and Immersive Structures containers.

**Version:** 1.4. **File:** `mods/loot-integrations-choicetheorems-overhauled.pw.toml`. [Project page](https://www.curseforge.com/projects/1135500).


### Loot Integrations: Dungeons and Taverns

**Feature family:** Compatibility and integrations. **Also serves:** —.

Connects additional loot to Dungeons and Taverns structures.

**Version:** 1. **File:** `mods/loot-integrations-dungeons-and-taverns.pw.toml`. [Project page](https://www.curseforge.com/projects/1139414).


### Loot Integrations: Moog's Voyager, Soaring, End & Nether Structures

**Feature family:** Compatibility and integrations. **Also serves:** —.

Loot compatibility for supported Moog structure packs. Its name does not prove all named packs are installed.

**Version:** ${version}. **File:** `mods/loot-integrations-moogs-voyager-soaring-end-nether.pw.toml`. [Project page](https://www.curseforge.com/projects/1152715).


### Loot Integrations: Structory & Towers

**Feature family:** Compatibility and integrations. **Also serves:** —.

Loot compatibility for Structory and Structory Towers.

**Version:** ${version}. **File:** `mods/loot-integrations-structory-towers.pw.toml`. [Project page](https://www.curseforge.com/projects/1152720).


### Polymorph (Fabric/Forge/Quilt)

**Feature family:** Compatibility and integrations. **Also serves:** Shared foundations.

Connects supported mods or resolves interactions; feature ownership remains with the participating content mods.

Short installed-metadata excerpt: “No more recipe conflicts! Adds an option to choose the crafting result if more than one is available.”.

**Version:** 0.49.10+1.20.1. **File:** `mods/polymorph.pw.toml`. [Project page](https://www.curseforge.com/projects/388800).


### Polymorphic Tom's Simple Storag

**Feature family:** Compatibility and integrations. **Also serves:** Quartermaster.

Adds recipe-conflict selection integration to Tom's Simple Storage crafting interface.

Short installed-metadata excerpt: “tom”.

**Version:** 1.0.4. **File:** `mods/polymorphic-tom.pw.toml`. [Project page](https://www.curseforge.com/projects/1151978).


### Radiant Gear (Fabric/Forge/Quilt)

**Feature family:** Compatibility and integrations. **Also serves:** Explorer.

Connects accessory-slot equipment with dynamic-light support, relevant to carried/worn lighting.

Short installed-metadata excerpt: “A compatibility bridge between Curios API or Trinkets API and dynamic light mods such as Dynamic Lights, Lucent, and LambDynamicLights.”.

**Version:** 2.1.6+1.20.1. **File:** `mods/radiant-gear.pw.toml`. [Project page](https://www.curseforge.com/projects/602199).


### Yung Structures Addon for Loot Integrations

**Feature family:** Compatibility and integrations. **Also serves:** —.

Loot compatibility for supported YUNG structure mods.

**Version:** ${version}. **File:** `mods/yung-structures-addon-for-loot-integrations.pw.toml`. [Project page](https://www.curseforge.com/projects/1012211).


## Pack and admin tools


### Chunky (Fabric)

**Feature family:** Pack and admin tools. **Also serves:** —.

Supports pack configuration, maintenance, diagnostics or authoring; not a normal survival profession.

Short installed-metadata excerpt: “Pre-generates chunks, quickly, efficiently, and safely”.

**Version:** 1.3.146. **File:** `mods/chunky-pregenerator.pw.toml`. [Project page](https://www.curseforge.com/projects/433175).


### CraftTweaker

**Feature family:** Pack and admin tools. **Also serves:** —.

Pack scripts change crafting, smithing, Create processing, tags and attributes. The complete local script index is included below.

Short installed-metadata excerpt: “Customize your minecraft experience!”.

**Version:** 14.0.60. **File:** `mods/crafttweaker.pw.toml`. [Project page](https://www.curseforge.com/projects/239197).


### Default Options

**Feature family:** Pack and admin tools. **Also serves:** —.

Supports pack configuration, maintenance, diagnostics or authoring; not a normal survival profession.

Short installed-metadata excerpt: “A way for modpacks to ship a default (key) configuration without having to include an options.txt file. Also allows local options from”.

**Version:** 18.0.4. **File:** `mods/default-options.pw.toml`. [Project page](https://www.curseforge.com/projects/232131).


### Item Obliterator (Modpack Utils Series)

**Feature family:** Pack and admin tools. **Also serves:** —.

Supports pack configuration, maintenance, diagnostics or authoring; not a normal survival profession.

Short installed-metadata excerpt: “Allows modpack devs to completely disable items and other misc features.”.

**Version:** 2.3.0. **File:** `mods/item-obliterator.pw.toml`. [Project page](https://www.curseforge.com/projects/835861).


### KubeJS

**Feature family:** Pack and admin tools. **Also serves:** —.

Pack scripting supplies custom items, recipes, loot and data changes. Those gameplay additions are catalogued in the pack-specific section.

Short installed-metadata excerpt: “Customize your modpack or server with JavaScript!”.

**Version:** 2001.6.5-build.26. **File:** `mods/kubejs.pw.toml`. [Project page](https://www.curseforge.com/projects/238086).


### KubeJS Create for Fabric

**Feature family:** Pack and admin tools. **Also serves:** —.

Supports pack configuration, maintenance, diagnostics or authoring; not a normal survival profession.

Short installed-metadata excerpt: “Create addon for KubeJS”.

**Version:** 2001.2.4-build.9999. **File:** `mods/kubejs-create-for-fabric-1-20-1.pw.toml`. [Project page](https://www.curseforge.com/projects/1082589).


### Log Begone

**Feature family:** Pack and admin tools. **Also serves:** —.

Supports pack configuration, maintenance, diagnostics or authoring; not a normal survival profession.

Short installed-metadata excerpt: “I hate log spam, don't you?”.

**Version:** 1.0.8. **File:** `mods/log-begone.pw.toml`. [Project page](https://www.curseforge.com/projects/623560).


### Log Cleaner

**Feature family:** Pack and admin tools. **Also serves:** —.

Supports pack configuration, maintenance, diagnostics or authoring; not a normal survival profession.

Short installed-metadata excerpt: “A lightweight mod that cleans old, unused log files”.

**Version:** 1.0.0. **File:** `mods/log-cleaner.pw.toml`. [Project page](https://www.curseforge.com/projects/667884).


### Mixin Conflict Helper

**Feature family:** Pack and admin tools. **Also serves:** —.

Supports pack configuration, maintenance, diagnostics or authoring; not a normal survival profession.

Short installed-metadata excerpt: “User-friendly errors for Mixin conflicts.”.

**Version:** 1.2.0. **File:** `mods/mixin-conflict-helper.pw.toml`. [Project page](https://www.curseforge.com/projects/643052).


### MixinTrace

**Feature family:** Pack and admin tools. **Also serves:** —.

Supports pack configuration, maintenance, diagnostics or authoring; not a normal survival profession.

Short installed-metadata excerpt: “Adds a list of mixins in the stack trace to crash reports”.

**Version:** 1.1.1+1.17. **File:** `mods/mixintrace.pw.toml`. [Project page](https://www.curseforge.com/projects/433447).


### Open Loader

**Feature family:** Pack and admin tools. **Also serves:** —.

Supports pack configuration, maintenance, diagnostics or authoring; not a normal survival profession.

Short installed-metadata excerpt: “An open source data and resource loader.”.

**Version:** 19.0.5. **File:** `mods/open-loader.pw.toml`. [Project page](https://www.curseforge.com/projects/354339).


### Packwiz Modpack Loader

**Feature family:** Pack and admin tools. **Also serves:** —.

Supports pack configuration, maintenance, diagnostics or authoring; not a normal survival profession.

Short installed-metadata excerpt: “Updates packwiz using commands”.

**Version:** 3.1.0+1.19. **File:** `mods/packwiz-modpack-loader.pw.toml`. [Project page](https://modrinth.com/mod/packwiz-modpack-loader).


### Quests Additions (Fabric)

**Feature family:** Pack and admin tools. **Also serves:** —.

Adds task/reward capabilities to FTB Quests; a quest-authoring extension rather than an independent profession.

Short installed-metadata excerpt: “An addon for the FTB quests mod. It adds some tasks and rewards that are missing in the base mod.”.

**Version:** 1.4.6. **File:** `mods/quests-additions-fabric.pw.toml`. [Project page](https://www.curseforge.com/projects/580136).


### spark

**Feature family:** Pack and admin tools. **Also serves:** —.

Supports pack configuration, maintenance, diagnostics or authoring; not a normal survival profession.

Short installed-metadata excerpt: “spark is a performance profiling plugin/mod for Minecraft clients, servers and proxies.”.

**Version:** 1.10.53. **File:** `mods/spark.pw.toml`. [Project page](https://www.curseforge.com/projects/361579).


### Sparse Structures

**Feature family:** Pack and admin tools. **Also serves:** Explorer.

Controls structure spacing; canonical config uses general factor 1.2 and mansion override 2, with further pack structure overrides.

Short installed-metadata excerpt: “Makes all structures more spread out. Configurable. If you want to support me, you can use code MAX at BisectHosting for 25%”.

**Version:** 3.0. **File:** `mods/sparse-structures.pw.toml`. [Project page](https://www.curseforge.com/projects/911437).


### StackDeobfuscator

**Feature family:** Pack and admin tools. **Also serves:** —.

Supports pack configuration, maintenance, diagnostics or authoring; not a normal survival profession.

Short installed-metadata excerpt: “Deobfuscates stacktraces to yarn/quilt/mojang mappings”.

**Version:** 1.4.3+08e71cc. **File:** `mods/stackdeobf.pw.toml`. [Project page](https://www.curseforge.com/projects/840896).


### WorldEdit

**Feature family:** Pack and admin tools. **Also serves:** Builder.

Administrative/creative world editing; do not make operator permissions a survival Builder requirement.

Short installed-metadata excerpt: “WorldEdit is an easy-to-use in-game world editor for Minecraft, supporting both single- and multi-player.”.

**Version:** 7.2.15+6463-5ca4dff. **File:** `mods/worldedit.pw.toml`. [Project page](https://modrinth.com/mod/worldedit).


### WorldEdit CUI (Fabric)

**Feature family:** Pack and admin tools. **Also serves:** Builder.

Visual selection interface for WorldEdit; primarily an administrative or creative building aid.

Short installed-metadata excerpt: “Client-side user interface for WorldEdit”.

**Version:** 1.20+01. **File:** `mods/worldeditcui-fabric.pw.toml`. [Project page](https://www.curseforge.com/projects/402098).


### Your Options Shall Be Respected (YOSBR)

**Feature family:** Pack and admin tools. **Also serves:** —.

Supports pack configuration, maintenance, diagnostics or authoring; not a normal survival profession.

Short installed-metadata excerpt: “Your options shall be respected.”.

**Version:** 0.1.2. **File:** `mods/yosbr.pw.toml`. [Project page](https://www.curseforge.com/projects/374274).


## Libraries and APIs


### [Let's Do] API 

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “This is an API for the Let's do mods”.

**Version:** 1.2.15. **File:** `mods/do-api.pw.toml`. [Project page](https://www.curseforge.com/projects/864599).


### Accessories

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “A extendable and data-driven Accessory Mod for Minecraft”.

**Version:** 1.0.0-beta.48+1.20.1. **File:** `mods/accessories.pw.toml`. [Project page](https://www.curseforge.com/projects/938917).


### Almanac Lib

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “Loader independent library mod for frikinjay's mods”.

**Version:** 1.0.2. **File:** `mods/almanac-lib.pw.toml`. [Project page](https://www.curseforge.com/projects/1115285).


### Architectury API

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “A intermediary api aimed to ease developing multiplatform mods.”.

**Version:** 9.2.14. **File:** `mods/architectury-api.pw.toml`. [Project page](https://modrinth.com/mod/architectury-api).


### Athena

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “Crossplatform Baked Model Loader”.

**Version:** 3.1.2. **File:** `mods/athena.pw.toml`. [Project page](https://www.curseforge.com/projects/841890).


### AzureLib

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “Java Minecraft mod using Bedrock models to create custom models and animations for items, blocks, entities”.

**Version:** 3.0.27. **File:** `mods/azurelib.pw.toml`. [Project page](https://www.curseforge.com/projects/817423).


### Balm

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “Abstraction Layer (but not really)™ for Blay's multiplatform mods”.

**Version:** 7.3.38. **File:** `mods/balm-fabric-1.20.1-7.3.38.jar`. [Project page](https://mods.twelveiterations.com/).


### BCLib

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “A library for BetterX team mods”.

**Version:** 3.0.14. **File:** `mods/bclib.pw.toml`. [Project page](https://modrinth.com/mod/bclib).


### Bookshelf

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “A library for building other mods.”.

**Version:** 20.2.15. **File:** `mods/bookshelf.pw.toml`. [Project page](https://www.curseforge.com/projects/228525).


### Cardinal Components API

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “Attaching more data to various game objects”.

**Version:** 5.2.3. **File:** `mods/cardinal-components-api.pw.toml`. [Project page](https://www.curseforge.com/projects/318449).


### CarrasconLib

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “A library for ECarrascon Mods”.

**Version:** 1.20.1-0.1. **File:** `mods/carrasconlib.pw.toml`. [Project page](https://www.curseforge.com/projects/1215789).


### CICADA

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “Confusing, Interesting and Considerably Agnostic Development Aid”.

**Version:** 0.14.3+1.20.1. **File:** `mods/cicada.pw.toml`. [Project page](https://www.curseforge.com/projects/989574).


### Cloth Config API

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “An API for config screens.”.

**Version:** 11.1.136. **File:** `mods/cloth-config.pw.toml`. [Project page](https://modrinth.com/mod/cloth-config).


### Collective

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “Collective is a shared library with common code for all of Serilum's mods.”.

**Version:** 8.22. **File:** `mods/collective.pw.toml`. [Project page](https://www.curseforge.com/projects/342584).


### Common Network

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “This mod unifies networking in to a single location to work with Forge and Fabric, so developers only need to work in”.

**Version:** 1.0.5-1.20.1. **File:** `mods/common-network.pw.toml`. [Project page](https://modrinth.com/mod/common-network).


### Configurable

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “Config library that allows decentralised settings in a mod”.

**Version:** 2.2.3. **File:** `mods/configurable.pw.toml`. [Project page](https://www.curseforge.com/projects/1092048).


### CorgiLib

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “Library with handy utilities.”.

**Version:** 4.0.3.5. **File:** `mods/corgilib.pw.toml`. [Project page](https://www.curseforge.com/projects/693313).


### CoroUtil

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “It utils”.

**Version:** 1.20.1-1.3.7. **File:** `mods/coroutil.pw.toml`. [Project page](https://www.curseforge.com/projects/237749).


### CraterLib

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “A Modding API used by First Dark Development Mods”.

**Version:** 3.1.1. **File:** `mods/craterlib.pw.toml`. [Project page](https://www.curseforge.com/projects/867099).


### CreativeCore

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “A simple but powerful coremod.”.

**Version:** 2.12.36. **File:** `mods/creativecore.pw.toml`. [Project page](https://www.curseforge.com/projects/257814).


### Cristel Lib

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “A Library mod for easy structure config and runtime datapacks.”.

**Version:** 1.1.5. **File:** `mods/cristel-lib.pw.toml`. [Project page](https://www.curseforge.com/projects/856996).


### Cupboard

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

**Version:** 1.20.1-3.9. **File:** `mods/cupboard.pw.toml`. [Project page](https://www.curseforge.com/projects/326652).


### Data Anchor

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “Simple mod with helpful data attaching and networking utilities including attaching data to entities, chunks, players, and worlds with low boilerplate code.”.

**Version:** 1.0.0.22. **File:** `mods/data-anchor.pw.toml`. [Project page](https://www.curseforge.com/projects/1203668).


### Deimos Lib

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “Configuration and data generation library”.

**Version:** 2.4. **File:** `mods/deimos-fabric-forge-neoforge.pw.toml`. [Project page](https://www.curseforge.com/projects/1158094).


### Deltabox Lib

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “A library mod for all my other mods”.

**Version:** 2.2.0. **File:** `mods/deltaboxlib.pw.toml`. [Project page](https://www.curseforge.com/projects/973463).


### Fabric API

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “Core API module providing key hooks and intercompatibility features.”.

**Version:** 0.92.12+1.20.1. **File:** `mods/fabric-api.pw.toml`. [Project page](https://modrinth.com/mod/fabric-api).


### Fabric Language Kotlin

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “Fabric language module for Kotlin.”.

**Version:** 1.13.13+kotlin.2.4.10. **File:** `mods/fabric-language-kotlin.pw.toml`. [Project page](https://modrinth.com/mod/fabric-language-kotlin).


### Faux Custom Entity Data

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

**Version:** 6.0.1. **File:** `mods/faux-custom-entity-data.pw.toml`. [Project page](https://www.curseforge.com/projects/575305).


### Forge Config API Port

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “Forge's whole config system provided to the Fabric ecosystem. Designed for a multiloader architecture.”.

**Version:** 8.0.3. **File:** `mods/forge-config-api-port.pw.toml`. [Project page](https://www.curseforge.com/projects/547434).


### Fragmentum

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “The lightweight framework for the Obscuria Collection cross-platform mods.”.

**Version:** 1.5.2. **File:** `mods/fragmentum.pw.toml`. [Project page](https://modrinth.com/mod/fragmentum).


### FrozenLib

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “A library that contains many tools for modders. Includes advanced math operations, noise sampling, advanced sounds, entity texture overrides, structure pool element”.

**Version:** 1.9.3-mc1.20.1. **File:** `mods/frozenlib.pw.toml`. [Project page](https://modrinth.com/mod/frozenlib).


### FTB Filter System

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “Smart and highly configurable item filtering system with useful GUI configuration”.

**Version:** 20.0.1. **File:** `mods/ftb-filter-system.pw.toml`. [Project page](https://www.curseforge.com/projects/943925).


### FTB Library (Fabric)

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “Foundational library for FTB mods.”.

**Version:** 2001.2.9. **File:** `mods/ftb-library-fabric.pw.toml`. [Project page](https://www.curseforge.com/projects/438495).


### Fzzy Config

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “Configuration engine with automatic GUI generation, client-server syncing, powerful validation and error handling, and much more.”.

**Version:** 0.7.6+1.20.1. **File:** `mods/fzzy-config.pw.toml`. [Project page](https://modrinth.com/mod/fzzy-config).


### Geckolib

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “GeckoLib is an animation engine for Minecraft Mods, with support for complex 3D keyframe-based animations, 30+ easings, concurrent animation support, sound and”.

**Version:** 4.8.4. **File:** `mods/geckolib.pw.toml`. [Project page](https://modrinth.com/mod/geckolib).


### Iceberg [Fabric]

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “A library containing events, helpers, and utilities to make modding easier.”.

**Version:** 1.1.25. **File:** `mods/iceberg-fabric.pw.toml`. [Project page](https://www.curseforge.com/projects/539382).


### JamLib

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “The platform-agnostic library used in all of JamCore's mods”.

**Version:** 1.3.6+1.20.1-patch.1. **File:** `mods/jamlib.pw.toml`. [Project page](https://modrinth.com/mod/jamlib).


### Kiwi 🥝 (Fabric)

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “Minecraft modding library”.

**Version:** 11.10.3+fabric. **File:** `mods/kiwi-fabric.pw.toml`. [Project page](https://www.curseforge.com/projects/549404).


### Konkrete [Fabric] [MOVED TO NEW PAGE]

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “Konkrete Copyright Â© 2020-2024 Keksuccino. Konkrete is licensed under Apache-2.0. | Open Imaging Copyright Â© 2014 Dhyan Blum. Open Imaging is licensed”.

**Version:** 1.8.1. **File:** `mods/konkrete-fabric.pw.toml`. [Project page](https://www.curseforge.com/projects/416797).


### Lavender API

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “Apparently Lavender and Patchouli are really similar-looking flowers. Oh yeah, also this is a Guidebook API”.

**Version:** 0.1.9+1.20. **File:** `mods/lavender-api.pw.toml`. [Project page](https://www.curseforge.com/projects/962916).


### Library Ferret - Fabric

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “Shared code for my mod.”.

**Version:** 4.0.0. **File:** `mods/library-ferret-fabric.pw.toml`. [Project page](https://www.curseforge.com/projects/532730).


### Lithostitched

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “Library mod with new configurability and compatibility enhancements for worldgen.”.

**Version:** 1.4.11. **File:** `mods/lithostitched.pw.toml`. [Project page](https://www.curseforge.com/projects/936015).


### MaLiLib

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “A library mod required by masa's client-side mods”.

**Version:** 0.16.3. **File:** `mods/malilib.pw.toml`. [Project page](https://www.curseforge.com/projects/303119).


### MCPitanLib

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “Pitan's Minecraft Mod Library”.

**Version:** 3.6.8-1.20.1-fabric. **File:** `mods/mcpitanlibarch.pw.toml`. [Project page](https://www.curseforge.com/projects/682213).


### Melody

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “OpenAL-based library mod for playing background music. | Melody © Copyright 2023 Keksuccino. Melody is licensed under MIT.”.

**Version:** 1.0.3. **File:** `mods/melody.pw.toml`. [Project page](https://www.curseforge.com/projects/938643).


### MidnightLib

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “Lightweight config library with config screens and commands.”.

**Version:** 1.9.3. **File:** `mods/midnightlib.pw.toml`. [Project page](https://www.curseforge.com/projects/488090).


### ModMenu Badges Lib

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

**Version:** 2023.6.1. **File:** `mods/modmenu-badges-lib.pw.toml`. [Project page](https://www.curseforge.com/projects/914586).


### MonoLib

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “A non-invasive library mod for Fabric and (Neo)Forge. Thanks to Jared, Darkhax, Serilum, and PacifistMC.”.

**Version:** 4.1.0. **File:** `mods/monolib.pw.toml`. [Project page](https://www.curseforge.com/projects/968432).


### Moog's Structure Lib (moogs_structures)

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “A library mod for generating structures”.

**Version:** 3.1.2. **File:** `mods/moogs-structure-lib.pw.toml`. [Project page](https://www.curseforge.com/projects/1337167).


### Moonlight Lib

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “Custom Villagers AI and Map Markers, First and third person item animations, dynamic assets and registration & more”.

**Version:** 1.20-2.16.34. **File:** `mods/selene.pw.toml`. [Project page](https://www.curseforge.com/projects/499980).


### More Axolotl Variants API

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “Implementation of new axolotl variants.”.

**Version:** 1.1.4. **File:** `mods/mavapi.pw.toml`. [Project page](https://www.curseforge.com/projects/709964).


### Necronomicon API

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “An utility library for my mods!”.

**Version:** 1.6.0. **File:** `mods/necronomicon.pw.toml`. [Project page](https://modrinth.com/mod/necronomicon).


### Oh The Trees You'll Grow

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “A Minecraft library that aims to give users incredible configurability by allowing the creation of trees with Minecraft's structure template `.nbt` files.”.

**Version:** 1.7.0. **File:** `mods/oh-the-trees-youll-grow.pw.toml`. [Project page](https://www.curseforge.com/projects/962544).


### Omnilib

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “Omnilib is a framework for exploring new possibilities in Minecraft modding.”.

**Version:** 0.1.4. **File:** `mods/omnilib.pw.toml`. [Project page](https://modrinth.com/mod/omnilib).


### oωo (owo-lib)

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “yes its bad i know thanks”.

**Version:** 0.11.2+1.20. **File:** `mods/owo-lib.pw.toml`. [Project page](https://www.curseforge.com/projects/532610).


### PandaLib

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “A multipurpose library with a Config API, Model Renderer API, a bit of utility code, and more.”.

**Version:** 0.5.2. **File:** `mods/pandalib.pw.toml`. [Project page](https://www.curseforge.com/projects/975460).


### Patchouli (Fabric/Quilt)

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “Patchouli: Accessible, Data-Driven, Dependency-Free Documentation for Minecraft Modders and Pack Makers”.

**Version:** 1.20.1-85-FABRIC. **File:** `mods/patchouli-fabric.pw.toml`. [Project page](https://www.curseforge.com/projects/393236).


### Pehkui

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “Allows resizing of most entities.”.

**Version:** 3.8.2+1.14.4-1.20.6. **File:** `mods/pehkui.pw.toml`. [Project page](https://www.curseforge.com/projects/319596).


### Platform

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “Cross-Platform library mod based on Architectury to access both Forge and Fabric APIs”.

**Version:** 1.3.4. **File:** `mods/platform.pw.toml`. [Project page](https://www.curseforge.com/projects/997634).


### PneumonoCore

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “Library mod for Pneumono's mods.”.

**Version:** 1.3.1. **File:** `mods/pneumono_core.pw.toml`. [Project page](https://modrinth.com/mod/pneumono_core).


### Prism [Fabric]

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “A library all about color! Provides lots of color-related functionality for dependent mods.”.

**Version:** 1.0.5. **File:** `mods/prism-fabric.pw.toml`. [Project page](https://www.curseforge.com/projects/665526).


### Puzzles Lib

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “Why's it called Puzzles you ask? That's the puzzle!”.

**Version:** 8.1.33. **File:** `mods/puzzles-lib.pw.toml`. [Project page](https://www.curseforge.com/projects/495476).


### Resourceful Config

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “Resourceful Config is a mod that allows for developers to make cross-platform configs”.

**Version:** 2.1.3. **File:** `mods/resourceful-config.pw.toml`. [Project page](https://modrinth.com/mod/resourceful-config).


### Resourceful Lib

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “Library Mod by Team Resourceful”.

**Version:** 2.1.29. **File:** `mods/resourceful-lib.pw.toml`. [Project page](https://modrinth.com/mod/resourceful-lib).


### Rhino

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “A fork of Mozilla's Rhino library, modified for use in mods”.

**Version:** 2001.2.3-build.10. **File:** `mods/rhino.pw.toml`. [Project page](https://www.curseforge.com/projects/416294).


### Searchables

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “A library mod to facilitate adding search bars with auto complete and search types.”.

**Version:** 1.0.3. **File:** `mods/searchables.pw.toml`. [Project page](https://www.curseforge.com/projects/858542).


### ShatterLib | OctoLib

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “Collection of shared code for OctoStudios' mods”.

**Version:** 0.5.0.1. **File:** `mods/shatterbyte-lib.pw.toml`. [Project page](https://www.curseforge.com/projects/916747).


### SmartBrainLib

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “A library mod for smarter Brains and easier usage of the Brain system.”.

**Version:** 1.15. **File:** `mods/smartbrainlib.pw.toml`. [Project page](https://modrinth.com/mod/smartbrainlib).


### Sodium/Embeddium Options API

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “Cross-platform Sodium config event API for Sodium 1.21 and Embeddium 1.20”.

**Version:** 1.0.10. **File:** `mods/sodium-options-api.pw.toml`. [Project page](https://www.curseforge.com/projects/1103431).


### Sophisticated Core (Unofficial Fabric port)

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “A library / shared functionality mod for Sophisticated Storage and Backpacks”.

**Version:** 1.20.1-1.2.7.15.166. **File:** `mods/sophisticated-core-unofficial-fabric-port.pw.toml`. [Project page](https://www.curseforge.com/projects/979317).


### SuperMartijn642's Core Lib

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “SuperMartijn642's Core Lib adds lots of basic implementations for guis that allow for similar code between Minecraft 1.12, 1.14, 1.15, and 1.16!”.

**Version:** 1.1.18+a. **File:** `mods/supermartijn642s-core-lib.pw.toml`. [Project page](https://www.curseforge.com/projects/454372).


### TerraBlender (Fabric)

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “A library mod for adding biomes in a simple and compatible manner with Minecraft's new biome/terrain system.”.

**Version:** 3.0.1.10. **File:** `mods/terrablender-fabric.pw.toml`. [Project page](https://www.curseforge.com/projects/565956).


### Trinkets (Fabric)

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “Adds a data-driven accessory system to Minecraft”.

**Version:** 3.7.2. **File:** `mods/trinkets.pw.toml`. [Project page](https://www.curseforge.com/projects/341284).


### TxniLib

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “Yet Another Library Mod”.

**Version:** 1.0.24. **File:** `mods/txnilib.pw.toml`. [Project page](https://www.curseforge.com/projects/1104882).


### YetAnotherConfigLib (YACL)

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “YetAnotherConfigLib (yacl) is just that. A builder-based configuration library for Minecraft.”.

**Version:** 3.6.6+1.20.1-fabric. **File:** `mods/yacl.pw.toml`. [Project page](https://modrinth.com/mod/yacl).


### YUNG's API (Fabric)

**Feature family:** Libraries and APIs. **Also serves:** —.

Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.

Short installed-metadata excerpt: “API Library for YUNG's minecraft mods.”.

**Version:** 1.20-Fabric-4.0.6. **File:** `mods/yungs-api-fabric.pw.toml`. [Project page](https://www.curseforge.com/projects/421649).


## Complete custom-script index

Every .zs and gameplay/client .js file is listed here; item/tag references are indexed in the HTML appendix. These include removals and compatibility references, not only additions.

- `scripts/mods/[Let's Do] Brewery/hops_based_beers.zs`
- `scripts/mods/AlcoCraft+/keg_test.zs`
- `scripts/mods/Compat/appletrinketfix.zs`
- `scripts/mods/Compat/bater_wucket.zs`
- `scripts/mods/Compat/butterfly_wings.zs`
- `scripts/mods/Compat/explorers_compass.zs`
- `scripts/mods/Compat/farmland_fix.zs`
- `scripts/mods/Compat/flour.zs`
- `scripts/mods/Compat/hammer_changes.zs`
- `scripts/mods/Compat/loot_table_fixes.zs`
- `scripts/mods/Compat/mod_compat.zs`
- `scripts/mods/Compat/obsidian_tool_tagging.zs`
- `scripts/mods/Compat/questbook_recipefix.zs`
- `scripts/mods/Compat/remove_prismarite_cluster_trim.zs`
- `scripts/mods/Compat/rope_arrow.zs`
- `scripts/mods/Compat/stack_upgrade_balance.zs`
- `scripts/mods/Compat/stone.zs`
- `scripts/mods/Create/coin_smelting.zs`
- `scripts/mods/Create/create_milk.zs`
- `scripts/mods/Create/ore_processing/main_processing.zs`
- `scripts/mods/Create/ore_processing/silver_additions.zs`
- `scripts/mods/Create/peaceful_blaze_burner.zs`
- `scripts/mods/Create/renewables/renewables_compacting.zs`
- `scripts/mods/Create/renewables/renewables_crushing.zs`
- `scripts/mods/Create/renewables/renewables_deploying.zs`
- `scripts/mods/Create/renewables/renewables_haunting.zs`
- `scripts/mods/Create/renewables/renewables_mixing.zs`
- `scripts/mods/Create/renewables/renewables_pressing.zs`
- `scripts/mods/Create/renewables/renewables_splashing.zs`
- `scripts/mods/Create/renewables/sandpaper_polishing.zs`
- `scripts/mods/Create/vault.zs`
- `scripts/mods/Custom/amd_drivers.zs`
- `scripts/mods/Custom/custom_smithing.zs`
- `scripts/mods/Custom/elytra.zs`
- `scripts/mods/Custom/logo.zs`
- `scripts/mods/Custom/lyn.zs`
- `scripts/mods/Custom/mama.zs`
- `scripts/mods/Custom/nametag.zs`
- `scripts/mods/Custom/nvidia_graphics_card.zs`
- `scripts/mods/Custom/plushies.zs`
- `scripts/mods/Custom/ram.zs`
- `scripts/mods/Custom/saddle.zs`
- `scripts/mods/Custom/shiitake_mushroom_soup.zs`
- `scripts/mods/Custom/template.zs`
- `scripts/mods/Custom/tuff.zs`
- `scripts/mods/Mythic Upgrades/armor_attribute_buff.zs`
- `scripts/mods/Mythic Upgrades/armor_crafting.zs`
- `scripts/mods/Spelunkery/ironpickonastick.zs`
- `kubejs/server_scripts/amethyst.js`
- `kubejs/server_scripts/charcoal_haunting.js`
- `kubejs/server_scripts/cluster_recipes.js`
- `kubejs/server_scripts/copper_nugget.js`
- `kubejs/server_scripts/flour.js`
- `kubejs/server_scripts/furnace_fix.js`
- `kubejs/server_scripts/hats.js`
- `kubejs/server_scripts/hops_based_beer.js`
- `kubejs/server_scripts/iron_recycling.js`
- `kubejs/server_scripts/misc.js`
- `kubejs/server_scripts/remove_broken_compat_recipes.js`
- `kubejs/server_scripts/resin.js`
- `kubejs/server_scripts/retire_toolshed_hammers.js`
- `kubejs/server_scripts/supplementaries_presents.js`
- `kubejs/server_scripts/suppsquared_daub.js`
- `kubejs/startup_scripts/amd_drivers.js`
- `kubejs/startup_scripts/homestead.js`
- `kubejs/startup_scripts/lyn.js`
- `kubejs/startup_scripts/mortar.js`
- `kubejs/startup_scripts/nvidia_graphics_card.js`
- `kubejs/startup_scripts/obsidian_template.js`
- `kubejs/startup_scripts/ram.js`
- `kubejs/startup_scripts/shiitake_mushroom_soup.js`
- `kubejs/client_scripts/example.js`
- `kubejs/client_scripts/retire_toolshed_hammers.js`