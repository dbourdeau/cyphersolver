"""decode.py "12 345 6 78" -> letters with the frozen key (key/key_positions.json)."""
import json, os, sys, unicodedata
K = {int(k): v for k, v in json.load(open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'key', 'key_positions.json')))['positions'].items()}
print(''.join((unicodedata.normalize('NFD', K[int(t)])[0].lower() if int(t) in K else f'[{t}]') if t.isdigit() else t for t in ' '.join(sys.argv[1:]).replace(',', ' ').split()))
