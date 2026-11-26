from pathlib import Path
from collections import Counter
import argparse, math, re, unicodedata, random, json

here=Path(__file__).resolve().parent
targets=here.parents[1]/'crawford_rebase/targets'
def norm(value):
    return re.sub('[^a-z]', '', unicodedata.normalize('NFKD',value.lower()))
def load_original():
    lines=(targets/'rubio1913/key.tsv').read_text().splitlines()
    original={i:v for ln in lines if ln and ln[0].isdigit() for i,v in [ln.split('\t')]}
    assert list(map(int,original))==list(range(1,161))
    return original
raw=(targets/'esp318/lit/quijote.txt').read_text()
text=norm(raw[raw.index('*** START'):raw.rindex('*** END')]);text=text[:len(text)*9//10]
two=Counter(text[i:i+2] for i in range(len(text)-1))
three=Counter(text[i:i+3] for i in range(len(text)-2))
def measure(runs,key):
    n=known=adj=tri=0;total=0.
    for run in runs:
        tail=[];prior=False
        for i,token in enumerate(run):
            n+=1
            if token not in key:
                tail=[];prior=False;continue
            known+=1;adj+=prior;prior=True
            for ch in key[token]:
                tail.append((ch,i));tail=tail[-3:]
                if len(tail)<3 or tail[0][1]==i:continue
                t=''.join(a for a,_ in tail)
                total+=math.log((three[t]+.1)/(two[t[:2]]+2.6));tri+=1
    return dict(groups=n,known=known,adjacent=adj,trigrams=tri,score=total/tri if tri else None)
def run(runs,seed):
    original=load_original()
    key={i:norm(v) for i,v in original.items()}
    out=measure(runs,key)
    vals=list(key.values());control=[];r=random.Random(seed)
    for _ in range(1000):
        r.shuffle(vals);control.append(measure(runs,dict(zip(key,vals)))['score'])
    cs=sorted(x for x in control if x is not None)
    assert len(cs)==1000
    lower=sum(x<out['score'] for x in cs)
    out.update(controls_lower=lower,p=(1001-lower)/1001,control_995=cs[994],control_max=cs[-1],seed=seed,
               emissions=[[original.get(t,'?') for t in row] for row in runs],controls=control)
    return out
def calibration():
    corpus={}
    for line in (targets/'rubio1913/transcription.txt').read_text().splitlines():
        if line.startswith('## '):
            witness=line[3:];corpus[witness]=[]
        else:
            row=re.sub(r'\[[^]]*\]','',line).strip()
            if re.fullmatch(r'\d+(?:\s+\d+)*',row):corpus[witness].append(row.split())
    assert len(corpus)==3
    results={w:run(rows,seed) for (w,rows),seed in zip(corpus.items(),(19130718,19140313,19140318))}
    return dict(positive_controls=results,assay_usable=all(o['controls_lower']>=990 for o in results.values()),
                floor=min(o['score'] for o in results.values())-.2)
def target(witness):
    cal=json.loads((here/'calibration.json').read_text())
    raw=(here/(witness+'.runs')).read_text()
    runs=[x.split() for x in raw.splitlines() if x.strip()]
    digits=sum(t.isdigit() for row in runs for t in row)
    total=sum(map(len,runs))
    if not cal['assay_usable'] or digits<35 or digits/total<.5:
        return dict(untestable=True,total=total,matched=digits,assay_usable=cal['assay_usable'])
    o=run(runs,19140325 if witness=='march25' else 19140519)
    o.update(matched_numbers=digits,language_floor=cal['floor'],coverage=o['known']/total)
    o['pass_statistics']=o['coverage']>=.75 and o['adjacent']>=12 and o['trigrams']>=20 and o['score']>=cal['floor'] and o['controls_lower']>=996
    return o
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('mode',choices=['calibrate','march25','may19']);args=p.parse_args()
    print(json.dumps(calibration() if args.mode=='calibrate' else target(args.mode),indent=2,ensure_ascii=False))
