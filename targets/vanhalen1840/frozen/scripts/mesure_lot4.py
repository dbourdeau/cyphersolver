"""mesure_lot4.py — MESURE UNIQUE sur H (S7, S8) selon PROTOCOLE-AVENANT-LOT4.md. NE PAS RELANCER.
python3 -I scripts/mesure_lot4.py
Écrit sa sortie brute dans RESULTAT-LOT4-sortie-brute.txt (création exclusive : refuse si le fichier existe).
"""
import os, sys, io, hashlib, contextlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lot4lib as L
M = L.M

OUT = os.path.join(L.ROOT, 'RESULTAT-LOT4-sortie-brute.txt')
C1, DK, DG = 0.75, 0.22, 0.08          # seuils calibrés (scripts/calib_lot4.out), recopiés dans l'avenant
P1 = os.path.join(L.ROOT, 'transcription.txt')      # passe 1 : décisive (P01)
P2 = os.path.join(L.ROOT, 'transcription-p2.txt')   # passe 2 : information seulement

DRY = '--dry-T' in sys.argv   # essai à blanc sur T (S1 tronquée à 10, S2 à 15) : n'écrit rien dans le dossier, ne lit pas H
if DRY:
    OUT = os.path.join(os.environ.get('TMPDIR', '/tmp'), 'dry-mesure-lot4.txt')
    if os.path.exists(OUT):
        os.replace(OUT, OUT + '.old')
if os.path.exists(OUT):
    sys.exit('MESURE DEJA JOUEE (%s existe) : ne pas relancer' % OUT)

# 1. vérification du gel
bad = []
for line in open(os.path.join(L.ROOT, 'AVENANT-LOT4.sha256'), encoding='utf-8'):
    if line.startswith('#') or not line.strip():
        continue
    h, f = line.split(None, 1)
    f = f.strip()
    p = f if os.path.isabs(f) else os.path.join(L.ROOT, f)
    got = hashlib.sha256(open(p, 'rb').read()).hexdigest()
    if got != h:
        bad.append(f)
if bad:
    sys.exit('GEL ROMPU : %s' % ', '.join(bad))

buf = io.StringIO()


def say(*a):
    print(*a)
    print(*a, file=buf)


say('gel verifie (AVENANT-LOT4.sha256)')
lex = M.load_lex(L.LEX)
lm = L.LM()
key = M.load_key(L.KEYF)


def show(runs):
    for (sid, ts), s in zip(runs, L.strings(runs, key)):
        say('%s\t%s' % (sid, ' '.join('%s=%s' % (t, M.norm(key.get(t, '?')) or '?') for t in ts)))
        say('%s\t%s' % (sid, s))


# 2. mesure P01 d'origine (measure.py haché, exécuté tel quel avec KEY.tsv sur la passe 1)
say('--- P01 (scripts/measure.py, inchange) sur H, passe 1 ---')
f = io.StringIO()
with contextlib.redirect_stdout(f):
    M.main([P1, L.KEYF, L.LEX] + (['--part', 'T'] if DRY else []))
for l in f.getvalue().rstrip('\n').split('\n'):
    say(l)

# 3. mesure LOT4 (decisive), passe 1
H = L.load_runs(P1, 'H') if not DRY else [(s, t[:n]) for (s, t), n in zip(L.load_runs(P2, 'T')[:2], (10, 15))]
assert DRY or [s for s, _ in H] == ['S7', 'S8'] and [len(t) for _, t in H] == [10, 15], 'H inattendue'
say('--- LOT4 : decodage brut H, passe 1 (cle gelee KEY.tsv, aucune correction) ---')
show(H)
car, lmpl = L.metrics(H, key, lex, lm)
K, G = L.witnesses(H, key, lex, lm, 200, 200, 2423, 2424)
c1, c2, c3, mK, mG = L.rule(car, lmpl, K, G, C1, DK, DG)
say('H : %d nombres (%d hors 70)' % (sum(len(t) for _, t in H), sum(1 for _, t in H for x in t if x != '70')))
say('car = %.3f ; lm/lettre = %.3f' % (car, lmpl))
say('200 cles melangees : max car %.3f ; max lm %.3f' % (max(x[0] for x in K), mK))
say('200 permutations de groupes : max car %.3f ; max lm %.3f' % (max(x[0] for x in G), mG))
say('C1 car>=%.2f : %s ; C2 lm>=%.3f : %s ; C3 lm>=%.3f : %s' % (C1, c1, mK + DK, c2, mG + DG, c3))
say('MESURE LOT4 :', 'VALIDEE' if (c1 and c2 and c3) else 'NON VALIDEE')

# 4. information (non decisive) : passe 2
H2 = L.load_runs(P2, 'H') if not DRY else H
say('--- information : H passe 2 (non decisive) ---')
show(H2)
car2, lm2 = L.metrics(H2, key, lex, lm)
say('passe 2 : car = %.3f ; lm/lettre = %.3f' % (car2, lm2))

with open(OUT, 'x', encoding='utf-8') as fo:
    fo.write('# sortie brute de scripts/mesure_lot4.py (execution unique)\n')
    fo.write(buf.getvalue())
