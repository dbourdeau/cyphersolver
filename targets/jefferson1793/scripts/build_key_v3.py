"""ROUND 3 (after the held-out test and the cold check): build Code No. 15 key v3 from all five letters (A-E).
Input: key/hand_alignment_v3.txt (hand alignment with the decipherments of the time),
transcription/code15_groups_v3.tsv, plaintext/training_cribs.tsv. Checks that each segment's groups are exactly the
transcribed groups in order and that the pieces spell the decipherment; then writes key/code15_key_v3.tsv.
Reads document A and its crib (A was the held-out letter of round 1). Run from output/code15_1793_2026-11-28: python3 scripts/build_key_v3.py"""
import csv, collections, re, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from code15lib import load_groups, parse, words_of

docs = load_groups('transcription/code15_groups_v3.tsv')
cribs = {r['segment']: r for r in csv.DictReader(open('plaintext/training_cribs.tsv', encoding='utf-8'), delimiter='\t')}
cribs['A'] = {'doc': 'A', 'plaintext': [l for l in open('plaintext/heldout_crib.txt', encoding='utf-8') if not l.startswith('#')][0]}

def seg_tokens(seg):
    doc = cribs[seg]['doc']; rows = docs[doc]
    toks = [g for (_, _, g) in rows]
    if seg in ('E1', 'E2'):
        cut = next(i for i, t in enumerate(toks) if t.startswith('[del'))
        toks = toks[:cut] if seg == 'E1' else toks[cut + 1:]
    if seg in ('C1', 'C2'):
        toks = [t for (l, _, t) in rows if (l <= 2) == (seg == 'C1')]
    return toks

SUF = {'=': ('s', 'es'), '+': ('ed', 'd'), 'x': ('ed', 'd')}
entries = collections.defaultdict(list)   # num -> [(base, sure, segment)]
errors = 0
for line in open('key/hand_alignment_v3.txt', encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    seg, rest = line.split(':', 1)
    items = [it.rsplit(':', 1) for it in rest.split()]
    toks = seg_tokens(seg)
    if [g for g, _ in items] != toks:
        print('GROUP MISMATCH', seg, [ (a,b) for a,b in zip([g for g,_ in items], toks) if a!=b][:5], len(items), len(toks)); errors += 1
    spelled = ''.join(p.rstrip('?').replace('_', '').replace('-', '') for _, p in items)
    crib = ''.join(words_of(cribs[seg]['plaintext']))
    if spelled != crib:
        i = next((k for k in range(min(len(spelled), len(crib))) if spelled[k] != crib[k]), None)
        print('SPELLING MISMATCH', seg, i, spelled[max(0,(i or 0)-15):(i or 0)+15], '|', crib[max(0,(i or 0)-15):(i or 0)+15]); errors += 1
    for g, p in items:
        sure = not p.endswith('?'); piece = p.rstrip('?').replace('_', ' ')
        whole = piece == '-' or ' ' in piece or piece in words_of(cribs[seg]['plaintext'])
        num, mark, _ = parse(g)
        if num is None: continue
        base = piece
        if mark in SUF:
            for s in SUF[mark]:
                if piece.endswith(s) and len(piece) > len(s): base = piece[:-len(s)]; break
        entries[num].append((base, sure, seg, whole))
if errors: sys.exit('fix the alignment first')
with open('key/code15_key_v3.tsv', 'w', encoding='utf-8') as f:
    f.write('group\tvalue\tstatus\tattested\tattested_marked_sure\tconflict\tletters\tnote\n')
    n = collections.Counter()
    for num in sorted(entries, key=int):
        e = entries[num]; c = collections.Counter(x[0] for x in e)
        top, k = c.most_common(1)[0]
        good = [x for x in e if x[0] == top]
        ns = sum(1 for x in good if x[1]); whole = any(x[3] for x in good)
        letters = sorted(set(x[2][0] for x in e))
        conflict = '; '.join(f'{b} ({v})' for b, v in c.items() if b != top)
        # rule (round 3); values seen only in A are at most 'probable'.
        # rule (round 3): "sure" only if marked sure AND (a whole word, a null, or marked sure in two places)
        if conflict: status = 'conflict'
        elif ns and (whole or ns >= 2): status = 'sure'
        else: status = 'unsure'
        note = ''
        if letters == ['A']:
            note = 'only in A: rests on the clear file copy as printed in PTJ 25'
            if status == 'sure': status = 'probable'
        n[status] += 1
        f.write(f'{num}\t{top}\t{status}\t{k}\t{ns}\t{conflict}\t{",".join(letters)}\t{note}\n')
print('key entries', sum(n.values()), dict(n))
