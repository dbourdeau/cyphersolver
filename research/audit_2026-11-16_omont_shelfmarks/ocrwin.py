"""Cipher items in the Omont OCR whose 4-line window matches a keyword: python -I -X utf8 ocrwin.py <omont_dir> <kw-regex>"""
import sys, re, os, glob
d, kw = sys.argv[1], re.compile(sys.argv[2], re.I)
C = re.compile(r'chiffr|chifl|chifr', re.I)
H = re.compile(r'^\s*([0-9oOlISB]{4}[a-z]?)(?:\s+(?:et|à)\s+[0-9oOlISB]{4})?\.\s*$')
for f in sorted(glob.glob(os.path.join(d, 't0*.txt'))):
    L = open(f, encoding='utf8').read().split('\n')
    heads = [(i, m.group(1)) for i, l in enumerate(L) if (m := H.match(l))]
    done = set()
    for i, l in enumerate(L):
        if C.search(l):
            w = ' '.join(x.strip() for x in L[max(0, i - 3):i + 3])
            if kw.search(w) and not done & set(range(i - 4, i + 1)):
                done.add(i)
                hb = [h for h in heads if h[0] < i][-1:] or [(0, '?')]
                anc = next((L[j].strip()[-28:] for j in range(i, min(i + 1500, len(L))) if re.search(r'\((?:Anc|Ane|Ano)[.,]', L[j])), '?')
                prev = next((L[j].strip()[-28:] for j in range(i, max(0, i - 2500), -1) if re.search(r'\((?:Anc|Ane|Ano)[.,]', L[j])), '?')
                sys.stdout.buffer.write(f'{os.path.basename(f)}:{i+1} head {hb[0][1]} | prev {prev} | next {anc}\n     {re.sub(chr(32)+"+"," ",w)[:300]}\n'.encode('utf8'))
