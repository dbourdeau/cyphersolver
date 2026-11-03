"""Filter gda_hits.json to cipher-bearing records dated to 1900; print one line each for reading by eye."""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
hits = json.load(open(os.path.join(HERE, 'gda_hits.json'), encoding='utf-8'))
print(hits['terms'])
WORD = re.compile(r'geheimschrift|geheimzeichen|geheimsprache|geheimschl|chiffr|chiffer|dechiff|dechif|verschlüssel|'
                  r'kryptogra|entziffer|ziffernbrief|zifferschrift|zifferbrief', re.I)
NOISE = re.compile(r'mobilmach|armeekorps|infanterie|kavallerie|artillerie|brigade|regiment|fernsprech|telegraf|telegraph|'
                   r'ziffer \d|ziffern? \d|ziff\. ?\d|monogramm|namenschiffre|chiffre der|gebührenziffer|kennziffer|'
                   r'pachtziffer|verhältnisziffer|meßziffer|zollziffer|tarifziffer|zweiziffer', re.I)
out = []
for rid, r in hits['hits'].items():
    text = ' '.join(str(v) for k, v in r.items() if k not in ('href', 'id', 'terms', 'Sprachcode', 'Schriftcode', 'Medium'))
    if not WORD.search(text) or NOISE.search(text):
        continue
    m = re.search(r'\b(1[3-9]\d\d)\b', r.get('Laufzeit') or r['head'])
    y = int(m.group(1)) if m else 9999
    if y > 1900:
        continue
    m2 = WORD.search(text)
    out.append((y, rid, r, text[max(0, m2.start() - 150):m2.end() + 130]))
out.sort(key=lambda x: x[0])
print(len(out))
for y, rid, r, ctx in out:
    d = 'D' if (r.get('Medium') or '').startswith('D') or 'igital' in (r.get('Medium') or '') else ' '
    print(y, d, r['head'][:60].replace('\n', ' '), '|', r.get('Provenienz', '')[:30], '|', re.sub(r'\s+', ' ', ctx)[:230])
