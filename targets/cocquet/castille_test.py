# Castille-key test on transcription_f317.txt (14 Nov 2026 integration). Run: python3 -I castille_test.py transcription_f317.txt
# The shape correspondences in K are a judgement from Tomokiyo's table image (research/gallica_siblings/src/louisxiii_Castille.png).
import re,sys,collections
src=open(sys.argv[1],encoding='utf-8').read()
# Castille 1616 (Tomokiyo reconstruction, Clair 369 f.11): shape-label -> plain value, where the
# Cocquet label has a counterpart of the same drawn shape in the reconstructed table. Ambiguous ones: first choice.
K={'d':'f','d2':'f','TH':'b','q':'s','g':'s','ot':'g','PI':'','PI_':'','PIbar':'','PIbar_':'',
   'FF':'h','H':'l','eta':'p','x':'e','6':'d','I':'i','S':'n','a_':'c','a':'c','c':'e','n':'p','n_':'p',
   'y':'i','y_':'i','Z':'l','Zbar':'l','m':'o','o':'q','T1':'x','T2':'x','T3':'x','89':'[di]'}
toks=[]
for line in src.splitlines():
    if not line.startswith('L'): continue
    body=line.split(':',1)[1]
    body=re.sub(r'"[^"]*"',' | ',body)
    body=re.sub(r"\{([^|}]*)\|[^}]*\}",lambda m:m.group(1).replace(" ","~"),body)
    for t in body.replace('/',' ').split():
        if t=='|': toks.append('|'); continue
        if t.startswith('{'): t=t[1:-1].split('|')[0]
        toks.append(t)
ct=[t for t in toks if t!='|']
print('cipher tokens',len(ct))
c=collections.Counter(ct)
mapped=sum(v for k,v in c.items() if k in K)
print('tokens with a Castille counterpart',mapped, 'of',len(ct), f'{mapped/len(ct):.0%}')
print('no counterpart:',sorted(((v,k) for k,v in c.items() if k not in K),reverse=True))
out=''.join('|' if t=='|' else (K[t] if t in K and K[t] else ('' if t in K else '.')) for t in toks)
print(out)
pl=collections.Counter(ch for ch in out if ch.isalpha() and ch.islower())
print('plain letter counts',pl.most_common())
