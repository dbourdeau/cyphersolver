"""ljs51-qummi : modèle 4-gramme arabe, lexique, recuit de substitution simple.

Lancer avec /usr/bin/python3 -E (numpy en site utilisateur), cwd hors du dossier de données.
"""
import re, math, random, unicodedata
import numpy as np

ALPHA = list("ابتثجحخدذرزسشصضطظعغفقكلمنهوي")  # 28 lettres
SP = " "
SYMS = ALPHA + [SP]
IDX = {c: i for i, c in enumerate(SYMS)}
N = len(SYMS)  # 29
ABJAD = list("ابجدهوزحطيكلمنسعفصقرشتثخذضظغ")

NORM = {"أ": "ا", "إ": "ا", "آ": "ا", "ٱ": "ا", "ة": "ه", "ى": "ي", "ؤ": "و", "ئ": "ي"}


def normalize(s):
    s = "".join(NORM.get(c, c) for c in s)
    out = []
    for c in s:
        if c in IDX and c != SP:
            out.append(c)
        elif unicodedata.category(c).startswith("M") or c in "ـء":
            continue
        else:
            out.append(SP)
    return re.sub(r" +", " ", "".join(out)).strip()


def read_openiti(path):
    lines = []
    with open(path, encoding="utf-8") as f:
        for ln in f:
            if ln.startswith("#META") or ln.startswith("######"):
                continue
            lines.append(normalize(ln))
    return [l for l in lines if l]


def build_lm(lines, lambdas=(0.6, 0.25, 0.1, 0.05)):
    c1 = np.zeros(N); c2 = np.zeros((N, N)); c3 = np.zeros((N, N, N)); c4 = np.zeros((N, N, N, N))
    for l in lines:
        t = [IDX[SP]] * 3 + [IDX[c] for c in l] + [IDX[SP]]
        a = np.array(t)
        np.add.at(c1, a[3:], 1)
        np.add.at(c2, (a[2:-1], a[3:]), 1)
        np.add.at(c3, (a[1:-2], a[2:-1], a[3:]), 1)
        np.add.at(c4, (a[:-3], a[1:-2], a[2:-1], a[3:]), 1)
    p1 = (c1 + 1) / (c1.sum() + N)
    def cond(c):
        s = c.sum(axis=-1, keepdims=True)
        return np.divide(c, s, out=np.zeros_like(c), where=s > 0)
    p2 = cond(c2); p3 = cond(c3); p4 = cond(c4)
    l4, l3, l2, l1 = lambdas
    P = (l4 * p4 + l3 * p3[None, :, :, :] + l2 * p2[None, None, :, :] + l1 * p1[None, None, None, :])
    return np.log(P)


def build_lexicon(lines, mincount=2):
    from collections import Counter
    c = Counter(w for l in lines for w in l.split())
    return {w for w, n in c.items() if n >= mincount}


def encode(text):
    return np.array([IDX[c] for c in text])


def score_idx(LM, arr):
    a = np.concatenate([[IDX[SP]] * 3, arr, [IDX[SP]]])
    return float(LM[a[:-3], a[1:-2], a[2:-1], a[3:]].sum())


def apply_key(arr, key):
    """key : tableau de longueur N (indice source -> indice cible), espace fixe."""
    return key[arr]


def anneal(LM, arr, rng, iters=6000, restarts=6, t0=3.0, t1=0.05):
    srcs = sorted(set(int(x) for x in arr) - {IDX[SP]})
    best_key, best_s = None, -1e18
    for r in range(restarts):
        key = np.arange(N)
        perm = list(range(len(ALPHA)))
        rng.shuffle(perm)
        key[:len(ALPHA)] = perm
        cur = score_idx(LM, apply_key(arr, key))
        for i in range(iters):
            T = t0 * (t1 / t0) ** (i / iters)
            a = rng.choice(srcs); b = rng.randrange(len(ALPHA))
            if a == b:
                continue
            k2 = key.copy(); k2[a], k2[b] = key[b], key[a]
            s = score_idx(LM, apply_key(arr, k2))
            if s >= cur or rng.random() < math.exp((s - cur) / T):
                key, cur = k2, s
                if cur > best_s:
                    best_s, best_key = cur, key.copy()
    return best_s, best_key


def decode(arr, key):
    return "".join(SYMS[i] for i in key[arr])


def lexcov(text, lex):
    ws = text.split()
    return sum(w in lex for w in ws) / len(ws) if ws else 0.0


def shuffled_control(text, rng):
    letters = [c for c in text if c != SP]
    rng.shuffle(letters)
    out, k = [], 0
    for c in text:
        if c == SP:
            out.append(SP)
        else:
            out.append(letters[k]); k += 1
    return "".join(out)


def table_key(src_seq, dst_seq):
    """Clé lettre->lettre depuis deux suites alignées par position (première occurrence gagne)."""
    m = {}
    for s, d in zip(src_seq, dst_seq):
        if s not in m:
            m[s] = d
    return m


def apply_table(text, m):
    return "".join(m.get(c, "·") if c != SP else SP for c in text)


def dedup(seq):
    out = []
    for c in seq:
        if c not in out:
            out.append(c)
    return out
