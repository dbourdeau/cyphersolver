#!/usr/bin/env python3
"""Score a frozen transcription of doc. 114 against the printed text, per PREREGISTRATION.md.

usage: score.py transcription.tsv reference.tsv [key.json] [--shuffles N]
transcription.tsv: tab columns block, leaf, line, kind, tokens  (kind = word|null|clear; tokens = labels, first shape
                   reading only is used: 'Z{5}?' -> Z)
reference.tsv:     tab columns block, text  (printed text of that cipher block)
"""
import csv, json, random, re, sys, unicodedata

def norm(s):
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(ch for ch in s if ch.isalpha() and not unicodedata.combining(ch))
    return s.replace("j", "i").replace("v", "u")

def label(tok):
    tok = tok.lstrip("^")
    tok = re.sub(r"\{.*?\}", "", tok)
    tok = tok.split("=")[0]
    return tok.rstrip("?") or "?"

def load_tr(path):
    blocks = {}
    for r in csv.DictReader((l for l in open(path) if not l.startswith("#")), delimiter="\t"):
        if r["kind"] == "clear":
            continue
        blocks.setdefault(r["block"], []).extend(label(t) for t in r["tokens"].split())
    return blocks

def valsets(key):
    out = {}
    for lab, v in key.items():
        vals = v["values"]
        if all(x == "" for x in vals):
            out[lab] = None                      # null
        elif any(x.startswith("[") or x == "?" for x in vals):
            out[lab] = "WILD"
        else:
            out[lab] = tuple(norm(x) for x in vals if x != "")
    return out

def expand(labels, vs, first_only=False):
    """-> list of sets of letters, one per output character."""
    seq = []
    for lab in labels:
        v = vs.get(lab, "WILD")
        if v is None:
            continue
        if v == "WILD":
            seq.append(frozenset()); continue
        if first_only:
            v = v[:1]
        n = max(len(x) for x in v)
        if all(len(x) == n for x in v):
            for i in range(n):
                seq.append(frozenset(x[i] for x in v))
        else:                                    # values of different length: use the first
            for ch in v[0]:
                seq.append(frozenset(ch))
    return seq

def matches(seq, ref):
    """Max matched positions in a minimum-cost global alignment (unit costs)."""
    n, m = len(seq), len(ref)
    INF = 10**9
    prev = [(j, 0) for j in range(m + 1)]        # (cost, -matches)
    for i in range(1, n + 1):
        cur = [(i, 0)] + [None] * m
        for j in range(1, m + 1):
            hit = ref[j - 1] in seq[i - 1]
            a = (prev[j - 1][0] + (0 if hit else 1), prev[j - 1][1] - (1 if hit else 0))
            b = (prev[j][0] + 1, prev[j][1])
            c = (cur[j - 1][0] + 1, cur[j - 1][1])
            cur[j] = min(a, b, c)
        prev = cur
    return -prev[m][1]

def agreement(blocks, refs, vs, first_only=False):
    num = den = 0
    for b, labels in blocks.items():
        seq = expand(labels, vs, first_only)
        ref = refs[b]
        num += matches(seq, ref)
        den += max(len(seq), len(ref))
    return num / den if den else 0.0

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    n_shuf = 1000
    if "--shuffles" in sys.argv:
        n_shuf = int(sys.argv[sys.argv.index("--shuffles") + 1]); args.remove(str(n_shuf))
    tr, refp = args[0], args[1]
    keyp = args[2] if len(args) > 2 else "key-46dec7b.json"
    key = json.load(open(keyp))["signs"]
    vs = valsets(key)
    blocks = load_tr(tr)
    refs = {r["block"]: norm(r["text"]) for r in csv.DictReader(open(refp), delimiter="\t")}
    used = sorted({l for ls in blocks.values() for l in ls})
    unknown = [l for l in used if l not in vs]
    print("signs:", sum(len(v) for v in blocks.values()), "labels used:", len(used), "not in key:", unknown)
    print("reference letters:", sum(len(refs[b]) for b in blocks))
    obs = agreement(blocks, refs, vs)
    print(f"agreement (any-of rule): {obs:.4f}")
    print(f"agreement (first value only): {agreement(blocks, refs, vs, True):.4f}")
    lettered = [l for l in used if isinstance(vs.get(l), tuple)]
    rng = random.Random(1494)
    sh = []
    for _ in range(n_shuf):
        perm = lettered[:]; rng.shuffle(perm)
        vs2 = dict(vs); vs2.update({a: vs[b] for a, b in zip(lettered, perm)})
        sh.append(agreement(blocks, refs, vs2))
    print(f"shuffles: n={n_shuf} best={max(sh):.4f} mean={sum(sh)/len(sh):.4f}")
    for b in blocks:
        seq = expand(blocks[b], vs)
        print(f"\n[{b}] key output ({len(seq)}):", "".join(sorted(s)[0] if len(s) == 1 else ("(" + "/".join(sorted(s)) + ")" if s else "?") for s in seq))
        print(f"[{b}] reference  ({len(refs[b])}):", refs[b])

if __name__ == "__main__":
    main()
