"""Held-out test: decode the 14 June 1814 groups with WE025 alone and score against the clerk's interlinear decode.
Controls: 200 keys made by shuffling WE025's elements over its numbers (seeded). Score = matched letters (difflib
matching blocks) between the concatenated letters of the decode and of the clerk's words, and the SequenceMatcher ratio.
Groups as transcribed before this work (Daniel's ciphertext_1814.txt), and again with the two image rereads (337->338, 435->485).

    python3 scripts/heldout_1814.py                        WE025 score only, from key/we025_poinsett.tsv (stdout)
    python3 scripts/heldout_1814.py --full-table PATH      also the 200 shuffled keys; writes ../tests/heldout_1814_result.txt

The control shuffles all 1592 elements of WE025 over its numbers, so it needs our full transcription of the table
(we025_table.tsv, sha256 in key/we025_SHA256.txt), which is not in the repository. As on 11 Nov 2026, the table is used
as frozen, without the post-freeze correction of 668 (668 does not occur in the 1814 letter; the WE025 score is the same
either way, and the shuffled keys are the same only without it)."""
import re, random, difflib, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import texts
OUT = texts.BEL
FULL = sys.argv[sys.argv.index('--full-table') + 1] if '--full-table' in sys.argv else None
we = texts.load_key(post_freeze=False)
full = texts.load_key(FULL, post_freeze=False) if FULL else None
rows = texts.load_1814()
clerk = ''.join(re.sub(r'[^a-z]', '', re.sub(r'\[number\]', '', r['gloss'].lower())) for r in rows)

def letters(key, groups):
    return ''.join(re.sub(r'[^a-z]', '', key.get(int(g), '').lower()) for g in groups)

def score(key, groups):
    d = letters(key, groups)
    sm = difflib.SequenceMatcher(None, d, clerk, autojunk=False)
    return sum(b.size for b in sm.get_matching_blocks()), sm.ratio(), d

def run(groups, tag, report):
    m, r, d = score(we, groups)
    nums = list(full.keys()) if full else []; els = [full[n] for n in nums]
    rng = random.Random(20261111)
    report.append(f'{tag}: groups={len(groups)} clerk_letters={len(clerk)} decode_letters={len(d)}')
    report.append(f'  WE025: matched letters {m}, ratio {r:.3f}')
    if not full:
        report.append('  shuffled keys: not run (needs --full-table)')
        return d
    ctrl = []
    for i in range(200):
        e = els[:]; rng.shuffle(e)
        ctrl.append(score(dict(zip(nums, e)), groups)[:2])
    cm = sorted(c[0] for c in ctrl); cr = sorted(c[1] for c in ctrl)
    mean = sum(cr) / len(cr); sd = (sum((x - mean) ** 2 for x in cr) / len(cr)) ** .5
    report.append(f'  shuffled x200: matched letters median {cm[100]}, best {cm[-1]}; ratio mean {mean:.3f} sd {sd:.3f} best {cr[-1]:.3f}; z(ratio) = {(r-mean)/sd:.1f}')
    return d

report = []
g0 = [g for r in rows for g in r['groups']]
run(g0, 'as transcribed (Daniel ciphertext_1814.txt, RC + Duplicate ends)', report)
g1 = [{'337': '338', '435': '485'}.get(g, g) for g in g0]
run(g1, 'with image rereads 337->338, 435->485', report)
report.append('')
report.append('Line by line, WE025 elements (as transcribed, rereads in brackets), then the clerk:')
for r in rows:
    el = []
    for g in r['groups']:
        gg = {'337': '338', '435': '485'}.get(g, g)
        e = we.get(int(gg), '??')
        el.append(f'{e}' if gg == g else f'{e}[{g}->{gg}]')
    report.append(f"{r['label']:4} {' '.join(r['groups'])}")
    report.append(f"     WE025: {' | '.join(el)}")
    report.append(f"     clerk: {r['gloss']}")
if full: open(OUT / 'tests' / 'heldout_1814_result.txt', 'w', encoding='utf-8').write('\n'.join(report) + '\n')
print('\n'.join(report))
