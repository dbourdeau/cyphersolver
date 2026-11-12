"""Daniel's 95% rule on a (b) reading file, by token, using measure_read.py's word test (es-golden-age, THRESH -4.5):
sure = word read as sense with no tentative value; probable = word read as sense with a tentative [x=v] value;
restored = none written in this re-read; unresolved = open groups [x] and letters without sense.
usage (from targets/sessa1523/dudout): python scripts/count95.py ../../sessa1524 reading_b.txt ..."""
import sys, re, os, io, contextlib
sys.argv, args = sys.argv[:1], sys.argv[1:]
sys.path.insert(0, args[0]); import measure_read as M  # targets/sessa1524/measure_read.py
def classes(path):
    m = M.lm.load('es-golden-age'); V = M.vocab(); words = []
    for ln in open(path, encoding='utf-8'):
        mm = re.match(r'\s*\d+[bd]\s+(.*)', ln)
        if not mm: continue
        ws = M.words_of(mm.group(1))
        if ws and words and words[-1].endswith('-') and ws[0].startswith('-') and not words[-1].startswith('{'):
            words[-1] = words[-1] + ws.pop(0)
        words.extend(ws)
    c = dict(sure=0, probable=0, restored=0, unresolved=0)
    for w in words:
        if w.startswith('{'):
            c['unresolved'] += len([p for p in re.split(r'[\s-]+', w.strip('{}')) if p]); continue
        pieces = [p for p in re.split(r'-(?![^\[]*\])', w) if p]; n = len(pieces)
        if not n: continue
        g = re.findall(r'\[([^\]]*)\]', w)
        if any('=' not in x for x in g): c['unresolved'] += n; continue
        word = re.sub(r'\[[^=\]]*=([^\]]*)\]', r'\1', w)
        word = re.sub(r'[^A-Za-zÀ-ÿñÑçÇ ]', '', word.replace('-', '')).replace('ç', 'c').replace('ñ', 'n')
        if not word: continue
        word = re.sub(r'n(?=[pb])', 'm', word.lower()).replace('embi', 'envi')
        ok = m.per_char(M.lm.norm(' ' + word + ' ', 'early')) >= M.THRESH or all(M.ortho(x) in V for x in word.split())
        c['probable' if ok and g else 'sure' if ok else 'unresolved'] += n
    return c
for p in args[1:]:
    c = classes(p); t = sum(c.values())
    print(f"{os.path.basename(p)}: tokens {t}; sure {c['sure']}; probable {c['probable']}; restored {c['restored']}; "
          f"unresolved {c['unresolved']}; read (sure+probable) {(c['sure']+c['probable'])/t:.1%}")
