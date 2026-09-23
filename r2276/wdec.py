"""Word-level Viterbi decoder: segments the sign stream into lexicon words.
Each sign emits one of its key values (free), another letter (SUB cost, max one per word, words >= 4 letters),
or nothing if it is a declared null. Word cost = -log unigram prob. Unknown spans cost UNK per sign."""
import sys, json, math
from decode import load
LEX = json.load(open('lex.json'))
tot = sum(LEX.values())
WC = {w: -math.log(c / tot) for w, c in LEX.items()}
SUB, UNK, MAXW = 7.0, 11.0, 16
BG = json.load(open('bigr.json'))
UNI = {w: c for w, c in LEX.items()}
LAM = 0.4
def wcost(prev, w):
    pu = UNI[w] / tot
    if prev is None: return -math.log(pu)
    pb = BG.get(prev + ' ' + w, 0) / UNI.get(prev, 1) if prev in UNI else 0
    return -math.log(LAM * pb + (1 - LAM) * pu)
TOPK = 12
LET = 'abcdefghilmnopqrstuxyz'
trie = {}
for w in WC:
    n = trie
    for ch in w: n = n.setdefault(ch, {})
    n['$'] = w
def vals(KEY, t):
    v = KEY.get(t, '*')
    return list(LET) if v == '*' else [x.replace('j','i').replace('v','u') for x in v.split(',')]
def walk(node, s):
    for ch in s:
        node = node.get(ch)
        if node is None: return None
    return node
def decode_stream(toks, KEY):
    n = len(toks); V = [vals(KEY, t) for t in toks]
    best = [dict() for _ in range(n+1)]; best[0][None] = (0.0, None)
    for i in range(n):
        if not best[i]: continue
        items = sorted(best[i].items(), key=lambda kv: kv[1][0])[:TOPK]
        cands = []
        c0 = min(v[0] for _, v in items)
        cands.append((i+1, '?' + V[i][0] + '?', UNK, True))
        stack = [(trie, i, 0.0, 0)]
        while stack:
            node, j, cost, subs = stack.pop()
            if '$' in node and j > i: cands.append((j, node['$'], cost, False))
            if j >= n: continue
            for v in V[j]:
                if v == '':
                    stack.append((node, j+1, cost + 0.5, subs)); continue
                nd = walk(node, v)
                if nd is not None: stack.append((nd, j+1, cost, subs))
            if subs == 0:
                for ch in LET:
                    if ch in V[j] or ch not in node: continue
                    stack.append((node[ch], j+1, cost + SUB, 1))
        for j, w, cost, unk in cands:
            for prev, (pc, _) in items:
                c = pc + cost + (0 if unk else wcost(prev, w))
                key = None if unk else w
                if key not in best[j] or c < best[j][key][0]: best[j][key] = (c, (i, prev, w))
    # backtrack
    last = min(best[n].items(), key=lambda kv: kv[1][0]); out = []; j, key = n, last[0]
    while j > 0:
        c, (i, prev, w) = best[j][key]; out.append((i, j, w)); j, key = i, prev
    return out[::-1], last[1][0]
if __name__ == '__main__':
    KEY = json.load(open(sys.argv[1], encoding='utf8')); files = sys.argv[2].split(',')
    L = load(files)
    for fname in files:
        pre = fname.split('.')[0] + '.'
        stream = []; where = []
        for name, toks in L:
            if not name.startswith(pre): continue
            for t in toks:
                stream.append(t); where.append(name)
        segs = []; cur = []
        for k, t in enumerate(stream + ['...']):
            if t == '...':
                if cur: segs.append(cur)
                cur = []
            else: cur.append((t, where[k]))
        lines = {}
        for seg in segs:
            toks = [t for t, _ in seg]
            out, sc = decode_stream(toks, KEY)
            for i, j, w in out:
                lines.setdefault(seg[i][1], []).append(w)
        for name, _ in L:
            if name.startswith(pre): print(name.ljust(6), ' '.join(lines.get(name, [])))
