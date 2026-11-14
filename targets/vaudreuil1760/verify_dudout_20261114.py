import json,sys,re,difflib,unicodedata
R=sys.argv[1]
k={int(a):b for a,b in json.load(open(R+'/key/key274.json')).items()}
for a,v in json.load(open(R+'/key/overrides.json')).items(): k[int(a)]=v['value'] if isinstance(v,dict) else v
def strip(s):
    s=unicodedata.normalize('NFD',s.lower()); s=''.join(c for c in s if c.isalpha() and not unicodedata.combining(c))
    return s.replace('y','i')
dec={};fol=None;n=0;unk=0
for l in open(R+'/transcription.txt'):
    if l.startswith('#'): continue
    if l.startswith('@'): fol=l.strip()[1:]; dec[fol]=[]; continue
    l=re.sub(r'\[[^\]]*\]',' ',l)
    for t in re.findall(r'\d+[?~^]*|~',l):
        if t=='~': continue
        n+=1
        if '~' in t: continue
        v=k.get(int(t.rstrip('?~^')))
        if v is None: unk+=1; continue
        dec[fol].append(v.rstrip('?'))
rd=open(R+'/reading.md').read()
parts=re.split(r'\n## (f\.\S+)',rd)
read={}
for i in range(1,len(parts),2):
    body=re.sub(r'\*[^*]*\*','',parts[i+1]); body=re.sub(r'\[[^\]]*\]','',body)
    read[parts[i].replace('f.','f')]=body
tot=m=0
for f in dec:
    a=strip(''.join(dec[f])); b=strip(read.get(f,''))
    sm=difflib.SequenceMatcher(None,a,b,autojunk=False); mm=sum(x.size for x in sm.get_matching_blocks())
    tot+=len(a); m+=mm
    print(f,'decoded letters',len(a),'matched in reading',mm,round(mm/max(1,len(a)),3))
    for op,i1,i2,j1,j2 in sm.get_opcodes():
        if op!='equal' and max(i2-i1,j2-j1)>=4: print('   ',op,repr(a[max(0,i1-8):i2+8]),'||',repr(b[max(0,j1-8):j2+8]))
print('numeric groups',n,'unkeyed',unk,'overall',round(m/tot,4))
