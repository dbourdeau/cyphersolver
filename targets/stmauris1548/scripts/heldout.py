"""Held-out test: decrypt a blind transcription with a frozen key; compare the 4-gram score per letter and the share
of letters inside common French words with 200 shuffled tables (values permuted among the signs).
python heldout.py <transcription> <key.tsv>"""
import sys, os, random, numpy as np, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from compare import load
H = os.path.dirname(os.path.abspath(__file__)); q = np.load(os.path.join(H, "..", "model", "quad.npy"))
AL = "abcdefghilmnopqrstuxyz"; LI = {c: i for i, c in enumerate(AL)}
rows = load(sys.argv[1]); K = {}
# signs split after the test take the frozen value of the blind reader's own class (as in check_marks.py)
PARENT = {"Lo": "Le", "L1": "Le", "N20": "R"}
if "frozen" in sys.argv[2]: rows = {k: [PARENT.get(t, t) for t in r] for k, r in rows.items()}
for l in open(sys.argv[2], encoding="utf-8"):
    if l.strip() and not l.startswith("# "): p = l.rstrip("\n").split("\t"); K[p[0]] = p[1]
toks = [t for r in rows.values() for t in r]
known = [t for t in toks if t in K]
print(f"tokens {len(toks)}, with a value in the frozen key {len(known)} ({len(known)/len(toks):.1%})")
WORDS = set("le la les de des du et en que qui il ils a au aux par pour sur son sa ses ce ces cest est sont ont auoit roy monsieur nous uous ne pas plus fait faict dict dite bien grand gens tout tous mais comme leur leurs aussi lequel laquelle lesquels encores fort temps estre auoir faire dire seroit pourroit".split())
def score(m):
    s = "".join(m.get(t, "") for t in toks); d = np.array([LI[c] for c in s if c in LI])
    qs = q[d[:-3], d[1:-2], d[2:-1], d[3:]].mean()
    cov = np.zeros(len(s), bool)
    for w in WORDS:
        if len(w) < 3: continue
        for mm in re.finditer(w, s): cov[mm.start():mm.end()] = True
    return qs, cov.mean(), s
qs, cv, s = score(K)
signs = sorted(set(known)); vals = [K[x] for x in signs]
res = []
random.seed(5)
for _ in range(200):
    v = vals[:]; random.shuffle(v); res.append(score(dict(zip(signs, v)))[:2])
r = np.array(res)
print(f"frozen key: 4-gram {qs:.3f}, word cover {cv:.3f}")
print(f"200 shuffled: 4-gram max {r[:,0].max():.3f} mean {r[:,0].mean():.3f}; word cover max {r[:,1].max():.3f} mean {r[:,1].mean():.3f}")
for k, rr in rows.items(): print(f"{k[0]} {k[1]}: " + "".join(K.get(t, "?") for t in rr))
