from pathlib import Path
import csv
import hashlib
import json
import random
import re
import unicodedata
from collections import Counter

here = Path(__file__).resolve().parent
outfile = here/'numeric_result.json'
if outfile.exists():
    raise SystemExit('A result exists. This test runs once.')
def get_rows(p):
    with (here/p).open() as f:
        return list(csv.DictReader(f, delimiter='\t'))
def digest(p):
    return hashlib.sha256((here/p).read_bytes()).hexdigest()
files = ['PLAN_numeric.md','a/cipher_groups.tsv','b/groups.tsv','key/V_names.tsv','run_numeric.py']
hashes = {p:digest(p) for p in files}
assert hashes['PLAN_numeric.md'] == '1bd08b2f13a4eac49c3a1366f3b6eb591a1f27f97cc5644a05aa1763de1faee1'
assert hashes['key/V_names.tsv'] == '4cf0357b4d64afc96769d1b5e8bc189c515bb39fc6d769e882f4c7aafe1d932e'
with (here/'numeric_inputs.json').open('x') as f:
    json.dump(hashes,f,indent=2)
aa=[(r['id'],r['diplomatic_shapes_in_order'].replace(' ','').rstrip(':')) for r in get_rows('a/cipher_groups.tsv') if r['folio']=='153r']
bb=[r for r in get_rows('b/groups.tsv') if r['scan']=='164' and r['classification']=='likely_cipher_number']
aa=[(i,n) for i,n in aa if re.fullmatch('[0-9]{3}',n)]
assert len(aa)==len(bb)==3
groups=[n if n==other['visible_shapes'] else None for (_,n),other in zip(aa,bb)]
key=sorted((r for r in get_rows('key/V_names.tsv') if r['eligible_exact_pair']=='yes'),key=lambda r:(r['scan'],r['section'],int(r['written_digits'])))
assert len({k['key'] for k in key})==1
digits=[r['written_digits'] for r in key]
assert len(digits)==len(set(digits))
values=[r['clear_equivalent'] for r in key]
names=['owen','paget','paldey']
def words(s):
    folded=unicodedata.normalize('NFKD',s.lower())
    return re.findall('[a-z]+',''.join(c for c in folded if not unicodedata.combining(c)))
def lookup(v):
    d=dict(zip(digits,v))
    return [d.get(n,'') for n in groups]
def score(readings):
    return sum(t in words(v) for t,v in zip(names,readings))
actual=lookup(values)
observed=score(actual)
rng=random.Random(15940921)
scores=[]
for _ in range(1000):
    perm=values.copy()
    rng.shuffle(perm)
    scores.append(score(lookup(perm)))
higher=sum(v>=observed for v in scores)
with (here/'numeric_controls.tsv').open('x') as f:
    f.write('permutation\tscore\n')
    for i,v in enumerate(scores,1):
        f.write(f'{i}\t{v}\n')
output=dict(groups=groups,key=key[0]['key'],eligible_entries=len(key),lookup=actual,predicted=names,score=observed,
            controls=1000,distribution=dict(sorted(Counter(scores).items())),at_least=higher,
            corrected_probability=(1+higher)/1001,passed=observed==3 and (1+higher)/1001<=0.01)
with outfile.open('x') as f:
    json.dump(output,f,indent=2)
print(json.dumps(output))
