"""Each round-2 blind reading scored alone, with no agreement filter (post hoc; outside PLAN.md and PLAN2.md).

python reader_scores.py   -> codes_1810_reader1.txt, codes_1810_reader2.txt, reader_scores.txt

Reading 1 is X for Nos. 23, 25, 27 and 28 and the round-1 blind second reading for No. 24; reading 2 is Y, and Z for
No. 24. No. 21 is left out (its two readings are not independent). The readings are parsed and paired exactly as in
build_round2.py (its code is run up to the point where it writes files), and each group is written as the reading has
it (the lower value where the reader gave two). Witness texts are those of ../codes_1810.txt.
Each file is scored with heldout_1810.py's own rules (run() and pooled(), align.py and ../../code_table.tsv
unchanged). No shuffled control and no pass mark: these figures are not a registered test. Python standard library only.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
B = os.path.dirname(HERE)
sys.path.insert(0, B)
import heldout_1810 as H  # noqa: E402

src = open(os.path.join(HERE, 'build_round2.py'), encoding='utf8').read()
src = src.split("lines = ['# Second round")[0]
g = {'__file__': os.path.join(HERE, 'build_round2.py'), '__name__': 'build_round2_parse'}
exec(compile(src, 'build_round2.py', 'exec'), g)

def fmt(x):
    if x[0] == 'num':
        return f"{sorted(x[1])[0]}{x[2]}"
    return x[1] if x[0] == 'word' else '0'

tab = H.A.load_table([os.path.join(os.path.dirname(B), 'code_table.tsv')])
report = ['# Each round-2 blind reading alone, no agreement filter; scored with heldout_1810.py run() and pooled().',
          '# Post hoc, outside PLAN.md and PLAN2.md; no shuffled control, no pass mark. Built by reader_scores.py.']
for which, name in ((0, 'reader1'), (1, 'reader2')):
    out = [f'# Round-2 {name} alone (no agreement filter), written by reader_scores.py. Format of ../../codes_ford.txt.']
    for w in g['wit']:
        ref = w['ref']
        if ref.startswith('No. 21'):
            continue
        k = [p for p in g['pairs'] if ref.startswith(p)]
        assert len(k) == 1, ref
        out += ['@ ' + ref, '= ' + w['plain'], ' '.join(fmt(x) for x in g['pairs'][k[0]][which])]
    path = os.path.join(HERE, f'codes_1810_{name}.txt')
    with open(path, 'w', encoding='utf8', newline='\n') as f:
        f.write('\n'.join(out) + '\n')
    rows = H.run(H.A.parse(path), tab)
    by = {}
    for r in rows:
        a = by.setdefault(r['ref'].split(',')[0], [0, 0, 0, 0, 0])
        for i, x in enumerate(('known', 'mis', 'new', 'words', 'read')):
            a[i] += r[x]
    report += ['', f'{name} (codes_1810_{name}.txt)', 'despatch\tgroups\tvalued\tknown\tagreement\tread_words_strict']
    for d, (k, m, n, wd, rd) in by.items():
        report.append(f'{d}\t{k+m+n}\t{k+m}\t{k}\t{k/(k+m):.3f}\t{rd}/{wd}')
    K, M, N, W, RD = (sum(v[i] for v in by.values()) for i in range(5))
    report.append(f'all\t{K+M+N}\t{K+M}\t{K}\t{H.pooled(rows):.3f}\t{RD}/{W} = {RD/W:.3f}')
with open(os.path.join(HERE, 'reader_scores.txt'), 'w', encoding='utf8', newline='\n') as f:
    f.write('\n'.join(report) + '\n')
print('\n'.join(report))
