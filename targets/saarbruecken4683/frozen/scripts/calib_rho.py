# Calibration PREREG-3 (portion grillée 297/298 seulement, sans aucune clé) :
# rho = accord des mots EN CLAIR de la lettre 297 avec le concept 298 (alignement local par run de mots clairs)
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from norm import norm
from sw import sw_match
B=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')
runs=[];cur=''
for l in open(os.path.join(B,'transcriptions','ARBITRE-297.txt')):
    m=re.match(r'(29\d[rv] L\d+) \| (.*)',l.strip())
    if not m: continue
    s=re.sub(r'\[[^\]]*\]',' ',m.group(2))
    for t in re.findall(r'\{[^}]*\}|\?\?|\d+\??',s):
        if t.startswith('{'): cur+=norm(t[1:-1])
        else:
            if len(cur)>=8: runs.append(cur)
            cur=''
if len(cur)>=8: runs.append(cur)
ref=[]
for l in open(os.path.join(B,'transcriptions','concept-298.txt')):
    if l.startswith('# Ratures'): break
    m=re.match(r'298[rv] L\d+ \| (.*)',l.strip())
    if m: ref.append(re.sub(r'\[\?\]','',m.group(1)))
ref=norm(' '.join(ref))
tot=ok=0
for r in runs:
    ok+=sw_match(r,ref); tot+=len(r)
print('runs',len(runs),'caractères',tot,'rho',round(ok/tot,4))
