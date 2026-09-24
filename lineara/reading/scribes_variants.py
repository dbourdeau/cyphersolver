"""Do SigLA's sign variants go with the scribal hands assigned in the editions?

SigLA records, for each attested sign, a variant code (e.g. AB 60 drawn two ways). The working corpus carries
the traditional scribe attributions (e.g. "HT Scribe 9"). If the attributions are sound and the variant codes
capture handwriting, a sign's variant should depend on the scribe. For each sign with 2+ variants and 2+
attributed scribes, the association is measured by chi-square, and its significance by permuting scribe labels
among that sign's attestations (5,000 runs), which keeps each sign's variant mix and each scribe's share.

Note: SigLA's variant field is empty ('0') for about 90% of attestations; the coded variants are mostly
editorial sub-types (VIN a/b/c, animal f/m, numbered L-series fractions), not handwriting allographs, so the
test can only reach the few signs that carry them.

A second use: tablets with no attributed scribe (such as HT 34) are compared with each scribe's variant
preferences (a simple naive-Bayes score over signs shared with that scribe) to suggest candidate hands. This is
a pointer for palaeographers, not an attribution.
"""
from collections import Counter, defaultdict
import json
from math import log
from pathlib import Path
import random

ROOT = Path(__file__).resolve().parent.parent


def load():
    sig = json.loads((ROOT / 'data/sigla_decoded.json').read_text(encoding='utf-8'))
    corpus = json.loads((ROOT / 'data/corpus.json').read_text(encoding='utf-8'))
    scribe = {r['name'].replace(' ', ''): r.get('scribe', '') for r in corpus}
    rows = []
    for d in sig:
        s = scribe.get(d['name'].replace(' ', ''), None)
        for a in d['attestations']:
            if a.get('sign_id') and a.get('confidence_raw') == 1:
                v = a.get('variant_raw')
                v = (v.get('fields') or ['?'])[0] if isinstance(v, dict) else ('none' if v in (0, None) else str(v))
                rows.append((d['name'], s or '', a['sign_id'], v))
    return rows


def chi2(pairs):
    ct = Counter(pairs)
    rs, cs = Counter(p[0] for p in pairs), Counter(p[1] for p in pairs)
    n = len(pairs)
    return sum((ct.get((r, c), 0) - rs[r] * cs[c] / n) ** 2 / (rs[r] * cs[c] / n) for r in rs for c in cs)


def main(reps=5000, seed=20260923):
    rng = random.Random(seed)
    rows = load()
    by_sign = defaultdict(list)
    for doc, s, sign, var in rows:
        if s:
            by_sign[sign].append((s, var))
    tests = {}
    total_real, total_null = 0.0, [0.0] * reps
    for sign, pairs in by_sign.items():
        scribes = Counter(p[0] for p in pairs)
        variants = Counter(p[1] for p in pairs)
        if len(variants) < 2 or len([s for s, n in scribes.items() if n >= 3]) < 2 or len(pairs) < 15:
            continue
        real = chi2(pairs)
        labels = [p[0] for p in pairs]
        vars_ = [p[1] for p in pairs]
        null = []
        for i in range(reps):
            rng.shuffle(labels)
            x = chi2(list(zip(labels, vars_)))
            null.append(x)
            total_null[i] += x
        total_real += real
        tests[sign] = {'attestations': len(pairs), 'scribes': len(scribes), 'variants': len(variants),
                       'chi2': round(real, 2), 'p': round((sum(n >= real for n in null) + 1) / (reps + 1), 4)}
    overall_p = (sum(n >= total_real for n in total_null) + 1) / (reps + 1)
    # candidate hands for unattributed tablets
    prefs = defaultdict(lambda: defaultdict(Counter))
    for doc, s, sign, var in rows:
        if s:
            prefs[s][sign][var] += 1
    unattr = defaultdict(list)
    for doc, s, sign, var in rows:
        if not s:
            unattr[doc].append((sign, var))
    cands = {}
    for doc in ('HT 34', 'HT 9a', 'HT 9b', 'HT 95a', 'HT 95b', 'HT 86a'):
        if doc not in unattr:
            continue
        scores = []
        for s, sp in prefs.items():
            shared = [(g, v) for g, v in unattr[doc] if g in sp and sum(sp[g].values()) >= 2]
            if len(shared) < 4:
                continue
            ll = sum(log((sp[g][v] + 0.5) / (sum(sp[g].values()) + 0.5 * (len(sp[g]) + 1))) for g, v in shared) / len(shared)
            scores.append((round(ll, 3), s, len(shared)))
        cands[doc] = sorted(scores, reverse=True)[:3]
    res = {'method': __doc__.strip(), 'signs_tested': len(tests), 'overall_chi2': round(total_real, 1),
           'overall_null_mean': round(sum(total_null) / reps, 1), 'overall_p': round(overall_p, 4),
           'signs_p_below_0.05': sum(1 for t in tests.values() if t['p'] < 0.05), 'per_sign': tests,
           'candidate_hands_for_unattributed': cands}
    (ROOT / 'reading/scribes_variants_results.json').write_text(json.dumps(res, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(f"signs tested {len(tests)}; overall chi2 {res['overall_chi2']} vs null {res['overall_null_mean']}, p {res['overall_p']}; "
          f"signs with p<0.05: {res['signs_p_below_0.05']}")
    for sign, t in sorted(tests.items(), key=lambda x: x[1]['p'])[:12]:
        print('  ', sign, t)
    print('candidate hands (mean log-likelihood per shared sign, higher = closer):')
    for doc, c in cands.items():
        print('  ', doc, c)


if __name__ == '__main__':
    main()
