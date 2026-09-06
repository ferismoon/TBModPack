// Recycle iron equipment into one ingot in either furnace type.
ServerEvents.recipes(event => {
  const recyclableItems = [
    'iron_pickaxe', 'iron_shovel', 'iron_axe', 'iron_hoe', 'iron_sword',
    'iron_helmet', 'iron_chestplate', 'iron_leggings', 'iron_boots',
    'iron_horse_armor', 'chainmail_helmet', 'chainmail_chestplate',
    'chainmail_leggings', 'chainmail_boots', 'iron_door', 'iron_trapdoor', 'bucket'
  ].map(name => ({ item: 'minecraft:' + name }))
  for (const method of ['smelting', 'blasting']) {
    var recipeId = 'minecraft:iron_nugget_from_' + method
    event.remove({ id: recipeId })
    event.custom({
      type: 'minecraft:' + method,
      category: 'misc',
      ingredient: recyclableItems,
      result: 'minecraft:iron_ingot',
      experience: 0.1,
      cookingtime: 200
    }).id(recipeId)
  }
})
