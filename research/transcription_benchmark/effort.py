"""Check 3: human transcription time (from the DECODE headers) against AI transcription time.

Human: '#TRANSCRIPTION TIME' in each DECODE reference (two ferdinand files have the time under '#DATE OF
TRANSCRIPTION'; the field holding a duration is taken). AI: wall-clock of the Sonnet 5.5 transcription subagents of
this session, from the task notifications (each agent read two documents; its time is split between them by reference
length). Opus and Fable timings were not recorded in this session, and hellen R1953 / kauderbach were transcribed in
another session, so they have no AI time here. Token counts per agent were about 100,000 to 125,000.
Writes effort.json.
"""
import json
import os
import re

import score

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
# Sonnet agent wall-clock seconds per pass, (doc_a, doc_b): [pass1, pass2, pass3]; source: task notifications 19 Nov
AGENTS = {("dandini_R72", "hellen_R1049"): [70.9, 102.7, 106.9],
          ("santacroce_R6", "santacroce_R7"): [89.3, 113.0, 111.3],
          ("carpio_R1009", "carpio_R1010"): [63.1, 60.8, 65.4],
          ("ferdinand_R1889", "ferdinand_R1890"): [78.1, 82.6, 78.2]}


def minutes(s):
    s = s.replace(" ", "")
    if "=" in s:
        s = s.split("=")[-1]
    h = re.search(r"(\d+)h", s)
    m = re.search(r"(\d+)min", s)
    if h or m:
        return (int(h.group(1)) * 60 if h else 0) + (int(m.group(1)) if m else 0)
    nums = [int(x) for x in re.findall(r"\d+", s)]
    return max(nums) if nums else None  # e.g. '30+30?60 mins' -> 60


def main():
    out, tot_h, tot_ai, tot_h_timed = {}, 0, 0.0, 0
    lengths = {d: len(score.digits("".join(score.ref_lines(p)), alnum=d in score.ALNUM_DOCS)) for d, p in score.REF.items()}
    ai = {}
    for (a, b), secs in AGENTS.items():
        for d in (a, b):
            share = lengths[d] / (lengths[a] + lengths[b])
            ai[d] = round(sum(secs) / len(secs) * share, 1)
    for d, p in score.REF.items():
        t = open(os.path.join(ROOT, p), encoding="utf-8-sig", errors="replace").read()
        fields = dict(re.findall(r"^#\s*(TRANSCRIPTION TIME|DATE OF TRANSCRIPTION|TRANSCRIPTION METHOD)\s*:\s*(.*)$", t, flags=re.M))
        raw = fields.get("TRANSCRIPTION TIME", "")
        if not re.search(r"h|min", raw):
            raw = fields.get("DATE OF TRANSCRIPTION", raw)  # swapped fields in the ferdinand headers
        mins = minutes(raw)
        out[d] = {"signs": lengths[d], "human_minutes": mins, "human_raw": raw.strip(),
                  "human_method": fields.get("TRANSCRIPTION METHOD", "").strip(), "sonnet_seconds_per_pass": ai.get(d)}
        tot_h += mins or 0
        if d in ai:
            tot_ai += ai[d]
            tot_h_timed += mins or 0
        print(f"{d:18s} {lengths[d]:5d} signs  human {mins:4d} min ({raw.strip()})  AI {ai.get(d, '-')} s per pass")
    print(f"total human time, 10 documents: {tot_h} min ({tot_h / 60:.1f} h)")
    print(f"8 documents with an AI time: human {tot_h_timed} min, AI {tot_ai / 60:.1f} min per pass, "
          f"ratio about {tot_h_timed * 60 / tot_ai:.0f}x")
    json.dump(out, open(os.path.join(HERE, "effort.json"), "w"), indent=1)


if __name__ == "__main__":
    main()
