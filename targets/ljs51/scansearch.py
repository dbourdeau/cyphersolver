"""Metre-constrained search for LJS 51 f. 106v: readings of one tawil hemistich that scan.

Word forms and their syllable weights come from the fully vowelled tokens of the classical poetry corpus
(lang/corpora/ar-classical-poetry.txt): each unvowelled form (28-letter alphabet) gets the weight patterns
(u short, - long) its vowelled occurrences show, with counts. A hemistich is a list of word slots, each a list of
sign labels; known signs are fixed, unknown signs are assigned consistently. A reading is kept only when the weights
of its words, concatenated, fit the tawil hemistich u - x | u - x - | u - x | u - x - (positions 1, 4, 8 and 11 short;
2, 5, 7, 9, 12 and 14 long; the last syllable free).

    python targets/ljs51/scansearch.py --half "N H~ H~ E 8 O | T Y K H M | ..." --fix N=و Y=م ... [--top 20]

A sign written X~ may be read as alif or lam (the alif sign that also stands for lam). Word dividers are '|'.
"""
import argparse, collections, math, os, re, sys, pickle

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, ROOT)
from lang import lm

SHORT = {'َ': 'a', 'ُ': 'u', 'ِ': 'i'}          # fatha damma kasra
TANWIN = {'ً', 'ٌ', 'ٍ'}
SUKUN, SHADDA = 'ْ', 'ّ'
LONG = {'ا', 'و', 'ي', 'ى', 'آ'}
TEMPLATE = 'u-xu-x-u-xu-x-'
CACHE = os.path.join(ROOT, 'lang', 'cache', 'ar-weights.pkl')


def weights(tok):
    """Syllable weights of a fully vowelled token, or None when it is not fully vowelled."""
    chars = [c for c in tok if c != 'ـ']
    units = []                                   # (consonant, marks)
    for c in chars:
        if 'ً' <= c <= 'ْ':
            if not units: return None
            units[-1][1].append(c)
        else:
            units.append((c, []))
    syl = []                                     # list of 'u' / '-'
    i = 0
    while i < len(units):
        c, m = units[i]
        if c in ('ا', 'ٱ') and i == 0 and not m:  # wasla alif: silent
            i += 1; continue
        if c == 'ل' and i == 1 and units[0][0] in ('ا', 'ٱ') and not units[0][1] and SUKUN in m:
            # article: its lam closes the preceding word's last syllable; treat as no syllable here
            i += 1; continue
        v = next((x for x in m if x in SHORT), None)
        tn = any(x in TANWIN for x in m)
        if SHADDA in m and syl:
            syl[-1] = '-'                        # doubled consonant closes the previous syllable
        if tn:
            syl.append('-'); i += 1; continue
        if v is None:
            if SUKUN in m or (c in LONG and not m):
                if syl: syl[-1] = '-'
                i += 1; continue
            return None                          # consonant without a mark: not fully vowelled
        nxt = units[i + 1] if i + 1 < len(units) else None
        if nxt and nxt[0] in LONG and not any(x in SHORT for x in nxt[1]) and SHADDA not in nxt[1]:
            syl.append('-'); i += 2; continue
        syl.append('u'); i += 1
    return ''.join(syl) if syl else None


def build():
    if os.path.exists(CACHE):
        return pickle.load(open(CACHE, 'rb'))
    W = collections.defaultdict(collections.Counter)
    F = collections.Counter()
    for line in open(os.path.join(ROOT, 'lang', 'corpora', 'ar-classical-poetry.txt'), encoding='utf-8'):
        for tok in line.split():
            key = lm.norm(tok, 'arabic28').replace(' ', '')
            if not key: continue
            F[key] += 1
            w = weights(tok)
            if w: W[key][w] += 1
    data = ({k: dict(v) for k, v in W.items()}, dict(F))
    os.makedirs(os.path.dirname(CACHE), exist_ok=True)
    pickle.dump(data, open(CACHE, 'wb'))
    return data


def fits(seq):
    if len(seq) != len(TEMPLATE): return False
    for i, (s, t) in enumerate(zip(seq, TEMPLATE)):
        if i == len(TEMPLATE) - 1: continue
        if t != 'x' and s != t: return False
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--half', required=True)
    ap.add_argument('--fix', nargs='*', default=[])
    ap.add_argument('--top', type=int, default=25)
    ap.add_argument('--maxcand', type=int, default=3000)
    a = ap.parse_args()
    W, F = build()
    tot = sum(F.values())
    fixed = dict(f.split('=') for f in a.fix)
    slots = [w.split() for w in a.half.split('|') if w.strip()]
    letters = lm.AR_LETTERS
    # prefixed forms: weights of the base word with the prefix's syllables in front (approximate)
    PREF = [('ولل', 'u-'), ('فلل', 'u-'), ('وال', '-'), ('فال', '-'), ('بال', 'u-'), ('كال', 'u-'), ('لل', '-'),
            ('ال', '-'), ('و', 'u'), ('ف', 'u'), ('ب', 'u'), ('ل', 'u'), ('ك', 'u')]
    W2 = dict(W)
    for base, pats in W.items():
        if F.get(base, 0) < 3: continue
        for pre, pw in PREF:
            k = pre + base
            if k in W2: continue
            nb = base[2:] if pre.endswith('ال') and base.startswith('ال') else base
            W2[k] = {pw + q: c for q, c in pats.items()}
            F.setdefault(k, 1)
    W = W2
    bylen = collections.defaultdict(list)
    for k in W:
        bylen[len(k)].append(k)
    cands = []
    for w in slots:
        lst = []
        for k in bylen[len(w)]:
            ok, mp = True, {}
            for s, ch in zip(w, k):
                if s.endswith('~'):
                    if ch not in 'ال' and not (ch == 'ي' and s is w[-1]): ok = False; break
                    continue
                if s in fixed:
                    if fixed[s] != ch: ok = False; break
                elif mp.setdefault(s, ch) != ch:
                    ok = False; break
            if ok:
                lst.append((k, mp, math.log(F[k] / tot), W[k]))
        lst.sort(key=lambda x: -x[2])
        cands.append(lst[:a.maxcand])
        print(f'slot {" ".join(w)}: {len(lst)} candidates', file=sys.stderr)
    out = []

    def rec(i, mp, words, pats, score):
        if i == len(slots):
            for p in pats:
                if fits(p):
                    out.append((score, words, p, dict(mp))); break
            return
        for k, wmp, lp, wp in cands[i]:
            new, ok = dict(mp), True
            for s, ch in wmp.items():
                if new.setdefault(s, ch) != ch: ok = False; break
            if not ok: continue
            # injectivity among unknown signs is not enforced (homophones allowed)
            npats = []
            for p in pats:
                for q in wp:
                    r = p + q
                    if len(r) <= len(TEMPLATE) and all(t == 'x' or s == t for s, t in zip(r[:len(TEMPLATE) - 1], TEMPLATE)):
                        npats.append(r)
            if not npats: continue
            rec(i + 1, new, words + [k], list(set(npats))[:200], score + lp)

    rec(0, {}, [], [''], 0.0)
    out.sort(key=lambda x: -x[0])
    seen = set()
    for sc, words, p, mp in out:
        t = ' '.join(words)
        if t in seen: continue
        seen.add(t)
        print(f'{sc:8.1f}  {t}   [{p}]   ' + ' '.join(f'{k}={v}' for k, v in sorted(mp.items())))
        if len(seen) >= a.top: break
    print(f'{len(out)} scanning readings', file=sys.stderr)


if __name__ == '__main__':
    main()
