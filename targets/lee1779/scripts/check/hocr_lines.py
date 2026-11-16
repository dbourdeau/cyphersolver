# Dump hOCR into per-leaf line records: leaf, x0,y0,x1,y1, text
import re, sys, html
src, out = sys.argv[1], sys.argv[2]
t = open(src, encoding='utf-8', errors='replace').read()
pages = re.split(r"<div class=['\"]ocr_page['\"]", t)[1:]
with open(out, 'w') as f:
    for leaf, p in enumerate(pages):
        m = re.search(r"bbox (\d+) (\d+) (\d+) (\d+)", p)
        W, H = int(m.group(3)), int(m.group(4))
        for lm in re.finditer(r"<span class=['\"]ocr_line['\"][^>]*title=['\"]bbox (\d+) (\d+) (\d+) (\d+)[^>]*>(.*?)</span>\s*(?=<span class=['\"]ocr_line|</p>|</div>)", p, re.S):
            words = []
            for wm in re.finditer(r"<span class=['\"]ocrx_word['\"][^>]*title=['\"]bbox (\d+) (\d+) (\d+) (\d+)[^>]*>(.*?)</span>", lm.group(5), re.S):
                words.append((int(wm.group(1)), int(wm.group(2)), int(wm.group(3)), int(wm.group(4)), html.unescape(re.sub('<[^>]+>', '', wm.group(5)))))
            if not words: continue
            # split OCR line into segments if big x gap (two columns merged)
            words.sort()
            segs = [[words[0]]]
            for w in words[1:]:
                if w[0] - segs[-1][-1][2] > W * 0.06: segs.append([w])
                else: segs[-1].append(w)
            for s in segs:
                x0 = min(w[0] for w in s); y0 = min(w[1] for w in s); x1 = max(w[2] for w in s); y1 = max(w[3] for w in s)
                f.write(f"{leaf}\t{W}\t{H}\t{x0}\t{y0}\t{x1}\t{y1}\t{' '.join(w[4] for w in s)}\n")
