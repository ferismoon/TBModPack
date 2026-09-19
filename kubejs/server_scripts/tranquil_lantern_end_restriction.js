// Prevent player placement of every Tranquil Lantern tier in the End.
// This does not disable existing lanterns or placement by commands/automation.
BlockEvents.rightClicked(event => {
  if (String(event.level.dimension) !== 'minecraft:the_end') return;

  const lanterns = [
    'cozystudioscore:tranquil_lantern',
    'cozystudioscore:golden_tranquil_lantern',
    'cozystudioscore:diamond_tranquil_lantern',
    'cozystudioscore:netherite_tranquil_lantern'
  ];
  if (lanterns.indexOf(String(event.item.id)) === -1) return;

  event.player.tell('Tranquil Lanterns cannot be placed in the End.');
  event.cancel();
});
