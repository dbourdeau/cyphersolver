"""Compare the blind helper's transcription with the frozen one and with v2, word by word, line by line.
W and w are merged (one cipher letter); bracketed letters above the line are dropped from the blind file. Letter
agreement is counted only over word pairs of equal length."""
import re, os, sys
H = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')   # targets/vind1647
def load(p):
    L = {}
    for line in open(p, encoding='utf-8'):
        if line.startswith('#') or not line.strip(): continue
        body = line.split('#')[0]
        if not re.match(r'\s*\d\d ', body): continue
        n, rest = body.split(None, 1)
        rest = re.sub(r'\[[a-z]\]', '', rest).replace('=', '').replace('W', 'w')
        L[int(n)] = rest.split()
    return L
b = load(os.path.join(H, 'review', 'blind_transcription.txt'))
for name in ('transcription_frozen.txt', 'transcription.txt'):
    a = load(os.path.join(H, name))
    same = tot = wl = 0; diffs = []
    for n in sorted(a):
        if len(a[n]) != len(b.get(n, [])): diffs.append('line %02d word count %d vs %d' % (n, len(a[n]), len(b.get(n, []))))
        for x, y in zip(a[n], b.get(n, [])):
            if len(x) != len(y): wl += 1; diffs.append('%02d %s / %s (length)' % (n, x, y)); continue
            for c1, c2 in zip(x, y):
                tot += 1; same += c1 == c2
            if x != y: diffs.append('%02d %s / %s' % (n, x, y))
    print('%s vs blind: %d of %d letters agree (equal-length words); %d words differ in length' % (name, same, tot, wl))
    for d in diffs: print('   ', d)
