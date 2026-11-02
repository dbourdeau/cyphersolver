# Apply the French numeric keys held in the repo to No. 5, against 50 permuted copies of each key.
import glob,re,random,unicodedata,sys
import wordscore as WS
CT=r'C:/Users/dbour/cypher/targets/delacroix1797/ciphertext.txt'
L=[int(x) for l in open(CT,encoding='utf8') if l[0] not in '#f' for x in l.split()]
R=r'C:/Users/dbour/cypher/targets/'
F=['bouille1778/key.tsv','damas1787/key.tsv','martinique1778/key_bouille.tsv','mercier1761/key1761.tsv','mercier1761/key1765_ennery.tsv','affry1757/key_X.tsv','champigny1744/key.tsv']
F+=[f[len(R):].replace(chr(92),'/') for f in glob.glob(R+'affry1757c/key*.tsv')]
def n(s):
    s=unicodedata.normalize('NFD',s); return re.sub(r'[^a-z]','',''.join(c for c in s if not unicodedata.combining(c)).lower())
def dec(k): return ''.join(k.get(x,'') for x in L)
for f in F:
    try: rows=[l.rstrip('\n').split('\t') for l in open(R+f,encoding='utf8') if l.strip() and not l.startswith('#')]
    except Exception as e: print(f,'absent'); continue
    k={}
    for r in rows:
        if len(r)>1 and r[0].strip().isdigit():
            v=n(r[1])
            if v and int(r[0]) not in k: k[int(r[0])]=v
    cov=sum(x in k for x in L)/len(L)
    t=dec(k)
    if not t: print(f,'no coverage',len(k)); continue
    s=WS.score(t); rng=random.Random(1); nul=[]
    for _ in range(50):
        v=list(k.values()); rng.shuffle(v); nul.append(WS.score(dec(dict(zip(k,v)))))
    print(f'{f}: entries={len(k)} coverage={cov:.2f} score={s:.3f} null mean={sum(nul)/50:.3f} max={max(nul):.3f} | {t[:90]}',flush=True)
