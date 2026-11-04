#!/usr/bin/env python3
"""Rebuild each decryption from its transcription and a key, then walk the French reading letter by letter against
it. Fails (exit 1) on any unmarked departure. Standard library only.

    python scripts/check_marks.py            all letters
    python scripts/check_marks.py --write    rewrite the decryption files first

Which key:
    l2 (10 Jan 1548, the letter the key was built on): key.tsv, the current table.
    l4 (2 Aug 1548, held out): key_frozen.tsv, unchanged since it was frozen. The signs split after the test
       (Lo, L1, N20) take the frozen value of the blind reader's own class (Le, R); yg has no frozen value.
       A second count shows how many words key.tsv (with values set after the test) gives verbatim. That count
       is not a test.
Marks in the reading (section '## French' of reading_<letter>.md):
    plain letters      must equal the next decrypted letters (case, spaces, punctuation, ' ignored; j=i, v=u)
    {r/s}              reading r where the signs give s            (word counts as repaired)
    {+r}               r restored, no sign                         (repaired)
    {-s}               sign letters s not read (null, slip)        (repaired)
    [?w:s]             word w proposed from context; signs give s  (proposed)
    [...:s]            hole; signs give s, not read                (unread)
Only one kind of round bracket is allowed in the French: a place note such as '(3r, after "...")'. Any other
round bracket fails, so no text can be dropped unseen.
"""
import re, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from compare import load
def readkey(fn):
    K = {}
    for l in open(ROOT / fn, encoding="utf-8"):
        if l.strip() and not l.startswith("# "):
            p = l.rstrip("\n").split("\t"); K[p[0]] = p[1]
    return K
CUR, FRO = readkey("key.tsv"), readkey("key_frozen.tsv")
PARENT = {"Lo": "Le", "L1": "Le", "N20": "R"}
def fro(t): return FRO.get(PARENT.get(t, t), "?")
def cur(t): return CUR.get(t, "?")
def norm(s): return s.lower().replace("j", "i").replace("v", "u")
TOK = re.compile(r"\{[^}]*\}|\[[^\]]*\]|[A-Za-z]|\s+|[^\sA-Za-z{\[]")
PLACE = re.compile(r"\(\d[rv][^)]*\)")
def build(rows, f):
    dec, pos2tok, toks = "", [], []
    for r in rows.values():
        for t in r:
            v = f(t); dec += v; pos2tok += [len(toks)] * len(v); toks.append(t)
    out = "\n".join(f"{k[0]} {k[1]}: " + "".join(f(t) for t in r) for k, r in rows.items()) + "\n"
    return dec, pos2tok, toks, out
def check(letter):
    rows = load(ROOT / f"transcription_{letter}.txt")
    f = cur if letter == "l2" else fro
    dec, pos2tok, toks, out = build(rows, f)
    files = [(ROOT / f"decryption_{letter}.txt", out)]
    if letter != "l2": files.append((ROOT / f"decryption_{letter}_current_key.txt", build(rows, cur)[3]))
    bad = 0
    for fn, o in files:
        if "--write" in sys.argv: fn.write_text(o, encoding="utf-8")
        if fn.read_text(encoding="utf-8") != o: print(f"{letter}: {fn.name} differs from transcription + key"); bad += 1
    txt = (ROOT / f"reading_{letter}.md").read_text(encoding="utf-8").split("## French")[1].split("## English")[0]
    txt = PLACE.sub(" ", txt)
    if "(" in txt or ")" in txt:
        print(f"{letter}: round bracket in the French that is not a place note: '{txt[max(0, txt.find('(')-20):txt.find('(')+30]}'"); return bad + 1
    i = 0; words = []; cur_w = None
    def take(s, what):
        nonlocal i
        s = norm(s)
        if dec[i:i+len(s)] != s:
            print(f"{letter}: {what} expects signs '{s}' at {i}, signs give '{dec[i:i+len(s)]}' (context '{dec[max(0,i-15):i+15]}')")
            raise SystemExit(1)
        i += len(s)
    def close():
        nonlocal cur_w
        if cur_w is not None: words.append(cur_w); cur_w = None
    for t in TOK.findall(txt):
        if t.isspace() or (len(t) == 1 and not t.isalpha() and t not in "{["):
            if t.isspace(): close()
            continue
        if cur_w is None: cur_w = {"kind": "verbatim", "start": i, "text": ""}
        if t.startswith("{"):
            b = t[1:-1]
            if b.startswith("+"): cur_w["text"] += b[1:]
            elif b.startswith("-"): take(b[1:], t)
            else: take(b.split("/")[1], t); cur_w["text"] += b.split("/")[0]
            if cur_w["kind"] == "verbatim": cur_w["kind"] = "repaired"
        elif t.startswith("[?"):
            take(t[2:-1].split(":")[1], t); cur_w["kind"] = "proposed"
        elif t.startswith("[..."):
            take(t[1:-1].split(":")[1], t); cur_w["kind"] = "unread"
        else:
            take(t, "letter"); cur_w["text"] += t
        cur_w["end"] = i
    close()
    if i != len(dec): print(f"{letter}: reading stops at {i} of {len(dec)} decrypted letters; next '{dec[i:i+30]}'"); bad += 1
    n = len(words); c = {k: sum(w["kind"] == k for w in words) for k in ("verbatim", "repaired", "proposed", "unread")}
    key = "key.tsv" if letter == "l2" else "key_frozen.tsv (held out)"
    print(f"{letter} [{key}]: words {n}: verbatim {c['verbatim']} ({c['verbatim']/n:.1%}), repaired {c['repaired']}, proposed {c['proposed']}, unread holes {c['unread']}; sense incl. repairs {(c['verbatim']+c['repaired'])/n:.1%}")
    if letter != "l2":
        v2 = 0
        for w in words:
            if w["kind"] not in ("verbatim", "repaired"): continue
            span = sorted(set(pos2tok[w["start"]:w.get("end", w["start"])]))
            if norm("".join(cur(toks[j]) for j in span)) == norm(w["text"]): v2 += 1
        print(f"{letter} [key.tsv, values set after the test; not a test]: verbatim {v2} of {n} ({v2/n:.1%})")
    return bad
bad = sum(check(l) for l in ([a for a in sys.argv[1:] if not a.startswith("--")] or ["l2", "l4"]))
sys.exit(1 if bad else 0)
