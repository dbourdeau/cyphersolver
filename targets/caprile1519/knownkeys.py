# Known-keys escalation for R1128 (1519 two-tier) and R1137 (Cistarelli, two-digit figures), 2 Oct 2026.
# Keys of the series/archive/decade available here:
#   ../caprile1520/key21.json  1520-21 Caprile sign cipher (moved 14 Oct 2026)
#   pairX/key.json        1519 syllabary from R1130 against its 1882 decipherment 4c (this folder)
#   fixed1519.json        1519 one-letter-per-column values from R1133/7c (this folder)
#   key1519_ann.json      LM-anneal 1519 table (this folder)
#   ../bonzagni1512       Bonzagni (Ippolito's agent at Eger) 1512-14 sign alphabet, word division kept
#   ../sadoleto1482       Este (Sadoleto) 1482 sign alphabet
#   ../buda1489/key.json  Maffeo da Treviglio 1489-92 (Ferrara-Buda) sign alphabet (Somogyi's numbering)
#   DECODE: no key record for Ferrara/Este/ASMo 1490-1550 in the harvested list (research/catalogue_harvest/decode).
# Run: python knownkeys.py [r1128|r1137|all]
import os, sys, re, json, random, collections
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
sys.path.insert(0, ROOT)
from lang import lm
HERE = os.path.dirname(os.path.abspath(__file__))

def cols1519(src):
    out = []
    for line in open(os.path.join(HERE, 't1519.txt'), encoding='utf8'):
        if line.startswith(src + ' '):
            out += [c.rstrip('?') for c in line.split(':', 1)[1].split()]
    return out

def r1128():
    m = lm.load('it-cinquecento', spaces=False)
    cols = cols1519('R1128')
    print('R1128 columns', len(cols), 'distinct', len(set(cols)))
    keys = {}
    px = json.load(open(os.path.join(HERE, 'pairX', 'key.json'), encoding='utf8'))
    keys['pairX syllabary (R1130/4c)'] = {k: max(v, key=v.get) for k, v in px.items()}
    keys['fixed1519 (R1133/7c)'] = json.load(open(os.path.join(HERE, 'fixed1519.json'), encoding='utf8'))
    ka = json.load(open(os.path.join(HERE, 'key1519_ann.json'), encoding='utf8'))
    keys['key1519_ann (anneal)'] = ka if isinstance(ka, dict) else {}
    rnd = random.Random(0)
    for name, k in keys.items():
        hit = [c for c in cols if c in k]
        dec = ''.join(k.get(c, '.') for c in cols)
        runs = [r for r in dec.split('.') if len(r) >= 4]
        txt = ''.join(runs)
        sc = m.per_char(lm.norm(txt, 'early')) if len(txt) > 5 else float('nan')
        ctl = []
        vals = list(k.values())
        for _ in range(20):
            kk = {c: rnd.choice(vals) for c in k}
            d2 = ''.join(kk.get(c, '.') for c in cols)
            t2 = ''.join(r for r in d2.split('.') if len(r) >= 4)
            if len(t2) > 5: ctl.append(m.per_char(lm.norm(t2, 'early')))
        print(f'  {name}: {len(hit)}/{len(cols)} columns have a value ({100*len(hit)/len(cols):.0f} %); '
              f'runs>=4: {len(runs)}, LM {sc:.2f} vs random key {sum(ctl)/max(1,len(ctl)):.2f}')
        print('   ', dec[:190])

def r1137(iters=60000, restarts=6):
    import anneal, fastanneal
    seqs = anneal.runs(os.path.join(HERE, '..', 'cistarelli1520', 'r1137_transcription.txt'))
    toks = [t for s in seqs for t in s]
    nums = [t for t in toks if t.isdigit()]
    print('R1137 tokens', len(toks), 'numeric', len(nums), 'distinct', len(set(toks)))
    print('  units digit of 2-digit groups:', dict(collections.Counter(t[-1] for t in nums if len(t) == 2)))
    print('  known keys of the series are sign alphabets (key21, Bonzagni 1512, Sadoleto 1482, Maffeo 1489, the 1519 '
          'syllabary); none assigns values to two-digit figures, so none can be applied.')
    (s1, k1), tk = fastanneal.run(seqs, iters, restarts, seed=1)
    rnd = random.Random(5)
    sh = toks[:]; rnd.shuffle(sh)
    cut = []; i = 0
    for s in seqs:
        cut.append(sh[i:i + len(s)]); i += len(s)
    (s2, k2), _ = fastanneal.run(cut, iters, restarts, seed=1)
    n = len(toks)
    print(f'  anneal score per token: real {s1/n:.3f}, same tokens shuffled {s2/n:.3f}')
    ti = {t: j for j, t in enumerate(tk)}
    M = fastanneal.M
    for s in seqs[:6]:
        print('   ', ''.join(M.alpha[k1[ti[t]]] for t in s))

if __name__ == '__main__':
    what = sys.argv[1] if len(sys.argv) > 1 else 'all'
    if what in ('r1128', 'all'): r1128()
    if what in ('r1137', 'all'): r1137()
