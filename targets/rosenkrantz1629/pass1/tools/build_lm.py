"""build_lm.py: Danish c.1620-35 character model from Christian IV's own letters (Bricka/Fridericia vols 1-3, archive.org OCR).
Paragraph blocks are kept when Danish marker words outnumber German ones. Output lm/da1620.txt (normalised text) and lm/da1620_5g.json."""
import re,json,math,collections
R='/home/claude/keyless/rosenkrantz1629'
DA=set('och att ieg jeg haffuer skall thill till med icke dett den som paa saa eller huad naar aff er y dy wy uy epther mig dig hannem sig forne bliffuer kand'.split())
DE=set('vndt und dass das ich nit nicht der die ist zu von wirdt auff mihr dem den eiin sii wii auch so'.split())
out=[]
for v in ('01','02','03'):
    t=open(f'{R}/dl/c4_{v}.txt',encoding='utf-8',errors='replace').read()
    t=t.replace('æ','ae').replace('Æ','ae').replace('ø','o').replace('Ø','o').replace('å','aa').replace('ö','o').replace('ü','u').replace('ä','a')
    for blk in re.split(r'\n\s*\n',t):
        w=re.findall(r'[A-Za-z]+',blk.lower())
        if len(w)<12: continue
        a=sum(x in DA for x in w); g=sum(x in DE for x in w)
        if a>=4 and a>2*g and a/len(w)>0.12:
            out.append(' '.join(w))
txt=' '.join(out); open(f'{R}/lm/da1620.txt','w').write(txt)
s=txt.replace(' ','')
N=5; c=collections.Counter(s[i:i+N] for i in range(len(s)-N+1)); tot=sum(c.values())
lp={k:math.log10(v/tot) for k,v in c.items() if v>=2}
json.dump({'n':N,'floor':math.log10(0.5/tot),'lp':lp},open(f'{R}/lm/da1620_5g.json','w'))
print('blocks',len(out),'words',len(txt.split()),'chars',len(s),'5grams',len(lp))
print(collections.Counter(s).most_common(26)); print(txt[5000:5400])
