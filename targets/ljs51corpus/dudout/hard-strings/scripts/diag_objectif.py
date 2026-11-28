"""Diagnostic (exploratoire, chaines deja mesurees = grillees) : la cle de Daniel bat-elle la solution aveugle
sous l'objectif du solveur de ljs51-aveugle ? Si oui -> echec de RECHERCHE ; si non -> echec de MODELE.
Lit les scripts/modele de ljs51-aveugle en lecture seule."""
import sys, os, json, subprocess
from array import array
AV = "../ljs51-aveugle"
sys.path.insert(0, AV + "/scripts")
from common import LETTERS, IDX, norm
from sigparse import read_sig
C = "../cyphersolver-pr/clone"
REF = "d8ac608093e1149f9456eaa2c99bb456ca0abc92"
V = 29
T = array('f'); T.frombytes(open(os.environ.get("LM", AV + "/modele/lm4_sp.bin"), "rb").read())
def lm(seq):  # seq: 0=espace, 1..28
    a = b = c = 0; t = 0.0
    for d in seq:
        t += T[((a*V+b)*V+c)*V+d]; a, b, c = b, c, d
    return t
def show(p): return subprocess.run(["git","-C",C,"show",f"{REF}:{p}"],capture_output=True,text=True,check=True).stdout
res = {l.split('\t')[1]: l.split('\t') for l in open(AV+"/mesure/RESULTATS.tsv").read().split('\n')[1:] if l}
LAM = 8.0
out = []
for cid in sys.argv[1:]:
    toks, K, labels = read_sig(f"{AV}/transcriptions/{cid}.sig")
    ke = json.loads(show(f"targets/ljs51corpus/keys_eye/{cid}.json"))
    key = []
    for lab in labels:
        d = {}
        for k, v in ke["key"].get(lab, {}).items():
            n = norm(k.replace('ﻻ', 'لا')) or '?'
            n = n[-1] if n != '?' else n  # lam-alif -> alif (approximation mono-lettre)
            d[n] = d.get(n, 0) + v
        key.append(IDX.get(max(d, key=d.get), 1) if d else 1)
    seq = [0 if t < 0 else key[t] for t in toks]
    L = lm(seq); dist = len(set(key)); O = L - LAM*(K - dist)
    n = len(seq)
    dec = ''.join(' ' if s == 0 else LETTERS[s-1] for s in seq)
    r = res.get(cid)
    out.append((cid, n, K, dist, round(L,1), round(L/n,3), round(O,1), r[6] if r else '-', r[7] if r else '-', dec))
print("chaine\tsymboles\tK\tlettres_cle_Daniel\tlogP_Daniel\tlogP/sym_Daniel\tobjectif_Daniel\tobjectif_aveugle\tlogP/sym_aveugle\tdecodage_Daniel")
for o in out: print('\t'.join(map(str, o)))
