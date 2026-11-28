"""Build Code No. 14 key v1 from groups 1-132 only. Checks that the alignment's groups equal the working sequence 1-132 and
that its pieces spell the start of Taylor's decipherment; writes key/code14_key_v1.tsv. A group whose pieces disagree is
written with status "conflict" and its majority value (more than half the attestations), else no value. Run from output/code14_2026-11-28: python3 -I scripts/build_key.py"""
import collections, sys, os
sys.path.insert(0, os.path.join(os.getcwd(), 'scripts'))
from code14lib import load_groups, clean, words_of, crib
train = [g for (p, g, part) in load_groups() if part == 'training']
items = []
for line in open('key/hand_alignment_training.txt', encoding='utf-8'):
    if line.startswith('#') or not line.strip(): continue
    items += [it.split(':', 1) for it in line.split()]
if [g for g, _ in items] != train:
    bad = [(i + 1, a, b) for i, (a, b) in enumerate(zip([g for g, _ in items], train)) if a != b][:5]
    sys.exit(f'GROUP MISMATCH {len(items)} vs {len(train)} {bad}')
spelled = ''.join(p.rstrip('?').replace('_', '') for _, p in items)
text = ''.join(words_of(crib()))
if not text.startswith(spelled):
    i = next(k for k in range(len(spelled)) if spelled[k] != text[k]); sys.exit(f'SPELLING MISMATCH at {i}: {spelled[i-15:i+15]} | {text[i-15:i+15]}')
print('training covers', len(spelled), 'of', len(text), 'letters; ends', spelled[-20:])
entries = collections.defaultdict(list)
for pos, (g, p) in enumerate(items, 1):
    num = clean(g)
    if num: entries[num].append((p.rstrip('?').replace('_', ' '), not p.endswith('?'), pos))
n = collections.Counter()
with open('key/code14_key_v1.tsv', 'w', encoding='utf-8') as f:
    f.write('group\tvalue\tstatus\tattested_sure\tattested_unsure\tconflict\tpositions\n')
    for num in sorted(entries, key=int):
        e = entries[num]; c = collections.Counter(b for b, _, _ in e)
        if len(c) > 1:
            top, k = c.most_common(1)[0]
            status, value = 'conflict', (top if 2 * k > len(e) else '')   # majority value kept, as in the Code No. 15 key
            conflict = '; '.join(f'{b} ({k})' for b, k in c.most_common())
            ns = nu = 0
        else:
            value = e[0][0]; ns = sum(1 for _, s, _ in e if s); nu = len(e) - ns
            status = 'sure' if ns else 'unsure'; conflict = ''
        n[status] += 1
        f.write(f'{num}\t{value}\t{status}\t{ns}\t{nu}\t{conflict}\t{",".join(str(p) for _, _, p in e)}\n')
print('key entries', sum(n.values()), dict(n))
