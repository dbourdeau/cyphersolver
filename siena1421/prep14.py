import re, sys
src = open(sys.argv[1], encoding='utf-8').read()
body = src.split('TRANSCRIPTION')[1]
body = body.split('\nCOUNT')[0] if '\nCOUNT' in body else body
words = []
for l in body.splitlines():
    m = re.match(r'L\d+\s(.*)', l)
    if not m: continue
    b = re.sub(r'\{[^}]*\}', ' ', m.group(1)); b = re.sub(r'\[[^\]]*\]', ' ', b)
    for w in re.split(r'\s/\s|\s/$|^/\s|::|:', ' ' + b + ' '):
        toks = []
        bad = False
        for t in w.split():
            if t in ('/',): continue
            if '??' in t or t == 'BLOT': bad = True; break
            t = t.rstrip('?').lstrip('^')
            t = re.sub(r'\^(tick|arch|curl|tilde|m)$', '', t)
            t = {"PLUS^dot": "PD", "^OR": "OR"}.get(t, t)
            if t in ('BAR', 'DASH', 'SLASH', 'ITICK', 'TILDE'): continue
            toks.append(t)
        if toks and not bad: words.append('_'.join(toks))
open(sys.argv[2], 'w', encoding='utf-8').write(' '.join(words) + '\n')
from collections import Counter
c = Counter(s for w in words for s in w.split('_'))
print(len(words), sum(c.values()), len(c)); print(c.most_common())
print(Counter(words).most_common(25))
