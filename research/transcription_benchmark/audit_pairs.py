"""Phase 1b: for each sampled document list the files whose names match its id (candidate reference text and page images).

Run:  PYTHONUTF8=1 python research/transcription_benchmark/audit_pairs.py
The frame's reference_file and images_in_target_folder were too loose (a measuring script, article figures, icons), so
the usable set is decided document by document from this listing and then recorded in usable.json by hand.
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
with open(os.path.join(HERE, "sample.json"), encoding="utf-8") as fh:
    sample = json.load(fh)["documents"]
for r in sample:
    t = os.path.join(ROOT, "targets", r["target"])
    d = str(r["doc"])
    key = re.sub(r"^DECODE ", "", d).lower()
    num = re.sub(r"\D", "", key)
    hits = []
    for dp, _dirs, fs in os.walk(t):
        if "icons" in dp:
            continue
        for f in fs:
            fl = f.lower()
            if not fl.endswith((".txt", ".png", ".jpg", ".jpeg")):
                continue
            if key in fl or (len(num) >= 2 and re.search(r"(^|[^0-9])r?" + num + r"([^0-9]|$)", fl)):
                hits.append(os.path.relpath(os.path.join(dp, f), t).replace(os.sep, "/"))
    print(r["target"], d, "|", len(hits), hits[:6])
