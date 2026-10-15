"""Corrected solver for (a) and any other letter file: simulated annealing on a substitution key.
modes: bij  = bijective (swap-only) substitution, symbols -> distinct letters
       homo = homophonic (a letter may own several symbols) but with a unigram chi-square penalty
              so the key cannot collapse onto 'e'/'n' as the old solve_a.py did.
usage: solve_a2.py <file: a|b|d> <lang nl|fr|en> <mode bij|homo> <seconds> [seed]"""
import re, json, math, os, random, sys, collections, time
HERE = os.path.dirname(os.path.abspath(__file__))
which, lang, mode = sys.argv[1], sys.argv[2], sys.argv[3]
SECONDS = float(sys.argv[4]); random.seed(int(sys.argv[5]) if len(sys.argv) > 5 else 1)

def load_groups(which):
    if which == "a":
        t = open(os.path.join(HERE, "a_beverning_1653.txt"), encoding="utf-8").read()
        segs = re.findall(r"--- CIPHER passage \d ---\n(.*?)\n--- clear", t, re.S)
        return [re.findall(r"\d+", s) for s in segs]
    if which == "b":
        return [["18","15","4","20","87","20","1"], ["12","17","24","15","8","15","17","20","18","15","9","7","6","13","20"]]
    if which == "d":
        t = open(os.path.join(HERE, "..", "waddall1656", "d_waddall_1656.txt"), encoding="utf-8").read()
        seg = re.search(r"--- CIPHER \(inline\) ---\n(.*?)\n--- end", t, re.S).group(1)
        return [re.findall(r"\d+", w) for w in re.split(r"[A-Za-z][A-Za-z',]*", seg) if re.findall(r"\d+", w)]
segs = load_groups(which)
groups = [g for s in segs for g in s]
MERGE = dict(p.split(":") for p in sys.argv[8].split(",")) if len(sys.argv) > 8 else {}   # e.g. "22:20" = treat 22 as 20
groups = [MERGE.get(g, g) for g in groups]; segs = [[MERGE.get(g, g) for g in s] for s in segs]
low = [int(g) for g in groups if int(g) < 100]          # 3-digit groups are code words: skipped
syms = sorted(set(low)); N = len(low)
cnt = collections.Counter(low)
lmpath = os.path.join(HERE, f"lm_{lang}.json") if lang != "en" else os.path.join(HERE, "..", "beale", "en_lm.json")
J = json.load(open(lmpath))["quad"]; TOT = sum(J.values())
LM = {k: math.log10(v / TOT) for k, v in J.items()}; FLOOR = math.log10(0.01 / TOT)
uni = collections.Counter()
for q, v in J.items(): uni[q[0]] += v
UT = sum(uni.values()); UNI = {l: uni[l] / UT for l in "abcdefghijklmnopqrstuvwxyz"}
letters_by_freq = [l for l, _ in uni.most_common()]
ALPH = "abcdefghijklmnopqrstuvwxyz"

def quad(pt):
    # score across segment boundaries too (segments are contiguous in the letter, only clear text between)
    return sum(LM.get(pt[i:i+4], FLOOR) for i in range(len(pt) - 3))
def chi(key):
    c = collections.Counter()
    for s in syms: c[key[s]] += cnt[s]
    return sum((c[l] - N * UNI[l]) ** 2 / (N * UNI[l] + 1) for l in ALPH)
LAM = float(sys.argv[6]) if len(sys.argv) > 6 else 0.15  # weight of the unigram penalty (homo mode)
MAXH = int(sys.argv[7]) if len(sys.argv) > 7 else 26        # max symbols per letter (homo mode)
def score(key):
    pt = "".join(key[n] for n in low)
    s = quad(pt)
    if mode == "homo": s -= LAM * chi(key)
    return s

def init():
    order = [s for s, _ in cnt.most_common()]
    if mode == "bij":
        pool = letters_by_freq[:len(syms)] if len(syms) <= 26 else letters_by_freq + list("aeiou")[:len(syms) - 26]
        pool = pool[:len(syms)]; random.shuffle(pool)
        return dict(zip(syms, pool))
    return {s: letters_by_freq[i % 26] for i, s in enumerate(order)}
def climb(deadline):
    key = init(); cur = best = score(key); bestk = dict(key); T0 = 3.0
    it = 0
    while time.time() < deadline:
        it += 1
        T = max(0.05, T0 * (0.99985 ** it))
        k2 = dict(key)
        if mode == "homo" and random.random() < 0.4:
            s0 = random.choice(syms); l0 = random.choice(ALPH)
            if sum(1 for s in syms if key[s] == l0) >= MAXH: continue
            k2[s0] = l0
        else:
            a, b = random.sample(syms, 2); k2[a], k2[b] = key[b], key[a]
        sc = score(k2)
        if sc > cur or random.random() < math.exp((sc - cur) / T):
            key, cur = k2, sc
            if cur > best: best, bestk = cur, dict(key)
        if it % 30000 == 0:      # periodic restart from best
            key, cur = dict(bestk), best
    return best, bestk
t_end = time.time() + SECONDS
results = []
while time.time() < t_end:
    results.append(climb(min(t_end, time.time() + max(5.0, SECONDS / 8))))
results.sort(key=lambda x: -x[0])
print(f"file={which} lang={lang} mode={mode} letters={N} symbols={len(syms)} restarts={len(results)}")
print("score = sum log10 quadgram (+penalty); per-quad avg shown. Real text ~ -3.0..-3.4 per quad, random ~ -6")
seen = set()
for sc, key in results:
    pt = "".join(key[n] for n in low)
    if pt in seen: continue
    seen.add(pt)
    print(f"\n{sc/(N-3):.3f} (quad-only {quad(pt)/(N-3):.3f}, chi {chi(key):.0f})  key: " + " ".join(f"{s}={key[s]}" for s in syms))
    for s in segs:
        print("   " + "".join((key[int(g)] if int(g) < 100 else f"[{g}]") for g in s))
    if len(seen) >= 4: break
