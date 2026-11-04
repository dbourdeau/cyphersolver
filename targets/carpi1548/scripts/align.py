"""Align the cipher of letter 1 (transcription/d1_digits.txt) with its contemporary decipherment
(decipherment/d1_contemporary.txt) and rebuild the key, by iterative Viterbi alignment.

Pass 1: two-digit groups only. Moves: group -> letter, group -> whole word (code group), doubled letter written once
(no digits), group -> nothing (null), and 1- or 3-digit slips (transcription errors).
Pass 2: a letter may also be a 1- or 3-digit unit; the key is learnt for every length, so recurring units show up
as key entries and one-off units remain as candidate misreadings.

Writes key/key_d1_rebuilt.json (key and code groups) and key/key_d1_rebuilt.tsv, and prints the counts.
Usage (from the target folder): python3 scripts/align.py
"""
import collections, json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent

def digits(path, prefixes):
    s = ''
    for line in (ROOT / path).read_text(encoding='utf-8').splitlines():
        if line[:2] in prefixes:
            body = line.split(None, 1)[1].split('[')[0]
            s += re.sub(r'[^0-9d]', '', body).replace('d', '8')
    return s

def plaintext(path):
    txt = ' '.join(l for l in (ROOT / path).read_text(encoding='utf-8').splitlines() if l and not l.startswith('#'))
    words = [w for w in (re.sub(r'[^a-z]', '', w) for w in txt.lower().replace('à', 'a').split()) if w]
    L = ''.join(words); wstart = set(); wend = {}; p = 0
    for w in words:
        wstart.add(p); wend[p] = p + len(w); p += len(w)
    return L, wstart, wend

S = digits('transcription/d1_digits.txt', ('r1', 'v1', 's1'))
L, WSTART, WEND = plaintext('decipherment/d1_contemporary.txt')
N, M = len(S), len(L)
norm = lambda c: 'u' if c == 'v' else c

# seed: values read by hand from a few stretches ("in questo modo pare haver ... fatto alcun ritratto ... speranza", "la negociatione")
SEED = {'15': 'o', '37': 'o', '19': 'm', '12': 'd', '46': 'p', '52': 'a', '30': 'a', '65': 'r', '50': 'e', '47': 'e',
        '70': 'h', '45': 'u', '87': 't', '58': 'f', '92': 'l', '25': 'c', '28': 'n', '26': 'i', '32': 'z', '54': 'u',
        '16': 'n', '82': 'q', '76': 's'}

def viterbi(K, CODE, lengths):
    INF = 1e18; band = 170; cost = {(0, 0): 0.0}; back = {}
    unk = {1: 9, 2: 4, 3: 7}
    for i in range(N + 1):
        jc = int(i / N * M)
        for j in range(max(0, jc - band), min(M, jc + band) + 1):
            c = cost.get((i, j))
            if c is None: continue
            def push(ni, nj, add, how):
                if ni > N or nj > M: return
                if c + add < cost.get((ni, nj), INF): cost[(ni, nj)] = c + add; back[(ni, nj)] = (i, j, how)
            if j < M:
                ch = norm(L[j])
                for n in lengths:
                    g = S[i:i+n]
                    if len(g) < n: continue
                    v = K.get(g)
                    if n == 2 or len(lengths) > 1:
                        wrong = 9 if len(lengths) == 1 else 10 + n
                        push(i+n, j+1, 0 if v == ch else (unk[n] if v is None else wrong), ('L', g, ch))
                if len(lengths) == 1:
                    for d in (1, 3): push(i+d, j+1, 12, ('S', S[i:i+d], ch))
                g = S[i:i+2]
                if len(g) == 2 and j in WSTART and WEND[j] - j >= 2:
                    w = L[j:WEND[j]]
                    push(i+2, WEND[j], 1 if CODE.get(g) == w else (5 if g not in K else 11), ('W', g, w))
                if j > 0 and L[j] == L[j-1]: push(i, j+1, 0.5, ('D', '', L[j]))
            if i + 2 <= N: push(i+2, j, 6, ('N', S[i:i+2], ''))
            if i + 1 <= N: push(i+1, j, 10 if len(lengths) == 1 else 9, ('X' if len(lengths) == 1 else 'N', S[i], ''))
    k = (N, M); path = []
    while k != (0, 0):
        i, j, how = back[k]; path.append((i, j, how)); k = (i, j)
    return cost[(N, M)], path[::-1]

def reestimate(path):
    cnt = collections.defaultdict(collections.Counter); wc = collections.defaultdict(collections.Counter)
    for _, _, (t, g, x) in path:
        if t == 'L': cnt[g][x] += 1
        if t == 'W': wc[g][x] += 1
    K = {g: c.most_common(1)[0][0] for g, c in cnt.items() if c.most_common(1)[0][1] >= 2}
    CODE = {g: c.most_common(1)[0][0] for g, c in wc.items() if c.most_common(1)[0][1] >= 2}
    return K, CODE, cnt, wc

K, CODE = dict(SEED), {}
for lengths, rounds in (((2,), 4), ((1, 2, 3), 4)):
    for r in range(rounds):
        tot, path = viterbi(K, CODE, lengths)
        K, CODE, cnt, wc = reestimate(path)
        moves = collections.Counter((h[0], len(h[1])) for _, _, h in path)
        print(f'pass {len(lengths) > 1 and 2 or 1} round {r}: cost {tot:.0f}', dict(sorted(moves.items())))

Lu = [h for _, _, h in path if h[0] == 'L']
agree = sum(1 for t, g, x in Lu if K.get(g) == x)
oneoff = collections.Counter(h[1] for h in Lu if len(h[1]) != 2)
print(f'digits {N}, plaintext letters {M}')
print(f'letter units {len(Lu)}, agreeing with the final key {agree} ({agree / len(Lu):.1%}); '
      f'word groups {sum(1 for _, _, h in path if h[0] == "W")}; doubled letters {sum(1 for _, _, h in path if h[0] == "D")}; '
      f'one-off irregular units {sum(1 for h in Lu if len(h[1]) != 2 and oneoff[h[1]] == 1)}')

(ROOT / 'key').mkdir(exist_ok=True)
json.dump({'K': K, 'CODE': CODE}, open(ROOT / 'key/key_d1_rebuilt.json', 'w'), indent=0, sort_keys=True)
with open(ROOT / 'key/key_d1_rebuilt.tsv', 'w', encoding='utf-8') as f:
    f.write('# carpi1548: key rebuilt from letter 1 alone (scripts/align.py). group, value, units agreeing / units aligned\n')
    for g, c in sorted(cnt.items(), key=lambda kv: (len(kv[0]), kv[0])):
        x, n = c.most_common(1)[0]
        if n >= 2: f.write(f'{g}\t{x}\t{n}/{sum(c.values())}\n')
    f.write('# word groups\n')
    for g, c in sorted(wc.items()):
        w, n = c.most_common(1)[0]
        if n >= 2: f.write(f'{g}\t[{w}]\t{n}/{sum(c.values())}\n')
