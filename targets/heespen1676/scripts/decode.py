"""Decode a frozen transcription with a frozen key, once (own code, standard library).
usage: python3 -I decode.py <key.tsv> <transcription.txt>
Only rows of type 'tok' are used; 'tie' and 'phr' rows are ignored. A token with no value prints as [token].
Lines that are blank or contain a run of 4+ lower-case letters (comments, clear text) are skipped.
Output format is that of the runs b179/b180, so the stamped/filed decodes can be compared byte for byte."""
import sys, re, hashlib
kf, tf = sys.argv[1], sys.argv[2]
print('key md5', hashlib.md5(open(kf, 'rb').read()).hexdigest(), 'tx md5', hashlib.md5(open(tf, 'rb').read()).hexdigest())
K = {}
for l in open(kf, encoding='utf-8'):
    p = l.rstrip('\n').split('\t')
    if p[0] == 'tok': K[p[1]] = p[2]
for l in open(tf, encoding='utf-8'):
    if not l.strip() or re.search(r'[a-z]{4,}', l): continue
    toks = l.split()
    print(' '.join(K.get(t, '[' + t + ']') for t in toks), '   |', ''.join(K.get(t, '·') for t in toks), '| valued %d/%d' % (sum(t in K for t in toks), len(toks)))
