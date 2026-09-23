"""Editorial alignment aid. Similarity is NOT verification or a recovered key."""
from pathlib import Path
import re,json,unicodedata,csv
from difflib import SequenceMatcher
from decrypt import lines,load_key,dec_word
ROOT=Path(__file__).resolve().parent
key=load_key(); units=sorted((k for k in key if not k.startswith('=')),key=len,reverse=True)
read={l.split('\t',1)[0]:l.split('\t',1)[1] for l in (ROOT/'reading_working.tsv').read_text(encoding='utf8').splitlines() if l and not l.startswith('#')}
def norm(s):
    s=''.join(c for c in unicodedata.normalize('NFD',s.lower()) if c.isascii() and c.isalpha())
    return s.replace('v','u').replace('j','i')
def distance(a,b):
    a,b=norm(a),norm(b)
    return 1-SequenceMatcher(None,a,b).ratio()
rows=[]; issues=[]
for fol,n,ct in lines():
    lab=f'{fol}.{n:02d}'
    cs=re.sub(r'\[[^\]]*\]','',ct).replace('=','').split()
    ps=read[lab].split()
    ds=[dec_word(x,key,units) for x in cs]
    N,M=len(cs),len(ps)
    dp={(0,0):(0,[])}
    for i in range(N+1):
        for j in range(M+1):
            if (i,j) not in dp:continue
            cost,path=dp[i,j]
            for a,b in [(1,1),(1,2),(2,1),(1,0),(0,1)]:
                if i+a>N or j+b>M:continue
                c=distance(''.join(ds[i:i+a]),''.join(ps[j:j+b]))+.2*(a+b-2) if a and b else .85
                new=(cost+c,path+[(i,j,a,b,c)])
                if (i+a,j+b) not in dp or new[0]<dp[i+a,j+b][0]:dp[i+a,j+b]=new
    for i,j,a,b,c in dp[N,M][1]:
        rec={'line':lab,'cipher':' '.join(cs[i:i+a]),'mechanical':' '.join(ds[i:i+a]),'reading':' '.join(ps[j:j+b]),'cost':round(c,3),'kind':f'{a}:{b}'}
        rows.append(rec)
        if not a or not b:issues.append(rec)
(ROOT/'alignment_draft.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
for r in issues:print(r['line'],r['kind'],r['cipher'],r['mechanical'],'->',r['reading'])
print(len(rows),'aligned groups;',len(issues),'insertion/deletion candidates')
