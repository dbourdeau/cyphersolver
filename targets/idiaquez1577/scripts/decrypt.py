"""Mechanical decryption of a shape transcription with key_frozen.tsv.
usage: python -I scripts/decrypt.py transcription.txt key_frozen.tsv > decryption.txt
A sign with a value or mark the frozen key does not give is printed '?' (the whole sign). Word gaps ' / ' become
spaces. Output: one 'Lnn: text' line per transcription line."""
import re, sys

def load(path):
    k = {"vowel": {}, "cons": {}, "mark": {}, "sup": {}, "special": {}, "code": {}}
    for ln in open(path, encoding="utf-8"):
        if ln.startswith("#") or not ln.strip():
            continue
        kind, sign, val = ln.rstrip("\n").split("\t")[:3]
        k[kind][sign] = val
    return k

TOK = re.compile(r"^(\d+)([+.@e|]?)([\^_v'%²†=]*)(\?)?$")

def dec_token(t, k):
    t0 = t.rstrip("?")
    if t0 in k["code"]:
        return "[" + k["code"][t0] + "]"
    if t0 in k["special"]:
        return k["special"][t0]
    m = TOK.match(t)
    if not m:
        return "?"
    num, mark, sups, _ = m.groups()
    if "=" in sups or "%" in sups or "²" in sups or "†" in sups:
        return "?"
    if num in k["vowel"] and not mark:
        base = k["vowel"][num]
    elif num in k["cons"]:
        base = k["cons"][num] + (k["mark"][mark] if mark else "")
    elif num in k["vowel"]:
        return "?"
    else:
        return "?"
    for s in sups:
        base += k["sup"].get(s, "?")
    return base

def dec_line(line, k):
    words = []
    for w in line.split(" / "):
        out = ""
        for t in w.split():
            if t in ("~", ",", "/."):
                continue
            out += dec_token(t, k)
        if out:
            words.append(out)
    return " ".join(words)

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    k = load(sys.argv[2])
    n = 0
    for ln in open(sys.argv[1], encoding="utf-8"):
        ln = ln.rstrip("\n")
        if ln.startswith("#") or not ln.strip():
            continue
        n += 1
        print(f"L{n:02d}: {dec_line(ln, k)}")
