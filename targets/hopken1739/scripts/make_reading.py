"""Write the cipher section of reading_<doc>.md: the contemporary French of each run, with every place where it departs
from what the frozen code list gives marked in place:
    [1234 ?text]  the group's key value does not give this text (or the group is not in the key): text rests on the gloss
    [1234 -]      the group's key value has no counterpart in the gloss
Plain letters are exactly what key.tsv gives (accents, apostrophes, case and u/v aside). Context paragraphs come from
contexts/<doc>.md when present."""
import pathlib, re, sys, unicodedata
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import decode
ROOT = decode.ROOT


def letter(ch):
    s = unicodedata.normalize("NFD", ch.lower())[:1]
    return s.replace("v", "u") if "a" <= s <= "z" else None


def mark(groups, gloss, key):
    pos = [i for i, c in enumerate(gloss) if letter(c)]
    text = "".join(letter(gloss[i]) for i in pos)
    vals = []
    for g in groups:
        c = g.rstrip("?")
        vals.append(key[c][0].replace("v", "u") if c in key and not key[c][0].startswith("[") else None)
    n, m, INF = len(groups), len(text), 10 ** 9
    best = [[INF] * (m + 1) for _ in range(n + 1)]; back = [[None] * (m + 1) for _ in range(n + 1)]; best[0][0] = 0
    for i in range(n):
        for j in range(m + 1):
            b = best[i][j]
            if b >= INF: continue
            v = vals[i]
            if v is not None and text.startswith(v, j) and b < best[i + 1][j + len(v)]:
                best[i + 1][j + len(v)] = b; back[i + 1][j + len(v)] = (j, 0)
            for L in range(0, min(14, m - j) + 1):
                # tie-break: a departure whose span still contains the group's own value (e.g. the gloss adds an
                # article before a code word: [1532 ?la Suede]) costs a little less than one that splits it
                c = b + 1 - (0.01 if v and v in text[j:j + L] else 0)
                if c < best[i + 1][j + L]:
                    best[i + 1][j + L] = c; back[i + 1][j + L] = (j, 1)
    spans, j = [], m
    for i in range(n, 0, -1):
        pj, dep = back[i][j]; spans.append((pj, j, dep)); j = pj
    spans.reverse()
    out, cur = [], 0
    for g, (a, b, dep) in zip(groups, spans):
        if not dep: continue
        c = g.rstrip("?")
        if a == b:
            at = pos[a] if a < m else len(gloss)
            out.append((at, at, f"[{c} -]"))
        else:
            out.append((pos[a], pos[b - 1] + 1, f"[{c} ?{gloss[pos[a]:pos[b - 1] + 1]}]"))
    res = ""
    for s, e, t in out:
        res += gloss[cur:s] + t; cur = e
    return res + gloss[cur:], sum(1 for *_, d in spans if d)


def cipher_section(doc, tr):
    key = decode.load_key(); lines = []
    for img, run, use, gs, gloss in decode.runs(doc):
        g = re.sub(r"\s*\[[^\]]*\]", "", gloss).strip()
        if not g:
            dec = " ".join(decode.show(x, key) for x in gs)
            lines.append(f"- **{img} {run}** (no gloss) decoded: `{dec}`  \n  English: {tr.get(img + run, '[not read]')}")
            continue
        r, d = mark(gs, g, key)
        lines.append(f"- **{img} {run}** {r}  \n  English: {tr.get(img + run, '')}")
    return "\n".join(lines)


if __name__ == "__main__":
    tr = dict(l.rstrip("\n").split("\t") for l in open(ROOT / "translations.tsv", encoding="utf-8") if l.strip())
    for doc in decode.DOCS:
        ctx = ROOT / "contexts" / f"{doc}.md"
        head = ctx.read_text(encoding="utf-8") if ctx.exists() else f"# {doc}\n"
        (ROOT / f"reading_{doc}.md").write_text(head.rstrip() + "\n\n## Cipher runs (French over the groups, marked against key.tsv)\n\n"
                                                 + cipher_section(doc, tr) + "\n", encoding="utf-8")
