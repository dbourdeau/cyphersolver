#!/usr/bin/env python3
"""Repository copy of the frozen test script (frozen sha256 23feea53dc94e699095d2c4123861220170a6b6c8c99d8ed9ecd8b83b825b952): only the paths and the table
loader are changed, so that it runs inside this folder.  Original docstring follows.

Test of our THE1385 table against the State Department clerk's decipherment of John Quincy Adams's
despatches No. 85 (27 May 1812, frame 0196 left, interlinear) and No. 74 (2 Nov 1811, frame 0168, against
the clerk's separate copy on frames 0170-0171).  Rule: see TEST_PLAN.md (written before this was run).

  python3 -I run_test.py counts   # how many numbers each part holds; opens no table
  python3 -I run_test.py pilot    # control calibration on SYNTHETIC tables (uses only the lengths of the
                                  # table's readings, never a reading)
  python3 -I run_test.py run      # the single real run
"""
import csv, difflib, os, random, re, statistics, sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = HERE
# The table: the State Department code sheet as transcribed in ../../../morris1813/beling/key/ (already in this
# repository). The frozen run of 21 Nov 2026 read the same sheet from a local JSON file (sha256 cfb85846...4a5,
# 1,571 readings); load_table() rebuilds exactly those 1,571 readings from the CSV (checked entry by entry).
TABLE = os.path.join(HERE, "..", "..", "..", "morris1813", "beling", "key", "codebook_M97_13_transcription.csv")
SKIP_STATUS = {"blank", "explicit_blank", "unresolved", "punctuation_glyph", "glyph_identity_unresolved"}


def load_table():
    tab = {}
    for r in csv.DictReader(open(TABLE, encoding="utf-8")):
        if r["status"] in SKIP_STATUS or r["code_number"] == "665":   # 665 (Z) was not in the frozen table
            continue
        v = r["reading"].split(" / ")[0].strip()
        if r["code_number"] == "681":                                 # the two faces of the sheet differ: are / arc
            v = r["numerical_sheet_1057_first_reading"]
        if re.sub(r"[^a-z]", "", v.lower()):
            tab[r["code_number"]] = v
    return tab


PASS_MARK = 0.85            # share of scored numbers that must agree, each part, both bases
CTRL_TOL = {"part1": 0.25, "part2": 0.40}   # largest shuffled-table score tolerated
MIN_SCORED = {"part1": 80, "part2": 200}
N_SHUFFLES = 1000
SEED = 20261121
SKIP_AFTER_MATCH = 2        # part 2: clerk letters that may be passed over after a matched number
SKIP_UNMATCHED = 14         # part 2: clerk letters that may be passed over by an unmatched number
SKIP_GAP = 30               # part 2: clerk letters that may be passed over at a gutter gap / cut group
ERROR_GROUPS = ["387", "1431", "1101"]   # the three numbers the clerk copied in figures: never scored

TOK = re.compile(r'"[^"]*"|<[^>]*>|[^\s{]*\{[^}]*\}|\S+')


def norm(s):
    s = re.sub(r"[^a-z]", "", (s or "").lower())
    return s.replace("j", "i").replace("v", "u")


def norm_reading(r):
    r = re.sub(r"[^a-z]", "", (r or "").lower())
    if r in ("ij", "ji"):
        return "i"
    if r in ("uv", "vu"):
        return "u"
    return r.replace("j", "i").replace("v", "u")


def parse_code(path):
    """Tokens in order: dict(kind='num'|'hole'|'clear', cands, doubt, gloss, line, raw)."""
    toks = []
    for ln in open(path, encoding="utf-8"):
        ln = ln.rstrip("\n")
        if ln.strip().upper().startswith("NOTES"):
            break
        m = re.match(r"\s*L(\d+)\s*:\s*(.*)$", ln)
        if not m:
            continue
        lno, text = int(m.group(1)), m.group(2)
        for raw in TOK.findall(text):
            if raw.startswith('"'):
                w = norm(raw)
                if w:
                    toks.append(dict(kind="clear", word=w, line=lno, raw=raw))
                continue
            if raw.startswith("<"):
                continue
            gloss = ""
            g = re.search(r"\{([^}]*)\}$", raw)
            body = raw
            if g:
                gloss, body = re.sub(r"\[[^\]]*\]", "", g.group(1)), raw[:g.start()]
            if not re.match(r"\d|\[\?\]|GAP|x", body):
                continue                      # punctuation and stray marks
            if "GAP" in body or "[?]" in body or "x" in body:
                toks.append(dict(kind="hole", cands=[], doubt=True, gloss=norm(gloss), line=lno, raw=raw))
                continue
            cands = [re.sub(r"\D", "", c) for c in body.split("/")]
            cands = [c for c in cands if c]
            toks.append(dict(kind="num", cands=cands, doubt=("?" in body or "/" in body),
                             gloss=norm(gloss), line=lno, raw=raw))
    return toks


def key_of(t):
    return t["cands"][0] if t.get("cands") else "<?>"


def mark_scored(ta, tb):
    """A number is scored iff difflib pairs it 'equal' with the other reader's number and neither is doubtful."""
    fa = [t for t in ta if t["kind"] != "clear"]
    fb = [t for t in tb if t["kind"] != "clear"]
    for t in ta + tb:
        t["scored"] = False
    sm = difflib.SequenceMatcher(None, [key_of(t) for t in fa], [key_of(t) for t in fb], autojunk=False)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag != "equal":
            continue
        for k in range(i2 - i1):
            a, b = fa[i1 + k], fb[j1 + k]
            ok = a["kind"] == "num" and b["kind"] == "num" and not a["doubt"] and not b["doubt"]
            a["scored"] = b["scored"] = ok


# ---------------------------------------------------------------- part 1: No. 85, interlinear
def part1_units(toks):
    """Numbers up to and including the last one that carries clerk's writing."""
    nums = [t for t in toks if t["kind"] != "clear"]
    last = max((i for i, t in enumerate(nums) if t["gloss"]), default=-1)
    return nums[:last + 1]


def segments(units):
    segs, cur = [], [units[0]]
    for prev, u in zip(units, units[1:]):
        if (prev["gloss"] == "" or u["gloss"] == "") and 0 <= u["line"] - prev["line"] <= 1:
            cur.append(u)
        else:
            segs.append(cur)
            cur = [u]
    segs.append(cur)
    return segs


def align_free(seg, table):
    """Monotone alignment, clerk letters may be skipped freely. Maximise (matched, matched scored)."""
    c = "".join(u["gloss"] for u in seg)
    K, L = len(seg), len(c)
    reads = [[norm_reading(table.get(n, "")) for n in t["cands"]] for t in seg]
    NEG = (-1, -1)
    best = [[NEG] * (L + 1) for _ in range(K + 1)]
    back = [[None] * (L + 1) for _ in range(K + 1)]
    best[0][0] = (0, 0)
    for i in range(K + 1):
        for p in range(L + 1):
            cur = best[i][p]
            if cur == NEG:
                continue
            if p < L and cur > best[i][p + 1]:
                best[i][p + 1] = cur; back[i][p + 1] = ("c", i, p)
            if i < K:
                if cur > best[i + 1][p]:
                    best[i + 1][p] = cur; back[i + 1][p] = ("n", i, p)
                for r in set(reads[i]):
                    if r and c.startswith(r, p):
                        q = p + len(r)
                        val = (cur[0] + 1, cur[1] + (1 if seg[i]["scored"] else 0))
                        if val > best[i + 1][q]:
                            best[i + 1][q] = val; back[i + 1][q] = ("m", i, p, r)
    i, p = K, L
    out = [False] * K
    while (i, p) != (0, 0):
        b = back[i][p]
        if b[0] == "m":
            out[b[1]] = True
        i, p = b[1], b[2]
    return out


def score_part1(units, table, detail=None):
    sc = ag = 0
    for seg in segments(units):
        res = align_free(seg, table)
        for t, m in zip(seg, res):
            if detail is not None:
                detail.append((t, m))
            if t["scored"]:
                sc += 1; ag += m
    return sc, ag


# ---------------------------------------------------------------- part 2: No. 74, separate copy
def clerk_stream(path):
    """Only the transcriber's numbered text lines; their bracketed remarks and struck words are dropped."""
    out = []
    for ln in open(path, encoding="utf-8"):
        m = re.match(r"\s*[A-Z]?\d+:\s*(.*)$", ln)
        if m:
            t = re.sub(r"\[[^\]]*\]", " ", m.group(1))
            out.append(re.sub(r"<[^>]*>", " ", t))
    txt = norm(" ".join(out))
    i = txt.find("howlong")
    return txt[i:] if i >= 0 else txt


def part2_stream(tl, tr):
    """Left leaf then right leaf. A virtual gap closes every left-leaf line (gutter). A last left-leaf line
    holding one number equal to the first number of the right leaf is the catchword and is dropped."""
    lines = {}
    for t in tl:
        lines.setdefault(t["line"], []).append(t)
    order = sorted(lines)
    if order:
        last = [t for t in lines[order[-1]] if t["kind"] == "num"]
        first_r = next((t for t in tr if t["kind"] == "num"), None)
        if len(lines[order[-1]]) == 1 and len(last) == 1 and first_r and key_of(last[0]) == key_of(first_r):
            order = order[:-1]
    out = []
    for ln in order:
        out += lines[ln]
        out.append(dict(kind="hole", cands=[], doubt=True, gloss="", line=ln, raw="(line end)", scored=False))
    out += tr
    # the three error numbers are never scored: the pair 1431 1101 and the number before it
    keys = [key_of(t) if t["kind"] == "num" else None for t in out]
    for i in range(1, len(out) - 1):
        if keys[i:i + 2] == ERROR_GROUPS[1:]:
            for t in out[i - 1:i + 2]:
                t["scored"] = False; t["error_group"] = True
            break
    return out


def split_by_anchors(stream, clerk):
    """Cut the number stream at Adams's clear words and the clerk stream at the same words (in order).
    A clear word not found in the clerk stream after the current point is ignored (segments merge)."""
    segs, cur, pos = [], [], 0
    for t in stream:
        if t["kind"] == "clear":
            w = t["word"]
            j = clerk.find(w, pos)
            if j < 0 and len(w) >= 5:
                j = clerk.find(w[:5], pos)
                w = w[:5] if j >= 0 else w
            if j >= 0:
                segs.append((cur, clerk[pos:j]))
                cur, pos = [], j + len(w)
            continue
        cur.append(t)
    segs.append((cur, clerk[pos:]))
    return [s for s in segs if s[0]]


def align_bounded(seg, c, table):
    """Monotone alignment with bounded skipping (see plan). Maximise (matched, matched scored)."""
    K, L = len(seg), len(c)
    reads = [[norm_reading(table.get(n, "")) for n in t["cands"]] if t["kind"] == "num" else [] for t in seg]
    NEG = (-1, -1)
    best = [dict() for _ in range(K + 1)]
    back = [dict() for _ in range(K + 1)]
    best[0][0] = (0, 0)
    for i in range(K):
        t = seg[i]
        for p, cur in best[i].items():
            lim = SKIP_GAP if t["kind"] == "hole" else SKIP_UNMATCHED
            for s in range(0, lim + 1):
                q = p + s
                if q > L:
                    break
                if cur > best[i + 1].get(q, NEG):
                    best[i + 1][q] = cur; back[i + 1][q] = (p, False)
            for r in set(reads[i]):
                if r and c.startswith(r, p):
                    val = (cur[0] + 1, cur[1] + (1 if t["scored"] else 0))
                    for s in range(0, SKIP_AFTER_MATCH + 1):
                        q = p + len(r) + s
                        if q > L:
                            break
                        if val > best[i + 1].get(q, NEG):
                            best[i + 1][q] = val; back[i + 1][q] = (p, True)
    out = [False] * K
    if not best[K]:
        return out
    p = max(best[K], key=lambda q: (best[K][q], -q))
    for i in range(K, 0, -1):
        pp, m = back[i][p]
        out[i - 1] = m
        p = pp
    return out


def score_part2(segs, table, detail=None):
    sc = ag = 0
    for seg, c in segs:
        res = align_bounded(seg, c, table)
        for t, m in zip(seg, res):
            if detail is not None:
                detail.append((t, m))
            if t["scored"]:
                sc += 1; ag += m
    return sc, ag


# ---------------------------------------------------------------- data, controls, main
def load():
    d = {}
    code = {}
    for f in ("no85_0196L", "no74_0168L", "no74_0168R"):
        a = parse_code(f"{OUT}/trans_A/{f}.txt"); b = parse_code(f"{OUT}/trans_B/{f}.txt")
        mark_scored(a, b)
        code[f] = (a, b)
    for base, k in (("A", 0), ("B", 1)):
        p1 = part1_units(code["no85_0196L"][k])
        clerk = clerk_stream(f"{OUT}/trans_{base}/no74clerk_0170_0171.txt")
        stream = part2_stream(code["no74_0168L"][k], code["no74_0168R"][k])
        d[base] = dict(part1=p1, part2=split_by_anchors(stream, clerk), clerk_len=len(clerk))
    return d


def frac(x):
    return x[1] / x[0] if x[0] else 0.0


def synthetic_tables(table, n, seed):
    freq = "eeeeeeeeeeeetttttttttaaaaaaaaooooooooiiiiiiinnnnnnnsssssshhhhhhrrrrrrddddllllcccuuummmwwffggyyppbbvk"
    rng = random.Random(seed)
    keys = sorted(table, key=int)
    lens = [len(norm_reading(table[k])) for k in keys]
    for _ in range(n):
        yield {k: "".join(rng.choice(freq) for _ in range(l)) for k, l in zip(keys, lens)}


def shuffled_tables(table, n, seed):
    rng = random.Random(seed)
    keys = sorted(table, key=int)
    vals = [table[k] for k in keys]
    for _ in range(n):
        v = vals[:]
        rng.shuffle(v)
        yield dict(zip(keys, v))


def summ(xs):
    s = sorted(xs)
    return f"max {max(s):.3f}  mean {statistics.mean(s):.3f}  95th {s[int(0.95 * (len(s) - 1))]:.3f}"


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    d = load()
    if mode == "counts":
        for base in "AB":
            p1 = d[base]["part1"]; segs = d[base]["part2"]
            n2 = [t for s, _ in segs for t in s]
            print(f"base {base}: part1 numbers {len(p1)}, scored {sum(t['scored'] for t in p1)}, segments {len(segments(p1))};"
                  f" part2 tokens {len(n2)}, scored {sum(t['scored'] for t in n2)}, segments {len(segs)},"
                  f" clerk letters {d[base]['clerk_len']}, error groups found {sum(1 for t in n2 if t.get('error_group'))}")
        return
    table = load_table()
    if mode == "pilot":
        r1, r2 = [], []
        for t in synthetic_tables(table, 200, SEED + 1):
            r1.append(frac(score_part1(d["A"]["part1"], t))); r2.append(frac(score_part2(d["A"]["part2"], t)))
        print("PILOT on 200 synthetic tables (random letters, lengths of the real readings), base A")
        print("part1:", summ(r1)); print("part2:", summ(r2))
        return
    if mode != "run":
        sys.exit(__doc__)
    print("TABLE", os.path.relpath(TABLE, HERE), "readings", len(table))
    verdicts = []
    for part, fn in (("part1", score_part1), ("part2", score_part2)):
        res = {}
        for base in "AB":
            det = []
            res[base] = fn(d[base][part], table, det)
            print(f"{part} base {base}: {res[base][1]} of {res[base][0]} scored numbers agree = {frac(res[base]):.3f}")
            with open(f"{OUT}/TEST_DETAIL_{part}_{base}.tsv", "w", encoding="utf-8") as fh:
                fh.write("line\traw\tscored\tagree\ttable_reading\tclerk_over_group\n")
                for t, m in det:
                    rd = "|".join(table.get(n, "") or "-" for n in t.get("cands", []))
                    fh.write(f"{t['line']}\t{t['raw']}\t{int(t['scored'])}\t{int(m)}\t{rd}\t{t.get('gloss', '')}\n")
        ctrl = [frac(fn(d["A"][part], t)) for t in shuffled_tables(table, N_SHUFFLES, SEED)]
        print(f"{part} control, {N_SHUFFLES} shuffles of the table's readings, base A: {summ(ctrl)}")
        nsc = res["A"][0]
        if nsc < MIN_SCORED[part]:
            v = "NOT ENOUGH DATA"
        elif max(ctrl) > CTRL_TOL[part]:
            v = "INCONCLUSIVE (control above tolerance)"
        elif frac(res["A"]) >= PASS_MARK and frac(res["B"]) >= PASS_MARK and frac(res["A"]) > max(ctrl):
            v = "PASS"
        else:
            v = "MISS"
        print(f"{part} verdict: {v}")
        verdicts.append(v)
    print("OVERALL:", "PASS" if all(v == "PASS" for v in verdicts) else "NOT PASSED (" + "; ".join(verdicts) + ")")


if __name__ == "__main__":
    main()
