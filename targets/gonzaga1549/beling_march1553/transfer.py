"""Document and paired-transcript checks under the frozen transfer plan."""
import csv
import json
import random
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from calibrate import Distance, HERE, HOLE, KEY, NAMES, PROJECT, WAINUT, decoded, distances, norm, sha, write_table


def stripped(token):
    return token.rstrip("?").strip("{}")


def known(key, label):
    return key.get(label, HOLE)


def canonical_value(key, names, label):
    mapped = names.get(label, label)
    if mapped.endswith("_"):
        return ""
    return key.get(mapped, known(key, label))


def main():
    assert sha(HERE/"PLAN_transfer.md") == "a0bcff2ffcef89a942d9d0aa5b1d80fc199fff9b0a2f139aa2431922fa04d268"
    assert sha(HERE/"assignments.tsv") == "96194a7090753441209671470f582981def06ea0617e34feceee3b1675adb5bc"
    with (HERE/"assignments.tsv").open() as file:
        rows = list(csv.DictReader(file, delimiter="\t"))
    changes = {r["label"]:r["fitted"] for r in rows if r["baseline"] != r["fitted"]}
    key = {}
    for line in KEY.read_text().splitlines():
        if line.strip() and not line.startswith("#"):
            name, val = line.split("\t")[:2]
            key[name] = HOLE if "[" in val else norm(val)
    names = json.loads(NAMES.read_text())
    signs = WAINUT/"transcription_ch1549_0930_1120_blind.txt"
    margin = WAINUT/"clear_margins_charles.txt"
    pass1 = WAINUT/"transcription_ch1549_1114.txt"
    pass2 = WAINUT/"transcription_kn14_pass2.txt"
    write_table(HERE/"transfer_inputs.tsv", ("sha256","path_from_project"),
                [(sha(p), p.relative_to(PROJECT)) for p in (signs, margin, pass1, pass2, KEY, NAMES)])
    documents, references = [], []
    for group, ref in [("K","M"),("N","N")]:
        tokens = [stripped(t) for line in signs.read_text().splitlines() if line.startswith(group+"-")
                  for t in line.split()[1:]]
        text = norm(" ".join(line.split(" ", 1)[1] for line in margin.read_text().splitlines() if re.match(ref+r"\d", line)))
        documents.append(tokens)
        references.append(text)
    eligible = [r["label"] for r in rows if r["eligible"] == "1"]
    counts = {r["label"]:int(r["training_n"]) for r in rows}
    strata = [[s for s in eligible if lo <= counts[s] < hi] for lo, hi in [(5,10), (10,20), (20,10**9)]]
    active = set(documents[0]) | set(documents[1])
    base = {label:canonical_value(key, names, label) for label in active | set(eligible)}
    fit = dict(base, **changes)
    metrics = list(map(Distance, references))
    bd, fd = distances(base, documents, metrics), distances(fit, documents, metrics)
    labels = sorted(s for s in active if fit[s] not in {HOLE, ""})
    values = [fit[s] for s in labels]
    full_rng, diff_rng = random.Random(15490930), random.Random(15491120)
    controls = []
    for i in range(1000):
        perm = values[:]
        full_rng.shuffle(perm)
        full = dict(fit)
        full.update(zip(labels, perm))
        redistributed = dict(base)
        for stratum in strata:
            dest = stratum[:]
            diff_rng.shuffle(dest)
            for label, d in zip(stratum, dest):
                if label in changes:
                    redistributed[d] = changes[label]
        controls.append((i+1, sum(distances(full, documents, metrics)), sum(distances(redistributed, documents, metrics))))
    write_table(HERE/"transfer_controls.tsv", ("shuffle","full_key_edits","redistributed_corrections_edits"), controls)
    details = [(name, len(seq), len(ref), sum(label in changes for label in seq), d, f, (d-f)/len(ref))
               for name,seq,ref,d,f in zip(["1549-09-30","1549-11-20"],documents,references,bd,fd)]
    write_table(HERE/"transfer_documents.tsv", ("document","raw_tokens","reference_letters","changed_label_occurrences","baseline_edits","corrected_edits","CER_gain"), details)
    nw = sum(len(r) for r in references)
    gain = (sum(bd) - sum(fd)) / nw
    kw = sum(r[1] <= sum(fd) for r in controls)
    cw = sum(r[2] <= sum(fd) for r in controls)
    summary = {"baseline_edits":sum(bd), "corrected_edits":sum(fd), "reference_letters":nw,
               "CER_gain":gain,"shuffled_key_ties_or_wins":kw,"relocated_corrections_ties_or_wins":cw,
               "best_full_key_edits":min(r[1] for r in controls),"best_relocated_corrections_edits":min(r[2] for r in controls),
               "pass":all(d > f for d,f in zip(bd,fd)) and gain>=.025 and kw==0 and cw<=9}
    (HERE/"transfer_result.json").write_text(json.dumps(summary, indent=2)+"\n")
    print("document check", summary)

    first = {r[0]:r[1:] for line in pass1.read_text().splitlines() if re.match(r"^[A-D]\d\d ",line) for r in [line.split()]}
    second = {int(r[0][3:]):r[1:] for line in pass2.read_text().splitlines() if line.startswith("P2-") for r in [line.split()]}
    excluded = {"A17","B25","C19","C29","D15","D16","D19","D21"}
    pairs, ledger = [], []
    for lo, hi, letter, offset in [(1,12,"A",7),(13,40,"B",-12),(41,69,"C",-40),(70,92,"D",-69)]:
        for n in range(lo, hi+1):
            line = f"{letter}{n+offset:02d}"
            p,q = first[line],second[n]
            pairs.append((line, "P2-%02d"%n, len(p), len(q), int(line in excluded)))
            for j,token in enumerate(q):
                label = stripped(token)
                if label not in changes:
                    continue
                reason = ""
                if line in excluded:
                    reason = "upstream_revised_line"
                elif len(p) != len(q):
                    reason = "unequal_line_length"
                elif j==0 or j==len(q)-1:
                    reason = "line_edge"
                elif token.endswith("?") or p[j].endswith("?"):
                    reason = "uncertain_center"
                elif any(t.endswith("?") for t in (q[j-1],q[j+1],p[j-1],p[j+1])):
                    reason = "uncertain_flank"
                elif any((names.get(stripped(q[k]),stripped(q[k])) != stripped(p[k]) or stripped(p[k]) in {"","#","?"}) for k in (j-1,j+1)):
                    reason = "flanks_disagree"
                observed = None if reason else known(key,stripped(p[j]))
                if not reason and (observed in {"",HOLE} or stripped(p[j]).endswith("_")):
                    reason = "reference_unvalued"
                original = canonical_value(key,names,label)
                winner = "" if reason else "baseline" if original==observed else "correction" if changes[label]==observed else "neither"
                ledger.append((line,n,j+1,label,original,changes[label],p[j] if not reason else "",observed if not reason else "",reason,winner))
    write_table(HERE/"paired_lines.tsv", ("pass1_line","pass2_line","pass1_n","pass2_n","upstream_changed"),pairs)
    write_table(HERE/"paired_positions.tsv", ("pass1_line","pass2_line_no","pass2_position","raw_label","baseline","fitted","pass1_label","reference_emission","ineligible_reason","matching_emission"),ledger)
    print("paired diagnostic",dict(Counter(row[-1] or row[-2] for row in ledger)))

if __name__ == "__main__":
    main()
