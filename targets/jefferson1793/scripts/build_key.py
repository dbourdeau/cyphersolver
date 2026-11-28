"""Build Code No. 15 key v1 from the training letters only (B, C, D, E).
Input: key/hand_alignment_training.txt (hand alignment with the decipherments of the time),
transcription/code15_groups.tsv, plaintext/training_cribs.tsv. Checks that each segment's groups are exactly the
transcribed groups in order and that the pieces spell the decipherment; then writes key/code15_key_v1.tsv.
Does not read document A or its crib. Run from output/code15_1793_2026-11-28: python3 scripts/build_key.py"""
import csv, collections, re, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from code15lib import load_groups, parse, words_of

docs = load_groups('transcription/code15_groups.tsv')
cribs = {r['segment']: r for r in csv.DictReader(open('plaintext/training_cribs.tsv', encoding='utf-8'), delimiter='\t')}

def seg_tokens(seg):
    doc = cribs[seg]['doc']; rows = docs[doc]
    toks = [g for (_, _, g) in rows]
    if seg in ('E1', 'E2'):
        cut = next(i for i, t in enumerate(toks) if t.startswith('[del'))
        toks = toks[:cut] if seg == 'E1' else toks[cut + 1:]
    if seg in ('C1', 'C2'):
        toks = [t for (l, _, t) in rows if (l <= 2) == (seg == 'C1')]
    return toks

SUF = {'=': ('s', 'es'), '+': ('ed', 'd')}
entries = collections.defaultdict(list)   # num -> [(base, sure, segment)]
errors = 0
for line in open('key/hand_alignment_training.txt', encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    seg, rest = line.split(':', 1)
    items = [it.rsplit(':', 1) for it in rest.split()]
    toks = seg_tokens(seg)
    if [g for g, _ in items] != toks:
        print('GROUP MISMATCH', seg, [ (a,b) for a,b in zip([g for g,_ in items], toks) if a!=b][:5], len(items), len(toks)); errors += 1
    spelled = ''.join(p.rstrip('?').replace('_', '') for _, p in items)
    crib = ''.join(words_of(cribs[seg]['plaintext']))
    if spelled != crib:
        i = next((k for k in range(min(len(spelled), len(crib))) if spelled[k] != crib[k]), None)
        print('SPELLING MISMATCH', seg, i, spelled[max(0,(i or 0)-15):(i or 0)+15], '|', crib[max(0,(i or 0)-15):(i or 0)+15]); errors += 1
    for g, p in items:
        sure = not p.endswith('?'); piece = p.rstrip('?').replace('_', ' ')
        num, mark, _ = parse(g)
        if num is None: continue
        base = piece
        if mark in SUF:
            for s in SUF[mark]:
                if piece.endswith(s) and len(piece) > len(s): base = piece[:-len(s)]; break
        entries[num].append((base, sure, seg))
if errors: sys.exit('fix the alignment first')
with open('key/code15_key_v1.tsv', 'w', encoding='utf-8') as f:
    f.write('group\tvalue\tstatus\tattested_sure\tattested_unsure\tconflict\tsegments\n')
    n = {'sure': 0, 'unsure': 0, 'conflict': 0}
    for num in sorted(entries, key=int):
        e = entries[num]; c = collections.Counter(b for b, _, _ in e)
        top, k = c.most_common(1)[0]
        ns = sum(1 for b, s, _ in e if b == top and s); nu = sum(1 for b, s, _ in e if b == top and not s)
        conflict = '; '.join(f'{b} ({v})' for b, v in c.items() if b != top)
        status = 'conflict' if conflict else ('sure' if ns else 'unsure')
        n[status] += 1
        f.write(f'{num}\t{top}\t{status}\t{ns}\t{nu}\t{conflict}\t{",".join(sorted(set(s for _,_,s in e)))}\n')
print('key entries', sum(n.values()), n)
