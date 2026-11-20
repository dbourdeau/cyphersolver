"""Compare masked sign contexts to complete words in separately transcribed plaintext."""
import argparse
import csv
import hashlib
import json
import random
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
options=argparse.ArgumentParser(description=__doc__)
options.add_argument("--targets", type=Path, required=True, help="repository targets directory")
options.add_argument("--march", type=Path, required=True, help="published March working transcript spanish_enclosure.txt")
options.add_argument("--output", type=Path, required=True, help="existing empty output directory")
args=options.parse_args()
FIG=args.targets/"figueroa1534"
GONZ=args.targets/"gonzaga1549"
KEY=FIG/"validation/K4.tsv"
MARCH=args.march
OUT=args.output

def norm(s):
    letters = unicodedata.normalize("NFKD",s.lower())
    return re.sub("[^a-z]","",letters).replace("j","i").replace("v","u")

def table(name, fields, rows):
    with (OUT/name).open("w",newline="") as out:
        writer=csv.writer(out,delimiter="\t",lineterminator="\n")
        writer.writerow(fields)
        writer.writerows(rows)

def clear_words(paths):
    words=defaultdict(set)
    for f in paths:
        for line in f.read_text().splitlines():
            if line.startswith(("#","Modena,")):
                continue
            line=re.sub(r"\[[^]]*\]"," ",line)
            line=re.sub(r"^([MN]\d+[a-z]?|\d+)\s+","",line)
            for word in re.findall(r"[^\W\d_]+",line):
                word=norm(word)
                if len(word)>=6:
                    words[word].add(f.name)
    return words

def contexts(files):
    loci=[]
    observed=set()
    for f in files:
        pages=defaultdict(list)
        for line in f.read_text().splitlines():
            if not line.startswith("P"):
                continue
            name,*tokens=line.partition(" #")[0].split()
            for j,token in enumerate(tokens,1):
                observed.add(token)
                pages[name.split("L")[0]].append((name,j,token))
        for page in pages.values():
            tokens=[row[2] for row in page]
            for i,(ln,j,token) in enumerate(page):
                if token=="+":
                    loci.append((f.stem,ln,j,tokens[:i],tokens[i+1:]))
    return observed,loci

def main():
    clear=[FIG/"validation/clear_1547_ref_img06.txt",FIG/"validation/img04/clear_1547_ref_img04_joined.txt",
           *sorted((GONZ/"wainut").glob("clear*.txt")),GONZ/"mcbratney_27may1549/27may1549_decipherment_12r.txt",MARCH]
    cipher=sorted((FIG/"transcriptions").glob("1383_*.txt"))
    words=clear_words(clear)
    assert len(clear)==9 and len(cipher)==5
    candidates=defaultdict(list)
    for word in sorted(words):
        for left in range(2,len(word)-1):
            for size in range(4):
                right=len(word)-size-left
                if right>=2 and left+right>=5:
                    candidates[(word[:left],word[left+size:])].append((word,word[left:left+size]))
    lengths=sorted({(len(a),len(b)) for a,b in candidates},key=lambda x: (sum(x),x),reverse=True)
    maxlen=max(len(w) for w in words)
    seen,loci=contexts(cipher)
    mapping={}
    for row in csv.DictReader((s for s in KEY.read_text().splitlines() if not s.startswith("#")),delimiter="\t"):
        val=row["valeur"].split("|")[0]
        mapping.setdefault(row["label"],"" if val=="NUL" else norm(val) or "?")
    mapping["+"]="?"
    active=sorted(s for s in seen if mapping.get(s) not in ("?",None,""))
    # A context needs at most the longest word in nonempty or unknown tokens on each side.
    compact=[]
    for doc,line,pos,left,right in loci:
        compact.append((doc,line,pos,[s for s in left if mapping.get(s)!=""][-maxlen:],
                        [s for s in right if mapping.get(s)!=""][:maxlen]))
    def query(key,detail=False):
        output=[]
        support=defaultdict(set)
        docs=defaultdict(set)
        for doc,line,pos,lft,rgt in compact:
            left="".join(key.get(l,"?") for l in lft)
            right="".join(key.get(l,"?") for l in rgt)
            found=set()
            best=0
            for m,n in lengths:
                if m+n<best:
                    break
                if len(left)<m or len(right)<n:
                    continue
                matches=candidates.get((left[-m:],right[:n]))
                if matches:
                    best=m+n
                    found.update(matches)
            variants={gap for _,gap in found}
            if len(variants)==1:
                v=next(iter(variants))
                support[v].update(w for w,_ in found)
                docs[v].add(doc)
            if detail:
                output.append((doc,line,pos,left[-maxlen:],right[:maxlen],best,
                              " | ".join(f"{w} [{g}] ({', '.join(sorted(words[w]))})" for w,g in sorted(found))))
        return support,docs,output
    empirical,documents,rows=query(mapping,True)
    rng=random.Random(1383351)
    controls=[]
    for k in range(1,1001):
        values=[mapping[s] for s in active]
        rng.shuffle(values)
        shuffled=dict(mapping)
        shuffled.update(zip(active,values))
        support,_,_=query(shuffled)
        controls.append((k,len(support["tt"]),len(support["ct"])))
    best=max(max(a,b) for _,a,b in controls)
    passed=any(len(empirical[a])>=2 and len(documents[a])>=2 and not empirical[b] and len(empirical[a])>best
               for a,b in [("ct","tt"),("tt","ct")])
    table("lexicon_inputs.tsv",["path","sha256"],((p.name,hashlib.sha256(p.read_bytes()).hexdigest())
                                                   for p in [KEY,*clear,*cipher]))
    table("lexicon_loci.tsv",["document","line","position","left","right","known_letters","best_glossary_matches"],rows)
    table("lexicon_controls.tsv",["permutation","tt_words","ct_words"],controls)
    report=dict(loci=len(loci),documents={p.stem:sum(x[0]==p.stem for x in loci) for p in cipher},
                glossary_words=len(words),matched_loci=sum(bool(row[-1]) for row in rows),
                observed={s:sorted(v) for s,v in empirical.items()},best_control=best,
                controls_tie_or_better=sum(max(a,b)>=max(len(empirical["ct"]),len(empirical["tt"])) for _,a,b in controls),
                passed=passed)
    (OUT/"lexicon_result.json").write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report))
if __name__=="__main__":
    main()
