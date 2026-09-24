"""Download explicitly selected comparison material to the local research cache."""
import hashlib
import json
from pathlib import Path
import urllib.request

ROOT = Path(__file__).resolve().parent
manifest = json.loads((ROOT/'source_manifest.json').read_text(encoding='utf8'))
base = 'https://raw.githubusercontent.com/mwenge/lineara.xyz/' + manifest['commit'] + '/'
paths = ['commentary/'+n+'.html' for n in ['HT88','HT94','HT117','HT123+124','HT13','HT1','HT30','HT37','HT95','HT119']]
paths += ['images/'+n+'-Facsimile.jpg' for n in ['HT88','HT94b','HT117a','HT123+124a']]
receipts = []
for relative in paths:
    path = ROOT/'data'/Path(relative).name
    if not path.exists():
        path.write_bytes(urllib.request.urlopen(base+relative).read())
    raw = path.read_bytes()
    receipts.append({'url':base+relative, 'sha256':hashlib.sha256(raw).hexdigest(),
                     'local_path':'data/'+path.name})
(ROOT/'collation_manifest.json').write_text(json.dumps(receipts, indent=2)+'\n',encoding='utf8')
print(f'{len(receipts)} collation sources cached and hashed')
