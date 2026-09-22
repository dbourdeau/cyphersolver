"""Matched control for the 42-sign attack of solve.py (ACA reg. 3225 f. 59r).

Question: at this length, does solve.py's annealer recover a cipher of the design it models?
Synthetic texts copy the target's layout exactly: three runs of 11, 14 and 17 signs, with the dotted word signs
at the same places (run 1 letters 5 + [W][W] + 4; run 2 letters 13 + [W]; run 3 letters 17), i.e. 39 letter
tokens, and the key is drawn so that the ciphertext has exactly 18 distinct alphabet signs + 3 word signs = 21,
as the target. Each run keeps 1-3 words of true clear context either side, as solve.py does.

Plaintext: held-out Catalan (last 20% of the lang/ corpus `ca-gutenberg`, the corpus of ca-modern, which
replaces maria1435/lm). Language model: solve.load_lm() on the first 80%, i.e. the same model family and
builder as the attack, trained on text that never supplies a control plaintext.

Designs:
  mono  one sign per letter (the model solve.py searches; 18 distinct letters in the 39)
  homo  1429-key style: three signs per vowel, one per consonant, homophone chosen at random per occurrence
        (18 distinct signs in the ciphertext)
Per trial, with solve.anneal() unchanged (200,000 iterations per seed):
  free        20 seeds, no crib (the attack's unconstrained run)
  true crib   5 seeds, the first five letters of run 2 pinned to their true values (the 'treua' test)
  false crib  5 seeds, the same five signs pinned to a wrong 5-letter word from the corpus
Recovery = share of the 39 letter tokens whose sign decrypts to the true letter.

usage: python control.py [trials_per_design] [workers]   -> writes control_out.txt
"""
import os, sys, random, re, json, math, collections, time
from multiprocessing import Pool

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..'))
import solve                                    # the attack itself: load_lm, score, anneal, total_score

LAYOUT = [(5, 'W', 'W', 4), (13, 'W'), (17,)]     # letters / word-sign slots per run, as in cipher.txt
WORDSIGNS = [['sq', 'bp'], ['O'], []]               # solve.NOMEN names, so solve.py treats them identically
N_ALPHA_SIGNS = 18                                  # target: 21 distinct = 18 alphabet signs + sq, bp, O
VOWELS = 'aeiou'
SEEDS_FREE, SEEDS_CRIB, ITERS = 20, 5, 200000


def normalise(t):
    t = t.lower()
    for a, b in [('[àá]', 'a'), ('[èé]', 'e'), ('[íï]', 'i'), ('[òó]', 'o'), ('[úü]', 'u')]:
        t = re.sub(a, b, t)
    t = t.replace('ç', 'c').replace('·', '').replace('j', 'i').replace('k', 'c').replace('w', 'u')
    t = re.sub(r'[^a-z ]+', ' ', t)
    return re.sub(r'\s+', ' ', t).strip()


def corpus_split():
    from lang import corpora
    t = normalise(corpora.text(['ca-gutenberg']))
    cut = t.index(' ', int(len(t) * 0.8))
    train, test = t[:cut], t[cut + 1:]
    p = os.path.join(HERE, 'lm', 'control_train.txt')
    os.makedirs(os.path.dirname(p), exist_ok=True)
    if not os.path.exists(p):
        open(p, 'w', encoding='utf8').write(train)
    return p, test.split(' ')


def take_letters(words, j, k):
    """consume whole words from j until exactly k letters; None if a word would overshoot"""
    s = ''
    while len(s) < k:
        if j >= len(words) or not words[j].isalpha():
            return None
        s += words[j]; j += 1
    return (s, j) if len(s) == k else None


def sample_run(words, rnd, layout):
    for _ in range(100000):
        i = rnd.randrange(3, len(words) - 60)
        j, segs = i, []
        ok = True
        for slot in layout:
            if slot == 'W':
                if len(words[j]) < 2: ok = False; break
                segs.append(('W', words[j])); j += 1
            else:
                r = take_letters(words, j, slot)
                if r is None: ok = False; break
                segs.append(('L', r[0])); j = r[1]
        if ok:
            return ' '.join(words[i - 2:i]), segs, ' '.join(words[j:j + 3])
    raise RuntimeError('no sample')


def make_trial(words, rnd, design):
    for _ in range(5000):
        runs = [sample_run(words, rnd, lay) for lay in LAYOUT]
        letters = ''.join(s for _, segs, _ in runs for kind, s in segs if kind == 'L')
        used = sorted(set(letters))
        if design == 'mono':
            if len(used) != N_ALPHA_SIGNS: continue
            homs = {l: 1 for l in used}
        else:
            homs = {l: (3 if l in VOWELS else 1) for l in used}
        signs = [f'x{n}' for n in range(sum(homs.values()))]; rnd.shuffle(signs)
        key, pos = {}, 0                               # letter -> list of signs
        for l in used:
            key[l] = signs[pos:pos + homs[l]]; pos += homs[l]
        out_runs, truth = [], []
        for (before, segs, after), ws in zip(runs, WORDSIGNS):
            toks, wi = [], 0
            for kind, s in segs:
                if kind == 'W':
                    toks.append(ws[wi]); wi += 1
                else:
                    for ch in s:
                        g = rnd.choice(key[ch]); toks.append(g); truth.append((g, ch))
            out_runs.append((before, toks, after))
        distinct = len({g for g, _ in truth})
        if distinct == N_ALPHA_SIGNS:
            return out_runs, truth, letters
    raise RuntimeError('could not match sign count')


LM = WORDS = None
def init(lmpath, words):
    global LM, WORDS
    LM = solve.load_lm(lmpath); WORDS = words


def accuracy(key, truth):
    return sum(key.get(g) == ch for g, ch in truth) / len(truth)


def run_trial(args):
    design, t = args
    rnd = random.Random(1000 * (design == 'homo') + t)
    runs, truth, letters = make_trial(WORDS, rnd, design)
    solve.RUNS = runs                                  # solve.decrypt/total_score/anneal read this global
    true_key = dict(truth)
    true_score = solve.total_score(true_key, LM)
    free = max((solve.anneal(LM, {}, iters=ITERS, seed=s) for s in range(SEEDS_FREE)), key=lambda x: x[0])
    run2 = [g for g in runs[1][1] if g not in solve.NOMEN][:5]
    crib_true = {g: true_key[g] for g in run2}
    # a wrong crib: a 5-letter corpus word consistent with the sign pattern of those five signs
    fw = None
    while fw is None:
        w = rnd.choice(WORDS)
        if len(w) == 5 and w.isalpha() and w != letters[9:14]:
            m = {}
            if all(m.setdefault(g, c) == c for g, c in zip(run2, w)):
                fw = w
    crib_false = {}
    for g, c in zip(run2, fw): crib_false[g] = c
    ct = max((solve.anneal(LM, crib_true, iters=ITERS, seed=s) for s in range(SEEDS_CRIB)), key=lambda x: x[0])
    cf = max((solve.anneal(LM, crib_false, iters=ITERS, seed=s) for s in range(SEEDS_CRIB)), key=lambda x: x[0])
    solve.RUNS = runs
    return dict(design=design, trial=t, plain=letters, true=round(true_score, 1),
                free=round(free[0], 1), free_acc=round(accuracy(free[1], truth), 3),
                crib_true=round(ct[0], 1), crib_true_acc=round(accuracy(ct[1], truth), 3),
                crib_false=round(cf[0], 1), false_word=fw,
                free_text=' | '.join(''.join(' ' if g in solve.NOMEN else free[1].get(g, '?') for g in r[1]) for r in runs))


def summary(rows, design):
    R = [r for r in rows if r['design'] == design]
    n = len(R)
    if not n: return []
    f = lambda c: sum(1 for r in R if c(r))
    acc = sorted(r['free_acc'] for r in R)
    L = [f'design {design}: {n} trials, 20 seeds x {ITERS} iterations each (unconstrained)',
         f'  recovered (>= 80% of letters right): {f(lambda r: r["free_acc"] >= 0.8)}/{n}',
         f'  >= 50% right: {f(lambda r: r["free_acc"] >= 0.5)}/{n};  median accuracy {acc[n // 2]:.2f}, mean {sum(acc) / n:.2f}, max {acc[-1]:.2f}',
         f'  solver optimum scores above the true key (model cannot tell): {f(lambda r: r["free"] > r["true"])}/{n}',
         f'  true 5-letter crib: penalty (free - crib) median {sorted(r["free"] - r["crib_true"] for r in R)[n // 2]:.1f}, '
         f'>= 35: {f(lambda r: r["free"] - r["crib_true"] >= 35)}/{n}; accuracy with true crib >= 80%: {f(lambda r: r["crib_true_acc"] >= 0.8)}/{n}',
         f'  wrong 5-letter crib: penalty median {sorted(r["free"] - r["crib_false"] for r in R)[n // 2]:.1f}; '
         f'true crib scores above wrong crib: {f(lambda r: r["crib_true"] > r["crib_false"])}/{n}']
    return L


if __name__ == '__main__':
    trials = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    workers = int(sys.argv[2]) if len(sys.argv) > 2 else 12
    lmpath, words = corpus_split()
    jobs = [(d, t) for t in range(trials) for d in ('mono', 'homo')]
    t0 = time.time(); rows = []
    with Pool(workers, initializer=init, initargs=(lmpath, words)) as pool:
        for r in pool.imap_unordered(run_trial, jobs):
            rows.append(r)
            print(r['design'], r['trial'], r['free_acc'], r['free'], r['true'], flush=True)
    rows.sort(key=lambda r: (r['design'], r['trial']))
    with open(os.path.join(HERE, 'control_out.txt'), 'w', encoding='utf8') as fh:
        fh.write('Matched control for solve.py on the 42-sign layout of f. 59r (control.py)\n')
        fh.write('Target layout: runs of 11/14/17 signs, 39 letter tokens + 3 word signs, 18 + 3 = 21 distinct.\n')
        fh.write('Target results for comparison (NOTES): unconstrained best ~ -401; cribs penalised 35-90.\n\n')
        for d in ('mono', 'homo'):
            fh.write('\n'.join(summary(rows, d)) + '\n\n')
        fh.write(f'elapsed {time.time() - t0:.0f} s\n\nper trial:\n')
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + '\n')
    print(open(os.path.join(HERE, 'control_out.txt'), encoding='utf8').read()[:3000])
