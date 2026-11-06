"""Build the Spanish model for the Soria -> Lannoy letter (es.lm, the 22-letter 1-5-gram tables read by wsa5) and the
whole-word option list for the code groups (words.txt, wide_words.txt), in this folder.

Corpus (all 1520s chancery Spanish):
- A. Rodriguez Villa, Memorias para la historia del asalto y saqueo de Roma (1875), lang/corpora/es-vasto-memorias.txt:
  the 1526-27 letters of Soria, Perez, Najera, Sanchez, Lannoy (Google boilerplate and numeral-only words dropped);
- Danvila, Memorial historico espanol 37 (Comunidades letters of 1520-21), targets/adrian1521/danvila/mhe37.txt;
- Soria's own deciphered letters of 1523 and 1527 (targets/soria1523/R94*_reading.md, targets/soria1527/*) x10;
- the clear passages of this letter (../transcription/clear.txt, if present) x10.
Same smoothing as targets/cardona1517/scripts/build_lm_chancery.py.

Usage: python build_lm.py   (from this folder)
"""
import re, collections, struct, math, unicodedata, os, glob
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
A = 'abcdefghilmnopqrstuxyz'; K = len(A); IX = {c: i for i, c in enumerate(A)}


def words(t):
    t = t.lower().replace('ñ', 'n').replace('ç', 'z'); t = unicodedata.normalize('NFD', t)
    t = ''.join(c for c in t if unicodedata.category(c) != 'Mn')
    return re.findall(r'[a-z]+', t.translate(str.maketrans('jvkw', 'iucu')))


def read(p):
    return open(p, encoding='utf-8', errors='ignore').read()


villa = read(os.path.join(ROOT, 'lang/corpora/es-vasto-memorias.txt'))
villa = villa[villa.find('INTRODUCCI') if 'INTRODUCCI' in villa else 3000:]
villa = [w for w in words(villa) if not re.fullmatch(r'[iuxlcdm]+', w) or w in ('de', 'mi', 'me', 'mil', 'di', 'dl')]
danvila = words(read(os.path.join(ROOT, 'targets/adrian1521/danvila/mhe37.txt')))
soria = []
for p in sorted(glob.glob(os.path.join(ROOT, 'targets/soria1523/R94*_reading.md'))) + \
        [os.path.join(ROOT, 'targets/soria1527/R9487_reading.md'), os.path.join(ROOT, 'targets/soria1527/claro.md')]:
    t = re.sub(r'<!--.*?-->', ' ', read(p), flags=re.S); t = re.sub(r'\[[^\]]*\]', ' ', t)
    soria += words(t)
clear = words(read(os.path.join(HERE, '..', 'transcription', 'clear.txt'))) if os.path.exists(
    os.path.join(HERE, '..', 'transcription', 'clear.txt')) else []
W = villa + danvila + soria * 10 + clear * 10
x = [IX[c] for c in ''.join(W) if c in IX]; n = len(x)
cnt = [collections.Counter() for _ in range(6)]
for o in range(1, 6):
    cnt[o] = collections.Counter(tuple(x[i:i + o]) for i in range(n - o + 1))
out = open(os.path.join(HERE, 'es.lm'), 'wb'); prev = None
for o in range(1, 6):
    tab = [0.0] * (K ** o)
    for idx in range(K ** o):
        t = []; v = idx
        for _ in range(o):
            t.append(v % K); v //= K
        t = tuple(reversed(t)); c = cnt[o][t]
        p = (c + 1) / (n + K) if o == 1 else (c + 3 * math.exp(prev[idx % (K ** (o - 1))])) / (cnt[o - 1][t[:-1]] + 3)
        tab[idx] = math.log(p)
    out.write(struct.pack(f'{K ** o}f', *tab)); prev = tab
out.close()
wc = collections.Counter(w for w in W if all(c in IX for c in w)); tot = sum(wc.values())
with open(os.path.join(HERE, 'words.txt'), 'w') as f:
    for w, c in wc.most_common(600):
        f.write(f'{w} {math.log(c / tot):.4f}\n')
CTX = '''su magestad uuestra magestad excelencia senoria papa rey francia frances franceses francesa emperador uenecianos uenecia
napoles roma genoua saona milan florencia ferrara lombardia italia espana inglaterra corcega sicilia piamonte ast pauia
duque comunidad armada galeras galera naues carraca bergantin uisorrey principe marques conde capitan borbon leyua
lodron bracamonte doria fregoso andrea antonio cesaro enemigos exercito campo gente infanteria alemanes espanoles
italianos suyzos lanzas cauallos artilleria poluora salitre dineros dinero ducados paga tregua liga paz guerra
concierto capitulos cartas carta letras auiso auisos nueuas correo tiempo dias hora agora luego despues antes
mucho muchos mucha mas menos muy bien mal assi tambien porque aunque sino pues mismo dicho dicha dichos hazer dezir
scriuir escreuir embiar uenir yr pasar partir armar tener poder querer saber esperar entender'''.split()
opts = []
for w in [w for w, _ in wc.most_common(600)] + [x.translate(str.maketrans('jvkwç', 'iucuz')) for x in CTX]:
    if w not in opts and all(c in IX for c in w) and (len(w) > 1 or w in ('y', 'a', 'e', 'o')):
        opts.append(w)
open(os.path.join(HERE, 'wide_words.txt'), 'w').write('\n'.join(opts) + '\n')
print('letters', n, 'villa', len(villa), 'danvila', len(danvila), 'soria', len(soria), 'clear', len(clear), 'options', len(opts))
