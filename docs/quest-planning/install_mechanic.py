"""Install only the staged Mechanic files and update Packwiz metadata."""
import hashlib,json,re,shutil,tomllib
from pathlib import Path
ROOT=Path('I:/McWork');OUT=ROOT/'docs/quest-planning/mechanic';STAGE=OUT/'staged'
manifest=json.loads((OUT/'manifest.json').read_text('utf-8'));paths=manifest['files']
grouprel='config/ftbquests/quests/chapter_groups.snbt'
roots={'pack':ROOT,'server':Path('I:/MC SERVER'),'client':Path('I:/PrismLauncher/instances/Forced Relocation/minecraft')}
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
preserved={}
for name,base in roots.items():
 current={p:sha(p) for p in (base/'config/ftbquests/quests').rglob('*.snbt') if p.relative_to(base).as_posix() not in paths+[grouprel]}
 group=base/grouprel;text=group.read_text('utf-8')
 backup=OUT/'backups'/name;backup.mkdir(parents=True,exist_ok=True)
 if not (backup/'chapter_groups.snbt').exists():shutil.copy2(group,backup/'chapter_groups.snbt')
 if manifest['group_id'] not in text:
  anchor=r'(\{\s*id:\s*"72F807709569B28F"[^{}]*\})'
  entry='\n\t\t{ id: "'+manifest['group_id']+'", title: "The Mechanic" }'
  text,n=re.subn(anchor,lambda m:m[1]+entry,text,count=1)
  assert n==1,'Expected existing New Beginnings group'
  group.write_text(text,'utf-8',newline='\n')
 for path in paths:
  source=STAGE/path;dest=base/path
  if dest.exists() and sha(dest)!=sha(source):
   save=backup/path;save.parent.mkdir(parents=True,exist_ok=True)
   if not save.exists():shutil.copy2(dest,save)
  dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(source,dest)
  assert sha(source)==sha(dest)
 for path,digest in current.items():assert sha(path)==digest,'Existing quest changed: '+str(path)
 preserved[name]=len(current)
changelog=ROOT/'docs/changelog.html';text=changelog.read_text('utf-8')
if 'quest-mechanic' not in text:
 text=text.replace('  <main>','  <main>\n    <section aria-labelledby="quest-mechanic">\n      <h2 id="quest-mechanic">In development — The Mechanic</h2>\n      <p>Four open chapters cover a first workshop, production lines, movement and delivery, and specialist machinery. Each of the 44 quests has one task, a useful item reward, and a short description.</p>\n      <p>Optional practice uses Create advancements where available; flexible projects use player confirmations. Existing chapters are preserved. In-game review is still needed.</p>\n    </section>',1)
 changelog.write_text(text,'utf-8',newline='\n')
home=ROOT/'index.html';text=home.read_text('utf-8')
text=text.replace('A Foothold introduces three independent settlement projects, with optional guidance and a commemorative reward.','A Foothold introduces three independent settlement projects. The Mechanic adds four open chapters with short guidance and item rewards for every task.')
home.write_text(text,'utf-8',newline='\n')
index=ROOT/'index.toml';text=index.read_text('utf-8')
for path in [grouprel]+paths:
 digest=sha(ROOT/path)
 pattern=r'(file = "'+re.escape(path)+r'"\s*\nhash = ")[^"]+(")'
 text,n=re.subn(pattern,lambda m:m[1]+digest+m[2],text)
 assert n<=1
 if not n:text+='\n[[files]]\nfile = "'+path+'"\nhash = "'+digest+'"\n'
index.write_text(text,'utf-8',newline='\n')
entries=tomllib.loads(text)['files'];assert len(entries)==len({e['file'] for e in entries})
for path in [grouprel]+paths:assert next(e['hash'] for e in entries if e['file']==path)==sha(ROOT/path)
pack=ROOT/'pack.toml';text=pack.read_text('utf-8')
text,n=re.subn(r'(?m)^hash = "[a-f0-9]+"$',f'hash = "{sha(index)}"',text);assert n==1
pack.write_text(text,'utf-8',newline='\n')
assert tomllib.loads(pack.read_text('utf-8'))['index']['hash']==sha(index)
report={'installed_files_per_location':len(paths),'locations':[str(p) for p in roots.values()],'preserved_existing_snbt_files':preserved,'packwiz_hashes':'passed','reloaded_running_game':False}
(OUT/'installation.json').write_text(json.dumps(report,indent=2),'utf-8',newline='\n')
print(json.dumps(report,indent=2))
