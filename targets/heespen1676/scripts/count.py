"""Count the 537L passage from its frozen files (own code, standard library).
usage: python3 -I count.py <folder>
Checks and prints:
 A. token counts per key (valued / unvalued) from the transcription;
 B. v1 ledger (figure of record): re-decodes each unit with KEY_HB_v1, checks it equals the ledger's decoded column,
    checks the rule 'E if and only if a unit holds a code with no value', counts S, N, E and the strict share S/(S+N+E);
 C. v2 non-blind: rebuilds the v2 ledger from the v1 units and the S/N/E lists of the v2 judging file, checks the same rule
    with KEY_HB_v2, counts strict and lenient (709 read 'vo');
 D. Dan Bourdeau's rule ('?' units count as holes): number of '?' tokens in the transcription and the share under that rule."""
import sys, re, pathlib
F = pathlib.Path(sys.argv[1])
def key(p):
    K = {}
    for l in open(p, encoding='utf-8'):
        q = l.rstrip('\n').split('\t')
        if q[0] == 'tok': K[q[1]] = q[2]
    return K
K1 = key(F / 'gloss/KEY_HB_v1.tsv'); K2 = key(F / 'gloss/KEY_HB_v2.tsv')
tx = F / 'transcriptions/heespen_1676-04-17_537L.txt'
toks = [t for l in open(tx, encoding='utf-8') if l.strip() and not re.search(r'[a-z]{4,}', l) for t in l.split()]
print('A. tokens in transcription:', len(toks))
for name, K in (('v1', K1), ('v2', K2)):
    v = sum(t in K for t in toks); print('   %s valued %d + unvalued %d = %d' % (name, v, len(toks) - v, len(toks)))
rows = [l.rstrip('\n').split('\t') for l in open(F / 'units/heespen_1676-04-17_537L_v1_ledger.tsv', encoding='utf-8') if not l.startswith('#')]
units = []
for r in rows:
    tk = r[1].replace('margin:', '').split(); units.append((int(r[0]), tk, r[2], r[3]))
ntok = sum(len(u[1]) for u in units)
print('B. v1 ledger: units %d, tokens covered %d (transcription %d)' % (len(units), ntok, len(toks)))
assert [t for u in units for t in u[1]] == toks, 'ledger tokens differ from transcription'
bad = []
for n, tk, dec, j in units:
    d = ''.join(K1.get(t, '·') for t in tk)
    if d != dec: bad.append('unit %d decoded %r, ledger %r' % (n, d, dec))
    hole = any(t not in K1 for t in tk)
    if hole != (j == 'E'): bad.append('unit %d judged %s but hole=%s' % (n, j, hole))
print('   ledger checks: %s' % ('all units agree with KEY_HB_v1 and the E rule' if not bad else 'JUDGING SLIPS (listed, not rescored): ' + '; '.join(bad)))
rule = {}
for n, tk, dec, j in units:
    rule[n] = 'E' if any(t not in K1 for t in tk) else ('S' if j == 'S' else 'N')
r = {x: sum(v == x for v in rule.values()) for x in 'SNE'}
print('   by the E rule applied mechanically (S kept as judged): S %d + N %d + E %d = %d; strict %d/%d = %.1f%% (figure of record unchanged)' % (r['S'], r['N'], r['E'], sum(r.values()), r['S'], len(units), 100 * r['S'] / len(units)))
c = {x: sum(u[3] == x for u in units) for x in 'SNE'}
print('   S %d + N %d + E %d = %d; strict S/(S+N+E) = %d/%d = %.1f%%' % (c['S'], c['N'], c['E'], sum(c.values()), c['S'], len(units), 100 * c['S'] / len(units)))
print('   S units:', ', '.join('%d %s' % (u[0], u[2]) for u in units if u[3] == 'S'))
jt = open(F / 'units/heespen_1676-04-17_537L_v2_NONBLIND_judging.txt', encoding='utf-8').read()
def lst(tag):
    m = re.search(r'^' + tag + r' \([^)]*\)[^:]*: (.*?) = \d+$', jt, re.M) or re.search(r'^' + tag + r'[^:]*: (.*?) = \d+$', jt, re.M)
    return [int(x.strip().split()[0]) for x in m.group(1).split(',')]
E2, S2, N2 = lst('E'), lst('S'), lst('N')
assert sorted(E2 + S2 + N2) == list(range(1, 61)), 'v2 lists do not partition 60 units'
J2 = {**{n: 'E' for n in E2}, **{n: 'S' for n in S2}, **{n: 'N' for n in N2}}
bad = []
out = ['#unit\ttokens\tdecoded(KEY_HB_v2)\tjudge(non-blind)']
for n, tk, _, _ in units:
    hole = any(t not in K2 for t in tk)
    if hole != (J2[n] == 'E'): bad.append('unit %d judged %s but hole=%s' % (n, J2[n], hole))
    out.append('%d\t%s\t%s\t%s' % (n, ' '.join(tk), ''.join(K2.get(t, '·') for t in tk), J2[n]))
open(F / 'units/heespen_1676-04-17_537L_v2_NONBLIND_ledger.tsv', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('C. v2 NON-BLIND (537L was seen before KEY_HB_v2 was built; not a test): E rule check: %s' % ('all units agree' if not bad else '; '.join(bad)))
print('   S %d + N %d + E %d = 60; strict %d/60 = %.1f%%' % (len(S2), len(N2), len(E2), len(S2), 100 * len(S2) / 60))
vo = [n for n in N2 if '709' in units[n - 1][1] and K2['709'] == 'vö']
fix = [n for n in vo if re.sub('vö', 'vo', ''.join(K2.get(t, '·') for t in units[n - 1][1])) in ('davor', 'von', 'davon')]
print('   lenient (709 read vo): N units holding 709 that become words: %s -> S %d, N %d, E %d; %d/60 = %.1f%%' % (fix, len(S2) + len(fix), len(N2) - len(fix), len(E2), len(S2) + len(fix), 100 * (len(S2) + len(fix)) / 60))
q = toks.count('?')
print("D. '?' tokens in the 537L transcription: %d. Unvalued signs are named (alpha, Gamma, T ...) and every unit holding one is E,"
      " so Dan's rule ('?' units are holes in the denominator) gives the same %d/%d = %.1f%%." % (q, c['S'], len(units), 100 * c['S'] / len(units)))
