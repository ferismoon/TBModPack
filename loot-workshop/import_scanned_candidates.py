"""Import confirmed structure-linked/runtime-observed loot roots into routes."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
scan=json.loads((ROOT/'reports/structure-scan/evidence.json').read_text())
path=ROOT/'structure-routes.json'; data=json.loads(path.read_text())
excluded={r['target'] for r in data.get('excluded',[])}
routes={r['target']:r for r in data['routes']}
routes={k:v for k,v in routes.items() if not k.endswith('/')}
def profile(table):
    p=table.split(':',1)[1].lower()
    if any(x in p for x in ('nether','bastion','fortress','crimson','warped','deepdark','ancient_temple')): return 'nether'
    if any(x in p for x in ('end','endcity','end_city','ender')): return 'end'
    if any(x in p for x in ('ocean','shipwreck','underwater','ruin','fisher','aquatic')): return 'water'
    if any(x in p for x in ('temple','stronghold','mansion','tower','dungeon','lich','outpost')): return 'medium'
    return 'village'
added=[]
for row in scan['coverage']:
    table=row['table']
    if table.endswith('/'): continue
    if row['profile'] or table in excluded or not (row['structures'] or row['runtime_observed']): continue
    low=table.lower()
    if any(x in low for x in ('/empty','/trash','/decor','/junk')): continue
    routes[table]={'target':table,'profile':profile(table)}; added.append(table)
data['routes']=sorted(routes.values(),key=lambda r:r['target'])
path.write_text(json.dumps(data,indent=2)+'\n')
print(f'Added {len(added)} safe scanned candidates; route total {len(data["routes"])}')
