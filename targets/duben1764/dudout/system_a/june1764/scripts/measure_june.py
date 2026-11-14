"""The one pre-registered measure (PREREG.md): metric of check2.py (PR #566), seed 1764.
usage: python3 -I measure_june.py key_c01.json cipher.txt clear.txt [--show]"""
import json,sys,re,random,difflib,unicodedata
K=json.load(open(sys.argv[1]))
def norm(s):
    s=unicodedata.normalize('NFD',s.lower()); return re.sub(r'[^a-z]','',s)
def clear_text(path):
    out=[]
    for l in open(path,encoding='utf-8'):
        if l.startswith('#'): continue
        p=l.split(None,1)
        if len(p)<2: continue
        t=re.sub(r'\[del:[^\]]*\]','',p[1])      # struck text dropped
        t=re.sub(r'\[ins:([^\]]*)\]',r'\1',t)    # interlinear insertions kept
        t=t.replace('[?]','')
        out.append(t)
    return norm(' '.join(out))
groups=[]
for l in open(sys.argv[2]):
    if l.startswith('#'): continue
    p=l.split(None,1)
    if len(p)<2: continue
    for g in re.split(r'[\s.]+',p[1]):
        v=re.sub(r'[^0-9]','',g.split('/')[0])
        if v and int(v)>=100: groups.append(str(int(v)))
gl=clear_text(sys.argv[3])
keymap={k:(v[0] if v and v[0] else '') for k,v in K.items()}
def dec(km): return ''.join(norm(km.get(g,'')) for g in groups)
def score(km):
    sm=difflib.SequenceMatcher(None,dec(km),gl,autojunk=False)
    return sum(b.size for b in sm.get_matching_blocks() if b.size>=4)/len(gl)
real=score(keymap); vals=list(keymap.values()); ks=list(keymap.keys())
random.seed(1764); ctr=[]
for i in range(200):
    random.shuffle(vals); ctr.append(score(dict(zip(ks,vals))))
cov=sum(1 for g in groups if keymap.get(g))/len(groups)
mx=max(ctr); ok= real>=0.15 and real>=mx+0.10
print(json.dumps({"groups_ge100":len(groups),"key_coverage":round(cov,3),"clear_letters":len(gl),
  "M":round(real,4),"ctrl_max":round(mx,4),"ctrl_mean":round(sum(ctr)/len(ctr),4),
  "threshold":"M>=0.15 and M>=ctrl_max+0.10","verdict":"PASS" if ok else "FAIL"},indent=1))
if '--show' in sys.argv: print(dec(keymap))
