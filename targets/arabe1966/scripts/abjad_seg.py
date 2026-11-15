"""H2: each digit is a letter's abjad value with its zeros (dots) lost: 1=ا ي ق غ, 2=ب ك ر, ... Segment the digit
string into Arabic words (wordfreq list), both directions. Prints the best segmentations."""
import math, re, sys, heapq
from wordfreq import top_n_list, word_frequency
AB = dict(zip("ابجدهوزحطيكلمنسعفصقرشتثخذضظغ",
              [1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800,900,1000]))
def norm(w):
    w = re.sub('[ً-ْـ]', '', w)
    for a,b in (('أ','ا'),('إ','ا'),('آ','ا'),('ى','ي'),('ة','ه'),('ؤ','و'),('ئ','ي'),('ء','')): w = w.replace(a,b)
    return w
def red(w): return ''.join(str(AB[c])[0] for c in w)
N = int(sys.argv[2]) if len(sys.argv) > 2 else 60000
code = {}
for w in top_n_list('ar', N):
    n = norm(w)
    if not n or any(c not in AB for c in n): continue
    f = word_frequency(w, 'ar')
    if len(n) == 1 and n not in 'وبلفك': continue
    code.setdefault(red(n), []).append((f, n))
for k in code: code[k] = sorted(set(code[k]), reverse=True)[:6]
def best(s, K=12):
    beams = {0: [(0.0, [])]}
    for i in range(len(s)):
        for sc, ws in beams.get(i, []):
            for L in range(1, 9):
                t = s[i:i+L]
                if len(t) < L or t not in code: continue
                f, w = code[t][0]
                pen = math.log10(f) - 1.0 + 0.9*L          # favour long words
                beams.setdefault(i+L, []).append((sc+pen, ws+[t]))
        for j in beams: beams[j] = heapq.nlargest(K, beams[j], key=lambda x: x[0])
    return beams.get(len(s), [])
LTR = sys.argv[1] if len(sys.argv) > 1 else "71589217218921518421924"
for name, s in (("read right to left", LTR[::-1]), ("read left to right", LTR)):
    print("==", name, s)
    for sc, ws in best(s)[:8]:
        print("  %.1f" % sc, ' | '.join('/'.join(w for f, w in code[t][:4]) for t in ws))
