"""Which results depend on readings where SigLA and lineara.xyz disagree?

The Linear A vocabulary is rebuilt with SigLA's reading in place of lineara.xyz's wherever errata.py found a
word-level disagreement of a definite kind in a document (substitution, one sign added or missing, or word
division). 'Other' and 'no counterpart' cases are left as they are and counted. The word-matching results are
then recomputed on both vocabularies: Linear B place and personal names (names_lb.py), the NeuroDecipher Linear B
list (soundvalues.py), the Pre-Greek comparison (pregreek.py) and the language-family matches (lang_test.py).

The fraction-order evidence is checked separately: every document that contributes an adjacent fraction pair is
looked up in SigLA, and the two signs' order is read from SigLA's sign positions: left to right on one line (bounding boxes whose vertical ranges
overlap), or top to bottom in a stack (horizontal ranges overlap), since fractions are also written in columns.
"""
from collections import Counter, defaultdict
import json
from pathlib import Path
import random
import re
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lang_test as L  # noqa: E402
import names_lb as N  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
SUB = str.maketrans('₀₁₂₃₄₅₆₇₈₉', '0123456789')


def vocabularies():
    """Linear A word types (lower-case sign tuples) with their records, as read and with SigLA's readings."""
    errata = json.loads((ROOT / 'errata_results.json').read_text(encoding='utf-8'))['word_disagreements']
    rows = json.loads((ROOT / 'data/corpus.json').read_text(encoding='utf-8'))
    subs = defaultdict(list)
    used = Counter()
    for e in errata:
        if e['kind'] in ('substitution', 'indel', 'segmentation') and e['lineara_xyz'] and e['sigla']:
            subs[e['document'].replace(' ', '')].append(e)
    orig, alt = defaultdict(set), defaultdict(set)
    for r in rows:
        words = []
        for t in r['transliteratedWords']:
            t = t.translate(SUB).strip().lower()
            parts = t.split('-')
            if len(parts) >= 2 and all(re.match(r'^[a-z]+[0-9]?$', p) for p in parts):
                words.append(tuple(parts))
        for w in words:
            orig[w].add(r['name'])
        changed = list(words)
        for e in subs.get(r['name'].replace(' ', ''), []):
            la = tuple(e['lineara_xyz'].lower().split('-'))
            si = tuple(e['sigla'].lower().split('-'))
            if e['kind'] == 'segmentation':
                for i in range(len(changed) - 1):
                    if changed[i] + changed[i + 1] == la:
                        changed[i:i + 2] = [si]
                        used[e['kind']] += 1
                        break
            elif la in changed:
                changed[changed.index(la)] = si
                used[e['kind']] += 1
        for w in changed:
            if all(re.match(r'^[a-z]+[0-9]?$', p) for p in w):
                alt[w].add(r['name'])
    return orig, alt, dict(used), Counter(e['kind'] for e in errata)


def lb_matches(vocab, lb, sites, cat, minlen=3):
    hits = sorted(w for w in vocab if len(w) >= minlen and w in lb)
    names = [w for w in hits if cat.get(w) in ('anthroponym', 'toponym')]
    return {'matches': ['-'.join(w).upper() for w in hits],
            'names': ['-'.join(w).upper() for w in names],
            'names_crete_only': sum(1 for w in names if N.where(sites[w]) == 'crete only')}


def value_null(vocab, lb, rng, reps=1000, minlen=3):
    words = [w for w in vocab if len(w) >= minlen]
    freq = Counter(s for w in vocab for s in w)
    signs = sorted(freq, key=lambda s: -freq[s])
    size = -(-len(signs) // 10)
    bins = [signs[i:i + size] for i in range(0, len(signs), size)]
    out = []
    for _ in range(reps):
        mp = {}
        for b in bins:
            v = b[:]
            rng.shuffle(v)
            mp.update(zip(b, v))
        out.append(sum(1 for w in words if tuple(mp[s] for s in w) in lb))
    return out


def fraction_pairs_in_sigla():
    order = json.loads((ROOT / 'fraction_order_results.json').read_text(encoding='utf-8'))
    sig = {d['name'].replace(' ', ''): d for d in json.loads((ROOT / 'data/sigla_decoded.json').read_text(encoding='utf-8'))}
    code = {'A': 'A701', 'B': 'A702', 'D': 'A703', 'E': 'A704', 'F': 'A705', 'H': 'A706', 'J': 'A707', 'K': 'A708',
            'L': 'A709', 'L2': 'A709-2', 'L4': 'A709-4', 'L6': 'A709-6', 'JE': 'A732'}
    out = []
    for pair, info in order['adjacent_pairs'].items():
        a, b = pair.split()
        for rec in info['records']:
            d = sig.get(rec)
            if d is None:
                out.append({'pair': pair, 'record': rec, 'sigla': 'document not in SigLA'})
                continue
            atts = [x for x in d['attestations'] if x.get('sign_id')]
            A = [x for x in atts if x['sign_id'] == code.get(a)]
            B = [x for x in atts if x['sign_id'] == code.get(b)]
            if not A or not B:
                have = sorted({x['sign_id'] for x in atts if x['sign_id'].startswith('A7')})
                out.append({'pair': pair, 'record': rec, 'sigla': f'sign(s) not recorded in SigLA (fraction signs recorded: {have})'})
                continue
            verdict = 'reverse order in SigLA'
            for x in A:
                bx = x['bbox_raw']['fields']  # x, y, width, height
                for y in B:
                    by = y['bbox_raw']['fields']
                    same_line = not (bx[1] + bx[3] < by[1] or by[1] + by[3] < bx[1])
                    same_column = not (bx[0] + bx[2] < by[0] or by[0] + by[2] < bx[0])
                    if same_line and bx[0] < by[0]:
                        verdict = 'same order in SigLA (left to right)'
                    elif same_column and not same_line and bx[1] < by[1] and verdict.startswith('reverse'):
                        verdict = 'same order in SigLA (stacked, larger above)'
                    elif not same_line and not same_column and verdict.startswith('reverse'):
                        verdict = 'not adjacent in SigLA (different line and column)'
            out.append({'pair': pair, 'record': rec, 'sigla': verdict})
    return out


def main(seed=20260923):
    rng = random.Random(seed)
    orig, alt, used, kinds = vocabularies()
    sites, _ = N.lb_vocabulary()
    lb = {w for w in sites if len(w) >= 3}
    cat = N.lb_categories()
    res = {'method': __doc__.strip(), 'errata_kinds': dict(kinds), 'substitutions_applied': used,
           'types_only_in_lineara': sorted('-'.join(w).upper() for w in set(orig) - set(alt)),
           'types_only_in_sigla_version': sorted('-'.join(w).upper() for w in set(alt) - set(orig)), 'results': {}}
    for label, vocab in (('lineara.xyz readings', orig), ('SigLA readings where they differ', alt)):
        m = lb_matches(vocab, lb, sites, cat)
        null = value_null(vocab, lb, rng)
        m['null_mean'] = round(sum(null) / len(null), 2)
        m['p_ge'] = round((sum(n >= len(m['matches']) for n in null) + 1) / (len(null) + 1), 4)
        # NeuroDecipher list (soundvalues.py)
        from soundvalues import lb_words
        ndl = lb_words()
        m['neurodecipher_matches'] = sorted('-'.join(w) for w in {tuple(x.upper() for x in w) for w in vocab if len(w) >= 3}
                                            if w in ndl)
        # Pre-Greek lemmas (pregreek.py forms, lemma mode)
        import pregreek as P
        pre = [(json.loads(l)['word'], '') for l in open(ROOT / 'data/lexica/pregreek_wiktionary.jsonl', encoding='utf-8')]
        fp = P.forms(pre, 'lemma')
        m['pregreek_matches'] = sorted('-'.join(k).upper() for k in fp if k in {w for w in vocab if len(w) >= 3})
        # language families (raw matches with each lexicon)
        fam = {}
        for name in ('Luwian', 'Hurrian', 'Akkadian', 'Ugaritic', 'Etruscan', 'Hawaiian', 'Maori', 'Yoruba'):
            forms = {L.spell(w) for w, _ in L.SOURCES[name][1]()} - {None}
            fam[name] = sorted('-'.join(f).upper() for f in forms if len(f) >= 3 and f in {w for w in vocab if len(w) >= 3})
        m['language_matches'] = fam
        res['results'][label] = m
    res['fraction_pairs'] = fraction_pairs_in_sigla()
    (ROOT / 'reading/sigla_sensitivity_results.json').write_text(json.dumps(res, ensure_ascii=False, indent=1) + '\n',
                                                                encoding='utf-8')
    print('errata kinds', dict(kinds), '| applied', used)
    print('types only in lineara.xyz reading:', res['types_only_in_lineara'])
    print('types only in SigLA reading:', res['types_only_in_sigla_version'])
    for label, m in res['results'].items():
        print(f'== {label}')
        print(f"   Linear B matches {len(m['matches'])} (null {m['null_mean']}, p {m['p_ge']}): {m['matches']}")
        print(f"   names {m['names']} crete-only {m['names_crete_only']}/{len(m['names'])}")
        print(f"   NeuroDecipher list: {m['neurodecipher_matches']}")
        print(f"   Pre-Greek: {m['pregreek_matches']}")
        print(f"   languages: { {k: len(v) for k, v in m['language_matches'].items()} }")
    print('fraction pairs:')
    for f in res['fraction_pairs']:
        print('  ', f)


if __name__ == '__main__':
    main()
