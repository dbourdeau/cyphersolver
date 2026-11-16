#!/usr/bin/env python3
"""Build the group -> word table from the crib despatches only (No. 35 is never read).
Several alignment runs with jittered settings (fixed seed); an entry is FIRM when, in the best-scoring run, the group is
aligned to the same headword at least twice with a share of at least 2/3, and the same headword is the group's top word in at
least 70% of the runs. Entries seen once, or not stable, are WEAK. Output: crib_table.json / crib_table.tsv"""
import sys, json, math, random, io
from collections import Counter, defaultdict
from align import build
import align2
from align2 import prep, table

def objective(D, A, P):
    tot = 0.0
    for k, d in enumerate(D):
        T = table(D, A, skip=k)
        for op, i, j in A[k]:
            if op == 'M':
                t = T.get(d['G'][i][0]); kk = d['K'][j]; p = P[kk]
                if t: tot += math.log(((t.get(kk, 0) + align2.ALPHA*p)/(sum(t.values()) + align2.ALPHA))/p)
            elif op == 'G': tot -= 1.4
            else: tot -= 1.6
    return tot

def one_run(D, P, rng):
    gapg = rng.uniform(1.0, 1.8); gapw = rng.uniform(1.2, 2.0)
    for d in D:
        own = any(x in d['file'] for x in ('ff132', 'ff185', 'ff219', 'No33', 'No34', 'n36'))
        d['lam_line'] = 0.0 if own else rng.uniform(0.3, 0.8)
        d['lam_diag'] = rng.uniform(0.3, 1.0) if own else 0.0
    A = [align2.align(d, {}, P, d['lam_line'], d['lam_diag'], gapg, gapw) for d in D]
    order = list(range(len(D)))
    for it in range(30):
        changed = 0; f = max(0.25, 1 - it/8.0); rng.shuffle(order)
        for k in order:
            d = D[k]; T = table(D, A, skip=k)
            new = align2.align(d, T, P, d['lam_line']*f, d['lam_diag']*f, gapg, gapw)
            if new != A[k]: changed += 1; A[k] = new
        if not changed: break
    return A

if __name__ == '__main__':
    nrun = int(sys.argv[1]) if len(sys.argv) > 1 else 16
    D = build(); P = prep(D); rng = random.Random(1778)
    runs = []
    for r in range(nrun):
        A = one_run(D, P, rng); sc = objective(D, A, P); runs.append((sc, A))
        print('run', r, 'objective %.1f' % sc, file=sys.stderr)
    runs.sort(key=lambda x: -x[0])
    best = runs[0][1]
    tops = []
    for sc, A in runs:
        T = table(D, A); tops.append({g: max(t, key=t.get) for g, t in T.items()})
    Tb = table(D, best)
    # phrase glosses and example forms from the best run
    forms = defaultdict(Counter); occs = defaultdict(list)
    for k, d in enumerate(D):
        pend = []
        for op, i, j in best[k]:
            if op == 'W': pend.append(d['W'][j][0])
            elif op == 'M':
                g = d['G'][i][0]; forms[g][' '.join(pend + [d['W'][j][0]])] += 1
                occs[g].append([d['file'].split('/')[-1], i, d['K'][j]]); pend = []
            else: pend = []
    allg = Counter(g for d in D for g, _, _ in d['G'])
    out = {}
    for g, n in sorted(allg.items()):
        t = Tb.get(g, Counter())
        e = {'seen': n, 'aligned': sum(t.values()), 'words': dict(t.most_common()), 'forms': dict(forms[g].most_common())}
        if t:
            w, c = t.most_common(1)[0]
            stab = sum(1 for tp in tops if tp.get(g) == w)/len(tops)
            e['top'] = w; e['top_n'] = c; e['stability'] = round(stab, 2)
            e['grade'] = 'firm' if (c >= 2 and c/sum(t.values()) >= 2/3 and stab >= 0.7) else 'weak'
        else:
            e['grade'] = 'none'
        out[g] = e
    json.dump({'runs': [r[0] for r in runs], 'table': out, 'best_alignment': best, 'files': [d['file'] for d in D]}, open('crib_table.json', 'w'), indent=0)
    with open('crib_table.tsv', 'w') as fh:
        fh.write('group\tgrade\theadword\ttimes_aligned_to_it\ttimes_aligned\ttimes_seen\tstability\tforms\n')
        for g, e in out.items():
            fh.write('%d\t%s\t%s\t%s\t%d\t%d\t%s\t%s\n' % (g, e['grade'], e.get('top', ''), e.get('top_n', ''), e['aligned'], e['seen'], e.get('stability', ''), '; '.join('%s x%d' % kv for kv in e['forms'].items())))
    c = Counter(e['grade'] for e in out.values())
    print('groups in cribs:', len(out), dict(c))
    print('objectives:', ['%.0f' % r[0] for r in runs])
