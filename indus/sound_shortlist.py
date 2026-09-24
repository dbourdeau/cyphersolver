"""A shortlist of candidate sound signs, from freedom (PREDICTIONS.md eighth and eleventh sets), with its precision
calibrated on Linear B.

Freedom = residual of log(distinct left/right neighbours) on log(tokens) (predict_test11.freedom), z-scored within a
source. Three independent sources: home seals and home tablets of the fuller ICIT corpus, and the M77-added texts.
Rule: a sign (not a numeral, opener or ending) scored in 2+ sources with z > 0 in every source that scores it;
ranked by mean z.

Calibration: the same rule on Linear B with Knossos and Pylos as the two sources; precision = share of the signs it
selects that are syllabograms, against the share of syllabograms among all signs scored.

This is a derived list, not a test: it ranks candidates for sound values; it gives no values.

Usage: python sound_shortlist.py path/to/icit_full_records_indusscript_net.csv path/to/linb
Writes results/sound_shortlist.md.
"""
import csv
import os
import sys
from collections import Counter

import icit_full
from gulf import IRAN_WEST, WEST
from numerals import NUMS
from predict_test8 import bound_pairs
from predict_test11 import freedom, linb_lines
from signs import load

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
LEAVE = {'740', '520', '817', '820', '861'}


def say(s=''):
    OUT.append(s)
    print(s)


def z(f):
    v = list(f.values())
    m = sum(v) / len(v)
    sd = (sum((x - m) ** 2 for x in v) / len(v)) ** 0.5
    return {g: (x - m) / sd for g, x in f.items()}


def sided(lines, min_tok=5):
    """Left and right freedom separately: residual of log(distinct left / right neighbours) on log(tokens)."""
    import math
    from collections import defaultdict
    tok = Counter(g for t in lines for g in t)
    L, R = defaultdict(set), defaultdict(set)
    for t in lines:
        for a, b in zip(t, t[1:]):
            R[a].add(b)
            L[b].add(a)
    out = []
    for nb in (L, R):
        sg = [g for g in tok if tok[g] >= min_tok]
        xs = [math.log(tok[g]) for g in sg]
        ys = [math.log(max(1, len(nb[g]))) for g in sg]
        mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
        sl = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
        out.append({g: y - (my + sl * (x - mx)) for g, x, y in zip(sg, xs, ys)})
    return out


def rule(zs):
    out = {}
    for g in set().union(*zs):
        sc = [s[g] for s in zs if g in s]
        if len(sc) >= 2 and all(x > 0 for x in sc):
            out[g] = sum(sc) / len(sc)
    return out


def main(path, linb):
    # calibration on Linear B, Knossos and Pylos as two sources
    import re
    srcs = {'KN': [], 'PY': []}
    for ln in open(os.path.join(linb, 'corpus_damos_lines.txt'), encoding='utf-8'):
        site = ln[:2]
        if site in srcs:
            srcs[site].append(ln)
    kinds = {}
    zl = []
    tmp = os.path.join(HERE, 'results', '_linb_tmp')
    os.makedirs(tmp, exist_ok=True)
    for site, lns in srcs.items():
        with open(os.path.join(tmp, 'corpus_damos_lines.txt'), 'w', encoding='utf-8') as f:
            f.writelines(lns)
        ll = linb_lines(tmp)
        for t in ll:
            for k, s in t:
                kinds.setdefault(s, k)
        zl.append(z({g: v for g, v in freedom([[s for _, s in t] for t in ll]).items() if g != 'N'}))
    scored = set().union(*zl)
    sel = rule(zl)
    base = sum(kinds[g] == 'syl' for g in scored) / len(scored)
    prec = sum(kinds[g] == 'syl' for g in sel) / len(sel)
    top20 = sorted(sel, key=lambda g: -sel[g])[:20]
    say('# Candidate sound signs')
    say()
    say('## Calibration on Linear B (Knossos and Pylos as two sources)')
    say()
    say('- signs scored: %d (%.0f%% syllabograms). Selected by the rule: %d, of which %.0f%% syllabograms; of the top '
        '20, %d.' % (len(scored), 100 * base, len(sel), 100 * prec, sum(kinds[g] == 'syl' for g in top20)))
    allb = []
    for lns in srcs.values():
        with open(os.path.join(tmp, 'corpus_damos_lines.txt'), 'w', encoding='utf-8') as f:
            f.writelines(lns)
        allb += [[x for _, x in t] for t in linb_lines(tmp)]
    os.remove(os.path.join(tmp, 'corpus_damos_lines.txt'))
    lf, rf = sided(allb)
    both = [g for g in sel if lf.get(g, -1) > 0 and rf.get(g, -1) > 0]
    one = [g for g in sel if g not in both]
    say('- of the selected, free on both sides (left and right residual > 0): %d, %.0f%% syllabograms; free on one '
        'side only: %d, %.0f%% syllabograms.' % (len(both), 100 * sum(kinds[g] == 'syl' for g in both) / max(1, len(both)),
                                                len(one), 100 * sum(kinds[g] == 'syl' for g in one) / max(1, len(one))))
    say('- syllabograms the rule misses: %d of %d.' % (
        sum(1 for g in scored if kinds[g] == 'syl' and g not in sel), sum(1 for g in scored if kinds[g] == 'syl')))
    os.rmdir(tmp)
    say()

    # Indus
    recs = {rec[0]: rec for rec in icit_full.records(path)}
    rows = [r for r in icit_full.objects(path, intact_only=True) if r['seq']]
    west = {r['sealid'] for r in rows if recs[r['sealid']][2] in WEST or r['site'] in IRAN_WEST}
    home = [r for r in rows if r['sealid'] not in west and recs[r['sealid']][2] not in ('Other',)]
    lines_of = lambda rs: [ln for r in rs for ln in r['seq'] if len(ln) >= 2]
    src = {'seals': freedom(lines_of([r for r in home if r['type'].startswith('SEAL')])),
           'tablets': freedom(lines_of([r for r in home if r['type'].startswith('TAB')])),
           'M77': freedom([ln for r in load(only_m77=True) for ln in r['seq'] if len(ln) >= 2 and '?' not in ln])}
    lfi, rfi = sided(lines_of(home) + [ln for r in load(only_m77=True) for ln in r['seq'] if len(ln) >= 2 and '?' not in ln])
    drop = LEAVE | set(NUMS)
    zs = {k: z({g: v for g, v in f.items() if g not in drop}) for k, f in src.items()}
    sel = rule(list(zs.values()))
    scored = set().union(*zs.values())
    info = {r['sign']: r for r in csv.DictReader(open(os.path.join(HERE, 'results', 'sign_list.tsv'), encoding='utf-8'),
                                                 delimiter='\t')}
    bp = bound_pairs(path)
    inbp = Counter(g for p in bp for g in p)
    wa = Counter(g for r in rows if r['sealid'] in west for ln in r['seq'] for g in ln)
    say('## Indus')
    say()
    say('- signs scored (not numerals, openers or endings): %d; selected: %d (%.0f%%). At the Linear B precision about '
        '%.0f of them would be sound signs, if the Indus script mixes the two kinds as Linear B does.' % (
            len(scored), len(sel), 100 * len(sel) / len(scored), prec * len(sel)))
    say()
    say('| rank | sign | mean z | seals | tablets | M77 | tokens | role | Fairservis label | in bound pairs | West Asian uses | free left / right |')
    say('|---|---|---|---|---|---|---|---|---|---|---|---|')
    for i, g in enumerate(sorted(sel, key=lambda g: -sel[g]), 1):
        inf = info.get(g, {})
        say('| %d | %s | %+.2f | %s | %s | %s | %s | %s | %s | %s | %d | %s |' % (
            i, g, sel[g], *['%+.2f' % zs[k][g] if g in zs[k] else '-' for k in ('seals', 'tablets', 'M77')],
            inf.get('tokens', '-'), inf.get('role', '-'), inf.get('fairservis', '') or '-', inbp[g] or '-', wa[g],
            '%+.2f / %+.2f%s' % (lfi.get(g, 0), rfi.get(g, 0), ' both' if lfi.get(g, 0) > 0 and rfi.get(g, 0) > 0 else '')))
    say()
    say('Least free (candidate word signs), by mean z, scored in 2+ sources and below 0 in all: ' + ', '.join(
        '%s (%s)' % (g, info.get(g, {}).get('fairservis', '') or '-') for g in sorted(
            (g for g in scored if sum(g in s for s in zs.values()) >= 2 and all(s[g] < 0 for s in zs.values() if g in s)),
            key=lambda g: sum(s[g] for s in zs.values() if g in s) / sum(g in s for s in zs.values()))[:20]) + '.')
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'sound_shortlist.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
