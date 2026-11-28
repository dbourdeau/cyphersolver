"""Diagnostic exploratoire : logP par symbole atteint par le solveur de ljs51-aveugle sur quelques temoins
melanges (meme generateur que mesure.py) vs logP par symbole du clair (cle de Daniel).
usage: diag_temoins.py modele.bin lam chaine n_temoins"""
import sys, random
from multiprocessing import Pool
sys.path.insert(0, "/Users/bdudout/Documents/Veille cyber/dechiffrements-europe/ljs51-aveugle/scripts")
import solve as S
from sigparse import read_sig
AV = "/Users/bdudout/Documents/Veille cyber/dechiffrements-europe/ljs51-aveugle/"
model, lam, cid, nw = sys.argv[1], float(sys.argv[2]), sys.argv[3], int(sys.argv[4])
toks, K, labels = read_sig(AV + f"transcriptions/{cid}.sig")
def job(i):
    import subprocess, os
    t = list(toks)
    if i > 0:
        rnd = random.Random(2811*100003+i); pos = [j for j, x in enumerate(toks) if x >= 0]
        vals = [toks[j] for j in pos]; rnd.shuffle(vals)
        for j, v in zip(pos, vals): t[j] = v
    inp = f"{len(t)}\n{' '.join(map(str,t))}\n{K}\n"
    out = subprocess.run([AV+"scripts/sa", model, str(lam), "20", "500000", str(2811+i)], input=inp, capture_output=True, text=True).stdout.split('\n')
    d, o, l = out[0].split(); key = list(map(int, out[1].split()))
    return i, float(o), float(l), len(set(key))
if __name__=='__main__':
  with Pool(8) as p:
    for i, o, l, dist in p.imap_unordered(job, range(nw+1)):
        print(f"{cid}\t{'reel' if i==0 else 'temoin'+str(i)}\tobjectif={o:.1f}\tlogP/sym={l:.3f}\tlettres={dist}/{K}", flush=True)
