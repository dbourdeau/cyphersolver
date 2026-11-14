import json,sys,re,random,difflib,unicodedata
K=json.load(open(sys.argv[1]))
def norm(s):
    s=unicodedata.normalize('NFD',s.lower()); return re.sub(r'[^a-z]','',s)
groups=[]
for l in open(sys.argv[2]):
    if l.startswith('#'):continue
    parts=l.split(None,1)
    if len(parts)<2: continue
    for g in parts[1].split():
        v=re.sub(r'[^0-9]','',g)
        if v and int(v)>=100: groups.append(str(int(v)))
gl=norm(' '.join(l.split(None,1)[1] if len(l.split(None,1))>1 else '' for l in open(sys.argv[3]) if not l.startswith('#')))
keymap={k:(v[0] if v and v[0] else '') for k,v in K.items()}
def score(km):
    d=''.join(norm(km.get(g,'')) for g in groups)
    sm=difflib.SequenceMatcher(None,d,gl,autojunk=False)
    return sum(b.size for b in sm.get_matching_blocks() if b.size>=4)/len(gl)
real=score(keymap); vals=list(keymap.values()); ks=list(keymap.keys())
random.seed(1616); ctr=[]
for i in range(200):
    random.shuffle(vals); ctr.append(score(dict(zip(ks,vals))))
cov=sum(1 for g in groups if keymap.get(g))/len(groups)
print(f"groups: {len(groups)} cov {cov:.3f} clear letters {len(gl)} real {real:.3f} ctrl max {max(ctr):.3f} mean {sum(ctr)/len(ctr):.3f}")
