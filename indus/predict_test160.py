"""Hundred-and-sixtieth registered prediction set (PREDICTIONS.md, RP1-RP10): the new findings on independent samples
(M77 additions, Harappa moulded tablets, Linear B inside Knossos, Ur III Umma against Nippur, Gujarat seals).
Writes results/predict_test160.md."""
import csv
import json
import os
import random
from collections import Counter, defaultdict

import predict_test13 as T
import rtools as R
import ur3_seals
from predict_test103 import CL
from predict_test112 import runs
from predict_test147 import chapman
from predict_test152 import LINB, classes
from predict_test157 import kind, profile
from predict_test18 import level
from signs import load

random.seed(180)
M = set(R.END) | set(CL) | {'400', '90'}


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-sixtieth registered predictions: the new findings on independent samples', 'predict_test160')
    rows = [r for r in load(only_m77=True) if r['site'] in ('Mohenjo-daro', 'Harappa')]
    names = sorted({(b, e) for b, e in T.names([ln for r in rows for ln in r['seq']]) if b})
    n5 = [b[-1] for b, e in names if e == '520']
    n7 = [b[-1] for b, e in names if e == '740']
    win = sum(len(set(random.sample(n7, len(n5)))) > len(set(n5)) for _ in range(1000)) if len(n7) >= len(n5) else 0
    rd.thr('RP1', 'B: 520 is narrow', '740 draws of %d names with more heads than 520 (%d)' % (len(n5), len(set(n5))), win, 1000, 0.95)
    lex = lambda g: g not in R.NUMS and g not in M
    vals = {c: defaultdict(Counter) for c in ('Mohenjo-daro', 'Harappa')}
    for r in rows:
        for ln in r['seq']:
            for i, j, rr in runs(ln):
                if j < len(ln) and lex(ln[j]):
                    vals[r['site']][ln[j]][sum(R.NUMS[g][0] for g in rr)] += 1
    sh = [x for x in vals['Mohenjo-daro'] if x in vals['Harappa']]
    same = sum(vals['Mohenjo-daro'][x].most_common(1)[0][0] == vals['Harappa'][x].most_common(1)[0][0] for x in sh)
    rd.rec('RP2', 'B: numeral values are local', 'signs counted in both cities %d; same commonest value %d (%.0f%%); threshold under 70%%' % (
        len(sh), same, 100 * same / max(1, len(sh))), len(sh) > 0 and same / len(sh) < 0.7)
    cat = {'names': {c: Counter() for c in vals}, 'heads': {c: Counter() for c in vals}}
    for r in rows:
        for b, e in {x for x in R.names_in(r) if x[0]}:
            cat['names'][r['site']][(b, e)] += 1
            cat['heads'][r['site']][b[-1]] += 1
    pn, ph = profile(cat['names']), profile(cat['heads'])
    rd.rec('RP3', 'B: names are open', 'names %s; estimate/observed %.2f; threshold 3' % (pn['n'], pn['ratio']), pn['ratio'] >= 3)
    rd.rec('RP4', 'B: heads are closed', 'heads %s; estimate/observed %.2f; threshold at most 1.5' % (ph['n'], ph['ratio']), ph['ratio'] <= 1.5)
    mt = {'E': Counter(), 'L': Counter()}
    for r in F:
        if recs[r['sealid']][3] == 'Harappa' and r['type'] in ('TAB:B', 'TAB:I'):
            lv = level('Harappa', recs[r['sealid']])
            if lv:
                mt[lv][tuple(r['flat'])] += 1
    pm = profile(mt)
    rd.rec('RP5', 'moulded tablets are closed sets', 'early %d / late %d texts, shared %d; %.2f, %.2f, %.2f -> %s' % (
        pm['n'][0], pm['n'][1], pm['n'][2], pm['ratio'], pm['shared'], pm['one'], kind(pm)), kind(pm) == 'title-like')
    series = {}
    for ln in open(os.path.join(LINB, 'corpus_damos_documents.jsonl'), encoding='utf-8'):
        d = json.loads(ln)
        if d['site'] == 'Knossos':
            series[d['id']] = 'D' if (d.get('series') or '').startswith('D') else 'other'
    per, tit = classes()
    kc = {'persons': {'D': Counter(), 'other': Counter()}, 'titles': {'D': Counter(), 'other': Counter()}}
    seen = set()
    with open(os.path.join(LINB, 'corpus_damos_words.tsv'), encoding='utf-8') as f:
        for r in csv.DictReader(f, delimiter='\t'):
            s = series.get(r['doc_id'])
            if s and r['status'] == 'complete' and r['uncertain'] == '0' and r['erased'] == '0' and r['badsign'] == '0':
                if (r['doc_id'], r['word']) in seen:
                    continue
                seen.add((r['doc_id'], r['word']))
                if r['word'] in per:
                    kc['persons'][s][r['word']] += 1
                elif r['word'] in tit:
                    kc['titles'][s][r['word']] += 1
    pp, pt = profile(kc['persons']), profile(kc['titles'])
    rd.rec('RP6', 'Linear B persons inside Knossos', 'D / other %s; %.2f, %.2f, %.2f -> %s' % (pp['n'], pp['ratio'], pp['shared'], pp['one'], kind(pp)), kind(pp) == 'person-like')
    rd.rec('RP7', 'Linear B titles inside Knossos', 'D / other %s; %.2f, %.2f, %.2f -> %s' % (pt['n'], pt['ratio'], pt['shared'], pt['one'], kind(pt)), kind(pt) == 'title-like')
    U = ur3_seals.load()
    legends = {}
    for (text, seal), o in U.items():
        legends.setdefault(tuple(tuple(ln) for ln in o['lines']), set()).add(o['site'])
    uc = {'owner': {'Umma': Counter(), 'Nippur': Counter()}, 'legend': {'Umma': Counter(), 'Nippur': Counter()}}
    for lg, ss in legends.items():
        own = next((cf for cf, pos in lg[0] if pos == 'PN'), None) if lg else None
        for s in ss:
            if s in ('Umma', 'Nippur'):
                if own:
                    uc['owner'][s][own] += 1
                uc['legend'][s][lg] += 1
    po, pl = profile(uc['owner']), profile(uc['legend'])
    rd.rec('RP8', 'Ur III owners, Umma against Nippur', '%s; %.2f, %.2f, %.2f -> %s' % (po['n'], po['ratio'], po['shared'], po['one'], kind(po)), kind(po) == 'title-like')
    rd.rec('RP9', 'Ur III legends, Umma against Nippur', '%s; %.2f, %.2f, %.2f -> %s' % (pl['n'], pl['ratio'], pl['shared'], pl['one'], kind(pl)), kind(pl) == 'person-like')
    gj = {'Gujarat': Counter(), 'Mohenjo-daro': Counter()}
    for r in F:
        s = recs[r['sealid']][3]
        g = 'Gujarat' if s in ('Lothal', 'Dholavira') else (s if s == 'Mohenjo-daro' else None)
        if g and r['type'].startswith('SEAL'):
            for nm in {x for x in R.names_in(r) if x[0]}:
                gj[g][nm] += 1
    pg = profile(gj)
    rd.rec('RP10', 'Gujarat against Mohenjo-daro: names open', '%s; estimate/observed %.2f; threshold 3' % (pg['n'], pg['ratio']), pg['ratio'] >= 3)
    rd.finish()


if __name__ == '__main__':
    main()
