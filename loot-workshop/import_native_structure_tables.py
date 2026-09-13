"""Add native chest tables from structure providers to the workshop route map."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
evidence = json.loads((ROOT / 'mod-coverage-audit' / 'evidence.json').read_text())
routes_path = ROOT / 'structure-routes.json'
routes_data = json.loads(routes_path.read_text())
excluded_ids = {row['target'] for row in routes_data.get('excluded', [])}
unique = []
seen = set()
for row in routes_data['routes']:
    if row['target'] in excluded_ids or row['target'] in seen:
        continue
    seen.add(row['target'])
    unique.append(row)
routes_data['routes'] = unique
existing = {row['target'] for row in routes_data['routes']}
existing.update(excluded_ids)

providers = ('repurposed_structures:', 'yungs', 'moogs_structures:', 'structory:', 'structory_towers:',
             'betterdungeons:', 'betterdeserttemples:', 'betterfortresses:', 'betterjungletemples:',
             'betterstrongholds:', 'betterwitchhuts:', 'nova_structures:', 'mns:', 'mmv:', 'mvs:')

def profile(table_id):
    p = table_id.split(':', 1)[1].lower()
    if any(x in p for x in ('nether', 'bastion', 'fortress', 'crimson', 'warped')):
        return 'nether'
    if any(x in p for x in ('end', 'endcity', 'end_city')):
        return 'end'
    if any(x in p for x in ('monument', 'ocean', 'shipwreck', 'underwater', 'ruin')):
        return 'water'
    if any(x in p for x in ('temple', 'stronghold', 'mansion', 'tower', 'dungeon')):
        return 'medium'
    return 'village'

added = []
for table in evidence['tables']:
    table_id = table['id']
    if table['layer'] != 'native' or 'chests/' not in table_id or not table_id.startswith(providers):
        continue
    if table_id in existing:
        continue
    routes_data['routes'].append({'target': table_id, 'profile': profile(table_id)})
    existing.add(table_id)
    added.append(table_id)

routes_data['routes'].sort(key=lambda row: row['target'])
routes_path.write_text(json.dumps(routes_data, indent=2) + '\n', encoding='utf-8')
print(f'Added {len(added)} native provider chest tables; route total {len(routes_data["routes"])}')
for table_id in added:
    print(table_id)
