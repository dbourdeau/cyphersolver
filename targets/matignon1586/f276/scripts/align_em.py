"""Hard-EM key recovery from a chart-id transcription of cipher lines and the contemporary decipherment (gloss).

cipher file : lines "L01: C13 C04 X:big L ..."   (chart ids C.., W.., X:<desc>, ?, alternatives A|B)
plain file  : lines "01 Monsieur Forget s'est alle ..." (number, then text); '#' comments, [?] / [...] / {struck} handled
chart tsv   : prior values for chart ids (C01 a, W01 faire, ...), used to initialise the key

Model: the cipher token stream and the plaintext letter stream are aligned by a Viterbi DP. A token emits one
letter (cost -log p(letter|token)), nothing (null, cost -log p(null|token)), or, for word tokens, a whole word
string. Plaintext letters may also be skipped (INS cost), since the clerk's text and the cipher differ in places.
After each alignment the emission table is re-estimated from the counts (add-alpha smoothing). Repeat.

    python scripts/align_em.py --cipher crib/f277r_all.txt --plain crib/plain_all.txt --iters 10 --out crib/key_em_all.tsv
"""
import argparse, math, re, unicodedata, collections, os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
A = 'abcdefghilmnopqrstuxyz'          # 16th-c. French letter set (k, w absent; v->u, j->i)
NUL = '-'
INS = 4.0            # plaintext letter with no cipher sign
WCOST = 0.3          # word-sign emitting its word
FREE_ENDS = True     # plaintext before the first / after the last cipher sign is free (partial transcriptions)
NULL_MIN = 2.5       # floor on the cost of reading a non-null sign as null

def norm_text(t):
    t = unicodedata.normalize('NFD', t); t = ''.join(c for c in t if unicodedata.category(c) != 'Mn')
    t = t.lower().replace('v', 'u').replace('j', 'i').replace('w', 'uu').replace('k', 'c')
    t = re.sub(r'\[\?\]|\[\.\.\.\]', ' ', t); t = re.sub(r'\{[^}]*\}', ' ', t)      # drop uncertainty marks, struck words
    t = re.sub(r'\(([^)]*)\)', r'\1', t)                                           # keep expansions
    return re.sub(r'[^a-z ]+', ' ', t)

def load_plain(path):
    words = []
    for l in open(path, encoding='utf-8'):
        l = l.strip()
        if not l or l.startswith('#'): continue
        l = re.sub(r'^\d+\s*', '', l)
        words += norm_text(l).split()
    P = ''.join(words)
    starts = set(); pos = 0
    for w in words: starts.add(pos); pos += len(w)
    return P, starts

def load_cipher(path):
    lines = []
    for l in open(path, encoding='utf-8'):
        l = l.strip()
        if not l or l.startswith('#'): continue
        m = re.match(r'^(L\d+)\s*:\s*(.*)$', l)
        if not m: continue
        toks = re.findall(r'X:[^|]+?(?=\s+(?:[CW]\d|X:|\?|$))|[CW]\d+(?:r\d+)?(?:\|[CW]\d+(?:r\d+)?)*|\?', m.group(2).strip() + ' ')
        lines.append((m.group(1), [t.strip() for t in toks]))
    return lines

def load_chart(path):
    d = {}
    for l in open(path, encoding='utf-8'):
        if l.startswith('#') or not l.strip(): continue
        k, v = l.rstrip('\n').split('\t'); d[k] = v
    return d

def token_type(t):
    return t.split('|')[0] if '|' in t else t

def chart_id(t):
    """chart column of a token: C13r2 -> C13, C05r1|C16r2 -> C05, X:... -> X:..."""
    base = t.split('|')[0]
    return re.sub(r'r\d+$', '', base) if base[:1] in 'CW' else base

class Key:
    def __init__(self, types, chart, words_by_type):
        self.types = types; self.idx = {t: i for i, t in enumerate(types)}
        n = len(types); self.L = len(A) + 1                      # letters + null
        self.counts = np.full((n, self.L), 0.0)
        self.words = words_by_type                               # type -> word string (for W tokens)
        self.prior = np.full((n, self.L), 0.3)
        for t, i in self.idx.items():
            base = chart_id(t)
            v = chart.get(base)
            if v is None: continue
            if v == '<null>': self.prior[i, self.L-1] += 6.0
            elif base.startswith('W'): continue
            else:
                for alt in v.split('|'):
                    if alt in A: self.prior[i, A.index(alt)] += 6.0
        self.update()
    def update(self, alpha=0.3):
        tot = self.counts + self.prior * alpha * 3 + alpha
        p = tot / tot.sum(1, keepdims=True)
        self.cost = -np.log(p)
        # a sign that the chart does not call a null may not become a cheap null: this stops the all-null collapse
        notnull = self.prior[:, self.L-1] < 1.0
        self.cost[notnull, self.L-1] = np.maximum(self.cost[notnull, self.L-1], NULL_MIN)

def viterbi(tokens, P, key):
    n, m = len(tokens), len(P)
    Pidx = np.array([A.index(c) for c in P])
    INF = 1e9
    rows = np.full((n+1, m+1), INF); rows[0, 0] = 0.0
    if FREE_ENDS: rows[0, :] = 0.0                                # plaintext before the first sign costs nothing
    back = np.zeros((n+1, m+1), dtype=np.int8)                   # 1 emit, 2 null, 3 ins (from left), 4 word
    wlen = np.zeros((n+1, m+1), dtype=np.int16)
    for i, t in enumerate(tokens):
        ti = key.idx[token_type(t)]
        prev = rows[i]
        cur = np.full(m+1, INF); bk = np.zeros(m+1, dtype=np.int8); wl = np.zeros(m+1, dtype=np.int16)
        # null emission
        c_null = prev + key.cost[ti, key.L-1]
        cur[:] = c_null; bk[:] = 2
        # letter emission
        c_emit = prev[:-1] + key.cost[ti, Pidx]
        better = c_emit < cur[1:]; cur[1:][better] = c_emit[better]; bk[1:][better] = 1
        # word emission
        w = key.words.get(token_type(t))
        if w:
            k = len(w)
            if k <= m:
                hits = np.array([P.startswith(w, j) for j in range(m-k+1)])
                js = np.nonzero(hits)[0]
                if len(js):
                    c_w = prev[js] + WCOST
                    sel = (js + k)[c_w < cur[js+k]]
                    cur[sel] = c_w[c_w < cur[js+k]]; bk[sel] = 4; wl[sel] = k
        # insertion of plaintext letters (running min along j)
        j = np.arange(m+1)
        run = np.minimum.accumulate(cur - j*INS) + j*INS
        better = run < cur - 1e-9; bk[better] = 3; cur = run
        rows[i+1] = cur; back[i+1] = bk; wlen[i+1] = wl
    # backtrack (with FREE_ENDS the plaintext after the last sign costs nothing: end at the cheapest column)
    j = int(np.argmin(rows[n])) if FREE_ENDS else m
    total = rows[n, j]; i = n; path = []
    while i > 0 or (j > 0 and not FREE_ENDS):
        b = back[i, j]
        if i == 0 or b == 3:
            path.append(('ins', None, P[j-1])); j -= 1
        elif b == 1: path.append(('emit', tokens[i-1], P[j-1])); i -= 1; j -= 1
        elif b == 2: path.append(('null', tokens[i-1], '')); i -= 1
        elif b == 4: k = wlen[i, j]; path.append(('word', tokens[i-1], P[j-k:j])); i -= 1; j -= k
        else: path.append(('ins', None, P[j-1])); j -= 1
    return total, path[::-1]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--cipher', required=True); ap.add_argument('--plain', required=True)
    ap.add_argument('--chart', default=os.path.join(HERE, '..', 'crib', 'chart_values.tsv'))
    ap.add_argument('--iters', type=int, default=12); ap.add_argument('--out', default=None)
    ap.add_argument('--noprior', action='store_true'); ap.add_argument('--fixed-ends', action='store_true')
    a = ap.parse_args()
    global FREE_ENDS
    if a.fixed_ends: FREE_ENDS = False
    chart = {} if a.noprior else load_chart(a.chart)
    allchart = load_chart(a.chart)
    lines = load_cipher(a.cipher); tokens = [t for _, ts in lines for t in ts]
    P, starts = load_plain(a.plain)
    types = sorted({token_type(t) for t in tokens})
    words = {t: norm_text(allchart[chart_id(t)]).replace(' ', '') for t in types if t.startswith('W') and chart_id(t) in allchart}
    key = Key(types, chart, words)
    print(f'{len(tokens)} tokens of {len(types)} types; plaintext {len(P)} letters', file=sys.stderr)
    for it in range(a.iters):
        cost, path = viterbi(tokens, P, key)
        key.counts[:] = 0; wordhits = collections.Counter()
        for op, t, l in path:
            if op == 'emit': key.counts[key.idx[token_type(t)], A.index(l)] += 1
            elif op == 'null': key.counts[key.idx[token_type(t)], key.L-1] += 1
            elif op == 'word': wordhits[token_type(t)] += 1
        key.update()
        n_emit = sum(1 for op, _, _ in path if op == 'emit'); n_ins = sum(1 for op, _, _ in path if op == 'ins')
        n_null = sum(1 for op, _, _ in path if op == 'null'); n_w = sum(1 for op, _, _ in path if op == 'word')
        print(f'iter {it}: cost {cost:.0f}  emit {n_emit} word {n_w} null {n_null} ins {n_ins}', file=sys.stderr)
    # report
    freq = collections.Counter(token_type(t) for t in tokens)
    out = []
    for t in sorted(types, key=lambda t: -freq[t]):
        i = key.idx[t]; c = key.counts[i]; tot = c.sum()
        top = sorted(((c[k], (A + NUL)[k]) for k in range(key.L) if c[k] > 0), reverse=True)[:4]
        if wordhits.get(t): top = [(wordhits[t], '=' + key.words[t])] + top
        chart_v = allchart.get(chart_id(t), '')
        out.append(f"{t}\t{freq[t]}\t{chart_v}\t" + ' '.join(f'{l}:{int(n)}' for n, l in top))
    hdr = 'token\tn\tchart\temissions (letter:count)'
    print(hdr); print('\n'.join(out))
    if a.out:
        with open(a.out, 'w') as f: f.write(hdr + '\n' + '\n'.join(out) + '\n')
    # alignment print per cipher line
    print('\nALIGNMENT')
    pos = 0
    for name, ts in lines:
        seg = []; k = 0
        while k < len(ts):
            op, t, l = path[pos]; pos += 1
            if op == 'ins': seg.append(f'+{l}'); continue
            seg.append(f'{t}>{l or "-"}'); k += 1
        print(name, ' '.join(seg))
    while pos < len(path): print('+' + path[pos][2], end=' '); pos += 1
    print()

if __name__ == '__main__':
    main()
