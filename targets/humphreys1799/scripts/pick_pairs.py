"""Pick 40 pairs for image check: stratified by group number (8 bins of 200) and frame quotas; seed 14."""
import csv, random
rows = [r for r in csv.DictReader(open('../humphreys1799_2026-11-14/pairs.tsv'), delimiter='\t') if r['uncertain'] == '' and r['value'] not in ('STOP', 'COMMA')]
quota = {'M43-02-0052': 7, 'M43-02-0053': 5, 'M43-02-0044': 4, 'M31-006-0127': 6, 'M31-006-0130': 5, 'M31-006-0253': 7, 'M31-006-0254': 6}
random.seed(14); random.shuffle(rows)
bins = {b: 0 for b in range(8)}; seen = set(); pick = []
for fr, q in quota.items():
    for r in rows:
        if q == 0: break
        if r['frame'] != fr or r['group'] in seen: continue
        b = min(int(r['group']) // 200, 7)
        if bins[b] >= 5: continue
        if fr not in ('M43-02-0044',) and r['source'] != '!': continue
        pick.append(r); seen.add(r['group']); bins[b] += 1; q -= 1
pick.sort(key=lambda r: (r['frame'], r['line'], int(r['pos'])))
for r in pick: print('\t'.join([r['frame'], r['line'], r['pos'], r['group'], r['value'], r['source']]))
print(bins)
