"""Mesure unique taulet-1866 (PROTOCOLE P01).
python3 -I measure.py transcription.txt KEY.tsv es.json.gz [--part T|H]
transcription.txt : lignes 'Sk<TAB>T|H<TAB>n.n.n...' (n? = douteux -> on prend n ; a|b -> a ; ? -> inconnu).
KEY.tsv : 'nombre<TAB>valeur' ; valeur = lettres, '_' = séparateur de mots, '-' = nulle.
"""
import sys, gzip, json, random, unicodedata

NOMS = ('jalset jalet tarragona reus cornudella poboleda porrera morera albarca ulldemolins prades alforja priorato montsant falset gratallops lloa vilella torroja siurana capsanes marsa bellmunt vinebre llaveria cabacers flix borjas taulet abella villarroya sagueta saguete montroig cambrils valls vilaseca'
        ' guardia civil soria zamora sublevados columna columnas').split()
SHORT = {'a', 'y', 'o', 'e'}


def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    return ''.join(c for c in s if 'a' <= c <= 'z')


def load_lex(p):
    d = json.load(gzip.open(p, 'rt', encoding='utf-8'))
    if isinstance(d, dict) and 'words' in d and isinstance(d['words'], (dict, list)):
        d = d['words']
    lex = set()
    if isinstance(d, dict):
        for w, c in d.items():
            try:
                ok = int(c) >= 2
            except Exception:
                ok = True
            w = norm(w)
            if ok and len(w) >= 2:
                lex.add(w)
    else:
        for w in d:
            w = norm(w if isinstance(w, str) else w[0])
            if len(w) >= 2:
                lex.add(w)
    return lex | SHORT | set(NOMS)


def load_trans(p, part):
    runs = []
    for line in open(p, encoding='utf-8'):
        line = line.rstrip('\n')
        if not line or line.startswith('#'):
            continue
        sid, pt, nums = line.split('\t')
        if pt != part:
            continue
        toks = []
        for t in nums.split('.'):
            t = t.strip().split('|')[0].rstrip('?')
            toks.append(t if t else '?')
        runs.append((sid, toks))
    return runs


def load_key(p):
    k = {}
    for line in open(p, encoding='utf-8'):
        line = line.rstrip('\n')
        if not line or line.startswith('#'):
            continue
        n, v = line.split('\t')[:2]
        k[n.strip()] = v.strip()
    return k


def decode(runs, key):
    out = []  # per run: list of words (letters, '?' kept)
    for sid, toks in runs:
        words, cur = [], ''
        for t in toks:
            v = key.get(t)
            if v is None:
                cur += '?'
            elif v == '_':
                if cur:
                    words.append(cur)
                cur = ''
            elif v == '-':
                pass
            else:
                cur += norm(v)
        if cur:
            words.append(cur)
        out.append(words)
    return out


def coverage(s, lex, maxw=20):
    n = len(s)
    best = [0] * (n + 1)
    for i in range(1, n + 1):
        best[i] = best[i - 1]
        for L in range(1, min(maxw, i) + 1):
            w = s[i - L:i]
            if '?' not in w and w in lex:
                best[i] = max(best[i], best[i - L] + L)
    return best[n]


def car(dec, lex):
    tot = cov = 0
    for words in dec:
        s = ''.join(words)
        tot += len(s)
        cov += coverage(s, lex)
    return cov / tot if tot else 0.0


def wordacc(dec, lex):
    ws = [w for words in dec for w in words]
    return sum(1 for w in ws if w in lex) / len(ws) if ws else 0.0


def main(a):
    part = 'H'
    if '--part' in a:
        part = a[a.index('--part') + 1]
    runs, key, lex = load_trans(a[0], part), load_key(a[1]), load_lex(a[2])
    nletters = sum(1 for _, t in runs for x in t if True)
    dec = decode(runs, key)
    c, w = car(dec, lex), wordacc(dec, lex)
    nums = [n for n, v in key.items() if v not in ('_', '-')]
    vals = [key[n] for n in nums]
    rng = random.Random(2444)
    wit = []
    for _ in range(200):
        p = vals[:]
        rng.shuffle(p)
        k2 = dict(key)
        k2.update(zip(nums, p))
        wit.append(car(decode(runs, k2), lex))
    mx = max(wit)
    print('part', part, 'nombres :', nletters)
    print('decode :', ' / '.join(' '.join(ws) for ws in dec))
    print(f'car = {c:.3f} ; mots = {w:.3f} ; meilleur temoin = {mx:.3f} ; marge = {c - mx:.3f}')
    ok = c >= 0.85 and c >= mx + 0.30 and nletters >= 30
    print('VERDICT :', 'VALIDEE' if ok else ('NON PROBANTE (H < 30)' if nletters < 30 else 'NON VALIDEE -> PARTIELLE au mieux'))


if __name__ == '__main__':
    main(sys.argv[1:])
