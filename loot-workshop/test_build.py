import json
from pathlib import Path
import shutil
import tempfile
import unittest
from build import ROOT, compile_pack, archive_bytes, table_path


class LootBuildTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / 'workshop'
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns('reports', '__pycache__'))

    def tearDown(self):
        self.temp.cleanup()

    def change_mapping(self, edit):
        path = self.root / 'mappings/ocean.json'
        values = json.loads(path.read_text())
        edit(values)
        path.write_text(json.dumps(values))

    def test_foundation_has_no_destination_overrides(self):
        files, report = compile_pack(self.root)
        self.assertEqual(len(files), 4)
        self.assertFalse(any(r['enabled'] for r in report))
        self.assertEqual(archive_bytes(files), archive_bytes(compile_pack(self.root)[0]))

    def test_preview_preserves_original_pools_and_adds_one(self):
        files, report = compile_pack(self.root, preview=True)
        for row in report:
            name = table_path(row['table'])
            original = json.loads((self.root / 'preserved-tables' / name).read_text())
            generated = json.loads(files[name])
            self.assertEqual(generated['pools'][:-1], original['pools'])
            self.assertEqual(generated['pools'][-1]['rolls'], 1)

    def test_unreviewed_activation_rejected(self):
        self.change_mapping(lambda rows: rows[0].update(enabled=True))
        with self.assertRaisesRegex(ValueError, 'Review other loot'):
            compile_pack(self.root)

    def test_reviewed_activation_emits_only_selected_target(self):
        self.change_mapping(lambda rows: rows[0].update(enabled=True, integration_reviewed=True))
        files, _ = compile_pack(self.root)
        self.assertIn(table_path('minecraft:chests/shipwreck_supply'), files)
        self.assertEqual(len(files), 5)

    def test_duplicate_target_rejected(self):
        self.change_mapping(lambda rows: rows.append(dict(rows[0])))
        with self.assertRaisesRegex(ValueError, 'Duplicate chest'):
            compile_pack(self.root)

    def test_tampered_baseline_rejected(self):
        path = next((self.root / 'preserved-tables').rglob('*.json'))
        path.write_bytes(path.read_bytes() + b' ')
        with self.assertRaisesRegex(ValueError, 'Snapshot changed'):
            compile_pack(self.root)

    def test_unreviewed_item_rejected(self):
        path = self.root / 'pools/ocean-jackpot.json'
        data = json.loads(path.read_text())
        data['entries'][0]['name'] = 'example:missing'
        path.write_text(json.dumps(data))
        with self.assertRaisesRegex(ValueError, 'missing from reviewed catalog'):
            compile_pack(self.root)


if __name__ == '__main__':
    unittest.main()
