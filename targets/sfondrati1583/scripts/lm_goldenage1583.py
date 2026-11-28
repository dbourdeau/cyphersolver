#!/usr/bin/env python3
"""Leak-free 1580s Golden-Age Spanish diplomatic LM, lexicon, and Viterbi segmenter.

Strictly uses cyphersolver_repo's built-in `es-golden-age` and `es-golden-age-nospace`
(Cervantes Quijote 1605-1615 + Villa's 1500-1530 Memorias) plus `es.json.gz` and general
late-16th-century Spanish diplomatic forms. Zero leakage from `sfondrati1583` (#2077)
or held-out synthetic targets (`mendoza1589`, `philip1574`, `sessa1593`, `ibarra1593`).
"""
import collections
import gzip
import json
import math
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent


def _find_repo() -> pathlib.Path:
    for cand in list(HERE.parents) + [pathlib.Path.cwd()] + [p / 'cyphersolver_repo' for p in HERE.parents]:
        if (cand / 'lang' / 'lm.py').is_file() and (cand / 'lang' / 'lexicons' / 'es.json.gz').is_file():
            return cand
    raise FileNotFoundError('Cannot locate cyphersolver repo root containing lang/lm.py')


REPO = _find_repo()
sys.path.insert(0, str(REPO))
from lang import lm as clm

DIPL_1580S_EXTRA = (
    'magestad', 'majestad', 'alteza', 'senoria', 'excellencia', 'santidad',
    'vuestra', 'uuestra', 'nuestro', 'nuestra', 'nuestros', 'nuestras',
    'rey', 'reyna', 'principe', 'infanta', 'duque', 'duquesa', 'marques', 'conde',
    'cardenal', 'papa', 'pontifice', 'obispo', 'nuncio', 'embaxador', 'embaxadores',
    'espana', 'francia', 'italia', 'piamonte', 'sauoya', 'saboya', 'milan', 'turin',
    'madrid', 'roma', 'flandes', 'portugal', 'napoles', 'sicilia', 'genoua', 'uenecia',
    'ginebra', 'saluzzo', 'esguizaros', 'suizos', 'ingleses', 'inglaterra', 'alemanha',
    'despacho', 'despachos', 'ordinario', 'estraordinario', 'correo', 'correos',
    'cartas', 'carta', 'auiso', 'auisos', 'auisar', 'auisado', 'auer', 'hauer', 'hauia',
    'hauiendo', 'hauerse', 'hazer', 'fazer', 'fecho', 'hecho', 'hechos', 'dicho', 'dicha',
    'dichos', 'dichas', 'escriuir', 'screuir', 'escrito', 'scripto', 'cifra', 'descifrar',
    'negocio', 'negocios', 'negociacion', 'trato', 'tratos', 'platica', 'concierto',
    'exercito', 'infanteria', 'caualleria', 'gente', 'gentes', 'soldados', 'capitan',
    'dineros', 'dinero', 'escudos', 'ducados', 'paga', 'pagas', 'socorro', 'socorrer',
    'enfermedad', 'mejoria', 'salud', 'conualecencia', 'peligro', 'remedio', 'casamiento',
    'matrimonio', 'alianza', 'liga', 'guerra', 'paz', 'tregua', 'suspension', 'armas',
    'seruicio', 'estado', 'reynos', 'republica', 'suplico', 'beso', 'manos', 'servidor',
    'assy', 'ansi', 'mesmo', 'mesma', 'agora', 'luego', 'despues', 'todauia', 'demas',
    'demanera', 'paresce', 'parece', 'parescido', 'parecido', 'requiere', 'conuiene',
)


def load_spanish_lms():
    return clm.load('es-golden-age-nospace'), clm.load('es-golden-age')


class GoldenAge1583Lexicon:
    def __init__(self):
        self.freq = collections.Counter()
        es_raw = json.loads(gzip.open(REPO / 'lang/lexicons/es.json.gz', 'rt', encoding='utf-8').read())
        for w, c in es_raw.items():
            nw = clm.norm(w, scheme='early', spaces=False)
            if nw:
                self.freq[nw] += c
        for w in DIPL_1580S_EXTRA:
            nw = clm.norm(w, scheme='early', spaces=False)
            if nw:
                self.freq[nw] += 200
        for fw in ('a', 'e', 'y', 'o', 'u', 'de', 'el', 'la', 'lo', 'en', 'es', 'al', 'del',
                   'su', 'si', 'se', 'no', 'ni', 'me', 'te', 'le', 'os', 'un', 'mi', 'tu',
                   'que', 'por', 'con', 'los', 'las', 'mas', 'muy', 'ya', 'ha', 'he', 'vn'):
            nw = clm.norm(fw, scheme='early', spaces=False)
            self.freq[nw] = max(self.freq[nw], 5000)

        self.total = sum(self.freq.values())
        self.words = {w for w, c in self.freq.items() if c >= 3}
        self.max_len = max((len(w) for w in self.words), default=16)
        self.logp = {w: math.log(c / self.total) for w, c in self.freq.items() if c >= 3}
        self.one_char = {'a', 'e', 'y', 'o', 'u'}

    def viterbi_segment(self, s):
        n = len(s)
        if n == 0:
            return []
        dp = [-1e18] * (n + 1)
        back = [0] * (n + 1)
        dp[0] = 0.0
        unk_pen = math.log(1e-8)
        for i in range(n):
            if dp[i] <= -1e17:
                continue
            lim = min(n, i + self.max_len)
            for j in range(i + 1, lim + 1):
                sub = s[i:j]
                L = j - i
                if L == 1:
                    if sub in self.one_char:
                        cand = dp[i] + self.logp.get(sub, -6.0) - 0.5
                    else:
                        cand = dp[i] + unk_pen - 4.0
                elif sub in self.logp:
                    cand = dp[i] + self.logp[sub] + 0.55 * L
                else:
                    if L <= 8:
                        cand = dp[i] + unk_pen - 2.2 * L
                    else:
                        continue
                if cand > dp[j]:
                    dp[j] = cand
                    back[j] = i
        words = []
        idx = n
        while idx > 0:
            prev = back[idx]
            words.append(s[prev:idx])
            idx = prev
        words.reverse()
        return words

    def evaluate_words(self, word_list):
        n_w = len(word_list)
        if n_w == 0:
            return 0.0, 0.0, 0.0, 0.0, []
        hits = []
        tot_ch = c4 = c5 = l3 = h3 = 0
        for w in word_list:
            nw = clm.norm(w, scheme='early', spaces=False)
            ok = nw in self.words
            hits.append(ok)
            L = len(nw)
            tot_ch += L
            if L >= 3:
                l3 += 1
                if ok:
                    h3 += 1
            if ok and L >= 4:
                c4 += L
            if ok and L >= 5:
                c5 += L
        return sum(hits) / n_w, h3 / max(1, l3), c4 / max(1, tot_ch), c5 / max(1, tot_ch), hits


if __name__ == '__main__':
    lm_ns, _ = load_spanish_lms()
    lex = GoldenAge1583Lexicon()
    sample = "haviendo ydo perseverando la mejoria del senor duque de saboya en turin como vuestra senoria me ha scripto"
    ns = clm.norm(sample, scheme='early', spaces=False)
    seg = lex.viterbi_segment(ns)
    wh, h3, c4, c5, _ = lex.evaluate_words(seg)
    print(f"Lexicon size={len(lex.words)} | nospace LM/ch={lm_ns.per_char(ns):.4f} | "
          f"seg={len(seg)} | word_hit={wh:.3f} | len3_hit={h3:.3f} | cov4={c4:.3f} | cov5={c5:.3f}")
    print("Segmented:", ' '.join(seg))
