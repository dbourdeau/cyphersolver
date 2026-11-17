"""Find a regex in the Omont OCR (archive.org p1cataloguegnr02-04 djvu text, kept outside the repo) and print, for each hit,
the nearest heading line above (OCR digits, unreliable), the closing '(Anc. N.)' below, and the hit line.
python -I -X utf8 ocrctx.py <omont_dir> <regex>"""
import sys, re, os, glob
d, pat = sys.argv[1], re.compile(sys.argv[2], re.I)
H = re.compile(r'^\s*([0-9oOlISB]{4}[a-z]?)(?:\s+(?:et|à)\s+[0-9oOlISB]{4})?\.\s*$')
for f in sorted(glob.glob(os.path.join(d, 't0*.txt'))):
    L = open(f, encoding='utf8').read().split('\n')
    heads = [(i, m.group(1)) for i, l in enumerate(L) if (m := H.match(l))]
    for i, l in enumerate(L):
        if pat.search(l):
            hb = [h for h in heads if h[0] < i][-1:] or [(0, '?')]
            anc = next((L[j].strip() for j in range(i, min(i + 800, len(L))) if re.search(r'\((?:Anc|Ane|Ano)[.,]', L[j])), '?')
            prevanc = next((L[j].strip() for j in range(i, max(0, i - 1500), -1) if re.search(r'\((?:Anc|Ane|Ano)[.,]', L[j])), '?')
            print(f'{os.path.basename(f)}:{i+1} heading-above {hb[0][1]} (line {hb[0][0]+1}) | prev-close {prevanc[-30:]} | next-close {anc[-30:]}')
            print('    ', ' '.join(L[i:i+3])[:220])
