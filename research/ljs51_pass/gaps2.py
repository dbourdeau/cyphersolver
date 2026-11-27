"""Chain cipher segments across page turns, then ask whether a plaintext answers each chain."""
import json, collections
P = json.load(open('pages_merged.json', encoding='utf8'))
seq = []  # reading order of (folio, seg)
for p in P:
    for s in p['contents']:
        if s.get('kind') in ('cipher', 'plaintext'): seq.append((p['folio'], p['n'], s))
def first(s): 
    l = s.get('lines') or [0, 0]; return l[0]
def last(s):
    l = s.get('lines') or [0, 0]; return l[-1]
chains = []; cur = None
for i, (fo, n, s) in enumerate(seq):
    if s['kind'] == 'cipher':
        if cur and cur['open'] and n == cur['last_n'] + 1 and first(s) <= 2:
            cur['segs'].append((fo, s)); cur['last_n'] = n; cur['open'] = last(s) >= 12; cur['idx'] = i
        else:
            if cur: chains.append(cur)
            cur = {'segs': [(fo, s)], 'last_n': n, 'open': last(s) >= 12, 'idx': i}
    else:
        if cur: cur['answered'] = cur.get('answered') or (i == cur['idx'] + 1)
if cur: chains.append(cur)
# a chain is answered if the segment right after its last cipher segment in reading order is plaintext
res = collections.Counter(); gaps = []
for c in chains:
    i = c['idx']
    nxt = seq[i+1] if i+1 < len(seq) else None
    ok = bool(nxt and nxt[2]['kind'] == 'plaintext')
    c['ok'] = ok
    res['answered' if ok else 'no plaintext follows'] += 1
    if not ok:
        a = c['segs'][0]; z = c['segs'][-1]
        gaps.append((a[0] + ' l.' + str(first(a[1])), z[0] + ' l.' + str(last(z[1])), sum(s.get('approx_signs') or 0 for _, s in c['segs'] if isinstance(s.get('approx_signs'), int)), (nxt[0] + ':' + nxt[2]['kind']) if nxt else 'END'))
print(len(chains), 'chains', dict(res))
for g in gaps: print(g)
json.dump([{'start': (c['segs'][0][0], first(c['segs'][0][1])), 'end': (c['segs'][-1][0], last(c['segs'][-1][1])), 'ok': c['ok'], 'red': any(s.get('red_gloss') for _, s in c['segs'])} for c in chains], open('chains.json', 'w'), indent=0)
