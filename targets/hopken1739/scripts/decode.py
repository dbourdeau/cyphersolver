"""Rebuild the decryption from the transcription and key.tsv: python decode.py  (writes decryption_<doc>.txt)
Each line: image, run, then group=value for every group; [1234] = group not in the key; a value the key does not
hold as 'confirmed' carries a trailing ?."""
import pathlib, re
ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = {"dialogue_dec1739": ("pairs.tsv", lambda img, run: img in ("255", "256") or (img == "257" and int(run[1:]) <= 47)),
        "enc2_dec1739": ("pairs.tsv", lambda img, run: img == "257" and int(run[1:]) >= 48),
        "img260_1740": ("heldout.tsv", lambda img, run: img == "260"),
        "ps_img263": ("bare_263.tsv", lambda img, run: img == "263")}


def load_key():
    k = {}
    for ln in open(ROOT / "key.tsv", encoding="utf-8"):
        if not ln[:1].isdigit(): continue
        f = ln.rstrip("\n").split("\t")
        if f[4].startswith("unresolved"): continue  # demoted EM filler (key_demoted.tsv): treated as not in the key
        k[f[0]] = (f[1], f[4])
    return k


def runs(doc):
    path, sel = DOCS[doc]
    for ln in open(ROOT / path, encoding="utf-8"):
        if ln.startswith("#") or not ln.strip(): continue
        img, run, use, groups, gloss = ln.rstrip("\n").split("\t")
        if sel(img, run):
            yield img, run, use, groups.split(), gloss


def show(g, key):
    c = g.rstrip("?")
    if c not in key: return f"{g}=[{c}]"
    v, st = key[c]
    return f"{g}={v}" + ("" if st == "confirmed" or st.startswith("codeword") else "?")


def decrypt(doc):
    key = load_key()
    return [f"{img} {run}\t" + " ".join(show(g, key) for g in gs) for img, run, use, gs, gloss in runs(doc)]


def transcription(doc):
    out = []
    for img, run, use, gs, gloss in runs(doc):
        out.append(f"{img} {run}\t{' '.join(gs)}")
        out.append(f"   gloss\t{gloss}")
    return out


if __name__ == "__main__":
    for d in DOCS:
        (ROOT / f"decryption_{d}.txt").write_text("\n".join(decrypt(d)) + "\n", encoding="utf-8")
        (ROOT / f"transcription_{d}.txt").write_text(
            "# Cipher groups per run (image, run), digits as settled from two blind passes; ? = doubtful digit.\n"
            "# 'gloss' = the contemporary French written over the run (Höpken/Carlson chancery decipherment), as written.\n"
            + "\n".join(transcription(d)) + "\n", encoding="utf-8")
        print(d, len(decrypt(d)))
