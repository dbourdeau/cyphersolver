"""Apply the unmodified No. 23 table; the held-out text is not opened here."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

p=Path(__file__).resolve().parent
source=p.parent/'march'
spec=importlib.util.spec_from_file_location('march_model',source/'predict.py')
module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
parser=argparse.ArgumentParser()
parser.add_argument('reference_sha256',help='Published commitment only')
args=parser.parse_args()
assert len(args.reference_sha256)==64 and all(c in '0123456789abcdef' for c in args.reference_sha256)
assert hashlib.sha256((source/'key.tsv').read_bytes()).hexdigest()=='00f88bb120ef8ae850e1a59746d2d38347e52a749b2cc0304d37e13ee199bc26'
key={r['code']:r['value'] for r in module.rows('key.tsv')}
module.p=p
held=module.rows('groups21.tsv')
groups=[r['strict'] for r in held]
preds=module.predict(key,groups)
module.write('predictions21.tsv',['first','last','start_location','end_location','word'],[(a,b,held[a-1]['position'],held[b-1]['position'],w) for a,b,w in preds])
module.write('label_coverage21.tsv',['ordinal','position','code','candidate'],[(r['ordinal'],r['position'],r['strict'],key.get(r['strict'],'')) for r in held])
result=dict(slots21=len(groups),strict21=len(groups)-groups.count('?'),key_entries=len(key),held_marked_slots_covered=sum(g in key for g in groups),predicted_words=len(preds),distinct_predicted_words=len({w for _,_,w in preds}),whole_prediction_slot_count=len({i for a,b,_ in preds for i in range(a,b+1)}),reference_sha256=args.reference_sha256)
(p/'pre_score.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
