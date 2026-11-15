"""Decode nos. 206, 207, 215 with the committed decoding key and with the follow-up clerks' key; count how many of
the groups that rested on Pusch's values alone now have a clerk's attestation, and list every group whose value
changes.
Usage: python3 -I compare_decodes.py <target dir>
Old key: key/key_manuscript.tsv + key/pusch_values_used.tsv (as merged in PR 586).
New key: key/key_clerks_enlarged.tsv, then key/pusch_values_used.tsv for codes the clerks' pages still lack."""
import os, sys
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kcommon import parse


def load(path, col=1, srccol=2):
    k = {}
    for l in open(path, encoding='utf-8'):
        if l[0].isdigit():
            f = l.rstrip('\n').split('\t')
            k[int(f[0])] = (f[col], f[srccol] if len(f) > srccol else '')
    return k


td = sys.argv[1]
man = load(os.path.join(td, 'key/key_manuscript.tsv'))
pus = load(os.path.join(td, 'key/pusch_values_used.tsv'))
enl = load(os.path.join(td, 'key/key_clerks_enlarged.tsv'))
files = [('206', 'transcriptions/no206_reconciled.txt'), ('207', 'transcriptions/no207_reconciled.txt'),
         ('215', 'transcriptions/no215_reconciled.txt')]
tot = Counter(); changes = []; pusch_only = Counter(); now = Counter(); words = Counter()
for name, fn in files:
    for p in parse(os.path.join(td, fn)):
        for L in p['lines']:
            for k, g in enumerate(L['codes']):
                if g['kind'] != 'code':
                    continue
                c = g['code']
                old = man[c][0] if c in man else (pus[c][0] if c in pus else None)
                new = enl[c][0] if c in enl else (pus[c][0] if c in pus else None)
                tot[name] += 1
                if c not in man and c in pus:
                    pusch_only[name] += 1
                    if c in enl:
                        now[(name, enl[c][1])] += 1
                    else:
                        now[(name, 'still Pusch only')] += 1
                if old != new:
                    changes.append('%s %s l.%d g.%d code %d: %s -> %s (%s)' % (
                        name, p['folio'], L['n'], k + 1, c, old, new, enl[c][1] if c in enl else '-'))
print('groups:', dict(tot), 'total', sum(tot.values()))
print('groups resting on Pusch alone in the committed key:', dict(pusch_only), 'total', sum(pusch_only.values()))
for name, _ in files:
    print('  no.', name, {k[1]: v for k, v in now.items() if k[0] == name})
s = Counter()
for (n, b), v in now.items():
    s[b] += v
print('  all three:', dict(s))
print('decoded value changes (%d):' % len(changes))
for ch in changes:
    print('  ' + ch)
