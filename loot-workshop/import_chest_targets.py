"""Explicitly refresh chest targets from installed resources; review before building."""
import json
from pathlib import Path
import zipfile
from build import ROOT, encoded

resources = {}
archives = sorted(Path('I:/PrismLauncher/instances/MS Test Client/minecraft/mods').glob('*.jar'))
archives.insert(0, Path('C:/Users/feris/.gradle/caches/fabric-loom/1.20.1/minecraft-client.jar'))
for archive in archives:
    with zipfile.ZipFile(archive) as z:
        for name in z.namelist():
            parts = name.split('/')
            if len(parts) < 5 or parts[0] != 'data' or parts[2] != 'loot_tables' or not name.endswith('.json'):
                continue
            try:
                resources[parts[1] + ':' + '/'.join(parts[3:])[:-5]] = json.loads(z.read(name))
            except (ValueError, UnicodeError):
                pass
for path in (ROOT.parent / 'kubejs/data').rglob('*.json'):
    parts = path.relative_to(ROOT.parent / 'kubejs/data').parts
    if len(parts) > 2 and parts[1] == 'loot_tables':
        resources[parts[0] + ':' + '/'.join(parts[2:])[:-5]] = json.loads(path.read_text())

referenced = set()
def visit(value):
    if isinstance(value, dict):
        if value.get('type') == 'minecraft:loot_table' and isinstance(value.get('name'), str):
            referenced.add(value['name'])
        for child in value.values(): visit(child)
    elif isinstance(value, list):
        for child in value: visit(child)
for data in resources.values(): visit(data)
targets = sorted(key for key, data in resources.items()
    if (data.get('type') == 'minecraft:chest' or ':chests/' in key)
    and key not in referenced and not key.startswith(('beachparty:', 'forced_relocation:', 'lootintegrations:'))
    and data.get('pools'))
(ROOT / 'player-plushies.json').write_bytes(encoded({
    'chance': 0.1,
    'items': [f'phomesteadplushies:homestead_player_{n}' for n in range(1, 28)] +
             ['phomesteadplushies:mushling_plushie', 'phomesteadplushies:mystical_elk_plushie', 'phomesteadplushies:fernling_plushie'],
    'targets': targets,
    'excluded_nested_tables': sorted(referenced),
    'note': 'Root chest tables only. Beachparty helper tables excluded to avoid a second roll through ocean injections.'
}))
print(f'Imported {len(targets)} root chest targets')
