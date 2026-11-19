"""Phases 3-4 analysis on top of score.py: confusion pairs, and the repeat-attempt curve with a consensus vote.

Usage:  python research/transcription_benchmark/analyze.py <out_dir>
Reads <out_dir>/pass<N>_<doc>.txt, writes analysis.json next to this file.

Confusions: reference digit -> transcribed character for every substitution in the alignment.
Repeat attempts: CER of each single pass, of the best single pass, and of a consensus vote. The vote aligns every pass
to pass 1 (character level, Levenshtein), then for each pass-1 position takes the most common aligned character among
all passes (ties keep the pass-1 character); characters other passes insert, and positions where most passes have a gap,
are dropped. The vote never sees the reference.
Also reported: where passes disagree with each other, how often is the pass-1 character wrong against the reference
(does disagreement predict error?).
"""
import collections
import json
import os
import re
import sys

import score

HERE = os.path.dirname(os.path.abspath(__file__))


def align(a, b):
    """Levenshtein alignment of a (reference) to b. Returns list of (a_char or None, b_char or None)."""
    n, m = len(a), len(b)
    D = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        D[i][0] = i
    for j in range(m + 1):
        D[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            D[i][j] = min(D[i - 1][j - 1] + (a[i - 1] != b[j - 1]), D[i - 1][j] + 1, D[i][j - 1] + 1)
    i, j, out = n, m, []
    while i > 0 or j > 0:
        if i > 0 and j > 0 and D[i][j] == D[i - 1][j - 1] + (a[i - 1] != b[j - 1]):
            out.append((a[i - 1], b[j - 1]))
            i, j = i - 1, j - 1
        elif i > 0 and D[i][j] == D[i - 1][j] + 1:
            out.append((a[i - 1], None))
            i -= 1
        else:
            out.append((None, b[j - 1]))
            j -= 1
    return out[::-1]


def streams(doc, path):
    rl = score.ref_lines(score.REF[doc])
    hl = score.hyp_lines(path)
    al = doc in score.ALNUM_DOCS
    return (score.digits("".join(rl), alnum=al),
            score.digits("".join(l.rstrip("! ") for l in hl), keep_q=True, alnum=al))


def cer(a, b):
    return score.lev_ops(a, b)[3] / len(a)


def vote(base, others):
    cols = [[c] for c in base]
    for o in others:
        al = align(base, o)
        bi = -1
        for x, y in al:
            if x is not None:
                bi += 1
                cols[bi].append(y)  # y may be None (gap)
    out = []
    for col in cols:
        cnt = collections.Counter(col)
        top, n = cnt.most_common(1)[0]
        if top is None:
            continue
        # ties keep the pass-1 character
        best = max(cnt.values())
        out.append(col[0] if cnt[col[0]] == best else top)
    return "".join(out), cols


def main(out_dir):
    files = collections.defaultdict(dict)
    for name in os.listdir(out_dir):
        m = re.match(r"pass(\d+)_(.+)\.txt$", name)
        if m and m.group(2) in score.REF:
            files[m.group(2)][int(m.group(1))] = os.path.join(out_dir, name)
    res = {}
    confusion = collections.Counter()
    for doc, passes in sorted(files.items()):
        ref = score.digits("".join(score.ref_lines(score.REF[doc])), alnum=doc in score.ALNUM_DOCS)
        hyp = {p: streams(doc, f)[1] for p, f in passes.items()}
        entry = {"ref_digits": len(ref), "single": {f"pass{p}": round(cer(ref, h), 4) for p, h in sorted(hyp.items())}}
        for h in hyp.values():
            for x, y in align(ref, h):
                if x is not None and y is not None and x != y:
                    confusion[f"{x}>{y}"] += 1
        if len(hyp) >= 2:
            ps = sorted(hyp)
            base = hyp[ps[0]]
            cons, cols = vote(base, [hyp[p] for p in ps[1:]])
            entry["best_single"] = min(entry["single"].values())
            entry["mean_single"] = round(sum(entry["single"].values()) / len(entry["single"]), 4)
            entry["consensus_cer"] = round(cer(ref, cons), 4)
            entry["passes_used"] = len(ps)
            # does disagreement predict error? compare pass-1 characters against the reference by alignment
            al = align(ref, base)
            refmap, bi = {}, -1
            for x, y in al:
                if y is not None:
                    bi += 1
                    refmap[bi] = x
            dis_err = dis_ok = agr_err = agr_ok = 0
            for k, col in enumerate(cols):
                disagree = len(set(col)) > 1
                wrong = refmap.get(k) != col[0]
                if disagree:
                    dis_err += wrong
                    dis_ok += not wrong
                else:
                    agr_err += wrong
                    agr_ok += not wrong
            entry["disagree_positions"] = dis_err + dis_ok
            entry["error_rate_where_passes_disagree"] = round(dis_err / max(1, dis_err + dis_ok), 4)
            entry["error_rate_where_passes_agree"] = round(agr_err / max(1, agr_err + agr_ok), 4)
            entry["share_of_pass1_errors_caught_by_disagreement"] = round(dis_err / max(1, dis_err + agr_err), 4)
        res[doc] = entry
        print(doc, json.dumps(entry))
    res["_confusions_top20"] = confusion.most_common(20)
    print("top confusions (ref>hyp):", confusion.most_common(12))
    with open(os.path.join(HERE, "analysis.json"), "w", encoding="utf-8") as fh:
        json.dump(res, fh, indent=1)


if __name__ == "__main__":
    main(sys.argv[1])
