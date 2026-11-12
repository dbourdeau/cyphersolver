"""Daniel's 95 % rule on an annotated reading: read = sure + probable; restored and unresolved are holes."""
import re, sys
L = re.compile(r"[A-Za-zÀ-ÿ_]")
def count(t):
    c = dict(sure=0, probable=0, restored=0, unresolved=0)
    for m in re.finditer(r"\[\?([^\]]*)\]|\[([^\]]*)\]|\{([^}]*)\}|([^\[\{]+)", t):
        u, r, p, s = m.groups()
        if u is not None:
            n = len(L.findall(u)); n = n if n else (3 if '…' in u else 1); c['unresolved'] += n
        elif r is not None: c['restored'] += len(L.findall(r)) or 1
        elif p is not None: c['probable'] += len(L.findall(p))
        else: c['sure'] += len(L.findall(s))
    tot = sum(c.values()); c['total'] = tot; c['read%'] = round(100 * (c['sure'] + c['probable']) / tot, 1)
    return c
for p in sys.argv[1:]:
    print(p.split('/')[-1], count(open(p, encoding='utf-8').read()))
