"""Hundred-and-sixty-eighth registered prediction set (PREDICTIONS.md, CT1-CT10): controls on published claims and on the
count texts. M77 path from the M77 environment variable; Linear B from LINB (predict_test152). Writes
results/predict_test168.md."""
import csv
import json
import os
import random
from collections import Counter, defaultdict

import predict_test13 as T
import rtools as R
import ur3_seals
from predict_test138 import fish_counts
from predict_test152 import LINB
from predict_test157 import kind, profile

random.seed(188)
M77 = os.environ.get('M77', 'C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher--claude-worktrees-florence-1414-'
                     'cipher-160632/03a95ee0-e290-45c7-bab7-1e38cbd68d34/scratchpad/indus_decipher/data/m77_indusscript_real_corpus.csv')
PICT = ('749', '341', '753', '777')


def m77_lines():
    best = {}
    with open(os.path.join(R.HERE, 'data', 'icit_m77_map.tsv'), encoding='utf-8') as f:
        for r in csv.DictReader(f, delimiter='\t'):
            if r['m77'] not in best or int(r['pairs']) > best[r['m77']][1]:
                best[r['m77']] = (r['icit'], int(r['pairs']))
    out = []
    with open(M77, encoding='utf-8') as f:
        for r in csv.DictReader(f):
            out.append(tuple(best.get(g, ('?',))[0] for g in r['sign_sequence'].split()))
    return out


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-sixty-eighth registered predictions: controls on published claims and on the count texts', 'predict_test168')
    allf = [tuple(ln) for r in F for ln in r['seq'] if ln]
    c1 = Counter(v for v, f, t in fish_counts(allf))
    rd.rec('CT1', 'with copies counted, 2 + fish is still commonest', 'values %s' % dict(c1.most_common(6)), c1.most_common(1)[0][0] == 2)
    c2 = Counter(v for v, f, t in fish_counts(m77_lines()))
    rd.rec('CT2', 'in M77, 2 + fish is commonest', 'values %s' % dict(c2.most_common(6)), c2.most_common(1)[0][0] == 2)
    site = {}
    for ln in open(os.path.join(LINB, 'corpus_damos_documents.jsonl'), encoding='utf-8'):
        d = json.loads(ln)
        site[d['id']] = d['site']
    ent = {'Knossos': Counter(), 'Pylos': Counter()}
    q = {'Knossos': defaultdict(Counter), 'Pylos': defaultdict(Counter)}
    islogo = lambda t: (t.isupper() and len(t) >= 2 and not t.isdigit()) or (t.startswith('*') and len(t) >= 4)
    with open(os.path.join(LINB, 'corpus_damos_lines.txt'), encoding='utf-8') as f:
        for ln in f:
            p = ln.rstrip('\n').split('\t')
            if len(p) < 3 or site.get(p[0]) not in ent:
                continue
            s = site[p[0]]
            toks = p[2].split()
            for i, t in enumerate(toks):
                if islogo(t):
                    j = i + 1
                    while j < len(toks) and len(toks[j]) == 1 and toks[j].isupper():
                        j += 1
                    if j < len(toks) and toks[j].isdigit():
                        ent[s][(t, toks[j])] += 1
                        q[s][t][toks[j]] += 1
    shared = [g for g in q['Knossos'] if g in q['Pylos'] and sum(q['Knossos'][g].values()) >= 5 and sum(q['Pylos'][g].values()) >= 5]
    diff = sum(q['Knossos'][g].most_common(1)[0][0] != q['Pylos'][g].most_common(1)[0][0] for g in shared)
    rd.thr('CT3', 'Linear B counts are local too', 'logograms whose commonest quantity differs between the palaces', diff, len(shared), 0.5)
    pe = profile(ent)
    rd.rec('CT4', 'Linear B entries are open', 'entries %s; %.2f, %.2f, %.2f -> %s' % (pe['n'], pe['ratio'], pe['shared'], pe['one'], kind(pe)), kind(pe) == 'person-like')
    il = sorted({tuple(ln) for r in F if r['type'].startswith('SEAL') for ln in r['seq'] if 5 <= len(ln) <= 7})
    U = ur3_seals.load()
    ul = sorted({tuple(cf for l_ in o['lines'] for cf, pos in l_) for o in U.values()})
    ul = [x for x in ul if 5 <= len(x) <= 7]
    rep = lambda xs: sum(len(set(x)) < len(x) for x in xs) / max(1, len(xs))
    ri, ru = rep(il), rep(ul)
    rd.rec('CT5', 'Indus repeats signs as legends repeat words', 'Indus lines %d, repeat %.3f; Ur III legends %d, repeat %.3f; threshold half' % (len(il), ri, len(ul), ru), ri >= ru / 2)

    def shuf(lines, n=1000):
        pool = [g for x in lines for g in x]
        out = []
        for _ in range(n):
            random.shuffle(pool)
            k, sim = 0, []
            for x in lines:
                sim.append(tuple(pool[k:k + len(x)]))
                k += len(x)
            out.append(rep(sim))
        return out
    si = shuf(il)
    rd.rec('CT6', 'Indus avoids repetition', 'real %.3f; shuffled mean %.3f; shuffles above real %d of 1000' % (ri, sum(si) / len(si), sum(x > ri for x in si)), sum(x > ri for x in si) >= 950)
    su = shuf(ul)
    rd.rec('CT7', 'Ur III legends repeat words', 'real %.3f; shuffled mean %.3f; shuffles below real %d of 1000' % (ru, sum(su) / len(su), sum(x < ru for x in su)), sum(x < ru for x in su) >= 950)
    DL = sorted({tuple(t) for t in A + B})
    ns = sorted({(b, e) for b, e in T.names(DL) if b})
    occ = [(b, e, i) for b, e in ns for i, g in enumerate(b) if g in PICT]
    rd.thr('CT8', 'picture signs head names', 'picture-sign tokens in names that are the head (%s)' % dict(Counter(b[i] for b, e, i in occ)),
           sum(i == len(b) - 1 for b, e, i in occ), len(occ), 0.5)
    hd = [e for b, e in ns if b[-1] in PICT]
    rd.thr('CT9', 'picture-headed names take 740', 'names headed by a picture sign ending 740', sum(e == '740' for e in hd), len(hd), 0.9)
    sealnames = {g for r in F if r['type'].startswith('SEAL') for b, e in R.names_in(r) if b for g in b + (e,)}
    cu = [g for r in F if r['type'] == 'TAB:C' for g in r['flat']]
    rd.thr('CT10', 'copper labels use the seal vocabulary', 'copper-tablet tokens whose sign is used in seal names', sum(g in sealnames for g in cu), len(cu), 0.9)
    rd.finish()


if __name__ == '__main__':
    main()
