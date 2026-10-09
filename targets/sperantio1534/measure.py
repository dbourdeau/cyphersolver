"""Measure the readings: share of words read from the cipher.
Lines '<n> text' in r9411/reading_r9411.txt and r9411/reading_r9412.txt (comments '#', '==' skipped).
Unread: [..], any token containing [ (a supply, whole or partial), <conjecture> tokens are skipped
entirely only when they stand alongside a cipher reading of the same place (they are commentary), clear
text (CAPS, '(…)') is left out: only cipher words are counted.
"""
import re, sys
def measure(fn):
    tot = rd = 0
    for ln in open(fn, encoding='utf-8'):
        if ln.startswith('#') or ln.startswith('==') or not ln.strip(): continue
        m = re.match(r'\s*\d+\s+(.*)', ln.rstrip('\n'))
        if not m: continue
        t = re.sub(r'<[^>]*>', ' ', m.group(1))
        t = re.sub(r'\[signature, unread\]', '[..]', t)
        t = re.sub(r'\([^)]*\)', ' ', t)
        t = re.sub(r'[A-Z][A-Z]+', ' ', t)
        for w in re.findall(r'\[[^\]]*\](?:\w*)|\S+', t):
            w = w.strip('.,;:')
            if not w or w in ('-',): continue
            if re.fullmatch(r'[\W_]+', w): continue
            n = max(1, len(w.split())) if w.startswith('[') and w != '[..]' else 1
            tot += n
            if '[' not in w: rd += 1
    return tot, rd
T = R = 0
for fn in sys.argv[1:] or ['r9411/reading_r9411.txt', 'r9411/reading_r9412.txt']:
    t, r = measure(fn); T += t; R += r
    print('%s  words %d  read %d  %.1f%%' % (fn, t, r, 100*r/t))
print('total  words %d  read %d  %.1f%%' % (T, R, 100*R/T))
