"""In-sample check (build lines only, not a test): score the built key on part 1 against its own aligned print."""
import json, sys
sys.path.insert(0, 'scripts')
from build_key import p1, p2, U
from measure_lib import score
K = json.load(open('build/key_1577.json')); key = {s: v['plain'] for s, v in K['key'].items() if '+' not in s}
sp = K['plain_spans_used']
for name, part, (j0, j1) in (('part1', p1, sp['part1']), ('part2', p2, sp['part2'])):
    r, s, h = score([t for _, _, t in part], key, U[j0:j1]); print(name, r, s, round(r / s, 3), 'holes', h)
