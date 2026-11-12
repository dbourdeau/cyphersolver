"""Held-out tests for target 1447.   python scripts/heldout.py

Test 1 (inside the sibling): key built only from rows 1-15 of DLI.3.524.1, applied to rows 16-31 of the same letter,
scored against the contemporary translation letter by letter.
Test 2 (target): key_frozen.tsv (all usable rows of 524.1) applied to DLI.4.634.1; reports coverage (groups the
frozen key knows). 634.1 has no contemporary decipherment, so test 2 is coverage, not accuracy.
"""
import sys
from keylib import ROOT, pairs_524, build, load_key

sys.stdout.reconfigure(encoding='utf-8', newline='\n')
train = pairs_524(set(range(1, 16)))
test = pairs_524(set(range(16, 32)))
key, _, _ = build(train)
right = sum(1 for _, g, p in test if key.get(g) == p)
wrong = [(s, g, p, key[g]) for s, g, p in test if g in key and key[g] != p]
unk = [(s, g, p) for s, g, p in test if g not in key]
print(f'Test 1: train {len(train)} pairs ({len(key)} groups) on rows 1-15; test {len(test)} letters on rows 16-31')
print(f'  right {right}/{len(test)} = {right/len(test):.3f}; wrong {len(wrong)} {wrong}; unknown group {len(unk)} {unk}')
known = [p for p in test if p[1] in key]
print(f'  on groups the training key knows: {right}/{len(known)} = {right/len(known):.3f}')
fk = load_key(ROOT / 'key_frozen.tsv')
groups = [g for l in (ROOT / 'transcription_634.txt').read_text(encoding='utf-8').splitlines() if l.startswith('R')
          for g in l.split()[1:]]
miss = [g for g in groups if g not in fk]
print(f'Test 2: DLI.4.634.1 {len(groups)} groups, frozen key covers {len(groups)-len(miss)} '
      f'({(len(groups)-len(miss))/len(groups):.3f}); not in key: {miss}')
