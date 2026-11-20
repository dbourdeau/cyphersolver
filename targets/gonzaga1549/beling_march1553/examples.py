"""Locate illustrative exact witness matches after the tests; never assign a word."""
import csv
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from calibrate import HERE, REFERENCE, TOKENS, norm, write_table


def main():
    with (HERE / "assignments.tsv").open() as file:
        assignments = list(csv.DictReader(file, delimiter="\t"))
    base = {row["label"]:row["baseline"] for row in assignments}
    fit = {row["label"]:row["fitted"] for row in assignments}
    text = REFERENCE.read_text().split("[37r]\n")[1].replace("[37v]", "").replace("[38r]", "")
    chunks = [s.strip() for s in re.split(r"\n\s*\n", text) if s.strip()]
    pars = [chunks[4]+" "+chunks[5], chunks[6], chunks[7]]
    cipher_lines = dict((int(n), line.split()) for n,line in re.findall(r"^B-(\d+) (.*)$",TOKENS.read_text(),re.M))
    report = []
    for para, ref, (lo,hi) in zip([4,5,6],pars,[(41,47),(48,55),(56,64)]):
        words = [s for s in re.findall(r"[^\W\d_]+",ref) if norm(s)]
        full = norm("".join(words))
        stream = [(line,i,token.rstrip("?").strip("{}")) for line in range(lo,hi+1)
                  for i,token in enumerate(cipher_lines[line],1)]
        fitted = "".join(fit[s] for _,_,s in stream)
        bounds = [0]
        for _,_,label in stream:
            bounds.append(bounds[-1]+len(fit[label]))
        candidates = []
        for a in range(len(words)):
            for b in range(a+3,len(words)+1):
                phrase = " ".join(words[a:b])
                letters = norm(phrase)
                if len(letters) < 8 or full.count(letters)!=1 or fitted.count(letters)!=1:
                    continue
                start = fitted.index(letters)
                stop = start+len(letters)
                if start not in bounds or stop not in bounds:
                    continue
                left = max(i for i,x in enumerate(bounds) if x==start)
                right = bounds.index(stop)
                span = stream[left:right]
                baseline = "".join(base[s] for _,_,s in span)
                if baseline == letters or any(s=="#" for _,_,s in span):
                    continue
                first, last = span[0],span[-1]
                impact = Counter(s for _,_,s in span if fit[s]!=base[s])
                candidates.append((-len(letters),a,first[0],first[1],last[0],last[1],phrase,letters,baseline,
                                   " ".join(s for _,_,s in span)," ".join(sorted(impact))))
        # One longest complete-word span per held-out paragraph. Earliest reference on ties.
        if candidates:
            length,a,l1,j1,l2,j2,p,t,old,signs,changed = min(candidates)
            report.append((para,f"B-{l1:02d}:{j1}",f"B-{l2:02d}:{j2}",a+1,p,t,old,signs,changed))
        else:
            report.append((para,"","","","","","","",""))
    write_table(HERE/"exact_examples.tsv",
                ("paragraph","start_line_token","end_line_token","clear_first_word","contemporary_words","fitted_letters","baseline_letters","raw_labels_cleaned","changed_labels"),
                report)


if __name__ == "__main__":
    main()
