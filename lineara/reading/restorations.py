"""Arithmetic restorations: what a damaged list must have held if its intact total is right.

For each KU-RO / PO-TO-KU-RO whose stated total is undamaged but whose natural window contains
damage, the shortfall (stated - legible sum) is what the damaged entries held. A negative
shortfall means the legible entries already exceed the total, so the window or the total is wrong.
Proposals only; each assumes the scribe added correctly.
"""
from fractions import Fraction as F
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
d = json.loads((ROOT / 'reading/reading.json').read_text(encoding='utf-8'))
out = []
for c in d['totals']:
    if c['stated_damaged'] or c['balances_in_some_window'] or not c['damage_in_windows']:
        continue
    for name, w in c['windows'].items():
        if not w['damage'] or w['unvalued_or_disputed_signs']:
            continue
        gap = F(c['stated']) - F(w['sum'])
        rec = next(r for r in d['records'] if r['name'] == c['record'])
        damaged = [f"entry {t['entry']}: {t['label'] or t['cls']}" for t in rec['tokens']
                   if t['damaged'] and t['cls'] != 'apparatus']
        out.append({'record': c['record'], 'term': c['term'], 'stated': c['stated'], 'window': name,
                    'legible_sum': w['sum'], 'shortfall': str(gap),
                    'status': 'restorable' if gap > 0 else 'inconsistent (legible sum exceeds total)',
                    'damaged_tokens': damaged[:8]})
(ROOT / 'reading/restorations.json').write_text(json.dumps({'method': __doc__.strip(), 'proposals': out},
                                                           ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
for o in out:
    print(f"{o['record']:11} {o['term']:11} total {o['stated']:>6} legible {o['legible_sum']:>7} -> {o['shortfall']:>6} [{o['window']}] {o['status']}")
