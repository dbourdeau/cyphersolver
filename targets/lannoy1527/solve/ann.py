"""Joint annealing driver for the Soria -> Lannoy letter (runs under WSL: python3 ann.py ...).

Signs (single cipher signs) get a letter; code groups (two- or three-letter Latin groups) get a whole word from the
option list (wide_words.txt) or stay unknown. Scored by es.lm (build_lm.py) with wsa5 (from targets/cardona1517).

  python3 ann.py control [NW] [ITERS]      matched control: a Danvila MHE 38 passage enciphered in the same system
  python3 ann.py real TOKENFILE [ITERS]    the letter (TOKENFILE from tokens.py)

Environment: RUNS (16), R (restarts per run, 3), PC (class-rule penalty, 4; 0 disables), FIXS "sign=letter ...",
FIXG "group=word ...", NCODE / NLET / NOISE for the control.
"""
import os, re, sys, json, math, random, collections, subprocess, multiprocessing as mp, unicodedata
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
A = 'abcdefghilmnopqrstuxyz'; IX = {c: i for i, c in enumerate(A)}
WS = [l.strip() for l in open('wide_words.txt') if l.strip()]


def norm_words(t):
    t = t.lower().replace('ñ', 'n').replace('ç', 'z'); t = unicodedata.normalize('NFD', t)
    t = ''.join(c for c in t if unicodedata.category(c) != 'Mn').translate(str.maketrans('jvkw', 'iucu'))
    return re.findall(r'[a-z]+', t)


G2 = set(os.environ.get('G2', '').split())   # two-letter tokens to treat as code groups


def is_group(t):
    return len(t) == 3 and t.isalpha() and t.islower() or t in G2


def task(toks, signs, groups, ws, fixg={}, fixs={}, classes=True):
    S = len(signs); si = {s: i for i, s in enumerate(signs)}; gi = {g: i for i, g in enumerate(groups)}
    ids = [si[t] if t in si else S + gi[t] for t in toks]
    out = [f'{len(A)} {S} {len(groups)} {len(ws)} {len(ids)}', ' '.join(map(str, ids))]
    out += [f'{len(w)} ' + ' '.join(str(IX[c]) for c in w) for w in ws]
    out += [f'FIX {gi[g]} {ws.index(w)}' for g, w in fixg.items() if g in gi]
    out += [f'FIXS {si[s]} {IX[v]}' for s, v in fixs.items() if s in si]
    if classes:
        cls = collections.defaultdict(list)
        for i, g in enumerate(groups):
            if len(g) == 3: cls[(g[0], g[2])].append(i)
        cid = 0
        for k, ids_ in sorted(cls.items()):
            if len(ids_) < 2: continue
            out += [f'GCLS {i} {cid}' for i in ids_]; cid += 1
    return '\n'.join(out) + '\n'


def runone(a):
    tk, seed, iters, R, d = a
    os.makedirs(d, exist_ok=True); open(f'{d}/task.txt', 'w').write(tk)
    o = subprocess.run(['./wsa5', 'es.lm', f'{d}/task.txt', str(iters), str(R), str(seed), '-12'],
                       capture_output=True, text=True).stdout
    best = float(re.search(r'BEST (\S+)', o).group(1))
    sm = list(map(int, o.split('\nSM')[1].split('\n')[0].split())); gw = list(map(int, o.split('\nGW')[1].split('\n')[0].split()))
    return best, seed, sm, gw


def anneal(toks, signs, groups, ws, iters, tag, fixg={}, fixs={}):
    runs = int(os.environ.get('RUNS', '16')); R = int(os.environ.get('R', '3'))
    tk = task(toks, signs, groups, ws, fixg, fixs, classes=os.environ.get('PC', '4') != '0')
    with mp.Pool(min(runs, 22)) as p:
        return sorted(p.map(runone, [(tk, s, iters, R, f'runs/{tag}{s}') for s in range(runs)]), reverse=True)


def decode(toks, signs, groups, ws, sm, gw):
    out = []
    for t in toks:
        if t in signs: out.append(A[sm[signs.index(t)]])
        else:
            w = gw[groups.index(t)]; out.append(' [' + (ws[w] if w < len(ws) else '?' + t) + '] ')
    return re.sub(' +', ' ', ''.join(out))


def control(nw, iters):
    rnd = random.Random(int(os.environ.get('CSEED', '1')))
    t = open('../../adrian1521/danvila/mhe38.txt', encoding='utf-8', errors='ignore').read()
    W = norm_words(t); st = rnd.randrange(20000, len(W) - 2 * nw); W = W[st:st + nw]
    wc = collections.Counter(W); ncode = int(os.environ.get('NCODE', '70'))
    codew = [w for w, _ in wc.most_common(ncode)]
    cons = 'bcdfglmprstz'; vow = 'aeiou'; names = set(); code = {}
    for w in codew:   # same-class groups for words with the same first letter, as in the real code
        while True:
            g = cons[IX[w[0]] % len(cons)] + rnd.choice(vow) + rnd.choice('bcdlmnprsxz')
            if g not in names: break
        names.add(g); code[w] = g
    noise = float(os.environ.get('NOISE', '0.0'))
    lc = collections.Counter(c for w in W if w not in code for c in w); signs = []; own = {}
    nlet = int(os.environ.get('NLET', '34'))
    for c, n in lc.most_common():
        k = max(1, round(nlet * n / sum(lc.values()))); own[c] = [f's{len(signs) + i}' for i in range(k)]; signs += own[c]
    toks = []; truth = []
    for w in W:
        if w in code: toks.append(code[w]); continue
        for c in w:
            s = rnd.choice(own[c])
            if rnd.random() < noise: s = rnd.choice(signs)
            toks.append(s); truth.append(c)
    groups = sorted(set(code.values())); ws = WS
    res = anneal(toks, signs, groups, ws, iters, 'c')
    stoks = [x for x in toks if x in signs]
    print(f'control: {len(toks)} tokens, {len(stoks)} sign tokens of {len(signs)} types, '
          f'{len(toks) - len(stoks)} group tokens of {len(groups)} types; iters {iters}')
    inv = {g: w for w, g in code.items()}
    for best, seed, sm, gw in res[:6]:
        dec = [A[sm[signs.index(x)]] for x in stoks]
        lr = sum(a == b for a, b in zip(truth, dec)) / len(truth)
        gr = sum(1 for x in toks if x in code.values() and gw[groups.index(x)] < len(ws) and ws[gw[groups.index(x)]] == inv[x]) / max(1, len(toks) - len(stoks))
        print(f'  seed {seed:2d} score/tok {best / len(toks):.3f}  sign tokens right {lr:.2f}  group tokens right {gr:.2f}')
    best, seed, sm, gw = res[0]
    print('  best run:', decode(toks, signs, groups, ws, sm, gw)[:300])


def real(fn, iters):
    toks = [x for l in open(fn) for x in l.split() if not l.startswith('#00')]
    signs = sorted({t for t in toks if not is_group(t)}); groups = sorted({t for t in toks if is_group(t)})
    fixs = dict(kv.split('=') for kv in os.environ.get('FIXS', '').split())
    fixg = dict(kv.split('=') for kv in os.environ.get('FIXG', '').split())
    ws = WS + [w for w in fixg.values() if w not in WS]
    res = anneal(toks, signs, groups, ws, iters, 'r', fixg, fixs)
    tag = os.environ.get('DUMP', 'last')
    json.dump({'signs': signs, 'groups': groups, 'ws': ws, 'res': res}, open(f'{tag}.json', 'w'))
    print(f'{len(toks)} tokens, {len(signs)} sign types, {len(groups)} group types; iters {iters}')
    for best, seed, sm, gw in res[:4]:
        print(f'{best / len(toks):.3f} seed {seed}', ' '.join(f'{s}={A[sm[i]]}' for i, s in enumerate(signs)))
        print('   ', decode(toks, signs, groups, ws, sm, gw)[:500])
    # agreement of the top runs with the best one, on sign tokens
    b = res[0][2]; st = [t for t in toks if t in signs]
    for best, seed, sm, gw in res[1:8]:
        agree = sum(sm[signs.index(t)] == b[signs.index(t)] for t in st) / len(st)
        print(f'  seed {seed}: agrees with best on {agree:.2f} of sign tokens')


if __name__ == '__main__':
    if sys.argv[1] == 'control':
        control(int(sys.argv[2]) if len(sys.argv) > 2 else 900, int(sys.argv[3]) if len(sys.argv) > 3 else 3000000)
    else:
        real(sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 3000000)
