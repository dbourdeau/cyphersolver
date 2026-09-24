"""Are the fraction-order exceptions tied to particular commodities?

Each multi-sign fraction run (from reading.json, same entry, undamaged) is tagged with the commodity that
governs its entry: the logogram in the entry, or else the last commodity written before it in the record.
Adjacent pairs are then scored against the Corazza et al. 2021 values commodity by commodity. If fraction
signs had commodity-specific values (different units for grain, oil, cyperus), violations would cluster in
one commodity and each commodity's own pairs would be consistent.
"""
from collections import Counter, defaultdict
from fractions import Fraction as F
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
READ = json.loads((ROOT / 'reading/reading.json').read_text(encoding='utf-8'))
V = dict(J=F(1, 2), E=F(1, 4), F=F(1, 8), H=F(1, 16), A=F(1, 24), B=F(1, 5), D=F(1, 6), K=F(1, 10), L2=F(1, 20),
         L3=F(1, 30), L4=F(1, 40), L6=F(1, 60), JE=F(3, 4))


def main():
    pairs = []
    for r in READ['records']:
        cur, entry = None, None
        last_com = None
        for t in r['tokens']:
            if t['cls'] == 'commodity':
                last_com = re.findall(r'[A-Z]{3,}', t['label'])[0]
            if t['entry'] != entry:
                entry = t['entry']
                ent_com = next((re.findall(r'[A-Z]{3,}', y['label'])[0] for y in r['tokens']
                                if y['entry'] == entry and y['cls'] == 'commodity'), None)
            fs = t.get('fraction_signs')
            if fs and len(fs) >= 2 and not t['damaged']:
                com = ent_com or last_com or '(none)'
                for a, b in zip(fs, fs[1:]):
                    if a != b:
                        pairs.append({'record': r['name'], 'site': r['site'], 'commodity': com, 'pair': f'{a} {b}',
                                      'ok': (V[a] > V[b]) if a in V and b in V else None})
    by = defaultdict(Counter)
    for p in pairs:
        by[p['commodity']]['ok' if p['ok'] else 'violated' if p['ok'] is False else 'unvalued'] += 1
    bad = [p for p in pairs if p['ok'] is False]
    res = {'method': __doc__.strip(), 'pairs': len(pairs), 'by_commodity': {k: dict(v) for k, v in by.items()},
           'violations': bad, 'all_pairs': pairs}
    (ROOT / 'reading/fraction_commodity_results.json').write_text(json.dumps(res, ensure_ascii=False, indent=1) + '\n',
                                                                 encoding='utf-8')
    print('pairs', len(pairs))
    for k, v in sorted(by.items(), key=lambda x: -sum(x[1].values())):
        print(f'  {k:8} {dict(v)}')
    print('violations of the 2021 values:')
    for p in bad:
        print('  ', p)


if __name__ == '__main__':
    main()
