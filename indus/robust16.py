"""Post-test checks on the sixteenth set (not registered).

Usage: python robust16.py
Writes results/robust16.md.
"""
import os
from collections import Counter
import predict_test13 as T
from numerals import NUMS
from predict_test7 import fisher_less
from predict_test16 import m_break
from signs import load
OUT = []
def say(s=''):
    OUT.append(s); print(s)
say('# Checks on the sixteenth set (after the test, not registered)')
say()
for lab, L in (('A', T.sample('A')), ('B', T.sample('B'))):
    c = Counter(x for t in L for x, y in zip(t, t[1:]) if x in NUMS and y == '520')
    say('- P6 %s: numerals before 520: %s.' % (lab, ', '.join('%s (%s %d) x%d' % (g, NUMS[g][1], NUMS[g][0], n)
                                                         for g, n in c.most_common())))
    lg = Counter(y for t in L for x, y in zip(t, t[1:]) if x in NUMS and NUMS[x][1] == 'long')
    tot = sum(lg.values())
    say('  long-stroke numerals are followed by: %s (of %d).' % (', '.join('%s x%d' % kv for kv in lg.most_common(8)), tot))
m77 = [r['seq'] for r in load(only_m77=True) if len(r['seq']) >= 2 and not any('?' in ln for ln in r['seq'])]
for lab, texts in (('as listed', m77), ('reversed', [t[::-1] for t in m77])):
    a, na, c, nc = m_break(texts, lambda t: {g for g in range(1, len(t)) if t[g] in ('740', '520') and t[g - 1] not in NUMS})
    say('- P18 %s, head + ending without numeral + ending: broken %d of %d (%.1f%%), other gaps %d of %d (%.1f%%), p = %.4f.' % (
        lab, a, na, 100 * a / max(1, na), c, nc, 100 * c / nc, fisher_less(a, na - a, c, nc - c)))
    a, na, c, nc = m_break(texts, lambda t: {g for g in range(1, len(t)) if t[g] == '740' and t[g - 1] not in NUMS})
    say('  740 only: broken %d of %d (%.1f%%), p = %.4f.' % (a, na, 100 * a / max(1, na), fisher_less(a, na - a, c, nc - c)))
open(os.path.join(T.HERE, 'results', 'robust16.md'), 'w', encoding='utf-8').write('\n'.join(OUT) + '\n')
