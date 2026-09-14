"""Add chest roots observed in the diagnostic session, including vanilla roots."""
import json
from pathlib import Path
root = Path(__file__).resolve().parent
path = root / 'structure-routes.json'
data = json.loads(path.read_text())
routes = {r['target']: r for r in data['routes']}
evidence = json.loads((root/'mod-coverage-audit/evidence.json').read_text())
for t in evidence['tables']:
    id = t['id']
    profile = None
    if id.startswith(('minecraft:chests/village/', 'villagersplus:chests/village/')): profile = 'village'
    if id.startswith('minecraft:chests/shipwreck_'): profile = 'water'
    if id.startswith('minecraft:chests/bastion_'): profile = 'nether'
    if id in ('incendium:pipeline/common','incendium:steam/rare','incendium:reactor/treasure'): profile = 'nether'
    if profile: routes[id] = {'target':id,'profile':profile}
# These observed tables are real even when absent from the static vanilla jar scan.
for id, profile in [('minecraft:chests/village/village_plains_house','village'),
                    ('minecraft:chests/village/village_cartographer','village'),
                    ('minecraft:chests/bastion_bridge','nether'),('minecraft:chests/bastion_other','nether'),
                    ('minecraft:chests/shipwreck_map','water'),('minecraft:chests/shipwreck_supply','water')]:
    routes[id] = {'target':id,'profile':profile}
routes.pop('mvs:empty', None)
data['routes'] = sorted(routes.values(), key=lambda r:r['target'])
path.write_text(json.dumps(data,indent=2)+'\n')
