#!/usr/bin/env python3
# Strict judge scoring for baselANV9 decode. Each fragment: (text, strict tag, lenient tag).
# Tags: S = all letters S; N = all N; E1 = one letter E, rest S; E2 = two letters E, rest S.
# Strict rule: a word with more than one wrong/inserted/missing letter is N.
# Lenient rule (sensitivity only): a long word with exactly two slips scores 2 E, rest S.
# Fragments of "=" joins carry the word's tag; the E letter sits in the fragment marked E1, the other fragment is S.
import re, os

W = {}  # line -> list of fragments
def L(key, *frags):
    W[key] = list(frags)

def f(t, s, l=None):
    return (t, s, l if l else s)

# ---------- H1 ----------
L('H1 L01', f('et','S'), f('per','S'), f('omnia','S'), f('documenta','S'), f('in','S'), f('fide','S'),
  f('irrstiana','N'), f('sunt','S'))
L('H1 L02', f('instituta','S'), f('et','S'), f('per','S'), f('sabctorum','E1'), f('bgnia','N'), f('bgni','E1'),
  f('imma','S'))
L('H1 L03', f('culate','S'), f('seqenuaa','N'), f('uestigrit','N'), f('et','S'), f('per','S'), f('omnes','S'),
  f('sanct','S'))
L('H1 L04', f('quo','S'), f('des','E1'), f('eregit','E1'), f('anr','E1'), f('mundi','S'), f('iabcta','E1'),
  f('fundbenta','E1'))
L('H1 L05', f('et','S'), f('pmer','E1'), f('iorum','E1'), f('meita','E1'), f('in','S'), f('gbudis','E1'),
  f('et','S'), f('grbait','N'))
L('H1 L06', f('sunt','S'), f('apud','S'), f('deum','S'))
L('H1 L07', f('alia','S'), f('coniubits','N'))
L('H1 L08', f('adiuo','E1'), f('u','S'), f('dimones','E1'), f('in','S'), f('qubcuque','N','E2'), f('parr','E1'), f('mundi','S'))
L('H1 L09', f('sits','E1'), f('per','S'), f('aiunciai','N'), f('irr','N'), f('per','S'), f('aduentun','E1'))
L('H1 L10', f('irr','N'), f('per','S'), f('nateeitatem','N','E2'), f('irr','N'), f('per','S'), f('circumci','S'))
L('H1 L11', f('siune','E1'), f('et','S'), f('bapisum','N','E2'), f('irr','N'), f('per','S'), f('ieiunuum','E1'),
  f('et','S'), f('trans','N'))
L('H1 L12', f('figmuaitne','N'), f('irr','N'), f('in','S'), f('monr','E1'), f('tabor','S'), f('per','S'),
  f('atundique','N'))
# ---------- H2 ----------
L('H2 L00', f('sigillu','E1'), f('ioui','S'))
L('H2 L01', f('fit','S'), f('ex','S'), f('oimi','S'), f('anglico','S'), f('stanno','S'), f('habesn','E1'), f('in','S'))
L('H2 L02', f('unque','E1'), f('parr','E1'), f('figuam','E1'), f('secunda','S'), f('ita','S'), f('ses','N'),
  f('nueers','N','E2'))
L('H2 L03', f('et','S'), f('ceuuulis','N'), f('dniositam','N'), f('sics','N'), f('anpparet','E1'), f('in','S'))
L('H2 L04', f('frontesticis','N','E2'), f('pro','S'), f('reliqua','S'), f('facies','S'), f('adhi','S'))
L('H2 L05', f('benda','S'), f('imabgo','E1'), f('seu','S'), f('tetpu','N'), f('planet','S'))
L('H2 L06', f('uir','S'), f('sanbcerdotolis','N'), f('et','S'), f('pcilosopcu','N'), f('in','S'), f('li','S'))
L('H2 L07', f('brum','S'), f('iniicoen','N'), f('ut','S'), f('reges','S'), f('supe','E1'), f('abps','N'), f('euiu','N'))
L('H2 L08', f('signbbis','N','E2'), f('quasudam','E1'), f('steuua','N'), f('cum','S'), f('nomine','S'), f('hoc','S'),
  f('iuupu','N'))
L('H2 L09', f('ten','N'), f('et','S'), f('contera','N','E2'), f('ut','S'), f('in','S'), f('prrorr','N'), f('idea','S'),
  f('sanbpni','N'))
L('H2 L10', f('tandes','E1'), f('obseruata','S'), f('in','S'), f('aliquo','S'), f('die','S'), f('iouis','S'))
L('H2 L11', f('quasn','N'), f('lona','E1'), f('intrit','E1'), f('prrmum','N','E2'), f('grbdum','E1'), f('librann','N'),
  f('et','S'), f('iu','S'))
L('H2 L12', f('pitet','E1'), f('intet','E1'), f('reliquo','E1'), f('planetu','N','E2'), f('fuerit','S'), f('bene','S'))
L('H2 L13', f('constitutum','S'), f('tunc','S'), f('funde','S'), f('et','S'), f('imprrme','N','E2'), f('tuum','S'),
  f('si','S'))
L('H2 L14', f('gnillum','E1'), f('et','S'), f('seua','E1'), f('ipum','E1'), f('in','S'), f('panno','S'), f('aliquo','S'))
L('H2 L15', f('ceuleo','E1'), f('seritco','E1'))
L('H2 L16', f('uirtutem','E1'), f('huiu','E1'), f('sunt','S'))
L('H2 L17', f('hoc','S'), f('signum','S'), f('gestbtum','E1'), f('amore','S'), f('graiam','E1'), f('aaiciiam','N','E2'))
L('H2 L18', f('et','S'), f('fauorem','S'), f('concilian','E1'), f('apud','S'), f('omnes','S'), f('homines','S'))
L('H2 L19', f('quocunque','S'), f('in','S'), f('loco','S'), f('repositum','S'), f('fuerit','S'), f('miran','N','E1'))
L('H2 L20', f('bilitet','N','E1'), f('buges','N','E2'), f('fortuna','E1'), f('et','S'), f('substanim','N','E2'))
L('H2 L21', f('qui','S'), f('hoc','S'), f('signum','S'), f('portan','E1'), f('secum','S'), f('in','S'), f('omnibs','E1'),
  f('nego','N','S'))
L('H2 L22', f('tes','N','E2'), f('uotum','S'), f('suum','S'), f('consequei','E1'), f('et','S'), f('metu','S'),
  f('uacabit','S'))
# ---------- H3 ----------
L('H3 P3', f('non','S'), f('tiebit','E1'), f('diabolum','S'), f('nec','S'), f('pcanta','N'), f('etotd','N'),
  f('usquod','N'))
L('H3 P4', f('qui','S'), f('hoc','S'), f('signum','S'), f('portan','E1'), f('i','N'), f('peribit','S'), f('in','S'),
  f('arms','E1'))

def score(frags, mode):
    S = E = N = 0
    for t, s, l in frags:
        tag = s if mode == 'strict' else l
        n = len(t)
        if tag == 'S': S += n
        elif tag == 'N': N += n
        elif tag == 'E1': E += 1; S += n - 1
        elif tag == 'E2':
            k = min(2, n); E += k; S += n - k
    return S, E, N

here = os.path.dirname(os.path.abspath(__file__))
dec = {}
for ln in open(os.path.join(here, 'decode.txt'), encoding='utf-8'):
    if '\t' in ln:
        k, v = ln.rstrip('\n').split('\t', 1)
        dec[k] = v

# integrity: fragment letters must equal decode letters per line
for k, v in dec.items():
    want = re.sub(r'[^a-z]', '', v)
    got = ''.join(t for t, _, _ in W[k])
    assert want == got, (k, want, got)
assert set(dec) == set(W)

rows = []
tot = {}
for k in dec:
    S, E, N = score(W[k], 'strict')
    Sl, El, Nl = score(W[k], 'lenient')
    q = dec[k].count('?')
    blk = k.split()[0]
    for m, tri in (('strict', (S, E, N)), ('lenient', (Sl, El, Nl))):
        a = tot.setdefault((blk, m), [0, 0, 0, 0])
        for i in range(3): a[i] += tri[i]
        if m == 'strict': a[3] += q
    rows.append((k, S, E, N, q, ' '.join(t + ('' if s == 'S' else '[' + s + ']') for t, s, _ in W[k])))

with open(os.path.join(here, 'judge.tsv'), 'w', encoding='utf-8') as o:
    o.write('line\tset\tletters\tS\tE\tN\tq\treading (strict tags)\n')
    for k, S, E, N, q, r in rows:
        o.write(f'{k}\t{k.split()[0]}\t{S+E+N}\t{S}\t{E}\t{N}\t{q}\t{r}\n')

print('line      letters  S   E   N  ?  %S')
for k, S, E, N, q, r in rows:
    print(f'{k:9s} {S+E+N:5d} {S:4d}{E:4d}{N:4d}{q:3d} {100*S/(S+E+N):5.1f}')
for m in ('strict', 'lenient'):
    print(f'--- {m} ---')
    G = [0, 0, 0]
    for b in ('H1', 'H2', 'H3'):
        S, E, N = tot[(b, m)][:3]
        for i, x in enumerate((S, E, N)): G[i] += x
        q = tot[(b, 'strict')][3]
        print(f'{b}: S {S}/{S+E+N} = {100*S/(S+E+N):.1f}%  E {E}  N {N}  ?={q}')
    S, E, N = G
    print(f'ALL: S {S}/{S+E+N} = {100*S/(S+E+N):.1f}%  E {E}  N {N}  (S+E {100*(S+E)/(S+E+N):.1f}%)')
low = min(rows, key=lambda r: r[1] / (r[1] + r[2] + r[3]))
print('lowest line (strict):', low[0], f'{100*low[1]/(low[1]+low[2]+low[3]):.1f}%')
