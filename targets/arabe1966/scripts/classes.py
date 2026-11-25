"""H10: digit = digital root of the letter's position in an alphabet order (hija'i, Maghribi hija'i, Maghribi abjad),
so each digit stands for three or four letters. Word segmentation, both directions, two vocabularies."""
import math, re, sys, heapq, collections
from wordfreq import top_n_list, word_frequency
def norm(w):
    w = re.sub('[ً-ْـٰ]', '', w)
    for a,b in (('أ','ا'),('إ','ا'),('آ','ا'),('ٱ','ا'),('ى','ي'),('ة','ه'),('ؤ','و'),('ئ','ي'),('ء','')): w = w.replace(a,b)
    return w
ORD = {'hijai': "ابتثجحخدذرزسشصضطظعغفقكلمنهوي", 'hijai-maghribi': "ابتثجحخدذرزطظكلمنصضعغفقسشهوي",
       'abjad-maghribi': "ابجدهوزحطيكلمنصعفضقرستثخذظغش", 'hijai-hw': "ابتثجحخدذرزسشصضطظعغفقكلمنوهي"}
AR = set(ORD['hijai'])
voc = {}
for w in top_n_list('ar', 60000):
    n = norm(w)
    if n and not set(n) - AR and (len(n) > 1 or n == 'و'): voc[n] = max(voc.get(n, -9), math.log10(word_frequency(w, 'ar')))
if len(sys.argv) > 1:
    raw = open(sys.argv[1], encoding='utf-8').read()
    cnt = collections.Counter(w for w in (norm(x) for x in re.findall('[ء-ْٰٱ]+', raw)) if w and not set(w) - AR)
    tot = sum(cnt.values())
    for w, c in cnt.items():
        if c >= 3 and (len(w) > 1 or w == 'و'): voc[w] = max(voc.get(w, -9), math.log10(c / tot))
LTR = "71589217218921518421924"
for oname, o in ORD.items():
    root = {c: str((i % 9) + 1) for i, c in enumerate(o)}
    code = collections.defaultdict(list)
    for w, lf in voc.items(): code[''.join(root[c] for c in w)].append((lf, w))
    for k in code: code[k].sort(reverse=True)
    for dname, s in (('rtl', LTR[::-1]), ('ltr', LTR)):
        beams = {0: [(0.0, [])]}
        for i in range(len(s)):
            for sc, ws in beams.get(i, []):
                for L in range(1, 9):
                    t = s[i:i+L]
                    if len(t) == L and t in code:
                        beams.setdefault(i+L, []).append((sc + code[t][0][0] + 0.9*L - 1.0, ws + [t]))
            for j in beams: beams[j] = heapq.nlargest(10, beams[j], key=lambda x: x[0])
        print("==", oname, dname)
        for sc, ws in beams.get(len(s), [])[:4]:
            print("  %.1f" % sc, ' | '.join('/'.join(w for f, w in code[t][:4]) for t in ws))
