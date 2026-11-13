"""Held-out score of the frozen key on Lit. B (no gloss exists, so the reference is the marked reading).
python scripts/heldout_litB.py key.tsv transcription_litB_all.txt marked_litB.txt
(key.tsv = the frozen hopken1740 key; key_1741.tsv is the work key)
For every group: the value the reading gives it (plain piece, y of {x/y}, y of [?y]; none for holes and {+y}).
Counts groups where the frozen key's value equals that value (i/j, u/v/w folded), and the same for 500 shuffles of
the frozen key's values among its groups (control). Caveat: the reading was made with the work key, which contains
the frozen key, so this is a consistency figure for the frozen key on a page it was not built from, not a blind test."""
import sys, re, random
sys.path.insert(0, __file__.rsplit('heldout_litB.py', 1)[0])
from decrypt_litB import load_key, tokens
from check_marks_litB import n, SPLIT
fz = load_key(sys.argv[1])
groups = []
for l in open(sys.argv[2], encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    lab, rest = l.split(' ', 1)
    groups += [(lab, t[1]) for t in tokens(rest) if t[0] == 'g']
vals = []
for l in open(sys.argv[3], encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    lab, rest = l.rstrip('\n').split(' ', 1)
    for tok in re.findall(r"«[^»]*»|\S+", rest):
        if tok in ('.', ',', ';', ':') or tok.startswith('«'): continue
        for p in SPLIT.split(tok):
            if p == '' or p.startswith('{+'): continue
            m1 = re.fullmatch(r'\{([^/]*)/([^}]*)\}', p); m2 = re.fullmatch(r'\[\?([^\]]*)\]', p)
            if m1: vals.append(None if m1.group(2) == '...' else m1.group(2).lstrip('?'))
            elif m2: vals.append(m2.group(1))
            elif re.fullmatch(r'\[\d{3,4}\]', p): vals.append(None)
            else: vals.append(p)
assert len(vals) == len(groups), (len(vals), len(groups))
CODEOK = {('ottporten', 'Porta')}
def score(key):
    s = 0
    for (lab, g), v in zip(groups, vals):
        if v is None or g not in key: continue
        if n(key[g]) == n(v) or (key[g], v) in CODEOK: s += 1
    return s
known = sum(1 for _, g in groups if g in fz); read = sum(1 for v in vals if v is not None)
real = score(fz)
ks = list(fz.keys()); vs = list(fz.values()); rnd = random.Random(2242); sh = []
for _ in range(500):
    rnd.shuffle(vs); sh.append(score(dict(zip(ks, vs))))
print('groups %d; given a value by the reading %d; in the frozen key %d' % (len(groups), read, known))
print('frozen key value = reading: %d of %d groups (%.1f%%); %.1f%% of the groups the frozen key knows'
      % (real, len(groups), 100 * real / len(groups), 100 * real / known))
print('shuffled control (500): mean %.1f, max %d' % (sum(sh) / len(sh), max(sh)))
