"""H4: numbers 1..28 = position of the letter in an alphabet order (abjad, Maghribi abjad, hija'i, Maghribi hija'i),
forward or counted from the end. All ways of cutting the digit string into numbers 1..28, both digit directions and
both letter orders; each candidate letter string is scored by its best segmentation into Arabic words."""
import math, re, sys
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
        if b[i] < -1e8: continue
        b[i+1] = max(b[i+1], b[i] - 4.0)                      # unexplained letter
        for L in range(2, 9):
            if i+L > len(t): break
            f = W.get(t[i:i+L])
            if f: b[i+L] = max(b[i+L], b[i] + math.log10(f) + 0.9*L - 1.5)
    return b[-1]
ORD = {'abjad': "ابجدهوزحطيكلمنسعفصقرشتثخذضظغ", 'abjad-maghribi': "ابجدهوزحطيكلمنصعفضقرستثخذظغش",
       'hijai': "ابتثجحخدذرزسشصضطظعغفقكلمنهوي", 'hijai-maghribi': "ابتثجحخدذرزطظكلمنصضعغفقسشهوي"}
LTR = "71589217218921518421924"
def cuts(s, i=0):
    if i == len(s): yield []; return
    yield from ([int(s[i])] + r for r in cuts(s, i+1))
    if i+1 < len(s) and 10 <= int(s[i:i+2]) <= 28: yield from ([int(s[i:i+2])] + r for r in cuts(s, i+2))
res = []
for dname, s in (('digits as written', LTR), ('digits reversed', LTR[::-1])):
    for c in cuts(s):
        for oname, o in ORD.items():
            for back in (0, 1):
                t = ''.join(o[28-n] if back else o[n-1] for n in c)
                for rev in (0, 1):
                    tt = t[::-1] if rev else t
                    res.append((wscore(tt), tt, dname, oname, 'from end' if back else 'from start', 'letters reversed' if rev else ''))
res.sort(reverse=True)
print(len(res), "candidates")
for r in res[:25]: print("%.1f" % r[0], *r[1:])
