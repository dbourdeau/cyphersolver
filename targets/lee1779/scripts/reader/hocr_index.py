"""Dump every OCR line of an IA hOCR file as TSV: leaf, col(a/b by x0 vs page mid), y0, x0, x1, text."""
import re, sys, html
path=sys.argv[1]
s=open(path,encoding='utf8').read()
for p in re.split(r"(?=<div class=['\"]ocr_page['\"])", s):
    m=re.search(r"id=['\"]page_(\d+)['\"]",p)
    if not m: continue
    leaf=int(m.group(1))-1
    pb=re.search(r"bbox (\d+) (\d+) (\d+) (\d+)",p); W=int(pb.group(3))
    for lm in re.finditer(r"<span class=['\"]ocr_(?:line|caption|textfloat|header)['\"][^>]*title=['\"]bbox (\d+) (\d+) (\d+) (\d+)[^'\"]*['\"][^>]*>(.*?)</span>\s*(?=<span class=['\"]ocr_|</p>)",p,re.S):
        x0,y0,x1,y1=map(int,lm.groups()[:4])
        words=re.findall(r"<span class=['\"]ocrx_word['\"][^>]*>(.*?)</span>",lm.group(5),re.S)
        t=html.unescape(' '.join(re.sub('<[^>]+>','',w) for w in words)).replace('\t',' ')
        print(f"{leaf}\t{'a' if x0<W*0.45 else 'b'}\t{y0}\t{x0}\t{x1}\t{W}\t{t}")
