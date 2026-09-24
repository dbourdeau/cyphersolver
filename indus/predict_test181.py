"""Hundred-and-eighty-first registered prediction set (PREDICTIONS.md, LS1-LS8): decipherment loop 6, a world-wide language
search by rebus substitution. Each CLICS4 language's basic words for what the signs depict are scored by how well they
make substitutable signs sound alike. Writes results/predict_test181.md."""
import csv
import io
import os
import random
import zipfile
from collections import Counter, defaultdict

import numpy as np

import predict_test13 as T
import rtools as R
from noun_class import HUMAN
from predict_test179 import M, subst_pairs
from signs import CRAB, FIG, FISH, load

random.seed(221)
CL4 = os.environ.get('CLICS4', 'C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher--claude-worktrees-florence-1414-'
                     'cipher-160632/03a95ee0-e290-45c7-bab7-1e38cbd68d34/scratchpad/clics4/cldf')
RULES = [('woman', 'woman'), ('bow', 'bow'), ('arrow', 'arrow'), ('pot', 'pot'), ('jar', 'pot'), ('container', 'pot'),
         ('tree', 'tree'), ('sun', 'sun'), ('moon', 'moon'), ('crescent', 'moon'), ('rain', 'rainprecipitation'),
         ('mountain', 'mountain'), ('river', 'river'), ('drum', 'drum'), ('comb', 'comb'), ('shield', 'shield'),
         ('sickle', 'sickle'), ('fence', 'fence'), ('roof', 'roof'), ('cover', 'roof'), ('grain', 'grain'), ('leaf', 'leaf'),
         ('pipal', 'leaf'), ('duck', 'duck'), ('bee', 'bee'), ('spear', 'spear'), ('axe', 'axe'), ('basket', 'basket'),
         ('wheel', 'wheel'), ('man', 'person')]


def concept_map():
    cm = {}
    for g in FISH:
        cm[g] = 'fish'
    for g in HUMAN:
        cm.setdefault(g, 'person')
    for g in CRAB:
        cm[g] = 'crab'
    for g in FIG:
        cm[g] = 'fig'
    import re
    for r in csv.DictReader((l for l in open(os.path.join(R.HERE, 'keys', 'fairservis1992_raw.tsv'), encoding='utf-8') if not l.startswith('#')), delimiter='\t'):
        if r['confidence'] in ('sure', 'likely') and r['icit']:
            g = r['icit'].split('|')[0]
            if g in cm:
                continue
            ident = r['gloss'].split('=>')[0].lower()
            words = set(re.findall(r'[a-z]+', ident))
            for kw, c in RULES:
                if kw in words:
                    cm[g] = c
                    break
    return cm


def load_clics(concepts):
    langs = {}
    for r in csv.DictReader(open(os.path.join(CL4, 'languages.csv'), encoding='utf-8')):
        langs[r['ID']] = r
    z = zipfile.ZipFile(os.path.join(CL4, 'forms.csv.zip'))
    words = defaultdict(dict)
    for r in csv.DictReader(io.TextIOWrapper(z.open(z.namelist()[0]), encoding='utf-8')):
        c = r['Parameter_ID']
        if c in concepts and c not in words[r['Language_ID']]:
            seg = r['Segments'].split() or list(r['Form'])
            if seg:
                words[r['Language_ID']][c] = tuple(seg)
    return langs, words


def lev(a, b):
    d = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        p, d[0] = d[0], i
        for j, cb in enumerate(b, 1):
            p, d[j] = d[j], min(d[j] + 1, d[j - 1] + 1, p + (ca != cb))
    return d[-1]


def cpairs(pairs, cm):
    out = Counter()
    for (a, b), w in pairs.items():
        ca, cb = cm.get(a), cm.get(b)
        if ca and cb and ca != cb:
            out[tuple(sorted((ca, cb)))] += w
    return out


def zscore(cp, word, rng, n=200):
    cs = sorted({c for p in cp for c in p if c in word})
    use = [(p, w) for p, w in cp.items() if p[0] in word and p[1] in word]
    tot = sum(w for p, w in use)
    if len(cs) < 12 or tot < 30:
        return None
    ix = {c: i for i, c in enumerate(cs)}
    S = np.zeros((len(cs), len(cs)))
    for i in range(len(cs)):
        for j in range(i + 1, len(cs)):
            a, b = word[cs[i]], word[cs[j]]
            S[i, j] = S[j, i] = 1 - lev(a, b) / max(len(a), len(b), 1)
    I = np.array([ix[p[0]] for p, w in use])
    J = np.array([ix[p[1]] for p, w in use])
    W = np.array([w for p, w in use], dtype=float)
    obs = float((W * S[I, J]).sum() / tot)
    perms = np.array([rng.permutation(len(cs)) for _ in range(n)])
    sims = (W * S[perms[:, I], perms[:, J]]).sum(axis=1) / tot
    sd = sims.std() or 1e-9
    return (obs - sims.mean()) / sd


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-eighty-first registered predictions: decipherment loop 6, a world-wide language search by rebus substitution', 'predict_test181')
    cm = concept_map()
    lexf = lambda g: g not in R.NUMS and g not in M
    bodies = lambda lines: sorted({b for b, e in T.names(lines) if b})
    pa = subst_pairs(bodies(A), lexf)
    pb = subst_pairs(bodies(sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln})), lexf)
    cpa, cpb, cpp = cpairs(pa, cm), cpairs(pb, cm), cpairs(pa + pb, cm)
    rd.say('- mapped signs %d (%s); concept pairs A %d, B %d, pooled %d (weight %d).' % (
        len(cm), dict(Counter(cm.values())), len(cpa), len(cpb), len(cpp), sum(cpp.values())))
    langs, words = load_clics(set(cm.values()))
    rng = np.random.default_rng(5)
    Z = {}
    for lid, wd in words.items():
        zp = zscore(cpp, wd, rng)
        if zp is not None:
            Z[lid] = (zp, zscore(cpa, wd, rng), zscore(cpb, wd, rng))
    ids = sorted(Z, key=lambda k: Z[k][0])
    pct = {k: (i + 1) / len(ids) for i, k in enumerate(ids)}
    fam = lambda k: langs[k]['Family_Name'] or 'unknown'
    ia = lambda k: fam(k) == 'Indo-European' and langs[k]['Longitude'] and langs[k]['Latitude'] and 66 <= float(langs[k]['Longitude']) <= 92 and 6 <= float(langs[k]['Latitude']) <= 36
    dr = [k for k in Z if fam(k) == 'Dravidian']
    iaa = [k for k in Z if ia(k)]
    mean = lambda xs: sum(xs) / max(1, len(xs))
    rd.say('- scored languages %d; Dravidian %d (%s); Indo-Aryan %d (%s).' % (len(Z), len(dr), ', '.join(langs[k]['Name'] for k in dr),
                                                                          len(iaa), ', '.join(langs[k]['Name'] for k in iaa)))
    top = sorted(Z, key=lambda k: -Z[k][0])[:15]
    rd.say('- top 15: %s.' % '; '.join('%s (%s) z %.2f' % (langs[k]['Name'], fam(k), Z[k][0]) for k in top))
    rd.say()
    pd_, pi_ = mean([pct[k] for k in dr]), mean([pct[k] for k in iaa])
    rd.rec('LS1', 'Dravidian ranks high', 'mean percentile %.2f over %d languages' % (pd_, len(dr)), bool(dr) and pd_ >= 0.75)
    rd.rec('LS2', 'Indo-Aryan ranks high', 'mean percentile %.2f over %d languages' % (pi_, len(iaa)), bool(iaa) and pi_ >= 0.75)
    zd, zi = mean([Z[k][0] for k in dr]), mean([Z[k][0] for k in iaa])
    rd.rec('LS3', 'Dravidian above Indo-Aryan', 'mean z %.2f against %.2f' % (zd, zi), bool(dr) and bool(iaa) and zd > zi)
    byf = defaultdict(list)
    for k in Z:
        byf[fam(k)].append(Z[k][0])
    fams = {f: mean(v) for f, v in byf.items() if len(v) >= 5}
    best = max(fams, key=fams.get)
    rd.rec('LS4', 'Dravidian is the best family', 'best of %d families: %s %.2f (Dravidian %s); top five %s' % (
        len(fams), best, fams[best], '%.2f' % fams['Dravidian'] if 'Dravidian' in fams else 'fewer than 5',
        ', '.join('%s %.2f' % kv for kv in sorted(fams.items(), key=lambda kv: -kv[1])[:5])), best == 'Dravidian')
    med = sorted(Z[k][0] for k in Z)[len(Z) // 2]
    rd.rec('LS5', 'the test does not reward every language', 'median z %.2f' % med, med < 0.5)
    both = [k for k in Z if Z[k][1] is not None and Z[k][2] is not None]
    rho = T.spearman([Z[k][1] for k in both], [Z[k][2] for k in both])
    rd.rec('LS6', 'scores are stable across samples', 'Spearman of A-z and B-z over %d languages: %.2f' % (len(both), rho), rho >= 0.3)
    t0 = top[0]
    rd.rec('LS7', 'the top language passes on both samples', '%s: A z %s, B z %s' % (langs[t0]['Name'], '%.2f' % Z[t0][1] if Z[t0][1] is not None else '-',
                                                                              '%.2f' % Z[t0][2] if Z[t0][2] is not None else '-'),
           Z[t0][1] is not None and Z[t0][2] is not None and Z[t0][1] >= 2 and Z[t0][2] >= 2)
    signs = sorted(cm)
    below = 0
    shuf_p = []
    for _ in range(20):
        vals = [cm[g] for g in signs]
        random.shuffle(vals)
        sm = dict(zip(signs, vals))
        cps = cpairs(pa + pb, sm)
        zs = {}
        for lid, wd in words.items():
            zz = zscore(cps, wd, rng, n=100)
            if zz is not None:
                zs[lid] = zz
        o = sorted(zs, key=zs.get)
        pc = {k: (i + 1) / len(o) for i, k in enumerate(o)}
        pdx = mean([pc[k] for k in dr if k in pc])
        shuf_p.append(pdx)
        below += pdx < pd_
    rd.rec('LS8', 'the Dravidian standing depends on the depictions', 'shuffled maps: Dravidian percentile %s; below the real %.2f in %d of 20' % (
        ', '.join('%.2f' % x for x in shuf_p[:8]), pd_, below), below >= 19)
    rd.finish()


if __name__ == '__main__':
    main()
