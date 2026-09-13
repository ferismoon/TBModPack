/*
 * Misc. Recipe Changes for various item conversions.
 *
 */

ServerEvents.recipes(event => {
       
    event.remove({id: 'cozystudioscore:string'})

    event.shapeless(Item.of('minecraft:string', 4), 'minecraft:white_wool')

    event.shapeless(
        Item.of('sophisticatedstorage:barrel', 1), 
        [
            'minecraft:barrel',
            'minecraft:redstone_torch'
        ]
    )
})

ServerEvents.blockLootTables(event => {
  event.addSimpleBlock('dustydecorations:cooking_pot')
})

// Player plushies are generated centrally by loot-workshop/build.py.
ServerEvents.chestLootTables(event => {

  // Beachparty replaces several vanilla ocean loot tables. Restore their
  // useful vanilla rewards without removing the Beachparty items.
  event.modify('beachparty:chests/buried_treasure', loot => {
    loot.addPool(pool => {
      pool.addItem('minecraft:heart_of_the_sea')
      pool.addItem('minecraft:diamond')
      pool.addItem('minecraft:gold_ingot')
      pool.addItem('minecraft:iron_ingot')
      pool.addItem('minecraft:prismarine_crystals')
      pool.addItem('minecraft:tnt')
      pool.addItem('minecraft:cooked_cod')
      pool.addItem('minecraft:cooked_salmon')
      pool.rolls = { min: 2, max: 4 }
    })
  })

  ;[
    'beachparty:chests/shipwreck_supply',
    'beachparty:chests/shipwreck_treasure',
    'beachparty:chests/underwater_ruin_big',
    'beachparty:chests/underwater_ruin_small'
  ].forEach(id => {
    event.modify(id, loot => {
      loot.addPool(pool => {
        pool.addItem('minecraft:iron_ingot')
        pool.addItem('minecraft:gold_nugget')
        pool.addItem('minecraft:emerald')
        pool.addItem('minecraft:paper')
        pool.addItem('minecraft:wheat')
        pool.addItem('minecraft:carrot')
        pool.addItem('minecraft:potato')
        pool.addItem('minecraft:coal')
        pool.addItem('minecraft:cooked_cod')
        pool.addItem('minecraft:cooked_salmon')
        pool.rolls = { min: 1, max: 3 }
      })
    })
  })

  const addVillagePool = (ids, items, rolls) => {
    if (!rolls) rolls = { min: 1, max: 2 }
    ids.forEach(id => event.modify(id, loot => {
      loot.addPool(pool => {
        items.forEach(item => pool.addItem(item))
        pool.rolls = rolls
      })
    }))
  }

  // Profession-themed village supplies. These are small extra pools, so the
  // original vanilla and CTOV entries remain intact.
  addVillagePool([
    'minecraft:chests/village/village_plains_house',
    'minecraft:chests/village/village_desert_house',
    'minecraft:chests/village/village_savanna_house',
    'minecraft:chests/village/village_snowy_house',
    'minecraft:chests/village/village_taiga_house'
  ], [
    'farmersdelight:cabbage',
    'farmersdelight:onion',
    'farmersdelight:tomato',
    'farmersdelight:cabbage_seeds',
    'farmersdelight:tomato_seeds',
    'farmersdelight:straw',
    'minecraft:bread'
  ])

  addVillagePool([
    'minecraft:chests/village/village_butcher',
    'minecraft:chests/village/village_fisher'
  ], [
    'farmersdelight:cooked_bacon',
    'farmersdelight:cooked_chicken_cuts',
    'farmersdelight:chicken_soup',
    'farmersdelight:fish_stew',
    'minecraft:cooked_cod',
    'minecraft:cooked_salmon'
  ])

  addVillagePool([
    'minecraft:chests/village/village_armorer',
    'minecraft:chests/village/village_toolsmith',
    'minecraft:chests/village/village_weaponsmith'
  ], [
    'minecraft:copper_ingot',
    'create:andesite_alloy',
    'create:raw_zinc',
    'create:copper_sheet',
    'farmersdelight:iron_knife'
  ])

  addVillagePool([
    'minecraft:chests/village/village_mason',
    'minecraft:chests/village/village_shepherd'
  ], [
    'minecraft:clay',
    'minecraft:terracotta',
    'farmersdelight:canvas_rug',
    'beautify:hanging_pot',
    'minecraft:string',
    'minecraft:wool'
  ])

  addVillagePool([
    'minecraft:chests/village/village_cartographer',
    'minecraft:chests/village/village_temple'
  ], [
    'minecraft:paper',
    'minecraft:compass',
    'minecraft:map'
  ], { min: 1, max: 1 })
})
