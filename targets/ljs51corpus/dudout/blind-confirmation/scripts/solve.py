"""Enveloppe Python du solveur C. solve(tokens, K, spaces, lam, R, IT, seed) -> (dir, obj, lmps, decoded)
tokens: liste d'entiers (classe) ou -1 (separateur)."""
import subprocess, os
from common import LETTERS
HERE = os.path.dirname(os.path.abspath(__file__))
MOD = os.path.join(HERE, '..', 'modele')
def solve(tokens, K, spaces, lam, R, IT, seed):
    model = os.path.join(MOD, 'lm4_sp.bin' if spaces else 'lm4_nosp.bin')
    toks = tokens if spaces else [t for t in tokens if t >= 0]
    inp = f"{len(toks)}\n{' '.join(map(str,toks))}\n{K}\n"
    out = subprocess.run([os.path.join(HERE,'sa'), model, str(lam), str(R), str(IT), str(seed)],
                         input=inp, capture_output=True, text=True, check=True).stdout.split('\n')
    d, o, l = out[0].split(); key = list(map(int, out[1].split()))
    seq = toks[::-1] if d == '1' else toks
    dec = ''.join(' ' if t < 0 else LETTERS[key[t]-1] for t in seq)
    return int(d), float(o), float(l), dec, key
