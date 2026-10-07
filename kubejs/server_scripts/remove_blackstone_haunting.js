ServerEvents.recipes(event => {
    // Prevent Create's cobblestone-tag recipe from competing with deepslate to netherrack.
    event.remove({ id: 'create:haunting/blackstone' })
})
