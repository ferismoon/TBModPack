"""Build the Mechanic path using the installed mod data; stage before installation."""
import hashlib,io,json,re,sys,zipfile
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
ROOT=Path('I:/McWork'); OUT=ROOT/'docs/quest-planning/mechanic'; STAGE=OUT/'staged'
OUT.mkdir(exist_ok=True);STAGE.mkdir(exist_ok=True)
sys.path.insert(0,str(ROOT/'ui-workshop/quest-validation-deps'))
import nbtlib
def uid(s):return f'{int(hashlib.sha256(("forced_relocation/mechanic/v1/"+s).encode()).hexdigest()[:16],16)&0x7fffffffffffffff:016X}'
GROUP=uid('group'); chapters=[]; evidence={}; jars={}; langs={}
project_icons={'brief':'create:wrench','ponder':'minecraft:book','power':'create:water_wheel','control':'create:clutch','job':'create:mechanical_press','open':'create:goggles',
 'prodbrief':'minecraft:paper','route':'create:belt_connector','fluids':'create:mechanical_pump','materials':'create:crushing_wheel','assembly':'create:mechanical_crafter','overflow':'create:stockpile_switch','productionservice':'create:brass_funnel',
 'movebrief':'create:super_glue','movingframe':'create:mechanical_bearing','movingjob':'create:mechanical_harvester','railservice':'create:track_station','order':'create:stock_ticker','reliable':'create:track',
 'specialbrief':'create:speedometer','shell':'copycats:copycat_block','electric':'createaddition:electric_motor','stone':'createcobblestone:mechanical_generator','connected':'create_connected:parallel_gearbox','capacity':'createaddition:alternator','enchant':'create_enchantment_industry:printer','jetpack':'create_jetpack:jetpack','upgrade':'create:steam_engine'}
rows=json.loads((ROOT/'docs/quest-planning/inventory-evidence.json').read_text('utf-8'))
for row in rows:
 if row['key'].startswith('create') or row['key']=='copycats':
  path=Path(row['present'][0]);z=zipfile.ZipFile(path);jars[row['modid']]=z
  evidence[row['key']]={'jar':path.name,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
  for name in z.namelist():
   if name.endswith('/lang/en_us.json'):langs.update(json.loads(z.read(name)))
vanilla=zipfile.ZipFile('I:/PrismLauncher/libraries/com/mojang/minecraft/1.20.1/minecraft-1.20.1-client.jar')
jars['minecraft']=vanilla;langs.update(json.loads(vanilla.read('assets/minecraft/lang/en_us.json')))
def label(item):
 ns,key=item.split(':')
 for prefix in ['item','block']:
  name=f'{prefix}.{ns}.{key}'
  if name in langs:return langs[name]
 raise ValueError('No installed item/block name: '+item)
def esc(s):return s.replace('&',r'\&')
def item(target,count=1):return {'type':'item','item':target,'count':count,'consume_items':False,'only_from_crafting':False,'match_nbt':False,'title':f'Have {count} '+label(target)}
def done(text):return {'type':'checkmark','title':text}
def adv(key):
 name='data/create/advancements/'+key+'.json';assert name in jars['create'].namelist()
 data=json.loads(jars['create'].read(name));desc=langs[data['display']['description']['translate']]
 return {'type':'advancement','advancement':'create:'+key,'criterion':'','title':desc}
def chapter(key,title,strap,lanes,icon):
 c={'filename':'10_mechanic_'+key,'id':uid('chapter/'+key),'group':GROUP,'title':esc(title),'icon':icon,'order_index':len(chapters),'default_quest_shape':'circle','default_hide_dependency_lines':False,'quest_links':[],'quests':[]}
 c['_key']=key;c['_strap']=strap;c['_lanes']=lanes;chapters.append(c);return c
def q(c,key,title,description,task,reward,count,x,y,kind='experiment',deps=()):
 if key in ['productionservice','reliable','upgrade']:kind='milestone'
 label(reward)
 task=dict(task,id=uid('task/'+key));task['title']=esc(task['title'])
 icon=project_icons.get(key) or task.get('item') or reward
 label(icon)
 if task['type']=='advancement':
  data=json.loads(jars['create'].read('data/create/advancements/'+task['advancement'].split(':')[1]+'.json'));icon=data['display']['icon']['item']
 quest={'id':uid('quest/'+key),'title':esc(title),'subtitle':{'experiment':'Optional practice','project':'Project — confirm after testing','reference':'Optional guidance','milestone':'Path milestone — confirm after testing'}[kind],
  'icon':icon,'x':float(x),'y':float(y),'size':1.35 if kind in ['project','milestone'] else .95,'shape':'diamond' if kind in ['project','milestone'] else 'square' if kind=='reference' else 'circle',
  'optional':kind!='milestone','description':[esc(description)],'tasks':[task],
  'rewards':[{'id':uid('reward/'+key),'type':'item','item':reward,'count':count}]}
 if deps:quest['dependencies']=[uid('quest/'+d) for d in deps]
 c['quests'].append(quest)

c=chapter('workshop','Your First Workshop','Power a job. Understand it. Make it useful.',['POWER','CONTROL','A USEFUL JOB'],'create:wrench')
q(c,'brief','The Mechanic',"Choose a job you want machinery to do. Chapters are open; small quests are optional. Each task has an item reward. Diamond projects use your confirmation; existing and shared machines count. Agree with your quest team before confirming.",done('Choose a useful job for your workshop'),'create:andesite_alloy',2,0,-7,'reference')
q(c,'ponder','See It in Motion','Open a Ponder scene for a machine you want to use. Watch how power reaches it, then check its current recipe in REI.',done('Watch a relevant Ponder scene'),'minecraft:iron_nugget',8,-5,-3.4,'reference')
q(c,'wrench','Tools of the Trade','Have a wrench ready for adjusting machinery. Use it to rotate a part or recover one before rebuilding your power route.',item('create:wrench'),'create:shaft',4,0,-3.4)
q(c,'press','Your First Sheets','Use a powered press to flatten ingots. Ponder shows the working space beneath it; this task tracks Create’s pressing advancement.',adv('mechanical_press'),'minecraft:iron_ingot',4,5,-3.4)
q(c,'wheel','Let the River Work','Place a water wheel in moving water to generate rotation. This is one power option; the workshop project accepts other sources too.',adv('water_wheel'),'create:cogwheel',4,-5,-.7)
q(c,'goggles','Read the Problem','Have engineer’s goggles available, then inspect a running network. Speed and stress capacity answer different questions; check both before expanding.',item('create:goggles'),'minecraft:redstone',8,0,-.7)
q(c,'mill','Grain into Ingredients','Process a suitable ingredient in a millstone. Check REI for a result your kitchen or workshop actually needs.',adv('millstone'),'minecraft:wheat',8,5,-.7)
q(c,'power','Power That Holds','Run your chosen machine under load without overstressing the network. Water, wind or another suitable source all count.',done('My chosen machine runs under load'),'create:andesite_alloy',8,-5,2.2,'project')
q(c,'control','Start, Stop & Adjust','Give the machine an accessible stop control and test it. Set its direction and speed for the job, then restart successfully.',done('I tested stopping and restarting the machine'),'create:shaft',8,0,2.2,'project')
q(c,'job','A Job Off Your Hands','Use your powered workshop to finish a useful batch of at least eight outputs. Choose the recipe yourself and keep the result.',done('My workshop completed a useful batch'),'minecraft:copper_ingot',8,5,2.2,'project')
q(c,'open','Open for Business','Your workshop has dependable power, usable controls and a finished job. Claim supplies for its next improvement; none of the optional examples is required.',done('The workshop is ready for its next job'),'create:andesite_casing',8,0,6.3,'milestone',('power','control','job'))

c=chapter('production','Production Lines','Follow the product, from ingredients to a useful result.',['PROCESS','COMBINE','KEEP IT RUNNING'],'create:mechanical_mixer')
q(c,'prodbrief','Start with the Output','Pick a product you regularly need. Read its recipe backwards to identify processing, ingredients and transport; build only the stages your product needs.',done('Choose a product and identify its recipe stages'),'minecraft:iron_ingot',2,0,-7,'reference')
q(c,'fan','Let the Air Do It','Use an encased fan to process material. The block in its airflow determines the process; check Ponder and REI for your chosen recipe.',adv('fan_processing'),'minecraft:coal',8,-5,-3.4)
q(c,'mix','A Proper Mixture','Combine ingredients with a mechanical mixer and basin. Match the recipe’s speed and heat needs; unheated recipes make a useful first experiment.',adv('mechanical_mixer'),'minecraft:copper_ingot',6,0,-3.4)
q(c,'route','From Input to Output','Route a batch between two work areas without carrying it yourself. Belts, chutes or funnels are options; collect the result somewhere accessible.',done('A batch reached its output storage'),'create:belt_connector',4,5,-3.4,'project')
q(c,'saw','Cut to Order','Use an upright mechanical saw to process material. Select a useful recipe and collect the cut result.',adv('saw_processing'),'minecraft:oak_log',16,-5,-.7)
q(c,'precision','A Little Precision','Have one precision mechanism available. For your own production, inspect its sequenced assembly recipe and keep unfinished parts cycling until complete.',item('create:precision_mechanism'),'minecraft:gold_ingot',4,0,-.7)
q(c,'fluids','No More Bucket Runs','Pump a useful fluid into storage or a processing station and use it there. Check pump direction and keep the system from starving its recipe.',done('My fluid feed supplied a working process'),'create:fluid_pipe',8,5,-.7,'project')
q(c,'materials','Make the Materials Count','Run an ore or bulk-material batch through a processing route you chose in REI. Collect and use its output; crushing is an option, not a required detour.',done('I processed and used a material batch'),'minecraft:iron_ingot',12,-5,2.2,'project')
q(c,'assembly','A Repeatable Recipe','Set up a heated recipe, sequenced assembly or mechanical crafting job. Complete two batches with the same setup; brass and precision mechanisms are useful starting choices.',done('The same setup completed two batches'),'create:brass_ingot',8,0,2.2,'project')
q(c,'overflow','When the Box Is Full','Test your output storage filling up. Add a shutoff, overflow route or buffer so the line can recover, then test the next batch.',done('The line recovered from full output storage'),'minecraft:redstone',16,5,2.2,'project')
q(c,'productionservice','Leave It Working','Choose one production line and run three batches without moving ingredients between its stages by hand. Other branches on this page are optional.',done('One line completed three batches without hand transfers'),'create:brass_casing',8,0,6.3,'project')

c=chapter('movement','Movement & Delivery','Move the work, the goods, or yourself.',['CONTRAPTIONS','RAILWAYS','DELIVERIES'],'create:track')
q(c,'movebrief','Choose the Journey','Choose something worth moving: a harvest, a platform, passengers or supplies. These are independent projects; you do not need a railway to finish a moving machine.',done('Choose a movement or delivery project'),'minecraft:slime_ball',4,0,-7,'reference')
q(c,'movingframe','Make It Move','Build a small moving assembly using a bearing, piston, pulley or minecart. Test its travel and return before adding a working tool.',done('My assembly moved and returned safely'),'create:linear_chassis',4,-5,-3.4,'project')
q(c,'train','All Aboard','Assemble a train at a station. Keep the first design small and leave enough clear track to test it.',adv('train'),'create:track',32,0,-3.4)
q(c,'package','Pack the Order','Use a packager to take items from an inventory and make a package. Check its addressing controls before designing a delivery route.',adv('packager'),'create:cardboard',16,5,-3.4)
q(c,'interface','Unload Without Dismantling','Transfer items to or from a contraption with a portable storage interface. Ponder shows the docking arrangement and required gap.',adv('portable_storage_interface'),'minecraft:barrel',4,-5,-.7)
q(c,'schedule','Give It a Timetable','Give a train driver a schedule. Choose stops and waiting conditions that match the route’s purpose.',adv('conductor'),'create:track',32,0,-.7)
q(c,'frog','Special Delivery','Catch a package from a chain conveyor with a frogport. Use matching addresses so the parcel reaches the intended destination.',adv('frogport'),'minecraft:chain',16,5,-.7)
q(c,'movingjob','A Machine with a Route','Use a moving assembly to harvest, drill, lift or perform another useful job. Collect the result and return the machine ready for another run.',done('My moving machine finished a useful job and returned'),'create:linear_chassis',8,-5,2.2,'project')
q(c,'railservice','A Railway with a Purpose','Carry passengers or a useful load between two stations and return. Steam ’n’ Rails adds conductors and railway options; use the ones that help your route.',done('My train completed a useful return service'),'create:track',64,0,2.2,'project')
q(c,'order','Order to Door','Request stock and deliver the correct package to its destination. Use Create’s stock tools and your chosen transport; test with a small order first.',done('A requested order arrived with the correct contents'),'create:cardboard',32,5,2.2,'project')
q(c,'reliable','A Reliable Service','Choose one route or moving machine and complete three useful runs. Fix any docking, timing or unloading problem before confirming.',done('One service completed three useful runs'),'minecraft:iron_ingot',24,0,6.3,'project')

c=chapter('specialists','Specialist Machinery','Choose the improvements your workshop actually needs.',['ENERGY','SPECIAL PROCESSES','WORKSHOP DESIGN'],'create:steam_engine')
q(c,'specialbrief','Choose Your Upgrade','Pick a limitation to solve: power, materials, enchanting or access. These projects stand alone; completing the whole page is optional.',done('Identify one useful workshop upgrade'),'minecraft:copper_ingot',4,0,-7,'reference')
q(c,'steam','A Head of Steam','Use a steam engine to generate rotation. Ponder explains the boiler; check its water and heat supply before attaching your load.',adv('steam_engine'),'minecraft:copper_ingot',16,-5,-3.4)
q(c,'wire','Wire for the Job','Have eight copper wires available. Create Crafts & Additions’ rolling mill supplies wire for electrical equipment; inspect its recipe in REI.',item('createaddition:copper_wire',8),'minecraft:copper_ingot',8,0,-3.4)
q(c,'shell','Give It a Home','Build an accessible casing or work area around a functioning machine. Copycats, Create Deco, Oxidized and Vibrant Vaults offer ways to fit it into your build.',done('My machine has a usable, accessible work area'),'minecraft:iron_ingot',8,5,-3.4,'project')
q(c,'electric','Power over a Wire','Use Crafts & Additions to supply an electric motor through an electrical connection and run a useful load. Inspect the equipment’s limits before wiring it.',done('An electrically supplied motor ran my chosen load'),'minecraft:redstone',16,-5,-.7,'project')
q(c,'stone','Stone on Demand','Use Create Cobblestone’s mechanical generator to produce a supported material. Set its type, supply rotation and collect a batch for a build.',done('The generator supplied material I used'),'minecraft:andesite',32,0,-.7,'project')
q(c,'connected','Fit the Space','Use a Create: Connected component to solve a real routing, control or fluid-storage problem. Compare its Ponder scene with the part it replaces.',done('A Connected component improved my working setup'),'create:andesite_alloy',12,5,-.7,'project')
q(c,'capacity','Room to Grow','Run your upgraded power system with the machines you actually use together. Keep spare capacity and make its fuel or water supply maintainable.',done('My upgraded system handled its intended combined load'),'minecraft:copper_ingot',24,-5,2.2,'project')
q(c,'enchant','Experience Put to Work','Use Enchantment Industry to complete a useful experience or enchanting process. Check its installed recipes and guides; choose a result you will actually use.',done('My Enchantment Industry setup produced a useful result'),'minecraft:book',8,0,2.2,'project')
q(c,'jetpack','Reach the Awkward Bit','Use a Create Jetpack for a useful building or maintenance job. Learn its controls and refilling method, then land safely.',done('I completed a useful job and landed safely'),'minecraft:copper_ingot',12,5,2.2,'project')
q(c,'upgrade','An Upgrade Worth Keeping','Use one specialist upgrade during a normal workshop job. Keep it because it solved your original problem; no other branch on this page is required.',done('One specialist upgrade proved useful in ordinary work'),'minecraft:iron_ingot',24,0,6.3,'project')

def snbt(o,level=0):
 if isinstance(o,dict):return '{\n'+',\n'.join('\t'*(level+1)+json.dumps(k)+': '+snbt(v,level+1) for k,v in o.items())+'\n'+'\t'*level+'}'
 if isinstance(o,list):return '['+', '.join(snbt(v,level+1) for v in o)+']'
 if isinstance(o,bool):return 'true' if o else 'false'
 if isinstance(o,float):return str(o)+'d'
 if isinstance(o,int):return str(o)
 return json.dumps(o,ensure_ascii=False)

S=80;W=1440;H=1600;origin=(720,800)
def xy(x,y):return round(origin[0]+S*x),round(origin[1]+S*y)
def font(n,bold=False):return ImageFont.truetype('C:/Windows/Fonts/'+('segoeuib.ttf' if bold else 'segoeui.ttf'),n)
colors=['#a9c8ac','#e0b76b','#99c5d7'];ink='#eee3ca';muted='#acbbb7'
def wrap(draw,text,x,y,width,n,color=ink,bold=False):
 words=text.split();lines=[];line=''
 for word in words:
  test=(line+' '+word).strip()
  if draw.textlength(test,font=font(n,bold))>width and line:lines.append(line);line=word
  else:line=test
 if line:lines.append(line)
 for i,line in enumerate(lines):draw.text((x,y+i*(n+5)),line,font=font(n,bold),fill=color,anchor='mt')

allids=[GROUP];rewardtotals={};checkcounts={};guide=['# The Mechanic','', 'Four open chapters. One task and one item reward per quest. No chapter requires completing another.','',
 'Text is kept to one short paragraph. Literal ampersands use a backslash in FTB text (encoded as a doubled backslash in SNBT).','',
 'Item tasks detect possession and do not consume the items. Advancement tasks use installed Create advancement definitions. Project tasks are explicit player confirmations. Existing work and shared builds count.','',
 'Rewards use the pack’s existing per-player reward policy. They are one-time claims; modest component bundles support more building. No reward supplies an item required by another item task in this path.','']
for c in chapters:
 for quest in c['quests']:
  if quest['y']==2.2:quest['y']=3.4
 key=c['_key'];im=Image.new('RGBA',(W,H),(0,0,0,0));d=ImageDraw.Draw(im)
 def center(text,x,y,n=24,col=ink,bold=False):d.text(xy(x,y),text,font=font(n,bold),fill=col,anchor='mm')
 center('T H E   M E C H A N I C',0,-9.4,21,muted)
 center(c['title'].replace(r'\&','&').upper(),0,-8.72,40,ink,True)
 center(c['_strap'],0,-8.12,22,muted)
 for x,lane,col in zip([-5,0,5],c['_lanes'],colors):
  d.rounded_rectangle([xy(x-2.3,-5.25),xy(x+2.3,4.45)],radius=18,fill=(26,36,40,240),outline=col,width=2)
  center(lane,x,-4.73,24,col,True)
 for quest in c['quests']:
  title=quest['title'].replace(r'\&','&');x,y=xy(quest['x'],1.65 if quest['y']==3.4 else quest['y']+.82)
  wrap(d,title,x,y,350,21,ink,True)
  reward=quest['rewards'][0];rtext=str(reward['count'])+' × '+label(reward['item'])
  wrap(d,rtext,x,y+60,340,16,muted)
 center('Choose projects freely. Small quests are optional practice.',0,8.55,21,muted)
 center('One task. One item reward. Existing work counts.',0,9.10,19,muted)
 tex='config/openloader/resources/ftbquests/assets/ftbquests/textures/chapters/mechanic_'+key+'.png'
 p=STAGE/tex;p.parent.mkdir(parents=True,exist_ok=True);im.save(p)
 c['images']=[{'image':'ftbquests:textures/chapters/mechanic_'+key+'.png','x':0.0,'y':0.0,'width':18.0,'height':20.0,'order':-100}]
 native={k:v for k,v in c.items() if not k.startswith('_')}
 path=STAGE/('config/ftbquests/quests/chapters/'+c['filename']+'.snbt');path.parent.mkdir(parents=True,exist_ok=True)
 serialized=snbt(native)+'\n';path.write_text(serialized,'utf-8',newline='\n');parsed=nbtlib.parse_nbt(serialized)
 assert str(parsed['title'])==c['title']
 allids.append(c['id']);guide+=['## '+c['title'].replace(r'\&','&'),'','| Quest | Task | Reward |','|---|---|---|']
 preview=Image.new('RGBA',im.size,'#141d22');preview.alpha_composite(im);pd=ImageDraw.Draw(preview)
 byid={q['id']:q for q in c['quests']}
 for quest in c['quests']:
  for dep in quest.get('dependencies',[]):
   a=byid[dep];pd.line([xy(a['x'],a['y']+.63),xy(quest['x'],quest['y']-.63)],fill='#718578',width=3)
 for quest in c['quests']:
  allids+=[quest['id'],quest['tasks'][0]['id'],quest['rewards'][0]['id']]
  task=quest['tasks'][0];reward=quest['rewards'][0]
  checkcounts[task['type']]=checkcounts.get(task['type'],0)+1
  rewardtotals[reward['item']]=rewardtotals.get(reward['item'],0)+reward['count']
  guide+=['| '+quest['title'].replace(r'\&','&')+' | '+task['title'].replace(r'\&','&')+' | '+str(reward['count'])+' '+label(reward['item'])+' |']
  x,y=xy(quest['x'],quest['y']);r=S*quest['size']*.45;col=colors[0 if quest['x']<0 else 2 if quest['x']>0 else 1]
  if quest['shape']=='diamond':pd.polygon([(x,y-r),(x+r,y),(x,y+r),(x-r,y)],fill='#233235',outline=col,width=4)
  elif quest['shape']=='square':pd.rounded_rectangle([x-r,y-r,x+r,y+r],radius=5,fill='#233235',outline=muted,width=3)
  else:pd.ellipse([x-r,y-r,x+r,y+r],fill='#233235',outline=col,width=3)
  ns,it=quest['icon'].split(':');z=jars.get(ns);names=z.namelist() if z else []
  candidates=[f'assets/{ns}/textures/item/{it}.png',f'assets/{ns}/textures/block/{it}.png',f'assets/{ns}/textures/block/{it}_side.png']
  texname=next((p for p in candidates if p in names),None)
  if texname:
   ico=Image.open(io.BytesIO(z.read(texname))).convert('RGBA');sz=round(r*1.15);ico.thumbnail((sz,sz),Image.Resampling.NEAREST);ico=ico.resize((sz,sz),Image.Resampling.NEAREST);preview.alpha_composite(ico,(x-sz//2,y-sz//2))
  else:pd.text((x,y),'GO' if quest['shape']=='diamond' else '?',font=font(21,True),fill=ink,anchor='mm')
 preview.convert('RGB').save(OUT/(key+'-preview.png'))
 guide+=['','### Short quest text','']
 for quest in c['quests']:guide+=['**'+quest['title'].replace(r'\&','&')+'** — '+quest['description'][0].replace(r'\&','&'),'']
assert len(allids)==len(set(allids))
quests=[q for c in chapters for q in c['quests']]
assert all(len(q['tasks'])==len(q['rewards'])==1 for q in quests)
assert max(len(q['description'][0].split()) for q in quests)<=45
assert not {q['tasks'][0]['item'] for q in quests if q['tasks'][0]['type']=='item'}.intersection(rewardtotals)
for c in chapters:
 for qst in c['quests']:
  for txt in [qst['title'],*qst['description'],qst['tasks'][0]['title']]:assert not re.search(r'(?<!\\)&',txt)
existing=set()
for p in (ROOT/'config/ftbquests/quests/chapters').glob('*.snbt'):
 if not p.name.startswith('10_mechanic_'):existing.update(re.findall(r'\b(?:"id"|id):\s*"([A-Fa-f0-9]{16})"',p.read_text('utf-8')))
assert not existing.intersection(allids)
manifest={'group_id':GROUP,'group_title':'The Mechanic','chapters':[{k:v for k,v in c.items() if not k.startswith('_')} for c in chapters],'files':[p.relative_to(STAGE).as_posix() for p in STAGE.rglob('*') if p.is_file()]}
(OUT/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),'utf-8',newline='\n')
(OUT/'quest-guide.md').write_text('\n'.join(guide),'utf-8',newline='\n')
report={'chapters':len(chapters),'quests':len(quests),'rewarded_tasks':len(quests),'task_types':checkcounts,'max_description_words':max(len(q['description'][0].split()) for q in quests),'unique_ids':len(allids),'checks':['SNBT parse and escaped ampersand round-trip','unique IDs and no collisions with other chapters','installed language names for items and rewards','installed Create advancement definitions','one reward for each single-task quest','no reward fulfils another item task'],'reward_totals':rewardtotals,'installed_mod_evidence':evidence,'in_game_test':'not performed'}
(OUT/'validation.json').write_text(json.dumps(report,indent=2),'utf-8',newline='\n')
print(json.dumps({k:v for k,v in report.items() if k not in ['installed_mod_evidence','reward_totals']},indent=2))
