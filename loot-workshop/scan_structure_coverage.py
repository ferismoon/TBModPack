"""Read-only structure/container inventory, including nested jars and data packs.

Reports potential resource variants rather than guessing Fabric pack precedence.
No gameplay files are changed. Python standard library only.
"""
import collections, gzip, io, json, re, struct, zipfile, hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CLIENT = Path('I:/PrismLauncher/instances/MS Test Client/minecraft')
OUT = ROOT / 'reports/structure-scan'
OUT.mkdir(parents=True, exist_ok=True)
inventory, resources, errors, code = [], [], [], []

def walk(x):
    yield x
    if isinstance(x, dict):
        for v in x.values(): yield from walk(v)
    if isinstance(x, list):
        for v in x: yield from walk(v)

def nbt(raw):
    f = io.BytesIO(gzip.decompress(raw) if raw[:2] == b'\x1f\x8b' else raw)
    def num(fmt):
        return struct.unpack('>'+fmt, f.read(struct.calcsize('>'+fmt)))[0]
    def string(): return f.read(num('H')).decode('utf-8', 'replace')
    def value(t):
        if t in (1,2,3,4,5,6): return num({1:'b',2:'h',3:'i',4:'q',5:'f',6:'d'}[t])
        if t == 8: return string()
        if t == 9:
            subtype, length = num('B'), num('i')
            return [value(subtype) for _ in range(length)]
        if t == 10:
            result = {}
            while True:
                subtype = num('B')
                if subtype == 0: return result
                name = string()
                result[name] = value(subtype)
        if t in (7,11,12):
            length = num('i'); f.read(length * {7:1,11:4,12:8}[t]); return {'array_length':length}
        raise ValueError('Unknown NBT tag '+str(t))
    t = num('B'); string(); return value(t)

def constants(raw):
    if raw[:4] != b'\xca\xfe\xba\xbe': return []
    count = int.from_bytes(raw[8:10],'big'); p=10; i=1; result=[]
    sizes={3:4,4:4,5:8,6:8,7:2,8:2,9:4,10:4,11:4,12:4,15:3,16:2,17:4,18:4,19:2,20:2}
    while i<count:
        t=raw[p]; p+=1
        if t==1:
            n=int.from_bytes(raw[p:p+2],'big');p+=2
            result.append(raw[p:p+n].decode('utf-8','replace'));p+=n
        else:
            p+=sizes[t]
            if t in (5,6):i+=1
        i+=1
    return result

def resource(name, raw, source):
    m=re.fullmatch(r'data/([^/]+)/(worldgen/structure|worldgen/template_pool|worldgen/processor_list|structures|loot_tables)/(.+)\.(json|nbt)',name)
    if not m: return
    ns,kind,path,ext=m.groups()
    try:
        data=nbt(raw) if ext=='nbt' else json.loads(raw)
        if kind=='structures':
            palette=data.get('palette',[]) or (data.get('palettes') or [[]])[0]
            kept=[]
            for b in data.get('blocks',[]):
                s=b.get('state',-1)
                block=palette[s].get('Name','') if 0<=s<len(palette) else ''
                if b.get('nbt') or any(v in block for v in ('chest','barrel','shulker','dispenser','dropper')): kept.append(b)
            data={'palette':palette,'blocks':kept}
        row={'id':ns+':'+path,'kind':kind,'source':source,'path':name,'data':data,'hash':hashlib.sha256(raw).hexdigest()}
        resources.append(row)
    except Exception as e: errors.append({'source':source,'path':name,'error':str(e)})

def archive(path, source, layer):
    entry={'source':source,'layer':layer,'mod_id':None,'name':None,'resources':0,'java_candidates':0}
    inventory.append(entry)
    before=len(resources)
    try:
        with zipfile.ZipFile(path) as z:
            if 'fabric.mod.json' in z.namelist():
                try:
                    meta=json.loads(z.read('fabric.mod.json'),strict=False)
                    entry.update(mod_id=meta.get('id'),name=meta.get('name'),version=meta.get('version'))
                except Exception as e: errors.append({'source':source,'path':'fabric.mod.json','error':str(e)})
            for name in z.namelist():
                if name.endswith(('.jar','.zip')):
                    archive(io.BytesIO(z.read(name)),source+'!'+name,layer+' nested')
                elif name.startswith('data/'):
                    resource(name,z.read(name),source)
                # Java generation is recorded by the runtime diagnostics; parsing every
                # class file here is prohibitively expensive for a large client.
        entry['resources']=len(resources)-before
    except Exception as e: errors.append({'source':source,'error':str(e)})

def directory(path, layer, prefix=''):
    if not path.exists(): return
    before=len(resources)
    for p in path.rglob('*'):
        if p.is_file(): resource(prefix+p.relative_to(path).as_posix(),p.read_bytes(),str(path))
    inventory.append({'source':str(path),'layer':layer,'resources':len(resources)-before})

for index,jar in enumerate(sorted((CLIENT/'mods').glob('*.jar'))):
    archive(jar,str(jar),'installed mod')
    if index%100==0:print(f'Scanned {index+1} mod jars',flush=True)
for base, layer in [(CLIENT/'config/openloader/data','client OpenLoader'),(ROOT.parent/'config/openloader/data','workspace OpenLoader')]:
    for p in sorted(base.glob('*')):
        if p.is_dir(): directory(p,layer)
        elif p.suffix=='.zip':archive(p,str(p),layer)
for base in [CLIENT/'kubejs/data',ROOT.parent/'kubejs/data']: directory(base,'KubeJS data','data/')
for world in (CLIENT/'saves').glob('*'):
    if not world.is_dir():continue
    for p in (world/'datapacks').glob('*'):
        if p.is_dir():directory(p,'world datapack (enabled state not inferred)')
        elif p.suffix=='.zip':archive(p,str(p),'world datapack (enabled state not inferred)')
# Vanilla structures are represented by the runtime observations and existing route map.

groups=collections.defaultdict(list)
for r in resources:groups[(r['kind'],r['id'])].append(r)
templates={}; edges=collections.defaultdict(set); containers=[]
def ident(v):return v if ':' in v else 'minecraft:'+v
for (kind,id),variants in groups.items():
    node=kind+'|'+id
    for r in variants:
        data=r['data']
        if kind=='worldgen/structure':
            if isinstance(data.get('start_pool'),str):edges[node].add('worldgen/template_pool|'+ident(data['start_pool']))
        if kind=='worldgen/template_pool':
            if isinstance(data.get('fallback'),str) and data['fallback']!='minecraft:empty': edges[node].add('worldgen/template_pool|'+ident(data['fallback']))
            for v in walk(data):
                if not isinstance(v,dict):continue
                if isinstance(v.get('location'),str):edges[node].add('structures|'+ident(v['location']))
                if isinstance(v.get('processors'),str):edges[node].add('worldgen/processor_list|'+ident(v['processors']))
        if kind=='structures':
            palette=data.get('palette',[])
            if not palette and data.get('palettes'): palette=data['palettes'][0]
            for b in data.get('blocks',[]):
                state=b.get('state',-1); block=palette[state].get('Name','unknown') if 0<=state<len(palette) else 'unknown'
                tag=b.get('nbt',{})
                if block=='minecraft:jigsaw' and tag.get('pool') and tag['pool']!='minecraft:empty':edges[node].add('worldgen/template_pool|'+ident(tag['pool']))
                loot=tag.get('LootTable')
                if loot or any(s in block for s in ('chest','barrel','shulker','dispenser','dropper')):
                    containers.append({'template':id,'source':r['source'],'block':block,'pos':b.get('pos'),
                        'loot_table':loot,'prefilled_items':len(tag.get('Items',[])), 'nbt_keys':sorted(tag)})
        if kind=='loot_tables':
            for v in walk(data):
                if isinstance(v,dict) and v.get('type') in ('minecraft:loot_table','loot_table') and isinstance(v.get('name'),str):edges[node].add('loot_tables|'+ident(v['name']))

bytemplate=collections.defaultdict(list)
for c in containers:bytemplate[c['template']].append(c)
structure_rows=[]; linked=set(); unresolved=[]
for kind,id in sorted(groups):
    if kind!='worldgen/structure':continue
    todo=[kind+'|'+id]; seen=set(); found=set(); pieces=set()
    while todo:
        n=todo.pop()
        if n in seen:continue
        seen.add(n); k,key=n.split('|',1)
        if (k,key) not in groups:
            unresolved.append({'structure':id,'reference':n});continue
        if k=='structures':
            pieces.add(key);linked.add(key)
            found.update(c['loot_table'] for c in bytemplate[key] if c['loot_table'])
        todo.extend(edges[n]-seen)
    structure_rows.append({'structure':id,'types':sorted({r['data'].get('type','unknown') for r in groups[(kind,id)]}),
        'sources':sorted({r['source'] for r in groups[(kind,id)]}),'templates':sorted(pieces),'loot_tables':sorted(found),
        'status':'template graph resolved' if pieces else 'no template graph: Java/custom generation review required'})

runtime=[]
log=CLIENT/'logs/latest.log'
for line in log.read_text(errors='replace').splitlines():
    m=re.search(r'\[LootDiag INTERACT\].*?block=(\S+).*?structures=\[(.*?)\].*?LootTable="([^"]+)"',line)
    if m:runtime.append({'block':m[1],'structure_candidates':m[2].split(', ') if m[2] else [],'table':m[3]})
config=json.loads((ROOT.parent/'config/forced-relocation-rewards.json').read_text())
routes=config['routes']; plush=set(config['plushies']['targets'])
root_ids={c['loot_table'] for c in containers if c['loot_table']}|{r['table'] for r in runtime}
coverage=[]
for id in sorted(root_ids):
    coverage.append({'table':id,'profile':routes.get(id),'plushies':id in plush,
        'definition_found':('loot_tables',id) in groups,
        'templates':sorted({c['template'] for c in containers if c['loot_table']==id}),
        'structures':sorted({r['structure'] for r in structure_rows if id in r['loot_tables']}),
        'runtime_observed':any(r['table']==id for r in runtime)})
missing=[r for r in coverage if not r['profile']]
duplicates=[{'kind':k,'id':id,'sources':sorted({r['source'] for r in rows})} for (k,id),rows in groups.items() if len({r['hash'] for r in rows})>1]
report={'inventory':inventory,'structures':structure_rows,'containers':containers,'coverage':coverage,
        'unresolved':unresolved,'java_candidates':code,'variant_conflicts':duplicates,'errors':errors,
        'runtime':runtime,'unlinked_templates':sorted(set(bytemplate)-linked),
        'nested_loot_references':{k:sorted(v) for k,v in edges.items() if k.startswith('loot_tables|')}}
(OUT/'evidence.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
lines=['# Installed structure and loot coverage scan','',
    f'Installed mod jars scanned: {sum(i["layer"]=="installed mod" for i in inventory)}. Archive/directory sources including nested dependencies and packs: {len(inventory)}.',
    f'Structure definitions: {len(structure_rows)}. Template containers (including resource variants): {len(containers)}. Unique container loot roots: {len(coverage)}.',
    f'Resource-mapped roots: {len(coverage)-len(missing)}. Unmapped roots requiring review: {len(missing)}. Parse/read errors: {len(errors)}.', '',
    'This is a potential-resource inventory, not a claim that every bundled or world datapack is enabled. Conflicting definitions are retained. Runtime observations confirm use only for the sampled containers. Java-generated structures, processor-assigned loot, function-generated containers, and unresolved references require review; absence of a static link is not proof of no loot.',
    'Missing mappings are review candidates, not automatic rewards: deliberately empty, decorative and progression-special tables need individual decisions.', '',
    '## Missing reward mappings','', '| Loot table | Templates | Linked structures | Runtime observed | Plushies |','|---|---:|---:|---|---|']
for r in missing:lines.append(f'| `{r["table"]}` | {len(r["templates"])} | {len(r["structures"])} | {r["runtime_observed"]} | {r["plushies"]} |')
lines+=['','## Full structure list','','| Structure | Template pieces | Loot roots | Status |','|---|---:|---:|---|']
for r in structure_rows:lines.append(f'| `{r["structure"]}` | {len(r["templates"])} | {len(r["loot_tables"])} | {r["status"]} |')
lines+=['','## Source inventory','','Every source below was attempted, including mods without structure resources. Counts can include nested resources. See evidence.json for errors, container details, graph links, Java candidates, resource conflicts and unlinked templates.','', '| Source | Kind | Resources |','|---|---|---:|']
for r in inventory:lines.append(f'| {r["source"]} | {r["layer"]} | {r["resources"]} |')
(OUT/'REPORT.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print('\n'.join(lines[2:5]))
