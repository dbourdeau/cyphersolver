"""Do Linear B personal names at Knossos look more like Linear A names than those at Pylos do?

Exact matches (names_lb.py) give six shared names. This asks a broader question with hundreds of names:
whether the *shape* of Knossos personal names (their syllables, first and last syllables) is closer to
Linear A's list names than the shape of Pylos personal names is. A Minoan naming substrate at Knossos
would show as Knossos names sitting closer to Linear A.

Linear A names: words classed as entry labels in administrative texts (build_reading.py), excluding the
recurrent transaction words (SA-RA2, A-DU, KA-PA, DA-RE, KU-PA, SA-MA, KU-RO, KI-RO). Linear B names:
headwords the Ventris-Chadwick glossary calls anthroponyms (tiripode lexicon), attested only at Knossos
or only at Pylos (linearb.xyz corpus). Only words of 2+ signs, one token per type.

Statistic: Jensen-Shannon divergence between syllable distributions (all syllables, first syllables,
last syllables) of Linear A names and each Linear B group; D = JSD(LA, Pylos) - JSD(LA, Knossos). Null:
the Knossos and Pylos names are pooled and the site labels shuffled, group sizes kept, 5,000 times.
Two controls: the same test on Knossos and Pylos *non-name* vocabulary (glossary 'other' words), which
should show no Knossos advantage if the effect is about names; and Greek-looking names removed (names
with a Greek etymology in the glossary definition) to see whether the effect is carried by non-Greek names.
"""
from collections import Counter
import json
from math import log2
from pathlib import Path
import random
import re
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import names_lb as N  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
TERMS = {'SA-RA2', 'A-DU', 'KA-PA', 'DA-RE', 'KU-PA', 'SA-MA', 'KU-RO', 'KI-RO', 'PO-TO-KU-RO'}


def jsd(p, q):
    keys = set(p) | set(q)
    m = {k: (p.get(k, 0) + q.get(k, 0)) / 2 for k in keys}
    kl = lambda a: sum(a[k] * log2(a[k] / m[k]) for k in keys if a.get(k, 0) > 0)
    return (kl(p) + kl(q)) / 2


def profile(words, part):
    c = Counter()
    for w in words:
        if part == 'all':
            c.update(w)
        elif part == 'first':
            c[w[0]] += 1
        else:
            c[w[-1]] += 1
    n = sum(c.values())
    return {k: v / n for k, v in c.items()}


def la_names():
    d = json.loads((ROOT / 'reading/reading.json').read_text(encoding='utf-8'))
    out = set()
    for r in d['records']:
        for t in r['tokens']:
            if t['cls'] == 'word' and t.get('function') == 'entry label' and t['label'] not in TERMS:
                w = tuple(t['label'].lower().split('-'))
                if len(w) >= 2 and all(re.match(r'^[a-z]+[0-9]?$', s) for s in w):
                    out.add(w)
    return sorted(out)


def lb_groups(category):
    sites, _ = N.lb_vocabulary()
    lex = json.loads((ROOT / 'data/linearb/tiripode_lexicon.json').read_text(encoding='utf-8'))
    cat = N.lb_categories()
    greek = {tuple(k.lower().split('-')) for k, v in lex.items()
             if re.search(r'[Ͱ-Ͽἀ-῿]', v['definition'])}
    kn, py = [], []
    for w, s in sites.items():
        if len(w) < 2 or cat.get(w) != category or any(x.startswith('*') for x in w):
            continue
        if s == {'Knossos'}:
            kn.append(w)
        elif s == {'Pylos'}:
            py.append(w)
    return kn, py, greek


def test(la, kn, py, rng, reps):
    res = {}
    for part in ('all', 'first', 'last'):
        pla = profile(la, part)
        real = jsd(pla, profile(py, part)) - jsd(pla, profile(kn, part))
        pool, k = kn + py, len(kn)
        null = []
        for _ in range(reps):
            rng.shuffle(pool)
            null.append(jsd(pla, profile(pool[k:], part)) - jsd(pla, profile(pool[:k], part)))
        res[part] = {'jsd_la_knossos': round(jsd(pla, profile(kn, part)), 4),
                     'jsd_la_pylos': round(jsd(pla, profile(py, part)), 4),
                     'D': round(real, 4), 'null_mean': round(sum(null) / reps, 4),
                     'p_knossos_closer': round((sum(n >= real for n in null) + 1) / (reps + 1), 4)}
    return res


def main(reps=5000, seed=20260923):
    rng = random.Random(seed)
    la = la_names()
    kn, py, greek = lb_groups('anthroponym')
    kn_o, py_o, _ = lb_groups('other')
    kn_ng = [w for w in kn if w not in greek]
    py_ng = [w for w in py if w not in greek]
    res = {'method': __doc__.strip(), 'linear_a_names': len(la),
           'names': {'knossos': len(kn), 'pylos': len(py)}, 'tests': {}}
    res['tests']['personal names'] = test(la, kn, py, rng, reps)
    res['tests']['personal names without a Greek etymology'] = test(la, kn_ng, py_ng, rng, reps)
    res['tests']['control: non-name vocabulary'] = test(la, kn_o, py_o, rng, reps)
    res['sizes'] = {'names without Greek etymology': {'knossos': len(kn_ng), 'pylos': len(py_ng)},
                    'non-name vocabulary': {'knossos': len(kn_o), 'pylos': len(py_o)}}
    top = lambda ws: [s for s, _ in Counter(w[-1] for w in ws).most_common(8)]
    res['commonest_last_syllables'] = {'linear_a': top(la), 'knossos_names': top(kn), 'pylos_names': top(py)}
    (ROOT / 'reading/name_shapes_results.json').write_text(json.dumps(res, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('Linear A names', len(la), '| Knossos names', len(kn), '| Pylos names', len(py))
    print('sizes', res['sizes'])
    for name, t in res['tests'].items():
        print('==', name)
        for part, v in t.items():
            print(f"   {part:5}  JSD(LA,KN) {v['jsd_la_knossos']}  JSD(LA,PY) {v['jsd_la_pylos']}  D {v['D']}  null {v['null_mean']}  p {v['p_knossos_closer']}")
    print('commonest last syllables', res['commonest_last_syllables'])


if __name__ == '__main__':
    main()
