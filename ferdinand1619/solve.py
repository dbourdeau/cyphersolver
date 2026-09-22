"""Homophonic anneal for R9426: each two-digit number -> one letter; words split at the z/c signs.
Single numbers standing alone and 3-digit numbers are treated as code words (not letters)."""
import os, sys, re, random, math, collections
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from lang import lm
HERE = os.path.dirname(os.path.abspath(__file__))

def parse(path=os.path.join(HERE, 'transcription.txt')):
    """Return list of (lineid, items) where items are ('clear',text) | ('word',[tokens]) | ('code',tok)."""
    out = []
    carry = []
    for ln in open(path, encoding='utf8'):
        ln = ln.rstrip('\n')
        if not ln or ln.startswith('#'): continue
        lid, rest = ln.split(' ', 1)
        items = []
        for m in re.finditer(r'\[([^\]]*)\]|(\S+)', rest):
            if m.group(1) is not None:
                if carry: items.append(('word', carry)); carry = []
                items.append(('clear', m.group(1))); continue
            t = m.group(2)
            if t in ('z', 'c'):
                if carry: items.append(('word', carry)); carry = []
                items.append(('sep', t))
            elif t == '-':
                pass  # word continues on next line
            else:
                carry.append(t)
        out.append((lid, items))
        # a trailing '-' keeps carry for next line; otherwise flush
        if not rest.rstrip().endswith('-') and carry:
            items.append(('word', carry)); carry = []
    return out

def words(parsed):
    ws = []
    for lid, items in parsed:
        for it in items:
            if it[0] == 'word': ws.append(it[1])
    return ws

def is_code(w):
    return len(w) == 1 or any(len(t) != 2 for t in w)

if __name__ == '__main__':
    P = parse(); W = [w for w in words(P) if not is_code(w)]
    cnt = collections.Counter(t for w in W for t in w)
    print(len(W), 'words', sum(cnt.values()), 'letters', len(cnt), 'symbols')
    print(sorted(cnt.items(), key=lambda x: -x[1]))
    m = lm.load('de-1500s')
    alpha = [c for c in m.alpha if c != ' ']
    syms = sorted(cnt)
    sidx = {s: i for i, s in enumerate(syms)}
    SP = m.index[' ']
    # build flat index stream with -1 for space
    stream = []
    for w in W:
        stream.append(-1); stream += [sidx[t] for t in w]
    stream.append(-1)
    stream = __import__('numpy').array(stream)
    import numpy as np
    fixed = {}
    for a in sys.argv[1:]:
        s, l = a.split('='); fixed[s] = l
    def score(key):
        x = np.where(stream < 0, SP, key[np.maximum(stream, 0)])
        return m.score_idx(x)
    best = None
    freq = 'enirstadhulgcmobwfkzpv'
    for restart in range(int(os.environ.get('RESTARTS', 8))):
        key = np.array([m.index[random.choice(freq[:12])] for _ in syms])
        for s, l in fixed.items():
            if s in sidx: key[sidx[s]] = m.index[l]
        cur = score(key); T = 20.0
        for it in range(40000):
            i = random.randrange(len(syms))
            if syms[i] in fixed: continue
            old = key[i]; key[i] = m.index[random.choice(alpha)]
            new = score(key)
            if new >= cur or random.random() < math.exp((new - cur) / T): cur = new
            else: key[i] = old
            T = max(0.5, T * 0.9998)
        if best is None or cur > best[0]: best = (cur, key.copy())
        print(restart, round(cur, 1), flush=True)
    key = best[1]
    K = {s: m.alpha[key[sidx[s]]] for s in syms}
    print(' '.join(f'{s}={K[s]}' for s in syms))
    for lid, items in P:
        o = []
        for it in items:
            if it[0] == 'clear': o.append('[' + it[1] + ']')
            elif it[0] == 'word':
                w = it[1]
                o.append('<' + '.'.join(w) + '>' if is_code(w) else ''.join(K[t] for t in w).upper())
        print(lid, ' '.join(o))
