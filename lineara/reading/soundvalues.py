"""Do Linear B sound values carry over to Linear A?  A matching test with a null.

Linear A word types (conventional LB-derived transliteration, as in the working corpus) are
compared with 919 Linear B words that have Greek cognates, including place names
(NeuroDecipher, Luo et al. 2019, commit 480bad2). Real exact matches are counted, then the
sound values are reassigned at random among Linear A syllabograms of similar frequency
(10 frequency bins; the word shapes and sign frequencies are unchanged) and matches recounted.
If the carried-over values were arbitrary labels, the real count would sit inside the null.
Only words of 3+ signs count; 2-sign matches are mostly accidental.
"""
from collections import Counter
import json
from pathlib import Path
import random
import re
import unicodedata as ud

ROOT = Path(__file__).resolve().parent.parent
ROWS = json.loads((ROOT / 'data/corpus.json').read_text(encoding='utf-8'))
SUB = str.maketrans('₀₁₂₃₄₅₆₇₈₉', '0123456789')
SYL = re.compile(r'^[A-Z]+[0-9]?$')


def lb_words():
    rows = [l.rstrip('\n').split('\t') for l in open(ROOT / 'data/linearb/linear_b-greek.cog', encoding='utf-8')][1:]
    out = {}
    for lb, greek in rows:
        signs = []
        for c in lb:
            n = ud.name(c, '')
            if 'SYLLABLE' not in n:
                signs = None
                break
            signs.append(n.split()[-1])
        if signs:
            out[tuple(signs)] = greek
    return out


def la_words():
    """Distinct Linear A syllabic words with their records."""
    words = {}
    for r in ROWS:
        for t in r['transliteratedWords']:
            t = t.translate(SUB).strip()
            if '-' not in t:
                continue
            signs = t.split('-')
            if all(SYL.match(s) for s in signs):
                words.setdefault(tuple(signs), set()).add(r['name'])
    return words


def matches(la, lb, mapping=None, minlen=3):
    found = []
    for w in la:
        if len(w) < minlen:
            continue
        m = tuple(mapping[s] for s in w) if mapping else w
        if m in lb:
            found.append((w, m))
    return found


def main(reps=2000, seed=20260923):
    lb = lb_words()
    la = la_words()
    freq = Counter(s for w, recs in la.items() for s in w for _ in [0])
    signs = sorted(freq, key=lambda s: -freq[s])
    nb = 10
    bins = [signs[i::nb] for i in range(nb)]  # interleaved: each bin spans the frequency range evenly? no
    # Contiguous frequency bins instead
    size = -(-len(signs) // nb)
    bins = [signs[i:i + size] for i in range(0, len(signs), size)]
    real = matches(la, lb)
    rng = random.Random(seed)
    null = []
    for _ in range(reps):
        mp = {}
        for b in bins:
            vals = b[:]
            rng.shuffle(vals)
            mp.update(zip(b, vals))
        null.append(len(matches(la, lb, mp)))
    ge = sum(n >= len(real) for n in null)
    res = {
        'method': __doc__.strip(),
        'linear_a_word_types': len(la), 'linear_a_types_3plus': sum(len(w) >= 3 for w in la),
        'linear_b_words': len(lb), 'syllabograms': len(signs),
        'real_matches': [{'linear_a': '-'.join(w), 'greek_cognate': lb[m], 'records': sorted(la[w])} for w, m in real],
        'null_mean': sum(null) / reps, 'null_max': max(null), 'null_distribution': dict(sorted(Counter(null).items())),
        'p_value': (ge + 1) / (reps + 1), 'reps': reps, 'seed': seed,
    }
    (ROOT / 'reading/soundvalues_results.json').write_text(json.dumps(res, ensure_ascii=False, indent=2) + '\n',
                                                          encoding='utf-8')
    print('LA types', res['linear_a_word_types'], '3+', res['linear_a_types_3plus'], 'LB words', len(lb))
    print('real matches', len(real))
    for x in res['real_matches']:
        print('  ', x['linear_a'], x['greek_cognate'], x['records'][:5])
    print('null mean', res['null_mean'], 'max', res['null_max'], 'p', res['p_value'])
    print(res['null_distribution'])


if __name__ == '__main__':
    main()
