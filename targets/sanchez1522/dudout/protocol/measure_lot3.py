"""PREREG_lot3 measure for sanchez-1522 (see ../PREREG_lot3.md). Frozen before any decoding of the held-out portion.
usage: measure_lot3.py SIGNS_TXT PAGE KEY_CODES_TSV CORPUS [seed]
Held-out H = every line of SIGNS_TXT whose ref starts with PAGE (R9647_signs.txt, '257r').
K  = Daniel's key unchanged (measure.py load_key) + letter map SIGNS3 (measure.py SIGNS + Daniel's own labels).
K' = K + the four proposed code values ADJ (C03).  Score S = measure.py LM per-char log-prob (4-gram, Quijote).
Sanity: 200 C1 (permuted K') + 200 C2 (shuffled tokens, K').  Gain G = S(K') - S(K);
C3 = 200 controls where the four codes take random values drawn from the key's plain values (seeded)."""
import sys, random
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from measure import SIGNS, LM, clean, load_key, tokens, decode
SIGNS3 = dict(SIGNS); SIGNS3.update({'mo':'h', 'xo':'s', '9':'l', 'OO':'g', 'U':'u', '⊥':'r', '3f':'a', 'x':'h'})
ADJ = {'dud':'vino', 'sod':'govierno', 'lud':'presente', 'cid':'xxii'}
def page_tokens(path, page):
    import tempfile, os
    lines = [l for l in open(path, encoding='utf-8') if l.startswith(page + '.')]
    fd, tmp = tempfile.mkstemp(suffix='.txt'); os.write(fd, ''.join(lines).encode()); os.close(fd)
    t = [x.lstrip('^') for x in tokens(tmp) if x != '|']; os.unlink(tmp); return t
def main():
    tr, page, kp, cp = sys.argv[1:5]; seed = int(sys.argv[5]) if len(sys.argv) > 5 else 20261113
    raw = open(cp, encoding='utf-8').read(); a = raw.find('*** START'); b = raw.find('*** END')
    lm = LM(clean(raw[a:b] if a >= 0 and b > a else raw))
    K = load_key(kp); toks = page_tokens(tr, page)
    K2 = dict(K); K2.update(ADJ)
    occ = {c: toks.count(c) for c in ADJ}
    d0, u0 = decode(toks, K, SIGNS3); d1, u1 = decode(toks, K2, SIGNS3)
    s0, s1 = lm.per_char(d0), lm.per_char(d1); G = s1 - s0
    rng = random.Random(seed); ctrl = []
    codes = list(K2); plains = [K2[c] for c in codes]; sl = list(SIGNS3); sv = [SIGNS3[x] for x in sl]
    for i in range(200):
        p = plains[:]; rng.shuffle(p); v = sv[:]; rng.shuffle(v)
        d, _ = decode(toks, dict(zip(codes, p)), dict(zip(sl, v))); ctrl.append(lm.per_char(d))
    for i in range(200):
        t = toks[:]; rng.shuffle(t); d, _ = decode(t, K2, SIGNS3); ctrl.append(lm.per_char(d))
    mu = sum(ctrl)/len(ctrl); sd = (sum((x-mu)**2 for x in ctrl)/len(ctrl))**.5; z = (s1 - mu)/sd
    pool = sorted(set(clean(v) for c, v in K.items() if c not in ADJ and clean(v)))
    g3 = []
    for i in range(200):
        K3 = dict(K); K3.update({c: rng.choice(pool) for c in ADJ})
        d, _ = decode(toks, K3, SIGNS3); g3.append(lm.per_char(d) - s0)
    beaten = sum(1 for g in g3 if G > g)
    print('held-out', tr, page, 'tokens', len(toks), 'occurrences', occ)
    print('decoded_chars K %d  K\' %d  unknown codes K %d  K\' %d' % (len(d0), len(d1), u0, u1))
    print("S(K) %.4f  S(K') %.4f  G %.5f" % (s0, s1, G))
    print('sanity C1+C2 n=400 mean %.4f sd %.4f max %.4f  z %.2f' % (mu, sd, max(ctrl), z))
    print('C3 gains n=200 mean %.5f max %.5f  G beats %d/200' % (sum(g3)/200, max(g3), beaten))
    ok = len(d1) >= 300 and s1 > max(ctrl) and z >= 5 and sum(occ.values()) >= 1 and G > 0 and beaten >= 190
    print('VERDICT', 'PASS' if ok else 'FAIL')
    print('adopted if PASS:', ' '.join('%s=%s' % (c, ADJ[c]) for c in ADJ if occ[c]) or 'none')
if __name__ == '__main__': main()
