"""Phase 1 of the transcription benchmark: draw the sample from frame.json, deterministically.

Only documents with the reference text present locally AND images in the target folder are eligible (113 at the time of
writing). The draw is stratified by symbol kind, then spread over period and reference source, at most 2 documents per
target, fixed seed. Writes sample.json and sample_summary.md next to this file.

Run:  PYTHONUTF8=1 python research/transcription_benchmark/sample.py
Commit sample.json BEFORE running any transcription, so the choice cannot be accused of cherry-picking.
"""
import collections
import json
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SEED = 20261117
SIZE = 48
MAX_PER_TARGET = 2
MIN_TOKENS = 50  # unknown token counts are allowed; known ones below this are too short to score
# quota per group of symbol kinds
GROUPS = {
    "digits": ({"digits"}, 20),
    "letters": ({"letters", "digits and letters"}, 14),
    "symbols": ({"symbols", "digits and symbols", "letters and symbols"}, 14),
}


def main():
    with open(os.path.join(HERE, "frame.json"), encoding="utf-8") as fh:
        frame = json.load(fh)
    pool = [r for r in frame
            if r["reference_file_present"] and r["images_in_target_folder"]
            and (r["tokens"] is None or r["tokens"] >= MIN_TOKENS)]
    rng = random.Random(SEED)
    chosen, per_target = [], collections.Counter()
    shortfall = {}
    for gname, (kinds, quota) in GROUPS.items():
        cand = [r for r in pool if r["symbol_kind"] in kinds]
        rng.shuffle(cand)
        # round-robin over (period, reference_by) cells so no cell dominates
        cells = collections.defaultdict(list)
        for r in cand:
            cells[(r["period"], r["reference_by"])].append(r)
        order = sorted(cells)
        picked = []
        while len(picked) < quota and any(cells.values()):
            for cell in order:
                while cells[cell]:
                    r = cells[cell].pop()
                    if per_target[r["target"]] < MAX_PER_TARGET:
                        per_target[r["target"]] += 1
                        r = dict(r, group=gname)
                        picked.append(r)
                        break
                if len(picked) >= quota:
                    break
        shortfall[gname] = quota - len(picked)
        chosen += picked
    chosen.sort(key=lambda r: (r["group"], r["target"], str(r["doc"])))
    with open(os.path.join(HERE, "sample.json"), "w", encoding="utf-8") as fh:
        json.dump({"seed": SEED, "size": len(chosen), "pool": len(pool), "documents": chosen}, fh,
                  ensure_ascii=False, indent=1)
    lines = ["# Transcription benchmark: sample", "",
             f"Seed {SEED}. Pool {len(pool)} eligible documents (reference text and images both on hand); "
             f"{len(chosen)} drawn, at most {MAX_PER_TARGET} per target.", ""]
    if any(shortfall.values()):
        lines += ["Shortfall against quota: " + ", ".join(f"{k} {v}" for k, v in shortfall.items() if v), ""]
    for key in ("group", "period", "reference_by", "language", "image_quality"):
        lines += [f"## By {key}", ""]
        lines += [f"- {k}: {v}" for k, v in collections.Counter(str(r[key]) for r in chosen).most_common()] + [""]
    lines += ["## Documents", ""]
    lines += [f"- {r['group']} | {r['target']} | {r['doc']} | {r['year']} | {r['language']} | {r['reference_by']} | "
              f"{r['tokens']} {r['unit'] or ''}" for r in chosen]
    with open(os.path.join(HERE, "sample_summary.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    print("pool", len(pool), "drawn", len(chosen), "shortfall", shortfall)
    return 0


if __name__ == "__main__":
    sys.exit(main())
