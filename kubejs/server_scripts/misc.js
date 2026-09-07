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

// Perfect Plushies' own global-loot serializers are broken on this Fabric
// profile. Add the same sort of rewards directly to the vanilla chest tables.
// This keeps the plushies obtainable without using the broken serializer.
ServerEvents.chestLootTables(event => {
  const plushies = [
    'phomesteadplushies:homestead_player_1',
    'phomesteadplushies:homestead_player_2',
    'phomesteadplushies:homestead_player_3',
    'phomesteadplushies:homestead_player_4',
    'phomesteadplushies:homestead_player_5',
    'phomesteadplushies:homestead_player_6',
    'phomesteadplushies:homestead_player_7',
    'phomesteadplushies:homestead_player_8',
    'phomesteadplushies:homestead_player_9',
    'phomesteadplushies:homestead_player_10',
    'phomesteadplushies:homestead_player_11',
    'phomesteadplushies:homestead_player_12',
    'phomesteadplushies:homestead_player_13',
    'phomesteadplushies:homestead_player_14',
    'phomesteadplushies:homestead_player_15',
    'phomesteadplushies:homestead_player_16',
    'phomesteadplushies:homestead_player_17',
    'phomesteadplushies:homestead_player_18',
    'phomesteadplushies:homestead_player_19',
    'phomesteadplushies:homestead_player_20',
    'phomesteadplushies:homestead_player_21',
    'phomesteadplushies:homestead_player_22',
    'phomesteadplushies:homestead_player_23',
    'phomesteadplushies:homestead_player_24',
    'phomesteadplushies:homestead_player_25',
    'phomesteadplushies:homestead_player_26',
    'phomesteadplushies:homestead_player_27',
    'phomesteadplushies:mushling_plushie',
    'phomesteadplushies:mystical_elk_plushie',
    'phomesteadplushies:fernling_plushie'
  ]

  const addPlushies = (id, chance) => {
    event.modify(id, loot => {
      loot.addPool(pool => {
        plushies.forEach(item => pool.addItem(item))
        pool.rolls = 1
        pool.addCondition({ condition: 'minecraft:random_chance', chance: chance })
      })
    })
  }

  addPlushies('minecraft:chests/buried_treasure', 0.5)
  addPlushies('minecraft:chests/desert_pyramid', 0.1)
  addPlushies('minecraft:chests/trail_ruins_common', 0.1)
  addPlushies('minecraft:chests/trail_ruins_rare', 0.1)

  ;[
    'minecraft:chests/village/village_armorer',
    'minecraft:chests/village/village_butcher',
    'minecraft:chests/village/village_cartographer',
    'minecraft:chests/village/village_desert_house',
    'minecraft:chests/village/village_fisher',
    'minecraft:chests/village/village_mason',
    'minecraft:chests/village/village_plains_house',
    'minecraft:chests/village/village_savanna_house',
    'minecraft:chests/village/village_shepherd',
    'minecraft:chests/village/village_snowy_house',
    'minecraft:chests/village/village_taiga_house',
    'minecraft:chests/village/village_temple',
    'minecraft:chests/village/village_toolsmith',
    'minecraft:chests/village/village_weaponsmith'
  ].forEach(id => addPlushies(id, 0.1))

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

  const addVillagePool = (ids, items, rolls = { min: 1, max: 2 }) => {
    ids.forEach(id => event.modify(id, loot => {
      loot.addPool(pool => {
        items.forEach(item => pool.addItem(item))
        pool.rolls = rolls
      })
    }))
  }

  // Profession-themed village supplies. These are small extra pools, so the
  // original vanilla, CTOV, and Loot Integrations entries remain intact.
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
    'minecraft:map',
    'perfectplushies:cat_plushie',
    'perfectplushies:frog_plushie'
  ], { min: 1, max: 1 })
})
