import json,tomllib,zipfile,re,urllib.request,urllib.parse
from pathlib import Path
root=Path('I:/McWork'); out=root/'docs/quest-planning'
locations=[root/'mods',Path('I:/PrismLauncher/instances/Forced Relocation/minecraft/mods'),Path('I:/MC SERVER/mods')]
rows=[]
for p in sorted((root/'mods').iterdir()):
 if not p.is_file(): continue
 d=tomllib.loads(p.read_text('utf-8')) if p.name.endswith('.toml') else {'name':p.stem,'filename':p.name,'side':'unspecified'}
 r={'key':p.name.removesuffix('.pw.toml').removesuffix('.jar'),'name':d['name'],'file':p.name,'jar':d['filename'],'side':d.get('side'),'update':d.get('update',{})}
 r['source']='https://modrinth.com/mod/'+str(d['update']['modrinth']['mod-id']) if 'modrinth' in d.get('update',{}) else ('https://www.curseforge.com/projects/'+str(d['update']['curseforge']['project-id']) if 'curseforge' in d.get('update',{}) else '')
 r['present']=[str(x/r['jar']) for x in locations if (x/r['jar']).exists()]
 if r['present']:
  try:
   with zipfile.ZipFile(r['present'][0]) as z:
    names=z.namelist()
    if 'fabric.mod.json' in names:
     m=json.loads(z.read('fabric.mod.json'),strict=False);r.update(modid=m.get('id'),version=m.get('version'),description=m.get('description',''),contacts=m.get('contact',{}))
     if not p.name.endswith('.toml'):r['name']=m.get('name',r['name']);r['source']=m.get('contact',{}).get('homepage','')
    langs={}
    for n in names:
     if re.match(r'assets/[^/]+/lang/en_us.json$',n):
      try:langs.update(json.loads(z.read(n)))
      except:pass
    r['lang']={k:v for k,v in langs.items() if k.startswith(('item.','block.','entity.','biome.','effect.','enchantment.')) and isinstance(v,str)}
    r['recipes']=[n for n in names if re.match(r'data/[^/]+/recipes/.+json$',n)]
    r['biomes']=[n for n in names if re.match(r'data/[^/]+/worldgen/biome/.+\.json$',n)]
    r['structures']=[n for n in names if re.match(r'data/[^/]+/worldgen/structure/.+\.json$',n)]
  except Exception as e:r['error']=str(e)
 rows.append(r)
ids=[r['update']['modrinth']['mod-id'] for r in rows if 'modrinth' in r['update']]
try:
 url='https://api.modrinth.com/v2/projects?ids='+urllib.parse.quote(json.dumps(ids))
 req=urllib.request.Request(url,headers={'User-Agent':'ForcedRelocationFeatureAudit/1.0'})
 projects=json.load(urllib.request.urlopen(req,timeout=45))
 mapping={p['id']:p for p in projects}
 for r in rows:
  p=mapping.get(r.get('update',{}).get('modrinth',{}).get('mod-id'))
  if p:r['project_description']=p['description'];r['project_body']=p['body'];r['source']='https://modrinth.com/mod/'+p['slug'];r['categories']=p['categories']
except Exception as e:print('WEB ERROR',e)
(out/'inventory-evidence.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False),'utf-8')
print('TOTAL',len(rows),'LOCAL JARS',sum(bool(r['present']) for r in rows),'WEB PROJECTS',sum('project_body' in r for r in rows))
