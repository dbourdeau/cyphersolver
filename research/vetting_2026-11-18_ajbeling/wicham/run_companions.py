from pathlib import Path
from collections import Counter
import csv, hashlib, json, random, re, unicodedata
p=Path(__file__).resolve().parent
output=p/'companions_result.json'
if output.exists():raise SystemExit('This test has been recorded.')
def rows(path):
    with (p/path).open() as f:return list(csv.DictReader(f,delimiter='\t'))
def digest(path):return hashlib.sha256((p/path).read_bytes()).hexdigest()
files=['PLAN_companions.md','a/companion.tsv','a/companion_sites.tsv','b/companion.tsv','key/V_names.tsv','run_companions.py']
hashes={f:digest(f) for f in files}
assert hashes['PLAN_companions.md']=='d65cc0f41409b281e3a3036370a34e1610ee124abab5f8dd2710d66812d876aa'
assert hashes['key/V_names.tsv']=='4cf0357b4d64afc96769d1b5e8bc189c515bb39fc6d769e882f4c7aafe1d932e'
with (p/'companions_inputs.json').open('x') as f:json.dump(hashes,f,indent=2)
aa=rows('a/companion.tsv');bb=[r for r in rows('b/companion.tsv') if r['category']=='likely_cipher']
def by_doc(r):
    folio=r['folio']
    if '154' in folio:return 'III'
    if '155' in folio:return 'IV'
    raise ValueError(folio)
pairs=[]
for doc in ['III','IV']:
    a=[r['digits'] for r in aa if by_doc(r)==doc and re.fullmatch('[0-9]{3}',r['digits'])]
    b=[r['digits_or_shapes'] for r in bb if by_doc(r)==doc]
    assert a==b
    pairs.extend((doc,n) for n in a)
key=sorted((r for r in rows('key/V_names.tsv') if r['eligible_exact_pair']=='yes'),key=lambda r:(r['scan'],r['section'],int(r['written_digits'])))
digits=[r['written_digits'] for r in key]
values=[r['clear_equivalent'] for r in key]
assert len(set(digits))==len(digits)==65
vocab={'III':[{'admiral','admirall'},{'norris','norreys'},{'essex'},{'cumberland'}],'IV':[{'jaques','jacques'},{'owen'},{'essex'},{'ross','rosse'}]}
def apply(choices):
    k=dict(zip(digits,choices))
    return [(doc,n,k.get(n,'')) for doc,n in pairs]
def score(out):
    s={}
    for doc,concepts in vocab.items():
        words=set(re.findall('[a-z]+',unicodedata.normalize('NFKD',' '.join(v for d,n,v in out if d==doc).lower())))
        s[doc]=sum(bool(words & concept) for concept in concepts)
    return s
rng=random.Random(15970720)
actual=apply(values);point=score(actual);total=sum(point.values())
control=[]
for i in range(1000):
    shuffled=values.copy();rng.shuffle(shuffled);control.append(sum(score(apply(shuffled)).values()))
above=sum(x>=total for x in control)
out=dict(lookups=actual,scores=point,total=total,control_dist=dict(sorted(Counter(control).items())),
    controls_at_least=above,p_corrected=(1+above)/1001,passed=(total>=3 and min(point.values())>0 and (1+above)/1001<=.01))
with (p/'companions_controls.tsv').open('x') as f:
    f.write('permutation\tscore\n')
    for i,v in enumerate(control,1):f.write(f'{i}\t{v}\n')
with output.open('x') as f:json.dump(out,f,indent=2)
print(json.dumps(out))
