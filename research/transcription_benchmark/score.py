"""Phase 3: score blind transcriptions against the human reference (DECODE).

Usage:  python research/transcription_benchmark/score.py <out_dir> [pass names...]
out_dir holds files named <pass>_<doc>.txt written by the blind transcribers ('#page N' headers, one line per
manuscript line, '!' at the end of a flagged line, '?' for an illegible digit).

Metric: the digit stream of the whole document (every non-digit removed from both sides) compared by Levenshtein
distance. character error rate (CER) = edits / reference digits. Substitutions, insertions and deletions are counted
separately from a backtrace. Where the reference separates groups with dots (hellen1752) an exact-group rate is also
given. '?' in a transcription is counted as a substitution (it never matches). The reference itself carries
uncertainty marks and alternatives written by the DECODE transcriber; those are not cleaned, so the reference is noisy
and the CER is an upper bound on the transcription's true error.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
REF = {
    "dandini_R72": "targets/dandini1580/decode/DOC_R72_D1824_1824.txt",
    "hellen_R1049": "targets/hellen1752/decode/DOC_R1049_D1890_1890.txt",
    "santacroce_R6": "targets/santacroce1552/decode/DOC_R6_D1624_1624.txt",
    "santacroce_R7": "targets/santacroce1552/decode/DOC_R7_D1625_1625.txt",
    "hellen_R1953": "targets/hellen1752/decode/DOC_R1953_D3616_3616.txt",
    "kauderbach_R2078": "targets/kauderbach1754/decode/DOC_R2078_D3618_3618.txt",
    "carpio_R1009": "targets/carpio1677/decode/DOC_R1009_D2422_2422.txt",
    "carpio_R1010": "targets/carpio1677/decode/DOC_R1010_D2421_2421.txt",
    "ferdinand_R1889": "targets/ferdinand3/decode/DOC_R1889_D3605_3605.txt",
    "ferdinand_R1890": "targets/ferdinand3/decode/DOC_R1890_D3604_3604.txt",
}
# documents that mix letters and digits are scored on the alphanumeric stream (lower-cased); the rest on digits only
ALNUM_DOCS = {"carpio_R1009", "carpio_R1010", "ferdinand_R1889", "ferdinand_R1890"}
GROUP_DOCS = {"hellen_R1049", "hellen_R1953"}  # reference separates groups with '.'


def ref_lines(path):
    txt = open(os.path.join(ROOT, path), encoding="utf-8-sig", errors="replace").read()
    txt = re.sub(r"<[^>]*>", " ", txt, flags=re.S)  # clear-text and note blocks
    return [l for l in txt.splitlines() if l.strip() and not l.lstrip().startswith("#")]


def hyp_lines(path):
    out = []
    for l in open(path, encoding="utf-8", errors="replace").read().splitlines():
        if l.strip() and not l.startswith("#"):
            out.append(l.rstrip())
    return out


def digits(s, keep_q=False, alnum=False):
    """Digit stream. Reference side drops '?' (the DECODE transcriber's own uncertainty mark); hypothesis side keeps
    it, so an illegible-digit mark counts as an error."""
    if alnum:
        return re.sub(r"[^0-9a-z?]" if keep_q else r"[^0-9a-z]", "", s.lower())
    return re.sub(r"[^0-9?]" if keep_q else r"[^0-9]", "", s)


def lev_ops(a, b):
    """Return (subs, ins, dels) turning reference a into hypothesis b; '?' in b never matches."""
    n, m = len(a), len(b)
    prev = list(range(m + 1))
    back = [bytearray(m + 1) for _ in range(n + 1)]  # 0 diag-match,1 sub,2 del(ref char missing),3 ins
    for j in range(1, m + 1):
        back[0][j] = 3
    for i in range(1, n + 1):
        cur = [i] + [0] * m
        back[i][0] = 2
        ai = a[i - 1]
        for j in range(1, m + 1):
            same = ai == b[j - 1]
            d = prev[j - 1] + (0 if same else 1)
            u = prev[j] + 1
            l = cur[j - 1] + 1
            if d <= u and d <= l:
                cur[j] = d
                back[i][j] = 0 if same else 1
            elif u <= l:
                cur[j] = u
                back[i][j] = 2
            else:
                cur[j] = l
                back[i][j] = 3
        prev = cur
    i, j, s, ins, dl = n, m, 0, 0, 0
    while i > 0 or j > 0:
        op = back[i][j]
        if op in (0, 1):
            s += op
            i, j = i - 1, j - 1
        elif op == 2:
            dl += 1
            i -= 1
        else:
            ins += 1
            j -= 1
    return s, ins, dl, prev[m]


def group_exact(ref_groups, hyp_groups):
    n, m = len(ref_groups), len(hyp_groups)
    # LCS on exact group equality = groups matched exactly in order
    prev = [0] * (m + 1)
    for i in range(1, n + 1):
        cur = [0] * (m + 1)
        for j in range(1, m + 1):
            cur[j] = prev[j - 1] + 1 if ref_groups[i - 1] == hyp_groups[j - 1] else max(prev[j], cur[j - 1])
        prev = cur
    return prev[m]


def score(doc, hyp_path):
    rl = ref_lines(REF[doc])
    hl = hyp_lines(hyp_path)
    al = doc in ALNUM_DOCS
    a = digits("".join(rl), alnum=al)
    b = digits("".join(l.rstrip("! ") for l in hl), keep_q=True, alnum=al)
    s, ins, dl, d = lev_ops(a, b)
    row = {"doc": doc, "ref_digits": len(a), "hyp_digits": len(b), "edits": d, "subs": s, "ins": ins, "dels": dl,
           "cer": round(d / len(a), 4), "ref_lines": len(rl), "hyp_lines": len(hl),
           "flagged_lines": sum(1 for l in hl if l.rstrip().endswith("!")),
           "unreadable_marks": b.count("?")}
    if doc in GROUP_DOCS:
        rg = [g for g in (digits(x) for x in " ".join(rl).split(".")) if g]
        hg = [g for g in (digits(x, keep_q=True) for x in " ".join(l.rstrip("! ") for l in hl).split(".")) if g]
        ok = group_exact(rg, hg)
        row.update({"ref_groups": len(rg), "hyp_groups": len(hg), "groups_exact": ok,
                    "group_exact_rate": round(ok / len(rg), 4)})
    return row


def main(out_dir, passes):
    rows = []
    for name in sorted(os.listdir(out_dir)):
        m = re.match(r"(pass\d+)_(.+)\.txt$", name)
        if not m or (passes and m.group(1) not in passes) or m.group(2) not in REF:
            continue
        r = score(m.group(2), os.path.join(out_dir, name))
        r["pass"] = m.group(1)
        rows.append(r)
        print(json.dumps(r))
    with open(os.path.join(HERE, os.environ.get("SCORES_OUT", "scores.json")), "w", encoding="utf-8") as fh:
        json.dump(rows, fh, indent=1)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2:]))
