"""Per-token Viterbi/beam decode of the transcription with the Zifra Prima (R1789) key, allowing each token to be
re-read under digit confusions (cost COST per changed digit). Score: 5-gram LM + CLEN per char - COST*changes -
WPEN per nomenclature word (value of 5+ letters). Context-merged beam."""
import sys, os, itertools, json, math
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm
SP = os.environ.get('SPACES', '1') == '1'
m = lm.load('it-cinquecento', order=5, spaces=SP) if SP else lm.load('it-cinquecento', order=5, spaces=False)
ctf = sys.argv[1] if len(sys.argv) > 1 else 'ct_all.txt'
keyf = os.environ.get('KEY', 'keys/zifra_prima_R1789.tsv')
CLEN = float(os.environ.get('CLEN', 1.6)); COST = float(os.environ.get('COST', 1.0)); WPEN = float(os.environ.get('WPEN', 3.0))
BEAM = int(os.environ.get('BEAM', 300))
# cost of reading digit X in the transcription when the hand wrote Y: CONF[X][Y]
CONF = {'0': {'0': 0, '8': 0.7, '6': 2.5}, '1': {'1': 0, '7': 1.5}, '2': {'2': 0, '7': 0.7, '3': 2.0},
        '3': {'3': 0, '5': 1.5, '2': 2.0, '8': 2.0}, '4': {'4': 0}, '5': {'5': 0, '3': 1.0, '8': 1.5},
        '6': {'6': 0, '8': 2.5}, '7': {'7': 0, '1': 2.0, '2': 2.0}, '8': {'8': 0, '5': 1.0, '3': 2.0, '0': 2.5, '6': 2.5},
        '9': {'9': 0, '7': 2.0}}
CONF = {k: {a: b * float(os.environ.get('CSCALE', 1.0)) for a, b in v.items()} for k, v in CONF.items()}
if os.environ.get('CONFFILE'):
    CONF = json.load(open(os.environ['CONFFILE']))
key = {}
for l in open(keyf, encoding='utf8'):
    if l.startswith('#') or not l.strip(): continue
    k, v = l.rstrip('\n').split('\t')[:2]; key[k] = v
EXP = [('M.ta', 'Maesta'), ('Sig.ria', 'Signoria'), ('Ill.ma', 'Illustrissima'), ('Ser.mo', 'Serenissimo'),
       ('Cons. di X', 'Consiglio di Dieci'), ('Capi di X', 'Capi di Dieci'), ('Gio.', 'Giovanni'), ('Mons.', 'Monsignor'),
       ('Sig.', 'Signor'), ('Princ.', 'Principe'), ('V.ra', 'Vostra')]
if os.path.exists('keys/ottobon_overrides.tsv') and not os.environ.get('NOOVR'):
    for l in open('keys/ottobon_overrides.tsv', encoding='utf8'):
        if l.startswith('#') or not l.strip(): continue
        k, v = l.rstrip(chr(10)).split(chr(9))[:2]; key[k] = v
def val(k):
    v = key[k]
    if v == '_' or v.startswith('#'): return ''
    for a, b in EXP: v = v.replace(a, b)
    return lm.norm(v, 'early')
def variants(t):
    b, n = t[0], t[1:]
    out = {}
    tab = (lambda p, d: list(CONF[p].get(d, {d: 0}))) if 'T' in CONF else (lambda p, d: list(CONF.get(d, {d: 0})))
    pos = ['S'] if len(n) == 1 else ['T', 'U']
    for combo in itertools.product(*[tab(p, d) for p, d in zip(pos, n)]):
        s = ''.join(combo).lstrip('0')
        if not s or int(s) > 99: continue
        if 'T' in CONF:
            pos = ['S'] if len(n) == 1 else ['T', 'U']
            c = sum(CONF[p].get(x, {x: 0}).get(y, 9) for p, x, y in zip(pos, n, combo))
        else:
            c = sum(CONF.get(x, {x: 0})[y] for x, y in zip(n, combo))
        k = b + s
        if k in key and (k not in out or out[k] > c): out[k] = c
    return out
lines = []
for l in open(ctf, encoding='utf8'):
    if l.startswith('#') or not l.strip(): continue
    lines.append([t.rstrip('?') for t in l.split()])
toks = [t for L in lines for t in L]
A, idx, lp, K = m.A, m.index, m.lp, m.order
def step(ctx, ch):
    # ctx: tuple of up to K-1 indices
    c = idx[ch]
    if len(ctx) < K - 1:
        return ctx + (c,), 0.0
    code = 0
    for x in ctx: code = code * A + x
    code = code * A + c
    return ctx[1:] + (c,), float(lp[code])
beam = {(): (0.0, None)}
hist = []
for t in toks:
    cands = variants(t) if (t[0] in 'acdfgh' and t[1:].isdigit()) else {}
    opts = [(k, c) for k, c in cands.items()] or [(None, 0)]
    nb = {}
    for ctx, (sc, bp) in beam.items():
        for k, c in opts:
            s = sc - COST * c
            v = val(k) if k else ''
            if k is None: s -= 6
            if len(v) >= 5: s -= WPEN
            for pre in ([' ', ''] if SP and v else ['']):
                s2 = s; cx = ctx
                for ch in pre + v:
                    if ch not in idx: continue
                    cx, l = step(cx, ch); s2 += l + (CLEN if ch != ' ' else 0)
                if cx not in nb or nb[cx][0] < s2:
                    nb[cx] = (s2, (bp, t, k, pre))
    beam = dict(sorted(nb.items(), key=lambda kv: -kv[1][0])[:BEAM])
best = max(beam.values(), key=lambda v: v[0])
seq = []; bp = best[1]
while bp: bp, t, k, pre = bp; seq.append((t, k, pre))
seq.reverse()
out = []
for t, k, pre in seq:
    v = key.get(k, '?') if k else '[' + t + ']'
    out.append(v if k == t else '%s<%s>' % (v, k) if k else v)
plain = ''.join(pre + (val(k) if k else '?') for t, k, pre in seq)
i = 0
for L in lines:
    print(' '.join(out[i:i + len(L)])); i += len(L)
chg = sum(1 for t, k, p in seq if k != t)
open(os.environ.get('PLAINOUT', 'beam_plain.txt'), 'w', encoding='utf8').write(plain)
print('# changed tokens', chg, 'of', len(seq), file=sys.stderr)
json.dump(seq, open(os.environ.get('SEQOUT', 'beam_seq.json'), 'w'))
