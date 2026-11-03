"""Held-out test: the frozen key (key_frozen.tsv, built from the gloss of ff. 4r-5r only) against the contemporary
gloss of ff. 5v-6v (gloss_heldout_5v-6v.tsv), mechanically.

For each gloss word the listed groups are first checked to stand, in that order, in transcription_1719.txt, then
decrypted with the frozen key and compared with the gloss. Comparison: lower case, accents dropped, u=v, j=i,
doubled letters written once (the cipher does not double), 'mp' = 'np'. Each gloss word falls in one class:
  exact        the frozen key gives the gloss word
  post-test    exact once the values found after the freeze (18 n, 20 qu, 32 e, 33 i) are put in, nothing else
  uncovered    a code or group the frozen key does not hold (an underlined short word counts as a code), and not
               one of the post-test values
  ending       the key gives the word with another final vowel (questo for questa) where the group carries a
               written superscript or dot that the frozen key does not interpret
  miss         the key gives something else
usage: python heldout_5v6v.py [--list]
"""
import os
import re
import sys
import unicodedata

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from decrypt import groups, load_key, lines, lookup  # noqa: E402

POST = {'18': 'n', '20': 'qu', '32': 'e', '33': 'i'}
key = load_key(os.path.join(D, 'key_frozen.tsv'))
tr = dict(lines(os.path.join(D, 'transcription_1719.txt')))


def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if 'a' <= c <= 'z').replace('u', 'v').replace('j', 'i')
    s = re.sub(r'(.)\1+', r'\1', s)
    return s.replace('mp', 'np')


def tokens(body):
    return re.sub(r'\{[^}]*\}', ' ', body).split()


def contains(seq, sub):
    return any(seq[i:i + len(sub)] == sub for i in range(len(seq) - len(sub) + 1))


cls = {'exact': [], 'post-test': [], 'uncovered': [], 'ending': [], 'miss': []}
bad = 0
for ln in open(os.path.join(D, 'gloss_heldout_5v-6v.tsv'), encoding='utf-8'):
    if ln.startswith('#') or not ln.strip():
        continue
    lid, grp, gloss, by = ln.rstrip('\n').split('\t')
    lids, parts = lid.split('+'), [p.split() for p in grp.split(' | ')]
    toks = []
    for l, p in zip(lids, parts):
        if l not in tr or not contains(tokens(tr[l]), p):
            print(f'GROUPS NOT IN TRANSCRIPTION: {lid} {grp}')
            bad += 1
        toks += p
    vals = []
    for t in toks:
        for g, under in groups(t):
            v = lookup(g, under, key)
            if under and g is not None and g + '_' not in key:
                v = None
            vals.append(v if v is not None else f'[{g}{"_" if under else ""}]')
    unk = [v.strip('[]') for v in vals if v.startswith('[')]
    frozen = norm(''.join(v for v in vals if not v.startswith('[')))
    post = norm(''.join(POST.get(v.strip('[]'), '') if v.startswith('[') else v for v in vals))
    g = norm(gloss)
    marked = any('^' in t or "'" in t for t in toks)
    if not unk and frozen == g:
        c = 'exact'
    elif unk and all(u in POST for u in unk) and post == g:
        c = 'post-test'
    elif any(u not in POST for u in unk):
        c = 'uncovered'
    elif marked and len(frozen) == len(g) and frozen[:-1] == g[:-1]:
        c = 'ending'
    else:
        c = 'miss'
    cls[c].append((lid, gloss, ' '.join(vals), by))

n = sum(len(v) for v in cls.values())
long_ = {k: [x for x in v if len(norm(x[1])) >= 4] for k, v in cls.items()}
nl = sum(len(v) for v in long_.values())
print(f'gloss words tested: {n} (of them {nl} with 4 or more letters)')
for k in cls:
    print(f'  {k:10s} {len(cls[k]):3d}   (4+ letters: {len(long_[k])})')
m = n - len(cls['uncovered'])
print(f'exact with the frozen key: {len(cls["exact"])} of {n} gloss words; of the {m} with no uncovered code group: '
      f'{len(cls["exact"])} exact ({len(cls["exact"]) / max(m, 1):.0%}), {len(cls["post-test"])} need only a post-test '
      f'value, {len(cls["ending"])} differ only in a marked ending, {len(cls["miss"])} miss')
if '--list' in sys.argv:
    for k, v in cls.items():
        for lid, gloss, dec, by in v:
            print(f'{k}\t{lid}\t{gloss}\t{dec}\t{by}')
sys.exit(1 if bad else 0)
