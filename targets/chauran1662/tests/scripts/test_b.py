#!/usr/bin/env python3
"""Test B (see TEST_PLAN.md). One run."""
import sys, math, collections, re
sys.path.insert(0,'scripts')
from testlib import *
T,tier=load_table()
corp=re.sub(r'[^a-z]','',open('tests/spanish_reference_corpus.txt').read())
c3=collections.Counter(corp[i:i+3] for i in range(len(corp)-2)); c2=collections.Counter(corp[i:i+2] for i in range(len(corp)-1))
def lp(run):
    s='##'+run; t=0.0
    for i in range(2,len(s)):
        t+=math.log((c3[s[i-2:i+1]]+0.1)/(c2[s[i-2:i]]+0.1*26))
    return t
def letters(v):
    import unicodedata
    v=unicodedata.normalize('NFD',v.lower()); return re.sub(r'[^a-z]','',''.join(c for c in v if unicodedata.category(c)!='Mn'))
def groups_of(path,sel):
    out=[]
    for sec,recs in sections(path).items():
        for r in recs:
            if not r['groups']: continue
            if sel(sec,r):
                out+= [gid(g) for g in r['groups'] if not g['struck'] and g['num'] is not None]
    return out
def lnum(r): return int(re.match(r'\d+',r['line']).group(0))
def bare(sec,r): return not r['gloss'] or r['gloss'].startswith('(none') or len(gloss_clean(r['gloss']))<3
ITEMS=[
 ('f187 bare (r L06-, v, 188r)','t187/f187_pass1.txt',lambda s,r: not(s.startswith('f187 page 1') and lnum(r)<=5)),
 ('f243 r L05-, v, 244r','t243a/f243_p1-2_pass1.txt',lambda s,r: not(s.startswith('f243 page 1') and lnum(r)<=4)),
 ('f243 244v (second hand)','t243b/f243_p3-5_pass1.txt',lambda s,r: s.startswith('f243 page 3 left')),
 ('f243 245r-v','t243b/f243_p3-5_pass1.txt',lambda s,r: not s.startswith('f243 page 3 left')),
 ('f231 r-v','t231/f231_pass1.txt',lambda s,r: s.startswith('f231 page 1') or s.startswith('f231 page 2')),
 ('f306 r-v','t306/f306_pass1.txt',lambda s,r: True),
 ('f313 r-314r','t313/f313_pass1.txt',lambda s,r: True),
 ('f315 r-316r','t315/f315_pass1.txt',lambda s,r: True),
 ('f317 r-318v','t317/f317_pass1.txt',lambda s,r: True),
]
REPORT=[
 ('f264 bare lines (reported only)','t264/f264_pass1.txt',None),
 ('f294 bare lines (reported only)','t294/f294_pass1.txt',None),
 ('control: f189+f260 (key letters)','KEY',None),
 ('control: f228 French cipher, 4 lines','t231/f228_pass1.txt',lambda s,r: s.startswith('Sample')),
]
def score(groups,Tb):
    runs=[];cur=''
    for g in groups:
        v=Tb.get(g)
        if v is None:
            if cur: runs.append(cur); cur=''
        else: cur+=letters(v)
    if cur: runs.append(cur)
    n=sum(len(x) for x in runs)
    return (sum(lp(x) for x in runs)/n) if n else float('nan')
out=open('tests/test_b_result.txt','w')
def P(*a):
    s=' '.join(str(x) for x in a); print(s); out.write(s+'\n')
P('Test B, table_v1 sha256',SHA,'; corpus letters',len(corp))
shuf=[shuffled(T,seed) for seed in range(1,201)]
def do(name,groups,judge=True):
    if not groups: P('%-36s no groups found'%name); return
    cov=sum(1 for g in groups if g in T)/len(groups)
    s=score(groups,T); ss=[score(groups,x) for x in shuf]
    above=sum(1 for x in ss if x>=s)
    verdict=''
    if judge:
        verdict='PASS' if (cov>=0.45 and above==0) else ('FAIL' if (cov<0.45 and above>0) else 'NOT SHOWN')
    P('%-36s groups %4d  coverage %.1f%%  Spanish score %.3f  shuffled mean %.3f max %.3f  shuffles >= real: %d/200  %s'%(name,len(groups),100*cov,s,sum(ss)/200,max(ss),above,verdict))
for name,path,sel in ITEMS: do(name,groups_of(path,sel))
# reported only
def glossed_off(path,off):
    out=[]
    for sec,recs in sections(path).items():
        gl=[gloss_clean('' if (r['gloss'] or '').startswith('(none') else r['gloss']) for r in recs]
        for k,r in enumerate(recs):
            if not r['groups']: continue
            j=k-off; own=gl[j] if 0<=j<len(gl) else ''
            if len(own)<10: out+=[gid(g) for g in r['groups'] if not g['struck'] and g['num'] is not None]
    return out
do('f264 bare lines (reported only)',glossed_off('t264/f264_pass1.txt',1),False)
do('f294 bare lines (reported only)',glossed_off('t294/f294_pass1.txt',0),False)
import json
D=json.load(open('key/reconciled_ff189_260.json'))
kg=[('%s%s'%(g['num'],(':'+g['mark']) if g['mark'] else '')) for f in D for r in D[f] for g in r['groups'] if not g['struck'] and g['num'] is not None]
do('control: ff.189+260 (key letters)',kg,False)
do('control: f228 French cipher sample',groups_of('t231/f228_pass1.txt',lambda s,r: True),False)
