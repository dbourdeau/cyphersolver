#!/usr/bin/env python3
"""Reproduce the Mantua 1524 key output from the three transcriptions and key.json, check it
against reading-words.tsv, enforce the tier rules and print the counts. Standard library only.

    python3 targets/mantua1524/aaymeloglu/verify.py        # exit 1 on any mismatch or rule violation

For every cipher or raised segment (one transcription row):
- the units are the signs with the pairs in key.json `_merges` joined (left to right), transcriber
  alternatives `x{y}?` taken as x, points dropped;
- the key output is each unit's value, or [unit] for a code sign or a sign with no value;
- units and key output must equal the `units` and `key_output` columns of reading-words.tsv.

A segment graded `strict` must have: no transcriber alternative in its row; no code sign; every
unit with a value of confidence A or B (at least two independently secure supporting words);
and a reading that spells the key output exactly, ignoring case, spacing, apostrophes, hyphens,
accents and u/v. An `unread` segment has no reading outside [brackets]. All values are grade S
(CONVENTIONS.md section 1): there is no key sheet or contemporary decipherment.
"""
import collections
import csv
import json
import os
import re
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
FILES = ["transcription-298.tsv", "transcription-68r.tsv", "transcription-198r.tsv"]
CODE = {"BOX", "IZ", "H", "CROSS", "C@"}
RESERVED = {("68r", "20"), ("68r", "21"), ("68r", "22"), ("68r", "23")}
TIERS = ["strict", "forced", "lenient", "doubt", "unread"]


def rows(name):
    with open(os.path.join(HERE, name), newline="") as f:
        lines = [l for l in f if not l.startswith("#")]
    return list(csv.DictReader(lines, delimiter="\t"))


def units(text, merges):
    t = [x.split("{")[0].rstrip("?") for x in text.split() if x != "."]
    out, i = [], 0
    while i < len(t):
        if i + 1 < len(t) and (t[i], t[i + 1]) in merges:
            out.append(t[i] + t[i + 1])
            i += 2
        else:
            out.append(t[i])
            i += 1
    return out


def norm(s):
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z]", "", s.replace("v", "u"))


def main():
    key = json.load(open(os.path.join(HERE, "key.json")))
    merges = {(p[0], p[1:]) for p in key["_merges"].split(",")}
    val = {s: d.get("value") for s, d in key.items() if not s.startswith("_")}
    conf = {s: d.get("confidence") for s, d in key.items() if not s.startswith("_")}
    for s, d in key.items():
        if not s.startswith("_") and d.get("value") and d.get("grade") != "S":
            sys.exit(f"key.json: {s} has grade {d.get('grade')!r}; every value here is S")

    words = {(r["leaf"], r["line"], r["seq"]): r for r in rows("reading-words.tsv")}
    errors, seen = [], set()
    counts = collections.defaultdict(collections.Counter)
    for name in FILES:
        for r in rows(name):
            if r["kind"] not in ("cipher", "raised"):
                continue
            k = (r["leaf"], r["line"], r["seq"])
            where = f"{name} {'.'.join(k)}"
            seen.add(k)
            u = units(r["text"], merges)
            out = "".join(val[x] if x not in CODE and val.get(x) else f"[{x}]" for x in u)
            w = words.get(k)
            if w is None:
                errors.append(f"{where}: missing from reading-words.tsv")
                continue
            if w["units"] != " ".join(u):
                errors.append(f"{where}: units {' '.join(u)!r} != tsv {w['units']!r}")
            if w["key_output"] != out:
                errors.append(f"{where}: key output {out!r} != tsv {w['key_output']!r}")
            tier = w["tier"]
            if tier not in TIERS:
                errors.append(f"{where}: unknown tier {tier!r}")
            if tier == "strict":
                if "{" in r["text"]:
                    errors.append(f"{where}: strict but the row has a transcriber alternative")
                if any(x in CODE for x in u):
                    errors.append(f"{where}: strict but contains a code sign")
                weak = [x for x in u if x not in CODE and conf.get(x) not in ("A", "B")]
                if weak:
                    errors.append(f"{where}: strict but {weak} lack two independent supporting words")
                if norm(w["reading"]) != norm(out):
                    errors.append(f"{where}: strict reading {w['reading']!r} does not spell {out!r}")
            if tier == "unread" and norm(re.sub(r"\[[^\]]*\]", "", w["reading"])):
                errors.append(f"{where}: unread segment has a reading outside [brackets]")
            part = "reserved" if k[:2] in RESERVED else r["leaf"]
            counts[part][tier] += 1
    for k in words:
        if k not in seen:
            errors.append(f"reading-words.tsv {'.'.join(k)}: no such segment in the transcriptions")

    print("segments by tier (a segment is one transcription row; it may be part of a word or several words)")
    print(f"{'part':<10}" + "".join(f"{t:>9}" for t in TIERS) + f"{'total':>8}")
    total = collections.Counter()
    for part in ("298r", "298v", "68r", "198r", "reserved"):
        c = counts[part]
        if part != "reserved":
            total.update(c)
        print(f"{part:<10}" + "".join(f"{c[t]:>9}" for t in TIERS) + f"{sum(c.values()):>8}")
    print(f"{'all but reserved':<10}" + "".join(f"{total[t]:>9}" for t in TIERS) + f"{sum(total.values()):>8}")
    print("grades: every keyed value is S; no H or C")
    if errors:
        print(f"\n{len(errors)} problem(s):")
        for e in errors:
            print("  " + e)
        sys.exit(1)
    print("ok: key output and tiers reproduce")


if __name__ == "__main__":
    main()
