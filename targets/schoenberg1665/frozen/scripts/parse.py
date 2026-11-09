# Lit H-CHIFFRE.txt -> mots chiffrés normalisés (minuscules, sans (), [?], ~, °, ponctuation ; = joint le mot coupé).
import re, sys
def lines(fn):
    out = []
    for l in open(fn, encoding='utf-8'):
        m = re.match(r'L(\d): (.*)', l.rstrip('\n'))
        if m: out.append((int(m.group(1)), m.group(2)))
    return out
def words(fn, which=None):
    txt = ''
    for n, s in lines(fn):
        if which and n not in which: continue
        s = s.replace('[?]', '').replace('(', '').replace(')', '').replace('~', '').replace('°', '')
        txt += s + (' ' if not s.endswith('=') else '')
    txt = txt.replace('=', '').lower()
    return [w for w in re.split(r'[^a-z]+', txt) if w]
if __name__ == '__main__':
    from collections import Counter
    W = words(sys.argv[1]); s = ''.join(W)
    print(len(W), 'mots', len(s), 'lettres'); print(Counter(s).most_common())
    print(' '.join(W))
    for part, w in (('A L1-5', range(1, 6)), ('H L6-9', range(6, 10))):
        ww = words(sys.argv[1], set(w)); print(part, len(ww), len(''.join(ww)))
