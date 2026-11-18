#!/usr/bin/env python3
"""Build the running text of each leaf, every word in order, from the transcriptions and reading-words.tsv,
and count cipher words by the project's rule (issue #697): only strict segments are read; forced, lenient,
doubtful and unread segments are holes. Standard library only.

    python3 targets/mantua1524/aaymeloglu/running_text.py          # write the files and print the counts
    python3 targets/mantua1524/aaymeloglu/running_text.py --check  # exit 1 if a written file is stale

Writes, next to this script: reading_298.md, reading_68r.md, reading_198r.md (Italian running text with holes) and
decryption_298.tsv, decryption_68r.tsv, decryption_198r.tsv (the decryption line by line against the
transcription: units, key output, reading and tier of every cipher segment, clear rows as transcribed).

Rendering (README Conventions, "Holes are counted by words"):
- clear text: abbreviations expanded (`ch[e]` -> che), u/v normalised by rule (word-initial u before a vowel, and u
  between vowels -> v), a clear word marked {?} in the transcription is shown [?word];
- a cipher word from a strict segment: plain;
- a cipher word from a forced, lenient or doubtful segment: [?word], the proposed reading, counted as a hole;
- a code sign with no value: [?BOX], [?IZ], [?H], [?CROSS]; counted as a hole;
- an unread segment: [...] for one word; a run of such marks is joined as [... n]. The size of an unread segment
  with no reading is an estimate: one word per segment, the least the decode shows;
- a raised segment (signs written above the line) stands in place as [?(ria)];
- a word split between segments or lines (`desi-` + `-deraria`) is one word, read only if every cipher segment in
  it is strict.
The heading numerals "26" on f. 298r are probably clear (the transcription gives them as a cipher row, tier
unread); they are shown as 26. The issue #697 count takes them as one unread cipher word; the sized count leaves
them out.

Two counts are printed. The issue #697 count (the project's, reproduced here): each whitespace-separated token of a
segment's reading is a word, so an unread group like [H g o] counts three. The sized count: as rendered, an unread
segment with no reading is one word.
"""
import collections
import csv
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = [("298", "transcription-298.tsv", ["298r", "298v"]),
        ("68r", "transcription-68r.tsv", ["68r"]),
        ("198r", "transcription-198r.tsv", ["198r"])]
CODE = {"BOX", "IZ", "H", "CROSS", "C@"}
NOT_CIPHER = {("298r", "H2", "1")}          # "26": probably clear numerals
TITLES = {
    "298": "Vat. lat. 8214, ff. 298r-v: extract of a letter of G. B. Suardino from the Imperial court, [Vitoria?], 26 February [1524]",
    "68r": "Vat. lat. 8214, f. 68r: a letter in the first person plural, almost all in cipher [Federico II Gonzaga to Baldassarre Castiglione?, early 1524]",
    "198r": "Vat. lat. 8214, f. 198r: extract of a letter of Capino de Capo, Robbio, 8 April 1524",
}


def rows(name):
    with open(os.path.join(HERE, name), newline="", encoding="utf-8") as f:
        return list(csv.DictReader([l for l in f if not l.startswith("#")], delimiter="\t"))


def uv(w):
    """u/v by rule: word-initial u before a vowel, and u between vowels -> v."""
    def fix(m):
        word = m.group(0)
        out = list(word)
        low = word.lower()
        for i, c in enumerate(low):
            if c != "u" or i + 1 >= len(low) or low[i + 1] not in "aeiou":
                continue
            prev = low[i - 1] if i else ""
            if i == 0 or prev in "aeiou":
                out[i] = "V" if word[i] == "U" else "v"
        return "".join(out)
    return re.sub(r"[A-Za-zàèéìòù]+", fix, w)


TOKEN = re.compile(r"(?:[^\s\[]*\[[^\]]*\])+[^\s\[]*|\S+")


def clear_tokens(text):
    """Clear text -> list of (display word, flags). Punctuation tokens attach to the previous word."""
    text = re.sub(r"(^|\s)\.\s+(s|la)\s+\.(?=\s|$)", r"\1.\2.", text)
    out = []
    for t in TOKEN.findall(text):
        if t in (".", ",", ":", ";") and out:
            out[-1]["text"] += t
            continue
        if t == "(?)" and out:
            out[-1]["doubt"] = True
            continue
        doubt = "{?}" in t
        t = t.replace("{?}", "")
        hole = "[..]" in t
        t = re.sub(r"\[([^\]]*)\]", r"\1", t)
        out.append({"text": uv(t), "cipher": False, "strict": False, "hole": hole, "doubt": doubt,
                    "code": None, "raised": False})
    return out


def cipher_tokens(reading, tier, raised):
    toks = TOKEN.findall(reading.strip())
    if not toks:
        return [{"text": "", "cipher": True, "strict": False, "hole": True, "doubt": False, "code": None,
                 "raised": raised}]
    out = []
    for t in toks:
        tok = {"text": "", "cipher": True, "strict": tier == "strict", "hole": False, "doubt": False,
               "code": None, "raised": raised}
        m = re.fullmatch(r"(-?)\[([^\]]*)\](-?)\??", t)
        if m:
            inner = m.group(2).strip()
            if inner in CODE:
                tok["code"] = inner
            elif re.fullmatch(r"[A-Za-z()]+\?", inner):
                tok["text"] = m.group(1) + inner.rstrip("?").replace("(", "").replace(")", "") + m.group(3)
                tok["doubt"] = True
            else:
                tok["hole"] = True
                tok["text"] = m.group(1) + m.group(3)
        else:
            w = t
            if w.endswith("?") and len(w) > 1:
                w, tok["doubt"] = w[:-1], True
            w = re.sub(r"\[([^\]]*)\]", r"\1", w)
            w = w.replace("(", "").replace(")", "")
            tok["text"] = uv(w)
        out.append(tok)
    return out


def join_words(tokens):
    """Join a fragment ending in '-' with the next token when that token begins with '-' or is of the same kind
    (cipher after cipher: a word split between segments; clear after clear: a word split at a line end): one word,
    read only if all its cipher parts are."""
    words = []
    for t in tokens:
        prev = words[-1] if words else None
        if (prev is not None and prev["text"].endswith("-") and len(prev["text"]) > 1
                and (t["text"].startswith("-") or t["cipher"] == prev["parts"][-1]["cipher"])):
            prev["parts"].append(t)
            prev["text"] = prev["text"][:-1] + t["text"].lstrip("-")
        else:
            words.append(dict(t, parts=[t]))
    return words


def project_count(trows, words_tsv):
    """The count of issue #697: each whitespace-separated token of a cipher segment's reading is a word (bracket
    contents included; an empty reading is one word; the heading "26" of 298r, a cipher row graded unread, is one
    word), joined as in join_words; read = every segment strict."""
    stream = []
    for r in trows:
        k = (r["leaf"], r["line"], r["seq"])
        if r["kind"] == "clear":
            stream += clear_tokens(r["text"])
        else:                       # the heading "26" counts here, as a cipher row graded unread
            w = words_tsv[k]
            stream += [{"text": x, "cipher": True, "strict": w["tier"] == "strict"} for x in (w["reading"].split() or [""])]
    c = collections.Counter()
    for wd in join_words(stream):
        if any(p["cipher"] for p in wd["parts"]):
            c["cipher words"] += 1
            c["read (strict)"] += all(p["strict"] for p in wd["parts"] if p["cipher"])
    return c


def render(word):
    parts = word["parts"]
    cipher = any(p["cipher"] for p in parts)
    codes = [p["code"] for p in parts if p["code"]]
    hole = any(p["hole"] for p in parts)
    strict = cipher and all(p["strict"] for p in parts if p["cipher"]) and not codes and not hole
    text = word["text"].lstrip("-") if word["text"] != "-" else ""
    if codes:
        shown = "[?" + "+".join(codes) + "]"
    elif hole:
        shown = "[...]"
    elif not cipher:
        shown = f"[?{text}]" if any(p["doubt"] for p in parts) else text
    elif strict:
        shown = text
    elif any(p["raised"] for p in parts):
        shown = f"[?({text})]"
    else:
        shown = f"[?{text}]"
    return shown, cipher, strict


def size_holes(shown):
    out = []
    for s in shown:
        if s == "[...]" and out and re.fullmatch(r"\[\.\.\.(?: (\d+))?\]", out[-1]):
            n = int(re.fullmatch(r"\[\.\.\.(?: (\d+))?\]", out[-1]).group(1) or 1) + 1
            out[-1] = f"[... {n}]"
        else:
            out.append(s)
    return out


def build():
    words_tsv = {(r["leaf"], r["line"], r["seq"]): r for r in rows("reading-words.tsv")}
    files, counts = {}, {}
    for doc, tfile, leaves in DOCS:
        trows = rows(tfile)
        stream, dec = [], []
        for r in trows:
            k = (r["leaf"], r["line"], r["seq"])
            w = words_tsv.get(k)
            dec.append([r["leaf"], r["line"], r["seq"], r["kind"], r["text"],
                        w["units"] if w else "", w["key_output"] if w else "", w["reading"] if w else "",
                        w["tier"] if w else ""])
            if r["kind"] == "clear":
                toks = clear_tokens(r["text"])
            elif k in NOT_CIPHER:
                toks = [{"text": "26", "cipher": False, "strict": False, "hole": False, "doubt": False,
                         "code": None, "raised": False}]
            else:
                toks = cipher_tokens(w["reading"], w["tier"], r["kind"] == "raised")
            for t in toks:
                t["leaf"] = r["leaf"]
            stream.extend(toks)
        words = join_words(stream)
        by_leaf = collections.OrderedDict((l, []) for l in leaves)
        c = collections.Counter()
        for wd in words:
            shown, cipher, strict = render(wd)
            by_leaf[wd["parts"][0]["leaf"]].append(shown)
            if cipher:
                c["cipher words"] += 1
                c["read (strict)"] += strict
        pc = project_count(trows, words_tsv)
        counts[doc] = (pc, c)
        lines = [f"# {TITLES[doc]}", "",
                 "Running text, every word in order, built by `running_text.py` from the transcription and "
                 "`reading-words.tsv` (do not edit by hand). Clear text as transcribed, abbreviations expanded, u/v "
                 "normalised by rule. A cipher word from a strict segment is plain; a word proposed from a forced, "
                 "lenient or doubtful segment is `[?word]`; a code sign with no value is `[?BOX]` (`[?IZ]`, `[?H]`, "
                 "`[?CROSS]`); an unread segment is `[...]`, or `[... n]` for n words. Every `[?...]` and `[...]` "
                 "is a hole in the count. Sizes of unread segments with no reading are estimates (one word per "
                 "segment, the least the decode shows). Raised signs stand in place as `[?(...)]`.",
                 "",
                 f"Count by the project's rule (issue #697: strict segments read, all others holes; each "
                 f"whitespace token of a segment's reading is a word): {pc['read (strict)']} of "
                 f"{pc['cipher words']} cipher words read ({100 * pc['read (strict)'] / pc['cipher words']:.0f}%). "
                 f"With unread sign groups sized as one word each, as marked below: {c['read (strict)']} of "
                 f"{c['cipher words']} ({100 * c['read (strict)'] / c['cipher words']:.1f}%). "
                 f"English: `translation_{doc}.md`. Decryption line by line: `decryption_{doc}.tsv`.", ""]
        if doc == "298":
            lines += ["The heading numerals 26 are probably clear: the issue #697 count takes them as one unread cipher word (the "
                      "transcription gives them as a cipher row), the sized count leaves them out. The word "
                      "Can-|celler is split between the two sides and is given at the end of 298r.", ""]
        for leaf, shown in by_leaf.items():
            lines += [f"## f. {leaf}", "", " ".join(size_holes(shown)), ""]
        files[f"reading_{doc}.md"] = "\n".join(lines)
        head = "leaf\tline\tseq\tkind\ttranscription\tunits\tkey_output\treading\ttier\n"
        files[f"decryption_{doc}.tsv"] = ("# Decryption of " + TITLES[doc] + ": one row per transcription row; "
                                         "units, key output (key.json), reading and tier from reading-words.tsv. "
                                         "Built by running_text.py.\n" + head +
                                         "".join("\t".join(x) + "\n" for x in dec))
    return files, counts


def main():
    files, counts = build()
    stale = []
    for name, text in files.items():
        p = os.path.join(HERE, name)
        old = open(p, encoding="utf-8").read() if os.path.exists(p) else None
        if old != text:
            stale.append(name)
            if "--check" not in sys.argv:
                with open(p, "w", encoding="utf-8") as f:
                    f.write(text)
    tp, ts = collections.Counter(), collections.Counter()
    print("cipher words by the project's rule (strict segments read; all others holes)")
    print("        issue #697 count       holes sized by words")
    for doc, (p, c) in counts.items():
        tp.update(p)
        ts.update(c)
        print(f"  {doc:<5} {p['read (strict)']:>4} of {p['cipher words']:>4} {100 * p['read (strict)'] / p['cipher words']:5.1f}%"
              f"   {c['read (strict)']:>4} of {c['cipher words']:>4} {100 * c['read (strict)'] / c['cipher words']:5.1f}%")
    print(f"  all   {tp['read (strict)']:>4} of {tp['cipher words']:>4} {100 * tp['read (strict)'] / tp['cipher words']:5.1f}%"
          f"   {ts['read (strict)']:>4} of {ts['cipher words']:>4} {100 * ts['read (strict)'] / ts['cipher words']:5.1f}%")
    if "--check" in sys.argv and stale:
        sys.exit("stale: " + ", ".join(stale))


if __name__ == "__main__":
    main()
