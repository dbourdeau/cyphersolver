import sys
sys.path.insert(0,'..');from lang import lm
M=lm.load('fr-1600-letters',order=5,spaces=False)
exec(open('cands.py',encoding='utf8').read())
lines=[l.split() for l in open(sys.argv[1],encoding='utf8') if l.strip()]
lat=[];brk=[]
for L in lines:
    for t in L:
        if t.startswith('{'): w=t[1:-1];lat.append([W.get(w,'['+w+']')])
        else: lat.append(list(C.get(t,'?')))
    brk.append(len(lat))
def sc(s):
    s2=lm.norm(s.replace('[','').replace(']',''),'early',spaces=False);return M.score_idx(M.encode(s2)) if s2 else 0
beam=[('',[])]
for opts in lat:
    nb=[(s+o,ch+[o]) for s,ch in beam for o in opts]
    nb.sort(key=lambda x:-sc(x[0][-80:]));beam=nb[:int(sys.argv[2]) if len(sys.argv)>2 else 80]
ch=beam[0][1];p=0
for i,b in enumerate(brk):
    print('%02d'%(i+1),''.join(ch[p:b]));p=b
