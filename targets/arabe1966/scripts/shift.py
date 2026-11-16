"""H5: numbers 1..28 are alphabet positions under a shift or affine map (n -> a*n+b mod 28), four alphabet orders,
both tokenisations (digits as written / reversed), both letter orders. Scored by word segmentation."""
import math, re
from wordfreq import top_n_list, word_frequency
def norm(w):
    w = re.sub('[ً-ْـ]', '', w)
    for a,b in (('أ','ا'),('إ','ا'),('آ','ا'),('ى','ي'),('ة','ه'),('ؤ','و'),('ئ','ي'),('ء','')): w = w.replace(a,b)
    return w
W = {}
for w in top_n_list('ar', 60000):
    n = norm(w)
    if n and (len(n) > 1 or n == 'و'): W[n] = max(W.get(n, 0), word_frequency(w, 'ar'))
def wscore(t):
    b = [0.0] + [-1e9]*len(t)
    for i in range(len(t)):
        b[i+1] = max(b[i+1], b[i] - 4.0)
        for L in range(2, min(8, len(t)-i)+1):
            f = W.get(t[i:i+L])
            if f: b[i+L] = max(b[i+L], b[i] + math.log10(f) + 0.9*L - 1.5)
    return b[-1]
ORD = {'abjad': "ابجدهوزحطيكلمنسعفصقرشتثخذضظغ", 'abjad-maghribi': "ابجدهوزحطيكلمنصعفضقرستثخذظغش",
       'hijai': "ابتثجحخدذرزسشصضطظعغفقكلمنهوي", 'hijai-maghribi': "ابتثجحخدذرزطظكلمنصضعغفقسشهوي"}
TOK = {'digits as written, numbers right to left': [24,9,21,4,18,5,21,9,8,21,7,21,9,8,15,7],
       'digits reversed': [4,2,9,12,4,8,15,12,9,8,12,7,12,9,8,5,17]}
res = []
for tn, toks in TOK.items():
    for on, o in ORD.items():
        for a in (1,3,5,9,11,13,15,17,19,23,25,27):
            for b in range(28):
                t = ''.join(o[(a*(n-1)+b) % 28] for n in toks)
                for rev in (0,1):
                    tt = t[::-1] if rev else t
                    res.append((wscore(tt), tt, tn, on, a, b, rev))
res.sort(reverse=True)
for r in res[:20]: print("%.1f" % r[0], *r[1:])
