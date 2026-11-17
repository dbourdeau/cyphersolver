"""Build items.json: the single catalogue items, and every 'no decipherment' cipher regest of Türkei I Kt. 93-120 in the
w20_b12 'sifrír*' harvest, grouped by catalogue entry (1226: up to 1620; 1227: 1621-31; 1228: Kt. 112-115; 1229: Kt. 116-120)."""
import json, re, os
HERE = os.path.dirname(os.path.abspath(__file__))
H = [json.loads(l) for l in open(os.path.join(HERE, '..', 'vetting_2026-11-16_w20_b12', 'raw', 'h_sifrir.jsonl'), encoding='utf8')]
NODEC = re.compile(r'nincs\s+feloldv|feloldás\s+nélkül|nincs\s+feloldás|feloldatlan|nincsen\s+feloldv|feloldása\s+nincs|'
                   r'csak\s+sifrír|sifrírben\s+maradt|sifrírban\s+maradt|semmi\s+feloldás|nincs\s+feloldása', re.I)
items = [{'group': g, 'id': i} for g, i in [
    ('2237', 49853), ('343', 48359), ('342', 47620), ('501', 43971), ('2675', 44944), ('2676', 46735),
    ('885', 43245), ('885', 43246), ('885', 43251),
    ('1230', 147865), ('1230', 147866), ('1231', 146487), ('1231', 146488), ('1232', 146748), ('2455', 146425),
    ('2457', 142904), ('2458', 142915), ('2459', 142345), ('2460', 164502), ('1234', 141595)]]
def kt(h):
    m = re.search(r'(?:Karton|Kt\.)\s*(\d+)', h['ref']); return int(m.group(1)) if m else -1
for h in sorted(H, key=lambda h: h['id']):
    if 'Türkei I' not in h['ref'] or not NODEC.search(h['desc']):
        continue
    k = kt(h)
    if 93 <= k <= 108:
        m = re.search(r'Konv\.\s*(\d+)', h['ref'])
        g = '1226' if (k < 108 or (m and m.group(1) == '1')) else '1227'
    elif 109 <= k <= 111: g = '1227'
    elif 112 <= k <= 115: g = '1228'
    elif 116 <= k <= 120: g = '1229'
    else: continue
    items.append({'group': g, 'id': h['id']})
json.dump(items, open(os.path.join(HERE, 'items.json'), 'w', encoding='utf8'), indent=0)
from collections import Counter
print(Counter(i['group'] for i in items))
