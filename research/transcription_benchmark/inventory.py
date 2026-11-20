"""Phase 0 of the transcription benchmark: list documents that have a human reference transcription.

Reads every targets/*/profile.json (famous targets have none) and writes, next to this file:
  frame.json          one record per document with a human reference
  frame_summary.md    counts per stratum

Run from anywhere:  PYTHONUTF8=1 python research/transcription_benchmark/inventory.py
Read-only on the repository; writes only the two files above.
"""
import collections
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
TARGETS = os.path.join(ROOT, "targets")
HUMAN = {"DECODE", "published", "human (project)"}
IMG = (".jpg", ".jpeg", ".png", ".tif", ".tiff")


def local_images(folder):
    n = 0
    for dirpath, _dirs, files in os.walk(folder):
        n += sum(1 for f in files if f.lower().endswith(IMG))
    return n


def period(year):
    if not isinstance(year, int):
        return "unknown"
    return "pre-1600" if year < 1600 else "1600s" if year < 1700 else "1700s" if year < 1800 else "1800s" if year < 1900 else "1900s"


def main():
    rows = []
    for name in sorted(os.listdir(TARGETS)):
        pj = os.path.join(TARGETS, name, "profile.json")
        if not os.path.isfile(pj):
            continue
        try:
            with open(pj, encoding="utf-8") as fh:
                prof = json.load(fh)
        except (OSError, ValueError):
            continue
        folder = os.path.join(TARGETS, name)
        n_img = local_images(folder)
        kind = (prof.get("system") or {}).get("symbol_kind", "unknown")
        for doc in prof.get("documents", []):
            tr = doc.get("transcription")
            by = tr.get("by") if isinstance(tr, dict) else None
            if by not in HUMAN:
                continue
            length = doc.get("length") or {}
            lfile = length.get("file") if isinstance(length, dict) else None
            rows.append({
                "target": name,
                "doc": doc.get("id"),
                "shelfmark": doc.get("shelfmark"),
                "year": doc.get("year"),
                "period": period(doc.get("year")),
                "language": doc.get("language"),
                "symbol_kind": kind,
                "reference_by": by,
                "reference_source": (tr.get("source") or "")[:160],
                "image_quality": tr.get("image_quality"),
                "tokens": length.get("tokens") if isinstance(length, dict) else None,
                "unit": length.get("unit") if isinstance(length, dict) else None,
                "reference_file": lfile,
                "reference_file_present": bool(lfile) and os.path.isfile(os.path.join(folder, lfile)),
                "images_in_target_folder": n_img,
            })
    with open(os.path.join(HERE, "frame.json"), "w", encoding="utf-8") as fh:
        json.dump(rows, fh, ensure_ascii=False, indent=1)

    def tally(key):
        return collections.Counter(str(r[key]) for r in rows).most_common()

    lines = ["# Transcription benchmark: sampling frame", "",
             f"{len(rows)} documents in {len({r['target'] for r in rows})} targets have a human reference "
             f"(DECODE, published or project).", "",
             f"- reference text file present locally: {sum(r['reference_file_present'] for r in rows)}",
             f"- target folder holds images: {sum(1 for r in rows if r['images_in_target_folder'])}",
             f"- both: {sum(1 for r in rows if r['reference_file_present'] and r['images_in_target_folder'])}", ""]
    for key in ("reference_by", "symbol_kind", "period", "language", "image_quality"):
        lines += [f"## By {key}", ""] + [f"- {k}: {v}" for k, v in tally(key)] + [""]
    with open(os.path.join(HERE, "frame_summary.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    print("documents with a human reference:", len(rows))
    print("targets:", len({r["target"] for r in rows}))
    print("with local reference text:", sum(r["reference_file_present"] for r in rows))
    print("with images in the target folder:", sum(1 for r in rows if r["images_in_target_folder"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
