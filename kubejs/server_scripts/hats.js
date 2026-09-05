ServerEvents.recipes(
    event => {
        event.shaped(Item.of('simplehats:hatbag_epic', 1),
            [
                'AA',
                'AA'
            ],
            {
                A: 'simplehats:hatbag_rare'
            }
        )

        event.shaped(Item.of('simplehats:hatbag_rare', 1),
            [
                'AA',
                'AA'
            ],
            {
                A: 'simplehats:hatbag_uncommon'
            }
        )

        event.shaped(Item.of('simplehats:hatbag_uncommon', 1),
            [
                'AA',
                'AA'
            ],
            {
                A: 'simplehats:hatbag_common'
            }
        )

        event.shaped(Item.of('simplehats:hatbag_easter', 1),
            [
                'AAA',
                'ABA',
                'AAA'
            ],
            {
                A: 'minecraft:egg',
                B: 'simplehats:hatbag_epic'
            }
        )

        event.shaped(Item.of('simplehats:hatbag_summer', 1),
            [
                'AAA',
                'ABA',
                'AAA'
            ],
            {
                A: 'spawn:sunflower',
                B: 'simplehats:hatbag_epic'
            }
        )

        event.shaped(Item.of('simplehats:hatbag_halloween', 1),
            [
                'AAA',
                'ABA',
                'AAA'
            ],
            {
                A: 'minecraft:pumpkin',
                B: 'simplehats:hatbag_epic'
            }
        )

        event.shaped(Item.of('simplehats:hatbag_festive', 1),
            [
                'AAA',
                'ABA',
                'AAA'
            ],
            {
                A: 'minecraft:snowball',
                B: 'simplehats:hatbag_epic'
            }
        )
})