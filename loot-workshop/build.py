"""Build the Minecraft 1.20.1 loot datapack; standard-library Python 3.11+."""
import argparse
import hashlib
import io
import json
from pathlib import Path
import re
import sys
import zipfile

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT.parent / 'config/openloader/data/forced-relocation-loot.zip'
ID = re.compile(r'^[a-z0-9_.-]+:[a-z0-9_./-]+$')


def require(ok, message):
    if not ok:
        raise ValueError(message)


def identifier(value):
    require(isinstance(value, str) and ID.fullmatch(value), f'Invalid resource ID: {value!r}')
    require(all(p not in ('', '.', '..') for p in value.split(':')[1].split('/')), f'Unsafe path: {value}')
    return value


def read(path):
    def unique(pairs):
        result = {}
        for k, v in pairs:
            require(k not in result, f'Duplicate key {k} in {path}')
            result[k] = v
        return result
    return json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=unique)


def encoded(value):
    return (json.dumps(value, indent=2, ensure_ascii=False) + '\n').encode('utf-8')


def table_path(resource):
    namespace, path = identifier(resource).split(':')
    return f'data/{namespace}/loot_tables/{path}.json'


def compile_pack(root=ROOT, preview=False):
    settings = read(root / 'settings.json')
    require(settings['minecraft'] == '1.20.1' and settings['pack_format'] == 15, 'This builder targets Minecraft 1.20.1 / pack format 15')
    catalog = read(root / 'catalog.json')
    legacy = read(root / 'legacy-migrations.json')
    require(isinstance(legacy.get('migrations'), list) and legacy['migrations'], 'Legacy migration record is empty')
    for migration in legacy['migrations']:
        require(isinstance(migration.get('name'), str) and migration['name'], 'Legacy migration missing name')
        require(isinstance(migration.get('targets'), list) and migration['targets'], f'Legacy migration has no targets: {migration.get("name")}')
        for target in migration['targets']:
            require(isinstance(target, str) and target, f'Legacy migration has invalid target: {migration["name"]}')
    require(any('rubber rings' in item for item in legacy.get('excluded', [])), 'Legacy rubber-ring exclusion is missing')
    items = set(catalog['items'])
    known_tables = set(catalog['tables'])
    tables, profiles, report = {}, {}, []
    for path in sorted((root / 'pools').glob('*.json')):
        pool = read(path)
        resource = identifier(pool['id'])
        require(resource.startswith('forced_relocation:shared/'), f'Pool must use forced_relocation:shared/: {resource}')
        require(resource not in tables, f'Duplicate pool {resource}')
        entries = pool['entries']
        require(bool(entries), f'Empty pool {resource}')
        for entry in entries:
            require(entry.get('type') == 'minecraft:item', f'Only item entries supported in shared pools: {resource}')
            item = identifier(entry['name'])
            require(item in items, f'Item missing from reviewed catalog: {item}')
            require(type(entry.get('weight', 1)) is int and entry.get('weight', 1) > 0, f'Invalid weight: {item}')
            require(set(entry) <= {'type', 'name', 'weight'}, f'Unsupported entry fields: {item}; add explicit validation before extending schema')
        tables[resource] = {'type': 'minecraft:chest', 'pools': [{'rolls': 1, 'entries': entries}]}
    for path in sorted((root / 'profiles').glob('*.json')):
        profile = read(path)
        name = profile['id']
        require(name not in profiles, f'Duplicate profile {name}')
        chance = profile['chance']
        require(type(chance) in (int, float) and 0 <= chance <= 1, f'Invalid chance in {name}')
        require(bool(profile['choices']), f'No choices in {name}')
        entries = []
        for choice in profile['choices']:
            require(choice['pool'] in tables, f'Unknown shared pool {choice["pool"]}')
            require(type(choice['weight']) is int and choice['weight'] > 0, f'Invalid choice weight in {name}')
            entries.append({'type': 'minecraft:loot_table', 'name': choice['pool'], 'weight': choice['weight']})
        profiles[name] = {'rolls': 1, 'conditions': [{'condition': 'minecraft:random_chance', 'chance': chance}], 'entries': entries}
    files = {'pack.mcmeta': encoded({'pack': {'pack_format': 15, 'description': settings['description']}})}
    for resource, data in sorted(tables.items()):
        files[table_path(resource)] = encoded(data)
    used = set()
    for mapping in read(root / 'mappings/ocean.json'):
        target = identifier(mapping['target'])
        require(target not in used, f'Duplicate chest mapping: {target}')
        used.add(target)
        require(target in known_tables, f'Unreviewed target {target}')
        require(type(mapping['enabled']) is bool, f'enabled must be boolean: {target}')
        require(mapping['profile'] in profiles, f'Unknown profile for {target}')
        # An explicit review gate prevents accidental activation of overlapping layers.
        require(not mapping['enabled'] or mapping['integration_reviewed'] is True, f'Review other loot injections before enabling {target}')
        snapshot = root / 'preserved-tables' / table_path(target)
        require(snapshot.is_file(), f'Missing preserved table: {target}')
        expected = catalog['tables'][target]['sha256']
        require(hashlib.sha256(snapshot.read_bytes()).hexdigest() == expected, f'Snapshot changed: {target}; review and update catalog hash deliberately')
        original = read(snapshot)
        require(isinstance(original.get('pools'), list), f'Unsupported source table: {target}')
        generated = dict(original)
        generated['pools'] = original['pools'] + [profiles[mapping['profile']]]
        if mapping.get('debug_marker', False):
            marker_name = mapping.get('debug_marker_name', 'Shipwreck Loot')
            generated['pools'].append({'rolls': 1, 'entries': [{'type': 'minecraft:item', 'name': 'minecraft:zombie_head', 'functions': [{'function': 'minecraft:set_name', 'name': {'text': marker_name, 'color': 'gold', 'italic': False}}]}]})
        if mapping.get('debug_plushies', False):
            generated['pools'].append({'rolls': 1, 'entries': [{'type': 'minecraft:item', 'name': f'phomesteadplushies:homestead_player_{number}'} for number in range(1, 28)]})
        if mapping['enabled'] or preview:
            files[table_path(target)] = encoded(generated)
        report.append({'table': target, 'profile': mapping['profile'], 'enabled': mapping['enabled'], 'integration_reviewed': mapping['integration_reviewed'], 'original_pools': len(original['pools']), 'generated_pools': len(generated['pools']), 'chance': profiles[mapping['profile']]['conditions'][0]['chance'], 'review_notes': mapping['review_notes']})
    return files, report


def archive_bytes(files):
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
        for name, data in sorted(files.items()):
            entry = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            entry.compress_type = zipfile.ZIP_DEFLATED
            entry.external_attr = 0o644 << 16
            archive.writestr(entry, data)
    return stream.getvalue()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Validate sources and compare committed output without writing')
    parser.add_argument('--preview', action='store_true', help='Generate every mapping into ignored reports only')
    args = parser.parse_args()
    require(not (args.check and args.preview), 'Choose --check or --preview')
    files, report = compile_pack(preview=args.preview)
    payload = archive_bytes(files)
    destination = ROOT / 'reports/preview.zip' if args.preview else OUTPUT
    if args.check:
        require(destination.is_file() and destination.read_bytes() == payload, 'Generated datapack is stale; run build.py')
    else:
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(payload)
        reports = ROOT / 'reports'
        reports.mkdir(exist_ok=True)
        (reports / ('preview.json' if args.preview else 'build.json')).write_bytes(encoded(report))
    print(f'{"Checked" if args.check else "Generated"} {destination}: {len(files)} files; {sum(r["enabled"] for r in report)} enabled mappings; {len(report)} reviewed targets.')


if __name__ == '__main__':
    try:
        main()
    except (ValueError, KeyError, OSError) as error:
        print(f'Loot build failed: {error}', file=sys.stderr)
        sys.exit(1)
