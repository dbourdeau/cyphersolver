"""Linear A words in the Linear B record: how many, of what kind, and where.

Linear B vocabulary: every word type in the Linear B corpus of linearb.xyz (R. Hogan, commit 84e0b00),
with its sites, and the category of each headword in Chadwick & Ventris 1973 as carried by the tiripode
lexicon (MIT; commit 0c3c821): anthroponym, toponym, ethnic, theonym, other, or not in the glossary.
Linear A: distinct syllabic word types of the working corpus (transliteration with Linear B values).

Real exact matches are counted, then the Linear A sign values are shuffled within 10 frequency bins
(the same null as soundvalues.py) and matches recounted, overall, by category and by where the Linear B
word is attested: Knossos only (Crete), mainland only (Pylos, Thebes, Mycenae, Tiryns...), or both.
If Minoan names lived on in Mycenaean Crete, real matches should exceed the null most at Knossos.
"""
from collections import Counter, defaultdict
import json
from pathlib import Path
import random
import re

ROOT = Path(__file__).resolve().parent.parent
LB = ROOT / 'data/linearb'
SUB = str.maketrans('₀₁₂₃₄₅₆₇₈₉', '0123456789')
SIGN = re.compile(r'^([a-z]+[0-9]?|\*[0-9]+[a-z]?)$')
CRETE = {'Knossos', 'Khania', 'Vases - Khania', 'Vases - Mallia', 'Mallia', 'Armenoi', 'Vases - Knossos'}


def load_js_map(path):
    """Parse a linearb.xyz `new Map([...])` data file as JSON without executing it."""
    s = path.read_text(encoding='utf-8')
    s = s[s.index('(') + 1:s.rindex(')')]
    s = re.sub(r',\s*([\]}])', r'\1', s)
    return json.loads(s)


def lb_vocabulary():
    sites = defaultdict(set)
    count = Counter()
    for name, rec in load_js_map(LB / 'LinearBInscriptions.js'):
        site = rec.get('site', '')
        for t in rec.get('transliteratedWords', []):
            t = t.strip().lower()
            if '-' not in t or any(ch in t for ch in '[]?'):
                continue
            parts = t.split('-')
            if all(SIGN.match(p) for p in parts):
                sites[tuple(parts)].add(site)
                count[tuple(parts)] += 1
    return sites, count


def lb_categories():
    lex = json.loads((LB / 'tiripode_lexicon.json').read_text(encoding='utf-8'))
    cat = {}
    for k, v in lex.items():
        d = v['definition'].lower()
        pos = {x: d.find(x) for x in ('anthroponym', 'toponym', 'ethnic', 'theonym') if x in d}
        c = min(pos, key=pos.get) if pos else 'other'  # the category the glossary names first
        cat[tuple(k.lower().split('-'))] = c
    cat[('pa', 'i', 'to')] = 'toponym'  # empty definition in the glossary; Phaistos (Ventris and Chadwick)
    return cat


def la_words():
    rows = json.loads((ROOT / 'data/corpus.json').read_text(encoding='utf-8'))
    words = defaultdict(set)
    for r in rows:
        for t in r['transliteratedWords']:
            t = t.translate(SUB).strip().lower()
            if '-' not in t:
                continue
            parts = t.split('-')
            if all(re.match(r'^[a-z]+[0-9]?$', p) for p in parts):
                words[tuple(parts)].add(r['name'])
    return words


def where(sites):
    crete = bool(sites & CRETE)
    main = bool(sites - CRETE)
    return 'both' if crete and main else 'crete only' if crete else 'mainland only'


def main(reps=2000, seed=20260923, minlen=3):
    sites, count = lb_vocabulary()
    cat = lb_categories()
    lb = {w for w in sites if len(w) >= minlen}
    la = la_words()
    la_types = [w for w in la if len(w) >= minlen]
    freq = Counter(s for w in la for s in w)
    signs = sorted(freq, key=lambda s: -freq[s])
    size = -(-len(signs) // 10)
    bins = [signs[i:i + size] for i in range(0, len(signs), size)]

    def tally(mapping=None):
        c = Counter()
        hits = []
        for w in la_types:
            m = tuple(mapping[s] for s in w) if mapping else w
            if m in lb:
                c['all'] += 1
                c['cat:' + cat.get(m, 'not in glossary')] += 1
                c['where:' + where(sites[m])] += 1
                hits.append((w, m))
        return c, hits

    real, hits = tally()
    rng = random.Random(seed)
    null = defaultdict(list)
    keys = set(real)
    runs = []
    for _ in range(reps):
        mp = {}
        for b in bins:
            v = b[:]
            rng.shuffle(v)
            mp.update(zip(b, v))
        c, _ = tally(mp)
        runs.append(c)
        keys |= set(c)
    stats = {}
    for k in sorted(keys):
        vals = [c.get(k, 0) for c in runs]
        r = real.get(k, 0)
        stats[k] = {'real': r, 'null_mean': round(sum(vals) / reps, 3),
                    'p_ge': round((sum(v >= r for v in vals) + 1) / (reps + 1), 4)}
    lb_base = Counter(where(sites[w]) for w in lb)
    # concentration: of the real matches, are more on Crete than the null split predicts?
    from math import comb
    ec, em = stats.get('where:crete only', {}).get('null_mean', 0), stats.get('where:mainland only', {}).get('null_mean', 0)
    oc, om = real.get('where:crete only', 0), real.get('where:mainland only', 0)
    q, n = ec / (ec + em), oc + om
    crete_p = sum(comb(n, k) * q ** k * (1 - q) ** (n - k) for k in range(oc, n + 1))
    by = Counter((cat.get(m, 'not in glossary'), where(sites[m])) for _, m in hits)
    matches = [{'linear_a': '-'.join(w).upper(), 'linear_a_records': sorted(la[w])[:8],
                'linear_b_category': cat.get(w, 'not in glossary'), 'linear_b_sites': sorted(sites[w]),
                'linear_b_count': count[w]} for w, _ in hits]
    res = {'method': __doc__.strip(), 'min_signs': minlen, 'linear_a_types': len(la_types),
           'linear_b_types': len(lb), 'linear_b_types_by_where': dict(lb_base), 'reps': reps, 'seed': seed,
           'stats': stats, 'crete_vs_mainland': {'crete_only': oc, 'mainland_only': om, 'null_share_crete': round(q, 3),
                                                 'p_crete_excess': round(crete_p, 3)},
           'category_by_where': {f'{a} / {b}': v for (a, b), v in sorted(by.items())}, 'matches': sorted(matches, key=lambda m: m['linear_a'])}
    (ROOT / 'reading/names_lb_results.json').write_text(json.dumps(res, ensure_ascii=False, indent=1) + '\n',
                                                       encoding='utf-8')
    print('LA types', len(la_types), 'LB types', len(lb), dict(lb_base))
    for k, v in stats.items():
        print(f'  {k:28} real {v["real"]:3}  null {v["null_mean"]:6}  p {v["p_ge"]}')
    print('  crete vs mainland:', res['crete_vs_mainland'])
    print('  category x where:', res['category_by_where'])
    for m in res['matches']:
        print(f"  {m['linear_a']:16} {m['linear_b_category']:16} {','.join(m['linear_b_sites'])[:40]:40} LA:{','.join(m['linear_a_records'][:4])}")


if __name__ == '__main__':
    import sys
    main(minlen=int(sys.argv[1]) if len(sys.argv) > 1 else 3)
