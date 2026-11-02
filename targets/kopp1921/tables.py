"""Find the 'table' family: 4-figure groups of the shape 11xx-13xx or d0xx."""
import json,re,collections,sys
sys.stdout.reconfigure(encoding='utf-8')
fr=[]
for l in open('targets/kopp1921/ocr_frames.jsonl',encoding='utf-8'):
    r=json.loads(l)
    t=r['text']
    toks=re.findall(r'\b[0-9IlOo]{4}\b',t)
    toks=[x.replace('I','1').replace('l','1').replace('O','0').replace('o','0') for x in toks]
    if len(toks)<8: continue
    sh=sum(1 for x in toks if re.fullmatch(r'1[0-5]\d\d|\d0\d\d',x))/len(toks)
    d=re.findall(r'(JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER)\s+\d+',t)
    fr.append((round(sh,2),len(toks),r['file'][5:-4],d[:1]))
for x in sorted(fr,reverse=True)[:40]: print(x)
