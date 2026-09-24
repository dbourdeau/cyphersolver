"""Hundred-and-eightieth registered prediction set (PREDICTIONS.md, DK1-DK7): decipherment loop 5. Depiction keys (the
word for what a sign depicts, per Fairservis's identifications) in Dravidian, Sanskrit and Sumerian, under the
substitution test of set 179. Writes results/predict_test180.md."""
import csv
import os
import re

import predict_test13 as T
import rtools as R
from equation_rebus import lexicon_mw
from predict_test179 import M, subst_pairs, test
from signs import load

SP = os.environ.get('LANG_DATA', 'C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher--claude-worktrees-florence-1414-'
                    'cipher-160632/03a95ee0-e290-45c7-bab7-1e38cbd68d34/scratchpad')
SKIP = {'a', 'an', 'the', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'one', 'pair', 'of'}


def concepts():
    out = {}
    for r in csv.DictReader((l for l in open(os.path.join(R.HERE, 'keys', 'fairservis1992_raw.tsv'), encoding='utf-8') if not l.startswith('#')), delimiter='\t'):
        if r['confidence'] in ('sure', 'likely') and r['icit']:
            ident = re.sub(r'\([^)]*\)', ' ', r['gloss'].split('=>')[0]).lower()
            words = [w for w in re.findall(r'[a-z]+', ident) if w not in SKIP]
            if words and words[0] != 'combination':
                out.setdefault(r['icit'].split('|')[0], words[0])
    return out


def pick(lex, concept):
    pat = re.compile(r'^\s*((m|f|n|mfn|ind|adj)\.\s*)*(a |an |the |to )?' + re.escape(concept) + r's?\b')
    for w, g in lex:
        if pat.search(g):
            return w
    return None


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-eightieth registered predictions: decipherment loop 5, depiction keys by language', 'predict_test180')
    con = concepts()
    dra = []
    for r in csv.DictReader(open(os.path.join(SP, 'drav', 'dedr_entry_v11.csv'), encoding='utf-8')):
        f = r['entry_str'].split('(')[0].split(',')[0].strip().strip('-').strip(')')
        f = f.split()[0] if f.split() else ''
        if f:
            dra.append((f, r['entry_meaning'].lower().strip()))
    sa = lexicon_mw(os.path.join(SP, 'skt', 'mw.txt'))
    sux = [(r['cf'], (r['gw'] + ' | ' + r['senses']).lower()) for r in csv.DictReader(open(os.path.join(SP, 'sux', 'sux_gloss.tsv'), encoding='utf-8'), delimiter='\t')]
    keys = {}
    for lab, lex in (('Dravidian', dra), ('Sanskrit', sa), ('Sumerian', sux)):
        keys[lab] = {g: v for g, c in con.items() for v in [pick(lex, c)] if v}
        rd.say('- %s depiction key: %d of %d signs (e.g. %s).' % (lab, len(keys[lab]), len(con), ', '.join('%s %s=%s' % (g, con[g], keys[lab][g]) for g in list(keys[lab])[:6])))
    rd.say()
    lexf = lambda g: g not in R.NUMS and g not in M
    bodies = lambda lines: sorted({b for b, e in T.names(lines) if b})
    pa = subst_pairs(bodies(A), lexf)
    pb = subst_pairs(bodies(sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln})), lexf)
    res = {}
    passed = []
    for key_id, lab in (('DK1', 'Dravidian'), ('DK2', 'Sanskrit'), ('DK3', 'Sumerian')):
        oa, ma, na, qa = test(pa, keys[lab])
        ob, mb, nb, qb = test(pb, keys[lab])
        op, mp, npp, qp = test(pa + pb, keys[lab])
        res[lab] = (op - mp if op is not None else float('-inf'), npp)
        ok = oa is not None and ob is not None and qa < 0.05 and qb < 0.05 and na >= 10 and nb >= 10
        if ok:
            passed.append(lab)
        fmt = lambda o, m, n, q: 'none' if o is None else '%.3f vs %.3f, %d pairs, p = %.4f' % (o, m, n, q)
        rd.rec(key_id, '%s depiction key' % lab, 'A: %s; B: %s; pooled: %s' % (fmt(oa, ma, na, qa), fmt(ob, mb, nb, qb), fmt(op, mp, npp, qp)), ok)
    rd.rec('DK4', 'Dravidian above Sanskrit', 'excess %.3f against %.3f' % (res['Dravidian'][0], res['Sanskrit'][0]), res['Dravidian'][0] > res['Sanskrit'][0])
    rd.rec('DK5', 'Dravidian above Sumerian', 'excess %.3f against %.3f' % (res['Dravidian'][0], res['Sumerian'][0]), res['Dravidian'][0] > res['Sumerian'][0])
    rd.rec('DK6', 'a language passes on both samples', 'passed: %s' % (', '.join(passed) or 'none'), bool(passed))
    rd.rec('DK7', 'the test has power', 'pooled keyed pairs: %s' % ', '.join('%s %d' % (k, v[1]) for k, v in res.items()), all(v[1] >= 10 for v in res.values()))
    rd.finish()


if __name__ == '__main__':
    main()
