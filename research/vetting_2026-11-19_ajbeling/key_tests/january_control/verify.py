"""Compare an unchanged masked key to the January positive reference."""
import csv
import itertools
import json
import random
import re
from functools import lru_cache
from pathlib import Path

P = Path(__file__).resolve().parent

def read(path):
    with path.open() as f:
        return list(csv.DictReader(f, delimiter="\t"))

def normalize(s):
    return re.sub("[^a-z]", "", s.lower()).replace("j", "i").replace("v", "u")

def nearest(x, points):
    dist = min(abs(x-y) for y in points)
    options = [y for y in points if abs(x-y)==dist]
    return options[0] if len(options)==1 and dist <=14 else None

def merged():
    maps=[]
    for name in ["a","b"]:
        rows=read(P/f"pass_{name}.tsv")
        mapping={int(r["x"]):r for r in rows}
        assert len(mapping)==len(rows)
        maps.append(mapping)
    first,second=maps
    slots=[]; seen=set()
    for x,r in first.items():
        y=nearest(x,second)
        if y is None or nearest(y,first)!=x:
            slots.append((x,None));continue
        seen.add(y)
        b=second[y]
        tile=None
        if (r["tile"].isdigit() and b["tile"].isdigit()
                and int(r["tile"])==int(b["tile"])
                and r["confidence"].lower()==b["confidence"].lower()=="high"):
            tile=r["tile"].zfill(2)
        slots.append(((x+y)/2,tile))
    slots.extend((y,None) for y in second if y not in seen)
    slots.sort(key=lambda v:v[0])
    return [s for _,s in slots]

def evaluate(runs, words, reference):
    strings=["".join(normalize(words[t]) for t in run) for run in runs]
    @lru_cache(None)
    def best(index, previous_end):
        if index==len(strings):return 0
        s=strings[index]
        score=best(index+1,previous_end)
        if len(s)>=4:
            pos=reference.find(s,previous_end)
            if pos!=-1:
                score=max(score,len(s)+best(index+1,pos+len(s)))
        return score
    return best(0,0)

def main():
    slots=merged()
    values={r["tile"]:(r["kind"],r["value"]) for r in read(P.parent/"values.tsv") if r["key"] == "97a"}
    assert all(t is None or t in values for t in slots)
    runs=[list(g) for k,g in itertools.groupby(slots,lambda t:t is not None) if k]
    pairs=sum(len(run)-1 for run in runs)
    covered=sum(map(len,runs))
    report=dict(slots=len(slots),covered=covered,adjacent_pairs=pairs)
    if (P/"reference_range_unverified.txt").exists():
        report.update(status="reference bounds unverified",shuffles=0)
    else:
        reference=normalize((P/"reference.txt").read_text())[:150]
        assert len(reference)>=20
        observed=evaluate(runs,{t:v for t,(_,v) in values.items()},reference)
        controls=[]
        rng=random.Random(15850104)
        groups={k:sorted({val for typ,val in values.values() if typ==k}) for k in ["letter","word"]}
        for _ in range(1000):
            by_kind={}
            for kind,words in groups.items():
                perm=words.copy();rng.shuffle(perm)
                by_kind.update({(kind,w):v for w,v in zip(words,perm)})
            controls.append(evaluate(runs,{t:by_kind[v] for t,v in values.items()},reference))
        report.update(matched_characters=observed,shuffles=1000,best_shuffle=max(controls),
                      controls_equal_or_better=sum(s>=observed for s in controls),
                      status="pass" if covered/len(slots)>=.40 and pairs>=5 and observed>=4 and observed>max(controls) else "miss")
    expected = json.loads((P/"result.json").read_text())
    if report != expected:
        raise ValueError(f"Positive control differs: {report}")
    print(f"Known January cipher: {covered}/{len(slots)} positions, {pairs} adjacent pairs. "
          f"Result {report['status']}.")
if __name__=="__main__":main()
