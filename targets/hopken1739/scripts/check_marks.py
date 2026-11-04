"""Check the readings against the groups and count words. Standard library only.
    python scripts/check_marks.py      exit 1 on any failure
1. decryption_<doc>.txt must equal what decode.py rebuilds from the transcription and key.tsv.
2. Every cipher-run line of reading_<doc>.md is walked letter by letter against the key values of its groups, in order.
   Plain letters must be exactly the key's letters (accents, apostrophes, case, u/v aside). A departure must be marked in
   place: [1234 ?text] (text not given by the key) or [1234 -] (key value with no counterpart). A mark must name the
   group that stands at that place. Fails on any unmarked departure, a misplaced mark, or groups left over.
3. Words: 'key' = every letter from a confirmed key value; 'single' = rests on a value attested in one place only
   (or a mixed one); 'gloss' = contains a marked departure, so it rests on the contemporary gloss alone."""
import pathlib, re, sys, unicodedata
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import decode
ROOT = decode.ROOT
LINE = re.compile(r"^- \*\*(\d{3}) (\w+)\*\* (.*?)\s*$")
TOK = re.compile(r"\[(\d{4}) (?:\?([^\]]*)|-)\]|(.)", re.S)


def let(ch):
    s = unicodedata.normalize("NFD", ch.lower())[:1]
    return s.replace("v", "u") if "a" <= s <= "z" else None


def check_run(text, groups, key):
    vals = [(g.rstrip("?"), key.get(g.rstrip("?"), (None, ""))) for g in groups]
    i, off, err, words, cur = 0, 0, [], [], set()
    def boundary():
        nonlocal i, off
        while i < len(vals) and vals[i][1][0] is not None and off == len(vals[i][1][0].replace("v", "u")):
            i += 1; off = 0
    for m in TOK.finditer(text):
        g, gl, ch = m.group(1), m.group(2), m.group(3)
        if g:
            boundary()
            if off != 0 or i >= len(vals) or vals[i][0] != g:
                err.append(f"mark [{g}] not at the place of that group"); continue
            cur.add("gloss"); i += 1; off = 0
            parts = gl.split() if gl is not None else []
            for _ in parts[1:]:  # a mark spanning several gloss words counts each of them as a gloss word
                words.append(cur); cur = {"gloss"}
            continue
        if ch.isspace():
            if cur: words.append(cur); cur = set()
            continue
        L = let(ch)
        if L is None: continue
        boundary()
        if i >= len(vals): err.append(f"letter {ch} past the last group"); continue
        g, (v, st) = vals[i]
        if v is None or v.startswith("["):
            err.append(f"UNMARKED group {g} not in the key under letter {ch}"); i += 1; continue
        v = v.replace("v", "u")
        if v[off] != L:
            err.append(f"UNMARKED departure at group {g}: reading {ch}, key {v}")
        cur.add("key" if st == "confirmed" or st.startswith("codeword") else "single"); off += 1
    if cur: words.append(cur)
    boundary()
    if i != len(vals): err.append(f"groups left over: {i} of {len(vals)}")
    return err, words


def main():
    key = decode.load_key(); bad = 0; tot = {}
    for doc in decode.DOCS:
        want = "\n".join(decode.decrypt(doc)) + "\n"
        if (ROOT / f"decryption_{doc}.txt").read_text(encoding="utf-8") != want:
            print(doc, ": decryption file differs from transcription + key.tsv"); bad += 1
        runs = {img + run: gs for img, run, use, gs, gloss in decode.runs(doc)}
        c = {"key": 0, "single": 0, "gloss": 0}
        for ln in (ROOT / f"reading_{doc}.md").read_text(encoding="utf-8").splitlines():
            m = LINE.match(ln)
            if not m or m.group(3).startswith("(no gloss)"): continue
            err, words = check_run(m.group(3), runs[m.group(1) + m.group(2)], key)
            for e in err: print(doc, m.group(1), m.group(2), e); bad += 1
            for w in words:
                c["gloss" if "gloss" in w else "single" if "single" in w else "key"] += 1
        n = sum(c.values()); tot[doc] = c
        if n: print(f"{doc}: cipher words {n}; from confirmed key values {c['key']} ({c['key']/n:.0%}); "
                    f"on single/mixed values {c['single']} ({c['single']/n:.0%}); resting on the gloss alone {c['gloss']} ({c['gloss']/n:.0%})")
    print("FAIL" if bad else "OK: no unmarked departure"); sys.exit(1 if bad else 0)


main()
