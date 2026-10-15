"""Render each letter's transcription with the 2-digit runs replaced by their decipherment {in braces}
and code numbers annotated from codes_key.json when a value is known: 187<der Kayser>.
usage: python render.py [R7486 ...]  -> reading/R74xx.txt
"""
import json, os, re, sys, glob
from key import letter
HERE = os.path.dirname(os.path.abspath(__file__))
CK = os.path.join(HERE, 'codes_key.json')
codes = json.load(open(CK, encoding='utf-8')) if os.path.exists(CK) else {}

NUM = re.compile(r'(?<![\w^])(\d{1,3})(\?)?(?:\|\d+)?(\^\[[^\]]*\]|\^[a-zäöü/?]+)?(?!\w)')

def render_line(txt):
    # mark pairs / single digits in runs; 3-digit codes annotated
    toks = list(NUM.finditer(txt))
    out, last = [], 0
    i = 0
    while i < len(toks):
        t = toks[i]
        v = t.group(1)
        if len(v) in (1, 2) and letter(v):
            j = i; run = []
            while j < len(toks) and len(toks[j].group(1)) in (1, 2) and letter(toks[j].group(1)):
                gap = txt[toks[j - 1].end():toks[j].start()] if j > i else ''
                if j > i and re.search(r'[A-Za-zÄÖÜäöü]{2,}', gap): break
                run.append(toks[j]); j += 1
            if len(run) >= 2:
                out.append(txt[last:run[0].start()])
                plain = ''.join(letter(r.group(1)) for r in run)
                out.append(' '.join(r.group(1) for r in run) + ' {' + plain + '}')
                last = run[-1].end(); i = j; continue
        if len(v) == 3 and v in codes:
            out.append(txt[last:t.end()]); out.append('<' + codes[v] + '>'); last = t.end()
        i += 1
    out.append(txt[last:])
    return ''.join(out)

def main():
    recs = sys.argv[1:] or [os.path.basename(p)[:-4] for p in sorted(glob.glob(os.path.join(HERE, 'transcr', 'R*.txt')))]
    os.makedirs(os.path.join(HERE, 'reading'), exist_ok=True)
    for rec in recs:
        lines = open(os.path.join(HERE, 'transcr', rec + '.txt'), encoding='utf-8').read().splitlines()
        res = []
        for ln in lines:
            m = re.match(r'(\[P\w+ l\.\d+\]\s*)(.*)', ln)
            res.append(m.group(1) + render_line(m.group(2)) if m else ln)
        open(os.path.join(HERE, 'reading', rec + '.txt'), 'w', encoding='utf-8').write('\n'.join(res) + '\n')

if __name__ == '__main__':
    main()
