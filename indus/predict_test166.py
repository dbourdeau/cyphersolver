"""Hundred-and-sixty-sixth registered prediction set (PREDICTIONS.md, RN1-RN10): the names that recur. Coordinates are
approximate (decimal degrees, from general sources) and used only for the distance test. Writes
results/predict_test166.md."""
import csv
import json
import math
import os
import random
from collections import Counter, defaultdict
from itertools import combinations

import predict_test13 as T
import rtools as R
import ur3_seals
from predict_test150 import sign_test
from predict_test152 import LINB, classes
from signs import FISH

random.seed(186)
COORD = {'Mohenjo-daro': (27.33, 68.14), 'Harappa': (30.63, 72.87), 'Lothal': (22.52, 72.25), 'Dholavira': (23.89, 70.21),
         'Kalibangan': (29.47, 74.13), 'Chanhujo-daro': (26.17, 68.32), 'Chanhudaro': (26.17, 68.32), 'Banawali': (29.60, 75.39),
         'Rakhigarhi': (29.29, 76.11), 'Surkotada': (23.62, 70.84), 'Rupar': (30.97, 76.53), 'Desalpur': (23.74, 69.58),
         'Nausharo': (29.36, 67.62), 'Amri': (26.16, 68.02), 'Kot Diji': (27.35, 68.71), 'Ganweriwala': (28.60, 71.58),
         'Mitathal': (28.89, 76.17), 'Farmana': (29.04, 76.32), 'Gola Dhoro (Bagasra)': (22.60, 71.79), 'Shikarpur': (23.23, 70.67)}


def km(a, b):
    la1, lo1, la2, lo2 = map(math.radians, a + b)
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 6371 * 2 * math.asin(math.sqrt(h))


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-sixty-sixth registered predictions: the names that recur', 'predict_test166')
    site = lambda r: recs[r['sealid']][3]
    seals = [r for r in F if r['type'].startswith('SEAL')]
    nms = lambda r: {x for x in R.names_in(r) if x[0]}
    city = defaultdict(set)
    for r in seals:
        if site(r) in ('Mohenjo-daro', 'Harappa'):
            for nm in nms(r):
                city[nm].add(site(r))
    both = [nm for nm, s in city.items() if len(s) == 2]
    rd.thr('RN1', 'shared names are fish names', 'names in both cities with a fish head (%s)' % '; '.join(' '.join(b) + ' ' + e for b, e in both),
           sum(b[-1] in FISH for b, e in both), len(both), 0.5)
    nseal = Counter(nm for r in seals for nm in nms(r))
    rd.gtl('RN2', 'recurring names are 520 names', '520, names on 2+ seals', [e == '520' for (b, e), n in nseal.items() if n >= 2],
           [e == '520' for (b, e), n in nseal.items() if n == 1])
    sites = defaultdict(set)
    for r in F:
        for nm in nms(r):
            sites[nm].add(site(r))
    by_k = defaultdict(list)
    for nm, n in nseal.items():
        if nm[1] == '740':
            by_k[n].append(len(sites[nm]))
    diffs = [len(sites[nm]) - sum(by_k[n]) / len(by_k[n]) for nm, n in nseal.items() if nm[1] == '520' and by_k.get(n)]
    w, l_, p = sign_test(diffs)
    rd.rec('RN3', '520 names travel further', '520 names with more sites than matched 740 names %d, fewer %d; sign test p = %.4f' % (w, l_, p), p < 0.05)
    wide = [(nm, s) for nm, s in sites.items() if len(s) >= 3]
    rd.rec('RN4', 'widespread names exist', 'names at 3+ sites: %d (%s)' % (len(wide), '; '.join('%s %s: %s' % (' '.join(b), e, ', '.join(sorted(s))) for (b, e), s in wide)), len(wide) >= 3)
    per = defaultdict(set)
    for r in F:
        for nm in nms(r):
            per[site(r)].add(nm)
    ss = [s for s in per if len(per[s]) >= 10 and s in COORD]
    prs = list(combinations(ss, 2))
    share = [len(per[a] & per[b]) / min(len(per[a]), len(per[b])) for a, b in prs]
    coords = [COORD[s] for s in ss]

    def rho(cs):
        cm = dict(zip(ss, cs))
        return T.spearman([km(cm[a], cm[b]) for a, b in prs], share)
    obs = rho(coords)
    le = 0
    for _ in range(1000):
        random.shuffle(coords)
        le += rho(coords) <= obs
    p = (le + 1) / 1001
    rd.rec('RN5', 'sharing falls with distance', 'sites %s; pairs %d; Spearman %.3f; p = %.4f' % (', '.join(ss), len(prs), obs, p), obs < 0 and p < 0.05)
    uni = lambda r: recs[r['sealid']][18].strip().startswith('Bull1')
    bs = set(both)
    mh = [r for r in seals if site(r) in ('Mohenjo-daro', 'Harappa') and nms(r)]
    rd.gtl('RN6', 'shared names are on unicorn seals', 'unicorn, seals with a shared name', [uni(r) for r in mh if nms(r) & bs], [uni(r) for r in mh if not nms(r) & bs])
    mot = lambda r: recs[r['sealid']][18].strip()
    grp = defaultdict(list)
    for r in seals:
        if mot(r) not in ('-', ''):
            for nm in nms(r):
                grp[nm].append(mot(r))
    same = [a == b for v in grp.values() if len(v) >= 2 for a, b in combinations(v, 2)]
    allm = [m for v in grp.values() for m in v]
    rnd = [random.choice(allm) == random.choice(allm) for _ in range(5000)]
    rd.gtl('RN7', 'one name, one motif', 'same motif, same-name seal pairs', same, rnd)
    tab = defaultdict(bool)
    for r in F:
        if r['type'].startswith('TAB'):
            for nm in nms(r):
                tab[nm] = True
    objs = Counter(nm for r in F for nm in nms(r))
    rd.gtl('RN8', 'recurring 520 names reach the tablets', 'on a tablet, recurring 520 names', [tab[nm] for nm, n in objs.items() if n >= 2 and nm[1] == '520'],
           [tab[nm] for nm, n in objs.items() if n >= 2 and nm[1] == '740'])
    st = {}
    for ln in open(os.path.join(LINB, 'corpus_damos_documents.jsonl'), encoding='utf-8'):
        d = json.loads(ln)
        st[d['id']] = d['site']
    persons, _ = classes()
    at = defaultdict(set)
    with open(os.path.join(LINB, 'corpus_damos_words.tsv'), encoding='utf-8') as f:
        for r in csv.DictReader(f, delimiter='\t'):
            if r['word'] in persons and st.get(r['doc_id']) in ('Knossos', 'Pylos') and r['status'] == 'complete':
                at[r['word']].add(st[r['doc_id']])
    rd.rank('RN9', 'Linear B shared persons are shorter', 'syllables, one-palace against both-palace persons',
            [len(w.split('-')) for w, s in at.items() if len(s) == 1], [len(w.split('-')) for w, s in at.items() if len(s) == 2])
    U = ur3_seals.load()
    ow = defaultdict(set)
    for (text, seal), o in U.items():
        if o['lines'] and o['site'] in ('Umma', 'Girsu'):
            own = next((cf for cf, pos in o['lines'][0] if pos == 'PN'), None)
            if own:
                ow[own].add(o['site'])
    rd.rank('RN10', 'Ur III shared owners are shorter', 'characters, one-city against both-city owners',
            [len(w) for w, s in ow.items() if len(s) == 1], [len(w) for w, s in ow.items() if len(s) == 2])
    rd.finish()


if __name__ == '__main__':
    main()
