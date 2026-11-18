"""Round 15 check: which values does the king's letter (R1156) support?
Usage: python3 -I check_r1156.py R1156_V2626_transcription.txt ../../vestigia/K_V.json
Counts, for each letter of the period clear copy (Vestigia 2627), the signs written for it, and decodes the
letter with three keys: K_V as it stands (rebuilt on the queen's letter of 31 May only), K_V plus the extra
signs of this letter, and the two disputed values of the earlier key of this letter (9 = e, 2 = d)."""
import sys, json, collections, difflib
runs=[]
for l in open(sys.argv[1],encoding='utf-8'):
    if l.startswith('#') or l.count('|')<2: continue
    ln,word,toks=[x.strip() for x in l.split('|')]
    runs.append((int(ln),word,toks.split()))
K=dict(json.load(open(sys.argv[2]))['key'])
NOM={'G','W','NFERD','NSTAR','NTRI','NK','NX'}
letters=[(w,t) for _,w,t in runs if not (set(t)<=NOM)]
signs=sum(len(t) for _,_,t in runs)
print('runs',len(runs),'signs',signs,'of which name signs',sum(1 for _,_,t in runs for x in t if x in NOM))
# sign-by-letter table, from the words whose sign count equals their letter count (tt = TT)
tab=collections.defaultdict(collections.Counter)
for w,t in letters:
    exp=[]
    i=0
    while i<len(w):
        if w[i:i+2]=='tt': exp.append('tt'); i+=2
        else: exp.append(w[i]); i+=1
    if len(exp)==len(t):
        for a,b in zip(exp,t): tab[a][b]+=1
for a in 'degiuvs':
    print(a, dict(tab[a]))
def score(key,label):
    ok=tot=0; bad=[]
    for w,t in letters:
        d=''.join(key.get(x,'?') for x in t)
        ref=w.replace('v','u'); d=d.replace('v','u')
        m=sum(b.size for b in difflib.SequenceMatcher(None,d,ref,autojunk=False).get_matching_blocks())
        ok+=m; tot+=len(ref)
        if d!=ref: bad.append(f'{w}:{d}')
    print(f'{label}: {ok}/{tot} = {ok/tot:.3f} of the letters of the copy')
    return bad
bad=score(K,'K_V as it stands')
ext=dict(K); ext.update({'5':'e','DH':'e','O0':'i','B':'s','3E':'u','9u':'d','Zs':'i'})
bad2=score(ext,'K_V + this letter\'s extra signs (5, DH = e; O0 = i; B = s; 3E = u)')
print('  words still differing:', ', '.join(bad2))
old=dict(ext); old.update({'9':'e','9u':'e','2':'d'})
score(old,'same, with the earlier key\'s 9 = e and 2 = d')
old2=dict(ext); old2.update({'9':'e','9u':'e','2':'i'})
score(old2,'same, with the earlier key\'s 9 = e and 2 = i')
