// Retire duplicate Toolshed hammers while preserving existing items.
ServerEvents.recipes(event => {
  [
    'tokimistoolshed:wooden_hammer',
    'tokimistoolshed:stone_hammer',
    'tokimistoolshed:copper_hammer',
    'tokimistoolshed:iron_hammer',
    'tokimistoolshed:golden_hammer',
    'tokimistoolshed:diamond_hammer',
    'tokimistoolshed:netherite_hammer',
    'tokimistoolshed:obsidian_hammer',
    'tokimistoolshed:rose_gold_hammer'
  ].forEach(id => event.remove({ output: id }))
})
