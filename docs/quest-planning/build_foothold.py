"""Author the A Foothold prototype and a preview from the same coordinates."""
import hashlib,json,re,zipfile,io,math,textwrap
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont

ROOT=Path('I:/McWork'); OUT=ROOT/'docs/quest-planning/foothold';OUT.mkdir(exist_ok=True)
CHAPTER=ROOT/'config/ftbquests/quests/chapters/00_a_foothold.snbt'
TEXTURE=ROOT/'config/openloader/resources/ftbquests/assets/ftbquests/textures/chapters/a_foothold.png'
TEXTURE.parent.mkdir(parents=True,exist_ok=True)
def ident(name):return f'{int(hashlib.sha256(("forced_relocation/foothold/v1/"+name).encode()).hexdigest()[:16],16)&0x7fffffffffffffff:016X}'
GROUP=ident('group'); CHID=ident('chapter'); quests=[]
def check(key,title):return {'id':ident('task/'+key),'type':'checkmark','title':title}
def observation(key,title,target):return {'id':ident('task/'+key),'type':'observation','title':title,'observe_type':0,'to_observe':target,'timer':0}
def advancement(key,title,target):return {'id':ident('task/'+key),'type':'advancement','title':title,'advancement':target,'criterion':''}
def quest(key,title,sub,icon,x,y,description,tasks,optional=True,size=1.0,shape='circle',deps=None,rewards=None):
 q={'id':ident('quest/'+key),'title':title,'subtitle':sub,'icon':icon,'x':float(x),'y':float(y),'size':float(size),'shape':shape,'optional':optional,'description':description,'tasks':tasks}
 if deps:q['dependencies']=[ident('quest/'+d) for d in deps]
 if rewards:q['rewards']=rewards
 quests.append(q);return q

quest('welcome','You Live Here Now','A beginning, not an itinerary.','minecraft:compass',0,-6.1,[
 '&lYOUR FIRST BRIEF&r','',
 'You have arrived. The accommodation department has supplied a landscape. Everything else is apparently your problem.','',
 'Your first project is simple: make this a place you can actually live. Find a foothold, arrange tomorrow\'s food, and make something useful.','',
 '&6The three large diamonds are your goals.&r Work on them together, separately, or in whatever order suits you. None requires the small quests above it.','',
 '&7Small circles are optional help or experiments. Squares are reference pages. Read what you need; there is no payment for reading the manual.&r','',
 'Already settled? Your existing home and shared facilities count. Nobody needs a second furnace for administrative reasons.','',
 '&lThis is a co-operative chapter.&r If you share an FTB quest team, discuss the project confirmations together: a teammate can complete tasks for the team.','',
 'The final reward is a keepsake for the place you made. The real reward is having somewhere worth coming back to.'
],[check('welcome','I know how this chapter works')],size=1.3)

quest('recipes','Find the Method','REFERENCE / Recipes, uses and alternatives','minecraft:book',-5,-4.35,[
 '&lWHEN AN UNFAMILIAR ITEM GETS IN THE WAY&r','',
 'Use the recipe viewer beside your inventory. Search for an item, inspect how it is made, then inspect what it is used for. The recipe screen identifies the station or processing method involved.','',
 'Recipe and usage shortcuts can be rebound. Look in Controls for REI if the usual keys do not work; do not copy a key from a video and assume your bindings match.','',
 '&6Try this when you need it:&r look up a sleeping bag, cooking pot or tool you actually want. Work backwards from the useful result.','',
 'This pack changes recipes. Its in-game recipe viewer is a better starting point than a tutorial written for another version. If several mods offer similar crops or materials, inspect the accepted ingredients before building duplicate farms.','',
 '&7Reference only. Marking this page read is optional and has no reward or prerequisite effect.&r'
],[check('recipes','Mark this reference as read')],shape='square',size=.85)
quest('rules','Small Print, Large Teeth','REFERENCE / Loot, recovery and travelling','minecraft:map',0,-4.35,[
 '&lA FEW THINGS WORTH KNOWING BEFORE YOU LEAVE&r','',
 '&6Lootr containers:&r supported loot containers give players their own loot. Leave the container in place for the next visitor. Ordinary chests are not automatically personal loot.','',
 '&6Graves:&r the pack has death recovery through Universal Graves. Read the location/recovery information after a death and prepare for the return journey; the grave does not make the surrounding danger disappear.','',
 '&6Maps:&r Xaero\'s maps can help you record a route and mark home. Check your Controls for the map and waypoint actions. Writing down coordinates is also perfectly valid.','',
 '&6Camping:&r Comforts sleeping bags are for portable rest without moving your respawn point. A permanent bed and a travelling bedroll solve different problems.','',
 '&7Reference only. No command use, death or dangerous trip is required to complete this chapter.&r'
],[check('rules','Mark this reference as read')],shape='square',size=.85)
quest('together','Borrow the Workshop','REFERENCE / Shared facilities and team progress','minecraft:oak_door',5,-4.35,[
 '&lYOU DO NOT HAVE TO MAKE EVERYTHING YOURSELF&r','',
 'A Farmer can supply the Cook. A Cook can feed the Builder. A Mechanic can build a machine that everyone uses.','',
 'Facilities you have permission to use count towards the projects below. You may contribute to a shared home instead of building a separate base.','',
 '&6Agree on what is shared:&r supplies, storage labels, access to machines and a place for everyone\'s things. Use the pack\'s party/claim tools where appropriate; their permissions and limits depend on the server.','',
 'FTB quest teams and land-claim parties are different systems. Joining one does not mean you have configured the other.','',
 '&6Team confirmations:&r manual project tasks record your FTB team\'s progress. Confirm what your team has actually achieved, not what you hope someone else is doing.','',
 '&7Reference only. You do not need to form a team, claim land or trade with another player to finish.&r'
],[check('together','Mark this reference as read')],shape='square',size=.85)

quest('bed','A Bed Is a Beginning','OPTIONAL / Find a place to rest','minecraft:red_bed',-6,-1.1,[
 '&lBEFORE YOU DESIGN THE GUEST WING&r','',
 'Find or place a normal bed and look directly at it. A bed you have permission to use in a shared base is fine.','',
 'A bed is one part of a home. Think about access, nearby danger and where you will reappear after a mistake. You do not need to wait for night for this observation task.','',
 'If you prefer a hammock, sleeping bag or another arrangement, skip this example and use the main home project instead.','',
 '&7Detected: looking at a block in the vanilla beds tag. This does not certify that the room is safe or that your spawn is set.&r'
],[observation('bed','Look at any normal bed','#minecraft:beds')],size=.85)
quest('bearings','Leave Yourself a Way Back','OPTIONAL / A useful location, recorded','minecraft:filled_map',-4,-1.1,[
 '&lFUTURE YOU HAS A TERRIBLE SENSE OF DIRECTION&r','',
 'Record the location of a home, camp or landmark you genuinely want to revisit. Use a map waypoint, written coordinates or a route you can reliably recognise.','',
 'Give it a useful name. "Home" is acceptable. "Somewhere near the tree" may require further work.','',
 'If you are learning Xaero\'s maps, find its waypoint controls in the key bindings. No particular key or waypoint name is required.','',
 '&7Self-confirmed: mark this when you have a usable way back. The quest cannot read your private map markers.&r'
],[check('bearings','I recorded a location I can return to')],size=.85)

quest('seed','Start Small, Keep Growing','OPTIONAL / Try growing your own food','minecraft:wheat_seeds',-1,-1.1,[
 '&lONE SMALL PATCH IS ENOUGH TO LEARN&r','',
 'Plant a crop recognised by the vanilla A Seedy Place advancement. Wheat is a simple example: prepare suitable farmland and plant a seed.','',
 'Put it somewhere you will visit again. Leave room to reach it, harvest it and replant. A vast field is less useful than a small patch you remember exists.','',
 'The bone meal reward helps you try another growth or harvest cycle. It is a small gardening supply, not a replacement farm.','',
 'Modded plants do not all grant this advancement. Skip this optional experiment if your chosen crop does not; the food project accepts any reliable supply.','',
 '&7Detected: A Seedy Place. An existing advancement counts. This is planting practice, not proof of an established farm.&r'
],[advancement('seed','Plant a crop: A Seedy Place','minecraft:husbandry/plant_seed')],size=.85,rewards=[{'id':ident('reward/seed'),'type':'item','item':'minecraft:bone_meal','count':4}])
quest('meal','Make More of an Ingredient','OPTIONAL / A simple cooking experiment','minecraft:baked_potato',1,-1.1,[
 '&lA POTATO WITH AMBITION&r','',
 'Have a baked potato available. Cooking a potato in a furnace is a simple example of turning a crop into ready-to-eat food. A shared or purchased meal also counts.','',
 'If you are learning the recipe viewer, inspect the baked potato recipe and follow the preparation method shown there.','',
 'Farmer\'s Delight and Farm & Charm offer much more substantial kitchens. You can explore those instead; this example is not a gate to either mod.','',
 '&6The question for your food project:&r can you obtain the ingredients again, and prepare food again, after this meal is gone?','',
 '&7Detected: one baked potato in your inventory. It is not consumed, and possession does not claim that you cooked it yourself.&r'
],[{'id':ident('task/meal'),'title':'Have one baked potato available','type':'item','item':'minecraft:baked_potato','count':1,'consume_items':False,'match_nbt':False,'only_from_crafting':False}],size=.85)

quest('workbench','Meet a Working Kitchen','OPTIONAL / Inspect a Farmer\'s Delight cooking pot','farmersdelight:cooking_pot',4,-1.1,[
 '&lA MACHINE SHOULD HAVE A JOB&r','',
 'Find or place a Farmer\'s Delight cooking pot and look at it. A friend\'s kitchen is a perfectly good classroom.','',
 'Look up a meal you would actually like to make. Inspect its ingredients and heat requirements in the recipe viewer, then consider where the inputs would come from.','',
 'This is a demonstration of thinking from the result backwards. You can apply the same approach to a Create machine, a storage network or a brewing station.','',
 'There is no obligation to build this particular kitchen. The main project accepts a useful build or system of your own choosing.','',
 '&7Detected: looking at a Farmer\'s Delight cooking pot. This confirms an introduction to the block, not a functioning or productive kitchen.&r'
],[observation('workbench','Look at a Farmer\'s Delight cooking pot','farmersdelight:cooking_pot')],size=.85)
quest('ideas','Pick a Problem Worth Solving','OPTIONAL / Choose a project that interests you','minecraft:writable_book',6,-1.1,[
 '&lSTART WITH WHAT YOU WANT TO DO&r','',
 '&6Builder:&r furnish a room you actually use, or make an outdoor space with a purpose.','',
 '&6Mechanic:&r make one powered machine perform a useful operation; a decorative cog display can wait.','',
 '&6Cook or Brewer:&r prepare something through a kitchen or brewing setup you can use again.','',
 '&6Quartermaster:&r organize storage so you can find and put away the things you need.','',
 '&6Rancher or Farmer:&r make a cared-for pen or working growing area. Collector? Make a display that can welcome the next find.','',
 '&6Explorer or Adventurer:&r establish and use a properly supplied expedition camp. Witch or Blacksmith? Prepare a practical workspace and use it.','',
 'Merchant and Angler projects count too. The test is simple: what can you do now that you could not do conveniently before?','',
 '&7Optional planning note. Choosing an idea here does not lock you into a path or complete the project.&r'
],[check('ideas','I have an idea I want to try')],size=.85)

quest('home','Somewhere to Come Back To','PROJECT / Make a foothold that works for you','minecraft:lantern',-5,1.45,[
 '&lA HOME IS A USEFUL PLACE, NOT A BLOCK COUNT&r','',
 'Choose somewhere you are happy to return to. A cabin, borrowed room, cave workshop or travelling base can all count.','',
 '&6Finish these three parts in any order:&r','',
 '&lRest:&r you have a place to rest and have considered nearby danger. Light and shelter should serve the space; nobody is counting torches.','',
 '&lBelongings:&r you have somewhere to put things and can find what you need again. A modest labelled chest is enough if it does the job.','',
 '&lReturn:&r you know how to get back. A waypoint, coordinates, familiar route or established travel point are all valid.','',
 'Use it: leave to do something nearby, return, and put your supplies away. Does the place work, or is something still awkward?','',
 '&7Project assessment: confirm each statement when it is true. These are your team\'s judgements; the game cannot evaluate the quality of a home. The optional examples above are not requirements.&r'
],[check('home/rest','We have a usable place to rest'),check('home/storage','Our belongings have a place we can use'),check('home/return','We can leave and find our way back')],optional=False,size=1.6,shape='diamond')
quest('food','Dinner Has a Tomorrow','PROJECT / Arrange a supply you can keep using','minecraft:bread',0,1.45,[
 '&lONE LUCKY CHEST IS LUNCH. WHAT ABOUT TOMORROW?&r','',
 'Arrange a food supply you can return to. Growing crops is one option. Fishing, animal husbandry, a renewable forage patch or a repeatable trade arrangement can work too.','',
 '&6Finish these three parts in any order:&r','',
 '&lSource:&r identify where your next ingredients or meals will come from after today\'s supply is used.','',
 '&lUse:&r obtain food through that arrangement and actually eat a meal. You may prepare it yourself or share the work.','',
 '&lContinue:&r leave the supply ready to continue: replant, keep breeding stock, retain your fishing equipment, or agree the next delivery.','',
 'You do not need every food mod, a particular diet or a stack of every crop. Choose something that suits how you want to live.','',
 '&7Project assessment: confirm the three outcomes yourself. The planting and potato examples are optional introductions, not compulsory ingredients in your food plan.&r'
],[check('food/source','We know where another meal will come from'),check('food/use','We have eaten from our chosen supply'),check('food/continue','The supply can continue after this meal')],optional=False,size=1.6,shape='diamond')
quest('purpose','Make Yourself Useful','PROJECT / Build something and put it to work','minecraft:crafting_table',5,1.45,[
 '&lGIVE SOMETHING A JOB&r','',
 'Choose a small project that makes life here better. Use the idea page if you need inspiration, or bring your own.','',
 '&6Finish these three parts in any order:&r','',
 '&lPurpose:&r decide what the project is meant to do. "It makes flour", "it stores the harvest" or "it gives us somewhere comfortable to eat" are good answers.','',
 '&lWorking result:&r build or arrange it, then use it for that purpose. A machine should process something. A kitchen should serve a meal. A room should be furnished for its intended use.','',
 '&lReady again:&r leave it in a state where you or a friend can use it again. Think about supplies, access and where the result goes.','',
 'No minimum size, prescribed mod or equipment tier. Improving a shared build counts. A food project can also satisfy this project if you genuinely meet both sets of outcomes; duplication is not a virtue.','',
 '&7Project assessment: confirm what your team has achieved. The cooking-pot example is not a prerequisite. We deliberately do not treat owning a workstation as proof that you have used it.&r'
],[check('purpose/job','Our project has a clear purpose'),check('purpose/use','We have put it to use'),check('purpose/repeat','It is ready for another use')],optional=False,size=1.6,shape='diamond')

name=json.dumps({'text':'A Place Worth Returning To','italic':False,'color':'gold'},separators=(',',':'))
lore=[json.dumps({'text':x,'italic':False,'color':'gray'},separators=(',',':')) for x in ['Forced Relocation — A Foothold','Rest. Supper. Something of your own.']]
quest('finish','You Are Not Just Visiting','MILESTONE / Hang out your sign','minecraft:green_banner',0,4.45,[
 '&lTHE ACCOMMODATION DEPARTMENT IS IMPRESSED&r','',
 'You have somewhere to return to, a food supply with a future, and something useful that you helped make.','',
 'That is a foothold. It does not need a castle, a factory or a diamond shovel.','',
 'Claim this small banner as a keepsake. Hang it at your home, workshop or shared meeting place if you wish. It has no special powers and does not unlock the next chapter.','',
 'Leave the optional examples unfinished if you do not need them. Your next direction is yours to choose.','',
 '&7This milestone brings together the three independent projects. It is the only prerequisite junction in the chapter. The final confirmation is a chance to recognise the result together.&r'
],[check('finish','We have made a foothold here')],optional=False,size=1.6,shape='diamond',deps=['home','food','purpose'],rewards=[{'id':ident('reward/banner'),'type':'item','title':'A Place Worth Returning To','item':{'id':'minecraft:green_banner','Count':1,'tag':{'display':{'Name':name,'Lore':lore},'BlockEntityTag':{'Patterns':[{'Pattern':'bs','Color':12},{'Pattern':'flo','Color':4},{'Pattern':'bo','Color':12}]}}}}])
quest('paths','What Will You Make of This Place?','REFERENCE / Fourteen paths. No class selection.','minecraft:written_book',0,7.15,[
 '&lFOLLOW YOUR INTEREST, NOT AN ASSIGNED CLASS&r','',
 '&6The Mechanic&r — power, processing and useful machines.',
 '&6The Farmer&r — growing, gardens, orchards and forestry.',
 '&6The Cook&r — ingredients, kitchens and food worth sharing.',
 '&6The Brewer&r — beer, wine, tea, coffee and a good cellar.',
 '&6The Witch&r — herbs, rituals, brews and practical magic.',
 '&6The Builder&r — places with character and purpose.',
 '&6The Collector&r — plushies, hats, curiosities and displays.',
 '&6The Explorer&r — landscapes, discoveries and routes.',
 '&6The Rancher&r — animals, companions and their care.',
 '&6The Angler&r — fishing, unusual catches and quiet waters.',
 '&6The Blacksmith&r — mining, tools, equipment and upkeep.',
 '&6The Adventurer&r — dangerous places and worthy opponents.',
 '&6The Merchant&r — trades, shops and a living settlement.',
 '&6The Quartermaster&r — storage and getting things where they belong.','',
 'Mix them freely. Build a tavern and brew its drinks. Explore for a friend\'s garden. Automate your kitchen. Be the person who makes everyone\'s supplies easy to find.','',
 '&7This page previews the agreed path structure. Their new chapters are not implemented yet; the existing chapters elsewhere in the book remain separate. Nothing here selects a class or locks an ability.&r'
],[check('paths','Mark this reference as read')],shape='square')

# A single native chapter image provides headers and spacing without fake prerequisite arrows.
S=80; W=1440;H=1440;origin=(W//2,720)
def xy(x,y):return (round(origin[0]+x*S),round(origin[1]+y*S))
fontbase=Path('C:/Windows/Fonts')
def font(n,bold=False):return ImageFont.truetype(str(fontbase/('segoeuib.ttf' if bold else 'segoeui.ttf')),n)
im=Image.new('RGBA',(W,H),(0,0,0,0));d=ImageDraw.Draw(im)
ink='#eadfc6';muted='#acbcb7';green='#a4c9a7';gold='#d6b56b';blue='#9dc5d1'
def center(text,x,y,size=25,fill=ink,bold=False):d.text(xy(x,y),text,font=font(size,bold),fill=fill,anchor='mm')
center('F O R C E D   R E L O C A T I O N',0,-8.5,19,muted)
center('A FOOTHOLD',0,-7.88,49,ink,True)
center('Three useful beginnings. One place to call yours.',0,-7.32,23,muted)
center('YOUR BRIEF',0,-5.12,18,muted,True)
for x,label in [(-5,'FIND THE METHOD'),(0,'THE SMALL PRINT'),(5,'WORK TOGETHER')]:center(label,x,-3.6,17,muted,True)
for x,title,kicker,color,goal in [(-5,'SOMEWHERE TO RETURN','REST  /  BELONGINGS  /  A WAY BACK',green,'MAKE A HOME'),(0,'SOMETHING FOR TOMORROW','SOURCE  /  A MEAL  /  ANOTHER DAY',gold,'ARRANGE A FOOD SUPPLY'),(5,'SOMETHING OF YOUR OWN','A PURPOSE  /  A RESULT  /  REPEAT',blue,'PUT A PROJECT TO WORK')]:
 a=xy(x-2.3,-3.05);b=xy(x+2.3,2.95)
 d.rounded_rectangle([a,b],radius=20,fill=(25,35,38,235),outline=color,width=2)
 center(title,x,-2.57,20,color,True);center('Optional experiments',x,-2.07,16,muted)
 center(goal,x,.22,18,color,True)
for x,y,label in [(-6,-.32,'Rest'),(-4,-.32,'Return'),(-1,-.32,'Grow'),(1,-.32,'Prepare'),(4,-.32,'Discover'),(6,-.32,'Choose')]:center(label,x,y,16,muted)
center('A PLACE WORTH RETURNING TO',0,5.64,22,ink,True)
center('The three projects meet here. The small quests are never required.',0,6.1,17,muted)
center('YOUR NEXT DIRECTION IS YOURS',0,7.97,20,ink,True)
center('Squares: references     Circles: optional experiments     Diamonds: projects',0,8.55,16,muted)
im.save(TEXTURE)

chapter={'filename':'00_a_foothold','id':CHID,'group':GROUP,'title':'A Foothold','icon':'minecraft:lantern','order_index':0,'default_quest_shape':'circle','default_hide_dependency_lines':False,'images':[{'image':'ftbquests:textures/chapters/a_foothold.png','x':0.0,'y':0.0,'width':18.0,'height':18.0,'rotation':0.0,'order':-100}],'quest_links':[],'quests':quests}
def snbt(obj,level=0):
 indent='\t'*level
 if isinstance(obj,dict):return '{\n'+',\n'.join('\t'*(level+1)+json.dumps(k)+': '+snbt(v,level+1) for k,v in obj.items())+'\n'+indent+'}'
 if isinstance(obj,list):return '[\n'+',\n'.join('\t'*(level+1)+snbt(v,level+1) for v in obj)+'\n'+indent+']' if obj else '[]'
 if isinstance(obj,bool):return 'true' if obj else 'false'
 if isinstance(obj,float):return str(obj)+'d'
 if isinstance(obj,int):return str(obj)
 return json.dumps(obj,ensure_ascii=False)
CHAPTER.write_text(snbt(chapter)+'\n','utf-8')
(OUT/'chapter-source.json').write_text(json.dumps(chapter,indent=2,ensure_ascii=False),'utf-8')

# Preview uses the exact native background, quest positions/sizes, and dependency edges.
preview=Image.new('RGBA',im.size,'#141d22');preview.alpha_composite(im);pd=ImageDraw.Draw(preview)
byid={q['id']:q for q in quests}
for q in quests:
 for dep in q.get('dependencies',[]):
  a=byid[dep];pd.line([xy(a['x'],a['y']+.85),xy(q['x'],q['y']-.85)],fill='#65756c',width=3)
client=zipfile.ZipFile('I:/PrismLauncher/libraries/com/mojang/minecraft/1.20.1/minecraft-1.20.1-client.jar')
jarrows=json.loads((ROOT/'docs/quest-planning/inventory-evidence.json').read_text('utf-8'))
potjar=next(r['present'][0] for r in jarrows if r['key']=='farmers-delight-refabricated')
modjar=zipfile.ZipFile(potjar)
for q in quests:
 x,y=xy(q['x'],q['y']);r=q['size']*S*.45
 col=green if q['x']<-2 else blue if q['x']>2 else gold
 if q['shape']=='diamond':pd.polygon([(x,y-r),(x+r,y),(x,y+r),(x-r,y)],fill='#223233',outline=col,width=4)
 elif q['shape']=='square':pd.rounded_rectangle([x-r,y-r,x+r,y+r],radius=6,fill='#243031',outline=muted,width=3)
 else:pd.ellipse([x-r,y-r,x+r,y+r],fill='#243031',outline=col,width=3)
 ns,item=q['icon'].split(':');source=client if ns=='minecraft' else modjar
 texture=f'assets/{ns}/textures/item/{item}.png'
 if item=='compass':texture='assets/minecraft/textures/item/compass_16.png'
 if texture not in source.namelist():texture=f'assets/{ns}/textures/block/{item}_side.png'
 if texture in source.namelist():
  icon=Image.open(io.BytesIO(source.read(texture))).convert('RGBA');size=round(r*1.18);icon.thumbnail((size,size),Image.Resampling.NEAREST);icon=icon.resize((size,size),Image.Resampling.NEAREST);preview.alpha_composite(icon,(x-size//2,y-size//2))
 else:
  pd.text((x,y),{'minecraft:red_bed':'REST','minecraft:green_banner':'HOME','minecraft:oak_door':'TEAM'}.get(q['icon'],'USE'),font=font(17,True),fill=ink,anchor='mm')
preview.convert('RGB').save(OUT/'layout-preview.png')

readme=['# A Foothold — first chapter prototype','',
 'A native FTB Quests chapter, added beside Local Operations and the old chapters. It appears under the new **New Beginnings** chapter group. Existing chapter files and progress IDs are preserved.','',
 '## Design','',
 '- Three parallel projects: a usable home, a repeatable food supply, and a useful project put to work.',
 '- Nine project statements can be completed in any order. They are honest self-assessments, not automatic building inspections.',
 '- Optional references and experiments have no prerequisite effect. The chapter does not require reading them or completing every example.',
 '- One final milestone depends on the three projects; nothing else is gated.',
 '- Four bone meal for the optional planting experiment, and one named decorative banner at the final milestone. No random loot, XP padding, tools or progression skips.',
 '- FTB team members share task progress. The chapter explicitly tells players to agree on project confirmations.',
 '- A native background texture groups the work spatially; quest positions in the preview are generated from the same source as the SNBT.',
 '', '## Review boundary','',
 'The PNG is a layout preview, not an in-game screenshot. Standard item sprites are used where available; a few 3D block icons are represented by labels in this preview. Minecraft renders the real item icons. Native rendering, font scaling, reward claiming and live task behaviour still need an in-game check.',
 '', '## Opening it','',
 f'Chapter ID: `{CHID}`. Group ID: `{GROUP}`.',
 '', 'Restart the client to load the added Open Loader texture, or reload client resources if that loader has already discovered it. Reload quest definitions with `/ftbquests reload` using an account with permission. In multiplayer, quest definitions come from the server; a client-only copy is not sufficient. No reload or server restart was performed by this authoring script.',
 '', '## Quest contents','']
for q in quests:
 readme+=['### '+q['title'],'',q['subtitle'],'']
 readme +=[re.sub(r'&[0-9a-fklmnor]','',s) for s in q['description']]
 readme+=['','Tasks:']+['- '+t['title'] for t in q['tasks']]+['']
(OUT/'chapter-guide.md').write_text('\n'.join(readme),'utf-8')
print(json.dumps({'chapter_id':CHID,'group_id':GROUP,'quests':len(quests),'optional':sum(q['optional'] for q in quests),'projects':sum(not q['optional'] for q in quests),'task_count':sum(len(q['tasks']) for q in quests),'texture':str(TEXTURE),'preview':str(OUT/'layout-preview.png')},indent=2))
