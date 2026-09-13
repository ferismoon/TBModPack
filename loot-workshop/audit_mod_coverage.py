"""Read-only pack audit. Writes reference artifacts only; never changes gameplay files."""
import collections
import csv
import gzip
import hashlib
import io
import json
from pathlib import Path
import re
import struct
import zipfile

ROOT = Path(__file__).resolve().parent
PACK = ROOT.parent
CLIENT = Path('I:/PrismLauncher/instances/MS Test Client/minecraft')
OUT = ROOT / 'mod-coverage-audit'
OUT.mkdir(exist_ok=True)
mods, tables, modifiers, structures, code = {}, [], [], collections.defaultdict(list), []
errors = []
models = collections.defaultdict(set)
display = {}

def walk(value):
    yield value
    if isinstance(value, dict):
        for child in value.values(): yield from walk(child)
    elif isinstance(value, list):
        for child in value: yield from walk(child)

def utf8_constants(data):
    # Java constant pool: decode UTF8 entries rather than searching arbitrary bytes.
    if data[:4] != b'\xca\xfe\xba\xbe': return []
    count = int.from_bytes(data[8:10], 'big'); pos = 10; i = 1; out = []
    sizes = {3:4,4:4,5:8,6:8,7:2,8:2,9:4,10:4,11:4,12:4,15:3,16:2,17:4,18:4,19:2,20:2}
    while i < count:
        tag = data[pos]; pos += 1
        if tag == 1:
            size = int.from_bytes(data[pos:pos+2], 'big'); pos += 2
            out.append(data[pos:pos+size].decode('utf-8', errors='replace')); pos += size
        else:
            if tag not in sizes: break
            pos += sizes[tag]
            if tag in (5,6): i += 1
        i += 1
    return out

def resource(name, raw, source, owner, layer):
    if '/structures/' in name and name.endswith('.nbt'):
        try:
            if raw[:2] == b'\x1f\x8b': raw = gzip.decompress(raw)
            for match in re.finditer(b'\x08\x00\x09LootTable(..)', raw):
                n = int.from_bytes(match[1], 'big')
                target = raw[match.end():match.end()+n].decode('utf-8')
                structures[target].append(source + '!' + name)
        except Exception as e: errors.append(str(e))
        return
    model = re.fullmatch(r'assets/([^/]+)/models/item/(.+)\.json', name)
    if model: models[model[1]].add(model[1] + ':' + model[2])
    if not name.endswith('.json'): return
    try: data = json.loads(raw)
    except (ValueError, UnicodeError): return
    if name.endswith('/lang/en_us.json') and isinstance(data, dict): display.update(data)
    match = re.fullmatch(r'data/([^/]+)/loot_tables/(.+)\.json', name)
    if match:
        leaves = [v for v in walk(data) if isinstance(v, dict)]
        tables.append({'id':match[1]+':'+match[2], 'source':source, 'path':name, 'owner':owner, 'layer':layer,
            'type':data.get('type'), 'items':sorted({v['name'] for v in leaves if v.get('type') in ('minecraft:item','item') and isinstance(v.get('name'),str)}),
            'refs':sorted({v['name'] for v in leaves if v.get('type') in ('minecraft:loot_table','loot_table') and isinstance(v.get('name'),str)}), 'data':data})
    elif '/loot_modifiers/' in name:
        modifiers.append({'source':source,'path':name,'owner':owner,'layer':layer,'data':data})

def archive(path_or_bytes, source, layer='native', parent=None):
    with zipfile.ZipFile(path_or_bytes) as z:
        try:
            meta = json.loads(z.read('fabric.mod.json')) if 'fabric.mod.json' in z.namelist() else {}
        except (ValueError, UnicodeError):
            meta = {}
        owner = meta.get('id', parent or Path(source).stem)
        if owner not in mods:
            mods[owner] = {'name':meta.get('name',owner), 'version':meta.get('version','unknown'), 'source':source,'layer':layer}
        for name in z.namelist():
            if name.startswith('META-INF/jars/') and name.endswith('.jar'):
                archive(io.BytesIO(z.read(name)), source+'!'+name, layer, owner)
            elif name.startswith(('data/','assets/')) and name.endswith(('.json','.nbt')):
                resource(name,z.read(name),source,owner,layer)
            elif layer == 'native' and name.endswith('.class'):
                values = utf8_constants(z.read(name))
                targets = sorted({s for s in values if re.fullmatch(r'(?:[a-z0-9_.-]+:)?chests/[a-z0-9_/.-]+',s)})
                has_api = any('LootTableEvents' in s or 'LootTableLoadingCallback' in s or 'LootTableModification' in s for s in values)
                if targets or has_api:
                    code.append({'owner':owner,'source':source,'class':name,'targets':targets,'api_signal':has_api,
                        'item_constants': sorted({s for s in values if re.fullmatch(r'[a-z0-9_.-]+:[a-z0-9_/.-]+',s) and not s.startswith('minecraft:chests/')})})

for path in sorted((CLIENT/'mods').glob('*.jar')): archive(path, path.name)
for path in sorted((PACK/'config/openloader/data').glob('*.zip')): archive(path,path.name,'pack')
for path in sorted((PACK/'kubejs/data').rglob('*.json')):
    resource('data/'+path.relative_to(PACK/'kubejs/data').as_posix(),path.read_bytes(),str(path.relative_to(PACK)),'pack','pack')

def chest(t):
    p = t['id'].split(':',1)[1]
    return t['type']=='minecraft:chest' or t['id'] in structures or p.startswith('chests/') or '/chests/' in p

native_chests = [t for t in tables if t['layer']=='native' and chest(t)]
routes = json.loads((ROOT/'structure-routes.json').read_text())['routes']
profiles = json.loads((ROOT/'structure-rewards.json').read_text())
plush = json.loads((ROOT/'player-plushies.json').read_text())
retained = set(json.loads((ROOT/'global-modifier-routes.json').read_text())['entries'])
disabled = set(json.loads((ROOT/'perfect-plushies-import.json').read_text())['disabled_routes'])
workshop = collections.defaultdict(list)
for profile, info in profiles.items():
    for item in info['items']:
        workshop[item['item'].split(':')[0]].append({'profile':profile,**item,'targets':sum(r['profile']==profile for r in routes)})
for item in plush['items']: workshop[item.split(':')[0]].append({'profile':'plushies','item':item,'targets':len(plush['targets'])})
for path in (ROOT/'pools').glob('*.json'):
    data=json.loads(path.read_text())
    for item in data['entries']: workshop[item['name'].split(':')[0]].append({'profile':'ocean sample (shipwreck treasure)','item':item['name'],'targets':1})

modroutes = []
for row in modifiers:
    if row['path'].endswith('/global_loot_modifiers.json'): continue
    m=re.fullmatch(r'data/([^/]+)/loot_modifiers/(.+)\.json',row['path'])
    if not m: continue
    key=m[1]+':'+m[2]
    target=sorted({v['loot_table_id'] for v in walk(row['data']) if isinstance(v,dict) and isinstance(v.get('loot_table_id'),str)})
    modroutes.append({**row,'id':key,'targets':target,'state':'disabled by workshop' if key in disabled else 'listed by workshop' if key in retained else 'not listed by workshop / inspect loader'})

# Every namespace with item models is included, not just a hand-picked list of familiar mods.
inventory=[]
for ns, items in sorted(models.items()):
    own=[t for t in native_chests if t['owner']==ns or t['id'].startswith(ns+':')]
    appearances=[{'table':t['id'],'provider':t['owner'],'source':t['source'],'path':t['path'],'items':[i for i in t['items'] if i.startswith(ns+':')]} for t in native_chests if any(i.startswith(ns+':') for i in t['items'])]
    hooks=[c for c in code if c['owner']==ns]
    globals_=[r for r in modroutes if r['owner']==ns or any(ns+':' in str(v) for v in walk(r['data']))]
    status='No chest route found in scanned evidence; code/registry review still required'
    if appearances: status='Native chest-table item references found'
    if hooks: status+='; Java chest-hook evidence'
    if any(r['state']=='listed by workshop' for r in globals_): status+='; retained global modifier'
    if workshop[ns]: status+='; workshop rewards configured'
    if ns in ('perfectplushies','phomesteadplushies'): status='Central shared plushie pool; broken native API routes disabled'
    inventory.append({'namespace':ns,'name':mods.get(ns,{}).get('name',ns),'item_models':len(items),'native_tables':len(own),
        'native_item_routes':len(appearances),'java_hook_classes':len(hooks),'workshop_entries':len(workshop[ns]),'status':status,
        'appearances':appearances,'own_tables':[{'id':t['id'],'refs':t['refs'],'source':t['source']} for t in own], 'java':hooks,'global_modifiers':globals_,'workshop':workshop[ns]})

data={'scope':'Current MS Test Client jars plus MCWork loot outputs; static evidence, not runtime probabilities',
 'mods':mods,'inventory':inventory,'tables':tables,'global_modifiers':modroutes,'structure_references':structures,'errors':errors}
(OUT/'evidence.json').write_text(json.dumps(data,indent=2),'utf-8')
with (OUT/'mod-coverage.csv').open('w',newline='',encoding='utf-8-sig') as f:
    fields=['namespace','name','item_models','native_tables','native_item_routes','java_hook_classes','workshop_entries','status']
    w=csv.DictWriter(f,fields,extrasaction='ignore');w.writeheader();w.writerows(inventory)
lines=['# Mod loot coverage audit','', 'Read the summary and proposals first. This reference covers every installed item-model namespace; libraries and visual-only namespaces can appear and do not automatically need loot.',
 '', 'Evidence is structural: a model is not proof of a registered item, an item in a helper table is not proof of an active chest route, and Java constants are candidates until the code path is inspected. No absence is reported as proof that a mod never adds loot.',
 '', '| Namespace | Native item-table references | Java hook classes | Workshop entries |', '| --- | ---: | ---: | ---: |']
for row in inventory: lines.append(f"| {row['namespace']} | {row['native_item_routes']} | {row['java_hook_classes']} | {row['workshop_entries']} |")
for row in inventory:
    lines += ['', '## '+row['name']+' (`'+row['namespace']+'`)', '', row['status']+'.','']
    for a in row['appearances']:
        lines.append('- Table `'+a['table']+'` ('+a['source']+'): '+', '.join('`'+i+'`' for i in a['items']))
    for h in row['java']:
        lines.append('- Java candidate `'+h['source']+'!'+h['class']+'`: '+(', '.join('`'+t+'`' for t in h['targets']) or 'loot callback API found; target IDs require code inspection'))
    for g in row['global_modifiers']:
        lines.append('- Global modifier `'+g['id']+'`: '+g['state']+'; targets '+(', '.join(g['targets']) or 'non-table condition / inspect JSON')+'.')
    if row['workshop']:
        lines.append('- Workshop: '+', '.join(sorted({w['profile'] for w in row['workshop']}))+'.')
(OUT/'MOD-BY-MOD.md').write_text('\n'.join(lines)+'\n','utf-8')
print(f'Audited {len(mods)} modules; {len(inventory)} item namespaces; {len(native_chests)} chest-like definitions; {len(code)} Java candidate classes; {len(modroutes)} global modifiers; errors={len(errors)}')
