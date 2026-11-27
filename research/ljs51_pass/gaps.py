"""Mechanical gap closure: for each cipher segment, is a plaintext segment later on the same page or on the next page?"""
import json
P = {p['n']: p for p in json.load(open('pages_merged.json', encoding='utf8'))}
def fo(p): return p['folio']
out = []
for n in sorted(P):
    p = P[n]; segs = p['contents']
    for i, s in enumerate(segs):
        if s.get('kind') != 'cipher': continue
        later = [t for t in segs[i+1:] if t.get('kind') in ('cipher', 'plaintext')]
        status = None
        if later and later[0]['kind'] == 'plaintext': status = 'same-page plaintext'
        elif later and later[0]['kind'] == 'cipher': status = 'next segment is another cipher (check)'
        else:
            nxt = P.get(n+1)
            if nxt:
                ns = [t for t in nxt['contents'] if t.get('kind') in ('cipher', 'plaintext')]
                if ns and ns[0]['kind'] == 'plaintext': status = 'next-page plaintext'
                elif ns and ns[0]['kind'] == 'cipher': status = 'continues as cipher on next page'
                else: status = 'nothing on next page (check)'
            else: status = 'end of book'
        out.append((fo(p), s.get('lines'), s.get('n_lines'), s.get('approx_signs'), status))
import collections
print(collections.Counter(o[4] for o in out))
for o in out:
    if o[4] not in ('same-page plaintext', 'next-page plaintext'): print(o)
