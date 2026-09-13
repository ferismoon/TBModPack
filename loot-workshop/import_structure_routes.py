"""Refresh compatibility evidence from installed jars and archived LI add-ons."""
import json
import re
import zipfile
from collections import Counter
from pathlib import Path
from build import ROOT, encoded

mods = Path('I:/PrismLauncher/instances/MS Test Client/minecraft/mods')
tables, models = {}, set()
for path in sorted(mods.glob('*.jar')):
    with zipfile.ZipFile(path) as z:
        for name in z.namelist():
            m = re.fullmatch(r'data/([^/]+)/loot_tables/(.+)\.json', name)
            if m:
                try: tables[m[1] + ':' + m[2]] = {'data': json.loads(z.read(name)), 'source': path.name}
                except ValueError: pass
            m = re.fullmatch(r'assets/([^/]+)/models/item/(.+)\.json', name)
            if m: models.add(m[1] + ':' + m[2])
old = {}
for path in sorted(Path('I:/MC SERVER/mods').glob('lootintegrations_*.jar')):
    with zipfile.ZipFile(path) as z:
        for name in z.namelist():
            if not name.startswith('data/lootintegrations/loot/') or not name.endswith('.json'): continue
            data = json.loads(z.read(name))
            for target in data.get('integrated_loot_tables', {}):
                old.setdefault(target, []).append({'profile': data['loot_table'].rsplit('/', 1)[1], 'source': path.name + '/' + name})
namespaces = {'ctov','mvs','mes','mns','mss','mmv','mtr','structory','structory_towers','nova_structures',
 'betterdeserttemples','betterdungeons','betterfortresses','betterjungletemples','bettermineshafts',
 'betteroceanmonuments','betterstrongholds','betterwitchhuts'}
namespaces.update(t.split(':')[0] for t in old if t in tables)
refs = {}
def visit(value, found):
    if isinstance(value, dict):
        if value.get('type') == 'minecraft:loot_table': found.add(value.get('name'))
        for child in value.values(): visit(child, found)
    elif isinstance(value, list):
        for child in value: visit(child, found)
for target, row in tables.items():
    refs[target] = set()
    visit(row['data'], refs[target])
nested = set().union(*refs.values())
routes, skipped = [], []
for target, row in sorted(tables.items()):
    namespace = target.split(':')[0]
    if namespace not in namespaces: continue
    data = row['data']
    if target not in old and data.get('type') != 'minecraft:chest' and '/chests/' not in target and ':chests/' not in target: continue
    if target in nested or not data.get('pools'):
        skipped.append({'target': target, 'reason': 'Nested helper or empty table'}); continue
    profile = old.get(target, [{'profile': 'easy'}])[0]['profile']
    if namespace == 'mes' or 'end_' in target or ':end/' in target: profile = 'end'
    elif namespace in {'mns','betterfortresses'} or 'nether' in target: profile = 'nether'
    elif any(x in target for x in ['ocean', 'shipwreck', 'underwater']): profile = 'water'
    elif namespace in {'ctov','mmv'} or 'village' in target: profile = 'village'
    elif target not in old and any(x in target for x in ['treasure','boss','rare','special']): profile = 'hard'
    routes.append({'target': target, 'profile': profile, 'source': row['source'], 'legacy': old.get(target, []), 'basis': 'legacy mapping with dimension/theme correction' if target in old else 'current table theme'})
missing = [{'target': target, 'legacy': evidence} for target, evidence in sorted(old.items()) if target not in tables]
(ROOT / 'structure-routes.json').write_bytes(encoded({'routes': routes, 'missing_legacy_targets': missing, 'excluded': skipped}))
(ROOT / 'structure-item-evidence.json').write_bytes(encoded(sorted(models)))
print(f'{len(routes)} active targets, {len(missing)} missing legacy targets, {len(skipped)} nested/empty exclusions')
print(dict(Counter(row['profile'] for row in routes)))
print(dict(Counter(row['target'].split(':')[0] for row in routes)))
