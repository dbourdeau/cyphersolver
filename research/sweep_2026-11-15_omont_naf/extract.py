"""Segment the Omont catalogue OCR by shelfmark heading and print/collect segments with a cipher word.
usage: python extract.py raw/<file>.txt [series-label] > out"""
import re,sys,json
f=sys.argv[1]
t=open(f,encoding='utf8',errors='ignore').read()
t=re.sub(r'-\s*\n\s*','',t); t=re.sub(r'[ \t]*\n[ \t]*','\n',t)
hd=re.compile(r'(?:(?<=\n)|^)(\d{4,5}(?:\s*[-–—]\s*\d{4,5}|\s*\(\d+\))?(?:\s*(?:bis|ter))?)\s*\.\s')
hs=list(hd.finditer(t))
cip=re.compile(r"(?<![a-zé])(?:non\s+)?(?:d[eé])?c[hl][il1]{1,2}[fl]{1,3}r[eé]?e?s?(?![a-z])|(?<![a-z])chifre|cryptogr\w*|st[eé]ganogr\w*|[eé]criture secr\w+",re.I)
bad=re.compile(r"chiffre\s+(?:de|du|d')|au[x]?\s+.{0,3}chiffre|chiffres?\s+romains?|Chifflet|Chiffrevast|chiffre\s+et\s+armes|armes\s+et\s+chiffre|Achille|Chiffrbville|non\s+chiffr",re.I)
out=[]
for i,h in enumerate(hs):
    s=h.start(); e=hs[i+1].start() if i+1<len(hs) else len(t)
    seg=t[s:e]
    if len(seg)>60000: seg=seg[:60000]
    hits=[]
    for m in cip.finditer(seg):
        ctx=seg[max(0,m.start()-30):m.end()+30]
        if bad.search(ctx): continue
        hits.append((m.start()))
    if hits:
        segc=re.sub(r'\s+',' ',seg)
        out.append({'head':h.group(1),'len':len(seg),'start':segc[:350],'hits':[re.sub(r'\s+',' ',seg[max(0,p-350):p+350]) for p in hits[:3]]})
for o in out:
    print('=====',o['head'],o['len']); print(o['start']);
    for x in o['hits']: print('  >>',x)
