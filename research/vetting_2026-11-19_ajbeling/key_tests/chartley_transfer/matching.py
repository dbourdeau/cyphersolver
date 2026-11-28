"""Alignment, ordered whole-tile string matching, and stratified shuffles."""
import csv
import random
import re


def load(path):
    with path.open() as f:
        return list(csv.DictReader(f, delimiter='\t'))


def normalized(s):
    return re.sub('[^a-z]', '', s.lower()).replace('j','i').replace('v','u')


def reference(s, limit=None):
    text = ''
    words = []
    for word in re.finditer(r'\[[^]]*\]|[a-zA-Z]+', s):
        value = '#' if word.group().startswith('[') else normalized(word.group())
        words.append((len(text)+1, len(text)+len(value), word.group()))
        text += value
    if limit:
        text = text[:limit]
    return text, words


def nearest(x, other):
    best = min(abs(x-y) for y in other)
    close = [y for y in other if abs(x-y)==best]
    return close[0] if len(close)==1 and best<=14 else None


def read_positions(path, table):
    rows = {}
    for row in load(path):
        x = int(row['x'])
        conf = row['confidence'].lower().strip()
        tile = row['tile'].strip()
        assert 0<=x<=2064 and x not in rows and conf in ('high','medium','low')
        if tile.isdigit():
            tile=tile.zfill(2)
            assert tile in table
        else:
            assert tile=='?'
        rows[x] = (tile,conf)
    return rows


def align(a,b):
    slots = []
    used = set()
    for x in a:
        y = nearest(x,b)
        if y is not None and nearest(y,a)==x:
            slots.append(((x+y)/2,x,y))
            used.add(y)
        else:
            slots.append((x,x,None))
    slots.extend((y,None,y) for y in b if y not in used)
    return sorted(slots,key=lambda v:v[0])


def better(first, second):
    return first if (-first[0],len(first[1]),first[1])<(-second[0],len(second[1]),second[1]) else second


def match(tokens, ref, whole=False):
    hits=[]
    for i,v in enumerate(tokens):
        if v is None or (whole and i and tokens[i-1] is not None):
            continue
        j=i
        s=''
        while j<len(tokens) and tokens[j] is not None:
            s+=tokens[j]
            j+=1
            if whole and j<len(tokens) and tokens[j] is not None:
                continue
            p=ref.find(s)
            if p==-1:
                break
            if len(s)<4:
                continue
            while p!=-1:
                hits.append((i+1,p+1,j,p+len(s)))
                p=ref.find(s,p+1)
    hits.sort()
    path=[]
    best=(0,())
    for h in hits:
        prev=(0,())
        for end,score in path:
            if end[2]<h[0] and end[3]<h[1]:
                prev=better(prev,score)
        scored=(prev[0]+h[3]-h[1]+1,prev[1]+(h,))
        path.append((h,scored))
        best=better(best,scored)
    return best


def has_long_match(track, reference_text):
    for start in range(len(track)):
        candidate = ''
        for stop in range(start,len(track)):
            if track[stop] is None:
                break
            candidate += normalized(track[stop][1])
            if candidate not in reference_text:
                break
            if stop-start+1 >= 3 and len(candidate)>=6:
                return True
    return False


def permutations(values,seed):
    rng=random.Random(seed)
    groups={k:sorted({word for typ,word in values if typ==k}) for k in ('letter','word')}
    for _ in range(1000):
        perm={}
        for k,words in groups.items():
            shuffled=words[:]
            rng.shuffle(shuffled)
            perm.update({(k,w):normalized(v) for w,v in zip(words,shuffled)})
        yield perm
