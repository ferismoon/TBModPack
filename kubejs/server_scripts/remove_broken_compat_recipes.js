ServerEvents.recipes(event => {
  const brokenRecipes = [
    'create:milling/compat/biomeswevegone/compat/biomeswevegone/winter_cyclamen',
    'create:crushing/compat/biomeswevegone/blue_nether_gold_ore',
    'create:milling/compat/biomeswevegone/orchid',
    'create:milling/compat/biomeswevegone/torch_ginger',
    'create:crushing/compat/biomeswevegone/brimstone_nether_gold_ore',
    'create:pressing/compat/biomeswevegone/lush_grass_path',
    'create:milling/compat/biomeswevegone/purple_rose',
    'create:milling/compat/biomeswevegone/lolipop_flower',
    'create:milling/compat/biomeswevegone/compat/biomeswevegone/white_sage',
    'create:crushing/compat/biomeswevegone/cryptic_redstone_ore',
    'create:crushing/compat/biomeswevegone/brimstone_nether_quartz_ore',
    'create:crushing/compat/biomeswevegone/blue_nether_quartz_ore'
  ]

  brokenRecipes.forEach(id => event.remove({ id }))
})