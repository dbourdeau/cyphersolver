"""Single run of the registered May 9 row-2 test."""
import csv
import hashlib
import json
from pathlib import Path
import random
import re

D = Path(__file__).resolve().parent

def rows(path):
    with (D / path).open(encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))

def lock(name):
    for line in (D / name).read_text().splitlines()[1:]:
        h, p = line.split('  ', 1)
        assert hashlib.sha256((D / p).read_bytes()).hexdigest() == h, p

def normalize(word):
    return word.upper().replace('J','I').replace('U','V')

def main():
    lock('FREEZE.txt')
    lock('RUN_FREEZE.txt')
    assert not (D / 'result.json').exists() and not (D / 'controls.tsv').exists()
    ordered = [r['group'] for r in rows('boxes.tsv')]
    tables = []
    for file in ('reader_a.tsv','reader_b.tsv','gloss.tsv'):
        content = rows(file)
        indexed = {r['group']: r for r in content}
        assert set(indexed) == set(ordered) and len(content) == len(ordered), file
        tables.append(indexed)
    row = next(r for r in rows('../nov20_william_transfer/alphabet.tsv') if r['marker']=='2')
    alphabet = row['header']
    table = str.maketrans(row['shift_row'], alphabet)
    record = []
    eligible = []
    for label in ordered:
        a,b,g = [r[label] for r in tables]
        l,r = normalize(a['reading'].strip()),normalize(b['reading'].strip())
        status = g['status'].lower().strip()
        assert status in {'sure','uncertain','absent'}, g
        sure_ink = bool(l == r and re.fullmatch('['+alphabet+']+2', l))
        gloss = g['gloss'].strip()
        gold = re.sub('[^A-Z]', '', normalize(gloss))
        is_gloss = bool(status=='sure' and gold and not re.search(r'[?\[\]\d\s]', gloss))
        rec = dict(group=label,a=a['reading'],b=b['reading'],sure_ink=sure_ink,gloss=gloss,gloss_status=status)
        if sure_ink and is_gloss:
            rec.update(output=l[:-1].translate(table),gold=gold)
            rec['exact']=rec['output']==gold
            eligible.append(rec)
        record.append(rec)
    distinct={e['output'] for e in eligible if e['exact']}
    metric=len(distinct)
    chars=sum(map(len,distinct))
    result=dict(eligible=len(eligible),whole_matches=sum(e['exact'] for e in eligible),distinct_matches=metric,letters=chars,groups=record,holdout=None)
    if not eligible:
        result['status']='unscorable'
    else:
        rng=random.Random(15950509)
        scores=[]
        for _ in range(1000):
            letters=list(alphabet)
            rng.shuffle(letters)
            remap=str.maketrans(alphabet, ''.join(letters))
            scores.append(len({e['gold'] for e in eligible if e['output'].translate(remap)==e['gold']}))
        result.update(control_max=max(scores),tied=scores.count(metric),higher=sum(s>metric for s in scores))
        passed=metric>=3 and chars>=12 and metric>max(scores)
        result['status']='pass' if passed else 'miss'
        if passed:
            for e in record:
                if e['sure_ink'] and e['gloss_status']=='absent':
                    stem=normalize(e['a'].strip())[:-1]
                    if len(stem)>=3 and stem.translate(table) not in {j['output'] for j in eligible}:
                        result['holdout']=dict(group=e['group'],ciphertext=e['a'],output=stem.translate(table))
                        break
        with (D/'controls.tsv').open('x') as f:
            f.write('replicate\tdistinct_matches\n')
            for i,n in enumerate(scores,1):
                f.write(f'{i}\t{n}\n')
    with (D/'result.json').open('x') as f:
        json.dump(result,f,indent=2)
        f.write('\n')
    print({k:v for k,v in result.items() if k!='groups'})

if __name__=='__main__':
    main()
