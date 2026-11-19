"""Adjudication pipeline: when the AI and the human reference disagree, who is right?

Every error in RESULTS*.md is counted against the AI, but the DECODE reference has its own slips. This pipeline finds
the places where the AI readings agree with each other against the reference, shows each one to a blind adjudicator
with a crop of the page, and re-scores every model against a reference corrected where the adjudicator sided with
the AI.

Steps (each is one command; WORK is a scratch folder outside the repository, because the crops are DECODE images):

  python adjudicate.py extract WORK [--threshold K] [--calib N]
      Aligns the human reference with every AI pass in passes/, passes_opus/, passes_fable/ (9 readings per document),
      finds DISPUTES: reference positions where at least K readings (default: a majority of those available) agree on
      something other than the reference (a different sign, a missing sign, or an extra sign). Adjacent disputes are
      merged into one item. Long runs where the AI has nothing (a skipped line) are counted as omissions and not
      adjudicated. Adds a CALIBRATION sample of N items (default 60) where only one or two readings differ from the
      reference, to estimate how often an isolated AI deviation is in fact right.
      Writes adjudication/items.json (text only, committed) and WORK/crops/<id>.jpg (page crops, not committed).

  python adjudicate.py batches WORK [--size 25] [--seed S]
      Shuffles the items and writes WORK/batches/batch_NN.json and WORK/batches/batch_NN_prompt.txt. Each prompt is
      self-contained: a blind adjudicator (any vision model; a person can use the same sheet) sees the crop, the
      context, and the two readings labelled A and B in random order, never which one is human.

  (run each prompt with a separate agent; each writes WORK/verdicts/batch_NN.jsonl, one line per item:
   {"id": ..., "verdict": "A" | "B" | "other" | "unclear", "seen": "<what is written, if other>"})

  python adjudicate.py apply WORK
      Collects the verdicts into adjudication/verdicts.jsonl, decodes A/B back to human/AI, builds the adjudicated
      reference stream per document (AI reading substituted where the verdict is AI or 'other' agrees with AI), and
      re-scores all 90 passes. Writes adjudication/summary.json and prints the before/after table.

  python adjudicate.py review WORK [--n 40]
      Writes WORK/review.html: a random sample of adjudicated items with their crops embedded, for a person to check
      the adjudicator (local file only; it embeds DECODE images).
"""
import argparse
import base64
import collections
import glob
import json
import os
import random
import re
import sys

from PIL import Image

import prep_tiles
import score

Image.MAX_IMAGE_PIXELS = None
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
ADJ = os.path.join(HERE, "adjudication")
MODELS = {"sonnet": "passes", "opus": "passes_opus", "fable": "passes_fable"}
GAP = ""


# ---------------------------------------------------------------- reference structure
def ref_structure(doc):
    """Reference stream as scored by score.py, with (page, line, lines_on_page) for every character."""
    al = doc in score.ALNUM_DOCS
    txt = open(os.path.join(ROOT, score.REF[doc]), encoding="utf-8-sig", errors="replace").read()
    txt = re.sub(r"<[^>]*>", " ", txt, flags=re.S)
    pages, cur = [], None
    for l in txt.splitlines():
        m = re.match(r"^#IMAGE NAME\s*:\s*(.+)$", l.strip())
        if m:
            names = re.findall(r"[\w]+\.(?:png|jpg|jpeg|tif)", m.group(1), flags=re.I)
            if len(names) != 1:  # a range header such as '5499.png - 5501.png'
                continue
            cur = {"name": names[0], "lines": []}
            pages.append(cur)
            continue
        if not l.strip() or l.lstrip().startswith("#"):
            continue
        if cur is None:
            cur = {"name": None, "lines": []}
            pages.append(cur)
        cur["lines"].append(l)
    pages = [p for p in pages if p["lines"]]
    stream, where = [], []
    for pi, p in enumerate(pages):
        n = len(p["lines"])
        for li, l in enumerate(p["lines"]):
            d = score.digits(l, alnum=al)
            stream.append(d)
            where += [(pi, li, n)] * len(d)
    s = "".join(stream)
    check = score.digits("".join(score.ref_lines(score.REF[doc])), alnum=al)
    assert s == check, (doc, len(s), len(check))
    return s, where, pages


def tile_page_for(doc, pages):
    """Map reference page index -> index into prep_tiles.DOCS[doc] pages (by image number, else by order)."""
    tpages = prep_tiles.DOCS[doc][1]
    nums = [re.search(r"_I(\d+)_", n).group(1) if re.search(r"_I(\d+)_", n) else None for n, _ in tpages]
    out = {}
    for pi, p in enumerate(pages):
        k = None
        if p["name"]:
            m = re.match(r"(\d+)\.", p["name"])
            if m and m.group(1) in nums:
                k = nums.index(m.group(1))
        out[pi] = k if k is not None else min(pi, len(tpages) - 1)
    return out


# ---------------------------------------------------------------- alignment
def align(a, b):
    """Levenshtein alignment of reference a to hypothesis b ('?' in b never matches).
    Returns (aligned, inserted): aligned[i] = char of b aligned to a[i] or '' ; inserted[i] = chars of b before a[i]
    (inserted[len(a)] = chars after the end)."""
    n, m = len(a), len(b)
    prev = list(range(m + 1))
    back = [bytearray(m + 1) for _ in range(n + 1)]
    for j in range(1, m + 1):
        back[0][j] = 3
    for i in range(1, n + 1):
        cur = [i] + [0] * m
        back[i][0] = 2
        ai = a[i - 1]
        for j in range(1, m + 1):
            bj = b[j - 1]
            d = prev[j - 1] + (0 if ai == bj else 1)
            u = prev[j] + 1
            lft = cur[j - 1] + 1
            if d <= u and d <= lft:
                cur[j] = d
                back[i][j] = 0 if ai == bj else 1
            elif u <= lft:
                cur[j] = u
                back[i][j] = 2
            else:
                cur[j] = lft
                back[i][j] = 3
        prev = cur
    aligned = [GAP] * n
    inserted = [""] * (n + 1)
    i, j = n, m
    while i > 0 or j > 0:
        op = back[i][j]
        if op in (0, 1):
            aligned[i - 1] = b[j - 1]
            i, j = i - 1, j - 1
        elif op == 2:
            aligned[i - 1] = GAP
            i -= 1
        else:
            inserted[i] = b[j - 1] + inserted[i]
            j -= 1
    return aligned, inserted


def readings(doc):
    """All AI hypothesis streams for a document: list of (model, pass, stream)."""
    al = doc in score.ALNUM_DOCS
    out = []
    for model, d in MODELS.items():
        for p in (1, 2, 3):
            f = os.path.join(HERE, d, f"pass{p}_{doc}.txt")
            if os.path.exists(f):
                hl = score.hyp_lines(f)
                out.append((model, p, score.digits("".join(l.rstrip("! ") for l in hl), keep_q=True, alnum=al)))
    return out


# ---------------------------------------------------------------- crops
_page_cache = {}


def page_image(doc, tpi):
    key = (doc, tpi)
    if key not in _page_cache:
        folder, pages = prep_tiles.DOCS[doc]
        name, rot = pages[tpi]
        im = Image.open(os.path.join(ROOT, "targets", folder, name)).convert("RGB")
        if rot:
            im = im.rotate(-rot, expand=True)
        if im.width > prep_tiles.MAXW:
            im = im.resize((prep_tiles.MAXW, round(im.height * prep_tiles.MAXW / im.width)), Image.LANCZOS)
        _page_cache.clear()
        _page_cache[key] = im
    return _page_cache[key]


def crop_for(doc, tpi, line, nlines, path, half=0.22):
    im = page_image(doc, tpi)
    y = (line + 0.5) / max(1, nlines)
    top = max(0.0, y - half)
    bot = min(1.0, top + 2 * half)
    top = max(0.0, bot - 2 * half)
    im.crop((0, int(top * im.height), im.width, int(bot * im.height))).save(path, quality=88)
    return round(top, 3), round(bot, 3)


# ---------------------------------------------------------------- extract
def extract(work, threshold=None, calib=60, seed=20261119):
    os.makedirs(ADJ, exist_ok=True)
    os.makedirs(os.path.join(work, "crops"), exist_ok=True)
    rng = random.Random(seed)
    items, minority_pool, omissions = [], [], collections.Counter()
    for doc in score.REF:
        ref, where, pages = ref_structure(doc)
        tmap = tile_page_for(doc, pages)
        hyps = readings(doc)
        if not hyps:
            continue
        K = threshold or (len(hyps) // 2 + 1)
        al = [align(ref, h) for _, _, h in hyps]
        print(doc, "aligned", len(hyps), "readings,", len(ref), "reference signs", flush=True)
        events = []  # (pos, kind, ai_str)
        for i in range(len(ref) + 1):
            # extra signs before position i
            ins = collections.Counter(a[1][i] for a in al if a[1][i])
            if ins:
                s, c = ins.most_common(1)[0]
                if c >= K and len(s) <= 3:
                    events.append((i - 0.5, "ins", s))
            if i == len(ref):
                break
            col = collections.Counter(a[0][i] for a in al)
            s, c = col.most_common(1)[0]
            if s != ref[i] and c >= K:
                events.append((i, "sub" if s else "del", s))
            elif col[ref[i]] >= len(hyps) - 2 and col[ref[i]] < len(hyps):
                devs = [(hyps[k][0], hyps[k][1], al[k][0][i]) for k in range(len(hyps)) if al[k][0][i] != ref[i]]
                minority_pool.append((doc, i, devs))
        # merge events closer than 3 positions
        groups = []
        for ev in events:
            if groups and ev[0] - groups[-1][-1][0] <= 2.5:
                groups[-1].append(ev)
            else:
                groups.append([ev])
        for g in groups:
            a = int(min(e[0] for e in g) + 0.5) if g[0][1] == "ins" else int(g[0][0])
            a = max(0, min(a, len(ref) - 1))
            b = max(int(e[0]) + 1 if e[1] != "ins" else int(e[0] + 0.5) for e in g)
            b = max(b, a + 1) if any(e[1] != "ins" for e in g) else max(b, a)
            human = ref[a:b]
            # AI consensus string over [a, b): insertion before each position + majority sign at it
            evmap = {e[0]: e for e in g}
            ai = ""
            for i in range(a, b + 1):
                e = evmap.get(i - 0.5)
                if e:
                    ai += e[2]
                if i < b:
                    e = evmap.get(i)
                    ai += e[2] if e else ref[i]
            if len(human) > 6 and not ai:
                omissions[doc] += len(human)
                continue
            if human == ai:
                continue
            pi, li, n = where[min(a, len(where) - 1)]
            per = {f"{hyps[k][0]}{hyps[k][1]}": "".join(
                (al[k][1][i] if (a < i < b or (i - 0.5) in evmap) else "") + (al[k][0][i] if i < b else "")
                for i in range(a, b + 1)) for k in range(len(hyps))}
            items.append({"doc": doc, "kind": "dispute", "pos": [a, b], "human": human, "ai": ai,
                          "left": ref[max(0, a - 12):a], "right": ref[b:b + 12],
                          "page": tmap[pi] + 1, "line": li + 1, "lines_on_page": n, "readings": per})
    rng.shuffle(minority_pool)
    for doc, i, devs in minority_pool[:calib]:
        ref, where, pages = ref_structure(doc)
        tmap = tile_page_for(doc, pages)
        pi, li, n = where[i]
        dev = devs[0][2]
        items.append({"doc": doc, "kind": "calibration", "pos": [i, i + 1], "human": ref[i], "ai": dev,
                      "left": ref[max(0, i - 12):i], "right": ref[i + 1:i + 13],
                      "page": tmap[pi] + 1, "line": li + 1, "lines_on_page": n,
                      "readings": {f"{m}{p}": c for m, p, c in devs}})
    for k, it in enumerate(items):
        it["id"] = f"adj{k:04d}"
        top, bot = crop_for(it["doc"], it["page"] - 1, it["line"] - 1, it["lines_on_page"],
                            os.path.join(work, "crops", it["id"] + ".jpg"))
        it["crop_band"] = [top, bot]
    json.dump({"threshold": threshold or "majority", "omitted_signs_line_skips": dict(omissions), "items": items},
              open(os.path.join(ADJ, "items.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    c = collections.Counter((it["doc"], it["kind"]) for it in items)
    for k in sorted(c):
        print(k, c[k])
    print("items:", len(items), "omitted signs in AI line skips:", dict(omissions))


# ---------------------------------------------------------------- batches
PROMPT = """You are adjudicating disagreements between two transcriptions of handwritten cipher manuscripts. For each item
you get an image crop of the page, the signs just before and after the disputed spot, and two candidate readings of
the disputed spot, A and B. One of them may be empty (meaning: no sign there). Find the spot in the crop by its
context, look carefully at what is written, and decide which reading matches the manuscript.

Rules:
- Judge only what is written on the page. Do not prefer a reading because it looks more regular or more likely.
- Old hands write some digits in unfamiliar shapes (a 4 that looks like an open 'a', a 5 like an 's', a crossed 1).
  When a shape is ambiguous, compare it with the same shape elsewhere on the page and with the other digits the
  writer forms, and decide what that writer means by it.
- Crosses, bars, dots and strokes attached to a sign are not part of the reading; letters are compared in lower case.
- Answer "A", "B", "other" (neither; then write in "seen" exactly what is written at that spot) or "unclear" (cannot
  be decided from the image, or the spot cannot be found).
- If the crop does not show the spot, open the listed page tiles (with the Read tool) and look for it there.
- Use ONLY the images named below. Do not open, list or search any other file or folder, and do not use the web.

Write your answers to {out} with the Write tool, as JSON Lines, one line per item, in this form:
{{"id": "adj0001", "verdict": "A", "seen": ""}}
Write the file once at the end with all {n} lines. Then reply with the file path and the counts of A, B, other and
unclear. Nothing else.

Items:
{items}
"""


def batches(work, size=25, seed=7, adjudicators=("opus", "fable")):
    data = json.load(open(os.path.join(ADJ, "items.json"), encoding="utf-8"))
    items = data["items"]
    rng = random.Random(seed)
    order = list(range(len(items)))
    rng.shuffle(order)
    bdir = os.path.join(work, "batches")
    os.makedirs(bdir, exist_ok=True)
    os.makedirs(os.path.join(work, "verdicts"), exist_ok=True)
    nb = 0
    for s in range(0, len(order), size):
        nb += 1
        rows, keys = [], {}
        for k in order[s:s + size]:
            it = items[k]
            human_first = rng.random() < 0.5
            A, B = (it["human"], it["ai"]) if human_first else (it["ai"], it["human"])
            keys[it["id"]] = "human" if human_first else "ai"  # what A is
            tdir = os.path.join(work, "tiles_all")
            tile_list = sorted(glob.glob(os.path.join(tdir, f"{it['doc']}_p{it['page']}_t*.jpg")))
            rows.append(f"- id {it['id']}: crop {os.path.join(work, 'crops', it['id'] + '.jpg')}\n"
                        f"  page tiles: {', '.join(tile_list) if tile_list else '(none)'}\n"
                        f"  approx. line {it['line']} of {it['lines_on_page']} cipher lines on the page\n"
                        f"  before: \"{it['left']}\"   after: \"{it['right']}\"\n"
                        f"  A: \"{A}\"   B: \"{B}\"")
        json.dump({"key": keys, "ids": [items[k]["id"] for k in order[s:s + size]]},
                  open(os.path.join(bdir, f"batch_{nb:02d}.json"), "w"), indent=1)
        for name in adjudicators:  # each adjudicator answers the same blind sheet into its own folder
            os.makedirs(os.path.join(work, "verdicts", name), exist_ok=True)
            out = os.path.join(work, "verdicts", name, f"batch_{nb:02d}.jsonl")
            open(os.path.join(bdir, f"batch_{nb:02d}_{name}_prompt.txt"), "w", encoding="utf-8").write(
                PROMPT.format(out=out, n=len(rows), items="\n".join(rows)))
    print(nb, "batches of up to", size, "in", bdir)


# ---------------------------------------------------------------- apply
def apply(work):
    data = json.load(open(os.path.join(ADJ, "items.json"), encoding="utf-8"))
    items = {it["id"]: it for it in data["items"]}
    vroot = os.path.join(work, "verdicts")
    names = sorted(d for d in os.listdir(vroot) if os.path.isdir(os.path.join(vroot, d)))
    per_adj = {}
    for name in names:
        per_adj[name] = read_verdicts(work, name, items)
        print(name, "verdicts:", len(per_adj[name]), dict(collections.Counter(v["side"] for v in per_adj[name].values())))
    # combined verdict: counted only where every adjudicator gave the same side; otherwise 'split'
    verdicts = {}
    for vid in items:
        sides = {n: per_adj[n][vid]["side"] for n in names if vid in per_adj[n]}
        if not sides or len(sides) < len(names):
            continue
        vals = set(sides.values())
        verdicts[vid] = {"id": vid, "side": vals.pop() if len(vals) == 1 else "split", "by": sides,
                         "seen": {n: per_adj[n][vid].get("seen", "") for n in names}}
    print("answered by all adjudicators:", len(verdicts), " agreed:",
          sum(1 for v in verdicts.values() if v["side"] != "split"))
    _finish(items, verdicts)


def read_verdicts(work, name, items):
    verdicts = {}
    for bf in sorted(glob.glob(os.path.join(work, "batches", "batch_*.json"))):
        key = json.load(open(bf))["key"]
        vf = os.path.join(work, "verdicts", name, os.path.basename(bf).replace(".json", ".jsonl"))
        if not os.path.exists(vf):
            print("missing verdicts:", vf)
            continue
        for l in open(vf, encoding="utf-8"):
            l = l.strip()
            if not l:
                continue
            v = json.loads(l)
            if v["id"] not in key:
                continue
            a_is = key[v["id"]]
            raw = str(v.get("verdict", "")).strip()
            it = items[v["id"]]
            if raw in ("A", "B"):
                side = a_is if raw == "A" else ("ai" if a_is == "human" else "human")
            elif raw.lower() == "other":
                seen = re.sub(r"[^0-9a-z]", "", str(v.get("seen", "")).lower())
                side = "ai" if seen == it["ai"] else ("human" if seen == it["human"] else "neither")
            else:
                side = "unclear"
            verdicts[v["id"]] = {"id": v["id"], "verdict": raw, "seen": v.get("seen", ""), "side": side}
    return verdicts


def _finish(items, verdicts):
    with open(os.path.join(ADJ, "verdicts.jsonl"), "w", encoding="utf-8") as fh:
        for k in sorted(verdicts):
            fh.write(json.dumps(verdicts[k], ensure_ascii=False) + "\n")
    # tallies
    tally = collections.defaultdict(collections.Counter)
    for vid, v in verdicts.items():
        it = items[vid]
        tally[(it["kind"], it["doc"])][v["side"]] += 1
        tally[(it["kind"], "ALL")][v["side"]] += 1
    # adjudicated reference per document: substitute the AI reading where the adjudicator sided with the AI
    adj_ref = {}
    for doc in score.REF:
        ref, _, _ = ref_structure(doc)
        subs = sorted(((it["pos"][0], it["pos"][1], it["ai"]) for vid, it in items.items()
                       if it["doc"] == doc and verdicts.get(vid, {}).get("side") == "ai"), reverse=True)
        s = ref
        for a, b, ai in subs:
            s = s[:a] + ai + s[b:]
        adj_ref[doc] = (ref, s)
    rows = []
    for model, d in MODELS.items():
        for doc in score.REF:
            ref, s = adj_ref[doc]
            al = doc in score.ALNUM_DOCS
            for p in (1, 2, 3):
                f = os.path.join(HERE, d, f"pass{p}_{doc}.txt")
                if not os.path.exists(f):
                    continue
                h = score.digits("".join(l.rstrip("! ") for l in score.hyp_lines(f)), keep_q=True, alnum=al)
                rows.append({"model": model, "doc": doc, "pass": p, "ref_len": len(ref), "adj_len": len(s),
                             "edits_orig": score.lev_ops(ref, h)[3], "edits_adj": score.lev_ops(s, h)[3]})
    summ = {"tally": {f"{k[0]}|{k[1]}": dict(v) for k, v in tally.items()}, "rows": rows}
    json.dump(summ, open(os.path.join(ADJ, "summary.json"), "w"), indent=1)
    print("verdicts:", len(verdicts), "of", len(items))
    for k in sorted(tally):
        if k[1] == "ALL":
            print(k, dict(tally[k]))
    print("\nmodel        orig CER   adjudicated CER")
    for model in MODELS:
        r = [x for x in rows if x["model"] == model]
        if r:
            o = sum(x["edits_orig"] for x in r) / sum(x["ref_len"] for x in r)
            a = sum(x["edits_adj"] for x in r) / sum(x["adj_len"] for x in r)
            print(f"{model:10s}  {100 * o:6.2f}%   {100 * a:6.2f}%")


# ---------------------------------------------------------------- review sheet
def review(work, n=40, seed=3):
    data = json.load(open(os.path.join(ADJ, "items.json"), encoding="utf-8"))
    items = {it["id"]: it for it in data["items"]}
    vs = [json.loads(l) for l in open(os.path.join(ADJ, "verdicts.jsonl"), encoding="utf-8")]
    rng = random.Random(seed)
    rng.shuffle(vs)
    parts = ["<!doctype html><meta charset=utf-8><title>Adjudication review</title><style>body{font:15px sans-serif;"
             "max-width:1100px;margin:auto;padding:16px}img{max-width:100%;border:1px solid #999}.it{margin:28px 0}"
             "code{font-size:17px;background:#eee;padding:2px 5px}</style><h1>Adjudication review sample</h1>"
             "<p>For each item: find the spot by its context and note whether the verdict is right.</p>"]
    for v in vs[:n]:
        it = items[v["id"]]
        b64 = base64.b64encode(open(os.path.join(work, "crops", it["id"] + ".jpg"), "rb").read()).decode()
        parts.append(f"<div class=it><h3>{it['id']} &middot; {it['doc']} p{it['page']} line {it['line']}/"
                     f"{it['lines_on_page']} &middot; {it['kind']}</h3><p>before <code>{it['left']}</code> &nbsp; "
                     f"after <code>{it['right']}</code></p><p>human <code>{it['human'] or '(nothing)'}</code> &nbsp; "
                     f"AI <code>{it['ai'] or '(nothing)'}</code> &nbsp; adjudicator: <b>{v['side']}</b>"
                     f" {json.dumps(v.get('by', {}))}</p><img src='data:image/jpeg;base64,{b64}'></div>")
    open(os.path.join(work, "review.html"), "w", encoding="utf-8").write("\n".join(parts))
    print("wrote", os.path.join(work, "review.html"))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("step", choices=["extract", "batches", "apply", "review"])
    ap.add_argument("work")
    ap.add_argument("--threshold", type=int)
    ap.add_argument("--calib", type=int, default=60)
    ap.add_argument("--size", type=int, default=25)
    ap.add_argument("--n", type=int, default=40)
    a = ap.parse_args()
    {"extract": lambda: extract(a.work, a.threshold, a.calib), "batches": lambda: batches(a.work, a.size),
     "apply": lambda: apply(a.work), "review": lambda: review(a.work, a.n)}[a.step]()
