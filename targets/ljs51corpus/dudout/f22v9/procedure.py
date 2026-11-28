#!/usr/bin/env python3
"""LJS 51 f.22v.9 -- procédure gelée (PREREG_v1.md). Agent piste 5, 28/11/2026.

Usage :
  python3 -I procedure.py selftest            # contrôle sur données synthétiques (aucune donnée réelle)
  python3 -I procedure.py measure <outdir>    # LA mesure (après confirmation que l'empreinte est postée sur #1023)

Clé apprise sur une moitié (alignement « hard-EM » signe<->lettre avec insertions/omissions),
décodage de l'autre moitié, accord en caractères = LCS(décodage, clair)/len(clair), 200 témoins
(même procédure, lettres du clair d'apprentissage permutées).
"""
import json, math, os, random, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SEED = 20261128
N_WIT = 200
GAP = math.log(0.02)
ALPHA = 0.5
CRIT_ABS, CRIT_MARGIN = 0.85, 0.30


def load_cipher(path):
    seq = []
    for l in open(path, encoding='utf8'):
        m = re.match(r'^L(\d): (.*)$', l.strip())
        if m:
            seq += m.group(2).split()
    return seq


def load_plain(path):
    merged, hamza = [], []
    for l in open(path, encoding='utf8'):
        if l.startswith('#') or not l.strip():
            continue
        a, b = l.rstrip('\n').split('\t')
        merged.append(a); hamza.append(b)
    return merged, hamza


VARIANTS = [(alph, order, first) for alph in ('merged', 'hamza') for order in ('asis', 'wordrev') for first in ('lbny', 'bny')]


def plain_letters(words, order, first):
    w = list(words)
    if first == 'bny' and w[0] == 'لبني':
        w[0] = 'بني'
    out = []
    for x in w:
        out += list(x[::-1] if order == 'wordrev' else x)
    return out


def align(cip, pla, logp):
    """Needleman-Wunsch global ; logp(c,l) score d'appariement ; GAP pour signe nul ou lettre omise."""
    n, m = len(cip), len(pla)
    S = [[0.0] * (m + 1) for _ in range(n + 1)]
    B = [[None] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        S[i][0] = S[i - 1][0] + GAP; B[i][0] = 'U'
    for j in range(1, m + 1):
        S[0][j] = S[0][j - 1] + GAP; B[0][j] = 'L'
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            d = S[i - 1][j - 1] + logp(cip[i - 1], pla[j - 1])
            u = S[i - 1][j] + GAP
            le = S[i][j - 1] + GAP
            best = max(d, u, le)
            S[i][j] = best
            B[i][j] = 'D' if best == d else ('U' if best == u else 'L')
    pairs = []
    i, j = n, m
    while i > 0 or j > 0:
        b = B[i][j]
        if b == 'D':
            pairs.append((i - 1, j - 1)); i -= 1; j -= 1
        elif b == 'U':
            i -= 1
        else:
            j -= 1
    return pairs[::-1]


def counts_from(pairs, cip, pla):
    C = {}
    for i, j in pairs:
        C.setdefault(cip[i], {}).setdefault(pla[j], 0)
        C[cip[i]][pla[j]] += 1
    return C


def _em(cip, pla, pairs, V):
    for _ in range(30):
        C = counts_from(pairs, cip, pla)
        tot = {c: sum(v.values()) for c, v in C.items()}

        def logp(c, l):
            return math.log((C.get(c, {}).get(l, 0) + ALPHA) / (tot.get(c, 0) + ALPHA * V))
        new = align(cip, pla, logp)
        if new == pairs:
            break
        pairs = new
    C = counts_from(pairs, cip, pla)
    tot = {c: sum(v.values()) for c, v in C.items()}
    ll = sum(math.log((C[cip[i]][pla[j]] + ALPHA) / (tot[cip[i]] + ALPHA * V)) for i, j in pairs)
    ll += GAP * ((len(cip) - len(pairs)) + (len(pla) - len(pairs)))
    return pairs, C, ll


def learn(cip, pla, restarts=40, seed=1):
    """Hard-EM multi-départs : diagonales décalées (-6..+6) + départs par segments aléatoires ; on garde la
    solution de plus grande vraisemblance (log P(lettre|signe) lissée + pénalités d'écart)."""
    V = max(1, len(set(pla)))
    n, m = len(cip), len(pla)
    inits = []
    for off in range(-6, 7):
        inits.append([(i, i + off) for i in range(n) if 0 <= i + off < m])
    r = random.Random(seed)
    for _ in range(restarts):
        # diagonale par morceaux : 3 points de rupture avec décalage aléatoire -3..+3
        cuts = sorted(r.sample(range(1, n), 3)); off = 0; pr = []; c = 0
        for i in range(n):
            if c < 3 and i == cuts[c]:
                off += r.randint(-3, 3); c += 1
            if 0 <= i + off < m:
                pr.append((i, i + off))
        # retirer les j répétés ou décroissants
        out = []; lastj = -1
        for i, j in pr:
            if j > lastj:
                out.append((i, j)); lastj = j
        inits.append(out)
    best = None
    for pairs in inits:
        pr, C, ll = _em(cip, pla, pairs, V)
        if best is None or ll > best[2] + 1e-9:
            best = (pr, C, ll)
    pairs, C, ll = best
    key = {c: sorted(v.items(), key=lambda kv: (-kv[1], kv[0]))[0][0] for c, v in C.items()}
    return key, pairs, C


def loo(cip, pla, pairs, C):
    ok = 0
    for i, j in pairs:
        c, l = cip[i], pla[j]
        v = dict(C[c]); v[l] -= 1
        v = {k: x for k, x in v.items() if x > 0}
        if v and sorted(v.items(), key=lambda kv: (-kv[1], kv[0]))[0][0] == l:
            ok += 1
    return ok / len(pla)


def lcs(a, b):
    P = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            P[i][j] = P[i - 1][j - 1] + 1 if a[i - 1] == b[j - 1] and a[i - 1] != '?' else max(P[i - 1][j], P[i][j - 1])
    return P[-1][-1]


def run(cip_tr, cip_te, words_tr, words_te, perm_rng=None):
    """Sélection de variante par LOO sur la moitié d'apprentissage seulement, puis décodage du test."""
    best = None
    for vi, (alph, order, first) in enumerate(VARIANTS):
        wtr = words_tr[alph]; wte = words_te[alph]
        ptr = plain_letters(wtr, order, first if words_tr['first_is_word1'] else 'lbny')
        pte = plain_letters(wte, order, first if words_te['first_is_word1'] else 'lbny')
        if perm_rng is not None:
            r = random.Random(perm_rng * 1000 + vi)
            ptr = ptr[:]; r.shuffle(ptr)
        key, pairs, C = learn(cip_tr, ptr)
        s = loo(cip_tr, ptr, pairs, C)
        if best is None or s > best[0]:
            best = (s, (alph, order, first), key, pairs, ptr, pte)
    s, var, key, pairs, ptr, pte = best
    dec = [key.get(c, '?') for c in cip_te]
    score = lcs(dec, pte) / len(pte)
    known = sum(1 for d in dec if d != '?')
    return dict(variant=var, loo=s, key=key, decoded=''.join(dec), plain_test=''.join(pte), score=score,
                coverage=known / len(dec), score_on_known=lcs(dec, pte) / max(1, known),
                pairs=[(i, j) for i, j in pairs])


def split(seq, merged, hamza, inverse=False):
    a, b = (seq[:40], seq[40:]), ({'merged': merged[:11], 'hamza': hamza[:11]}, {'merged': merged[11:], 'hamza': hamza[11:]})
    tr_w, te_w = b
    tr_w['first_is_word1'] = True; te_w['first_is_word1'] = False
    if not inverse:
        return a[0], a[1], tr_w, te_w
    return a[1], a[0], te_w, tr_w


def measure(outdir):
    seq = load_cipher(os.path.join(HERE, 'arbitrage.txt'))
    merged, hamza = load_plain(os.path.join(HERE, 'clair_23r.txt'))
    assert len(seq) == 81 and len(merged) == 21
    os.makedirs(outdir, exist_ok=True)
    res = {}
    for name, inv in (('primaire_apprend_1-40_mesure_41-81', False), ('inverse_apprend_41-81_mesure_1-40', True)):
        ctr, cte, wtr, wte = split(seq, merged, hamza, inv)
        real = run(ctr, cte, wtr, wte)
        wit = [run(ctr, cte, wtr, wte, perm_rng=SEED + k)['score'] for k in range(1, N_WIT + 1)]
        bw = max(wit)
        real['witness_best'] = bw; real['witness_mean'] = sum(wit) / len(wit)
        real['witness_scores'] = wit
        real['n_witnesses'] = len(wit)
        real['pass'] = real['score'] >= CRIT_ABS and real['score'] >= bw + CRIT_MARGIN
        res[name] = real
        print(name, 'variant', real['variant'], 'loo %.3f' % real['loo'], 'score %.3f' % real['score'],
              'best witness %.3f mean %.3f' % (bw, real['witness_mean']), 'PASS' if real['pass'] else 'FAIL')
    json.dump(res, open(os.path.join(outdir, 'resultat.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)


def selftest():
    """Synthétique : texte aléatoire, chiffre homophonique (2 signes pour 3 lettres fréquentes), 2 insertions, 1 omission."""
    r = random.Random(7)
    letters = list('abcdefghijklmnop')
    words = [''.join(r.choice(letters) for _ in range(r.randint(2, 6))) for _ in range(40)]
    flat = ''.join(words)
    hom = {l: ['X' + l + '1', 'X' + l + '2'] if l in 'abc' else ['X' + l] for l in letters}
    cip = [r.choice(hom[l]) for l in flat]
    cip.insert(10, 'Xnull'); cip.insert(len(cip) // 2 + 5, 'Xnull'); del cip[30]
    half = len(cip) // 2
    # coupe au mot le plus proche de la moitié dans le clair
    acc, k = 0, 0
    while acc + len(words[k]) <= half:
        acc += len(words[k]); k += 1
    key, pairs, C = learn(cip[:half], list(''.join(words[:k])))
    dec = [key.get(c, '?') for c in cip[half:]]
    pte = list(''.join(words[k:]))
    print('selftest score %.3f (attendu élevé, sous 1 à cause des classes jamais vues)' % (lcs(dec, pte) / len(pte)))
    key2, pairs2, C2 = learn(cip[:half], r.sample(list(''.join(words[:k])), len(''.join(words[:k]))))
    dec2 = [key2.get(c, '?') for c in cip[half:]]
    print('selftest témoin permuté %.3f' % (lcs(dec2, pte) / len(pte)))


if __name__ == '__main__':
    if sys.argv[1] == 'selftest':
        selftest()
    elif sys.argv[1] == 'measure':
        measure(sys.argv[2])
