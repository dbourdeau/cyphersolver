"""Build the Osnabrück letter key from LEFT-page booklet pairs only (see PREREG.md)."""
import csv, json, sys, collections
from pathlib import Path
base = Path(sys.argv[1])
def norm_clear(s):
    s = s.lower()
    for a, b in (('ä','a'),('ö','o'),('ü','u'),('v','u'),('j','i'),(' ','')): s = s.replace(a, b)
    return s
votes = collections.defaultdict(collections.Counter)
used = skipped = 0
for r in csv.DictReader(open(base/'transcription/booklet_pairs.tsv', encoding='utf-8'), delimiter='\t'):
    if r['page'] != 'L': continue
    c, p = r['cipher_as_seen'], norm_clear(r['clear_as_seen'])
    if len(c) != len(p): skipped += 1; continue
    used += 1
    for a, b in zip(c, p): votes[a][b] += 1
key = {a: v.most_common(1)[0][0] for a, v in sorted(votes.items())}
conflicts = {a: dict(v) for a, v in votes.items() if len(v) > 1}
json.dump({'key': key, 'pairs_used': used, 'pairs_skipped_unequal_length': skipped, 'conflicts': conflicts},
          open(base/'results/key.json', 'w'), indent=1, sort_keys=True)
print(json.dumps(key), 'used', used, 'skipped', skipped, 'conflicts', conflicts)
