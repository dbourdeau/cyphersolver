"""Cross-tablet record linkage: the same entry words (mostly personal names) on different tablets.

Each entry of an administrative record is reduced to: its label word, the section it stands in (the last
KI-RO / KU-RO / heading word before it), the commodity that governs it (in the entry, or the last commodity
written before it in the record), its quantity, the record, site and scribe.

1. Series: records that share three or more entry words are linked; linked groups are 'series'. For each
   pair in a series, the quantities of the shared words are compared (equal, constant ratio, or neither).
2. Sections: for words that stand in a KI-RO section on one record and outside one elsewhere, the two
   quantities are listed, to see whether the KI-RO figure is a remainder of the other.
3. A null for series: entry words are permuted across all administrative entries of the same site (1,000 runs)
   and the number of record pairs sharing 3+ words recounted, so that shared lists are not an artefact of
   a few common words.
"""
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import combinations
import json
from pathlib import Path
import random
import re

ROOT = Path(__file__).resolve().parent.parent
READ = json.loads((ROOT / 'reading/reading.json').read_text(encoding='utf-8'))
ADMIN = {'Tablet', 'Lames (short thin tablet)', '3-sided bar', '4-sided bar', 'Label'}
TERMS = {'KI-RO', 'KU-RO', 'PO-TO-KU-RO'}


def entries():
    out = []
    for r in READ['records']:
        if r['support'] not in ADMIN:
            continue
        toks = r['tokens']
        section, commodity, heading = None, None, []
        by_entry = defaultdict(list)
        for t in toks:
            by_entry[t['entry']].append(t)
        for e in sorted(by_entry):
            ts = by_entry[e]
            com = [re.findall(r'[A-Z]{3,}', t['label'])[0] for t in ts if t['cls'] == 'commodity']
            if com:
                commodity = com[0]
            q = [t for t in ts if t['cls'] in ('number', 'fraction')]
            words = [t for t in ts if t['cls'] == 'word']
            terms = [t['label'] for t in ts if t['cls'] == 'term']
            anyq = [t for t in ts if t['cls'] in ('number', 'fraction', 'fraction-disputed', 'fraction-unvalued',
                                                    'quantity-mixed')]
            if terms and not anyq:
                section = terms[-1]
            for w in words:
                if w.get('function') == 'entry label':
                    out.append({'word': w['label'], 'record': r['name'], 'site': r['site'], 'scribe': r['scribe'],
                                'section': section or ('heading:' + heading[0] if heading else None),
                                'commodity': com[0] if com else commodity,
                                'quantity': str(sum((F(t['value']) for t in q), F(0))) if q else None,
                                'damaged': any(t['damaged'] for t in ts)})
                elif w.get('function') == 'heading' and not heading:
                    heading.append(w['label'])
            if terms and q and terms[-1] == 'KU-RO':
                section = None
    return out


def series(E, k=3):
    rec_words = defaultdict(set)
    for e in E:
        rec_words[e['record']].add(e['word'])
    pairs = [(a, b, rec_words[a] & rec_words[b]) for a, b in combinations(sorted(rec_words), 2)
             if len(rec_words[a] & rec_words[b]) >= k]
    return rec_words, pairs


def null_pairs(E, k, rng, reps):
    by_site = defaultdict(list)
    for i, e in enumerate(E):
        by_site[e['site']].append(i)
    counts = []
    for _ in range(reps):
        words = [e['word'] for e in E]
        for idx in by_site.values():
            vals = [words[i] for i in idx]
            rng.shuffle(vals)
            for i, v in zip(idx, vals):
                words[i] = v
        rw = defaultdict(set)
        for e, w in zip(E, words):
            rw[e['record']].add(w)
        counts.append(sum(1 for a, b in combinations(rw, 2) if len(rw[a] & rw[b]) >= k))
    return counts


def main(reps=1000, seed=20260923):
    E = entries()
    rng = random.Random(seed)
    rec_words, pairs = series(E)
    null = null_pairs(E, 3, rng, reps)
    q = {(e['record'], e['word']): e for e in E}
    comparisons = []
    for a, b, shared in pairs:
        rows = []
        for w in sorted(shared):
            ea, eb = q[(a, w)], q[(b, w)]
            rows.append({'word': w, a: ea['quantity'], b: eb['quantity'], 'section_' + a: ea['section'],
                         'section_' + b: eb['section'], 'commodity_' + a: ea['commodity'], 'commodity_' + b: eb['commodity']})
        ratios = {str(F(r[b]) / F(r[a])) for r in rows if r[a] not in (None, '0') and r[b] not in (None, '0')}
        comparisons.append({'records': [a, b], 'shared': len(shared), 'constant_ratio': ratios.pop() if len(ratios) == 1 else None,
                            'rows': rows})
    # KI-RO sections against the same word elsewhere
    kiro = defaultdict(list)
    for e in E:
        kiro[e['word']].append(e)
    kiro_cross = {w: [{k: x[k] for k in ('record', 'section', 'commodity', 'quantity', 'scribe')} for x in v]
                  for w, v in kiro.items() if any(x['section'] == 'KI-RO' for x in v) and len({x['record'] for x in v}) >= 2}
    recurring = {w: [{k: x[k] for k in ('record', 'site', 'scribe', 'section', 'commodity', 'quantity')} for x in v]
                 for w, v in kiro.items() if len({x['record'] for x in v}) >= 2}
    res = {'method': __doc__.strip(), 'entries': len(E), 'entry_words': len(kiro), 'recurring_words': len(recurring),
           'series_pairs': len(pairs), 'null_pairs_mean': round(sum(null) / reps, 2), 'null_pairs_max': max(null),
           'p_series': round((sum(n >= len(pairs) for n in null) + 1) / (reps + 1), 4),
           'series': comparisons, 'kiro_cross': kiro_cross, 'recurring': recurring}
    (ROOT / 'reading/prosopography_results.json').write_text(json.dumps(res, ensure_ascii=False, indent=1) + '\n',
                                                            encoding='utf-8')
    print(f"entries {len(E)}, entry words {len(kiro)}, recurring on 2+ records {len(recurring)}")
    print(f"record pairs sharing 3+ words: {len(pairs)} (null mean {res['null_pairs_mean']}, max {res['null_pairs_max']}, p {res['p_series']})")
    for c in comparisons:
        a, b = c['records']
        print(f"  {a} ~ {b}: {c['shared']} shared, ratio {c['constant_ratio']}")
        for r in c['rows']:
            print(f"     {r['word']:12} {r[a]!s:>6} [{r['section_' + a]}, {r['commodity_' + a]}]  {r[b]!s:>6} [{r['section_' + b]}, {r['commodity_' + b]}]")
    print('Words in a KI-RO section and elsewhere:')
    for w, v in kiro_cross.items():
        print(f"  {w:12}", [(x['record'], x['section'], x['commodity'], x['quantity']) for x in v])


if __name__ == '__main__':
    main()


def cross_site(reps=2000, seed=20260923, minlen=2):
    """Entry words (names) attested at two or more sites, against a null that permutes entry words across
    all administrative entries regardless of site, keeping each entry's site."""
    E = [e for e in entries() if len(e['word'].split('-')) >= minlen]
    def count(words):
        sites = defaultdict(set)
        for e, w in zip(E, words):
            sites[w].add(e['site'])
        return {w: s for w, s in sites.items() if len(s) >= 2}
    real = count([e['word'] for e in E])
    rng = random.Random(seed)
    null = []
    for _ in range(reps):
        ws = [e['word'] for e in E]
        rng.shuffle(ws)
        null.append(len(count(ws)))
    detail = {w: [{k: x[k] for k in ('record', 'site', 'scribe', 'section', 'commodity', 'quantity')}
                  for x in E if x['word'] == w] for w in sorted(real)}
    out = {'entries': len(E), 'sites': dict(Counter(e['site'] for e in E)), 'cross_site_words': len(real),
           'null_mean': round(sum(null) / reps, 2), 'p_le': round((sum(n <= len(real) for n in null) + 1) / (reps + 1), 4),
           'p_ge': round((sum(n >= len(real) for n in null) + 1) / (reps + 1), 4), 'detail': detail}
    (ROOT / 'reading/cross_site_results.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n',
                                                         encoding='utf-8')
    print('entries', len(E), out['sites'])
    print(f"entry words at 2+ sites: {len(real)} (null {out['null_mean']}; P(null<=real) {out['p_le']}, P(null>=real) {out['p_ge']})")
    for w, v in detail.items():
        print(f'  {w:12}', [(x['record'], x['commodity'], x['quantity'], x['section']) for x in v])
