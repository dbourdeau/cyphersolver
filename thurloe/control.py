"""Matched control for solve_a2.py on letter (a) (Beverning 1653, TSP i.435).

Question: does solve_a2.py's hill-climb recover a cipher of (a)'s size and design? Synthetic ciphertexts copy (a)
exactly: three passages with the same sequence of letter groups and 3-digit code groups (66 + 47 + 15 = 128 letter
tokens, 8 code groups that the solver skips), plaintext taken as whole words so that each code group replaces one
word, and the key drawn so that the letter tokens use:
  bij   a one-to-one substitution (whatever distinct count the plaintext gives, ~20), solved in mode bij
  homo  a homophonic substitution with exactly 25 distinct symbols, as (a) (the most frequent letters get a
        second symbol until 25 are in use), solved in mode homo (LAM 0.5, MAXH 2, the settings of the homo2 runs that gave
        NOTES' best -4.71; the defaults LAM 0.15, MAXH 26 collapse onto e/n, as solve_a2_nl_homo.txt shows)
The climber below is solve_a2.py's code unchanged (init, swap/reassign moves, T0 3.0, decay 0.99985, floor 0.05,
restart-from-best every 30,000 iterations, 8 restarts, best kept), except that each restart runs a fixed
ITERS iterations instead of a wall-clock slice, so trials are comparable across machines.
LMs: quadgram counts built as lm_build.py does (letters only, a-z) from the first 80% of the lang/ corpus;
plaintexts come from the held-out last 20%. nl = nl-gutenberg (the corpus of nl-modern, which replaces
thurloe/lm_nl.json), fr = fr-gutenberg (fr-modern, replaces lm_fr.json), en = en-1640s-history (period English).
Recovery = share of the 128 letter tokens decrypted to the true letter; recovered = >= 80%.

usage: python control.py [trials per cell] [workers] [iters per restart]  -> control_out.txt
"""
import os, sys, re, math, json, random, collections, time
from multiprocessing import Pool

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..'))
ALPH = 'abcdefghijklmnopqrstuvwxyz'
CORPUS = {'nl': 'nl-gutenberg', 'fr': 'fr-gutenberg', 'en': 'en-1640s-history'}
RESTARTS = 8
LAM, MAXH = 0.5, 2     # the settings of the run that gave NOTES' best -4.71 (solve_a2_*_homo2.txt:
                       # chi 30 and score - quad-only = 0.5 x chi; no letter owns more than two symbols)


def layout():
    t = open(os.path.join(HERE, 'a_beverning_1653.txt'), encoding='utf-8').read()
    segs = re.findall(r'--- CIPHER passage \d ---\n(.*?)\n--- clear', t, re.S)
    out = []
    for s in segs:
        lay = []
        for g in re.findall(r'\d+', s):
            if int(g) >= 100: lay.append('C')
            elif lay and isinstance(lay[-1], int): lay[-1] += 1
            else: lay.append(1)
        out.append(lay)
    return out


def corpus(lang):
    from lang import corpora, lm
    words = lm.norm(corpora.text([CORPUS[lang]]), 'modern').split()
    cut = int(len(words) * 0.8)
    train = ''.join(words[:cut])
    cnt = collections.Counter(train[i:i + 4] for i in range(len(train) - 3))
    return cnt, words[cut:]


def sample(words, rnd, lay):
    for _ in range(200000):
        j = rnd.randrange(0, len(words) - 200)
        segs, ok = [], True
        for slot in lay:
            if slot == 'C':
                segs.append(('C', words[j])); j += 1; continue
            s = ''
            while len(s) < slot:
                s += words[j]; j += 1
            if len(s) != slot: ok = False; break
            segs.append(('L', s))
        if ok: return segs
    raise RuntimeError('no sample')


def make(words, rnd, design, LAY):
    for _ in range(2000):
        passages = [sample(words, rnd, lay) for lay in LAY]
        plain = ''.join(s for p in passages for k, s in p if k == 'L')
        freq = collections.Counter(plain)
        letters = [l for l, _ in freq.most_common()]
        nsym = {l: 1 for l in letters}
        if design == 'homo':
            if len(letters) > 25: continue
            i = 0
            while sum(nsym.values()) < 25:
                nsym[letters[i % len(letters)]] += 1; i += 1
        syms = rnd.sample(range(6, 34 + 40), sum(nsym.values()))
        key, pos = {}, 0
        for l in letters:
            key[l] = syms[pos:pos + nsym[l]]; pos += nsym[l]
        cipher = [rnd.choice(key[c]) for c in plain]
        if design == 'homo' and len(set(cipher)) != 25: continue
        return plain, cipher
    raise RuntimeError('no key')


class Climber:
    """solve_a2.py's scorer and climber, lifted verbatim into a class (globals -> attributes)."""
    def __init__(self, J, low, mode, rnd):
        self.mode, self.low, self.random = mode, low, rnd
        TOT = sum(J.values())
        self.LM = {k: math.log10(v / TOT) for k, v in J.items()}; self.FLOOR = math.log10(0.01 / TOT)
        uni = collections.Counter()
        for q, v in J.items(): uni[q[0]] += v
        UT = sum(uni.values()); self.UNI = {l: uni[l] / UT for l in ALPH}
        self.letters_by_freq = [l for l, _ in uni.most_common()]
        self.syms = sorted(set(low)); self.N = len(low); self.cnt = collections.Counter(low)

    def quad(self, pt):
        LM, F = self.LM, self.FLOOR
        return sum(LM.get(pt[i:i + 4], F) for i in range(len(pt) - 3))

    def chi(self, key):
        c = collections.Counter()
        for s in self.syms: c[key[s]] += self.cnt[s]
        return sum((c[l] - self.N * self.UNI[l]) ** 2 / (self.N * self.UNI[l] + 1) for l in ALPH)

    def score(self, key):
        pt = ''.join(key[n] for n in self.low)
        s = self.quad(pt)
        if self.mode == 'homo': s -= LAM * self.chi(key)
        return s

    def init(self):
        order = [s for s, _ in self.cnt.most_common()]
        if self.mode == 'bij':
            lbf, syms = self.letters_by_freq, self.syms
            pool = lbf[:len(syms)] if len(syms) <= 26 else lbf + list('aeiou')[:len(syms) - 26]
            pool = pool[:len(syms)]; self.random.shuffle(pool)
            return dict(zip(syms, pool))
        return {s: self.letters_by_freq[i % 26] for i, s in enumerate(order)}

    def climb(self, iters):
        random, syms = self.random, self.syms
        key = self.init(); cur = best = self.score(key); bestk = dict(key); T0 = 3.0
        it = 0
        while it < iters:
            it += 1
            T = max(0.05, T0 * (0.99985 ** it))
            k2 = dict(key)
            if self.mode == 'homo' and random.random() < 0.4:
                s0 = random.choice(syms); l0 = random.choice(ALPH)
                if sum(1 for s in syms if key[s] == l0) >= MAXH: continue
                k2[s0] = l0
            else:
                a, b = random.sample(syms, 2); k2[a], k2[b] = key[b], key[a]
            sc = self.score(k2)
            if sc > cur or random.random() < math.exp((sc - cur) / T):
                key, cur = k2, sc
                if cur > best: best, bestk = cur, dict(key)
            if it % 30000 == 0:
                key, cur = dict(bestk), best
        return best, bestk


DATA = {}
def winit(langs):
    for l in langs: DATA[l] = corpus(l)
    DATA['LAY'] = layout()


def trial(args):
    lang, design, t, iters = args
    rnd = random.Random(100000 * 'nlfren'.index(lang) + 10000 * (design == 'homo') + t)
    J, words = DATA[lang]
    plain, cipher = make(words, rnd, design, DATA['LAY'])
    c = Climber(J, cipher, 'bij' if design == 'bij' else 'homo', random.Random(t))
    truth = {}
    for g, ch in zip(cipher, plain): truth[g] = ch
    res = max((c.climb(iters) for _ in range(RESTARTS)), key=lambda x: x[0])
    acc = sum(res[1][g] == ch for g, ch in zip(cipher, plain)) / len(plain)
    n4 = len(plain) - 3
    pt = ''.join(res[1][g] for g in cipher)
    return dict(lang=lang, design=design, trial=t, distinct=len(set(cipher)), acc=round(acc, 3),
                best_pq=round(res[0] / n4, 3), best_quad_pq=round(c.quad(pt) / n4, 3),
                true_pq=round(c.score(truth) / n4, 3), true_quad_pq=round(c.quad(plain) / n4, 3),
                plain=plain, decrypt=pt)


if __name__ == '__main__':
    trials = int(sys.argv[1]) if len(sys.argv) > 1 else 30
    workers = int(sys.argv[2]) if len(sys.argv) > 2 else 12
    iters = int(sys.argv[3]) if len(sys.argv) > 3 else 60000
    langs = ['nl', 'fr', 'en']
    jobs = [(l, d, t, iters) for t in range(trials) for l in langs for d in ('bij', 'homo')]
    t0 = time.time(); rows = []
    with Pool(workers, initializer=winit, initargs=(langs,)) as pool:
        for r in pool.imap_unordered(trial, jobs):
            rows.append(r); print(r['lang'], r['design'], r['trial'], r['acc'], r['best_pq'], r['true_pq'], flush=True)
    rows.sort(key=lambda r: (r['lang'], r['design'], r['trial']))
    L = ['Matched control for solve_a2.py on the layout of (a) (control.py)',
         f'(a): 128 letter tokens in passages of 66/47/15 with 8 code groups, 25 distinct symbols, IC 0.051.',
         f'Target results (NOTES, solve_a2_*.txt): best -4.71 per quad (homo, nl), -5.79 (bij, nl).',
         f'{RESTARTS} restarts x {iters} iterations per trial; recovered = >= 80% of letter tokens right.', '']
    for l in langs:
        for d in ('bij', 'homo'):
            R = [r for r in rows if r['lang'] == l and r['design'] == d]; n = len(R)
            if not n: continue
            acc = sorted(r['acc'] for r in R)
            f = lambda c: sum(1 for r in R if c(r))
            L += [f'{l} {d}: {n} trials, distinct symbols median {sorted(r["distinct"] for r in R)[n // 2]}',
                  f'  recovered >= 80%: {f(lambda r: r["acc"] >= 0.8)}/{n};  >= 50%: {f(lambda r: r["acc"] >= 0.5)}/{n};'
                  f'  accuracy median {acc[n // 2]:.2f}, mean {sum(acc) / n:.2f}, min {acc[0]:.2f}',
                  f'  best score per quad median {sorted(r["best_pq"] for r in R)[n // 2]:.2f}; true key median {sorted(r["true_pq"] for r in R)[n // 2]:.2f};'
                  f' solver optimum above true key: {f(lambda r: r["best_pq"] > r["true_pq"] + 1e-9)}/{n}', '']
    L.append(f'elapsed {time.time() - t0:.0f} s'); L.append(''); L.append('per trial:')
    L += [json.dumps(r) for r in rows]
    open(os.path.join(HERE, 'control_out.txt'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    print('\n'.join(L[:40]))
