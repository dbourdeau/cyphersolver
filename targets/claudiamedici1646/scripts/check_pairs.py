"""Recheck the key against the glossed pairs, and grade the held-out test. Standard library only.

    python scripts/check_pairs.py

1. pairs.tsv: every row (signs of one cipher word on 24784 or 24796, and the contemporary gloss over it) is
   decrypted with key_frozen.tsv and must give the gloss letter for letter (case, accents, spaces, apostrophes and
   points ignored; v = u). Prints which key tokens the pairs attest. Exit 1 on any row that differs.
2. heldout_24786_pairs.tsv: the held-out words of 24786 are decrypted the same way and compared with the gloss;
   the words that differ are listed (not a failure: they are graded by hand as spelling variants or errors).
"""
import pathlib
import re
import sys
import unicodedata

sys.stdout.reconfigure(encoding='utf-8')
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.dont_write_bytecode = True
sys.path.insert(0, str(ROOT / 'scripts'))
from decrypt import load_key  # noqa: E402


def norm(s):
    s = unicodedata.normalize('NFD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c)).lower().replace('v', 'u')
    return re.sub(r'[^a-z]', '', s)


def dec(signs, key):
    out, used = [], []
    for t in signs.split():
        if t in ('=', '.', '|'):
            continue
        used.append(t)
        out.append(key.get(t, '[?' + t + ']'))
    return ''.join(out), used


def rows(path):
    for line in open(path, encoding='utf-8'):
        if line.startswith('#') or not line.strip():
            continue
        yield line.rstrip('\n').split('\t')


key = load_key(ROOT / 'key_frozen.tsv')
ok = True
n = signs = 0
seen = set()
for r in rows(ROOT / 'pairs.tsv'):
    if r[0] == 'frame':
        continue
    frame, s, gloss = r[:3]
    got, used = dec(s, key)
    n += 1
    signs += len(used)
    seen.update(used)
    if norm(got) != norm(gloss):
        print(f'FAIL pairs.tsv {frame} {s!r}: key gives {got!r}, gloss {gloss!r}')
        ok = False
codes = [t for t in key if key[t].startswith('[')]
letters = [t for t in key if t not in codes]
print(f'pairs.tsv: {n} glossed words, {signs} signs and groups, all decrypt to the gloss: {ok}')
print(f'  letter signs attested: {len([t for t in letters if t in seen])} of {len(letters)}'
      f'{"; not attested: " + " ".join(t for t in letters if t not in seen) if any(t not in seen for t in letters) else ""}')
print(f'  code groups attested: {" ".join(t for t in codes if t in seen)}'
      f'{"; not attested: " + " ".join(t for t in codes if t not in seen) if any(t not in seen for t in codes) else ""}')

same, diff, code = 0, [], []
for r in rows(ROOT / 'heldout_24786_pairs.tsv'):
    if r[0] == 'line':
        continue
    lid, s, gloss = r[:3]
    got, used = dec(s, key)
    if all(key.get(t, '').startswith('[') for t in used):
        code.append(f'{s} = {got} (gloss {gloss!r})')
        continue
    if norm(got) == norm(gloss):
        same += 1
    else:
        diff.append(f'{lid} {got!r} vs gloss {gloss!r}')
print(f'held-out 24786: {same + len(diff)} words, {same} letter for letter with the gloss; differ: '
      f'{"; ".join(diff) if diff else "none"}; code groups: {"; ".join(code)}')
sys.exit(0 if ok else 1)
