"""Build a letter 4-gram model from 16th-century French (Montaigne, Essais I, 1595 spelling; Project Gutenberg 48529).
Letters: a-z with j->i, v->u, k->c, w dropped; accents stripped. Output: model/quad.npy (log10 probs)."""
import sys, re, unicodedata, numpy as np, os
src = sys.argv[1]; out = os.path.join(os.path.dirname(__file__), "..", "model"); os.makedirs(out, exist_ok=True)
t = open(src, encoding="utf-8").read()
s, e = t.find("*** START"), t.find("*** END"); t = t[s:e]
t = unicodedata.normalize("NFD", t.lower()); t = "".join(c for c in t if not unicodedata.combining(c))
t = t.replace("j", "i").replace("v", "u").replace("k", "c").replace("w", "")
t = re.sub(r"[^a-z]", "", t)
A = "abcdefghilmnopqrstuxyz"  # 22 letters
idx = {c: i for i, c in enumerate(A)}
t = "".join(c for c in t if c in idx)
n = len(A); q = np.ones((n, n, n, n))
a = np.array([idx[c] for c in t])
np.add.at(q, (a[:-3], a[1:-2], a[2:-1], a[3:]), 1)
q = np.log10(q / q.sum()); np.save(os.path.join(out, "quad.npy"), q)
uni = np.bincount(a, minlength=n) / len(a)
open(os.path.join(out, "alphabet.txt"), "w").write(A + "\n" + " ".join(f"{c}:{u:.4f}" for c, u in zip(A, uni)))
print(len(t), "letters"); print(" ".join(f"{c}:{u:.3f}" for c, u in sorted(zip(A, uni), key=lambda x: -x[1])))
