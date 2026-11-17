"""Cloze test for valueless cipher numbers, with a split-half agreement rule and a hidden-value validation.

For a number N, the fit-half lines that contain it are dealt alternately into sets A and B (cap 8 each); the
model is asked about A and about B in separate calls and never sees both, or any value for N. A and B must
agree (equal, or one a prefix of the other with >= 3 shared letters) for a value to be accepted.
  unknown: numbers 146-999 with no key value and >= 4 fit occurrences (excl. 500, 600, 800)
  hidden : numbers 146-226 and 250-399 that HAVE a value and >= 6 fit occurrences; N is removed from the key
           and the second nearest known entries on each side are the ordering hint. Same procedure, then
           scored against the true value (oe/o, ue/u, ck/k folded).

  python3 analysis/cloze.py run [KEY.json] [--evidence fit|all] [--limit K] [--only unknown|hidden]
  python3 analysis/cloze.py show N [KEY.json] [--evidence ..]   # print the full hidden prompt for N (set A), no model call
  python3 analysis/cloze.py report                              # -> data/cloze_report.txt
Env: CLOZE_MAX_CALLS (default 60) aborts a run whose planned calls exceed it.
"""
import collections, concurrent.futures as cf, fcntl, json, os, re, subprocess, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common as P
import p5
from common import norm

OUT = os.path.join(P.D, "cloze.jsonl")
MODEL = "vertex/gemini-4-argon"
ENV = dict(os.environ, PATH=os.path.expanduser("~/.local/bin") + ":" + os.environ["PATH"],
           VERTEX_PROJECT_ID="ai-engineering-team-491520", VERTEX_LOCATION="us-central1")
THINK = ["-o", "thinking_budget", "4000"]
MAXOUT = ["-o", "max_output_tokens", "16000"]  # 8000 thinking + answer overflowed the default cap (MAX_TOKENS, empty answer)
CAP = 8
LAYOUT = """The text is a 1680s German diplomatic letter in numeric cipher. Plain German words are written out; the rest is
dot-separated numbers. Each number stands for letters (‹..›, already decoded for you) or for a whole word. Layout of the key:
14-65 two alphabets of single letters, 66-145 syllables, 146-226 an alphabetical German word list (v-words such as
ver/von/vor sort BEFORE u-words such as uber/um/und), 227-249 a supplement that is not alphabetical (ein, dreissig, tausend),
250 and up an alphabetical list of names and titles (e.g. armee, bischof, brandenburg, cron, feld, frankreich, furst, herr, kayser, koenig, pohlen, wien).
[?] is a number whose value is not known. 'clerk:' is a contemporary clerk's loose interlinear decryption of nearby cipher; it may be misplaced."""


def fold(s):
    return norm(s).replace("oe", "o").replace("ue", "u").replace("ck", "k")


def which_list(n):
    return ("a word from the alphabetical German word list (146-226)" if n <= 226 else
            "the supplement list (227-249, not alphabetical: an ordinary word or number word)" if n <= 249 else
            "the alphabetical list of names and titles (250 and up)")


def occurrences(lines, evidence):
    by = collections.defaultdict(list)
    for r in lines:
        if evidence == "all" or p5.fold(r["half"]) == "fit":
            by[r["half"]].append(r)
    return by


def index(lines, evidence):
    """n -> sorted [(half, row index)] of fit L lines containing it."""
    occ = collections.defaultdict(list)
    for r in lines:
        if r["tag"] == "L" and (evidence == "all" or p5.fold(r["half"]) == "fit"):
            for n in set(p5.nums_of(r)):
                occ[n].append((r["half"], r["i"]))
    return {n: sorted(v) for n, v in occ.items()}


def render(text, key, target):
    out = []
    for k, v in p5.tokens(text):
        if k == "w":
            out.append(v.strip())
        elif v == str(target):
            out.append("[%d]" % target)
        elif norm(key.get(v, "")):
            out.append("‹%s›" % norm(key[v]))
        else:
            out.append("[?]")
    return " ".join(x for x in out if x)


def contexts(rows, key, n, occ):
    """rows: half -> list of rows (all tags, by i). Context = prev L, the line, next L, plus nearby clerk lines."""
    res = []
    for half, i in occ:
        rs = rows[half]
        pos = next(j for j, r in enumerate(rs) if r["i"] == i)
        Ls = [j for j, r in enumerate(rs) if r["tag"] == "L"]
        k = Ls.index(pos)
        parts = [rs[Ls[x]] for x in (k - 1, k, k + 1) if 0 <= x < len(Ls)]
        s = " / ".join(render(r["text"], key, n) for r in parts)
        g = [r["text"] for r in rs if r["tag"] == "G" and i - 2 <= r["i"] <= i + 1]
        res.append(s + ("  clerk: " + " | ".join(g) if g else "  clerk: "))
    return res


def neighbours(key, n, skip):
    lo, hi = (146, 226) if n <= 226 else (250, 999)
    ent = sorted((int(k), norm(v)) for k, v in key.items() if k.isdigit() and lo <= int(k) <= hi and norm(v) and int(k) != n)
    below = [e for e in ent if e[0] < n][::-1]
    above = [e for e in ent if e[0] > n]
    return (below[skip] if len(below) > skip else None), (above[skip] if len(above) > skip else None)


def prompt(n, ctxs, nb):
    lo, hi = nb
    hint = ""
    if 227 <= n <= 249:
        hint = "No ordering hint: this part of the key is not alphabetical."
    else:
        hint = "Ordering hint (not a hard rule): in this list, number %s is %s and number %s is %s, so [%d] should sort between them." % (
            lo[0] if lo else "?", lo[1] if lo else "(start)", hi[0] if hi else "?", hi[1] if hi else "(end)", n)
    ex = "\n".join("%d. %s" % (j + 1, c) for j, c in enumerate(ctxs))
    return ("%s\n\nThe number [%d] belongs to %s. %s\n\nContexts where [%d] occurs:\n%s\n\n"
            "What does [%d] stand for? Answer with one line of JSON only: "
            '{"value": "<lower-case letters, a word, word stem or name; or UNKNOWN>", "confidence": "high|medium|low", "why": "<15 words"}'
            % (LAYOUT, n, which_list(n), hint, n, ex, n))


def call(p):
    global THINK
    for _ in range(3):
        opts = ["-o", "tier", "standard"] + THINK + MAXOUT
        r = subprocess.run(["llm", "-n", "-m", MODEL] + opts + [p], capture_output=True, text=True, timeout=600,
                           stdin=subprocess.DEVNULL, env=ENV)
        if r.returncode and "thinking_budget" in r.stderr and THINK:
            THINK = []
            print("NOTE: thinking_budget rejected; dropped", flush=True)
            continue
        m = re.search(r"\{.*\}", r.stdout, re.S)
        try:
            d = json.loads(m.group(0))
            return {"value": str(d.get("value", "")), "confidence": str(d.get("confidence", "")), "why": str(d.get("why", ""))}
        except Exception:
            err = (r.stdout + r.stderr)[-200:]
    return {"value": "", "confidence": "", "why": "", "error": err}


def agree(a, b):
    x, y = norm(a), norm(b)
    if not x or not y or x == "unknown" or y == "unknown":
        return None
    s, l = sorted((x, y), key=len)
    return s if l.startswith(s) and (len(s) >= 3 or x == y) else None


def correct(ans, true):
    x, y = fold(ans), fold(true)
    s, l = sorted((x, y), key=len)
    return bool(x and y and l.startswith(s) and (len(s) >= 3 or x == y))


def build(kind, n, key, rows, occ, evidence):
    k = {a: b for a, b in key.items() if not (kind == "hidden" and a == str(n))}
    o = occ[str(n)]
    A, B = o[0::2][:CAP], o[1::2][:CAP]
    nb = neighbours(k, n, 1 if kind == "hidden" else 0)
    return [prompt(n, contexts(rows, k, n, s), nb) for s in (A, B)], len(A), len(B)


def targets(key, occ, only):
    t = []
    for n in range(146, 1000):
        c = len(occ.get(str(n), []))
        if (only in (None, "unknown") and not key.get(str(n)) and c >= 4 and n not in (500, 600, 800)):
            t.append(("unknown", n))
        if (only in (None, "hidden") and norm(key.get(str(n), "")) and (n <= 226 or 250 <= n <= 399) and c >= 6):
            t.append(("hidden", n))
    return t


def setup(args):
    ev = args[args.index("--evidence") + 1] if "--evidence" in args else "fit"
    paths = [a for i, a in enumerate(args) if a.endswith(".json")]
    key = p5.load_key(paths[0] if paths else os.path.join(P.D, "key_c04.json"))
    lines = p5.load_lines()
    rows = collections.defaultdict(list)
    for r in lines:
        rows[r["half"]].append(r)
    return key, rows, index(lines, ev), ev


def run(args):
    key, rows, occ, ev = setup(args)
    only = args[args.index("--only") + 1] if "--only" in args else None
    lim = int(args[args.index("--limit") + 1]) if "--limit" in args else None
    done = set()
    if os.path.exists(OUT):
        done = {(r["kind"], r["n"]) for r in map(json.loads, open(OUT))}
    todo = []
    for kind in ("unknown", "hidden"):
        todo += [t for t in targets(key, occ, only) if t[0] == kind and t not in done][:lim]
    cap = int(os.environ.get("CLOZE_MAX_CALLS", 60))
    print("targets %d, planned calls %d (cap %d)" % (len(todo), 2 * len(todo), cap), flush=True)
    if 2 * len(todo) > cap:
        raise SystemExit("ABORT: planned calls exceed CLOZE_MAX_CALLS")
    lock = open(OUT + ".lock", "w")
    try:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError:
        raise SystemExit("ABORT: another run holds the lock")

    def one(t):
        kind, n = t
        (pa, pb), na, nb = build(kind, n, key, rows, occ, ev)
        a, b = call(pa), call(pb)
        v = agree(a["value"], b["value"])
        rec = {"kind": kind, "n": n, "uses": len(occ[str(n)]), "nA": na, "nB": nb, "a": a, "b": b,
               "agree": v is not None, "value": v}
        if kind == "hidden":
            rec["true"] = key[str(n)]
            rec["correct"] = v is not None and correct(v, key[str(n)])
        return rec

    with cf.ThreadPoolExecutor(8) as ex, open(OUT, "a") as o:
        for rec in ex.map(one, todo):
            o.write(json.dumps(rec, ensure_ascii=False) + "\n"); o.flush()
            print(rec["kind"], rec["n"], rec["a"]["value"], "|", rec["b"]["value"], "->", rec["value"],
                  rec.get("correct", ""), flush=True)


def show(args):
    n = int(args[0])
    key, rows, occ, ev = setup(args[1:])
    kind = "hidden" if norm(key.get(str(n), "")) else "unknown"
    print(kind, "true value (not shown to model):", key.get(str(n)))
    print(build(kind, n, key, rows, occ, ev)[0][0])


def report():
    rs = [json.loads(l) for l in open(OUT)]
    out = []
    p = out.append
    h = [r for r in rs if r["kind"] == "hidden"]
    ag = [r for r in h if r["agree"]]
    ok = [r for r in ag if r["correct"]]
    hi = [r for r in ag if r["a"]["confidence"] == "high" and r["b"]["confidence"] == "high"]
    lo = [r for r in ag if r not in hi]
    f = lambda a, b: "%d/%d = %.2f" % (a, b, a / b) if b else "0/0"
    p("HIDDEN (validation): tested %d" % len(h))
    p("  A and B agree: " + f(len(ag), len(h)))
    p("  precision among agreeing: " + f(len(ok), len(ag)))
    p("  recall (correct and agree / tested): " + f(len(ok), len(h)))
    p("  precision both high: " + f(sum(r["correct"] for r in hi), len(hi)) + " | otherwise: " + f(sum(r["correct"] for r in lo), len(lo)))
    p("  wrong but agreeing:")
    for r in ag:
        if not r["correct"]:
            p("    %d true=%s got=%s (A=%s B=%s)" % (r["n"], r["true"], r["value"], r["a"]["value"], r["b"]["value"]))
    u = [r for r in rs if r["kind"] == "unknown"]
    p("\nUNKNOWN: tested %d, agreed %d" % (len(u), sum(r["agree"] for r in u)))
    p("  accepted: n, uses, value, a, b, confidences")
    for r in u:
        if r["agree"]:
            p("    %d\t%d\t%s\t%s\t%s\t%s/%s" % (r["n"], r["uses"], r["value"], r["a"]["value"], r["b"]["value"],
                                                  r["a"]["confidence"], r["b"]["confidence"]))
    p("  not agreed:")
    for r in u:
        if not r["agree"]:
            p("    %d\t%d\tA=%s\tB=%s%s" % (r["n"], r["uses"], r["a"]["value"], r["b"]["value"],
                                              "  ERROR" if "error" in r["a"] or "error" in r["b"] else ""))
    t = "\n".join(out)
    print(t)
    open(os.path.join(P.D, "cloze_report.txt"), "w").write(t + "\n")


if __name__ == "__main__":
    {"run": lambda: run(sys.argv[2:]), "show": lambda: show(sys.argv[2:]), "report": report}[sys.argv[1]]()
