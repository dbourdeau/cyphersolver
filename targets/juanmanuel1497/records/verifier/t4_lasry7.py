"""T4: in Lasry's own no. 95, what does each plain-7 token ('7', his D) become in his edited reading? Also '7-' and '7o'.
Aligns the key-decoded letter stream of each image with his edited text (letters only)."""
import sys, re, difflib
from collections import Counter, defaultdict
base = sys.argv[1]
key = {}
for line in open(base + "/key.txt", encoding='utf8'):
    if line.startswith('#') or ' - ' not in line: continue
    signs, v = line.rstrip('\n').rsplit(' - ', 1)
    for s in signs.split('|'): key[s] = v
res = defaultdict(Counter)
for img in ("f122a", "f122b", "f122c", "f122v"):
    toks = [t for l in open(f"{base}/transcription/{img}.txt", encoding='utf8') if not l.startswith('#') for t in l.strip().split(';') if t]
    stream, owner = [], []
    for t in toks:
        v = key.get(t, '?')
        if len(v) == 1 and v.isalpha(): stream.append(v.lower()); owner.append(t)
    ed = ''.join(re.sub(r'\[[^\]]*\]', '', l.split('|', 1)[1]) for l in open(f"{base}/edited/{img}_edits.txt", encoding='utf8') if '|' in l)
    ed = re.sub(r'[^a-z]', '', ed.lower())
    sm = difflib.SequenceMatcher(a=stream, b=list(ed), autojunk=False)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal':
            for i in range(i1, i2): res[owner[i]][stream[i]] += 1
        elif op == 'replace' and i2 - i1 == j2 - j1:
            for k in range(i2 - i1): res[owner[i1+k]][ed[j1+k] + '(edited)'] += 1
for t in ('7', '7-', '7o', 'S', ':-', 'np', 'T:', 'a_', 'ee', 'pi', 'pi:', '77'):
    print(t, key.get(t), dict(res[t]))
