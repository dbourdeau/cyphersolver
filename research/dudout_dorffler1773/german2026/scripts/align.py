"""Whole-half alignment of the clerk's decryptions to the cipher, with a same-procedure shuffled-key control.

The old score (p5.gloss_pairs) pairs each G line with the next two L lines. Here every candidate gloss
(each G line, plus each L line with no cipher numbers: "plain candidates", maybe a decryption the readers
tagged L) is matched against the cipher tokens within +-W lines, in blocks of 3+ letters, over a compact
token span. One span (or none) per G line, in page order, spans overlapping by <= 2 tokens, chosen by DP to
maximise matched letters. Plain candidates then go only into tokens no accepted G line claimed.
Searching a neighbourhood lifts the score of ANY key, so every figure is repeated with the key's values
shuffled among its numbers (the whole procedure re-run per draw). tau = smallest step-0.05 threshold at
which < 2% of fit-half G lines are accepted under shuffled keys. W and tau are chosen on the fit half only.

  python3 analysis/align.py run [KEY.json] [--draws 20] [--W 4]   # -> data/aligned.jsonl, misread_candidates.tsv, align_report.txt
  python3 analysis/align.py tune [KEY.json] [--draws 8]           # W grid on the fit half only
"""
import bisect, collections, difflib, json, multiprocessing as mp, os, random, sys, time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common as P
import p5
from common import norm

W_DEF, FLOOR, TOPK, MAXOV = 8, 0.10, 4, 2
LAM = float(os.environ.get('ALIGN_LAM', 0))
CONF = [("1", "7"), ("3", "8"), ("0", "8"), ("6", "8"), ("0", "6"), ("5", "6"), ("2", "7"), ("4", "9")]
SWAP = {}
for a, b in CONF:
    SWAP.setdefault(a, set()).add(b); SWAP.setdefault(b, set()).add(a)
H = {}  # half -> {"toks": [(line, pos, n)], "G": [(i, gloss)], "P": [(i, text)]}; set before the pool forks


def prep(lines):
    by = collections.defaultdict(list)
    for r in lines:
        by[r["half"]].append(r)
    for half, rs in by.items():
        toks, g, pl = [], [], []
        for r in rs:
            ns = [n for n in p5.nums_of(r) if n.isdigit()] if r["tag"] == "L" else []
            toks += [(r["i"], p, n) for p, n in enumerate(ns)]
            t = norm(r["text"].replace("[?]", ""))
            if r["tag"] == "G" and len(t) >= 4:
                g.append((r["i"], t))
            elif r["tag"] == "L" and not ns and not p5.nums_of(r) and len(t) >= 8:
                pl.append((r["i"], t))
        H[half] = {"toks": toks, "G": g, "P": pl}


def blocks_of(g, d):
    sm = difflib.SequenceMatcher(None, g, d, autojunk=False)
    return [b for b in sm.get_matching_blocks() if b.size >= 3]


def spans_for(g, i, toks, tl, pieces, W, blocked):
    """Top few (matched, ts, te) spans for gloss g on line i, inside tokens within +-W lines."""
    lo, hi = bisect.bisect_left(tl, i - W), bisect.bisect_right(tl, i + W)
    if hi <= lo:
        return []
    pc = pieces[lo:hi]
    starts, pos = [], 0
    for p in pc:
        starts.append(pos); pos += len(p)
    D = "".join(pc)
    bl = blocks_of(g, D)
    if not bl:
        return []
    lim = 2 * len(g) + 10
    tk = lambda x: bisect.bisect_right(starts, x) - 1
    cand = {}
    for a in range(len(bl)):
        s, m = tk(bl[a].b), 0
        for z in range(a, len(bl)):
            e = tk(bl[z].b + bl[z].size - 1)
            L = starts[e] + len(pc[e]) - starts[s]
            if L > lim:
                break
            m += bl[z].size
            sc = m - LAM * (L - m)  # compact spans: unmatched decoded letters inside cost LAM each
            if (s, e) not in cand or cand[(s, e)][0] < sc:
                cand[(s, e)] = (sc, m)
    out = []
    for (s, e), (sc, m) in sorted(cand.items(), key=lambda kv: (-kv[1][0], kv[0][1] - kv[0][0]))[:TOPK]:
        if blocked and any(t in blocked for t in range(lo + s, lo + e + 1)):
            continue
        m2 = sum(b.size for b in blocks_of(g, "".join(pc[s:e + 1])))
        if m2 >= 3 and m2 / len(g) >= FLOOR:
            out.append((m2, lo + s, lo + e, m2 - LAM * (sum(map(len, pc[s:e + 1])) - m2)))
    return out


def dp(opts):
    """opts[j] = list of (m, ts, te); one or none per line, in order, overlap <= MAXOV tokens. -> chosen per line."""
    f = [[o[3] for o in os_] for os_ in opts]
    bp = [[None] * len(os_) for os_ in opts]
    for j in range(len(opts)):
        for a, (m, ts, te, sc) in enumerate(opts[j]):
            for j2 in range(j):
                for b, (m2, ts2, te2, sc2) in enumerate(opts[j2]):
                    if ts >= te2 - MAXOV + 1 and f[j2][b] + sc > f[j][a]:
                        f[j][a] = f[j2][b] + sc; bp[j][a] = (j2, b)
    best, at = 0, None
    for j in range(len(opts)):
        for a in range(len(opts[j])):
            if f[j][a] > best:
                best, at = f[j][a], (j, a)
    pick = [None] * len(opts)
    while at:
        pick[at[0]] = at[1]
        at = bp[at[0]][at[1]]
    return pick


def align_half(h, key, W, kind, blocked=None):
    d = H[h]
    toks = d["toks"]
    tl = [t[0] for t in toks]
    pieces = [norm(key.get(t[2], "")) for t in toks]
    if blocked:
        pieces = ["" if k in blocked else p for k, p in enumerate(pieces)]
    cands = d[kind]
    opts = [spans_for(g, i, toks, tl, pieces, W, blocked) for i, g in cands]
    pick = dp(opts)
    return [(i, len(g), *(opts[j][pick[j]][:3] if pick[j] is not None else (0, -1, -1))) for j, (i, g) in enumerate(cands)]


def old_pairs(lines):
    return p5.gloss_pairs(lines)


def jobG(a):
    key, W, halves, pairs = a
    res = {h: align_half(h, key, W, "G") for h in halves}
    old = [(p["half"], p5.local_match(p["gloss"], "".join(norm(key.get(n, "")) for n in p["nums"])), len(p["gloss"])) for p in pairs]
    return res, old


def claimed_of(rows, tau):
    return {t for (i, gl, m, ts, te) in rows if m and m / gl >= tau for t in range(ts, te + 1)}


def jobP(a):
    key, W, res, tau = a
    return {h: align_half(h, key, W, "P", claimed_of(res[h], tau)) for h in res}


def run_keys(keys, W, halves, pairs, tau_fn):
    """keys[0] real, rest shuffled. Pass 1 (G + old), choose tau on shuffled fit, pass 2 (plain)."""
    ctx = mp.get_context("fork")
    with ctx.Pool(os.cpu_count()) as pool:
        r1 = pool.map(jobG, [(k, W, halves, pairs) for k in keys], chunksize=1)
        tau = tau_fn([r[0] for r in r1])
        r2 = pool.map(jobP, [(k, W, r[0], tau) for k, r in zip(keys, r1)], chunksize=1) if tau is not None else None
    return r1, tau, r2


def fold_of(h):
    return p5.fold(h)


def acc(rows, tau):
    return [(i, gl, m) for (i, gl, m, ts, te) in rows if m and m / gl >= tau]


def pick_tau(shuf, halves_sel):
    """Smallest tau (step .05) with mean shuffled G acceptance on the selected halves < 2%."""
    n = sum(len(H[h]["G"]) for h in halves_sel)
    for k in range(1, 21):
        tau = k * 0.05
        rates = [sum(len(acc(r[h], tau)) for h in halves_sel) / n for r in shuf]
        if sum(rates) / len(rates) < 0.02:
            return round(tau, 2)
    return 1.0


def mk_keys(key, draws):
    rng = random.Random(7)
    return [key] + [p5.shuffled(key, rng) for _ in range(draws)]


# ---------- tune ----------

def tune(keypath, draws):
    key = p5.load_key(keypath)
    lines = p5.load_lines(); prep(lines)
    fit = sorted(h for h in H if fold_of(h) == "fit")
    keys = mk_keys(key, draws)
    den = sum(len(g) for h in fit for _, g in H[h]["G"])
    for W in (2, 3, 4, 6, 8, 12):
        t0 = time.time()
        r1, tau, _ = run_keys(keys, W, fit, [], lambda rs: pick_tau(rs[1:], fit))
        sc = [sum(m for h in fit for (i, gl, m, ts, te) in r[0][h] if m and m / gl >= tau) / den for r in r1]
        print("W=%d tau=%.2f fit score real %.3f shuffled mean %.3f max %.3f margin %.3f (%.0fs)" % (
            W, tau, sc[0], sum(sc[1:]) / draws, max(sc[1:]), sc[0] - sum(sc[1:]) / draws, time.time() - t0), flush=True)


# ---------- details ----------

def detail(h, key, row, kind, tau):
    """Per-token classes for one accepted line."""
    i, gl, m, ts, te = row
    d = H[h]
    g = dict(d[kind])[i]
    tk = d["toks"][ts:te + 1]
    pcs = [norm(key.get(t[2], "")) for t in tk]
    D = "".join(pcs)
    bl = blocks_of(g, D)
    st, pos = [], 0
    for p in pcs:
        st.append(pos); pos += len(p)
    first, last = (bl[0].b, bl[-1].b + bl[-1].size) if bl else (0, 0)
    opp = {}
    for P_, N_ in zip(bl, bl[1:]):
        tp = bisect.bisect_right(st, P_.b + P_.size - 1) - 1
        tn = bisect.bisect_right(st, N_.b) - 1
        if P_.b + P_.size == st[tp] + len(pcs[tp]) and N_.b == st[tn] and tn - tp == 2:
            opp[tp + 1] = g[P_.a + P_.size:N_.a] or None
    span = []
    for k, (t, p) in enumerate(zip(tk, pcs)):
        a0, a1 = st[k], st[k] + len(p)
        if not p:
            cls = "unknown"
        elif any(b.b <= a0 and a1 <= b.b + b.size for b in bl):
            cls = "ok"
        elif a0 < first or a1 > last:
            cls = "edge"
        else:
            cls = "conflict"
        span.append([t[0], t[1], t[2], p, cls, opp.get(k)])
    return span


def alts(n):
    out = set()
    for k, c in enumerate(n):
        for r in SWAP.get(c, ()):
            out.add(n[:k] + r + n[k + 1:])
    if n.startswith("0") and len(n) > 1:
        out |= {"8" + n[1:], n[1:]}
    out |= {"26"} if n == "21" else {"21"} if n == "26" else set()
    out.discard(n)
    return sorted(out)


# ---------- run ----------

def run(keypath, draws, W):
    t0 = time.time()
    key = p5.load_key(keypath)
    lines = p5.load_lines(); prep(lines)
    pairs = old_pairs(lines)
    allh = sorted(H)
    fit = [h for h in allh if fold_of(h) == "fit"]
    keys = mk_keys(key, draws)
    r1, tau, r2 = run_keys(keys, W, allh, pairs, lambda rs: pick_tau(rs[1:], fit))
    real, shufs = r1[0][0], [r[0] for r in r1[1:]]
    realP, shufP = r2[0], r2[1:]
    out = []
    pr = out.append
    pr("align.py: key %s, W=%d, draws=%d. W and tau chosen on the FIT half only (W grid: align.py tune); test half not used for any choice."
       % (os.path.basename(keypath), W, draws))
    pr("tau = %.2f (smallest step-0.05 threshold with mean shuffled G acceptance < 2%% on fit-half G lines)" % tau)
    ar = lambda res, hs, kind, rl=None: (sum(len(acc(res[h], tau)) for h in hs), sum(len(H[h][kind]) for h in hs))
    for name, hs in (("fit half", fit), ("all halves", allh)):
        a, n = ar(real, hs, "G")
        sh = [ar(s, hs, "G")[0] / n for s in shufs]
        pr("G acceptance, %s: real %d/%d = %.3f | shuffled mean %.3f max %.3f" % (name, a, n, a / n, sum(sh) / draws, max(sh)))
        a, n = (sum(len(acc(realP[h], tau)) for h in hs), sum(len(H[h]["P"]) for h in hs))
        sh = [sum(len(acc(s[h], tau)) for h in hs) / n for s in shufP]
        pr("plain acceptance, %s: real %d/%d = %.4f | shuffled mean %.4f max %.4f" % (name, a, n, a / n, sum(sh) / draws, max(sh)))
    # scores
    gl = {(h, i): len(g) for h in allh for i, g in H[h]["G"]}
    fresh = lambda h: h.split("/")[0] not in p5.TRAIN_VOLS and h[:-1] not in p5.SPENT
    sets = [("test", lambda h: fold_of(h) == "test"), ("fit", lambda h: fold_of(h) == "fit"), ("fresh", fresh)]
    sets += [(v, (lambda v: lambda h: h.startswith(v + "/"))(v)) for v in sorted({h.split("/")[0] for h in allh})]

    def new_score(res, f):
        num = sum(m for h in allh if f(h) for (i, g_, m, ts, te) in res[h] if m and m / g_ >= tau)
        den = sum(g_ for h in allh if f(h) for (i, g_, *_r) in res[h])
        return num / max(den, 1), den

    def old_score(r, f):
        sel = [(hit, tot) for (h, hit, tot) in r[1] if f(h)]
        return sum(a for a, b in sel) / max(sum(b for a, b in sel), 1), len(sel)

    pr("")
    pr("%-18s %7s %-24s | %7s %-24s" % ("C04 score", "oldN", "old next-two: real shuf mean/max", "newN", "new alignment: real shuf mean/max"))
    for name, f in sets:
        so, no = old_score(r1[0], f)
        co = [old_score(r, f)[0] for r in r1[1:]]
        sn, nn = new_score(real, f)
        cn = [new_score(s, f)[0] for s in shufs]
        pr("%-18s %7d %.3f  %.3f / %.3f        | %7d %.3f  %.3f / %.3f" % (
            name, no, so, sum(co) / draws, max(co), nn, sn, sum(cn) / draws, max(cn)))
    pr("(oldN = G lines with numbers in the next two L lines; newN = G lines >= 4 letters. Denominators are letters of those lines, not lines.)")
    # per-line evidence
    rows, mis, votes = [], [], collections.defaultdict(lambda: {"all": collections.Counter(), "fit": collections.Counter()})
    na = collections.Counter()
    for kind, res in (("G", real), ("P", None)):
        for h in allh:
            rr = real[h] if kind == "G" else realP[h]
            for row in rr:
                i, g_, m, ts, te = row
                if not (m and m / g_ >= tau):
                    continue
                na[kind] += 1
                span = detail(h, key, row, kind, tau)
                rec = {"half": h, "i": i, "tag": kind if kind == "G" else "plain", "gloss": dict(H[h][kind])[i],
                       "matched": m, "fold": fold_of(h), "span": span}
                rows.append(rec)
                for t in span:
                    if t[4] in ("conflict", "unknown") and t[5] and 1 <= len(t[5]) <= 10:
                        for a in alts(t[2]):
                            if key.get(a) is not None and norm(key[a]) == t[5]:
                                mis.append((h, t[0], t[1], t[2], a, norm(key[a]), t[5], t[4], rec["fold"]))
                    if t[4] == "unknown" and t[5]:
                        votes[t[2]]["all"][t[5]] += 1
                        if rec["fold"] == "fit":
                            votes[t[2]]["fit"][t[5]] += 1
    with open(os.path.join(P.D, "aligned.jsonl"), "w") as o:
        for r in rows:
            o.write(json.dumps(r, ensure_ascii=False) + "\n")
    with open(os.path.join(P.D, "misread_candidates.tsv"), "w") as o:
        o.write("half\tline\tpos\tread\talt\talt_value\topp\tcls\tfold\n")
        for r in mis:
            o.write("\t".join(map(str, r)) + "\n")
    cls = collections.Counter(t[4] for r in rows for t in r["span"])
    pr("")
    pr("accepted lines: G %d, plain recovered %d | token classes %s" % (na["G"], na["P"], dict(cls)))
    pr("misread candidate rows %d (distinct tokens %d)" % (len(mis), len({m[:4] for m in mis})))
    uv = sum(sum(v["all"].values()) for v in votes.values())
    pr("unknown tokens with non-null opp: %d over %d numbers" % (uv, len(votes)))
    for which in ("fit", "all"):
        pr("")
        pr("unknown-number votes (%s): number, total, top opp letters x count" % which)
        top = sorted(votes.items(), key=lambda kv: -sum(kv[1][which].values()))[:30]
        for n, v in top:
            c = v[which]
            if c:
                pr("  %-5s %3d  %s" % (n, sum(c.values()), ", ".join("%s x%d" % kv for kv in c.most_common(3))))
    pr("")
    pr("runtime %.0fs" % (time.time() - t0))
    open(os.path.join(P.D, "align_report.txt"), "w").write("\n".join(out) + "\n")
    print("\n".join(out))


def main():
    a = sys.argv[1:]
    opt = lambda f, d: type(d)(a[a.index(f) + 1]) if f in a else d
    pos = [x for k, x in enumerate(a) if not x.startswith("--") and (k == 0 or not a[k - 1].startswith("--"))]
    keypath = pos[1] if len(pos) > 1 else os.path.join(P.D, "key_c04.json")
    if pos[0] == "run":
        run(keypath, opt("--draws", 20), opt("--W", W_DEF))
    elif pos[0] == "tune":
        tune(keypath, opt("--draws", 8))


if __name__ == "__main__":
    main()
