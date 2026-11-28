"""Escovedo sheet (TNA SP 106/1 f. 116, DECODE 340) applied unchanged to the held-out lines of f. 93 (run from
targets/guaras1577 after scripts/fetch_kervyn.py). Exploratory, after the held-out test: not frozen or stamped.
Sheet values from escovedo_sheet/sheet_transcription.tsv, mapped onto the f. 93 shape notation; the vowel marks
of its syllables (1 a, 6 e, t i, e u) are read as their vowels."""
import json, os, sys, collections
os.environ['TSPLIT']='1'; sys.path.insert(0,'scripts')
import build_key as B, measure_lib as M
TR={'y':'i','f':'s','e':'c','t':'l'}; f=lambda x:''.join(TR.get(c,c) for c in x)
rebuilt=json.load(open('verification/key_1577_v1.json'))['key']
# Escovedo sheet, f.93 notation tokens that exist in both; vowel marks read as their vowels
sheet={'4':'a','3':'b','a':'c','2':'d','0':'e','1':'a','6':'e','t':'i','e':'u','7':'m','8':'n','9':'o','n':'o','b':'qu','P':'t','v':'y','g':'l','z':'d'}
P=json.load(open('verification/PROTOCOL_v1.json')); j0,j1=P['reference_units']
ref=[u if len(u)>1 else f(u) for u in B.U[j0:j1]]
toks=[t for lab in sorted(B.L) if lab in B.HELDOUT for t in B.L[lab]]
r,s,h=M.score(toks,{k:f(v) for k,v in sheet.items()},ref); c=M.controls(toks,{k:f(v) for k,v in sheet.items()},ref,n=200)
print('sheet unchanged on held-out:',r,s,round(r/s,3),'best control',round(max(c),3),'mean',round(sum(c)/len(c),3))
both=[t for t in toks if t in sheet and t in rebuilt]; same=sum(f(sheet[t])==f(rebuilt[t]) for t in both)
print('held-out tokens valued by both:',len(both),'same value:',same)
cnt=collections.Counter(toks)
for t in sorted(sheet, key=lambda x:-cnt[x]): print(t, 'sheet',sheet[t],'rebuilt',rebuilt.get(t),'n',cnt[t])
