"""Decrypt: python scripts/decrypt.py   (standard library only)
Applies key.tsv (Narváez 2015, p. 122) to both transcriptions, pair by pair, with no edit: a pair outside the table
is printed as <pair>. Writes decryption_<doc>.txt, then compares the control runs with Narváez's printed clear
(control_narvaez2015.tsv) letter by letter."""
import os, sys
sys.stdout.reconfigure(encoding='utf-8')
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = ['DCXXI.3.244.1', 'DCXXI.3.250.2']
key = {}
for l in open(os.path.join(ROOT, 'key.tsv'), encoding='utf-8'):
    if l.startswith('#') or not l.strip() or l.startswith('code'): continue
    c, v = l.rstrip('\n').split('\t'); key[c] = v
def dec(groups):
    return '|'.join(''.join(key.get(p, '<%s>' % p) for p in w.split('-')) for w in groups.split('|'))
ref = {}
for l in open(os.path.join(ROOT, 'control_narvaez2015.tsv'), encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    f = l.rstrip('\n').split('\t'); ref[f[0]] = f[1]
ok = tot = 0
for doc in DOCS:
    out = ['# Mechanical decryption of transcription_%s.txt with key.tsv (no edit; "|" = word division as transcribed)' % doc,
           '# id\tfolio\trole\tdecryption']
    for l in open(os.path.join(ROOT, 'transcription_%s.txt' % doc), encoding='utf-8'):
        if l.startswith('#') or not l.strip(): continue
        rid, fol, role, groups = l.rstrip('\n').split('\t')
        d = dec(groups); out.append('\t'.join([rid, fol, role, d]))
        if role == 'control':
            a, b = d.replace('|', ''), ref[rid].replace('|', '')
            m = sum(1 for x, y in zip(a, b) if x == y); n = max(len(a), len(b)); ok += m; tot += n
            print('%s control %s / Narváez %s: %d/%d' % (rid, d, ref[rid], m, n))
    open(os.path.join(ROOT, 'decryption_%s.txt' % doc), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('control: %d of %d letters agree with Narváez (%.3f)' % (ok, tot, ok / tot))
