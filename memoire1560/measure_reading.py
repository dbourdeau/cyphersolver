"""Conservative editorial coverage, not independently measured decipherment accuracy.

Longest-first units from the inherited sign convention count compound ASCII signs once.
Every sign on any line containing a bracketed reading is treated as unresolved. This
deliberately understates lexical coverage. Counts describe this transcription, not a
definitive census of the manuscript's graphically distinct symbols.
"""
from pathlib import Path
import json,re,csv
from decrypt import lines,load_key
ROOT=Path(__file__).resolve().parent
key=load_key()
units=sorted((k for k in key if not k.startswith('=')),key=len,reverse=True)
read={l.split('\t',1)[0]:l.split('\t',1)[1] for l in (ROOT/'reading_working.tsv').read_text(encoding='utf8').splitlines() if l and not l.startswith('#')}
def tokenize(w):
    if '='+w in key:return ['WORD_'+w]
    out=[]
    while w:
        t=next((u for u in units if w.startswith(u)),w[0]);out.append(t);w=w[len(t):]
    return out
cts={f'{f}.{n:02d}':c for f,n,c in lines()}
# New supplemental transcriptions, checked on image; diplomatic spellings may differ
# from the normalized reading. Marginal source is written across three short lines.
cts['153r.14m']='+mmxppdWxm xr W+ fg+ppds3x hio f:rmxiW'
cts['157v.01']='+hioxSQDmmxppxrm'
rows=[];tokens=[];tot=bad=0
for lab,ct in sorted(cts.items()):
    ct=re.sub(r'\[[^\]]*\]','',ct).replace('=','')
    if lab=='155v.03':ct=re.sub(r'\sZ$','',ct) # horizontal line filler, not POUR
    ts=[t for w in ct.split() for t in tokenize(w)]
    unresolved='[' in read[lab]
    rows.append([lab,len(ts),'M' if unresolved else 'I',read[lab],ct])
    tokens.append(lab+' '+' '.join(ts))
    tot+=len(ts);bad+=len(ts) if unresolved else 0
with (ROOT/'coverage.tsv').open('w',encoding='utf8',newline='') as f:
    wr=csv.writer(f,delimiter='\t');wr.writerow(['line','transcribed_sign_units','grade','normalized_reading','source_transcription']);wr.writerows(rows)
(ROOT/'cipher_tokens.txt').write_text('\n'.join(tokens)+'\n',encoding='utf8')
result={'transcribed_sign_units':tot,'conservatively_unresolved_units':bad,'coherent_units':tot-bad,'fraction_coherent':(tot-bad)/tot,'lines':len(rows),'uncertain_lines':[r[0] for r in rows if r[2]=='M'],'method':'All inherited-transcription sign units on every bracketed line count unresolved, including otherwise readable words; normalised editorial reading, not independent token-accuracy validation.'}
(ROOT/'coverage.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps(result,ensure_ascii=False,indent=2))
