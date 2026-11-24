"""Second round, step 4: blind transcription prompts for the drawn sample, batched (~35 tiles per agent).

  python prompts2.py TILE_DIR OUT_DIR -> frame2/batches2.json (one prompt per batch; same rules as round one, with one
                                         generic description per stratum so no prompt carries reference content)
"""
import collections
import json
import os
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
F2 = HERE / "frame2"
DIGIT = ("The pages hold cipher numerals (digits), written in groups that may be separated by dots, colons, spaces or "
         "nothing, possibly with marks over or under them, and usually some ordinary words (a heading, a date, a "
         "signature, whole sentences in clear text). Write only the digits.")
LETTER = ("The pages hold a cipher written with letters and/or digits (cipher letters, numbers, letters with small "
          "numbers beside or above them), usually mixed with ordinary words in clear text. Write every cipher sign: "
          "digits and letters, in order, with a superscript or small number written straight after its letter. Skip "
          "the clear text.")


def main(tiles, out):
    pages = json.load(open(F2 / "pages2.json"))
    names = sorted(os.listdir(tiles))
    per = collections.defaultdict(lambda: collections.defaultdict(list))
    for n in names:
        m = re.match(r"(R\d+)_p(\d+)_t(\d+)\.jpg$", n)
        per[m.group(1)][int(m.group(2))].append(int(m.group(3)))
    docs = sorted(per, key=lambda d: int(d[1:]))
    batches, cur, size = [], [], 0
    for d in docs:
        n = sum(len(v) for v in per[d].values())
        if cur and size + n > 38:
            batches.append(cur)
            cur, size = [], 0
        cur.append(d)
        size += n
    batches.append(cur)
    out_batches = []
    for bi, b in enumerate(batches, 1):
        lines = []
        for k, d in enumerate(b, 1):
            pl = ", ".join(f"p{p} (t1..t{max(t)})" for p, t in sorted(per[d].items()))
            desc = LETTER if pages[d]["stratum"] == "letter" else DIGIT
            lines.append(f" {k}. {d}: pages {pl}; files {d}_p<page>_t<tile>.jpg, top to bottom. {desc}")
        files = ", ".join(f"{out}/pass1_{d}.txt" for d in b)
        prompt = f"""You are doing a blind transcription of handwritten cipher text from page-image tiles. Accuracy matters more than speed.

INPUT: image tiles in {tiles}/ . You handle exactly these {len(b)} documents, in this order, reading each tile with the Read tool (it shows images):
{chr(10).join(lines)}
Consecutive tiles of a page overlap by about 90 pixels, so the first line of a tile may repeat the last line of the previous tile: do NOT transcribe a line twice. Some tiles are blank or hold only margin, address or clear text: say so and move on.

WHAT TO TRANSCRIBE: only the cipher signs described for each document. IGNORE ordinary words, signatures, page numbers, stamps, marginal notes and clear-text prose. Copy what is written, sign by sign. Do not correct, guess a 'sensible' value, or smooth anything. If a sign is genuinely illegible write ? in its place. Mark a line with a trailing ' !' ONLY if you are really unsure about a sign in it (most lines should have no flag). Separate groups with a single space. One output line per manuscript line, in reading order. Use plain ASCII only (no zero-width or other invisible characters).

OUTPUT: write plain-text files with the Write tool (create the folder if needed): {files}. Format: a line '#page N' before each page's lines, then the cipher lines. Write each file as soon as its document is finished (do not hold everything to the end).

RULES: Use ONLY the tile images above. Do not look at, list, search or read anything else on this computer (no repository, no other folders, no web, and no other files in the output folder): the point is a blind, independent test and any other source would invalidate it. Do not reread tiles to 'improve' a line you have already written beyond one careful look. When all files are written, reply with: the file paths, the number of lines written per page, and your model ID."""
        out_batches.append({"batch": bi, "docs": b, "tiles": sum(len(t) for d in b for t in per[d].values()),
                            "prompt": prompt})
    json.dump(out_batches, open(F2 / "batches2.json", "w"), indent=1)
    print(len(out_batches), "batches:", [(x["batch"], len(x["docs"]), x["tiles"]) for x in out_batches])


if __name__ == "__main__":
    main(sys.argv[1].rstrip("/"), sys.argv[2].rstrip("/"))
