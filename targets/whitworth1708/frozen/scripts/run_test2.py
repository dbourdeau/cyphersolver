"""Second Whitworth test, run once (plans/TEST_PLAN_2_whitworth1708.md).
Table from the two interlined originals (stamped ff. 90 and 110); held-out: bare duplicate f. 49 against the
1886 print (Sbornik vol. 50 No. 22). The table is frozen and hashed before the held-out file is opened.
Usage: python3 -I scripts/run_test2.py   (from the lead's output folder)"""
import sys, json, hashlib, time, os
sys.path.insert(0, 'scripts')
from wlib import score_letter, score_run, control_shuffled_values, control_rotated_runs, pct, norm
from wlib2 import load_build2, combined_table

D = None                # no band: the helper's attachments enter only through the direct entries (plan, step 2)
MIN_COVERED = 40; H_PASS = 0.80; MARGIN = 0.30; CTL_MAX = 0.50
T = 'transcriptions/'
out = 'test2/'
if os.path.exists(out + 'test2_result.json'):
    sys.exit('test2_result.json exists: the test has been run; it is not run again')

runs, paths, units, info = load_build2([
    (T + 'spo_f090_deciphered.txt', T + 'merged_f114.tsv', T + 'adjudication.tsv', 'f114'),
    (T + 'spo_f110_deciphered.txt', T + 'merged_f112.tsv', T + 'adjudication.tsv', 'f112')])
keep, best, fits, conflict = combined_table(runs, paths, units, D, range(10))
table = {k: v[0] for k, v in keep.items()}
with open(out + 'table2_frozen.tsv', 'w', encoding='utf-8') as f:
    f.write('number\tvalue\ttier\n')
    for k in sorted(keep, key=int):
        f.write(f'{k}\t{keep[k][0]}\t{keep[k][1]}\n')
sha = hashlib.sha256(open(out + 'table2_frozen.tsv', 'rb').read()).hexdigest()
stamp = time.strftime('%Y-%m-%d %H:%M:%S %Z')
open(out + 'table2_frozen.sha256', 'w').write(f'{sha}  table2_frozen.tsv  frozen {stamp}, before the held-out file was opened\n')
with open(out + 'build2_alignment.tsv', 'w', encoding='utf-8') as f:
    al = best[2]
    for r, (groups, text) in enumerate(runs):
        if al.seg[r] is None:
            f.write(f'{r}\tNOT ALIGNED\n'); continue
        f.write(f'{r}\t' + ' '.join(f'{g or "?"}={p}' for g, p in zip(groups, al.seg[r])) + '\n')
print(f'band D={D}; build: {info}')
tiers = {t: sum(v[1] == t for v in keep.values()) for t in 'SAB'}
print(f'table: {len(table)} entries {tiers}; numbers left out for conflicting glosses: {sorted(conflict, key=int)}; sha256 {sha}; frozen {stamp}')

# ---- only now the held-out letter ----
d = json.load(open(T + 'runs_f049.json'))
held = [(r['groups'], norm(''.join(r['print_words']))) for r in d['runs']]
s = score_letter(held, table)
c1 = control_shuffled_values(held, table, 1000, 1708)
c2 = control_rotated_runs(held, table)
p99 = pct(c1, 0.99)
if s['covered'] < MIN_COVERED or p99 > CTL_MAX:
    verdict = 'VOID'
elif s['H'] >= H_PASS and s['H'] - p99 >= MARGIN:
    verdict = 'PASS'
else:
    verdict = 'MISS'
per_run = []
for r, (g, t) in zip(d['runs'], held):
    h, cov, l, ok = score_run(g, t, table)
    per_run.append(dict(run=r['run'], place=r['place'], groups=len(g), covered=cov, hits=h, tiled=ok,
                        exact=(ok and cov == len(g) and h == cov), text=t,
                        reading=' '.join((table[x] if x in table else f'<{x}>') for x in g)))
ins = score_letter(runs, table)
res = dict(test='whitworth1708 second test', run_at=stamp, band=D, build=info, table_size=len(table),
           tiers=tiers, conflicting=sorted(conflict, key=int),
           table_sha256=sha, held_out=s, control1=dict(n=len(c1), median=pct(c1, 0.5), p95=pct(c1, 0.95), p99=p99, max=c1[-1]),
           control2=dict(n=len(c2), max=(c2[-1] if c2 else None), values=c2), in_sample=ins,
           marks=dict(min_covered=MIN_COVERED, H_pass=H_PASS, margin=MARGIN, control_max=CTL_MAX),
           verdict=verdict, per_run=per_run, seeds_loglik=[(sd, ll) for ll, sd, _ in fits])
json.dump(res, open(out + 'test2_result.json', 'w'), indent=1)
print(f"held-out f. 49: groups {s['groups']}, covered {s['covered']} ({s['coverage']:.1%}), hits {s['hits']}, H {s['H']:.3f}; "
      f"letters under hits {s['hit_letters']}/{s['letters']} ({s['letter_share']:.1%}); untiled runs {s['untiled_runs']}")
print(f"control 1 (1,000 shuffled tables): median {pct(c1,0.5):.2f}, p95 {pct(c1,0.95):.2f}, p99 {p99:.2f}, max {c1[-1]:.2f}")
print(f"control 2 (rotated runs): max {c2[-1] if c2 else float('nan'):.2f}")
print(f"in sample (building letters, office's text): covered {ins['covered']}/{ins['groups']}, hits {ins['hits']}, letters {ins['hit_letters']}/{ins['letters']}")
for q in per_run:
    print(f"  run {q['run']:2d} {q['place']:7s} groups {q['groups']:2d} covered {q['covered']:2d} hits {q['hits']:2d} | print: {q['text']} | table: {q['reading']}")
print('VERDICT:', verdict)
