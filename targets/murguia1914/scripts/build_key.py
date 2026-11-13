"""Build the Clave Extra 3 key from the cipher/gloss pairs of LXVIII-1.14.1943.1.
usage: build_key.py TRAIN_SEGS(comma list or 'all') OUT_TSV
Alignment: gloss letters (accents dropped, spaces dropped, bracketed insertions dropped) are cut into
one chunk per group by dynamic programming. Pass 1 uses only segments where letters == groups
(one letter per group). Later passes align every segment with the current key: a known group costs 0
if its chunk equals its value, 1 otherwise; an unknown group may take 0-8 letters at cost 0.5.
The final key is the majority value per group over all aligned training pairs."""
import sys, re, unicodedata, collections
import os, pathlib
T = str(pathlib.Path(__file__).resolve().parent.parent)   # the target folder
D = T
def norm(s):
    s = re.sub(r'\[[^\]]*\]', '', s)
    s = s.replace('ñ','#').replace('Ñ','#'); s = unicodedata.normalize('NFD', s); s = ''.join(c for c in s if unicodedata.category(c) != 'Mn').replace('#','ñ')
    return re.sub(r'[^a-zñ]', '', s.lower())
def load():
    segs = {}
    for ln in open(os.path.join(D, 'transcription_LXVIII-1.14.1943.1.txt'), encoding='utf8'):
        if ln.startswith('#') or not ln.strip(): continue
        sid, rest = ln.rstrip('\n').split('\t'); g = rest.split(' | ')[1].strip()
        toks = []
        for t in g.split('-'):
            m = re.match(r'\[(\d\d)\|(\d\d)\]', t); toks.append(m.group(1) if m else t)
        segs[sid] = toks
    gl = {}
    for ln in open(os.path.join(D, 'gloss_LXVIII-1.14.1943.1.txt'), encoding='utf8'):
        if ln.startswith('#') or not ln.strip(): continue
        sid, t = ln.rstrip('\n').split('\t'); gl[sid] = norm(t)
    return segs, gl
def align(groups, text, key):
    n, m = len(groups), len(text); INF = 1e9
    best = [[INF] * (m + 1) for _ in range(n + 1)]; back = [[None] * (m + 1) for _ in range(n + 1)]
    best[0][0] = 0
    for i in range(n):
        g = groups[i]
        for j in range(m + 1):
            if best[i][j] >= INF: continue
            for L in range(0, 9):
                if j + L > m: break
                ch = text[j:j + L]
                if g in key: c = 0 if ch == key[g] else (1 + abs(len(ch) - len(key[g])) * 0.5)
                else: c = 0.5 + (0.3 if L == 0 else 0) + (0.2 * max(0, L - 1))
                if best[i][j] + c < best[i + 1][j + L]:
                    best[i + 1][j + L] = best[i][j] + c; back[i + 1][j + L] = (j, ch)
    out = []; j = m
    if best[n][m] >= INF: return None, INF
    for i in range(n, 0, -1):
        pj, ch = back[i][j]; out.append(ch); j = pj
    return out[::-1], best[n][m]
def build(train, segs, gl):
    key = {}; votes = collections.defaultdict(collections.Counter)
    for s in train:
        if len(segs[s]) == len(gl[s]):
            for g, c in zip(segs[s], gl[s]): votes[g][c] += 1
    key = {g: v.most_common(1)[0][0] for g, v in votes.items()}
    for it in range(4):
        votes = collections.defaultdict(collections.Counter)
        for s in train:
            al, cost = align(segs[s], gl[s], key)
            for g, ch in zip(segs[s], al): votes[g][ch] += 1
        key = {g: v.most_common(1)[0][0] for g, v in votes.items()}
    return key, votes
if __name__ == '__main__':
    segs, gl = load()
    train = sorted(segs) if sys.argv[1] == 'all' else sys.argv[1].split(',')
    key, votes = build(train, segs, gl)
    with open(sys.argv[2], 'w', encoding='utf8') as f:
        f.write('group\tvalue\tvotes\tall_values_seen\n')
        for g in sorted(key, key=lambda x: int(x)):
            f.write(f'{g}\t{key[g] or "(none)"}\t{votes[g][key[g]]}\t{dict(votes[g])}\n')
    print(len(key), 'groups'); print(' '.join(f'{g}={key[g]}' for g in sorted(key, key=int)))
