"""Calibration AVANT gel, sur données synthétiques seulement (aucune donnée de 37v.12/38r) :
un vers arabe réel de ~90 lettres (al-Ṣafadī, hors corpus d'entraînement) chiffré par une substitution
aléatoire doit être retrouvé par le recuit au budget prévu. Sert à fixer iters/restarts."""
import sys, time, random, pickle
sys.path.insert(0, sys.argv[1])
from qummi_lib import *

CORP = "/Volumes/SPOF_2/Archives-Veille-cyber/dechiffrements-europe/ljs51/corpus/"
train = read_openiti(CORP + "0750SafiDinHilli.Diwan.JK007639-ara1") + read_openiti(CORP + "0768IbnNubataShacir.Diwan.JK007636-ara1")
t = time.time(); LM = build_lm(train); lex = build_lexicon(train)
print("lm", round(time.time() - t, 1), "s ; lexique", len(lex))
pickle.dump((LM, lex), open(sys.argv[2], "wb"))
_s = read_openiti(CORP + "0764Safadi.AlhanSawajic.AOCP20240423140Vols-ara1")
test = [a + " " + b for a, b in zip(_s[::2], _s[1::2]) if 80 <= len((a + b).replace(" ", "")) <= 100]
print("vers test", len(test))
rng = random.Random(7)
ok = 0
for j in range(int(sys.argv[3])):
    plain = rng.choice(test)
    perm = list(range(28)); rng.shuffle(perm)
    key = np.arange(N); key[:28] = perm
    ct = decode(encode(plain), key)
    t = time.time()
    s, k = anneal(LM, encode(ct), rng, iters=int(sys.argv[4]), restarts=int(sys.argv[5]))
    dec = decode(encode(ct), k)
    acc = sum(a == b for a, b in zip(dec, plain) if a != " ") / len(plain.replace(" ", ""))
    print(j, round(time.time() - t, 1), "s acc", round(acc, 2), "lex", round(lexcov(dec, lex), 2), "| vrai lex", round(lexcov(plain, lex), 2))
    ok += acc >= 0.8
print("réussites", ok)
