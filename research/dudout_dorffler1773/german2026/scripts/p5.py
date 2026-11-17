"""Phase 5: merge the whole-line reads, pair the contemporary decrypts, score a key, refine it.

Starting key: B. Dudout's TABLE-C04 (github.com/dbourdeau/cyphersolver, research/dudout_dorffler1773,
CC BY 4.0), built from 19/102 pages 467, 468, 470, 475, 476. Copied to data/key_c04.json.

Test design, fixed before any score was seen (2026-11-15):
  train decrypts = volume 19/102 only (where C04 came from)
  held-out decrypts = 19/100, 19/101, 19/103; never used to change the key, only to score it
  score = share of decrypt letters matched by the decoding of the cipher under it (local alignment
          over the next two lines, since a decrypt runs on across line ends)
  control = the same key with its values shuffled among its numbers, 200 draws
The language model sees the cipher of every volume (no decrypts), which is fair: it is unsupervised.

  python3 analysis/p5.py merge            # data/reread.jsonl -> data/p5_lines.jsonl
  python3 analysis/p5.py score KEY.json   # train / held-out / shuffled scores
  python3 analysis/p5.py vote             # clerk votes on the fit half -> data/key_fitvote.json
  python3 analysis/p5.py refine           # coordinate ascent from C04 -> data/key_p5.json
  python3 analysis/p5.py decode KEY.json  # readable decode of every line -> data/p5_decoded.txt
"""
import collections, difflib, json, math, os, random, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common as P
from common import norm

LINES = os.path.join(P.D, "p5_lines.jsonl")
TRAIN_VOLS = {"dorffler-19-102"}
# pages Dudout/Bourdeau already used to build or test C04 outside 19/102; reported separately so the
# "fresh" figure contains no page they have seen
SPENT = {"dorffler-19-100/p0277", "dorffler-19-100/p0304"}
NUM = re.compile(r"\d[\d?]*\"?")
PRIMARY = "vertex/gemini-4-argon"


# ---------- reading ----------

def tokens(text):
    """'und 179.60.121 nicht' -> [('w','und'), ('n','179'), ('n','60'), ('n','121'), ('w','nicht')]"""
    out = []
    for piece in re.split(r"(\d[\d?\"]*(?:\.\s?\d[\d?\"]*)*\.?)", text):
        if not piece.strip():
            continue
        if piece[0].isdigit():
            out += [("n", g.strip().rstrip('"')) for g in piece.split(".") if g.strip()]
        else:
            out.append(("w", piece))
    return out


def parse(text):
    """Tagged reader output -> list of {'tag': 'L'|'G', 'text': ...}."""
    out = []
    for l in (text or "").splitlines():
        m = re.match(r"\s*([LG])\s*:\s?(.*)", l)
        if m:
            out.append({"tag": m.group(1), "text": m.group(2).strip()})
    return out


def nums_of(line):
    return [v for k, v in tokens(line["text"]) if k == "n"]


def merge():
    """Argon is the primary reading. The second reader votes on numbers: where both read a cipher line
    with the same count of numbers, a disagreeing number keeps both readings as alternatives, and the
    language model picks between them later (alt field)."""
    reads = collections.defaultdict(dict)
    for l in open(os.path.join(P.D, "reread.jsonl")):
        r = json.loads(l)
        if "error" not in r:
            reads[r["half"]][r["model"]] = parse(r["text"])
    n_lines = n_alt = n_two = 0
    with open(LINES, "w") as o:
        for half in sorted(reads):
            got = reads[half]
            prim = got.get(PRIMARY) or next(iter(got.values()))
            other = [x for m, x in got.items() if x is not prim]
            sec = [x for x in other[0] if x["tag"] == "L" and nums_of(x)] if other else []
            for i, line in enumerate(prim):
                rec = {"half": half, "i": i, "tag": line["tag"], "text": line["text"]}
                ns = nums_of(line) if line["tag"] == "L" else []
                if ns:
                    best, ratio = None, 0
                    for s in sec:
                        q = difflib.SequenceMatcher(None, ns, nums_of(s)).ratio()
                        if q > ratio:
                            best, ratio = s, q
                    rec["agree"] = round(ratio, 3)
                    if best is not None and ratio >= 0.5:
                        n_two += 1
                        bs = nums_of(best)
                        if len(bs) == len(ns):
                            alt = {str(j): b for j, (a, b) in enumerate(zip(ns, bs)) if a != b and b.isdigit()}
                            if alt:
                                rec["alt"] = alt
                                n_alt += len(alt)
                o.write(json.dumps(rec, ensure_ascii=False) + "\n")
                n_lines += 1
    print("halves", len(reads), "lines", n_lines, "cipher lines read by both", n_two, "number alternatives", n_alt)


def load_lines():
    return [json.loads(l) for l in open(LINES)]


# ---------- decrypt pairs ----------

def gloss_pairs(lines):
    """Each G line with the numbers of the next two L lines of the same half."""
    pairs = []
    by_half = collections.defaultdict(list)
    for r in lines:
        by_half[r["half"]].append(r)
    for half, rs in by_half.items():
        for k, r in enumerate(rs):
            if r["tag"] != "G":
                continue
            nums, seen = [], 0
            for nxt in rs[k + 1:]:
                if nxt["tag"] != "L":
                    continue
                nums += [n for n in nums_of(nxt) if n.isdigit()]
                seen += 1
                if seen == 2:
                    break
            g = norm(r["text"].replace("[?]", ""))
            if len(g) >= 4 and nums:
                pairs.append({"half": half, "gloss": g, "nums": nums})
    return pairs


def local_match(gloss, dec):
    """Letters of the decrypt matched, in order, by the decoding, counting only runs of 3+ letters
    (single scattered letters match by chance and made a shuffled key score 0.36)."""
    if not dec:
        return 0
    sm = difflib.SequenceMatcher(None, gloss, dec, autojunk=False)
    return sum(b.size for b in sm.get_matching_blocks() if b.size >= 3)


def gloss_score(key, pairs):
    hit = tot = 0
    for p in pairs:
        dec = "".join(norm(key.get(n, "")) for n in p["nums"])
        hit += local_match(p["gloss"], dec)
        tot += len(p["gloss"])
    return hit / max(tot, 1)


def shuffled(key, rng):
    ks = list(key)
    vs = [key[k] for k in ks]
    rng.shuffle(vs)
    return dict(zip(ks, vs))


def load_key(path):
    return {k: v for k, v in json.load(open(path)).items() if not k.startswith("_")}


def score(path, draws=200):
    key = load_key(path)
    pairs = gloss_pairs(load_lines())
    tr = [p for p in pairs if p["half"].split("/")[0] in TRAIN_VOLS]
    ho = [p for p in pairs if p["half"].split("/")[0] not in TRAIN_VOLS]
    rng = random.Random(1)
    ctl = [gloss_score(shuffled(key, rng), ho) for _ in range(draws)]
    print("%s | train decrypts %d: %.3f | held-out decrypts %d (%d letters): %.3f | shuffled key on held-out: mean %.3f max %.3f"
          % (os.path.basename(path), len(tr), gloss_score(key, tr), len(ho), sum(len(p["gloss"]) for p in ho),
             gloss_score(key, ho), sum(ctl) / draws, max(ctl)))
    fresh = [p for p in ho if p["half"][:-1] not in SPENT]
    ctl_f = [gloss_score(shuffled(key, rng), fresh) for _ in range(draws)]
    print("   fresh only (no page used by Dudout/Bourdeau) %d decrypts: %.3f | shuffled mean %.3f max %.3f"
          % (len(fresh), gloss_score(key, fresh), sum(ctl_f) / draws, max(ctl_f)))
    by_vol = collections.defaultdict(list)
    for p in ho:
        by_vol[p["half"].split("/")[0]].append(p)
    for v, ps in sorted(by_vol.items()):
        print("   %s: %d decrypts, %.3f" % (v, len(ps), gloss_score(key, ps)))


# ---------- decoding ----------

def decode_line(key, r, choose=None):
    out = []
    for j, (k, v) in enumerate(tokens(r["text"])):
        if k == "w":
            out.append(v)
        else:
            n = (choose or {}).get(j, v)
            out.append("[" + key.get(n, "#" + n) + "]")
    return " ".join(out)


def decode(path):
    key = load_key(path)
    out = os.path.join(P.D, "p5_decoded.txt")
    with open(out, "w") as o:
        half = None
        for r in load_lines():
            if r["half"] != half:
                half = r["half"]
                o.write("\n== %s\n" % half)
            o.write(("   G: " + r["text"]) if r["tag"] == "G" else decode_line(key, r))
            o.write("\n")
    print("->", out)


# ---------- vote: the period decrypter as the teacher ----------
# The language-model refinement (refine.py) made the key WORSE on held-out decrypts (0.641 vs 0.655,
# shuffled control rose 0.10 -> 0.17): a letter model prefers common letters, not right ones. Here a
# number's value comes from what the 1680s decrypter wrote over it instead.

def fold(half):
    """Fit fold: 19/102 and even-numbered pages elsewhere. Test fold: odd pages outside 19/102."""
    v, p = half.split("/")
    return "fit" if v in TRAIN_VOLS or int(p[1:5]) % 2 == 0 else "test"


def votes_from(key, pairs):
    """For each pair, align the decrypt with the decoding. A number whose decoded piece sits alone in
    a mismatched stretch votes for the decrypt letters opposite it; a matched piece votes for itself."""
    v = collections.defaultdict(collections.Counter)
    for p in pairs:
        pieces = [norm(key.get(n, "")) for n in p["nums"]]
        dec = "".join(pieces)
        starts, pos = [], 0
        for pc in pieces:
            starts.append(pos); pos += len(pc)
        sm = difflib.SequenceMatcher(None, p["gloss"], dec, autojunk=False)
        blocks = [b for b in sm.get_matching_blocks() if b.size >= 3]
        if sum(b.size for b in blocks) < 0.4 * len(p["gloss"]):
            continue  # this decrypt is not the one over these numbers (misplaced line): no votes
        anchors = [(b.a, b.b, b.size) for b in blocks]
        for k, n in enumerate(p["nums"]):
            a0, a1 = starts[k], starts[k] + len(pieces[k])
            inside = [b for b in anchors if b[1] <= a0 and a1 <= b[1] + b[2]]
            if inside and pieces[k]:
                v[n][pieces[k]] += 1
                continue
            # gap between the anchor ending before this piece and the one starting after it
            prev = [b for b in anchors if b[1] + b[2] <= a0]
            nxt = [b for b in anchors if b[1] >= a1]
            if not prev or not nxt:
                continue
            pb, nb = prev[-1], nxt[0]
            if pb[1] + pb[2] == a0 and nb[1] == a1:  # this number alone fills the decoding gap
                g = p["gloss"][pb[0] + pb[2]:nb[0]]
                if 1 <= len(g) <= 8:
                    v[n][g] += 1
    return v


def vote_key(key, pairs, min_votes=3, share=0.6):
    new = dict(key)
    v = votes_from(key, pairs)
    changes = []
    for n, c in v.items():
        val, k = c.most_common(1)[0]
        tot = sum(c.values())
        if k >= min_votes and k / tot >= share and val != norm(key.get(n, "")):
            changes.append((n, key.get(n, "-"), val, k, tot))
            new[n] = val
    return new, changes


def vote(rounds=3):
    key = load_key(os.path.join(P.D, "key_c04.json"))
    pairs = gloss_pairs(load_lines())
    fit = [p for p in pairs if fold(p["half"]) == "fit"]
    test = [p for p in pairs if fold(p["half"]) == "test"]
    rng = random.Random(2)
    def report(name, k):
        ctl = [gloss_score(shuffled(k, rng), test) for _ in range(100)]
        print("%-28s test fold %d decrypts: %.3f | shuffled mean %.3f max %.3f" % (
            name, len(test), gloss_score(k, test), sum(ctl) / len(ctl), max(ctl)), flush=True)
    report("C04", key)
    cv = key
    for r in range(rounds):
        cv, ch = vote_key(cv, fit)
        print("round %d: %d changes from the fit fold" % (r, len(ch)))
        if not ch:
            break
    report("C04 + votes (fit fold)", cv)
    json.dump(dict(sorted(cv.items(), key=lambda kv: int(kv[0])),
                   _source="TABLE-C04 (B. Dudout, CC BY 4.0) + decrypt votes from the fit half only, analysis/p5.py vote"),
              open(os.path.join(P.D, "key_fitvote.json"), "w"), ensure_ascii=False, indent=0)
    print("fit-half key: %d change(s) over C04 -> data/key_fitvote.json" % sum(cv.get(n) != key.get(n) for n in cv))


# ---------- fill: WITHDRAWN. Its prompts showed decrypts from both halves, so its test score is not held out.
# Kept for the record; analysis/order.py replaces it. ----------

FILL_PROMPT = """You are helping complete the codebook of a 1680s German diplomatic cipher (Simon Dorffler, Swedish
resident in Poland, writing to Charles XI). Each cipher number stands for a letter, a syllable, a word or
a name. Below, for ONE unknown number written [N], are places it occurs: the decoded text before and after
it (letters only, no spaces, the decoding itself may contain errors), and the contemporary decryption
written near that cipher line (also letters only, not aligned word for word).
Propose the value of [N]: the letters it stands for, lower case, letters only (it may be a whole word or
a name). If the evidence does not support one value, answer UNKNOWN.
Answer with one line of JSON: {"value": "...", "confidence": "high|medium|low", "why": "<15 words"}

"""


def fill(model="vertex/gemini-4-argon", min_uses=5, max_ex=10):
    import subprocess
    key = load_key(os.path.join(P.D, "key_final.json"))
    lines = load_lines()
    pairs = gloss_pairs(lines)
    fit = [p for p in pairs if fold(p["half"]) == "fit"]
    test = [p for p in pairs if fold(p["half"]) == "test"]
    cnt = collections.Counter(n for r in lines if r["tag"] == "L" for n in nums_of(r) if n.isdigit())
    todo = [n for n, c in cnt.most_common() if n not in key and c >= min_uses
            and not (len(n) == 4 and n.startswith("16"))]  # 1682-1690 are dates in clear text
    out = os.path.join(P.D, "fill.jsonl")
    done = {json.loads(l)["n"] for l in open(out)} if os.path.exists(out) else set()
    for n in todo:
        if n in done:
            continue
        ex = []
        for p in pairs:
            if n in p["nums"] and len(ex) < max_ex:
                i = p["nums"].index(n)
                ex.append("before=%s [N] after=%s | decryption=%s" % (
                    "".join(norm(key.get(x, "")) for x in p["nums"][max(0, i - 4):i]),
                    "".join(norm(key.get(x, "")) for x in p["nums"][i + 1:i + 5]), p["gloss"][:90]))
        if len(ex) < 3:
            continue
        r = subprocess.run(["llm", "-n", "-m", model, "-o", "tier", "standard", FILL_PROMPT + "\n".join(ex)],
                           capture_output=True, text=True, timeout=600, stdin=subprocess.DEVNULL)
        m = re.search(r"\{.*\}", r.stdout, re.S)
        rec = {"n": n, "uses": cnt[n], "examples": len(ex)}
        try:
            rec.update(json.loads(m.group(0)))
        except Exception:
            rec["error"] = (r.stdout + r.stderr)[-200:]
        open(out, "a").write(json.dumps(rec, ensure_ascii=False) + "\n")
        print(n, rec.get("value"), rec.get("confidence"), rec.get("why", rec.get("error", ""))[:80], flush=True)
    # keep a proposal only if it raises the fit-fold score
    props = [json.loads(l) for l in open(out)]
    new = dict(key)
    base = gloss_score(new, fit)
    kept = []
    for pr in props:
        v = norm(pr.get("value", ""))
        if not v or pr.get("value", "").upper() == "UNKNOWN":
            continue
        new[pr["n"]] = v
        s = gloss_score(new, fit)
        if s > base:
            base = s
            kept.append(pr)
        else:
            del new[pr["n"]]
    rng = random.Random(3)
    ctl = [gloss_score(shuffled(new, rng), test) for _ in range(100)]
    print("proposals %d, kept %d (fit fold improved)" % (len(props), len(kept)))
    print("test fold: before fill %.3f, after fill %.3f, shuffled mean %.3f max %.3f" % (
        gloss_score(key, test), gloss_score(new, test), sum(ctl) / len(ctl), max(ctl)))
    for pr in kept:
        new_src = "fill: %s (%s)" % (pr["value"], pr.get("confidence"))
    json.dump(dict(sorted(new.items(), key=lambda kv: int(kv[0])),
                   _source="TABLE-C04 (B. Dudout, CC BY 4.0) + decrypt votes + model-proposed fills kept on the fit fold"),
              open(os.path.join(P.D, "key_final.json"), "w"), ensure_ascii=False, indent=0)
    with open(os.path.join(P.D, "key_changes.tsv"), "a") as o:
        for pr in kept:
            o.write("%s\t-\t%s\tmodel:%s\t%s uses\n" % (pr["n"], norm(pr["value"]), pr.get("confidence"), pr["uses"]))


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "merge":
        merge()
    elif cmd == "score":
        score(sys.argv[2])
    elif cmd == "decode":
        decode(sys.argv[2])
    elif cmd == "fill":
        fill()
    elif cmd == "vote":
        vote()
    elif cmd == "refine":
        import refine
        refine.main()
