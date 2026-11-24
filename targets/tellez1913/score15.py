from pathlib import Path
from collections import Counter
import argparse, json, math, random, re, unicodedata

def load_key(path):
    return dict(line.split()[:2] for line in path.read_text().splitlines())

def corpus_counts(path):
    text=path.read_text()
    letters=re.sub('[^a-z]','',unicodedata.normalize('NFKD',text[text.index('*** START'):text.rindex('*** END')].lower()))
    letters=letters[:len(letters)*9//10]
    return [Counter(letters[i:i+size] for i in range(len(letters)-size+1)) for size in (2,3)]

def measure(runs,key,new,counts):
    two,three=counts
    known=total=adj=0
    full=inc=0.0
    nfull=ninc=0
    active=set()
    hits=Counter()
    raws=[]
    for run in runs:
        prev=[]; parts=[]; last_known=False
        for i,code in enumerate(run):
            total+=1
            if code not in key:
                parts.append('?');prev=[];last_known=False;continue
            known+=1
            if last_known: adj+=1
            last_known=True
            if code in new: hits[code]+=1
            value=key[code];parts.append(value)
            for char in value:
                prev.append((char,i,code));prev=prev[-3:]
                if len(prev)<3 or prev[0][1]==prev[-1][1]: continue
                gram=''.join(z[0] for z in prev)
                ll=math.log((three[gram]+.1)/(two[gram[:2]]+2.6))
                full+=ll;nfull+=1
                present={z[2] for z in prev}&new
                if present:
                    inc+=ll;ninc+=1;active.update(present)
        raws.append(''.join(parts))
    return dict(n=total,known=known,adj=adj,boundary_trigrams=nfull,score=full/nfull if nfull else -1000,
                increment_trigrams=ninc,increment_score=inc/ninc if ninc else -1000,raw=raws,
                new_hits={c:hits[c] for c in sorted(new,key=int)},scored_new=sorted(active,key=int))

def controls(result,observed):
    ordered=sorted(result);lower=sum(x<observed for x in result)
    return dict(controls_lower=lower,p=(1001-lower)/1001,q995=ordered[994],maxcontrol=ordered[-1])

def run(folder,corpus):
    runs=[s.split() for s in (folder/'oct15.runs').read_text().splitlines() if s.strip()]
    old=load_key(folder/'candidate.tsv'); key=load_key(folder/'candidate15.tsv')
    new=set(key)-set(old);counts=corpus_counts(corpus)
    fixed=measure(runs,key,new,counts); earlier=measure(runs,old,set(),counts)
    all_controls=[];delta_controls=[]
    for incremental in [False,True]:
        pool=[k for k in key if not incremental or k in new]
        vals=[key[k] for k in pool]
        rng=random.Random(15101913 if incremental else 19131015)
        for _ in range(1000):
            rng.shuffle(vals); shuffled={**key,**dict(zip(pool,vals))}
            stat=measure(runs,shuffled,new,counts)
            (delta_controls if incremental else all_controls).append(stat['increment_score' if incremental else 'score'])
    whole=controls(all_controls,fixed['score']);inc=controls(delta_controls,fixed['increment_score'])
    whole['pass_stats']=bool(fixed['known']/fixed['n']>=.4 and fixed['adj']>=10 and fixed['boundary_trigrams']>=12 and whole['controls_lower']>=995)
    inc['pass_stats']=sum(fixed['new_hits'].values())>=4 and len(fixed['scored_new'])>=3 and inc['controls_lower']>=995
    return dict(expanded=fixed,earlier_descriptive=earlier,whole_key=whole,increment=inc)

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('folder',type=Path)
    parser.add_argument('corpus',type=Path)
    args=parser.parse_args()
    print(json.dumps(run(args.folder,args.corpus),indent=2))
