"""Independent second sign pass: a separate AI language-model agent transcribes each cipher line from a tight band
image. It gets no key, no decipherment and no clear text, only a sign legend. Output: validation/pass2_raw.txt
usage: pass2_blind.py IMG OUTDIR
The model call goes through a local helper that is not included: set PASS2_HELPER_DIR to the folder holding a module
llm_direct with ask(provider, model, prompt, image_b64=..., max_tokens=...) -> (text, usage), and set PASS2_PROVIDER
and PASS2_MODEL.
"""
import sys, os, io, base64, json
sys.path.insert(0, os.environ.get("PASS2_HELPER_DIR", "."))
from llm_direct import ask
from PIL import Image, ImageOps

CENTRES = [100, 335, 600, 875, 1120, 1395, 1690, 1960, 2190, 2460, 2790, 3045, 3300, 3575]
HH = 88
PROMPT = """This image shows ONE line of a 17th-century numeric cipher, cut into three overlapping pieces stacked top to bottom (read piece 1, then 2, then 3; the pieces overlap by a few signs, so do not repeat the overlapping signs).
Transcribe ONLY the cipher signs, left to right, separated by single spaces. Rules:
- digits 0-9 as written (in this hand 2 looks like a hooked 'r', 5 may look like a long 's' with a tail, 1 may look like an i with a dot);
- write W for a sign shaped like a small omega or lying 8 (two joined loops);
- write ^ directly after a sign that has a horizontal bar above it (e.g. 7^);
- copy commas and dots that sit on the line as , and .;
- write [TXT] for any ordinary handwritten words on the line, and ? for a sign you cannot read.
Ignore fragments of writing cut off at the top or bottom edge. Do not guess words or meaning; this is a sign copy only.
Output just the sign sequence on one line, nothing else."""


def band(im, c):
    W = im.width; n = 3; step = W // n
    parts = [im.crop((max(0, k * step - 120), c - HH, min(W, (k + 1) * step + 120), c + HH)) for k in range(n)]
    pw = max(p.width for p in parts)
    out = Image.new("L", (pw, n * (2 * HH + 10)), 255)
    for k, p in enumerate(parts):
        out.paste(p, (0, k * (2 * HH + 10)))
    out = ImageOps.autocontrast(out, cutoff=1)
    out = out.resize((int(out.width * 0.75), int(out.height * 0.75)), Image.LANCZOS)
    b = io.BytesIO(); out.convert("RGB").save(b, "JPEG", quality=92)
    return base64.b64encode(b.getvalue()).decode()


def main():
    img, outdir = sys.argv[1], sys.argv[2]
    os.makedirs(outdir, exist_ok=True)
    im = Image.open(img).convert("L")
    res = []
    for i, c in enumerate(CENTRES):
        txt, u = ask(os.environ["PASS2_PROVIDER"], os.environ["PASS2_MODEL"], PROMPT, image_b64=band(im, c), max_tokens=2500)
        open(os.path.join(outdir, f"pass2_full_L{i:02d}.txt"), "w", encoding="utf-8").write(txt)
        lines = [l for l in txt.strip().splitlines() if l.strip()]
        line = lines[-1] if lines else ""
        res.append(f"L{i:02d}\t{line}")
        print(f"L{i:02d}", line.encode("ascii","replace").decode(), u, flush=True)
    open(os.path.join(outdir, "pass2_raw.txt"), "w", encoding="utf-8").write("\n".join(res) + "\n")


if __name__ == "__main__":
    main()
