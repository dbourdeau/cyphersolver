"""LM-guided label correction for the sister letters (13, 18, 22 Oct 1552).

    python scripts/beam.py            -> work/beam_<letter>.tsv  (page, line, machine labels, chosen labels, decryption)

For each cipher line (median nearest-neighbour distance < 4.5, little cursive ink), each sign keeps the
classifier's top four labels with their probabilities. A beam search over the whole letter picks one label
per sign to maximise  W * sum log(p_label + 0.02)  +  Latin 5-gram score of the decrypted letters
(la-letters, no spaces). Nulls emit nothing, codes emit nothing to the model, numerals emit double letters.
The key (key.tsv) is fixed; only the reading of the shapes is chosen.
"""
import pickle, sys, math, numpy as np, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT.parent.parent))
from lang import lm
M = lm.load('la-letters', spaces=False)
A = M.A; IDX = M.index; LP = M.lp; K = M.order
W = float(sys.argv[1]) if len(sys.argv) > 1 else 2.0
BEAM = 400

key = {}
for l in open(ROOT / 'key.tsv', encoding='utf8'):
    if l.startswith('#') or not l.strip(): continue
    p = l.rstrip('\n').split('\t'); key[p[0]] = p[1]

LETTERS = {'13oct': ['9r', '9v', '10r', '10v', '11r', '11v', '12r', '12v', '13r', '13v', '14r', '14v', '15r'],
           '18oct': ['37r', '37v', '38r', '38v', '39r', '39v', '40r', '40v', '41r', '41v', '42r'],
           '22oct': ['43r', '43v', '44r', '44v', '45r', '45v', '46r', '46v', '47r', '47v', '48r']}


SEL = pickle.load(open(ROOT / 'work/sel.pkl', 'rb'))  # cipher signs per line, from cipher_lines.tsv (marked by eye)


def cipher_lines(out, pages):
    for p, j, y, c, d, labs in out:
        if p in pages and (p, j) in SEL:
            yield p, j, [(i, labs[i]) for i in SEL[(p, j)]]


def emit(lab):
    if lab == '-': return ''
    v = key.get(lab, '?')
    if v == 'null': return ''
    if v.startswith('[') or v == '?': return None
    return v


def run(letter, out, probs):
    pages = LETTERS[letter]
    seq = []
    for p, j, labs in sorted(cipher_lines(out, pages), key=lambda x: (pages.index(x[0]), x[1])):
        for i, lab in labs:
            seq.append((p, j, i, lab, probs[(p, j)][i]))
    # state: context tuple (last K-1 letter indices) -> (score, chain)
    beam = {(): (0.0, None)}
    for (p, j, i, lab, cands) in seq:
        nb = {}
        for ctx, (sc, ch) in beam.items():
            for cl, pr in cands:
                if pr < 0.03 and cl != lab: continue
                e = emit(cl)
                s = sc + W * math.log(pr + 0.02)
                c2 = ctx
                if e:
                    for chr_ in e:
                        if chr_ not in IDX: continue
                        x = IDX[chr_]
                        if len(c2) == K - 1:
                            code = 0
                            for t in c2: code = code * A + t
                            s += LP[code * A + x]
                        else:
                            s += math.log(1 / 26)
                        c2 = (c2 + (x,))[-(K - 1):]
                old = nb.get(c2)
                if old is None or s > old[0]:
                    nb[c2] = (s, (ch, cl))
        beam = dict(sorted(nb.items(), key=lambda kv: -kv[1][0])[:BEAM])
    best = max(beam.values(), key=lambda v: v[0])[1]
    chosen = []
    while best: best, cl = best; chosen.append(cl)
    chosen = chosen[::-1]
    rows = {}
    for (p, j, i, lab, cands), cl in zip(seq, chosen):
        rows.setdefault((p, j), []).append((lab, cl, i))
    with open(ROOT / f'work/beam_{letter}.tsv', 'w', encoding='utf8') as f:
        for (p, j), r in rows.items():
            dec = ''.join(('[' + cl + ']') if emit(cl) is None else emit(cl) for lab, cl, i in r)
            ch = sum(lab != cl for lab, cl, i in r)
            f.write(chr(9).join([p, str(j), " ".join(x[0] for x in r), " ".join(x[1] for x in r), str(ch), dec, " ".join(str(x[2]) for x in r)]) + chr(10))
    print(letter, len(seq), 'signs', sum(a[3] != c for a, c in zip(seq, chosen)), 'changed')


if __name__ == '__main__':
    out, probs = pickle.load(open(ROOT / 'work/machine.pkl', 'rb'))
    for L in (sys.argv[2:] or LETTERS):   # beam.py W letter...; eye edits refer to a letter's beam: never rerun a letter once its eye pass has begun
        run(L, out, probs)
