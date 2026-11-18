"""Group the Hungaricana 'sifrír*' regests (raw/h_sifrir.jsonl) of HHStA Türkei I by despatch date, per lead's Karton range,
and flag the dates on which every regest says 'no decipherment' (no deciphered copy of the same date in the hits)."""
import json, re, sys
from collections import defaultdict

RANGES = {1221: (36, 45), 1222: (46, 49), 1223: (51, 63), 1224: (65, 76), 1225: (77, 92)}
H = [json.loads(l) for l in open('raw/h_sifrir.jsonl', encoding='utf8')]
NODEC = re.compile(r'nincs\s+feloldv|feloldás\s+nélkül|nincs\s+feloldás|feloldatlan|nincsen\s+feloldv|feloldása\s+nincs', re.I)
DEC = re.compile(r'feloldv|feloldás|megfejt', re.I)


def kt(h):
    m = re.search(r'Karton (\d+)', h['ref'])
    return int(m.group(1)) if m else -1


def dkey(h):
    m = re.match(r'(\d{4})\.(\d{2})\.(\d{2})', h['date'].strip('( ad'))
    if not m:
        m = re.search(r'(\d{4})\.(\d{2})\.(\d{2})', h['date'])
    return m.group(0) if m else 'undated'


def status(h):
    d = h['desc']
    if NODEC.search(d):
        rest = NODEC.sub('', d)
        return 'nodec+dec' if DEC.search(rest) else 'nodec'
    return 'dec' if DEC.search(d) else 'none'


out = {}
for lead, (a, b) in RANGES.items():
    T = [h for h in H if 'Türkei I.' in h['ref'] and a <= kt(h) <= b]
    by = defaultdict(list)
    for h in T:
        by[dkey(h)].append(h)
    clean = []
    for d, hs in sorted(by.items()):
        st = [status(h) for h in hs]
        if d != 'undated' and all(s == 'nodec' for s in st):
            clean.append((d, hs))
    out[lead] = clean
    print(f'== lead {lead} Kt {a}-{b}: {len(T)} cipher regests, {len(by)} dates, {len(clean)} dates with only no-decipherment regests')
    for d, hs in clean:
        for h in hs:
            orig = 'ORIG' if re.search(r'\borig', h['desc'], re.I) else ('DUP' if re.search(r'dupl|tripl|quadr', h['desc'], re.I) else '')
            print(f'   {d} {h["id"]} {orig:4} | {h["ref"][16:70]} | {h["desc"][:150]}')
