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
