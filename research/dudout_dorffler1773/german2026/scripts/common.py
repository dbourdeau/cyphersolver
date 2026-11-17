"""Shared helpers: paths, letter folding, model calls, page splitting.

Model calls go through Simon Willison's `llm` CLI (https://llm.datasette.io) with a Vertex AI
plugin; any plugin that accepts `-a IMAGE` works. Set the model names in reread.py.
"""
import concurrent.futures as cf, json, os, subprocess, unicodedata

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = os.path.join(REPO, "analysis")
D = os.environ.get("CIPHER_DATA") or os.path.join(REPO, "data")


def norm(text):
    """Letters only, lower case, umlauts folded (a contemporary decrypter's spelling varies)."""
    t = text.lower().replace("ß", "ss").replace("ÿ", "y").replace("ſ", "s")
    t = unicodedata.normalize("NFKD", t)
    return "".join(ch for ch in t if "a" <= ch <= "z")


def sh(*a, timeout=None):
    return subprocess.run(a, capture_output=True, text=True, timeout=timeout, stdin=subprocess.DEVNULL)


def ask(model, image, prompt, timeout=600, tier=None):
    err = ""
    opts = ["-o", "tier", tier] if tier else []
    for _ in range(2):
        try:
            r = sh("llm", "-n", "-m", model, *opts, "-a", image, prompt, timeout=timeout)
            if r.returncode == 0 and r.stdout.strip():
                return r.stdout.strip(), None
            err = r.stderr[-200:]
        except Exception as e:
            err = str(e)[:200]
    return None, err


def run_pool(jobs, fn, out_path, workers=8):
    with cf.ThreadPoolExecutor(workers) as ex, open(out_path, "a") as o:
        bad = 0
        for n, rec in enumerate(ex.map(fn, jobs), 1):
            o.write(json.dumps(rec, ensure_ascii=False) + "\n"); o.flush()
            bad += "error" in rec
            if n == 16 and bad == 16:
                raise SystemExit("ABORT: first 16 calls all failed: " + rec.get("error", "")[-200:])
            if n % 50 == 0:
                print(n, "done,", bad, "errors", flush=True)


def halves(src, out_dir, stem):
    """Split a two-page opening into L and R halves with a 40 px overlap at the gutter."""
    from PIL import Image
    im = Image.open(src)
    w, h = im.size
    out = []
    for side, x in (("L", 0), ("R", w // 2)):
        o = os.path.join(out_dir, stem + side + ".jpg")
        if not os.path.exists(o):
            im.crop((max(0, x - 20), 0, min(w, x + w // 2 + 20), h)).save(o, quality=92)
        out.append(o)
    return out
