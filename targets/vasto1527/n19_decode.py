"""No. 19 (BnF fr. 3022 ff. 41r-42r): decode the sign transcription with George Lasry's Cipher 2 key, unchanged,
and run the pre-registered held-out check (PREREG_n19.md).

  python3 n19_decode.py n19_transcription.txt [--lexicon es.json.gz] [--measure]

Notation of the transcription: see its header. Letter classes follow Lasry's key image (prior/BnF_fr3022_f16.png).
"""
import sys, json, gzip, random, re

# Lasry's letter classes: cipher forms (this transcription's notation) -> plaintext
LETTERS = {
    'a': ['b', 'B'], 'b': ['ct', 'c'], 'c': ['d'], 'd': ['e'], 'e': ['fi', 'f'], 'f': ['g'], 'g': ['h'],
    'h': ['LH'], 'i': ['l', 'T', 't'], 'j': [], 'l': ['m', 'n'], 'm': ['nn'], 'n': ['o', '4', 'z'], 'o': ['p'],
    'p': ['q'], 'r': ['s', 'E'], 's': ['tt'], 't': ['x', 'ci'], 'v': ['#'], 'y': ['Z', '@'], 'x': ['y'],
}
# Lasry's two-per-syllable signs (his labels) and nomenclator groups: fixed labels, not scored
SYLL = {'bie': 'al', 'bar': 'con', 'bop': 'con', 'bis': 'de', 'cif': 'de', 'biz': 'el', 'boe': 'el', 'baz': 'es',
        'bep': 'es', 'bnz': 'la', 'cem': 'la', 'bap': 'lo', 'ram': 'lo', 'cnz': 'no', 'ras': 'no', 'bes': 'para',
        'cep': 'para', 'dur': 'por', 'dir': 'por', 'rem': 'por', 'ciq': 'qve', 'dio': 'qve', 'bab': 'sin',
        'boz': 'sin', 'bez': 'en'}
CODES = ['title1', 'title2', 'quia', 'at', 'dnd', 'dod', 'dum', 'dnb', 'dnh', 'rat', 'rar', 'raq', 'coh', 'cot',
         'coq', 'cof', 'cef', 'cil', 'cnt', 'fab', 'dob', 'der', 'det', 'dar', 'das', 'daf', 'dor', 'don', 'dig',
         'dez', 'bet', 'bat', 'baq', 'bnq', 'bob', 'bog', 'fn', 'de', 'be', 'dati']


def units():
    u = {}
    for p, forms in LETTERS.items():
        for f in forms:
            u[f] = ('L', p)
    for k, v in SYLL.items():
        u[k] = ('S', v)
    return u


def segment(tok, U):
    """Greedy: nomenclator code only as a whole group or group prefix; syllable signs and letters anywhere."""
    out, i = [], 0
    for c in sorted(CODES, key=len, reverse=True):
        if tok.startswith(c) and (len(tok) == len(c) or c in ('das', 'daf', 'dati')):
            out.append(('C', c)); i = len(c); break
    keys = sorted(U, key=len, reverse=True)
    while i < len(tok):
        for k in keys:
            if tok.startswith(k, i):
                out.append(U[k]); i += len(k); break
        else:
            out.append(('U', tok[i])); i += 1
    return out


def read(path):
    rows = []
    for line in open(path, encoding='utf8'):
        if line.startswith('#') or not line.strip():
            continue
        loc, *toks = line.split()
        rows.append((loc, toks))
    return rows


def norm(w):
    return w.replace('j', 'i').replace('v', 'u').replace('y', 'i').replace('ç', 'c')


def letter_words(rows, U, mapping):
    words = []
    for _, toks in rows:
        for t in toks:
            seg = segment(t, U)
            if all(k == 'L' for k, _ in seg) and len(seg) >= 2:
                words.append(''.join(mapping[v] for _, v in seg))
    return words


def main():
    path = sys.argv[1]
    lexp = sys.argv[sys.argv.index('--lexicon') + 1] if '--lexicon' in sys.argv else None
    U = units(); rows = read(path)
    ident = {p: p for p in LETTERS}
    ntok = sum(len(t) for _, t in rows)
    for loc, toks in rows:
        dec = []
        for t in toks:
            s = ''
            for k, v in segment(t, U):
                s += v if k == 'L' else ('·' + v + '·' if k == 'S' else ('[' + v + ']' if k == 'C' else '?'))
            dec.append(s)
        print(loc, ' '.join(dec))
    print('groups', ntok)
    if '--measure' in sys.argv:
        lex = set(norm(w) for w in json.load(gzip.open(lexp)))
        def score(mp):
            ws = [norm(w) for w in letter_words(rows, U, mp)]
            return sum(w in lex for w in ws) / len(ws), len(ws)
        real, n = score(ident)
        rnd = random.Random(20261114); plains = list(LETTERS); ctl = []
        for _ in range(200):
            sh = plains[:]; rnd.shuffle(sh)
            ctl.append(score(dict(zip(plains, sh)))[0])
        best = max(ctl)
        print(f'letter-only words scored: {n}')
        print(f'real {real:.3f}; controls n=200 mean {sum(ctl)/200:.3f} max {best:.3f}')
        ok = real >= 0.50 and real >= best + 0.30
        print('VERDICT', 'PASS' if ok else 'FAIL', '(real >= 0.50 and >= best control + 0.30)')


if __name__ == '__main__':
    main()
