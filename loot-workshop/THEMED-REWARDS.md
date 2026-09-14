# Themed rewards test pass

Loot Tidy 0.3.0 adds a separate optional bonus roll to each configured profile. Sources remain structure-rewards.json and structure-routes.json; build.py generates config/forced-relocation-rewards.json. Update the jar and config together, then restart.

114 distinct reward IDs now span ordinary materials, Create transmission parts and casings, food, seeds, ingredients, eight Hexalia brews, compasses, advanced materials and finished equipment. Counts are small. A bonus grants a single selection, never a complete equipment set. Existing native loot remains intact.

| Theme | Main roll | Separate bonus |
|---|---|---|
| Village / farm / kitchen | Guaranteed varied supplies | None |
| Workshop / medium | Guaranteed supplies | 8% one machinery part |
| Navigation | Guaranteed travel supplies | 10% compass: 7.5% Nature's, 2.5% Explorer's overall |
| Magic | Guaranteed herbs or brews | 6% magical resource/tool |
| Water | Guaranteed food or supplies | 6% diving equipment/pump |
| Armoury / hard | Guaranteed materials | 4% individual armour/tool |
| Nether | 85% supplies | 4% individual armour/tool |
| End | Guaranteed themed supplies | 10% advanced material or equipment |

The End bonus includes topaz, aquamarine and ametrine ingots (one each), obsidian armour pieces and netherite armour/tools. With current weights the total netherite chance is about 2.6% per mapped End container, distributed across six pieces; one specific piece is about 0.43%. Lootr refresh settings still matter for repeat farming.

127 routes were reassigned by theme or corrected dimension. End City treasure is mapped; Lootr's special elytra table remains untouched. Assignments are based on table identities, not overlapping runtime structure boxes. Detailed changes are in reports/theme-pass.json.

Update checks validate identifiers, counts, weights and bonus references. The live item registry remains the final validation when the mod starts. Test new loot generations and inspect CONFIG / REWARDS logs. A clean build is not in-game validation. The original End iron rolls have not been removed.
