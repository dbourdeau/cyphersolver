"""Rebuild key/key_full_r3.json: majority unit per number from every draft pair (pp.599-609) and the recipient's glosses."""
import json, hashlib, collections, os, sys
D = sys.argv[1] if len(sys.argv) > 1 else '.'
def rows(fn):
    for l in open(os.path.join(D, fn), encoding='utf-8'):
        if l.startswith('#') or not l.strip(): continue
        yield l.rstrip('\n').split('\t')
v = collections.defaultdict(collections.Counter)
for f in rows('key/key_source_pairs_pp600-603_609.tsv'): v[int(f[0])][f[1]] += 1
for f in rows('transcriptions/p604-606_cipher_with_p599_draft.tsv'):
    if len(f) >= 3 and not f[0].endswith('s') and f[2] != '?': v[int(f[1])][f[2]] += 1
for fn in ('key/key_additions_round2.tsv', 'key/heldout_p608_truth.tsv', 'key/key_pairs_classB_glosses.tsv'):
    for f in rows(fn): v[int(f[0])][f[1]] += 1
K = {n: c.most_common(1)[0][0] for n, c in v.items()}
blob = json.dumps(sorted(K.items()), ensure_ascii=False)
out = sys.argv[2] if len(sys.argv) > 2 else os.path.join(D, 'key/key_full_r3.json')
open(out, 'w').write(blob)
print(len(K), hashlib.sha256(blob.encode()).hexdigest())
