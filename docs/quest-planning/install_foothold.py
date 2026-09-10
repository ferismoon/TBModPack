import sys,json,re,hashlib,shutil,tomllib
from pathlib import Path
sys.path.insert(0,'I:/McWork/ui-workshop/quest-validation-deps')
import nbtlib
root=Path('I:/McWork')
out=root/'docs/quest-planning/foothold'
rel='config/ftbquests/quests/chapters/00_a_foothold.snbt'
texture='config/openloader/resources/ftbquests/assets/ftbquests/textures/chapters/a_foothold.png'
grouprel='config/ftbquests/quests/chapter_groups.snbt'
chapter=json.loads((out/'chapter-source.json').read_text('utf-8'))
parsed=nbtlib.parse_nbt((root/rel).read_text('utf-8'))
assert str(parsed['id'])==chapter['id']
ids=[chapter['id'],chapter['group']]
for q in chapter['quests']:
 ids.append(q['id'])
 ids.extend(t['id'] for t in q['tasks'])
 ids.extend(t['id'] for t in q.get('rewards',[]))
assert len(ids)==len(set(ids))
qid={q['id'] for q in chapter['quests']}
edges=[(q['id'],d) for q in chapter['quests'] for d in q.get('dependencies',[])]
assert len(edges)==3 and all(d in qid for _,d in edges)
assert sum(not q['optional'] for q in chapter['quests'])==4
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
roots={'pack':root,'server':Path('I:/MC SERVER'),'client':Path('I:/PrismLauncher/instances/Forced Relocation/minecraft')}
old={}
for name,base in roots.items():
 old[name]={str(p):sha(p) for p in (base/'config/ftbquests/quests/chapters').glob('*.snbt') if p.name!='00_a_foothold.snbt'}
 for path in old[name]:
  existing=set(re.findall(r'\bid:\s*"([A-Fa-f0-9]{16})"',Path(path).read_text('utf-8')))
  assert not existing.intersection(ids),path
 text=(base/grouprel).read_text('utf-8')
 if chapter['group'] not in text:
  backup=out/'backups'/f'{name}-chapter_groups.snbt'
  backup.parent.mkdir(exist_ok=True)
  if not backup.exists():shutil.copy2(base/grouprel,backup)
  text,n=re.subn(r'(chapter_groups:\s*\[)',r'\1\n\t\t{ id: "'+chapter['group']+'", title: "New Beginnings" }',text,count=1)
  assert n==1
  (base/grouprel).write_text(text,'utf-8')
 if base!=root:
  for path in [rel,texture]:
   (base/path).parent.mkdir(parents=True,exist_ok=True)
   shutil.copy2(root/path,base/path)
 for path,digest in old[name].items():assert sha(Path(path))==digest
 for path in [rel,texture]:assert sha(base/path)==sha(root/path)
changelog=root/'docs/changelog.html'
text=changelog.read_text('utf-8')
if 'quest-foothold' not in text:
 text=text.replace('  <main>','  <main>\n    <section aria-labelledby="quest-foothold">\n      <h2 id="quest-foothold">In development — A Foothold</h2>\n      <p>A new starter quest chapter under New Beginnings: establish a home, arrange a repeatable food supply, and put a useful project to work, in any order. Optional examples and reference pages provide guidance. Shared facilities and existing work count.</p>\n      <p>Rewards are a small planting aid and a commemorative banner. Existing chapters are preserved. This chapter is ready for an in-game review.</p>\n    </section>',1)
 changelog.write_text(text,'utf-8')
home=root/'index.html';text=home.read_text('utf-8')
if 'A Foothold' not in text:
 text=text.replace('<li><strong>Utilities:</strong>','<li><strong>Quests in development:</strong> A Foothold introduces three independent settlement projects, with optional guidance and a commemorative reward.</li><li><strong>Utilities:</strong>',1)
 home.write_text(text,'utf-8')
for base in roots.values():
 for path in [grouprel,rel]:
  p=base/path;p.write_text(p.read_text('utf-8'),'utf-8',newline='\n')
for p in [changelog,home]:p.write_text(p.read_text('utf-8'),'utf-8',newline='\n')
index=root/'index.toml';text=index.read_text('utf-8')
for path in [grouprel,rel,texture]:
 digest=sha(root/path)
 pattern=r'(file = "'+re.escape(path)+r'"\s*\nhash = ")[^"]+(" )'
 pattern=r'(file = "'+re.escape(path)+r'"\s*\nhash = ")[^"]+(")'
 text,n=re.subn(pattern,lambda m:m[1]+digest+m[2],text)
 if not n:text+='\n[[files]]\nfile = "'+path+'"\nhash = "'+digest+'"\n'
index.write_text(text,'utf-8',newline='\n')
entries=tomllib.loads(text)['files'];assert len(entries)==len({e['file'] for e in entries})
for path in [grouprel,rel,texture]:assert next(e['hash'] for e in entries if e['file']==path)==sha(root/path)
pack=root/'pack.toml';text=pack.read_text('utf-8')
text,n=re.subn(r'(?m)^hash = "[a-f0-9]+"$',f'hash = "{sha(index)}"',text)
assert n==1
pack.write_text(text,'utf-8',newline='\n')
report={'snbt_parse':'passed','unique_ids':len(ids),'dependency_edges':len(edges),'preserved_chapters':{k:len(v) for k,v in old.items()},'installed_to':[str(p) for p in roots.values()],'packwiz_hashes':'passed','in_game_test':'not performed'}
(out/'validation.json').write_text(json.dumps(report,indent=2),'utf-8')
print(json.dumps(report,indent=2))
