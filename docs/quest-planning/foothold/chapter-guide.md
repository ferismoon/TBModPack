# A Foothold — first chapter prototype

A native FTB Quests chapter, added beside Local Operations and the old chapters. It appears under the new **New Beginnings** chapter group. Existing chapter files and progress IDs are preserved.

## Design

- Three parallel projects: a usable home, a repeatable food supply, and a useful project put to work.
- Nine project statements can be completed in any order. They are honest self-assessments, not automatic building inspections.
- Optional references and experiments have no prerequisite effect. The chapter does not require reading them or completing every example.
- One final milestone depends on the three projects; nothing else is gated.
- Four bone meal for the optional planting experiment, and one named decorative banner at the final milestone. No random loot, XP padding, tools or progression skips.
- FTB team members share task progress. The chapter explicitly tells players to agree on project confirmations.
- A native background texture groups the work spatially; quest positions in the preview are generated from the same source as the SNBT.

## Review boundary

The PNG is a layout preview, not an in-game screenshot. Standard item sprites are used where available; a few 3D block icons are represented by labels in this preview. Minecraft renders the real item icons. Native rendering, font scaling, reward claiming and live task behaviour still need an in-game check.

## Opening it

Chapter ID: `62FDE84753179607`. Group ID: `72F807709569B28F`.

Restart the client to load the added Open Loader texture, or reload client resources if that loader has already discovered it. Reload quest definitions with `/ftbquests reload` using an account with permission. In multiplayer, quest definitions come from the server; a client-only copy is not sufficient. No reload or server restart was performed by this authoring script.

## Quest contents

### You Live Here Now

A beginning, not an itinerary.

YOUR FIRST BRIEF

You have arrived. The accommodation department has supplied a landscape. Everything else is apparently your problem.

Your first project is simple: make this a place you can actually live. Find a foothold, arrange tomorrow's food, and make something useful.

The three large diamonds are your goals. Work on them together, separately, or in whatever order suits you. None requires the small quests above it.

Small circles are optional help or experiments. Squares are reference pages. Read what you need; there is no payment for reading the manual.

Already settled? Your existing home and shared facilities count. Nobody needs a second furnace for administrative reasons.

This is a co-operative chapter. If you share an FTB quest team, discuss the project confirmations together: a teammate can complete tasks for the team.

The final reward is a keepsake for the place you made. The real reward is having somewhere worth coming back to.

Tasks:
- I know how this chapter works

### Find the Method

REFERENCE / Recipes, uses and alternatives

WHEN AN UNFAMILIAR ITEM GETS IN THE WAY

Use the recipe viewer beside your inventory. Search for an item, inspect how it is made, then inspect what it is used for. The recipe screen identifies the station or processing method involved.

Recipe and usage shortcuts can be rebound. Look in Controls for REI if the usual keys do not work; do not copy a key from a video and assume your bindings match.

Try this when you need it: look up a sleeping bag, cooking pot or tool you actually want. Work backwards from the useful result.

This pack changes recipes. Its in-game recipe viewer is a better starting point than a tutorial written for another version. If several mods offer similar crops or materials, inspect the accepted ingredients before building duplicate farms.

Reference only. Marking this page read is optional and has no reward or prerequisite effect.

Tasks:
- Mark this reference as read

### Small Print, Large Teeth

REFERENCE / Loot, recovery and travelling

A FEW THINGS WORTH KNOWING BEFORE YOU LEAVE

Lootr containers: supported loot containers give players their own loot. Leave the container in place for the next visitor. Ordinary chests are not automatically personal loot.

Graves: the pack has death recovery through Universal Graves. Read the location/recovery information after a death and prepare for the return journey; the grave does not make the surrounding danger disappear.

Maps: Xaero's maps can help you record a route and mark home. Check your Controls for the map and waypoint actions. Writing down coordinates is also perfectly valid.

Camping: Comforts sleeping bags are for portable rest without moving your respawn point. A permanent bed and a travelling bedroll solve different problems.

Reference only. No command use, death or dangerous trip is required to complete this chapter.

Tasks:
- Mark this reference as read

### Borrow the Workshop

REFERENCE / Shared facilities and team progress

YOU DO NOT HAVE TO MAKE EVERYTHING YOURSELF

A Farmer can supply the Cook. A Cook can feed the Builder. A Mechanic can build a machine that everyone uses.

Facilities you have permission to use count towards the projects below. You may contribute to a shared home instead of building a separate base.

Agree on what is shared: supplies, storage labels, access to machines and a place for everyone's things. Use the pack's party/claim tools where appropriate; their permissions and limits depend on the server.

FTB quest teams and land-claim parties are different systems. Joining one does not mean you have configured the other.

Team confirmations: manual project tasks record your FTB team's progress. Confirm what your team has actually achieved, not what you hope someone else is doing.

Reference only. You do not need to form a team, claim land or trade with another player to finish.

Tasks:
- Mark this reference as read

### A Bed Is a Beginning

OPTIONAL / Find a place to rest

BEFORE YOU DESIGN THE GUEST WING

Find or place a normal bed and look directly at it. A bed you have permission to use in a shared base is fine.

A bed is one part of a home. Think about access, nearby danger and where you will reappear after a mistake. You do not need to wait for night for this observation task.

If you prefer a hammock, sleeping bag or another arrangement, skip this example and use the main home project instead.

Detected: looking at a block in the vanilla beds tag. This does not certify that the room is safe or that your spawn is set.

Tasks:
- Look at any normal bed

### Leave Yourself a Way Back

OPTIONAL / A useful location, recorded

FUTURE YOU HAS A TERRIBLE SENSE OF DIRECTION

Record the location of a home, camp or landmark you genuinely want to revisit. Use a map waypoint, written coordinates or a route you can reliably recognise.

Give it a useful name. "Home" is acceptable. "Somewhere near the tree" may require further work.

If you are learning Xaero's maps, find its waypoint controls in the key bindings. No particular key or waypoint name is required.

Self-confirmed: mark this when you have a usable way back. The quest cannot read your private map markers.

Tasks:
- I recorded a location I can return to

### Start Small, Keep Growing

OPTIONAL / Try growing your own food

ONE SMALL PATCH IS ENOUGH TO LEARN

Plant a crop recognised by the vanilla A Seedy Place advancement. Wheat is a simple example: prepare suitable farmland and plant a seed.

Put it somewhere you will visit again. Leave room to reach it, harvest it and replant. A vast field is less useful than a small patch you remember exists.

The bone meal reward helps you try another growth or harvest cycle. It is a small gardening supply, not a replacement farm.

Modded plants do not all grant this advancement. Skip this optional experiment if your chosen crop does not; the food project accepts any reliable supply.

Detected: A Seedy Place. An existing advancement counts. This is planting practice, not proof of an established farm.

Tasks:
- Plant a crop: A Seedy Place

### Make More of an Ingredient

OPTIONAL / A simple cooking experiment

A POTATO WITH AMBITION

Have a baked potato available. Cooking a potato in a furnace is a simple example of turning a crop into ready-to-eat food. A shared or purchased meal also counts.

If you are learning the recipe viewer, inspect the baked potato recipe and follow the preparation method shown there.

Farmer's Delight and Farm & Charm offer much more substantial kitchens. You can explore those instead; this example is not a gate to either mod.

The question for your food project: can you obtain the ingredients again, and prepare food again, after this meal is gone?

Detected: one baked potato in your inventory. It is not consumed, and possession does not claim that you cooked it yourself.

Tasks:
- Have one baked potato available

### Meet a Working Kitchen

OPTIONAL / Inspect a Farmer's Delight cooking pot

A MACHINE SHOULD HAVE A JOB

Find or place a Farmer's Delight cooking pot and look at it. A friend's kitchen is a perfectly good classroom.

Look up a meal you would actually like to make. Inspect its ingredients and heat requirements in the recipe viewer, then consider where the inputs would come from.

This is a demonstration of thinking from the result backwards. You can apply the same approach to a Create machine, a storage network or a brewing station.

There is no obligation to build this particular kitchen. The main project accepts a useful build or system of your own choosing.

Detected: looking at a Farmer's Delight cooking pot. This confirms an introduction to the block, not a functioning or productive kitchen.

Tasks:
- Look at a Farmer's Delight cooking pot

### Pick a Problem Worth Solving

OPTIONAL / Choose a project that interests you

START WITH WHAT YOU WANT TO DO

Builder: furnish a room you actually use, or make an outdoor space with a purpose.

Mechanic: make one powered machine perform a useful operation; a decorative cog display can wait.

Cook or Brewer: prepare something through a kitchen or brewing setup you can use again.

Quartermaster: organize storage so you can find and put away the things you need.

Rancher or Farmer: make a cared-for pen or working growing area. Collector? Make a display that can welcome the next find.

Explorer or Adventurer: establish and use a properly supplied expedition camp. Witch or Blacksmith? Prepare a practical workspace and use it.

Merchant and Angler projects count too. The test is simple: what can you do now that you could not do conveniently before?

Optional planning note. Choosing an idea here does not lock you into a path or complete the project.

Tasks:
- I have an idea I want to try

### Somewhere to Come Back To

PROJECT / Make a foothold that works for you

A HOME IS A USEFUL PLACE, NOT A BLOCK COUNT

Choose somewhere you are happy to return to. A cabin, borrowed room, cave workshop or travelling base can all count.

Finish these three parts in any order:

Rest: you have a place to rest and have considered nearby danger. Light and shelter should serve the space; nobody is counting torches.

Belongings: you have somewhere to put things and can find what you need again. A modest labelled chest is enough if it does the job.

Return: you know how to get back. A waypoint, coordinates, familiar route or established travel point are all valid.

Use it: leave to do something nearby, return, and put your supplies away. Does the place work, or is something still awkward?

Project assessment: confirm each statement when it is true. These are your team's judgements; the game cannot evaluate the quality of a home. The optional examples above are not requirements.

Tasks:
- We have a usable place to rest
- Our belongings have a place we can use
- We can leave and find our way back

### Dinner Has a Tomorrow

PROJECT / Arrange a supply you can keep using

ONE LUCKY CHEST IS LUNCH. WHAT ABOUT TOMORROW?

Arrange a food supply you can return to. Growing crops is one option. Fishing, animal husbandry, a renewable forage patch or a repeatable trade arrangement can work too.

Finish these three parts in any order:

Source: identify where your next ingredients or meals will come from after today's supply is used.

Use: obtain food through that arrangement and actually eat a meal. You may prepare it yourself or share the work.

Continue: leave the supply ready to continue: replant, keep breeding stock, retain your fishing equipment, or agree the next delivery.

You do not need every food mod, a particular diet or a stack of every crop. Choose something that suits how you want to live.

Project assessment: confirm the three outcomes yourself. The planting and potato examples are optional introductions, not compulsory ingredients in your food plan.

Tasks:
- We know where another meal will come from
- We have eaten from our chosen supply
- The supply can continue after this meal

### Make Yourself Useful

PROJECT / Build something and put it to work

GIVE SOMETHING A JOB

Choose a small project that makes life here better. Use the idea page if you need inspiration, or bring your own.

Finish these three parts in any order:

Purpose: decide what the project is meant to do. "It makes flour", "it stores the harvest" or "it gives us somewhere comfortable to eat" are good answers.

Working result: build or arrange it, then use it for that purpose. A machine should process something. A kitchen should serve a meal. A room should be furnished for its intended use.

Ready again: leave it in a state where you or a friend can use it again. Think about supplies, access and where the result goes.

No minimum size, prescribed mod or equipment tier. Improving a shared build counts. A food project can also satisfy this project if you genuinely meet both sets of outcomes; duplication is not a virtue.

Project assessment: confirm what your team has achieved. The cooking-pot example is not a prerequisite. We deliberately do not treat owning a workstation as proof that you have used it.

Tasks:
- Our project has a clear purpose
- We have put it to use
- It is ready for another use

### You Are Not Just Visiting

MILESTONE / Hang out your sign

THE ACCOMMODATION DEPARTMENT IS IMPRESSED

You have somewhere to return to, a food supply with a future, and something useful that you helped make.

That is a foothold. It does not need a castle, a factory or a diamond shovel.

Claim this small banner as a keepsake. Hang it at your home, workshop or shared meeting place if you wish. It has no special powers and does not unlock the next chapter.

Leave the optional examples unfinished if you do not need them. Your next direction is yours to choose.

This milestone brings together the three independent projects. It is the only prerequisite junction in the chapter. The final confirmation is a chance to recognise the result together.

Tasks:
- We have made a foothold here

### What Will You Make of This Place?

REFERENCE / Fourteen paths. No class selection.

FOLLOW YOUR INTEREST, NOT AN ASSIGNED CLASS

The Mechanic — power, processing and useful machines.
The Farmer — growing, gardens, orchards and forestry.
The Cook — ingredients, kitchens and food worth sharing.
The Brewer — beer, wine, tea, coffee and a good cellar.
The Witch — herbs, rituals, brews and practical magic.
The Builder — places with character and purpose.
The Collector — plushies, hats, curiosities and displays.
The Explorer — landscapes, discoveries and routes.
The Rancher — animals, companions and their care.
The Angler — fishing, unusual catches and quiet waters.
The Blacksmith — mining, tools, equipment and upkeep.
The Adventurer — dangerous places and worthy opponents.
The Merchant — trades, shops and a living settlement.
The Quartermaster — storage and getting things where they belong.

Mix them freely. Build a tavern and brew its drinks. Explore for a friend's garden. Automate your kitchen. Be the person who makes everyone's supplies easy to find.

This page previews the agreed path structure. Their new chapters are not implemented yet; the existing chapters elsewhere in the book remain separate. Nothing here selects a class or locks an ability.

Tasks:
- Mark this reference as read
