"""The Linear A 'libation formula': slot order and variant forms, measured.

Words on stone vessels, metal objects and other non-administrative supports are grouped into
families by stem (regular expressions below, fixed from the variants seen). For every pair of
families that co-occur on an inscription, the written order is counted. A stable order across
sites is what makes this a formula; the variants within a family are where morphology shows.
Previous work: Davis 2014 (verb-initial syntax), Salgarella 2022; this is a re-measurement on the
working corpus, not a new identification.
"""
from collections import Counter, defaultdict
from itertools import combinations
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
READ = json.loads((ROOT / 'reading/reading.json').read_text(encoding='utf-8'))
FAMILIES = [  # (slot, name, pattern) in the order the canonical texts show
    (1, 'A-TA-I-*301-WA-JA', r'^A-TA-I-\*301-WA-(JA|E)$'),
    (2, 'place word (DI-KI-TE / TU-RU-SA / O-SU-QA-RE)', r'DI-KI-T|^TU-RU-SA$|^O-SU-QA-RE$'),
    (3, '(J)A-SA-SA-RA-ME', r'SA-SA-RA|^RA-ME$|^SA-RA-ME$'),
    (4, 'U-NA-(RU-)KA-NA-SI', r'U-NA-(RU-)?KA-(NA|JA)|^U-NA-KA-NA'),
    (5, 'I-PI-NA-MA', r'^I-PI(-NA-M|$)'),
    (6, 'SI-RU-TE', r'^SI-RU(-TE)?$'),
    (7, 'TA-NA-...-U-TI-NU', r'U-TI-NU$'),
]
NON_ADMIN_SKIP = {'Tablet', 'Nodule', 'Roundel', 'Sealing', 'Lames (short thin tablet)', '3-sided bar', '4-sided bar',
                  'Label'}


def family(w):
    for slot, name, pat in FAMILIES:
        if re.search(pat, w):
            return slot
    return None


def main():
    seqs, variants, sites = [], defaultdict(Counter), defaultdict(set)
    for r in READ['records']:
        if r['support'] in NON_ADMIN_SKIP:
            continue
        words = [t['label'] for t in r['tokens'] if t['cls'].startswith('word') or
                 (t['cls'] == 'toponym')]
        tagged = [(family(w), w) for w in words]
        slots = [s for s, _ in tagged if s]
        for s, w in tagged:
            if s:
                variants[s][w] += 1
                sites[s].add(r['site'])
        if len(set(slots)) >= 2:
            seqs.append({'record': r['name'], 'site': r['site'], 'words': words,
                         'slots': [s if s else '-' for s, _ in tagged]})
    agree, disagree = Counter(), Counter()
    for q in seqs:
        pos = {}
        for i, s in enumerate(q['slots']):
            if s != '-' and s not in pos:
                pos[s] = i
        for a, b in combinations(sorted(pos), 2):
            (agree if pos[a] < pos[b] else disagree)[(a, b)] += 1
    names = {s: n for s, n, _ in FAMILIES}
    res = {
        'method': __doc__.strip(),
        'inscriptions_with_2plus_slots': len(seqs),
        'pair_order': [{'first': names[a], 'second': names[b], 'in_order': agree[(a, b)],
                        'reversed': disagree[(a, b)]} for a, b in sorted(set(agree) | set(disagree))],
        'order_agreement': f"{sum(agree.values())}/{sum(agree.values()) + sum(disagree.values())}",
        'variants': {names[s]: {'forms': dict(v.most_common()), 'sites': sorted(sites[s])} for s, v in sorted(variants.items())},
        'sequences': seqs,
    }
    (ROOT / 'reading/formula_results.json').write_text(json.dumps(res, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('inscriptions with 2+ formula slots:', len(seqs), '| pairwise order agreement', res['order_agreement'])
    for p in res['pair_order']:
        if p['reversed']:
            print('  reversed:', p)
    for k, v in res['variants'].items():
        print(f'  {k}: {v["forms"]}  sites={v["sites"]}')


if __name__ == '__main__':
    main()
