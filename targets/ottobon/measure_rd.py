"""Measure the hand reading in rd_*.txt: tokens per page, tokens in lines of high/medium/low confidence, and tokens
read (not '?') in high+medium lines. Usage: python -I measure_rd.py [rd files]"""
import sys, glob, re
files = sys.argv[1:] or sorted(glob.glob('rd_f3*.txt'))
T = {'tot': 0, 'high': 0, 'medium': 0, 'low': 0, 'read': 0}
for f in files:
    blocks = re.split(r'^# f\.', open(f, encoding='utf8').read(), flags=re.M)[1:]
    t = {'tot': 0, 'high': 0, 'medium': 0, 'low': 0, 'read': 0}
    for b in blocks:
        ct = re.search(r'^ct:\s*(.*)$', b, re.M); cf = re.search(r'^conf:\s*(\w+)', b, re.M)
        if not ct: continue
        toks = ct.group(1).split(); n = len(toks); c = cf.group(1).lower() if cf else 'low'
        c = c if c in ('high', 'medium', 'low') else 'low'
        t['tot'] += n; t[c] += n
        if c in ('high', 'medium'): t['read'] += sum(1 for x in toks if '?' not in x)
    print('%-14s lines %3d tokens %4d  high %4d medium %4d low %4d  read(high+medium, no ?) %4d = %.1f%%' % (
        f, len(blocks), t['tot'], t['high'], t['medium'], t['low'], t['read'], 100 * t['read'] / max(1, t['tot'])))
    for k in T: T[k] += t[k]
print('TOTAL tokens %d read %d = %.1f%% (of the 1,528-token first pass: %.1f%%)' % (T['tot'], T['read'], 100 * T['read'] / max(1, T['tot']), 100 * T['read'] / 1528))
