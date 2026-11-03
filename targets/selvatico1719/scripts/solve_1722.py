"""Ciphertext-only attack on the 1722 Selvatico -> Riva letters (homophonic substitution test).

Corpus: Italian plaintexts from this repository (git ref HEAD, or CYPHERSOLVER_REF; read with git show), letters a-z only,
u/v and i/j merged. Symbols: the number of each group (marks ignored); groups over 99 are
treated as code words and dropped from the letter stream (kept as '#').
Simulated annealing over symbol->letter maps, quadgram score. Prints the best decryption.
usage: python solve_1722.py <pass file> [restarts] [iters]
"""
import math, random, re, subprocess, sys, collections
sys.stdout.reconfigure(encoding='utf-8')
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from decrypt import lines, norm

# repository root: targets/<name>/scripts/ -> three levels up; override with CYPHERSOLVER_REPO.
REPO = os.environ.get('CYPHERSOLVER_REPO', os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..')))
REF = os.environ.get('CYPHERSOLVER_REF', 'HEAD')


def corpus():
    names = subprocess.run(['git', '-C', REPO, 'ls-tree', '-r', '--name-only', REF, 'targets/'],
                           capture_output=True, text=True, encoding='utf-8').stdout.split()
    pick = [n for n in names if re.search(r'(alessandrino1568|morosini1588|capilupi1545|nuncio1566).*(decryption|plaintext).*\.txt$', n)]
    txt = []
    for n in pick:
        txt.append(subprocess.run(['git', '-C', REPO, 'show', REF + ':' + n], capture_output=True,
                                  text=True, encoding='utf-8', errors='ignore').stdout)
    t = ' '.join(txt).lower()
    t = t.replace('v', 'u').replace('j', 'i')
    t = re.sub(r'[^a-z]', '', t)
    return t


def quad(t):
    c = collections.Counter(t[i:i + 4] for i in range(len(t) - 3))
    tot = sum(c.values())
    floor = math.log10(0.01 / tot)
    return {k: math.log10(v / tot) for k, v in c.items()}, floor


def main():
    fn = sys.argv[1]
    R = int(sys.argv[2]) if len(sys.argv) > 2 else 8
    N = int(sys.argv[3]) if len(sys.argv) > 3 else 60000
    t = corpus()
    print('corpus letters', len(t))
    Q, floor = quad(t)
    freq = collections.Counter(t)
    alpha = sorted(freq)
    weights = [freq[a] for a in alpha]
    seq = []
    for lid, body in lines(fn):
        body = re.sub(r'\{[^}]*\}', ' ', body)
        for tok in body.split():
            n, u = norm(tok)
            if n.isdigit():
                seq.append(n if int(n) < 100 else '#')
    syms = sorted({s for s in seq if s != '#'}, key=lambda x: int(x))
    print('stream', len(seq), 'symbols', len(syms))
    # segments between code words
    segs, cur = [], []
    for s in seq:
        if s == '#':
            if cur:
                segs.append(cur)
            cur = []
        else:
            cur.append(s)
    if cur:
        segs.append(cur)

    def score(m):
        sc = 0.0
        for sg in segs:
            p = ''.join(m[s] for s in sg)
            for i in range(len(p) - 3):
                sc += Q.get(p[i:i + 4], floor)
        return sc

    best_all = (-1e18, None)
    for r in range(R):
        m = {s: random.choices(alpha, weights)[0] for s in syms}
        cur_s = score(m)
        best = (cur_s, dict(m))
        T0 = 1.5
        for it in range(N):
            T = T0 * (1 - it / N) + 0.05
            s = random.choice(syms)
            old = m[s]
            m[s] = random.choice(alpha)
            ns = score(m)
            if ns >= cur_s or random.random() < math.exp((ns - cur_s) / T):
                cur_s = ns
                if ns > best[0]:
                    best = (ns, dict(m))
            else:
                m[s] = old
        print('restart', r, round(best[0], 1), flush=True)
        if best[0] > best_all[0]:
            best_all = best
    m = best_all[1]
    print('best', round(best_all[0], 1))
    print(' '.join(f'{s}={m[s]}' for s in syms))
    for lid, body in lines(fn):
        body = re.sub(r'\{[^}]*\}', ' ', body)
        out = []
        for tok in body.split():
            n, u = norm(tok)
            if n.isdigit():
                out.append(m.get(n, f'[{n}]') if int(n) < 100 else f'[{n}]')
        print(lid, ''.join(out))


if __name__ == '__main__':
    main()
