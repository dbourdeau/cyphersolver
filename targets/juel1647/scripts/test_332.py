"""Tests on the 3-32 set (p. 6, to Hannibal Sehested): (1) Vibe old cipher (Dudout PR #410, section G); (2) Vibe new
alphabet (section N); (3) the juel 8-64 table shifted by s = -40..+40 (number n read as key[n + s]); (4) plain rank
ciphers n -> letter n - s over the 23- and 25-letter alphabets. Prints each candidate with a crude Danish score
(share of letters in the 8 most frequent Danish letters e r n t d a s i, and of bigram hits in a small list)."""
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from decrypt import load_key, vibeold, tokens
K = load_key()
TXT = open(os.path.join(os.path.dirname(__file__), '..', 'transcription_hsehested.txt'), encoding='utf8').read().splitlines()
L = [l for l in TXT if l and not l.startswith('#')][0]
nums = [int(t) for t in tokens(L) if t.isdigit() and int(t) < 100]
BIG = set('er en de te nd ge st an et re ar ri in ed ig le el se ke ha ma ll om og ck'.split())
def score(s):
    s = re.sub('[^a-zø]', '', s)
    if not s: return 0
    f = sum(c in 'erntdasi' for c in s) / len(s); b = sum(s[i:i+2] in BIG for i in range(len(s)-1)) / max(1, len(s)-1)
    return round(f + b, 3)
res = []
res.append(('vibe old', vibeold(L)))
N = 'abcdefghiklmnopqrstuwxyzø'
def vnew(nums):
    out = []; k = None
    for n in nums:
        if (24 <= n <= 39 or 1 <= n <= 3) and (k is None or n > 25 or n <= 3 and k is None):
            k = 0 if n <= 29 and n >= 24 else 1 if n <= 34 and n >= 30 else 2 if n >= 35 else 3; out.append(' '); continue
        out.append(N[n - k - 1] if 0 < n - k <= 25 else '?')
    return ''.join(out)
res.append(('vibe new', vnew(nums)))
for s in range(-40, 41):
    out = ''.join((K.get(n + s, '?') if K.get(n + s, '?') != '(null)' else '.') for n in nums)
    res.append(('juel shift %+d' % s, out))
for A, name in (('abcdefghiklmnopqrstuxyz', 'rank23'), (N, 'rank25')):
    for s in range(-10, 30):
        res.append(('%s shift %d' % (name, s), ''.join(A[(n - s - 1) % len(A)] for n in nums)))
res.sort(key=lambda r: -score(r[1]))
for name, out in res[:12]: print('%-18s %.3f  %s' % (name, score(out), out))
print('n numbers', len(nums))
