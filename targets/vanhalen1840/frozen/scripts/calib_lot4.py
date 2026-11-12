"""calib_lot4.py — calibration de l'avenant LOT4 sur T SEUL (S1-S6). H (S7, S8) n'est jamais lue ici.
python3 -I scripts/calib_lot4.py > scripts/calib_lot4.out
"""
import os, sys, random, math, statistics as st
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lot4lib as L
M = L.M

P2 = os.path.join(L.ROOT, 'transcription-p2.txt')
T = L.load_runs(P2, 'T')
assert [s for s, _ in T] == ['S1', 'S2', 'S3', 'S4', 'S5', 'S6']
# contrôle : T (passe 2, '58|5.8' -> 58) = copie de travail Fable T-58.txt
T58 = L.load_runs(os.path.join(L.ROOT, 'fable-lot4-2026-11-11', 'T-58.txt'), 'T')
assert T == T58, 'T differe de T-58.txt'
LEN7, LEN8 = 10, 15          # longueurs des suites de H (nombres, 70 compris), comptées sans lire les valeurs
NPH, NW, NCAND = 300, 200, 20
lex = M.load_lex(L.LEX)
lm = L.LM()
key = M.load_key(L.KEYF)
strict = M.load_key(os.path.join(L.ROOT, 'fable-lot4-2026-11-11', 'KEY-PROPOSAL-strict.tsv'))

W7 = [(i, ts[j:j + LEN7]) for i, (_, ts) in enumerate(T) for j in range(len(ts) - LEN7 + 1)]
W8 = [(i, ts[j:j + LEN8]) for i, (_, ts) in enumerate(T) for j in range(len(ts) - LEN8 + 1)]
pairs = [(a, b) for a in W7 for b in W8 if a[0] != b[0]]
rng = random.Random(1840)
PH = rng.sample(pairs, NPH)
print('T : %d nombres ; fenetres %d (10) x %d (15) -> %d paires, %d pseudo-H tirees (graine 1840)'
      % (sum(len(t) for _, t in T), len(W7), len(W8), len(pairs), NPH))


def perturb(runs, k, r):
    """k nombres remplacés par un autre nombre de la clé (lettre fausse : simule un nombre de H mal prédit
    par l'extension, ou une faute de chiffreur/transcription)."""
    flat = [(a, b) for a, (_, ts) in enumerate(runs) for b in range(len(ts))]
    new = [(s, ts[:]) for s, ts in runs]
    nums = sorted(key)
    for a, b in r.sample(flat, k):
        old = new[a][1][b]
        new[a][1][b] = r.choice([n for n in nums if key[n] != key.get(old)])
    return new


def evaluate(kk, cond, n):
    rows = []
    for idx, ((ia, a), (ib, b)) in enumerate(PH[:n]):
        runs = [('pS7', a), ('pS8', b)]
        if cond:
            runs = perturb(runs, cond, random.Random(10000 * cond + idx))
        car, lmpl = L.metrics(runs, kk, lex, lm)
        K, G = L.witnesses(runs, kk, lex, lm, NW, NW, 2423 + idx, 2424 + idx)
        CK, CG = L.witnesses(runs, kk, lex, lm, NCAND, NCAND, 90000 + idx, 95000 + idx) if cond == 0 else ([], [])
        rows.append(dict(car=car, lm=lmpl, K=K, G=G, CK=CK, CG=CG,
                         maxcarK=max(x[0] for x in K), mK=max(x[1] for x in K), mG=max(x[1] for x in G)))
    return rows


def q(xs, p):
    xs = sorted(xs)
    return xs[min(len(xs) - 1, max(0, int(math.floor(p * len(xs)))))]


def fl(x, step):
    return math.floor(x / step + 1e-9) * step


def power(rows, c1, dK, dG):
    return sum(1 for r in rows if r['car'] >= c1 and r['lm'] >= r['mK'] + dK and r['lm'] >= r['mG'] + dG) / len(rows)


def fpr(rows, c1, dK, dG, which):
    n = ok = 0
    for r in rows:
        for car, lmpl in r[which]:
            n += 1
            ok += car >= c1 and lmpl >= r['mK'] + dK and lmpl >= r['mG'] + dG
    return ok / n


base = evaluate(key, 0, NPH)
cars = [r['car'] for r in base]
gK = [r['lm'] - r['mK'] for r in base]
gG = [r['lm'] - r['mG'] for r in base]
poolK = [x[0] for r in base for x in r['K']]
poolG = [x[0] for r in base for x in r['G']]
print('\n== Cle gelee KEY.tsv (etendue), %d pseudo-H de 10+15 nombres ==' % NPH)
print('car cle : min %.3f p05 %.3f p10 %.3f p20 %.3f mediane %.3f' % (min(cars), q(cars, .05), q(cars, .10), q(cars, .20), st.median(cars)))
print('car temoins (tous) : cles melangees p50 %.3f p99 %.3f ; permutations p50 %.3f p99 %.3f'
      % (q(poolK, .5), q(poolK, .99), q(poolG, .5), q(poolG, .99)))
print('lm/lettre cle : min %.3f p10 %.3f mediane %.3f' % (min(r['lm'] for r in base), q([r['lm'] for r in base], .1), st.median(r['lm'] for r in base)))
print('ecart lm - max(200 cles melangees) : min %.3f p05 %.3f p10 %.3f p20 %.3f mediane %.3f'
      % (min(gK), q(gK, .05), q(gK, .10), q(gK, .20), st.median(gK)))
print('ecart lm - max(200 permutations)   : min %.3f p05 %.3f p10 %.3f p20 %.3f mediane %.3f'
      % (min(gG), q(gG, .05), q(gG, .10), q(gG, .20), st.median(gG)))
p01 = sum(1 for r in base if r['car'] >= 0.85 and r['car'] >= r['maxcarK'] + 0.30) / NPH
print('critere P01 d\'origine (car>=0.85 et car>=max temoin+0.30) : puissance %.3f' % p01)

# selection deterministe des seuils (fixee dans l'avenant AVANT ce calcul)
c1 = fl(q(cars, .05), 0.05)
chosen = None
for qq in (0.20, 0.15, 0.10, 0.05, 0.0):
    dK = max(0.0, fl(q(gK, qq), 0.01))
    dG = max(0.0, fl(q(gG, qq), 0.01))
    pw = power(base, c1, dK, dG)
    fk, fg = fpr(base, c1, dK, dG, 'CK'), fpr(base, c1, dK, dG, 'CG')
    print('  essai q=%.2f : c1=%.2f dK=%.2f dG=%.2f -> puissance %.3f ; faux positifs cles %.4f permutations %.4f'
          % (qq, c1, dK, dG, pw, fk, fg))
    if chosen is None and pw >= 0.80 and fk <= 0.01 and fg <= 0.01:
        chosen = (qq, c1, dK, dG, pw, fk, fg)
if chosen is None:
    print('AUCUN SEUIL ne satisfait puissance >= 0.80 et faux positifs <= 1 % -> mesure non probante')
    sys.exit(0)
qq, c1, dK, dG, pw, fk, fg = chosen
c1_fpK = sum(1 for x in poolK if x >= c1) / len(poolK)
c1_fpG = sum(1 for x in poolG if x >= c1) / len(poolG)
print('\nSEUILS RETENUS : C1 car >= %.2f ; C2 lm >= max(cles melangees) + %.2f ; C3 lm >= max(permutations) + %.2f' % (c1, dK, dG))
print('  puissance (cle juste, pseudo-H intactes) = %.3f ; faux positifs : cles melangees %.4f, permutations %.4f (%d candidats chacun)'
      % (pw, fk, fg, NPH * NCAND))
print('  part des temoins passant C1 seul : cles %.4f permutations %.4f' % (c1_fpK, c1_fpG))
for k in (1, 2):
    rows = evaluate(key, k, NPH)
    print('  robustesse : %d nombre(s) faux dans la pseudo-H -> puissance %.3f' % (k, power(rows, c1, dK, dG)))
srows = evaluate(strict, 0, 100)
print('  comparaison cle stricte (100 pseudo-H, memes seuils, info) : puissance %.3f' % power(srows, c1, dK, dG))
