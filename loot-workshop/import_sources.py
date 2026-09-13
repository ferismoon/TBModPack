"""Explicitly import reviewed ocean baselines; rerun only when reviewing a pack update."""
import argparse
import hashlib
import json
from pathlib import Path
import zipfile
from build import ROOT, encoded, table_path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--minecraft-jar', type=Path, required=True)
    parser.add_argument('--moogs-jar', type=Path, required=True)
    parser.add_argument('--beachparty-jar', type=Path, required=True)
    args = parser.parse_args()
    mappings = json.loads((ROOT / 'mappings/ocean.json').read_text('utf-8'))
    catalog = {'minecraft': '1.20.1', 'items': {}, 'tables': {}}
    for mapping in mappings:
        target = mapping['target']
        source = args.minecraft_jar if target.startswith('minecraft:') else args.moogs_jar
        resource = table_path(target)
        with zipfile.ZipFile(source) as archive:
            data = archive.read(resource)
            json.loads(data)
        destination = ROOT / 'preserved-tables' / resource
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(data)
        catalog['tables'][target] = {'archive': source.name, 'archive_sha256': hashlib.sha256(source.read_bytes()).hexdigest(), 'resource': resource, 'sha256': hashlib.sha256(data).hexdigest()}
    for pool in (ROOT / 'pools').glob('*.json'):
        for entry in json.loads(pool.read_text('utf-8'))['entries']:
            item = entry['name']
            namespace, name = item.split(':')
            source = args.minecraft_jar if namespace == 'minecraft' else args.beachparty_jar
            model = f'assets/{namespace}/models/item/{name}.json'
            with zipfile.ZipFile(source) as archive:
                archive.getinfo(model)
            catalog['items'][item] = {'archive': source.name, 'model': model, 'evidence': 'Installed item model; runtime registry validation still required'}
    (ROOT / 'catalog.json').write_bytes(encoded(catalog))
    print(f'Imported {len(catalog["tables"])} snapshots and verified {len(catalog["items"])} item models.')


if __name__ == '__main__':
    main()
