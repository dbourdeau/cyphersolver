# Diagnostic (non PREREG): C01 key (built on letter 96, Jan-Feb 1764) applied to 15 Nov 1765 cipher;
# score = share of gloss letters covered by matching blocks (difflib) between decoded letters and gloss letters.
import json,sys,re,random,difflib,unicodedata
K=json.load(open(sys.argv[1])); txt=open(sys.argv[2]).read().splitlines()
def norm(s):
    s=unicodedata.normalize('NFD',s.lower()); return re.sub(r'[^a-z]','',s)
gl='';groups=[]
for l in txt:
    m=re.match(r'^(\S+?)([TGC])\s(.*)$',l)
    if not m: continue
    if m.group(2)=='G' and m.group(3).strip()!='-': gl+=norm(m.group(3))
    if m.group(2)=='C':
        for g in m.group(3).split():
            v=re.sub(r'[^0-9]','',g)
            if v and int(v)>=100: groups.append(str(int(v)))
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
print(f"groups>=100: {len(groups)} ; covered by C01 key: {cov:.3f} ; gloss letters {len(gl)}")
print(f"real {real:.3f} ; controls (200 permuted keys) max {max(ctr):.3f} mean {sum(ctr)/len(ctr):.3f}")
