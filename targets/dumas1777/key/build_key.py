"""Build position->character table from keytext_1775.txt; check line totals against Dumas's 1776 list and against the 1778 glosses."""
import json,unicodedata,hashlib,os,sys
D=os.path.dirname(os.path.abspath(__file__))
lines=[l.rstrip('\n') for l in open(os.path.join(D,'keytext_1775.txt')) if not l.startswith('#')]
s=[];ends=[]
for l in lines:
    s+= [c for c in l if not c.isspace()]; ends.append(len(s))
dumas=[57,114,168,223,278,335,394,445,499,555,612,666,682]
print('line ends ours ',ends); print('line ends Dumas',dumas, 'OK' if ends==dumas else 'MISMATCH')
def base(c):
    b=unicodedata.normalize('NFD',c)[0].lower(); return b
key={i+1:c for i,c in enumerate(s)}
out={'source':'see keytext_1775.txt','positions':{str(k):v for k,v in key.items()}}
p=os.path.join(D,'key_positions.json'); json.dump(out,open(p,'w'),ensure_ascii=False,indent=0)
print('sha256 key_positions.json',hashlib.sha256(open(p,'rb').read()).hexdigest())
gl=json.load(open(os.path.join(D,'..','tests','test1','key_full.json')))
eq={"'":",'=.;","=":"-",",":",;'",'&':'&'}
mis=[]
for k,v in gl['key'].items():
    c=key.get(int(k),'?'); 
    if base(c)==v.lower() or (v in eq and c in eq[v]) : continue
    mis.append((int(k),v,c))
print('glossed numbers',len(gl['key']),'disagree',len(mis),sorted(mis))
