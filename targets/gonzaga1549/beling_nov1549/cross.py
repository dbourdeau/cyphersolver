"""Find the blind 1547 cross-sign loci using only equality of neighboring letters."""
import csv
import json
import random
import re
import sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/"beling_march1553"))
from calibrate import PROJECT, norm, sha, write_table
FOLDER=PROJECT/"targets/figueroa1534"
K4=FOLDER/"validation/K4.tsv"
TOK=FOLDER/"transcriptions/1379_14-18_img06.txt"
REF=FOLDER/"validation/clear_1547_ref_img06.txt"

def matches(ref,flank,left):
    found={}
    for k in range(1,len(flank)+1):
        term=flank[-k:] if left else flank[:k]
        pos=ref.find(term)
        if pos<0:
            break
        while pos>=0:
            found[pos+k if left else pos]=k
            pos=ref.find(term,pos+1)
    return found

def locate(ref,left,right):
    a,b=matches(ref,left,True),matches(ref,right,False)
    best=(0,0)
    choices=[]
    for i,ln in a.items():
        for j in range(i,i+5):
            rn=b.get(j,0)
            score=min(ln,rn),ln+rn
            if score>best:
                best=score
                choices=[(i,j,ln,rn)]
            elif score==best:
                choices.append((i,j,ln,rn))
    return (len(choices)==1 and best[0]>=4),best,choices

def main():
    key={}
    for r in csv.DictReader((r for r in K4.read_text().splitlines() if r and not r.startswith("#")),delimiter="\t"):
        v=r["valeur"].split("|")[0]
        key.setdefault(r["label"],"" if v=="NUL" else norm(v) or "?")
    names,positions=[],[]
    for line in TOK.read_text().splitlines():
        if line.startswith("L"):
            line_num,*labels=line.partition(" #")[0].split()
            for j,label in enumerate(labels,1):
                if label=="+":
                    positions.append((len(names),line_num,j))
                names.append(label)
    assert len(positions)==2
    clear=norm(re.sub(r"\[[^]]*\]",""," ".join(s for s in REF.read_text().splitlines() if not s.startswith("#"))))
    def query(k):
        vals=["?" if s=="+" else k.get(s,"?") for s in names]
        out=[]
        for i,line,pos in positions:
            left,right="".join(vals[:i])[-20:],"".join(vals[i+1:])[:20]
            anchored,score,spans=locate(clear,left,right)
            out.append((line,pos,left,right,anchored,score,spans))
        return out
    data=query(key)
    rows=[]
    for line,pos,left,right,anchored,score,spans in data:
        for i,j,l,r in spans[:10]:
            rows.append((line,pos,left,right,anchored,*score,len(spans),i,j,l,r,clear[i:j],clear[max(0,i-20):i],clear[j:j+20]))
    write_table(HERE/"cross_loci.tsv",("line","pos","mechanical_left","mechanical_right","anchored","min_support","sum_support","equally_best_spans","ref_start0","ref_end0","left_letters","right_letters","reference_gap","reference_left","reference_right"),rows)
    actual=sum(bool(x[4]) for x in data)
    rng=random.Random(15471114)
    labs=sorted(s for s in set(names) if s!="+" and key.get(s) not in {None,"","?"})
    vals=[key[s] for s in labs]
    ctr=[]
    for i in range(1000):
        values=vals[:]
        rng.shuffle(values)
        shuffled=dict(key)
        shuffled.update(zip(labs,values))
        ctr.append((i+1,sum(bool(x[4]) for x in query(shuffled))))
    write_table(HERE/"cross_controls.tsv",("shuffle","anchored"),ctr)
    write_table(HERE/"cross_inputs.tsv",("sha256","project_relative_path"),[(sha(p),p.relative_to(PROJECT)) for p in (K4,TOK,REF)])
    between=[r[12] for r in rows if r[4]]
    wins=sum(n>=actual for i,n in ctr)
    result={"anchored":actual,"anchored_gaps":between,"full_key_ties_or_wins":wins,
            "pass":actual==2 and len(set(between))==1 and between[0] in ("tt","ct") and wins==0}
    (HERE/"cross_result.json").write_text(json.dumps(result,indent=2)+"\n")
    print(result)
if __name__=="__main__":
    main()
