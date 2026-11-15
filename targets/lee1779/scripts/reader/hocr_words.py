"""Word-level dump of an IA hOCR file: leaf, x0, y0, x1, y1, pageW, pageH, word (TSV)."""
import re, sys, html
s=open(sys.argv[1],encoding='utf8').read()
for p in re.split(r"(?=<div class=['\"]ocr_page['\"])", s):
    m=re.search(r"id=['\"]page_(\d+)['\"]",p)
    if not m: continue
    leaf=int(m.group(1))-1
    pb=re.search(r"bbox (\d+) (\d+) (\d+) (\d+)",p); W,H=int(pb.group(3)),int(pb.group(4))
    for wm in re.finditer(r"<span class=['\"]ocrx_word['\"][^>]*title=['\"]bbox (\d+) (\d+) (\d+) (\d+)[^'\"]*['\"][^>]*>(.*?)</span>",p,re.S):
        x0,y0,x1,y1=map(int,wm.groups()[:4]); t=html.unescape(re.sub('<[^>]+>','',wm.group(5))).replace('\t',' ').strip()
        if t: print(f"{leaf}\t{x0}\t{y0}\t{x1}\t{y1}\t{W}\t{H}\t{t}")
