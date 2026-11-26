#!/usr/bin/env python3
"""Validate the hand alignment (key/alignment_by_group.txt; alignment_manual.txt in the first session) against the cipher and the test text; write the table."""
import sys, os, json, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import align_em as A
cipher = A.read_cipher(sys.argv[1])
words = [w for l in open(sys.argv[2], encoding='utf-8') if l.strip() and not l.startswith('#') for w in A.normalise(l)]
text = ''.join(words)
toks = []; consumed = ''; skipped = []
for line in open(sys.argv[3], encoding='utf-8'):
    if line.startswith('#') or not line.strip(): continue
    for item in line.split():
        if item.startswith('~'):
            consumed += item[1:]; skipped.append((len(toks), item[1:])); continue
        g, c = item.split('=')
        draft, _, meaning = c.partition('!')
        kind = 'text'
        if draft in ('0', '.', '?'):
            kind = {'0': 'null', '.': 'stop', '?': 'unknown'}[draft]; draft = ''
        consumed += draft
        toks.append((int(g), draft, meaning or draft, kind))
gs = [t[0] for t in toks]
ok = True
if gs != cipher:
    ok = False
    for i, (a, b) in enumerate(zip(gs, cipher)):
        if a != b: print('GROUP MISMATCH at', i, a, b, gs[max(0,i-3):i+3], cipher[max(0,i-3):i+3]); break
    print('lengths', len(gs), len(cipher))
if consumed != text:
    ok = False
    for i, (a, b) in enumerate(zip(consumed, text)):
        if a != b: print('TEXT MISMATCH at', i, repr(consumed[max(0,i-30):i+15]), 'vs', repr(text[max(0,i-30):i+15])); break
    print('lengths', len(consumed), len(text))
print('VALID' if ok else 'INVALID', len(toks), 'groups;', len(skipped), 'draft words without a group:', ' '.join(w for _, w in skipped))
by = collections.defaultdict(list)
for i, (g, d, m, k) in enumerate(toks):
    by[g].append((i, m if k == 'text' else {'null': '(null)', 'stop': '(full stop)', 'unknown': '(unknown)'}[k]))
json.dump({'tokens': toks, 'by_group': {str(g): v for g, v in sorted(by.items())}}, open(sys.argv[4], 'w'), indent=0)
if len(sys.argv) > 5:
    print('--- groups with more than one value ---')
    for g in sorted(by):
        vals = collections.Counter(v for _, v in by[g])
        if len(vals) > 1: print(g, dict(vals), [i for i, _ in by[g]])
