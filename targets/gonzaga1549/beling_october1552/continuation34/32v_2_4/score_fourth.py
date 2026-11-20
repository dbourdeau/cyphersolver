"""One prespecified directional test on the fourth cipher row."""
from collections import defaultdict
from pathlib import Path
import csv
import json
import random
import runpy

HERE = Path(__file__).resolve().parent
original = runpy.run_path(str(HERE / 'check.py'))
reference_words = 'en Roma lo qual haureis entendido y dello nos ha desplazido muy mucho'.split()
words = [original['norm'](word) for word in reference_words]
reference = ''.join(words)
spans = []
for i, word in enumerate(words):
    start = sum(map(len, words[:i]))
    spans.append((start, start + len(word)))


def compare(labels, key):
    parts = []
    usable = 0
    for label in labels:
        values = key.get(label, ())
        if values == ('NUL',):
            continue
        if len(values) != 1 or not all(ch.isalpha() or ch.isspace() for ch in values[0]):
            parts.append('#')
            continue
        parts.append(original['norm'](values[0]))
        usable += 1
    stream = ''.join(parts)
    best_size, best_start = 0, 0
    for block in stream.split('#'):
        for offset in range(len(block)):
            for end in range(offset + 1, len(block) + 1):
                fragment = block[offset:end]
                start = reference.find(fragment)
                if start < 0:
                    break
                if len(fragment) > best_size or (len(fragment) == best_size and start < best_start):
                    best_size, best_start = len(fragment), start
    end = best_start + best_size
    included = [w for w,(a,b) in zip(words,spans) if best_start <= a and b <= end]
    return {'stream':stream,'usable':usable,'score':best_size,'start':best_start,
            'fragment':reference[best_start:end], 'enclosed_reference_words':included}


def main():
    read = original['read_tsv']
    specimens = {int(r['number']):r['published_label'] for r in read(original['PLATE'])}
    mapping = defaultdict(set)
    for r in read(original['KEY']):
        mapping[r['label']].update(r['valeur'].split('|'))
    mapping = {k:tuple(sorted(v)) for k,v in mapping.items()}
    grids = []
    for tag in 'ab':
        grid = {}
        for r in read(HERE/f'reader_{tag}/reading.tsv'):
            if r['row'].strip().lower() != 'c':
                continue
            x = int(r['x'])
            assert x not in grid and 0<=x<800
            spec = r['specimen'].strip()
            high = r['confidence'].strip().lower() in ('high','medium')
            grid[x] = specimens[int(spec)] if spec.isdecimal() and high else None
        grids.append(grid)
    pairs = original['align'](*grids)
    fields = ['x_a','x_b','a','b','consensus']
    labels = []
    with (HERE/'fourth_positions.tsv').open('x') as f:
        w=csv.writer(f,delimiter='\t',lineterminator='\n')
        w.writerow(fields)
        for a,b in pairs:
            left,right=grids[0].get(a),grids[1].get(b)
            agreed=left if left is not None and left==right else None
            labels.append(agreed)
            w.writerow((a,b,left,right,agreed))
    result=compare(labels,mapping)
    keys=sorted(mapping)
    rng=random.Random(1552100633)
    controls=[]
    for _ in range(1000):
        vs=[mapping[k] for k in keys]
        rng.shuffle(vs)
        controls.append(compare(labels,dict(zip(keys,vs)))['score'])
    score=result['score']
    result.update({'union':len(pairs),'paired':sum(a is not None and b is not None for a,b in pairs),
                   'exact_labels':sum(v is not None for v in labels),'control_max':max(controls),
                   'control_greater':sum(n>score for n in controls),'control_tie':controls.count(score)})
    result['pass']=(result['usable']/len(pairs)>=.55 and score>=8 and
                    len(result['enclosed_reference_words'])>=2 and score>max(controls))
    with (HERE/'fourth_controls.txt').open('x') as f:
        f.write('\n'.join(map(str,controls))+'\n')
    with (HERE/'fourth_result.json').open('x') as f:
        json.dump(result,f,indent=2)
        f.write('\n')
    print(json.dumps(result))


if __name__=='__main__':
    main()
