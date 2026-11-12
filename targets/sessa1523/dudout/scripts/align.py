"""Align Daniel's b34 (a) tokens with his (b) pieces (one piece per cipher token) where counts agree;
write token -> Counter(values) table. Read-only on Daniel's file."""
import json, re, sys
from collections import Counter, defaultdict
def a_tokens(a):
    a = re.sub(r'"[^"]*"', ' ', a); a = re.sub(r'\([^()]*\)', ' ', a)
    return [t for t in a.split() if t not in ('f~', '/', '..', '...', '¶', "''", '▷db', 'v:db') and not t.startswith('"')]
def b_pieces(b):
    b = re.sub(r'"[^"]*"', ' ', b); b = re.sub(r'\((?:[^()]*)\)', ' ', b)
    b = b.replace('...', ' ').replace('¶', ' ').replace('/', ' ')
    out = []
    for w in re.findall(r'\{[^}]*\}|(?:\[[^\]]*\]|[^\s\[])+', b):
        for p in re.split(r'[\s-]+(?![^\[]*\])', w.strip('{}')):
            if p: out.append(p)
    return out
if __name__ == '__main__':
    recs = json.load(open(sys.argv[1]))
    T = defaultdict(Counter); ok = 0
    for r in recs:
        A, B = a_tokens(r['a']), b_pieces(r['b'])
        if len(A) == len(B):
            ok += 1
            for t, p in zip(A, B):
                m = re.match(r'\[([^\]=]*)(?:=([^\]]*))?\]$', p)
                v = (m.group(2) or '?') if m else p
                T[t][v] += 1
    print(ok, 'of', len(recs), 'lines aligned', file=sys.stderr)
    json.dump({t: dict(c) for t, c in T.items()}, open(sys.argv[2], 'w'), ensure_ascii=False, indent=0)
    for t, c in sorted(T.items(), key=lambda x: -sum(x[1].values()))[:70]:
        print(t, c.most_common(4))
