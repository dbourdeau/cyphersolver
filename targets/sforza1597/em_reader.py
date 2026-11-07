"""Language-guided re-assignment of glyphs to clusters (ICM over an Italian letter LM).
usage: python em_reader.py <tokens.pkl> <solver_out.txt> <out_prefix> [beta] [K] [sweeps]"""
import sys, re, pickle, collections, numpy as np
sys.path.insert(0, 'C:/Users/dbour/cypher')
from lang import lm
pkl, keyf, outp = sys.argv[1:4]
beta = float(sys.argv[4]) if len(sys.argv) > 4 else 2.0
K = int(sys.argv[5]) if len(sys.argv) > 5 else 4
sweeps = int(sys.argv[6]) if len(sys.argv) > 6 else 4
recs, lab = pickle.load(open(pkl, 'rb')); lab = np.array(lab)
F = np.array([r['feat'] for r in recs])
cnt = collections.Counter(lab); rank = {c: i for i, (c, _) in enumerate(cnt.most_common())}
tok = np.array([rank[l] for l in lab])            # cluster id as in the token files (s00 = most frequent)
key = {}
for line in open(keyf, encoding='utf-8'):
    m = re.match(r'^([s\d|]+) - ([A-Za-z])$', line.strip())
    if m:
        for c in m.group(1).split('|'): key[int(c[1:])] = m.group(2).lower()
M = lm.load('it-cinquecento', order=5, spaces=False)
A = M.alpha
def enc(ch): return M.index['u' if ch == 'v' else ch] if ('u' if ch == 'v' else ch) in M.index else None
cent = np.array([F[tok == c].mean(0) for c in range(len(rank))])
d_all = np.sqrt(((F[:, None, :] - cent[None]) ** 2).sum(2))        # glyph x cluster
s2 = np.median(d_all[np.arange(len(F)), tok]) ** 2
lines = collections.OrderedDict()
for i, r in enumerate(recs): lines.setdefault((r['page'], r['line']), []).append(i)
cur = tok.copy()
def letter_of(c): return key.get(int(c))
def dictionary_hits(text):
    import re as _re
    return len(_re.findall(r'(?:della|dello|delle|nostro|nostra|signore|signoria|vostra|vostro|questo|questa|lettera|havere|havea|quello|quella|essere|stato|stata|molto|molti|parte|parti|tutto|tutti|altro|altra|ancora|perche|dicto|dicta|ducha|duca|conte|campo|gente|cavalli|cavalli|terra|tempo|modo|cosa|cose|dire|fare|dare|venire|andare|stare|mandare|scrivere|havemo|havete|sono|sera|dove|come|quando|ogni|dopo|prima|sopra|contra|verso|senza)', text))
def text_of(assign):
    out = []
    for k, idx in lines.items():
        out.append(''.join(letter_of(assign[i]) or '?' for i in idx))
    return out
def lm_score(assign):
    tot = 0; n = 0
    for k, idx in lines.items():
        s = ''.join(letter_of(assign[i]) or 'a' for i in idx)
        x = np.array([enc(ch) if enc(ch) is not None else 0 for ch in s])
        tot += M.score_idx(x); n += max(1, len(x) - 4)
    return tot / n
print('start: LM per char %.3f' % lm_score(cur), 'dict hits', dictionary_hits(' '.join(text_of(cur))))
for sw in range(sweeps):
    changed = 0
    for k, idx in lines.items():
        L = [enc(letter_of(cur[i])) or 0 for i in idx]
        for p, gi in enumerate(idx):
            cands = np.argsort(d_all[gi])[:K]
            dmin2 = d_all[gi, cands[0]] ** 2
            best = None
            for c in cands:
                ch = letter_of(c)
                if ch is None: continue
                e = enc(ch)
                lo, hi = max(0, p - 4), min(len(L), p + 5)
                w = L[lo:hi].copy(); w[p - lo] = e
                score = M.score_idx(np.array(w)) - beta * (d_all[gi, c] ** 2 - dmin2) / s2
                if best is None or score > best[0]: best = (score, c, e)
            if best and best[1] != cur[gi]:
                # keep within the same letter if the cluster already gives that letter
                if letter_of(best[1]) != letter_of(cur[gi]) or True:
                    cur[gi] = best[1]; L[p] = best[2]; changed += 1
    print('sweep', sw + 1, 'changed', changed, 'LM %.3f' % lm_score(cur), 'dict hits', dictionary_hits(' '.join(text_of(cur))))
# write refined token file (cluster ids) and text
out = ['\n'.join(' '.join(f's{cur[i]:02d}' for i in idx) for k, idx in lines.items())]
open(outp + '_tokens.txt', 'w').write(out[0] + '\n')
open(outp + '_text.txt', 'w').write('\n'.join(text_of(cur)) + '\n')
orig = sum(1 for i in range(len(cur)) if cur[i] != tok[i])
print('glyphs reassigned', orig, 'of', len(cur), '(%.1f%%)' % (100 * orig / len(cur)))
