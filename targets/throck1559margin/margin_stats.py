# Word-level identifiability test for the R2988 margin: count group types and hapaxes, and compare the
# repeat structure with English prose of the same length (Bain ii windows).
import re,collections,random,os
os.chdir(os.path.dirname(os.path.abspath(__file__)))   # split 14 Oct 2026: bain2.txt (Bain ii OCR, git-ignored) stays in ../wod1568/
L=[l.split(':',1)[1] for l in open('margin_transcription.txt',encoding='utf-8') if re.match(r'[MDS]\d\d:',l)]
txt=' '.join(L); txt=re.sub(r'\{[^}]*\}','',txt).replace('[','').replace(']','')
g=[x for x in txt.split() if x not in('/','//','//#','...')]
C=collections.Counter(g); n=len(g)
print('tokens',n,'types',len(C),'hapax',sum(v==1 for v in C.values()),'top',C.most_common(8))
w=re.findall('[a-z]+',open('../wod1568/bain2.txt',encoding='utf-8',errors='ignore').read().lower())
ts=[];hs=[]
for _ in range(500):
    k=random.randrange(len(w)-n); c=collections.Counter(w[k:k+n]); ts.append(len(c)); hs.append(sum(v==1 for v in c.values()))
ts.sort();hs.sort(); print('English',n,'words: types median',ts[250],'hapax median',hs[250])
