"""Phase 5: does the transcription error matter downstream? Santacroce R6 and R7 (the only documents here whose key is
established and whose decoder runs on a bare digit stream).

For each document the SAME decoder (targets/santacroce1552/decode.py: Lasry's reconstructed key, beam-search
segmentation under the it-cinquecento language model) is run on
  - the human digit stream (DECODE transcription with every mark removed),
  - each of the three blind AI passes (digit streams),
  - the three-pass consensus vote (analyze.vote),
  - CONTROL: the human stream with random substitutions, insertions and deletions injected at each AI pass's own error
    counts (n_draws draws per pass). A transcription error of the AI that is no worse than random errors of the same
    size would show the same damage.
Dotted nomenclator marks are not in any stream, so nomenclator elements decode as letters in all of them alike; what is
compared is how far each reading's plaintext departs from the human-stream plaintext, and how readable it is.

Metrics per reading:
  plain_cer  = Levenshtein distance between the letters of its plaintext and the human-stream plaintext, divided by
               the human-stream plaintext length
  lm_per_char = mean per-character log-probability of its plaintext under it-cinquecento (higher = more like Italian)

Run (slow, minutes):  PYTHONUTF8=1 python research/transcription_benchmark/downstream.py <passes_dir> [n_draws]
Writes downstream.json next to this file.
"""
import importlib.util
import json
import os
import random
import re
import statistics
import sys

import analyze
import score

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
DOCS = ["santacroce_R6", "santacroce_R7"]


def load_decoder():
    path = os.path.join(ROOT, "targets", "santacroce1552", "decode.py")
    sys.path.insert(0, os.path.join(ROOT, "targets"))
    spec = importlib.util.spec_from_file_location("sc_decode", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


DEC = load_decoder()
_cache = {}


def decode_stream(digits):
    """Plaintext of a digit stream: '1' is the null/separator (as in decode.py); each run between nulls is segmented."""
    if digits in _cache:
        return _cache[digits]
    out = []
    for run in digits.split("1"):
        if run:
            out.append(DEC.segment(run.replace("?", "x")))
    txt = " ".join(out)
    _cache[digits] = txt
    return txt


def letters(txt):
    return re.sub(r"[^a-z]", "", txt.lower())


def plain_cer(a, ref):
    ra, rb = letters(ref), letters(a)
    return score.lev_ops(ra, rb)[3] / max(1, len(ra))


def lm_per_char(txt):
    t = re.sub(r"\{[^}]*\}", "", txt.lower())
    t = re.sub(r"[^a-z ]", "", t)
    return DEC.M.per_char(t)


def perturb(stream, subs, ins, dels, rng):
    s = list(stream)
    n = len(s)
    for _ in range(dels):
        if s:
            del s[rng.randrange(len(s))]
    for _ in range(subs):
        i = rng.randrange(len(s))
        s[i] = rng.choice([c for c in "0123456789" if c != s[i]])
    for _ in range(ins):
        s.insert(rng.randrange(len(s) + 1), rng.choice("0123456789"))
    return "".join(s)


def main(pdir, n_draws=5):
    rng = random.Random(20261119)
    res = {}
    for doc in DOCS:
        ref = score.digits("".join(score.ref_lines(score.REF[doc])))
        hum = decode_stream(ref)
        entry = {"human_lm_per_char": round(lm_per_char(hum), 4), "human_plain_letters": len(letters(hum)), "readings": {}}
        hyps, rows = {}, {}
        for p in (1, 2, 3):
            f = os.path.join(pdir, f"pass{p}_{doc}.txt")
            hyps[p] = analyze.streams(doc, f)[1]
            rows[p] = score.score(doc, f)
        cons, _ = analyze.vote(hyps[1], [hyps[2], hyps[3]])
        for name, st in [(f"pass{p}", hyps[p]) for p in (1, 2, 3)] + [("consensus", cons)]:
            pt = decode_stream(st)
            entry["readings"][name] = {"digit_cer": round(score.lev_ops(ref, st.replace("?", "x"))[3] / len(ref), 4),
                                       "plain_cer": round(plain_cer(pt, hum), 4),
                                       "lm_per_char": round(lm_per_char(pt), 4)}
            print(doc, name, entry["readings"][name], flush=True)
        ctrl = []
        for p in (1, 2, 3):
            r = rows[p]
            for _ in range(n_draws):
                st = perturb(ref, r["subs"], r["ins"], r["dels"], rng)
                pt = decode_stream(st)
                ctrl.append({"digit_cer": round(r["cer"], 4), "plain_cer": plain_cer(pt, hum), "lm_per_char": lm_per_char(pt)})
        entry["random_control"] = {
            "draws": len(ctrl),
            "mean_digit_cer": round(statistics.mean(c["digit_cer"] for c in ctrl), 4),
            "mean_plain_cer": round(statistics.mean(c["plain_cer"] for c in ctrl), 4),
            "sd_plain_cer": round(statistics.pstdev(c["plain_cer"] for c in ctrl), 4),
            "mean_lm_per_char": round(statistics.mean(c["lm_per_char"] for c in ctrl), 4)}
        print(doc, "control", entry["random_control"], flush=True)
        res[doc] = entry
    with open(os.path.join(HERE, "downstream.json"), "w", encoding="utf-8") as fh:
        json.dump(res, fh, indent=1)


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 5)
