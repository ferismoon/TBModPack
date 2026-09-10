import json,re,html,tomllib,hashlib
from pathlib import Path
from collections import Counter
base=Path(__file__).parent; root=base.parent.parent
rows=json.loads((base/'inventory-evidence.json').read_text('utf-8'))
lookup={r['key']:r for r in rows}
curated={}
for line in (base/'features.tsv').read_text('utf-8').splitlines():
 key,primary,cross,family,detail=line.split('\t')
 assert key not in curated and key in lookup,key
 curated[key]=(primary,cross.split(',') if cross else [],family,detail)
groups={
 'Performance and fixes': 'c2me clumps createbetterfps debugify enhanced-block-entities entityculling fastboot faster-random fastquit ferritecore-fabric forcecloseworldloadingscreen icterine immediatelyfast keybind-fix ksyxis let-me-despawn lithium lmft memoryleakfix modernfix moreculling neruina not-enough-crashes notenoughrecipebook packet-fixer ridingmousefix rrls sodium structure-essentials-forge-fabric structure-layout-optimizer stutterfix',
 'Visuals and sound': '3dskinlayers advancement-plaques-fabric ambientsounds boat-item-view chat-heads cit-resewn colorwheel colorwheel-patcher continuity coolrain drippy-loading-screen eating-animation-fabric entity-model-features entitytexturefeatures euphoria-patches fadeless fancymenu illagerblabber irisshaders lambdynamiclights not-enough-animations nuit nuit-interop particle-rain presence-footsteps show-me-your-skin sound-physics-remastered subtle-effects sun-and-moon-celestial-configuration tiny-item-animations travelers-titles-fabric typewriter-daycounter visuality what-are-they-up-to',
 'Interface and controls': 'advancementinfo appleskin better-mount-hud bridging-mod configured controlling cubes-without-borders detail-armor-bar enchantment-descriptions extreme-sound-muffler-fabric-official inventory-hud-forge jade jade-addons-fabric justenoughbreeding magnesium-extras modernworldcreation modmenu more-enchantment-info mouse-tweaks no-chat-reports no-chat-restrictions no-resource-pack-warnings puzzle reeses-sodium-options rei roughly-enough-professions-rep screenshot-viewer screenshottoclipboard show-me-what-you-got smooth-scroll sodium-extra sort-it-out stack-refill Stfu-1.2.3 tool-stats tooltip-overhaul trashslot xaeros-minimap xaeros-world-map zoomify',
 'Compatibility and integrations': 'ftb-xmod-compat indium lets-do-addon-compat loot-integrations loot-integrations-choicetheorems-overhauled loot-integrations-dungeons-and-taverns loot-integrations-moogs-voyager-soaring-end-nether loot-integrations-structory-towers polymorph polymorphic-tom radiant-gear yung-structures-addon-for-loot-integrations',
 'Pack and admin tools': 'chunky-pregenerator crafttweaker default-options item-obliterator kubejs kubejs-create-for-fabric-1-20-1 log-begone log-cleaner mixin-conflict-helper mixintrace open-loader packwiz-modpack-loader quests-additions-fabric spark sparse-structures stackdeobf worldedit worldeditcui-fabric yosbr',
}
assigned={}
for group,keys in groups.items():
 for key in keys.split():
  assert key in lookup and key not in curated and key not in assigned,key
  assigned[key]=group
help_cross={'rei':['Shared foundations'],'jade':['Shared foundations'],'appleskin':['Cook','Farmer'],'justenoughbreeding':['Rancher'],'roughly-enough-professions-rep':['Merchant'],'xaeros-minimap':['Explorer'],'xaeros-world-map':['Explorer'],'bridging-mod':['Builder'],'enchantment-descriptions':['Witch','Blacksmith'],'more-enchantment-info':['Witch','Blacksmith'],'tool-stats':['Blacksmith'],'lambdynamiclights':['Explorer'],'radiant-gear':['Explorer'],'polymorphic-tom':['Quartermaster'],'polymorph':['Shared foundations'],'sparse-structures':['Explorer'],'worldedit':['Builder'],'worldeditcui-fabric':['Builder'],'lets-do-addon-compat':['Farmer','Cook','Brewer']}
overrides={
 'rei':'Recipe and usage lookup across the pack; the first tool for checking effective crafting after custom scripts load.',
 'jade':'Identifies targeted blocks/entities and exposes supported information; helps newcomers understand unfamiliar content.',
 'jade-addons-fabric':'Extends Jade information for supported modded blocks and systems.',
 'appleskin':'Shows additional hunger/saturation information for choosing meals and understanding food value.',
 'justenoughbreeding':'Shows supported animal breeding information in the recipe viewer; a Rancher reference rather than an animal-content mod.',
 'roughly-enough-professions-rep':'Shows profession information in REI; useful when planning villager workstations and trades.',
 'xaeros-minimap':'Local minimap and navigation interface for finding the way around explored areas.',
 'xaeros-world-map':'Exploration map for reviewing discovered terrain and planning routes.',
 'worldedit':'Administrative/creative world editing; do not make operator permissions a survival Builder requirement.',
 'worldeditcui-fabric':'Visual selection interface for WorldEdit; primarily an administrative or creative building aid.',
 'polymorphic-tom':'Adds recipe-conflict selection integration to Tom\'s Simple Storage crafting interface.',
 'radiant-gear':'Connects accessory-slot equipment with dynamic-light support, relevant to carried/worn lighting.',
 'kubejs':'Pack scripting supplies custom items, recipes, loot and data changes. Those gameplay additions are catalogued in the pack-specific section.',
 'crafttweaker':'Pack scripts change crafting, smithing, Create processing, tags and attributes. The complete local script index is included below.',
 'sparse-structures':'Controls structure spacing; canonical config uses general factor 1.2 and mansion override 2, with further pack structure overrides.',
 'quests-additions-fabric':'Adds task/reward capabilities to FTB Quests; a quest-authoring extension rather than an independent profession.',
 'Stfu-1.2.3':'A local convenience/fix mod. Metadata describes minor annoyance fixes; exact toggles were not independently verified, so no standalone gameplay claims are made.',
 'euphoria-patches':'Shader customization/compatibility support; affects presentation rather than adding a survival content progression.',
 'loot-integrations-choicetheorems-overhauled':'Connects additional loot to CTOV and Immersive Structures containers.',
 'loot-integrations-dungeons-and-taverns':'Connects additional loot to Dungeons and Taverns structures.',
 'loot-integrations-moogs-voyager-soaring-end-nether':'Loot compatibility for supported Moog structure packs. Its name does not prove all named packs are installed.',
 'loot-integrations-structory-towers':'Loot compatibility for Structory and Structory Towers.',
 'yung-structures-addon-for-loot-integrations':'Loot compatibility for supported YUNG structure mods.',
}
fallbacks={
 'Performance and fixes':'Improves runtime efficiency or corrects behaviour; not a separate activity or collection tree.',
 'Visuals and sound':'Changes presentation, animation, lighting, weather or audio; supports the experience without supplying its own profession.',
 'Interface and controls':'Improves information, configuration, controls or inventory interaction; explain useful controls in shared onboarding.',
 'Compatibility and integrations':'Connects supported mods or resolves interactions; feature ownership remains with the participating content mods.',
 'Pack and admin tools':'Supports pack configuration, maintenance, diagnostics or authoring; not a normal survival profession.',
 'Libraries and APIs':'Shared code, loading, configuration, rendering, entity or guidebook infrastructure used by other mods; not an independent quest path.',
}
for r in rows:
 if r['key'] in curated:
  r['primary'],r['cross'],r['family'],r['detail']=curated[r['key']];r['kind']='Gameplay / rule / pack feature'
 else:
  r['primary']=assigned.get(r['key'],'Libraries and APIs');r['cross']=help_cross.get(r['key'],[]);r['family']=r['primary'];r['kind']='Supporting mod'
  r['detail']=overrides.get(r['key'],fallbacks[r['primary']])
  desc=(r.get('description') or r.get('project_description','')).strip()
  r['metadata_excerpt']=' '.join(desc.split()[:22]) if desc else ''
 r['names']=[{'key':k,'name':re.sub('§.','',v)} for k,v in r.get('lang',{}).items() if len(k.split('.'))==3]
 r['names'].sort(key=lambda x:(x['key'].split('.')[0],x['name'].casefold()))
 r['version']=r.get('version','not declared in parsed metadata')
 if r['key']=='trinketlantern-1.0.1':r['source']=''
index=tomllib.loads((root/'index.toml').read_text('utf-8'))
indexed={x['file'] for x in index['files'] if x['file'].startswith('mods/')}
actual={'mods/'+r['file'] for r in rows}
assert actual==indexed,(actual-indexed,indexed-actual)
assert len(rows)==len({r['key'] for r in rows})==423
assert all(r['present'] for r in rows)
paths=['Mechanic','Farmer','Cook','Brewer','Witch','Builder','Collector','Explorer','Angler','Rancher','Blacksmith','Adventurer','Merchant','Quartermaster','Shared foundations','Pack customization']
allgroups=paths+list(groups)+['Libraries and APIs']
counts=Counter(r['primary'] for r in rows)
coverage={'files':len(rows),'packwiz_records':sum(r['file'].endswith('.toml') for r in rows),'direct_jars':sum(r['file'].endswith('.jar') for r in rows),'local_jars':sum(bool(r['present']) for r in rows),'indexed_files':len(indexed),'curated_entries':len(curated),'supporting_entries':len(rows)-len(curated),'unclassified':sum(not r.get('primary') for r in rows),'jar_read_errors':[{r['key']:r['error']} for r in rows if 'error'in r],'primary_counts':dict(counts)}
(base/'coverage.json').write_text(json.dumps(coverage,indent=2),'utf-8')
overview=(base/'overview.md').read_text('utf-8')
md=[overview,'\n## Coverage by primary home\n','| Home | Mod files |','| --- | ---: |']
for g in allgroups:md.append(f'| {g} | {counts[g]} |')
md+=['\nA mod appears once in the sections below. Crossover references are part of its record and searchable in the HTML catalogue.\n']
for g in allgroups:
 md.append('\n## '+('The '+g if g in paths[:14] else g)+'\n')
 for r in sorted((x for x in rows if x['primary']==g),key=lambda x:x['name'].casefold()):
  md.extend(['\n### '+r['name']+'\n','**Feature family:** '+r['family']+'. **Also serves:** '+(', '.join(r['cross']) or '—')+'.\n',r['detail']+'\n'])
  if r.get('metadata_excerpt'):md.append('Short installed-metadata excerpt: “'+r['metadata_excerpt']+'”.\n')
  names=list(dict.fromkeys(n['name'] for n in r['names']))
  if names and r['key']in curated:md.append('**Installed-name examples:** '+', '.join(names[:36])+('. Full extracted list in the HTML catalogue.' if len(names)>36 else '.')+'\n')
  md.append('**Version:** '+str(r['version'])+'. **File:** `mods/'+r['file']+'`. '+ ('[Project page]('+r['source']+').' if r['source'] else 'Source: local jar metadata/assets; no trusted project URL supplied.')+'\n')
scripts=[]
for folder in [root/'scripts',root/'kubejs/server_scripts',root/'kubejs/startup_scripts',root/'kubejs/client_scripts']:
 for p in sorted(folder.rglob('*')):
  if p.suffix not in ['.js','.zs']:continue
  t=p.read_text('utf-8',errors='replace')
  # Inventory references, not a claim that every referenced item is created or obtainable.
  refs=sorted(set(re.findall(r'(?:[a-z][a-z0-9_]*):[a-z0-9_/]+',t)))
  scripts.append({'path':p.relative_to(root).as_posix(),'refs':refs,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
md+=['\n## Complete custom-script index\n','Every .zs and gameplay/client .js file is listed here; item/tag references are indexed in the HTML appendix. These include removals and compatibility references, not only additions.\n']
for s in scripts:md.append('- `'+s['path']+'`')
(base/'feature-catalogue.md').write_text('\n'.join(md),'utf-8')
# Small renderer for this controlled report's headings, paragraphs, links and tables.
def inline(t):
 t=html.escape(t)
 t=re.sub(r'`([^`]+)`',r'<code>\1</code>',t)
 t=re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)',r'<a href="\2" target="_blank" rel="noreferrer">\1</a>',t)
 return t
def render(t):
 out=[];table=False
 for line in t.splitlines():
  if line.startswith('|'):
   cells=[x.strip() for x in line.strip('|').split('|')]
   if all(re.fullmatch(r'[: -]+',x) for x in cells):continue
   if not table:out.append('<div class="tablewrap"><table>');table=True;tag='th'
   else:tag='td'
   out.append('<tr>'+''.join(f'<{tag}>{inline(c)}</{tag}>' for c in cells)+'</tr>');continue
  if table:out.append('</table></div>');table=False
  if not line.strip():continue
  if line.startswith('#'):
   n=len(line)-len(line.lstrip('#'));out.append(f'<h{n}>'+inline(line[n:].strip())+f'</h{n}>')
  else:out.append('<p>'+inline(line)+'</p>')
 if table:out.append('</table></div>')
 return '\n'.join(out)
data=[{k:r[k] for k in ['key','name','primary','cross','family','detail','version','jar','file','side','source','kind','names','biomes','structures'] if k in r}|{'recipeCount':len(r.get('recipes',[])),'metadata_excerpt':r.get('metadata_excerpt','')} for r in rows]
payload=json.dumps(data,ensure_ascii=False).replace('<','\\u003c')
script_payload=json.dumps(scripts,ensure_ascii=False).replace('<','\\u003c')
page='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Forced Relocation · Feature catalogue</title><style>
:root{color-scheme:light;--ink:#203c34;--muted:#56665f;--line:#d2dbd2;--paper:#faf9f3;--accent:#356b55}*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font:16px/1.65 system-ui,sans-serif}header{background:#203c34;color:#fff;padding:42px max(24px,calc((100vw - 1160px)/2));}header p{color:#d7e3da;max-width:760px}h1{font:600 clamp(29px,4vw,44px)/1.2 Georgia,serif;margin:0 0 16px}h2{font:600 28px/1.3 Georgia,serif;margin-top:32px}h3{font-size:20px;margin:0 0 8px}main{max-width:1208px;margin:auto;padding:24px}a{color:#27694f}header a{color:#e0f3dc}.stats{display:flex;gap:14px;flex-wrap:wrap}.stat{border:1px solid #81988c;padding:10px 20px;border-radius:8px}.stat b{font-size:24px;display:block}.toolbar{position:sticky;top:0;background:#faf9f3f7;padding:16px 0;z-index:2;border-bottom:1px solid var(--line);display:flex;gap:10px;flex-wrap:wrap}input,select,button{font:inherit;padding:9px 12px;border:1px solid #9daea2;border-radius:6px;background:white;color:var(--ink)}input{flex:1;min-width:240px}button{cursor:pointer}.card{padding:23px;background:white;border:1px solid var(--line);border-radius:10px;margin:16px 0}.meta{font-size:13px;color:var(--muted);overflow-wrap:anywhere}.pill{display:inline-block;border-radius:20px;background:#e9eee4;color:#35563e;padding:2px 10px;margin:0 5px 5px 0;font-size:13px}.sub{background:#f2eadb;color:#645032}.tablewrap{overflow:auto}table{border-collapse:collapse;width:100%;font-size:14px;margin:16px 0}td,th{border:1px solid var(--line);padding:10px;text-align:left;vertical-align:top}th{background:#e9eee4}details{margin:16px 0}summary{cursor:pointer;font-weight:600}code{font-size:13px;overflow-wrap:anywhere}.names{max-height:420px;overflow:auto;border-top:1px solid var(--line);margin-top:12px}.names td:first-child{width:44%}.muted{color:var(--muted)}.intro{border-bottom:1px solid var(--line);padding-bottom:20px}.intro h1{display:none}.count{font-size:14px;margin-top:12px}.toplinks{display:flex;gap:24px;flex-wrap:wrap}.notice{background:#eeeadd;padding:15px 20px;border-radius:8px}footer{padding:40px 0;color:var(--muted)}@media print{.toolbar,.toplinks,button{display:none}header{background:white;color:black;padding:0}.card{break-inside:avoid}.names{max-height:none}body{font-size:11pt}}
</style></head><body><header><p>FORCED RELOCATION · QUEST PLANNING · 9 SEPTEMBER 2026</p><h1>Find the paths through the pack.</h1><p>A detailed feature catalogue covering every canonical mod file, with crossover paths, installed content names and the pack's own changes.</p><div class="stats"><div class="stat"><b>423 / 423</b>mod files accounted for</div><div class="stat"><b>14</b>candidate player paths</div><div class="stat"><b>0</b>unclassified files</div></div></header><main><nav class="toplinks"><a href="#catalogue">Browse the catalogue</a><a href="#scripts">Custom script index</a><a href="feature-catalogue.md">Read the full Markdown document</a></nav><details class="intro" open><summary>Path map, scope and pack-specific findings</summary>OVERVIEW</details><section id="catalogue"><h2>Mod and feature catalogue</h2><p>Choose a path to include its main mods and all crossover contributions. Search also checks every extracted content name. Expand a mod to see its complete installed-name list.</p><p class="notice">Extracted names are discovery candidates. They can include disabled, creative-only, compatibility or unused assets. This is not a verified list of obtainable survival items.</p><div class="toolbar"><input id="search" aria-label="Search mods and features" placeholder="Search mods, features, items, creatures…"><select id="path" aria-label="Filter by path"><option value="">All paths and support</option></select><select id="kind" aria-label="Filter by kind"><option value="">All mods</option><option value="gameplay">Gameplay and shared rules</option><option value="support">Supporting mods only</option></select><button id="reset">Reset</button></div><div id="count" class="count" aria-live="polite"></div><div id="cards"></div></section><section id="scripts"><h2>Complete custom script index</h2><p>All SCRIPTCOUNT script files under scripts and KubeJS startup/server/client scripts. Expand to see referenced identifiers; these include additions, removals and compatibility references.</p><div id="scriptlist"></div></section><footer>Planning audit only. No quests, configuration, Packwiz metadata or public navigation were changed. Source data: canonical Packwiz records, locally available matching jars, configuration and scripts, plus project references.</footer></main><script>
const mods=PAYLOAD;const scripts=SCRIPTS;const groups=GROUPS;
const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const search=document.getElementById('search'),path=document.getElementById('path'),kind=document.getElementById('kind');
groups.forEach(g=>{const o=document.createElement('option');o.value=g;o.textContent=g;path.append(o)});
mods.forEach(m=>m.searchText=[m.name,m.key,m.family,m.detail,m.primary,...m.cross,...m.names.map(n=>n.name+' '+n.key),...(m.biomes||[]),...(m.structures||[])].join(' ').toLowerCase());
function content(m){let h='';if(m.names.length)h+='<details><summary>Installed content names ('+m.names.length+')</summary><div class="names"><table><tr><th>Name</th><th>Asset key</th></tr>'+m.names.map(n=>'<tr><td>'+esc(n.name)+'</td><td><code>'+esc(n.key)+'</code></td></tr>').join('')+'</table></div></details>';for(const field of ['biomes','structures'])if(m[field]?.length)h+='<details><summary>Packaged '+field+' ('+m[field].length+')</summary><div class="names">'+m[field].map(x=>'<div><code>'+esc(x)+'</code></div>').join('')+'</div></details>';return h}
function draw(){const q=search.value.toLowerCase().trim(),p=path.value,k=kind.value;const list=mods.filter(m=>(!q||m.searchText.includes(q))&&(!p||m.primary===p||m.cross.includes(p))&&(!k||(k==='support')===(m.kind==='Supporting mod')));document.getElementById('count').textContent=list.length+' of '+mods.length+' mod files shown';document.getElementById('cards').innerHTML=list.map(m=>'<article class="card" data-key="'+esc(m.key)+'"><div><span class="pill">'+esc(m.primary)+'</span>'+m.cross.map(x=>'<span class="pill sub">Also: '+esc(x)+'</span>').join('')+'</div><h3>'+esc(m.name)+'</h3><div class="meta">'+esc(m.family)+' · '+esc(m.kind)+'</div><p>'+esc(m.detail)+'</p>'+(m.metadata_excerpt?'<p class="meta">Short metadata excerpt: “'+esc(m.metadata_excerpt)+'”.</p>':'')+content(m)+'<p class="meta">Version '+esc(m.version)+' · '+esc(m.side)+' · '+m.recipeCount+' packaged recipe files (before pack changes)<br>'+esc(m.jar)+'<br>Pack record: '+esc(m.file)+(m.source?' · <a href="'+esc(m.source)+'" target="_blank" rel="noreferrer">Project page</a>':' · Local jar evidence')+'</p></article>').join('')||'<p>No matching entries.</p>'}
[search,path,kind].forEach(e=>e.addEventListener('input',draw));document.getElementById('reset').onclick=()=>{search.value='';path.value='';kind.value='';draw()};
document.getElementById('scriptlist').innerHTML=scripts.map(s=>'<details><summary><code>'+esc(s.path)+'</code></summary><div class="names">'+s.refs.map(x=>'<span class="pill">'+esc(x)+'</span>').join('')+'</div></details>').join('');draw();
</script></body></html>'''
page=page.replace('OVERVIEW',render(overview)).replace('SCRIPTCOUNT',str(len(scripts))).replace('PAYLOAD',payload).replace('SCRIPTS',script_payload).replace('GROUPS',json.dumps(allgroups))
(base/'feature-catalogue.html').write_text(page,'utf-8')
(base/'categorized-inventory.json').write_text(json.dumps(data,indent=2,ensure_ascii=False),'utf-8')
print(json.dumps(coverage,indent=2))
print('SCRIPTS',len(scripts),'NAMES',sum(len(r['names']) for r in rows),'HTML_BYTES',len(page.encode()))
print('LIBRARY_REVIEW',','.join(r['key'] for r in rows if r['primary']=='Libraries and APIs'))
