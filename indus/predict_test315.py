"""Three-hundred-and-fifteenth registered prediction set (PREDICTIONS.md, PA1-PA3): decipherment loop 140, pictographic
referent signs. The single-sign referent units of the current configuration (set 312: 3+ objects in 2+ texts, 67%+ one
picture, both tablet pools): does a sign's CISI description (Parpola, data/cisi_signs.tsv via the M77 map) name the
thing in its referent picture? Keyword lists per picture code, fixed here; matches against 1,000 shuffles of the
pictures among these signs. A match is a pictograph checked against the object's iconography, as the copper-tablet
anchors are. Writes results/predict_test315.md."""
import csv
import os
import random
import re

import rtools as R
import referents as X

HERE = os.path.dirname(os.path.abspath(__file__))
KEYS = {'Bult': 'bull ox unicorn cattle', 'Bull1': 'bull ox unicorn cattle', 'Bull': 'bull ox cattle', 'Bull2': 'bull ox cattle',
        'Zebu': 'zebu bull ox', 'Gaur': 'gaur bison', 'Elep': 'elephant', 'Gavi': 'gharial crocodile', 'Phyt': 'plant tree leaf branch',
        'Pipal': 'pipal leaf tree', 'Goat': 'goat markhor ibex antelope', 'Rhin': 'rhinoceros rhino', 'Hare': 'hare rabbit',
        'Fish': 'fish', 'Anth': 'man human person figure', 'Tigr': 'tiger', 'Buff': 'buffalo'}


def descriptions():
    m = {r[0]: r[1] for r in csv.reader(open(os.path.join(HERE, 'data', 'icit_m77_map.tsv'), encoding='utf-8'), delimiter='\t') if r and r[0] != 'icit'}
    desc = {}
    for r in csv.DictReader((l for l in open(os.path.join(HERE, 'data', 'cisi_signs.tsv'), encoding='utf-8') if not l.startswith('#')), delimiter='\t'):
        for mm in r['mahadevan'].split(','):
            x = re.sub(r'\D', '', mm)
            if x:
                desc.setdefault(x.lstrip('0'), r['description'].lower())
    return {g: desc[re.sub(r'\D', '', mm).lstrip('0')] for g, mm in m.items() if re.sub(r'\D', '', mm).lstrip('0') in desc}


def hit(desc, pic):
    return any(re.search(r'\b%s' % k, desc) for k in KEYS.get(pic, '').split())


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Three-hundred-and-fifteenth registered predictions: decipherment loop 140, pictographic referent signs', 'predict_test315')
    P = X.pools(F, recs)
    D = descriptions()
    singles = []
    for lab, (clean, both) in P.items():
        for g, m in X.q_pairs(both, 3, 0.67, 1).items():
            singles.append((lab, g[0], m))
    have = [(lab, g, m) for lab, g, m in singles if g in D]
    real = [(lab, g, m) for lab, g, m in have if hit(D[g], m)]
    for lab, g, m in have:
        rd.say('- %s sign %s -> %s: "%s"%s' % (lab, g, m, D[g][:70], '  MATCH' if hit(D[g], m) else ''))
    rnd = random.Random(315)
    pics = [m for lab, g, m in have]
    null = []
    for _ in range(1000):
        rnd.shuffle(pics)
        null.append(sum(hit(D[g], p) for (lab, g, m), p in zip(have, pics)))
    p = (1 + sum(x >= len(real) for x in null)) / 1001
    rd.say('- %d single-sign referents (%d with a description); %d match their picture; shuffles 95th percentile %d; p = %.3f.' % (len(singles), len(have), len(real), sorted(null)[949], p))
    rd.say()
    rd.rec('PA1', '2+ matches, above the 95th percentile of the shuffles', '%d, p = %.3f' % (len(real), p), len(real) >= 2 and p < 0.05)
    rd.rec('PA2', 'the matches include a sign not already an anchor (749, 341, 753, 777)', ', '.join(g for lab, g, m in real) or 'none', any(g not in ('749', '341', '753', '777') for lab, g, m in real))
    rd.rec('PA3', 'progress rule: PA1 and PA2 (the matching signs join the anchored meanings; V strict rises)', 'PA1 %s, PA2 %s' % (len(real) >= 2 and p < 0.05, any(g not in ('749', '341', '753', '777') for lab, g, m in real)), len(real) >= 2 and p < 0.05 and any(g not in ('749', '341', '753', '777') for lab, g, m in real))
    rd.finish()


if __name__ == '__main__':
    main()
