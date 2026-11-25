"""Run the frozen, marker-directed Gifford comparison once, offline."""
import csv
import hashlib
import json
import random
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
LETTERS = 'ABCDEFGHIKLMNOPQRSTVWXYZ'
IDS = 'ABCDEFGHIJKL'
MARKERS = set('2468')
NORMAL = str.maketrans({'J':'I','U':'V'})


def tsv(path):
    with path.open(encoding='utf-8-sig',newline='') as stream:
        return list(csv.DictReader(stream,delimiter='\t'))


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def word(raw):
    text = unicodedata.normalize('NFKC',raw.upper()).translate(NORMAL)
    if '?' in text or any(c.isdigit() for c in text):
        return ''
    return ''.join(c for c in text if c in LETTERS)


def reader(path):
    data = tsv(path)
    groups = {entry['group'].upper():entry['reading'].upper().strip() for entry in data}
    assert len(data)==len(IDS) and set(groups)==set(IDS)
    assert all(re.fullmatch('[A-Z0-9?]*', text) for text in groups.values())
    return groups


def agree(first,second):
    found = []
    for group in IDS:
        a,b=first[group],second[group]
        mark,stem,reason=None,'',''
        if not a or not b or a[-1] != b[-1] or a[-1] not in MARKERS:
            reason='no agreed final selector'
        elif len(a) != len(b):
            reason='unequal stem lengths'
        else:
            mark=a[-1]
            left,right=a[:-1].translate(NORMAL),b[:-1].translate(NORMAL)
            stem=''.join(x if x==y and x in LETTERS else '?' for x,y in zip(left,right))
            if sum(c in LETTERS for c in stem)<3:
                reason='fewer than three agreed letters'
        found.append(dict(group=group,a=a,b=b,marker=mark,stem=stem,reason=reason))
    return found


def reference_index(ref):
    index=defaultdict(list)
    for i,w in enumerate(ref):
        for start in range(len(w)):
            for end in range(start+3,len(w)+1):
                index[w[start:end]].append((i,start))
    return index


def rank(matches):
    # Maximize letters and number of groups, then earliest reference positions and group IDs.
    return (sum(entry['length'] for entry in matches),len(matches),
            tuple(-entry['reference_word'] for entry in matches),
            tuple(-ord(entry['group']) for entry in matches))


def matches(streams,ref,index):
    # Each saved path ends in a particular reference word. Update only after
    # finishing an entire group, so a group can never match two words.
    paths={-1:[]}
    for group,stream in streams.items():
        possible={}
        for start in range(len(stream)):
            for end in range(start+3,len(stream)+1):
                piece=stream[start:end]
                if '?' in piece:
                    break
                for pos,offset in index.get(piece,()):
                    detail=dict(group=group,reference_word=pos+1,reference=ref[pos],stream=stream,
                                fragment=piece,length=len(piece),cipher_span=[start,end],
                                reference_span=[offset,offset+len(piece)],whole=stream==ref[pos])
                    if pos not in possible or len(piece)>possible[pos]['length']:
                        possible[pos]=detail
        updated=dict(paths)
        for pos,detail in possible.items():
            best=max((old for prev,old in paths.items() if prev<pos),key=rank)
            candidate=best+[detail]
            if pos not in updated or rank(candidate)>rank(updated[pos]):
                updated[pos]=candidate
        paths=updated
    best=max(paths.values(),key=rank)
    return dict(streams=streams,score=rank(best)[0],matches=best)


def main():
    inputs=json.loads((HERE/'INPUT_FREEZE.json').read_text())['sha256']
    for name,checksum in inputs.items():
        assert digest(HERE/name)==checksum
    files=json.loads((HERE/'FREEZE.json').read_text())['sha256']
    for name,checksum in files.items():
        path=Path(__file__).resolve().parents[3]/name
        assert digest(path)==checksum, name
    assert digest(HERE/'score.py') in (HERE/'SCORER_FREEZE.txt').read_text()
    assert not (HERE/'result.json').exists(), 'original result already exists'

    first,second=[reader(HERE/f'reader_{r}/reading.tsv') for r in 'ab']
    consensus=agree(first,second)
    eligible=[entry for entry in consensus if not entry['reason']]
    letters=sum(sum(c in LETTERS for c in entry['stem']) for entry in eligible)
    rawref=(HERE/'clear/reading.txt').read_text(encoding='utf-8-sig').splitlines()
    ref=[word(r) for r in rawref]
    result={'consensus':consensus,'eligible_groups':len(eligible),'eligible_letters':letters}
    if len(ref)!=120 or ref[:2]!=['IT','TROVBLED'] or len(eligible)<5 or letters<18:
        result.update(status='insufficient input',reference_tokens=len(ref),reference_anchor=ref[:2])
    else:
        idx=reference_index(ref)
        alphabets=tsv(HERE/'alphabet.tsv')
        outputs={}
        for orientation,fromcol,tocol in [('row_to_top','shift_row','header'),('top_to_row','header','shift_row')]:
            maps={r['marker']:str.maketrans(r[fromcol],r[tocol]) for r in alphabets}
            outputs[orientation]={e['group']:e['stem'].translate(maps[e['marker']]) for e in eligible}
        real={name:matches(streams,ref,idx) for name,streams in outputs.items()}
        winner=max(real,key=lambda name:rank(real[name]['matches']))
        best=real[winner]
        rng=random.Random(15950615)
        controls=[]
        for i in range(1000):
            shuffled=list(LETTERS)
            rng.shuffle(shuffled)
            mapping=str.maketrans(LETTERS,''.join(shuffled))
            pair=[]
            for streams in outputs.values():
                transformed={name:value.translate(mapping) for name,value in streams.items()}
                pair.append(matches(transformed,ref,idx)['score'])
            controls.append((i+1,*pair,max(pair)))
        dist=Counter(c[-1] for c in controls)
        with (HERE/'controls.tsv').open('x',newline='') as out:
            w=csv.writer(out,delimiter='\t',lineterminator='\n')
            w.writerow(['replicate','row_to_top','top_to_row','best'])
            w.writerows(controls)
        result.update(status='scored',orientations=real,best_orientation=winner,score=best['score'],
                      match_count=len(best['matches']),full_words=sum(x['whole'] for x in best['matches']),
                      greater=sum(count for score,count in dist.items() if score>best['score']),
                      tied=dist[best['score']],control_max=max(dist),distribution=dict(sorted(dist.items())),
                      passed=best['score']>=12 and len(best['matches'])>=3 and best['score']>max(dist))
    with (HERE/'result.json').open('x') as out:
        json.dump(result,out,indent=2)
        out.write('\n')
    print({k:v for k,v in result.items() if k not in ('consensus','orientations','distribution')})


if __name__=='__main__':
    main()
