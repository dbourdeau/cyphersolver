"""Normalisation arabe et alphabet (28 lettres + espace = 29 symboles, 0 = espace)."""
import re
DIAC = re.compile('[ؐ-ًؚ-ٰٟۖ-ۭـ]')
LETTERS = 'ابتثجحخدذرزسشصضطظعغفقكلمنهوي'
IDX = {c: i + 1 for i, c in enumerate(LETTERS)}
def norm(w):
    w = DIAC.sub('', w)
    for a, b in (('أ','ا'),('إ','ا'),('آ','ا'),('ٱ','ا'),('ى','ي'),('ة','ه'),('ؤ','و'),('ئ','ي'),('ء',''),('ک','ك'),('ی','ي')):
        w = w.replace(a, b)
    return ''.join(c for c in w if c in IDX)
def words(text):
    out = []
    for tok in re.split(r'[^؀-ۿ]+', text):
        n = norm(tok)
        if n: out.append(n)
    return out
CORPUS = "/Volumes/SPOF_2/Archives-Veille-cyber/dechiffrements-europe/ljs51/corpus/"
TRAIN = ["0749IbnFadlAllahCumari.TacrifBiMustalahSharif.Shamela0037051-ara1.mARkdown",
         "0750SafiDinHilli.Diwan.JK007639-ara1",
         "0764Safadi.AlhanSawajic.AOCP20240423140Vols-ara1",
         "0764Safadi.KashfHal.Shamela0005393-ara1"]
CALIB = "0768IbnNubataShacir.Diwan.JK007636-ara1"
def strip_meta(text):
    return '\n'.join(l for l in text.split('\n') if not l.startswith('#META#'))
