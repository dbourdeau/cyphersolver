# Beam decoder for the 1520-21 sign cipher (2 Oct 2026).
# Tokens from a transcription line (labels of seg21/signs.md); ligatures merged: o SL o -> OSO (= o), m t -> MT,
# n t -> NT, z t -> ZQ (z+ = q), x t -> XQ (x+ = q), o o -> OO (= b). Each sign's candidate values come from
# key21_counts.json plus the values fixed on V1921 (lone o = h/u/null, OO = b); any other letter is allowed at a
# penalty (OFFKEY) so the language model can show where the transcription or the key is wrong. Off-key letters print
# in CAPITALS: they are proposals to check on the image, not readings.
# Usage: python beam21.py R1136 [file]   (file defaults to caprile1521_transcription.txt)
import os, sys, re, json, math, collections
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm

HERE = os.path.dirname(os.path.abspath(__file__))
OFFKEY = -7.0
BEAM = 3000

def tokens(line):
    s = re.sub(r'\[[^\]]*\]', ' | ', line.split(':', 1)[1])
    s = ' ' + ' '.join(x.rstrip('?') for x in s.split()) + ' '
    for a, b in [(' o SL o ', ' OSO '), (' m t ', ' MT '), (' n t ', ' NT '), (' z t ', ' ZQ '), (' x t ', ' XQ '),
                 (' z+ ', ' ZQ '), (' x+ ', ' XQ '), (' xp ', ' XQ '), (' Zp ', ' XQ '), (' Z+ ', ' ZQ '), (' o+ ', ' OP '), (' oSLo ', ' OSO '), (' oo ', ' OO ')]:
        while a in s:
            s = s.replace(a, b)
    s = s.replace(' o o ', ' OO ')
    return [t for t in s.split()]

def priors():
    C = json.load(open(os.path.join(HERE, 'key21_counts.json'), encoding='utf8'))
    P = {}
    for sgn, c in C.items():
        n = sum(c.values())
        P[sgn] = {l: math.log((k + 0.3) / (n + 1)) for l, k in c.items()}
    P['o'] = {'': math.log(0.4), 'h': math.log(0.25), 'u': math.log(0.2), 'o': math.log(0.15)}
    P['OSO'] = {'o': 0.0}
    P['OO'] = {'b': math.log(0.7), '': math.log(0.1), 'u': math.log(0.1), 'h': math.log(0.1)}
    P['ZQ'] = {'q': 0.0}
    P['XQ'] = {'q': 0.0}
    P['EL'] = {'p': math.log(0.6), 'f': math.log(0.4)}
    P['AMP'] = {'p': math.log(0.6), 'f': math.log(0.4)}
    P['K'] = {'t': math.log(0.6), 'e': math.log(0.2), 'm': math.log(0.2)}
    P['Z'] = {'x': math.log(0.6), 'q': math.log(0.4)}
    P['8'] = {'e': math.log(0.8), '': math.log(0.2)}
    P['SL'] = {'': 0.0}
    if os.environ.get('LOOK'):                           # look-alike tabulation (lookalike21.py, 3 Oct 2026)
        P['EL'] = {'p': math.log(0.45), 'd': math.log(0.4), 'f': math.log(0.15)}
        P['AMP'] = {'p': math.log(0.7), 'd': math.log(0.15), 'f': math.log(0.15)}
        P['c'] = {'o': math.log(0.45), 'e': math.log(0.35), 'c': math.log(0.2)}
        P['x'] = {'r': math.log(0.8), 'q': math.log(0.2)}
        P['8'] = {'e': math.log(0.4), 'o': math.log(0.3), 't': math.log(0.3)}
    if os.environ.get('FREE'):                           # test signs as letters with no prior (numeral question)
        for t in os.environ['FREE'].split(','): P[t] = {c: math.log(1 / 22) for c in 'abcdefghilmnopqrstuxz'}; P[t][''] = math.log(1 / 22)
    P['OP'] = {'s': 0.0}                                   # o+ (R1136 pass 4: presia, esser)
    P['D'] = {'b': math.log(0.5), 'x': math.log(0.5)}      # Bachiensis; Excelentia, excludera
    P['c'] = {'o': math.log(0.7), 'c': math.log(0.3)}      # plain c: inteso, ho
    P['QB'] = {'o': math.log(0.75), 't': math.log(0.1), 'e': math.log(0.1), 'd': math.log(0.05)}
    return P

def decode(toks, m, P):
    A = m.A; k = m.order; idx = m.index; letters = [c for c in m.alpha if c != ' ']
    beams = {(): (0.0, '')}   # context tuple -> (score, text with case marks)
    for t in toks:
        if t in ('|', '#'):
            cand = {'': 0.0} if t == '|' else {c: -3.0 for c in letters}
        else:
            cand = dict(P.get(t, {}))
            for c in letters:
                if c not in cand: cand[c] = OFFKEY
        nb = {}
        for ctx, (sc, txt) in beams.items():
            for v, pv in cand.items():
                s2 = sc + pv; c2 = ctx; t2 = txt
                for ch in v:
                    i = idx[ch]
                    if len(c2) == k - 1:
                        flat = 0
                        for x in c2: flat = flat * A + x
                        s2 += float(m.lp[flat * A + i])
                    c2 = (c2 + (i,))[-(k - 1):]
                mark = v.upper() if pv == OFFKEY else (v if v else '_' if t == 'o' else '')
                if t == '#': mark = v.upper()
                t2 = txt + mark
                if c2 not in nb or nb[c2][0] < s2:
                    nb[c2] = (s2, t2)
        beams = dict(sorted(nb.items(), key=lambda kv: -kv[1][0])[:BEAM])
    return max(beams.values())

def main():
    src = sys.argv[1]
    f = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, 'caprile1521_transcription.txt')
    m = lm.load('it-cinquecento', spaces=False)
    P = priors()
    for line in open(f, encoding='utf8'):
        if not line.startswith(src + ' '): continue
        toks = tokens(line)
        sc, txt = decode(toks, m, P)
        n = sum(1 for t in toks if t not in ('|',))
        off = sum(1 for ch in txt if ch.isupper())
        print(line.split(':')[0], f'[{n} signs, {off} off-key]', txt)

if __name__ == '__main__':
    main()
