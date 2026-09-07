import struct, zlib, json, pathlib, math, gzip, zipfile

class NBT:
    def __init__(self,b): self.b=b; self.i=0
    def take(self,n): r=self.b[self.i:self.i+n]; self.i+=n; return r
    def num(self,f): return struct.unpack('>'+f,self.take(struct.calcsize('>'+f)))[0]
    def string(self): return self.take(self.num('H')).decode('utf8')
    def value(self,t):
        if t in (1,2,3,4,5,6): return self.num({1:'b',2:'h',3:'i',4:'q',5:'f',6:'d'}[t])
        if t==7: return list(self.take(self.num('i')))
        if t==8: return self.string()
        if t==9:
            kind=self.num('B'); return [self.value(kind) for _ in range(self.num('i'))]
        if t==10:
            out={}
            while True:
                kind=self.num('B')
                if not kind: return out
                name=self.string(); out[name]=self.value(kind)
        if t in (11,12): return [self.num('i' if t==11 else 'q') for _ in range(self.num('i'))]
        raise ValueError(t)
    def root(self): t=self.num('B'); self.string(); return self.value(t)

root=pathlib.Path(r'I:\PrismLauncher\instances\Forced Relocation\minecraft\saves\New World')
def chunk(cx,cz):
    p=root/'region'/f'r.{cx//32}.{cz//32}.mca'
    if not p.exists(): return None
    with p.open('rb') as f:
        f.seek(4*((cx%32)+(cz%32)*32)); h=f.read(4); offset=int.from_bytes(h[:3],'big')*4096
        if not offset: return None
        f.seek(offset); n=int.from_bytes(f.read(4),'big'); kind=f.read(1)[0]; data=f.read(n-1)
    return NBT(zlib.decompress(data) if kind==2 else data).root()
def block(c,x,y,z):
    for s in c.get('sections',[]):
        if s['Y']!=y//16: continue
        bs=s.get('block_states',{}); pal=bs.get('palette',[])
        if not pal: return None
        if len(pal)==1: return pal[0]
        bits=max(4,(len(pal)-1).bit_length()); per=64//bits; i=(y%16)*256+(z%16)*16+x%16
        v=(bs['data'][i//per] & ((1<<64)-1)) >> ((i%per)*bits) & ((1<<bits)-1)
        return pal[v]
x,y,z=-3517,66,-266; cx,cz=x//16,z//16
template='data/minecraft/structures/village/plains/houses/plains_small_house_4.nbt'
archives=[pathlib.Path(r'I:\PrismLauncher\libraries\com\mojang\minecraft\1.20.1\minecraft-1.20.1-client.jar')]
client=root.parent.parent
archives+=list((client/'mods').glob('*.jar'))+list((client/'config/openloader/data').glob('*.zip'))
for archive in archives:
    with zipfile.ZipFile(archive) as a:
        if template not in a.namelist(): continue
        t=NBT(gzip.decompress(a.read(template))).root()
        containers=[b for b in t['blocks'] if any(k in t['palette'][b['state']]['Name'] for k in ('chest','barrel'))]
        print('TEMPLATE',archive.name,'containers',containers)
        # Counterclockwise rotation maps (x,z) to (z,-x).
        for b in t['blocks']:
            px,py,pz=b['pos']
            if (-3520+pz,65+py,-264-px)==(x,y,z): print('TEMPLATE_TARGET',t['palette'][b['state']])
c=chunk(cx,cz)
if c is None:
    level=NBT(gzip.decompress((root/'level.dat').read_bytes())).root()
    player=level.get('Data',{}).get('Player',{})
    print('No saved chunk at supplied coordinates. Saved player:',player.get('Pos'),player.get('Dimension'))
    raise SystemExit(0)
print('TARGET',cx,cz,block(c,x,y,z))
for yy in range(y-1,y+3):
    print('LAYER',yy,[(xx,zz,block(c,xx,yy,zz)) for xx in range(x-1,x+2) for zz in range(z-1,z+2)])
for dx in range(-2,3):
    for dz in range(-2,3):
        q=chunk(cx+dx,cz+dz)
        if not q: continue
        for be in q.get('block_entities',[]):
            if 'LootTable' in be or any(k in be.get('id','') for k in ('chest','barrel','lootr')):
                print('CONTAINER',json.dumps(be)[:1200])
        st=q.get('structures',{})
        if dx==0 and dz==0: print('REFERENCES',st.get('References',{}))
        for name,v in st.get('starts',{}).items():
            if v.get('id')!='INVALID':
                print('STRUCTURE',name, v.get('ChunkX'),v.get('ChunkZ'))
                for child in v.get('Children',[]):
                    bb=child.get('BB',[])
                    if len(bb)==6 and bb[0]-10<=x<=bb[3]+10 and bb[2]-10<=z<=bb[5]+10: print('PIECE',json.dumps(child))
