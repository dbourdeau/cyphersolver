"""Fetch a pinned corpus; parse JSON records without executing upstream JavaScript."""
import hashlib
import json
import re
from pathlib import Path
import urllib.request

ROOT = Path(__file__).resolve().parent
DATA = ROOT / 'data'
DATA.mkdir(exist_ok=True)
api = 'https://api.github.com/repos/mwenge/lineara.xyz/commits?path=LinearAInscriptions.js&per_page=1'
manifest_path = ROOT / 'source_manifest.json'
if manifest_path.exists():
    commit = json.loads(manifest_path.read_text(encoding='utf-8'))['commit']
else:
    req = urllib.request.Request(api, headers={'User-Agent': 'LinearA-research'})
    commit = json.load(urllib.request.urlopen(req))[0]['sha']
url = f'https://raw.githubusercontent.com/mwenge/lineara.xyz/{commit}/LinearAInscriptions.js'
raw = urllib.request.urlopen(url).read()
(DATA / 'LinearAInscriptions.js').write_bytes(raw)
s = raw.decode('utf-8')
s = re.sub(r'\\u\{([0-9a-fA-F]+)\}', lambda m: chr(int(m[1], 16)), s)
# Allow JavaScript trailing commas outside strings; no evaluation is performed.
chars = list(s)
quoted = False
escaped = False
for i, char in enumerate(s):
    if quoted:
        if escaped:
            escaped = False
        elif char == '\\':
            escaped = True
        elif char == '"':
            quoted = False
    elif char == '"':
        quoted = True
    elif char == ',':
        j = i + 1
        while j < len(s) and s[j].isspace():
            j += 1
        if j < len(s) and s[j] in ']}':
            chars[i] = ' '
s = ''.join(chars)
start = s.index('var inscriptions = new Map([') + len('var inscriptions = new Map([')
decoder = json.JSONDecoder()
rows = []
pos = start
while True:
    while s[pos].isspace() or s[pos] == ',':
        pos += 1
    if s[pos] == ']':
        break
    row, pos = decoder.raw_decode(s, pos)
    assert isinstance(row, list) and len(row) == 2
    name, record = row
    # This is an interpretative gloss, not epigraphic evidence.
    record.pop('translatedWords', None)
    rows.append({'source_key': name, **record})
(DATA / 'corpus.json').write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding='utf-8')
manifest = {'source': url, 'commit': commit, 'sha256': hashlib.sha256(raw).hexdigest(),
            'access_date': '2026-09-23', 'records': len(rows),
            'description': 'Robert Hogan / mwenge digital corpus, derived from GORILA, Douros and Younger; provisional transliteration, not a translation.',
            'excluded_fields': ['translatedWords'],
            'limitations': 'Editorial segmentation and missing uncertainty marks require source collation. Records may be alternate faces or duplicate witnesses.'}
(ROOT / 'source_manifest.json').write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
print(json.dumps(manifest, indent=2))
