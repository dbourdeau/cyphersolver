"""Third reader: each page-half read in overlapping full-resolution horizontal strips, then stitched.

Why: whole-half reads at ~2-3k px make digits tiny and 8 is read as 0 ("20" for 28, "10" for 18).
A strip is read at the original pixel size. The key is never shown to the reader.

  python3 analysis/strips.py cut HALF --height 0.15 --overlap 0.06      # just write the strip files
  python3 analysis/strips.py read HALF... --model M --height 0.15 --overlap 0.06 --out data/strips_pilot.jsonl
  python3 analysis/strips.py eval data/strips_pilot.jsonl
HALF is "volume/pNNNNL", e.g. dorffler-19-102/p0483R. height/overlap below 1 are fractions of the
image height, otherwise pixels of the ORIGINAL image. Needs Pillow (use the Xcode python3) and `llm`.
Done-test: every (half, model, height, overlap) has a row without "error". A lock stops a second copy.
"""
import argparse, collections, concurrent.futures as cf, difflib, fcntl, json, os, re, sys, time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common as P
import p5

HALVES = os.environ.get("CIPHER_HALVES") or os.path.join(P.D, "halves")
WORK = os.path.join(P.D, "strips_work")
SIM = 0.6          # duplicate threshold
WINDOW = 10        # lines examined at each end of a seam
MAX_CALLS = int(os.environ.get("STRIPS_MAX_CALLS", "200"))   # raise on purpose for a full run
BLIND_DIR = os.environ.get("CIPHER_BLIND", "blind")   # optional independent reads, {"half","lines":[{"numbers":[...]}]}
BLIND = {"dorffler-19-102/p0483R": BLIND_DIR + "/blind_102_0483R/read.json",
         "dorffler-19-101/p0219L": BLIND_DIR + "/blind_101_0219L/read.json"}

PROMPT = """This is a horizontal STRIP cut from one page-half of a 1680s German diplomatic despatch. Parts of the text are in a numeric cipher: numbers separated by dots, e.g. "218. 77. 53.", often in the middle of ordinary German sentences. Above some cipher runs a later hand wrote the decryption in small letters, in the gap between lines.

Transcribe the manuscript lines in this strip, top to bottom, one output line per manuscript line, each starting with a tag:
L: an ordinary manuscript line. Write German words as they stand (old spelling, no modernising) and cipher numbers inline exactly as written, dot-separated with no spaces, e.g.  L: und habe ich 179.60.121.87 nicht erfahren
G: a small interlinear decryption written in the gap ABOVE the next L line. Write only its words, in order, e.g.  G: dieser Materie
Rules:
- Skip any line that is cut by the top or bottom edge of this image. Transcribe only lines that are fully visible. A G line cut by an edge is skipped too.
- Every digit exactly as written. If one digit is unreadable write ? for it, e.g. 1?5. Never guess a digit from sense or from the surrounding words. If a number has two dots or a stroke above it, append " after it, e.g. 29"
- Never invent or repeat numbers to fill a line. If you are unsure of a word, write [?].
- Keep the manuscript's line order. A G line always comes directly before the L line it sits above.
Output only the tagged lines."""


# ---------- cut ----------

def px(v, total):
    return int(round(v * total)) if v < 1 else int(v)


def cut(image, height, overlap, out_dir=None):
    """Full-width strips of `height` px stepping by height-overlap. Returns [(y0, y1, path)]."""
    from PIL import Image
    im = Image.open(image)
    w, h = im.size
    H, O = px(height, h), px(overlap, h)
    assert O < H, "overlap must be smaller than strip height"
    if out_dir is None:
        v, f = os.path.split(image)
        out_dir = os.path.join(WORK, os.path.basename(v), "%s_h%d_o%d" % (f[:-4], H, O))
    os.makedirs(out_dir, exist_ok=True)
    ys, y = [], 0
    while True:
        if y + H >= h:
            ys.append(max(0, h - H))
            break
        ys.append(y)
        y += H - O
    out = []
    for k, y0 in enumerate(ys):
        p = os.path.join(out_dir, "s%02d.jpg" % k)
        if not os.path.exists(p):
            im.crop((0, y0, w, min(h, y0 + H))).save(p, quality=95)
        out.append((y0, min(h, y0 + H), p))
    return out


# ---------- stitch ----------

def line_key(line):
    ns = [n for n in p5.nums_of(line)] if line["tag"] == "L" else []
    return ("n", ns) if ns else ("t", P.norm(line["text"].replace("[?]", "")))


def same_line(a, b):
    if a["tag"] != b["tag"]:
        return 0.0
    ka, kb = line_key(a), line_key(b)
    if ka[0] != kb[0]:
        # one copy shows numbers the other lacks: compare the letters instead
        ka, kb = ("t", P.norm(re.sub(r"[\d.?\" ]+", "", a["text"]))), ("t", P.norm(re.sub(r"[\d.?\" ]+", "", b["text"])))
    if ka[0] == "t" and (len(ka[1]) < 4 or len(kb[1]) < 4):
        return 0.0
    q = difflib.SequenceMatcher(None, ka[1], kb[1], autojunk=False).ratio()
    return q if q >= SIM else 0.0


def stitch(strip_texts, verbose=True):
    """strip_texts: tagged-line texts, top strip first. Returns (lines, seam_drops) where lines is a
    list of {'tag','text'} and seam_drops[k] = duplicates dropped between strip k and k+1."""
    strips = [p5.parse(t) for t in strip_texts]
    res = [dict(l, strip=0, pos=i, n=len(strips[0])) for i, l in enumerate(strips[0])]
    drops = []
    for k in range(1, len(strips)):
        cur = strips[k]
        tail_ix = [i for i, r in enumerate(res) if r["strip"] == k - 1][-WINDOW:]
        ptr, dropped, replaced = 0, 0, {}
        head_skip = set()
        for j, line in enumerate(cur[:WINDOW]):
            best, bq = None, 0.0
            for t in range(ptr, len(tail_ix)):
                q = same_line(res[tail_ix[t]], line)
                if q > bq:
                    best, bq = t, q
            if best is None:
                continue
            ptr = best + 1
            old = res[tail_ix[best]]
            d_old = old["n"] - 1 - old["pos"]       # distance from the bottom edge of strip k-1
            d_new = j                                # distance from the top edge of strip k
            dropped += 1
            if d_new > d_old:
                replaced[tail_ix[best]] = dict(line, strip=k, pos=j, n=len(cur))
            head_skip.add(j)
        for i, r in replaced.items():
            res[i] = r
        res += [dict(l, strip=k, pos=j, n=len(cur)) for j, l in enumerate(cur) if j not in head_skip]
        drops.append(dropped)
    return [{"tag": r["tag"], "text": r["text"]} for r in res], drops


# ---------- read ----------

def cfg_of(half, model, h, o):
    return (half, model, h, o)


def image_of(half):
    v, p = half.split("/")
    return os.path.join(HALVES, v, p + ".jpg")


def ask(model, image, prompt, extra, timeout=600, tier="standard"):
    """common.ask plus extra `llm -o key value` options (e.g. max_output_tokens for 3.x models)."""
    err = ""
    opts = ["-o", "tier", tier] + [x for kv in extra for x in ("-o",) + tuple(kv.split("=", 1))]
    for _ in range(2):
        try:
            r = P.sh("llm", "-n", "-m", model, *opts, "-a", image, prompt, timeout=timeout)
            if r.returncode == 0 and r.stdout.strip():
                return r.stdout.strip(), None
            err = r.stderr[-200:]
        except Exception as e:
            err = str(e)[:200]
    return None, err


def read(args):
    lock = open(args.out + ".lock", "w")
    try:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError:
        raise SystemExit("another copy holds " + args.out + ".lock")
    done = set()
    if os.path.exists(args.out):
        for l in open(args.out):
            r = json.loads(l)
            if "error" not in r:
                done.add((r["half"], r["model"], r["height"], r["overlap"]))
    jobs = []
    for half in args.halves:
        key = (half, args.model, args.height, args.overlap)
        if key in done:
            continue
        for k, (y0, y1, path) in enumerate(cut(image_of(half), args.height, args.overlap)):
            jobs.append((half, k, path))
    n_halves = len({j[0] for j in jobs})
    print("%d strip calls for %d halves (cap %d)" % (len(jobs), n_halves, MAX_CALLS), flush=True)
    if len(jobs) > MAX_CALLS:
        raise SystemExit("ABORT: would exceed the call cap")
    t0 = time.time()

    def one(job):
        half, k, path = job
        text, err = ask(args.model, path, PROMPT, args.llm_opt)
        return job, text, err

    calls = bad = 0
    todo = sorted({j[0] for j in jobs})
    with cf.ThreadPoolExecutor(8) as ex, open(args.out, "a") as o:
        for c in range(0, len(todo), 8):  # 8 halves at a time, written as they finish: a stop loses little
            chunk = set(todo[c:c + 8])
            cjobs = [j for j in jobs if j[0] in chunk]
            got = collections.defaultdict(dict)
            errs = collections.defaultdict(list)
            for job, text, err in ex.map(one, cjobs):
                calls += 1
                if text is None:
                    bad += 1
                    errs[job[0]].append("strip %d: %s" % (job[1], err))
                else:
                    got[job[0]][job[1]] = text
                if calls == 16 and bad == 16:
                    raise SystemExit("ABORT: first 16 calls all failed: " + str(err)[-200:])
            for half in sorted(chunk):
                base = {"half": half, "model": args.model, "height": args.height, "overlap": args.overlap}
                nstrips = len([j for j in cjobs if j[0] == half])
                if errs[half] or len(got[half]) != nstrips:
                    rec = dict(base, error="; ".join(errs[half])[:300] or "missing strips")
                else:
                    raw = [got[half][k] for k in range(nstrips)]
                    lines, drops = stitch(raw, verbose=False)
                    print("%s h=%s o=%s: strips %d, lines %d, dups dropped per seam %s%s"
                          % (half, args.height, args.overlap, nstrips, len(lines), drops,
                             "  RED FLAG" if redflag(drops) else ""), flush=True)
                    rec = dict(base, opts=args.llm_opt, text="\n".join("%s: %s" % (l["tag"], l["text"]) for l in lines),
                               seam_drops=drops, strips=nstrips, raw=raw)
                o.write(json.dumps(rec, ensure_ascii=False) + "\n")
                o.flush()
    print("calls %d, failures %d, wall %.0fs" % (calls, bad, time.time() - t0))


def redflag(drops):
    """Zero dropped at a seam, or far more than the ~2-4 lines (G+L) a 6% overlap holds."""
    return any(d == 0 or d > 8 for d in drops)


# ---------- eval ----------

def cipher_tokens(rows):
    return [n for r in rows if r["tag"] == "L" for n in p5.nums_of(r)]


def out_of_system(t):
    return t.startswith("0") or "?" in t or (t.isdigit() and int(t) < 14)


def rows_of(half, text):
    return [{"half": half, "i": i, "tag": l["tag"], "text": l["text"]} for i, l in enumerate(p5.parse(text))]


def agree(ref, new):
    if not ref:
        return float("nan")
    sm = difflib.SequenceMatcher(None, ref, new, autojunk=False)
    return sum(b.size for b in sm.get_matching_blocks()) / len(ref)


def subs(ref, new, c):
    sm = difflib.SequenceMatcher(None, ref, new, autojunk=False)
    for tag, a0, a1, b0, b1 in sm.get_opcodes():
        if tag == "replace" and a1 - a0 == b1 - b0:
            for x, y in zip(ref[a0:a1], new[b0:b1]):
                c[(x, y)] += 1


def blind_tokens(path):
    d = json.load(open(path))
    return [n.rstrip('"') for l in d["lines"] for n in l.get("numbers", [])]


def evaluate(path):
    key = p5.load_key(os.path.join(P.D, "key_c04.json"))
    existing = collections.defaultdict(list)
    for r in p5.load_lines():
        existing[r["half"]].append(r)
    recs = [json.loads(l) for l in open(path)]
    recs = [r for r in recs if "error" not in r]
    cfgs = collections.OrderedDict()
    for r in recs:
        cfgs.setdefault((r["model"], r["height"], r["overlap"]), {})[r["half"]] = r
    hdr = "%-22s %-24s %5s %7s %7s %5s %7s %7s"
    print(hdr % ("config", "half", "nums", "vsExist", "vsBlind", "oos", "gloss", "g.exist"))
    for cfg, byhalf in cfgs.items():
        name = "%s h%s o%s" % (cfg[0].split("/")[-1].replace("gemini-", ""), cfg[1], cfg[2])
        subc = collections.Counter()
        allnew, allex = [], []
        for half, r in sorted(byhalf.items()):
            rows = rows_of(half, r["text"])
            new, ex = cipher_tokens(rows), cipher_tokens(existing[half])
            pairs_new = p5.gloss_pairs(rows)
            pairs_ex = p5.gloss_pairs(existing[half])
            vb = "-"
            if half in BLIND and os.path.exists(BLIND[half]):
                vb = "%.3f" % agree(blind_tokens(BLIND[half]), new)
            print(hdr % (name, half, len(new), "%.3f" % agree(ex, new), vb, sum(map(out_of_system, new)),
                         "%.3f" % p5.gloss_score(key, pairs_new), "%.3f" % p5.gloss_score(key, pairs_ex)))
            subs(ex, new, subc)
            allnew += new; allex += ex
        print("   existing for the same halves: %d numbers, %d out-of-system" % (len(allex), sum(map(out_of_system, allex))))
        print("   top substitutions existing->strip:", ", ".join("%s>%s x%d" % (a, b, n) for (a, b), n in subc.most_common(15)))
        print("   seam drops:", {h: r.get("seam_drops") for h, r in sorted(byhalf.items())})
    print("blind-read numbers for context:", {h: len(blind_tokens(p)) for h, p in BLIND.items() if os.path.exists(p)})
    for half in sorted({h for b in cfgs.values() for h in b}):
        if half in BLIND and os.path.exists(BLIND[half]):
            print("existing vs blind %s: %.3f" % (half, agree(blind_tokens(BLIND[half]), cipher_tokens(existing[half]))))


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("cut", "read"):
        s = sub.add_parser(name)
        s.add_argument("halves", nargs="+")
        s.add_argument("--height", type=float, required=True)
        s.add_argument("--overlap", type=float, required=True)
        if name == "read":
            s.add_argument("--model", required=True)
            s.add_argument("--out", required=True)
            s.add_argument("--llm-opt", action="append", default=[], help="extra llm option key=value, repeatable")
    sub.add_parser("eval").add_argument("file")
    a = ap.parse_args()
    if a.cmd == "cut":
        for half in a.halves:
            for y0, y1, p in cut(image_of(half), a.height, a.overlap):
                print(half, y0, y1, p)
    elif a.cmd == "read":
        read(a)
    else:
        evaluate(a.file)


if __name__ == "__main__":
    main()
