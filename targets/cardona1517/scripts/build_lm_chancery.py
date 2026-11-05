"""Build the chancery-leaning Spanish model used for the code groups (es.lm, the 22-letter 1-5-gram tables read by
wsa5) and the whole-word option list (wide_words.txt), in the current folder.

Corpus: La Celestina (Gutenberg 1619, corp/g1619.txt) x2, Villa's Memorias (lang/corpora/es-vasto-memorias.txt,
numeral-only words removed), and the vich1511 clear letters n12/n39/n41 (targets/vich1511/*_clear.txt) x10.
No Quijote: a model built partly on it filled rare code groups with its names (don quijote, Dulcinea ...).
Option list: the corpus's 600 commonest words, the chancery list of vich1515's make_wide.py, drv.EXTRA and a few
context words; one-letter words only y a e o; Celestina speaker labels removed.

Usage (from a work folder holding drv.py and corp/g1619.txt): python3 build_lm_chancery.py REPO_ROOT
"""
import re, sys, collections, struct, math, unicodedata, os
ROOT = sys.argv[1]
A = 'abcdefghilmnopqrstuxyz'; K = len(A); IX = {c: i for i, c in enumerate(A)}

def words(t):
    t = t.lower().replace('ñ', 'n').replace('ç', 'z'); t = unicodedata.normalize('NFD', t)
    t = ''.join(c for c in t if unicodedata.category(c) != 'Mn')
    return re.findall(r'[a-z]+', t.translate(str.maketrans('jvkw', 'iucu')))

def body(p):
    t = open(p, encoding='utf-8', errors='ignore').read(); a = t.find('*** START'); b = t.find('*** END')
    return t[t.find('\n', a):b] if a >= 0 else t

cel = words(body('corp/g1619.txt'))
villa = [w for w in words(open(os.path.join(ROOT, 'lang/corpora/es-vasto-memorias.txt'), errors='ignore').read())
         if not re.fullmatch(r'[iuxlcdm]+', w) or w in ('de', 'mi', 'me', 'mil', 'di', 'dl')]
vich = []
for n in ('n12', 'n39', 'n41'):
    raw = open(os.path.join(ROOT, f'targets/vich1511/{n}_clear.txt'), encoding='utf-8').read()
    vich += words('\n'.join(l.split(':', 1)[1] if re.match(r'^C\d+:', l) else l
                            for l in raw.splitlines() if not l.startswith('#')))
W = cel * 2 + villa + vich * 10
x = [IX[c] for c in ''.join(W) if c in IX]; n = len(x)
cnt = [collections.Counter() for _ in range(6)]
for o in range(1, 6): cnt[o] = collections.Counter(tuple(x[i:i + o]) for i in range(n - o + 1))
out = open('es.lm', 'wb'); prev = None
for o in range(1, 6):
    tab = [0.0] * (K ** o)
    for idx in range(K ** o):
        t = []; v = idx
        for _ in range(o): t.append(v % K); v //= K
        t = tuple(reversed(t)); c = cnt[o][t]
        p = (c + 1) / (n + K) if o == 1 else (c + 3 * math.exp(prev[idx % (K ** (o - 1))])) / (cnt[o - 1][t[:-1]] + 3)
        tab[idx] = math.log(p)
    out.write(struct.pack(f'{K ** o}f', *tab)); prev = tab
out.close()
wc = collections.Counter(w for w in W if all(c in IX for c in w)); tot = sum(wc.values())
with open('words.txt', 'w') as f:
    for w, c in wc.most_common(600): f.write(f'{w} {math.log(c / tot):.4f}\n')
CH = '''su santidad papa rey francia frances franceses emperador uenecianos uenecia napoles roma cardenal cardenales embaxador
dineros gente gentes armada tregua liga concierto capitulos capitulacion capitulado scriuir escreuir scriuo escriuo
carta cartas letras milan suyzos suizos esguizaros florencia mantua ferrara genoua ytalia lombardia exercito campo
cauallos infanteria artilleria dinero ducados nuestro nuestra nuestros nuestras uos uuestro uuestra sabiduria
paz guerra principe principes reyno reynos estado estados negocio negocios fecho fazer hazer dezir dicho dicha
tierra tierras lugar lugares tiempo assi porende otrosi mismo misma'''.split()
CTX = '''alteza magestad santidad ynfanteria infanteria dineros dinero lanzas gente armas capitan uisorrey napoles roma papa
reyno pagar paga pagada sustener sostener entretener embaxador conde marques cardenal cardenales sena florencia urrea
imposibilidad imposible proceder pronunciar mandar mande manda suplico merced seruicio seruir carta cartas'''.split()
sys.path.insert(0, '.'); from drv import EXTRA
SPEAKERS = {'cel', 'semp', 'parm', 'cal', 'mel', 'luc', 'elic', 'areu', 'sos', 'trist', 'cent', 'alis', 'pleb', 'melib',
            'celestina', 'sempronio', 'parmeno', 'calisto', 'melibea', 'lucrecia', 'elicia', 'areusa', 'sosia',
            'centurio', 'pleberio', 'alisa', 'tristan'}
opts = []
for w in [w for w, _ in wc.most_common(600)] + [x.translate(str.maketrans('jvkwç', 'iucuz')) for x in CH + EXTRA + CTX]:
    if w not in opts and w not in SPEAKERS and all(c in IX for c in w) and (len(w) > 1 or w in ('y', 'a', 'e', 'o')):
        opts.append(w)
open('wide_words.txt', 'w').write('\n'.join(opts) + '\n')
print('letters', n, 'options', len(opts))
