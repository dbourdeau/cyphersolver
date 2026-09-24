"""Pre-Greek substrate words against Linear A.

If Minoan is one of the sources of the Pre-Greek substrate, Greek words of Pre-Greek origin should match
Linear A word shapes more often than ordinary Greek words do. Comparing the two within Greek holds Greek
phonology and word-building constant, which unrelated control languages cannot.

Pre-Greek list: Ancient Greek entries whose Wiktionary etymology derives or borrows them from Pre-Greek
(template source code qsb-grc; mostly following Beekes and Furnee), streamed from the Kaikki extract: 1,600
entries. Ordinary Greek: Ancient Greek nouns, adjectives, names and verbs in the same extract not so marked.
Spelling: lang_test.spell, the same fixed Linear B rules. Two forms per word: the lemma, and the lemma minus
its last syllable (Greek endings such as -os, -a, -e would not appear in a Minoan original).
Statistic: exact matches with the Linear A word types of 3+ signs, per 1,000 forms; the ordinary-Greek rate
is estimated from 2,000 random samples matched to the Pre-Greek list's word-length distribution (Pre-Greek
lemmas are shorter, and length alone changes the chance of an exact match), giving a p-value for the excess.
"""
import json
from pathlib import Path
import random
import sys
import unicodedata as ud

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lang_test as L  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
LEX = ROOT / 'data/lexica'


def romanise(word):
    g = ud.normalize('NFD', word.lower())
    g = ''.join(ch for ch in g if not ud.combining(ch))
    return ''.join(L.GREEK.get(ch, ch) for ch in g)


def forms(words, mode):
    out = {}
    for w, gloss in words:
        sp = L.spell(romanise(w))
        if not sp:
            continue
        if mode == 'stem':
            sp = sp[:-1]
        if len(sp) >= 3:
            out.setdefault(sp, (w, gloss))
    return out


def main(reps=2000, seed=20260923):
    rng = random.Random(seed)
    la3 = {tuple(x.lower() for x in w) for w in L.la_types() if len(w) >= 3}
    pre = [(json.loads(l)['word'], json.loads(l)['gloss']) for l in open(LEX / 'pregreek_wiktionary.jsonl', encoding='utf-8')]
    pre_set = {w for w, _ in pre}
    ordinary = []
    for line in open(LEX / 'AncientGreek_head.jsonl', encoding='utf-8'):
        r = json.loads(line)
        if r.get('pos') in ('noun', 'adj', 'name', 'verb') and r['word'] not in pre_set and ' ' not in r['word']:
            g = (r.get('senses') or [{}])[0].get('glosses', [''])
            ordinary.append((r['word'], (g or [''])[0][:80]))
    res = {'method': __doc__.strip(), 'pregreek_entries': len(pre), 'ordinary_entries': len(ordinary), 'modes': {}}
    for mode in ('lemma', 'stem'):
        fp = forms(pre, mode)
        fo = list(forms(ordinary, mode).items())
        hits = sorted(k for k in fp if k in la3)
        n = len(fp)
        # ordinary Greek sampled to the Pre-Greek list's word-length distribution (lemmas of Pre-Greek origin
        # are shorter, and length alone changes the chance of an exact match)
        from collections import Counter, defaultdict
        by_len = defaultdict(list)
        for k, v in fo:
            by_len[len(k)].append(k)
        need = Counter(len(k) for k in fp)
        samp = []
        for _ in range(reps):
            c = 0
            for L_, m in need.items():
                pool = by_len.get(L_, [])
                c += sum(1 for k in rng.sample(pool, min(m, len(pool))) if k in la3)
            samp.append(c)
        mean = sum(samp) / reps
        res['modes'][mode] = {
            'pregreek_forms': n, 'pregreek_matches': len(hits), 'pregreek_per_1000': round(1000 * len(hits) / n, 2),
            'ordinary_forms': len(fo), 'ordinary_expected_at_same_size': round(mean, 2),
            'ordinary_per_1000': round(1000 * mean / n, 2),
            'p_excess': round((sum(x >= len(hits) for x in samp) + 1) / (reps + 1), 4),
            'matches': [{'linear_a': '-'.join(h).upper(), 'greek': fp[h][0], 'gloss': fp[h][1]} for h in hits]}
    (ROOT / 'reading/pregreek_results.json').write_text(json.dumps(res, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(f"Pre-Greek entries {len(pre)}, ordinary Greek entries {len(ordinary)}")
    for m, v in res['modes'].items():
        print(f"== {m}: Pre-Greek {v['pregreek_matches']}/{v['pregreek_forms']} ({v['pregreek_per_1000']}/1000) vs ordinary "
              f"{v['ordinary_expected_at_same_size']} expected ({v['ordinary_per_1000']}/1000)  p {v['p_excess']}")
        for x in v['matches']:
            print(f"     {x['linear_a']:14} {x['greek']:14} {x['gloss'][:60]}")


if __name__ == "__main__" and len(sys.argv) == 1:
    main()


def jsd(p, q):
    from math import log2
    keys = set(p) | set(q)
    m = {k: (p.get(k, 0) + q.get(k, 0)) / 2 for k in keys}
    def kl(a):
        return sum(a[k] * log2(a[k] / m[k]) for k in keys if a.get(k, 0) > 0)
    return (kl(p) + kl(q)) / 2


def syllable_profile(forms_):
    from collections import Counter
    c = Counter(s for f in forms_ for s in f)
    n = sum(c.values())
    return {k: v / n for k, v in c.items()}


def phonotactic_distance(reps=200, seed=20260923, size=300):
    """Jensen-Shannon divergence between the syllable distribution of Linear A word types and that of each
    lexicon's Linear B-style spellings (equal-size samples of word forms, averaged), plus word-length means."""
    rng = random.Random(seed)
    la = [tuple(x.lower() for x in w) for w in L.la_types()]
    la_p = syllable_profile(la)
    pre = [(json.loads(l)['word'], '') for l in open(LEX / 'pregreek_wiktionary.jsonl', encoding='utf-8')]
    pre_set = {w for w, _ in pre}
    ordinary = [(json.loads(l)['word'], '') for l in open(LEX / 'AncientGreek_head.jsonl', encoding='utf-8')
                if json.loads(l).get('pos') in ('noun', 'adj', 'name', 'verb')]
    ordinary = [x for x in ordinary if x[0] not in pre_set and ' ' not in x[0]]
    lists = {'Pre-Greek (Wiktionary)': [L.spell(romanise(w)) for w, _ in pre],
             'Greek, ordinary': [L.spell(romanise(w)) for w, _ in ordinary]}
    for name in ('Luwian', 'Hurrian', 'Akkadian', 'Ugaritic', 'Hawaiian', 'Maori', 'Yoruba', 'Samoan'):
        lists[name] = [L.spell(w) for w, _ in L.SOURCES[name][1]()]
    out = {}
    for name, fl in lists.items():
        fl = [f for f in fl if f and len(f) >= 2]
        vals = [jsd(la_p, syllable_profile(rng.sample(fl, min(size, len(fl))))) for _ in range(reps)]
        vals.sort()
        out[name] = {'forms': len(fl), 'jsd_mean': round(sum(vals) / reps, 4), 'jsd_90ci': [round(vals[int(.05 * reps)], 4), round(vals[int(.95 * reps)], 4)],
                     'mean_len': round(sum(map(len, fl)) / len(fl), 2)}
    # Linear A against itself (split halves) as the floor
    halves = []
    for _ in range(reps):
        s = rng.sample(la, len(la))
        halves.append(jsd(syllable_profile(s[:size]), syllable_profile(s[size:2 * size])))
    out['Linear A vs itself (split halves)'] = {'jsd_mean': round(sum(halves) / reps, 4), 'mean_len': round(sum(map(len, la)) / len(la), 2)}
    return out


if __name__ == '__main__' and len(sys.argv) > 1 and sys.argv[1] == 'profile':
    res = json.loads((ROOT / 'reading/pregreek_results.json').read_text(encoding='utf-8'))
    res['phonotactic_distance'] = phonotactic_distance()
    (ROOT / 'reading/pregreek_results.json').write_text(json.dumps(res, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    for k, v in sorted(res['phonotactic_distance'].items(), key=lambda x: x[1]['jsd_mean']):
        print(f"  {k:36} JSD {v['jsd_mean']}  {v.get('jsd_90ci', '')}  mean length {v['mean_len']}")
