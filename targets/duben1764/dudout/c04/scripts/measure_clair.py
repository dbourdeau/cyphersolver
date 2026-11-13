"""C04 — mesure unique (PREREG-AMENDEMENT-1) : key_c03 (gelée) sur 121-124L contre le clair 127-128. Graine 1231."""
import sys,json,re,random,difflib,statistics
B='/Users/bdudout/Documents/Veille cyber/dechiffrements-europe/lovisa-ulrika-1764/cryptanalysis/'
ORDER=['121','122L','123R','124L','122R']
def groups():
    pages={p:[] for p in ORDER}
    for l in open(B+'c03/transcr/lecture_121-124L.txt'):
        if l.startswith('#') or not l.strip(): continue
        lab,rest=l.split(' ',1); pg=lab.split('.')[0]
        rest=re.sub(r'\[del:[^\]]*\]','',rest)
        for t in rest.split():
            g=re.sub(r"[?'`]",'',t)
            if g.isdigit(): pages[pg].append(g)
    return [g for p in ORDER for g in pages[p]]
def norm(s): return re.sub(r'[^a-z]','',(s or '').lower())
def dec(key,G): return ''.join(norm(key.get(g)) for g in G)
def M(D,R):
    sm=difflib.SequenceMatcher(None,D,R,autojunk=False)
    return sum(b.size for b in sm.get_matching_blocks() if b.size>=4)/len(R)
def run(key,G,R,seed=1231):
    m=M(dec(key,G),R); rnd=random.Random(seed)
    vals=sorted(key); strs=[key[v] for v in vals]; W1=[];W2=[]
    for _ in range(200):
        p=strs[:]; rnd.shuffle(p); W1.append(M(dec(dict(zip(vals,p)),G),R))
    for _ in range(200):
        g=G[:]; rnd.shuffle(g); W2.append(M(dec(key,g),R))
    W=W1+W2
    return {'M':round(m,4),'perm_max':round(max(W1),4),'perm_mean':round(statistics.mean(W1),4),
            'shuf_max':round(max(W2),4),'shuf_mean':round(statistics.mean(W2),4),
            'known_groups':sum(1 for g in G if key.get(g) is not None),'groups':len(G),
            'verdict':'VALIDEE' if (m>=0.35 and m>max(W) and m-max(W)>=0.15) else 'NON VALIDEE'}
if __name__=='__main__':
    G=groups(); R=open(B+'c04/clair/127-128_norm.txt').read().strip()
    K=json.load(open(B+'c03/construction/key_c03.json'))
    out={'primaire_key_c03':run(K,G,R),'R_len':len(R)}
    K2=dict(K); K2.update(json.load(open(B+'c03/construction/c03b_ajouts.json')))
    out['descriptif_key_c03_plus_ajouts']=run(K2,G,R)
    print(json.dumps(out,indent=1))
