"""Decrypt the Morosini 1588-89 nunciature ciphers (ASV Segr. Stato Francia 22) with Meister no. 40.

Key: Meister, Die Geheimschrift im Dienste der papstlichen Kurie (1906), p. 393-394, no. 40,
"Con monsig. Moresino nuntio in Francia, 8 Giugno 1587" (also DECODE R18 DOC_3174/3175).
The digits run on without separators; codes are 1, 2 or 3 digits, so the reading is a beam
search over segmentations scored by the shared Italian model (lang/, it-cinquecento, no spaces).
Dotted codes (DECODE transcription 'X Y^. Z') are the nomenclator.

usage: python decrypt.py [record ...]      (default: all DOC_R*_D16xx/17xx/18xx transcriptions)
"""
import glob, os, re, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
for p in (os.path.join(HERE, '..'), os.path.join(HERE, '..', '..')):
    if os.path.isdir(os.path.join(p, 'lang')):
        sys.path.insert(0, os.path.abspath(p)); break
from lang import lm

LET = {
    'a': '21 212 2', 'b': '24 42', 'c': '25 52', 'd': '26 62', 'e': '35 153 5', 'f': '30 03',
    'g': '40 04', 'h': '41 14', 'i': '17 171 7', 'k': '60 06', 'l': '50 05', 'm': '20 02',
    'n': '10 01 0', 'o': '91 191 9', 'p': '70 07', 'qu': '90 09', 'r': '00 13 1', 's': '54 45 4',
    't': '51 15 6', 'u': '37 173 3', 'x': '11', 'z': '12', 'et': '16 69 75', 'con': '19 76 55',
    'cr': '22', 'fr': '23', 'gr': '59', 'lt': '27', 'mp': '29', 'nt': '31', 'ntr': '32', 'pr': '33',
    'scr': '36', 'sc': '34', 'sf': '57', 'sfr': '39', 'sgr': '43', 'sp': '44', 'spr': '46',
    'st': '47', 'str': '49', 'non': '61 71', 'che': '56', 'chi': '63', 'per': '64', 'perche': '65',
    'percioche': '66', 'accio': '67', 'acchioche': '72', 'nondimeno': '77', 'come': '79',
    'ancora': '92', 'ancorche': '93', 'benche': '94', 'qua': '95', 'que': '96', 'qui': '97',
    'quando': '99',
}
# second readings printed with a mark in Meister (sg 42, tr 49): allowed at a small cost
ALT = {'42': 'sg', '49': 'tr'}
NOM = {
    '111': 'il papa', '113': 'sua maesta', '114': 're di spagna', '112': "l'imperatore",
    '115': 're di polonia', '116': 'regina madre', '117': 'regina regnante', '119': "regina d'inghilterra",
    '121': 'signoria di genova', '122': 'signori venetiani', '123': 're di dania', '124': 're di suetia',
    '125': 'gran turco', '126': 'gran duca di toscana', '127': 'arciduca di', '129': 'duca di',
    '131': 'cardinale di', '132': 'principe di', '133': 'arciuescouo', '134': 'arciuescouado',
    '135': 'uescouo', '136': 'uescouado', '137': 'abbatia', '139': 'priorato', '141': 'clero',
    '142': 'presidente', '143': 'guerra', '144': 'pace', '145': 'triegua', '146': 'danari',
    '147': 'italia', '149': 'italiani', '151': 'francia', '152': 'franzesi', '154': 'spagna',
    '155': 'spagnioli', '156': 'alemagna', '157': 'alemani', '159': 'fiandra', '161': 'quanto',
    '163': 'quantunque', '164': 'qualmente', '165': 'quello', '166': 'questo', '167': 'u s illma',
    '169': 'u s', '172': 'fiamenghi', '173': 'inghilterra', '174': 'inglesi', '175': 'polonia',
    '176': 'polacchi', '177': 'turco', '179': 'ungaria', '192': 'bascia', '193': 'austria',
    '194': 'austriaci', '195': 'auignone', '196': 'sauoia', '197': 'geneura', '199': 'genoua',
    '211': 'genouesi', '213': 'ambassadore', '214': 'agente', '215': 'secretario', '216': 'auisi',
    '217': 'corriere', '219': 'cifra', '221': 'lettere', '222': 'santo officio', '223': 'inquisitione',
    '224': 'padri del iesu', '225': 'padri capuccini', '226': 'catolici', '227': 'heretici',
    '229': 'ugonotti', '231': 'principe di conde', '232': 'il gia re di nauarra',
}
CODES = {}
for pt, cs in LET.items():
    for c in cs.split():
        CODES.setdefault(c, []).append((pt, 0.0))
for c, pt in ALT.items():
    CODES.setdefault(c, []).append((pt, -2.0))
NULL_COST = -4.0

# Second key (DECODE 'F22b', reconstructed by Lasry 2020, incomplete): items 22/32-33 (R53, R54).
# Syllabic, 1-2 digit elements, no nulls; dotted codes carry the dot on the FIRST digit.
KEYB = dict(x.split(' - ') for x in '''3|7 - a;86 - ba;55 - bi;64 - bo;73 - ca;51 - ce;40 - ci;16 - co;20 - cu;91 - d;76 - da;99 - de;93 - di;44 - do;5|8 - e;79 - fa;97 - fe;67 - fo;12 - g;37 - ga;22 - ge;28|71 - gi;61 - go;9 - h;98 - he;17|6 - i;14 - l;60 - la;26 - le;25 - li;29 - lo;10 - m;92 - mo;23 - n;74 - na;70 - ne;31 - ni;36 - no;15|18 - o;80 - p;49 - pa;52 - pe;33 - pi;32 - qua;35 - que;34 - r;41 - ra;43 - re;48 - ri;63 - ro;19 - s;78 - sa;83|85|89|95 - si;96 - so;62 - su;30 - t;47 - ta;50 - te;56 - ti;58 - to;65 - tu;21|54 - u;82 - za;102 - mpo;106 - mi;116|216 - me;130 - ma;495|498 - chi;496 - che'''.split(';'))
CODES_B = {}
for cs, pt in KEYB.items():
    for c in cs.split('|'):
        CODES_B.setdefault(c, []).append((pt, 0.0))
NOM_B = {'116': 're', '216': 're', '124': 'umena', '137': 'al', '151': 'sua santita', '185': 'nauarro', '186': 'mente'}
B_RECORDS = {'R53', 'R54'}

M = lm.load('it-cinquecento', spaces=False)
A, K = M.A, M.order
IDX = M.index
LP = M.lp.reshape(-1, A)          # row = context of K-1 chars


def enc(s):
    return [IDX[ch] for ch in lm.norm(s, 'early', False)]


def step(ctx, chars):
    """Advance context (int of K-1 chars) over chars; return (new ctx, logp)."""
    s = 0.0
    mod = A ** (K - 1)
    for x in chars:
        s += float(LP[ctx, x])
        ctx = (ctx * A + x) % mod
    return ctx, s


def parse(path, dot_first=False):
    """Yield (image, items); an item is a digit '0'-'9' or ('N', code) for a dotted code."""
    out, cur, items = [], None, []
    for line in open(path, encoding='utf-8', errors='replace'):
        line = line.rstrip('\n')
        m = re.match(r'#IMAGE NAME:\s*(\S+)', line)
        if m:
            if items:
                out.append((cur, items))
            cur, items = m.group(1), []
            continue
        if line.startswith('#'):
            continue
        line = re.sub(r'<[^>]*>', ' ', line)
        toks = line.split()
        i = 0
        while i < len(toks):
            t = toks[i]
            if '^.' in t and dot_first:
                ds = re.sub(r'\D', '', t) + ''.join(re.sub(r'\D', '', x) for x in toks[i + 1:i + 3])
                items.append(('N', ds[:3]))
                items.extend(ds[3:])
                i += 3
                continue
            if '^.' in t and items and i + 1 < len(toks):
                prev = items.pop() if items and isinstance(items[-1], str) else '?'
                d = re.sub(r'\D', '', t)
                nxt = re.sub(r'\D', '', toks[i + 1])[:1]
                items.append(('N', prev + d + nxt))
                rest = re.sub(r'\D', '', toks[i + 1])[1:]
                items.extend(rest)
                i += 2
                continue
            items.extend(re.sub(r'\D', '', t))
            i += 1
    if items:
        out.append((cur, items))
    return out


def decode(items, beam=400, codes=None, nom=None, nulls=True):
    codes, nom = codes or CODES, nom or NOM
    start = 0
    for x in enc('ente'):
        start = (start * A + x) % (A ** (K - 1))
    # states at each position: ctx -> (score, back)
    n = len(items)
    states = [dict() for _ in range(n + 1)]
    states[0][start] = (0.0, None)
    for p in range(n):
        if not states[p]:
            continue
        best = sorted(states[p].items(), key=lambda kv: -kv[1][0])[:beam]
        for ctx, (sc, _) in best:
            it = items[p]
            moves = []
            if isinstance(it, tuple):
                code = it[1]
                pt = nom.get(code)
                if pt:
                    moves.append((1, '[' + pt.upper() + ']', enc(pt), 0.0))
                else:
                    moves.append((1, '[' + code + '?]', [], -6.0))
            else:
                for L in (1, 2, 3):
                    seg = items[p:p + L]
                    if len(seg) < L or not all(isinstance(x, str) for x in seg):
                        break
                    code = ''.join(seg)
                    if nulls and L == 2 and code[0] == '8':
                        moves.append((2, '', [], NULL_COST))
                    for pt, pen in codes.get(code, []):
                        moves.append((L, pt, enc(pt), pen))
                if nulls and it == '8':
                    moves.append((1, '', [], NULL_COST - 2))
                if not moves:
                    moves.append((1, '?', [], -12.0))
            for L, txt, chars, pen in moves:
                nctx, s = step(ctx, chars)
                ns = sc + s + pen
                q = p + L
                old = states[q].get(nctx)
                if old is None or ns > old[0]:
                    states[q][nctx] = (ns, (p, ctx, txt))
    end = max(states[n].items(), key=lambda kv: kv[1][0])
    out, q, ctx = [], n, end[0]
    while states[q][ctx][1] is not None:
        p, pctx, txt = states[q][ctx][1]
        out.append(txt)
        q, ctx = p, pctx
    return ''.join(reversed(out)), end[1][0] / max(1, n)


def main():
    # Since the 14 Oct 2026 split the F22b records R53/R54 live in ../morosini1589/decode/ (their own entry):
    # `python decrypt.py --f22b > ../morosini1589/decrypt_raw.txt`. R17 (Francia 18/3) was decoded with this
    # script from ../bergamo1585 before it moved here: `python decrypt.py R17_transcription_decode.txt`.
    args = sys.argv[1:]
    where = os.path.join(HERE, 'decode')
    if args[:1] == ['--f22b']:
        args, where = args[1:], os.path.join(HERE, '..', 'morosini1589', 'decode')
    files = args or sorted([f for f in glob.glob(os.path.join(where, 'DOC_R*_D1[678]*.txt')) if 'Francia 22' in open(f, encoding='utf-8', errors='replace').read(300) and '<ABBR' not in open(f, encoding='utf-8', errors='replace').read()])
    for f in files:
        rec = re.search(r'(R\d+)_', os.path.basename(f)).group(1)
        b = rec in B_RECORDS
        for img, items in parse(f, dot_first=b):
            txt, per = decode(items, codes=CODES_B, nom=NOM_B, nulls=False) if b else decode(items)
            print(f'== {rec} {img} ({len(items)} items, {per:.2f}/item)')
            print(txt)
            print()


if __name__ == '__main__':
    main()
