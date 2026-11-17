"""Extract lines per column from an Internet Archive hOCR file.
usage: python3 -I hocr_cols.py <hocr> <leaf> [<leaf>...]
Prints for each leaf: column (a/b), y, x, text, sorted top to bottom."""
import re, sys, html
path=sys.argv[1]; leaves=set(int(x) for x in sys.argv[2:])
s=open(path,encoding='utf8').read()
pages=re.split(r"(?=<div class=['\"]ocr_page['\"])", s)
for p in pages:
    m=re.search(r"id=['\"]page_(\d+)['\"]",p)
    if not m: continue
    leaf=int(m.group(1))-1
    if leaf not in leaves: continue
    pb=re.search(r"bbox (\d+) (\d+) (\d+) (\d+)",p); W=int(pb.group(3)); H=int(pb.group(4))
    out=[]
    for lm in re.finditer(r"<span class=['\"]ocr_line['\"][^>]*title=['\"]bbox (\d+) (\d+) (\d+) (\d+)[^'\"]*['\"][^>]*>(.*?)</span>\s*(?=<span class=['\"]ocr_line|</p>)",p,re.S):
        x0,y0,x1,y1=map(int,lm.groups()[:4])
        words=re.findall(r"<span class=['\"]ocrx_word['\"][^>]*>(.*?)</span>",lm.group(5),re.S)
        t=html.unescape(' '.join(re.sub('<[^>]+>','',w) for w in words))
        out.append((x0,y0,x1,y1,t))
    print(f"### leaf {leaf} size {W}x{H} lines {len(out)}")
    for x0,y0,x1,y1,t in sorted(out,key=lambda r:(0 if r[0]<W*0.48 else 1, r[1])):
        print(f"{'a' if x0<W*0.48 else 'b'}\t{y0}\t{x0}-{x1}\t{t}")
