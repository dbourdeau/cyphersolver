"""Viterbi word segmentation of a decoded span whose letters may be ambiguous ('(c/d)' etc.), against a French word list
(19th-c. Gutenberg + a few 16th-c. spellings). Unknown words cost UNK per letter. u=v, i=j=y are merged.
    python segment.py 'que(i/e)(c/d)...'
"""
import sys, re, math, os
HERE = os.path.dirname(os.path.abspath(__file__))
EXTRA = ('pouldre leuera aultre aultant deffence hasart renuoier estoit faict seroit malaise plassees oultre basti maieste '
         'souloit leuer desseruiront seruiront contenir deuoir dehors craindre tailles denier ville forces habitans obeissance '
         'retournant conseruer emporter pourueu pouruoir retirer honneur passer iusques puis ains aussi auec leurs')
def norm(w): return w.lower().replace('v', 'u').replace('j', 'i').replace('y', 'i')
words = {}
for l in open(os.path.join(HERE, '..', 'data', 'fr_words.tsv')):
    if l.startswith('#'): continue
    w, c = l.rstrip('\n').split('\t'); words[w] = int(c)
tot = sum(words.values())
LEX = {}
for w, c in words.items():
    if c >= 3: LEX[norm(w)] = max(LEX.get(norm(w), -99), math.log(c / tot))
for w in EXTRA.split(): LEX[norm(w)] = max(LEX.get(norm(w), -99), math.log(30 / tot))
UNK = 7.0
def parse(s):
    out = []
    for m in re.finditer(r'\(([a-z/]+)\)|([a-z])', s):
        out.append(set(norm(x) for x in m.group(1).split('/')) if m.group(1) else {norm(m.group(2))})
    return out
def seg(s, top=3):
    L = parse(s); n = len(L)
    best = [(0.0, [])] + [(-1e9, None)] * n
    for i in range(n):
        if best[i][1] is None: continue
        sc, path = best[i]
        for j in range(i + 1, min(n, i + 16) + 1):
            cands = ['']
            for k in range(i, j):
                cands = [c + x for c in cands for x in L[k]]
                if len(cands) > 64: cands = cands[:64]
            hits = [(LEX[c], c) for c in cands if c in LEX]
            if hits: w_sc, w = max(hits)
            else: w_sc, w = -UNK * (j - i) - 3, '[' + ''.join(sorted(L[k])[0] for k in range(i, j)) + ']'
            if sc + w_sc > best[j][0]: best[j] = (sc + w_sc, path + [w])
    return best[n]
if __name__ == '__main__':
    for s in sys.argv[1:]:
        sc, ws = seg(s); print(round(sc, 1), ' '.join(ws))
