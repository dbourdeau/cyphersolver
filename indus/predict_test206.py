"""Two-hundred-and-sixth registered prediction set (PREDICTIONS.md, KY1-KY5): decipherment loop 31, the published Indus
keys through the gate-validated character-LM scorer (lmkey.py, set 205), in their claimed language and the two
others. Writes results/predict_test206.md."""
import csv
import glob
import os
import re
import unicodedata
from collections import Counter

import bench
import lang_names as L
import rtools as R
from equation_rebus import lexicon_mw
from linb_control import adjust
from lmkey import CharLM, score
from predict_test205 import LB, lb_lines
from progress import data

ORDER = 5


def plain(s):
    s = unicodedata.normalize('NFKD', s.lower())
    return re.sub(r'[^a-z]', '', ''.join(c for c in s if not unicodedata.combining(c)))


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-sixth registered predictions: decipherment loop 31, the published keys through the validated scorer', 'predict_test206')
    words = {'sa': [plain(a) for a, _ in lexicon_mw(os.path.join(L.SP, 'skt', 'mw.txt'))],
             'dra': [plain(r['Form'].strip().strip('-')) for r in csv.DictReader(open(os.path.join(L.SP, 'drav', 'forms.csv'), encoding='utf-8'))],
             'sux': [plain(r['cf']) for r in csv.DictReader(open(os.path.join(L.SP, 'sux', 'sux_gloss.tsv'), encoding='utf-8'), delimiter='\t')]}
    lms = {k: CharLM([w for w in v if w], ORDER) for k, v in words.items()}
    rd.say('- word lists (plain a-z): %s.' % ', '.join('%s %d' % (k, len([w for w in v if w])) for k, v in words.items()))
    DL, tr, te = data()
    freq = Counter(g for t in DL for g in t)
    keys = []
    for p in sorted(glob.glob(os.path.join(R.HERE, 'keys', '*.tsv'))):
        if p.endswith(('_raw.tsv', '_wide.tsv')):
            continue
        meta, key, gloss = bench.load_key(p)
        keys.append((os.path.basename(p), meta.get('lang', '?'), key))
    ym, yk, _ = bench.load_yajnadevam(os.path.join(L.SP, 'yaj', 'xlits.csv'))
    keys.append(('yajnadevam2024', 'sa', yk))
    rd.say()
    rows = []
    for name, lang, key in keys:
        k2 = {g: plain(v) for g, v in key.items() if plain(v)}
        shuf = list(bench.shuffles(k2, freq, n=100, band=10))
        res = {}
        for lg, lm in lms.items():
            real = score(DL, k2, lm)
            sims = sorted(score(DL, s, lm) for s in shuf)
            res[lg] = (real, sims[50], sum(1 for x in sims if x >= real))
        rows.append((name, lang, len(k2), res))
        rd.say('- %s (claimed %s, %d signs): %s.' % (name, lang, len(k2), '; '.join('%s real %.3f, median %.3f, %d of 100 as good' % (lg, *v) for lg, v in res.items())))
    rd.say()
    passed = [(n, lg, r) for n, lg, k, r in rows if lg in r and r[lg][2] <= 5]
    rd.rec('KY1', 'a published key beats 95 of 100 shuffles in its claimed language', 'passing: %s' % (', '.join(n for n, lg, r in passed) or 'none'), bool(passed))
    spec = [n for n, lg, r in passed if all(r[o][2] > 5 for o in r if o != lg)]
    rd.rec('KY2', 'passing keys are language-specific', 'specific: %s' % (', '.join(spec) or 'none'), bool(passed) and len(spec) == len(passed))
    best = [(n, lg, max(r, key=lambda o: r[o][0] - r[o][1])) for n, lg, k, r in rows if lg in r]
    ok3 = sum(1 for n, lg, b in best if b == lg)
    rd.rec('KY3', 'margin largest in the claimed language for most keys', '%d of %d (%s)' % (ok3, len(best), ', '.join('%s: %s' % (n, b) for n, lg, b in best)), ok3 > len(best) / 2)
    lines, lbk = lb_lines()
    lbf = Counter(s for t in lines for s in t)
    even = lines[0::2]
    gk = [plain(adjust(w.strip())) for w in open(os.path.join(LB, 'greek', 'greek_translit_wordlist.txt'), encoding='utf-8') if w.strip()]
    glm = CharLM([w for w in gk if w], ORDER)
    lbk2 = {g: plain(v) for g, v in lbk.items()}
    real = score(even, lbk2, glm)
    sims = sorted(score(even, s, glm) for s in bench.shuffles(lbk2, lbf, n=100, band=10))
    ge = sum(1 for x in sims if x >= real)
    rd.rec('KY4', 'the a-z reduction keeps the Linear B gate', "Ventris's key %.3f; shuffles median %.3f; %d of 100 as good" % (real, sims[50], ge), ge <= 5)
    rd.rec('KY5', 'progress rule', 'KY1 %s, KY2 %s' % (bool(passed), bool(passed) and len(spec) == len(passed)), bool(passed) and len(spec) == len(passed))
    rd.finish()


if __name__ == '__main__':
    main()
