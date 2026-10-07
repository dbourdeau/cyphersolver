"""control.py: shuffled-key control for the spelled (homophone) layer of the June 1676 letter.
Real key vs N random permutations of the number->letter table: share of decoded spelled words that are Dutch words/known names."""
import re,random,itertools,os
from pathlib import Path
B = Path(__file__).resolve().parents[1]
lex=set(w.strip().lower() for w in open(os.environ['BEUNINGEN_OPENTAAL'],encoding='utf-8') if w.strip().isalpha())
names={'briel','hellevoet','brugge','brussel','bastiaense','thomas','plat','platt','straught','engelschen','engelsche'}
# period/loan words attested in WNT (17th-c. spelling), added equally for real and shuffled runs
names|={'attrapperen','gedestineert','bylanders','prouven','steerl'}
def variants(w):
    out={w}
    rules=[('y','ij'),('y','i'),('uy','u'),('ue','oe'),('ou','oe'),('wd','d'),('lt','ld'),('ae','aa'),('uy','ui'),('gh','g'),('ck','k'),('c','k'),('uu','uv'),('ou','ouw'),('sch','s'),('u','v'),('v','u'),('ee','e'),('oo','o'),('ght','cht'),('gt','cht'),('dt','d'),('th','t')]
    for _ in range(3):
        new=set()
        for v in out:
            for a,b in rules:
                if a in v: new.add(v.replace(a,b))
        out|=new
        if len(out)>400: break
    return out
def isword(w):
    if w in names: return True
    if len(w)<2: return w in ('t',)
    return any(v in lex for v in variants(w))
L={}
for l in open(B / 'key/key_letters.tsv'):
    if l.startswith('#') or not l.strip(): continue
    p=l.split('\t'); L[p[0]]=p[1]
seqs=[]
for line in open(B / 'transcription/june1676_tx.txt'):
    if line.startswith('#'): continue
    for m in re.finditer(r'\{([^}]*)\}',line): seqs.append([x.strip() for x in m.group(1).split(',')])
def score(K):
    ok=0
    for s in seqs4:
        w=''.join(K.get(n,'?') for n in s).replace('uu','uv')
        w=('v'+w[1:]) if w.startswith('u') and len(w)>2 and w[1] not in 'aeiou' else w
        if '?' not in w and isword(w): ok+=1
    return ok
seqs4=[q for q in seqs if len(q)>=4]
real=score(L)
nums=list(L.keys()); vals=[L[n] for n in nums]
random.seed(1676); sh=[]
for i in range(1000):
    v=vals[:]; random.shuffle(v); sh.append(score(dict(zip(nums,v))))
# second control: shuffle token order within each sequence (keeps letter frequencies, destroys words)
def score_perm():
    ok=0
    for s in seqs4:
        s2=s[:]; random.shuffle(s2); w=''.join(L.get(n,'?') for n in s2)
        if '?' not in w and len(s2)>2 and isword(w) : ok+=1
        elif len(s2)<=2:
            if '?' not in w and isword(w): ok+=1
    return ok
sp=[score_perm() for _ in range(200)]
print('spelled sequences:',len(seqs4))
print('real key: %d/%d = %.1f%% decode to Dutch words/names'%(real,len(seqs4),100*real/len(seqs4)))
print('shuffled key (1000x): mean %.1f%%, max %.1f%%'%(100*sum(sh)/len(sh)/len(seqs4),100*max(sh)/len(seqs4)))
print('within-word token shuffle (200x): mean %.1f%%, max %.1f%%'%(100*sum(sp)/len(sp)/len(seqs4),100*max(sp)/len(seqs4)))
bad=[''.join(L.get(n,'?') for n in s) for s in seqs4 if not isword(''.join(L.get(n,'?') for n in s))]
print('real-key non-words:',bad)
