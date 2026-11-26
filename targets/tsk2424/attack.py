"""Monoalphabetic-substitution attack with a shared language model, plus shuffle and known-plaintext controls.
Usage: python attack.py <transcription> <model> [--drop '?'] [--noword] [--restarts 6] [--steps 3000] [--nctl 20]
Every sign class (token) is mapped to one letter of the model alphabet (several tokens may share a letter, so merged
look-alike signs are allowed); dividers become spaces unless --noword. Score = mean log-prob per character.
Reports real text in both reading directions, token-shuffled copies (null), and a control: real model-language text
enciphered with a random many-to-one class mapping of the same alphabet size and layout (does the method separate
a true monoalphabetic text from its shuffle at this length and merge rate?)."""
import sys, os, random, math
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm

args = sys.argv[1:]
path, model = args[0], args[1]
drop = set(args[args.index('--drop') + 1].split(',')) if '--drop' in args else set()
noword = '--noword' in args
R = int(args[args.index('--restarts') + 1]) if '--restarts' in args else 6
STEPS = int(args[args.index('--steps') + 1]) if '--steps' in args else 3000
NCTL = int(args[args.index('--nctl') + 1]) if '--nctl' in args else 20
DIV = {'-', '.', '|'}
lines = [l.split(':', 1)[1].split() for l in open(path, encoding='utf-8') if l.startswith('L') and ':' in l]
m = lm.load(model, order=4, spaces=not noword)
A = m.A
space = 0 if not noword else None
sch = lm.registry()[0][model]['norm']


def stream(lns):
    """token id stream; -1 = word break"""
    out = []
    for ln in lns:
        for t in ln:
            if t in DIV:
                if not noword and out and out[-1] != -1:
                    out.append(-1)
            elif t not in drop:
                out.append(t)
        if not noword and out and out[-1] != -1:
            out.append(-1)
    return out


def solve(tokens, rng):
    voc = sorted({t for t in tokens if t != -1}, key=str)
    idx = {t: i for i, t in enumerate(voc)}
    T = np.array([idx[t] if t != -1 else -1 for t in tokens])
    V = len(voc)
    lo = 0 if noword else 1  # letters start at 1 when space is index 0
    best = (-1e18, None)
    for r in range(R):
        mp = np.array([rng.randrange(lo, A) for _ in range(V)])

        def sc(mp):
            x = np.where(T >= 0, mp[np.clip(T, 0, None)], 0)
            if noword:
                x = x[T >= 0]
            return m.score_idx(x) / max(1, len(x) - m.order + 1)

        cur = sc(mp)
        for s in range(STEPS):
            temp = 0.15 * (1 - s / STEPS) + 0.002
            j = rng.randrange(V)
            old = mp[j]
            mp[j] = rng.randrange(lo, A)
            new = sc(mp)
            if new >= cur or rng.random() < math.exp((new - cur) / temp):
                cur = new
            else:
                mp[j] = old
        if cur > best[0]:
            best = (cur, mp.copy(), voc)
    return best


def decode(best, tokens):
    cur, mp, voc = best
    idx = {t: i for i, t in enumerate(voc)}
    al = m.alpha
    return ''.join(' ' if t == -1 else al[mp[idx[t]]] for t in tokens)


rng = random.Random(11)
tok = stream(lines)
n = sum(1 for t in tok if t != -1)
real = solve(tok, rng)
rev = solve(stream([ln[::-1] for ln in lines]), rng)
print(f'{os.path.basename(path)} model {model}: {n} signs, {len(set(tok) - {-1})} classes, alphabet {A - (0 if noword else 1)}')
print('real  forward  %.3f   %s' % (real[0], decode(real, tok)[:90]))
print('real  reversed %.3f' % rev[0])
flat = [t for t in tok if t != -1]
nulls = []
for _ in range(NCTL):
    sh = flat[:]
    rng.shuffle(sh)
    it = iter(sh)
    t2 = [(-1 if t == -1 else next(it)) for t in tok]
    nulls.append(solve(t2, rng)[0])
nulls = np.array(nulls)
print('shuffled nulls: mean %.3f sd %.3f max %.3f  -> real forward z %.2f, reversed z %.2f' % (
    nulls.mean(), nulls.std(), nulls.max(), (real[0] - nulls.mean()) / nulls.std(), (rev[0] - nulls.mean()) / nulls.std()))

# control: model-language text, merged classes
from lang import corpora
src = lm.norm(corpora.text(lm.registry()[0][model]['sources'])[-400000:], sch, not noword)
if True:
    V = len(set(flat))
    ctl = []
    for k in range(NCTL):
        start = rng.randrange(0, len(src) - 2000)
        seg = src[start:start + 2000]
        # take a stretch with about n letters and the same break rate
        cut = []
        cnt = 0
        for ch in seg:
            cut.append(ch)
            if ch != ' ':
                cnt += 1
            if cnt >= n:
                break
        pt = ''.join(cut).strip()
        letters = sorted({c for c in pt if c != ' '})
        merge = {c: i % V for i, c in enumerate(rng.sample(letters, len(letters)))}   # many-to-one to V classes
        tk = [(-1 if c == ' ' else 'k%d' % merge[c]) for c in pt]
        ctl.append(solve(tk, rng)[0])
    ctl = np.array(ctl)
    print('control (model-language text, %d classes, merged): mean %.3f sd %.3f min %.3f; separation from nulls z %.2f' % (
        V, ctl.mean(), ctl.std(), ctl.min(), (ctl.mean() - nulls.mean()) / nulls.std()))
