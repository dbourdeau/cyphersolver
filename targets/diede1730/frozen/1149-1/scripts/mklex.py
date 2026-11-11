# Lexique M5 : prose de chancellerie 1730 (CLEAR de Nr. 1687, clair P.S.16, glose H 1687) n>=1 + Gutenberg allemand n>=3.
# Normalisation identique à measure.py 1687. Mots >=3 lettres ; mots courts : liste fermée.
import re,glob,collections
B='../../'  # local path redacted for publication (this copy's SHA-256 differs from PREREG-1730-A1.sha256)
H=B+'hannover-chancellerie-1719/1687/'
def norm(s):
    s=s.lower().replace('ß','ss')
    for a,b in (('ä','a'),('ö','o'),('ü','u'),('ÿ','y'),('j','i'),('y','i'),('w','u'),('v','u')): s=s.replace(a,b)
    return ''.join(ch if 'a'<=ch<='z' else ' ' for ch in s)
chanc=''
for f in sorted(glob.glob(H+'transcr/1687_*.txt')):
    for ln in open(f,encoding='utf-8'):
        if ln.startswith('CLEAR'): chanc+=' '+re.sub(r'\[[^\]]*\]','',ln[5:]).replace('-|','').replace('|',' ')
chanc+=' '+open(H+'transcr/CLAIR-PS16.txt',encoding='utf-8').read().replace('-|','')+' '+open(H+'G-GLOSE.txt',encoding='utf-8').read()
gut=''
for f in glob.glob(B+'cyphersolver-pr/wt-pares/targets/adfgvx/corpus/de_*.txt'):
    t=open(f,encoding='utf-8').read(); i=t.find('*** START'); j=t.find('*** END'); gut+=' '+t[i:j]
c1=collections.Counter(norm(chanc).split()); c2=collections.Counter(norm(gut).split())
SHORT={'zu','in','an','ob','so','da','es','er','um','im','ab','wo','ia','ia','du','am'}
lex={w for w,n in c1.items() if len(w)>=3}|{w for w,n in c2.items() if len(w)>=3 and n>=3}|SHORT
open('LEX-M5.txt','w').write('\n'.join(sorted(lex))+'\n'); print(len(lex),'mots; chancellerie',len(c1),'formes')
