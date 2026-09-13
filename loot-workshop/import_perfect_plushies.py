"""Import installed plushie IDs and preserve non-plushie global modifier routes."""
import io
import json
from pathlib import Path
import zipfile
from build import ROOT, encoded, read

mods = Path('I:/PrismLauncher/instances/MS Test Client/minecraft/mods')
entries = []
def scan(z):
    for name in z.namelist():
        if name == 'data/forge/loot_modifiers/global_loot_modifiers.json':
            data = json.loads(z.read(name))
            entries.extend(data.get('entries', []))
        elif name.startswith('META-INF/jars/') and name.endswith('.jar'):
            with zipfile.ZipFile(io.BytesIO(z.read(name))) as nested: scan(nested)
for path in sorted(mods.glob('*.jar')):
    with zipfile.ZipFile(path) as z: scan(z)
with zipfile.ZipFile(mods / 'perfectplushies-fabric-1.20.1-1.13.3.jar') as z:
    items = sorted('perfectplushies:' + n.rsplit('/', 1)[1][:-5]
        for n in z.namelist() if n.startswith('assets/perfectplushies/models/item/') and n.endswith('.json'))
    items = [item for item in items if 'data/perfectplushies/loot_tables/blocks/' + item.split(':')[1] + '.json' in z.namelist()]
config = read(ROOT / 'player-plushies.json')
config['items'] = list(dict.fromkeys(config['items'] + items))
(ROOT / 'player-plushies.json').write_bytes(encoded(config))
removed = sorted(set(e for e in entries if e.startswith('perfectplushieapi:')))
retained = list(dict.fromkeys(e for e in entries if not e.startswith('perfectplushieapi:')))
(ROOT / 'global-modifier-routes.json').write_bytes(encoded({'replace': True, 'entries': retained}))
(ROOT / 'perfect-plushies-import.json').write_bytes(encoded({'items': items, 'disabled_routes': removed, 'retained_routes': retained}))
print(f'Imported {len(items)} plushies; disabled {len(removed)} broken routes; retained {len(retained)} other routes')
