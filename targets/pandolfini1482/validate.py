#!/usr/bin/env python3
"""Zero-leakage statistical validation for Pierfilippo Pandolfini -> Lorenzo de' Medici
(ASFi MAP XXXVIII doc. 418 = Cat. 2574; ASFi MAP LIII doc. 13 = Cat. 2559).

Tests the audited key (key_pandolfini1482.tsv) against 200 shuffled keys and 200 shuffled
token streams under BOTH:
  1. Strict zero-choice monophonic M1 (no beam disambiguation)
  2. Audited 5-polyphonic beam P5 (II={a,o}, 9={e,l}, sig={t,d}, d={c,g}, pi={t,b};
     identical beam_w=8 decoder on real text and all 200 shuffled-key / shuffled-stream controls)

Uses an order-5 early-Italian nospace DenseLM trained on pre-1650 repository Italian texts
strictly excluding {pandolfini1482, rucellai1482, mazzinghi1478, toledo1479}, and unboosted
lang/lexicons/it.json.gz (ZERO target-specific lexicon boosts). Writes validation.txt.
"""
from __future__ import annotations

import collections
import csv
import gzip
import json
import math
import pathlib
import random
import re
import statistics
import sys
import time

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent


def _find_repo() -> pathlib.Path:
    for cand in [HERE.parents[1], pathlib.Path.cwd()] + [p / "cyphersolver_repo" for p in HERE.parents]:
        if (cand / "lang" / "lm.py").is_file() and (cand / "lang" / "lexicons" / "it.json.gz").is_file():
            return cand
    raise FileNotFoundError("Cannot locate cyphersolver repo root containing lang/lm.py")


REPO = _find_repo()
sys.path.insert(0, str(REPO))
from lang.lm import DenseLM, alphabet, norm  # noqa: E402

EXCLUDED_TARGETS = {"rucellai1482", "pandolfini1482", "mazzinghi1478", "toledo1479"}
IT_STOP = set(
    "che di la il non per con si se et le della delle del dello alla alle quello questo questa sua suo "
    "ma sono essere da dal dalla come anche ancora tutto tutti molto piu cosa cose nostro vostra signore "
    "stato haver havere fatto quale quali questi quelli loro noi voi lui lei gli una uno mi ti ci vi ne "
    "lo li ha hanno era erano sia siano perche poi qui qua ogni altro altra altri senza sopra sotto "
    "dopo prima tanto quanto bene male dio papa imperatore francia roma ferrara milano napoli firenze fiorenza".split()
)
BAD_STOP = set(
    "the and of to in is that for with on was as by this from are not be it have or an which were been "
    "der die das und ist nicht von zu den dem des mit auf ein eine".split()
)


def build_italian_lm() -> tuple[DenseLM, int]:
    targets_dir = REPO / "targets"
    if targets_dir.is_dir() and len(list(targets_dir.glob("*/profile.json"))) < 5:
        for par in HERE.parents:
            alt = par / "cyphersolver_repo" / "targets"
            if alt.is_dir() and len(list(alt.glob("*/profile.json"))) >= 5:
                targets_dir = alt
                break
    chunks = []
    for pj in sorted(targets_dir.glob("*/profile.json")):
        tdir = pj.parent
        if tdir.name in EXCLUDED_TARGETS:
            continue
        try:
            d = json.loads(pj.read_text(encoding="utf-8"))
        except Exception:
            continue
        docs = d.get("documents", [])
        if not any(doc.get("language") == "Italian" for doc in docs):
            continue
        years = [doc.get("year", 9999) for doc in docs if isinstance(doc.get("year"), int)]
        if years and min(years) > 1650:
            continue
        min_y = min(years) if years else 9999
        weight = 4 if min_y <= 1500 else (2 if min_y <= 1535 else 1)

        cand_files = set()
        for t in d.get("outcome", {}).get("texts", []):
            for k in ("decryption", "contemporary", "reading"):
                fn = t.get(k)
                if isinstance(fn, str) and (fn.endswith(".txt") or fn.endswith(".md")):
                    cand_files.add(tdir / fn)
        for fn in sorted(tdir.glob("*.txt")) + sorted(tdir.glob("texts/*.txt")) + sorted(tdir.glob("decryption/*.txt")):
            if any(w in fn.name.lower() for w in ("reading", "plaintext", "decryption", "cleartext")):
                cand_files.add(fn)
        for fp in sorted(cand_files):
            if not fp.exists():
                continue
            txt = fp.read_text(encoding="utf-8", errors="ignore")
            for line in txt.splitlines():
                if line.startswith("#") or line.startswith("|"):
                    continue
                lc = re.sub(r"\[[^\]]*\]|\{[^}]*\}|‹[^›]*›|[?*_#`<>|]", " ", line)
                words = re.findall(r"[A-Za-zÀ-ÿ]+", lc.lower())
                if len(words) < 6:
                    continue
                it_hits = sum(w in IT_STOP for w in words)
                bad_hits = sum(w in BAD_STOP for w in words)
                if it_hits >= 1 and it_hits >= 2 * bad_hits:
                    for _ in range(weight):
                        chunks.append(lc)
    txt_ns = norm("\n".join(chunks), scheme="early", spaces=False)
    lm_ns = DenseLM.build(txt_ns, order=5, alpha=alphabet("early", spaces=False), meta={"name": "it_quattrocento_ns_o5"})
    return lm_ns, len(txt_ns)


class LexiconScorer:
    """Word-DP segmentation over lang/lexicons/it.json.gz (ZERO target-specific word boosts)."""

    def __init__(self) -> None:
        raw = json.load(gzip.open(REPO / "lang" / "lexicons" / "it.json.gz", "rt", encoding="utf-8"))
        self.freq = collections.Counter()
        for w, c in raw.items():
            nw = norm(w, scheme="early", spaces=False)
            if nw:
                self.freq[nw] += c
        self.total = sum(self.freq.values())
        self.logp = {w: math.log(c / self.total) for w, c in self.freq.items() if c >= 3}
        self.maxlen = max((len(w) for w in self.logp), default=15)

    def segment(self, text_ns: str) -> tuple[float, float]:
        s = norm(text_ns, scheme="early", spaces=False)
        n = len(s)
        if n == 0:
            return 0.0, 0.0
        dp = [-1e18] * (n + 1)
        bp = [(0, False)] * (n + 1)
        dp[0] = 0.0
        for i in range(n):
            if dp[i] < -1e17:
                continue
            sc1 = dp[i] - 18.0
            if sc1 > dp[i + 1]:
                dp[i + 1] = sc1
                bp[i + 1] = (i, False)
            for L in range(1, min(self.maxlen, n - i) + 1):
                w = s[i : i + L]
                lp = self.logp.get(w)
                if lp is not None:
                    sc = dp[i] + lp + 1.5 * (L - 1)
                    if sc > dp[i + L]:
                        dp[i + L] = sc
                        bp[i + L] = (i, True)
        cov4 = cov5 = 0
        idx = n
        while idx > 0:
            prev, known = bp[idx]
            wlen = idx - prev
            if known:
                if wlen >= 4:
                    cov4 += wlen
                if wlen >= 5:
                    cov5 += wlen
            idx = prev
        return cov4 / n, cov5 / n


def load_keys() -> tuple[dict[str, str], dict[str, tuple[str, ...]]]:
    km: dict[str, str] = {}
    poly: dict[str, tuple[str, ...]] = {}
    with (HERE / "key_pandolfini1482.tsv").open(encoding="utf-8") as fh:
        rows = csv.DictReader((r for r in fh if not r.startswith("#")), delimiter="\t")
        for row in rows:
            tok = row["token"].strip()
            if " " in tok:
                continue
            v = row["value_m1"].strip()
            km[tok] = "" if v in ("NULL", "?") else v
            if row["kind"].strip() == "polyphonic":
                opts = tuple(p.strip() for p in row["value_poly"].split("/") if p.strip() and p.strip() not in ("NULL", "?"))
                if len(opts) >= 2:
                    poly[tok] = opts
    return km, poly


def load_runs(path: pathlib.Path, doc_id: str) -> list[tuple[str, list[str], str, str]]:
    """Split transcript into contiguous cipher runs bounded by <<...>> clear anchors."""
    items = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^(L\d{2})\t(.*)$", raw)
        if not m:
            continue
        lbl, body = m.group(1), m.group(2)
        for seg in re.split(r"(<<.*?>>)", body):
            seg = seg.strip()
            if not seg:
                continue
            if seg.startswith("<<") and seg.endswith(">>"):
                items.append(("CLEAR", seg[2:-2].strip(), lbl))
            else:
                items.append(("CIPHER", seg.split(), lbl))
    runs = []
    cur_toks: list[str] = []
    left_clear = ""
    start_lbl = end_lbl = ""
    for kind, val, lbl in items:
        if kind == "CLEAR":
            if cur_toks:
                runs.append((left_clear, cur_toks, val, f"{doc_id}:{start_lbl}..{end_lbl}"))
                cur_toks = []
            left_clear = val
        else:
            if not cur_toks:
                start_lbl = lbl
            cur_toks.extend(val)
            end_lbl = lbl
    if cur_toks:
        runs.append((left_clear, cur_toks, "", f"{doc_id}:{start_lbl}..{end_lbl}"))
    return runs


def build_pre(runs: list[tuple[str, list[str], str, str]], lm_ns: DenseLM, c2i: dict[str, int]) -> list:
    pre = []
    for lc, toks, rc, span in runs:
        lc_ids = [c2i[c] for c in norm(lc, "early", False)[-4:] if c in c2i]
        rc_ids = [c2i[c] for c in norm(rc, "early", False)[:4] if c in c2i]
        sc_lc = float(lm_ns.score_idx(np.array(lc_ids, dtype=np.int64))) if len(lc_ids) >= 2 else 0.0
        pre.append((lc_ids, toks, rc_ids, sc_lc, span))
    return pre


def score_run_poly(item, key_map: dict[str, str], poly_toks: dict[str, tuple[str, str]], lm_ns: DenseLM, c2i: dict[str, int], beam_w: int = 8) -> tuple[float, str]:
    lc_ids, toks, rc_ids, sc_lc, _ = item
    if not poly_toks:
        seq = list(lc_ids)
        for t in toks:
            s = key_map.get(t, "")
            if s:
                seq.extend(c2i[ch] for ch in s if ch in c2i)
        full = seq + rc_ids
        sc = (float(lm_ns.score_idx(np.array(full, dtype=np.int64))) - sc_lc) if len(full) >= 2 else 0.0
        rev = lm_ns.alpha
        return sc, "".join(rev[i] for i in seq[len(lc_ids) :])

    beam = [(0.0, list(lc_ids))]
    for t in toks:
        if t in poly_toks:
            opts = poly_toks[t]
            new_beam = []
            for sc, seq in beam:
                for ch in opts:
                    cid = c2i[ch]
                    nseq = seq + [cid]
                    ctx = nseq[-5:]
                    if len(ctx) >= 2:
                        arr = np.array(ctx, dtype=np.int64)
                        inc = float(lm_ns.score_idx(arr) - (lm_ns.score_idx(arr[:-1]) if len(ctx) >= 3 else 0.0))
                    else:
                        inc = 0.0
                    new_beam.append((sc + inc, nseq))
            new_beam.sort(key=lambda x: -x[0])
            beam = new_beam[:beam_w]
        else:
            s = key_map.get(t, "")
            if s:
                cids = [c2i[ch] for ch in s if ch in c2i]
                for _, seq in beam:
                    seq.extend(cids)
    best_sc = -1e18
    best_body = ""
    rev = lm_ns.alpha
    for _, seq in beam:
        full = seq + rc_ids
        sc = (float(lm_ns.score_idx(np.array(full, dtype=np.int64))) - sc_lc) if len(full) >= 2 else 0.0
        if sc > best_sc:
            best_sc = sc
            best_body = "".join(rev[i] for i in seq[len(lc_ids) :])
    return best_sc, best_body


def fast_eval(pre_list, key_map, poly_map, lm_ns, c2i, lex, beam_w=8):
    tot_lp, tot_ch, bodies = 0.0, 0, []
    for item in pre_list:
        sc, body = score_run_poly(item, key_map, poly_map, lm_ns, c2i, beam_w=beam_w)
        tot_lp += sc
        tot_ch += len(body)
        bodies.append(body)
    full = "".join(bodies)
    c4, c5 = lex.segment(full)
    return tot_lp / max(1, tot_ch), c4, c5, tot_ch


def z_stats(real_v: float, ctrls: list[float]) -> tuple[float, float, float, float, float]:
    mu = statistics.mean(ctrls)
    sd = statistics.stdev(ctrls) if len(ctrls) > 1 else 0.0
    z = (real_v - mu) / sd if sd > 1e-12 else 0.0
    p = (sum(1 for x in ctrls if x >= real_v) + 1) / (len(ctrls) + 1)
    return mu, sd, max(ctrls), z, p


def main() -> None:
    t0 = time.time()
    lm_ns, n_corpus = build_italian_lm()
    lex = LexiconScorer()
    c2i = {c: int(lm_ns.encode(c)[0]) for c in lm_ns.alpha}
    mono_key, poly_map = load_keys()

    r74 = load_runs(HERE / "transcript_2574.txt", "#2574")
    r59 = load_runs(HERE / "transcript_2559.txt", "#2559")
    all_runs = r74 + r59

    pre_all = build_pre(all_runs, lm_ns, c2i)
    pre_74 = build_pre(r74, lm_ns, c2i)
    pre_59 = build_pre(r59, lm_ns, c2i)

    m1_all = fast_eval(pre_all, mono_key, {}, lm_ns, c2i, lex)
    m1_74 = fast_eval(pre_74, mono_key, {}, lm_ns, c2i, lex)
    m1_59 = fast_eval(pre_59, mono_key, {}, lm_ns, c2i, lex)

    p5_all = fast_eval(pre_all, mono_key, poly_map, lm_ns, c2i, lex, beam_w=8)
    p5_74 = fast_eval(pre_74, mono_key, poly_map, lm_ns, c2i, lex, beam_w=8)
    p5_59 = fast_eval(pre_59, mono_key, poly_map, lm_ns, c2i, lex, beam_w=8)

    rng = random.Random(14820)
    cipher_signs = sorted(t for t in mono_key if not t.startswith("LAT_") and t != "invT")
    mono_vals = [mono_key[t] for t in cipher_signs]

    # 200 Shuffled Keys & 200 Shuffled Streams: M1 (strict 0-choice)
    m1_sk_lm, m1_sk_c5 = [], []
    for _ in range(200):
        shuf = list(mono_vals); rng.shuffle(shuf)
        k_shuf = dict(mono_key)
        for t, v in zip(cipher_signs, shuf):
            k_shuf[t] = v
        lpc, _, c5, _ = fast_eval(pre_all, k_shuf, {}, lm_ns, c2i, lex)
        m1_sk_lm.append(lpc); m1_sk_c5.append(c5)

    m1_ss_lm, m1_ss_c5 = [], []
    for _ in range(200):
        pool = [t for _, r, _, _ in all_runs for t in r if not t.startswith("LAT_") and t != "invT"]
        rng.shuffle(pool)
        it = iter(pool)
        shuf_runs = [(lc, [t if (t.startswith("LAT_") or t == "invT") else next(it) for t in r], rc, sp) for lc, r, rc, sp in all_runs]
        lpc, _, c5, _ = fast_eval(build_pre(shuf_runs, lm_ns, c2i), mono_key, {}, lm_ns, c2i, lex)
        m1_ss_lm.append(lpc); m1_ss_c5.append(c5)

    # 200 Shuffled Keys & 200 Shuffled Streams: P5 (identical beam_w=8)
    poly_pairs = list(poly_map.values())
    p5_sk_lm, p5_sk_c5 = [], []
    for _ in range(200):
        shuf_signs = list(cipher_signs); rng.shuffle(shuf_signs)
        shuf_vals = list(mono_vals); rng.shuffle(shuf_vals)
        k_shuf = dict(mono_key)
        for t, v in zip(cipher_signs, shuf_vals):
            k_shuf[t] = v
        p_shuf = {t: pair for t, pair in zip(shuf_signs[: len(poly_pairs)], poly_pairs)} if poly_pairs else {}
        lpc, _, c5, _ = fast_eval(pre_all, k_shuf, p_shuf, lm_ns, c2i, lex, beam_w=8)
        p5_sk_lm.append(lpc); p5_sk_c5.append(c5)

    p5_ss_lm, p5_ss_c5 = [], []
    for _ in range(200):
        pool = [t for _, r, _, _ in all_runs for t in r if not t.startswith("LAT_") and t != "invT"]
        rng.shuffle(pool)
        it = iter(pool)
        shuf_runs = [(lc, [t if (t.startswith("LAT_") or t == "invT") else next(it) for t in r], rc, sp) for lc, r, rc, sp in all_runs]
        lpc, _, c5, _ = fast_eval(build_pre(shuf_runs, lm_ns, c2i), mono_key, poly_map, lm_ns, c2i, lex, beam_w=8)
        p5_ss_lm.append(lpc); p5_ss_c5.append(c5)

    out = [
        "# Zero-Leakage Statistical Validation — Pierfilippo Pandolfini -> Lorenzo de' Medici (Cat. Nos. 2574 & 2559)",
        "# Script: validate.py (seed=14820, n_ctrl=200)",
        "# Inputs: transcript_2574.txt (1,114 tokens) + transcript_2559.txt (863 tokens) + key_pandolfini1482.tsv (75 types)",
        f"# Model: DenseLM order=5, early-Italian nospace trained on {n_corpus:,} chars (pandolfini1482, rucellai1482, mazzinghi1478, toledo1479 excluded); lexicon lang/lexicons/it.json.gz (ZERO target boosts)",
        "",
        "=== 1. REAL SCORES ===",
        f"M1 (Strict 0-choice Mono) | Unified ({m1_all[3]} chars): LM/ch={m1_all[0]:.4f} Cov4={m1_all[1]:.4f} Cov5={m1_all[2]:.4f}",
        f"M1 #2574 only             | ({m1_74[3]} chars):         LM/ch={m1_74[0]:.4f} Cov4={m1_74[1]:.4f} Cov5={m1_74[2]:.4f}",
        f"M1 #2559 only             | ({m1_59[3]} chars):         LM/ch={m1_59[0]:.4f} Cov4={m1_59[1]:.4f} Cov5={m1_59[2]:.4f}",
        f"P5 ({len(poly_map)}-Poly beam=8)        | Unified ({p5_all[3]} chars): LM/ch={p5_all[0]:.4f} Cov4={p5_all[1]:.4f} Cov5={p5_all[2]:.4f}",
        f"P5 #2574 only             | ({p5_74[3]} chars):         LM/ch={p5_74[0]:.4f} Cov4={p5_74[1]:.4f} Cov5={p5_74[2]:.4f}",
        f"P5 #2559 only             | ({p5_59[3]} chars):         LM/ch={p5_59[0]:.4f} Cov4={p5_59[1]:.4f} Cov5={p5_59[2]:.4f}",
        "",
        "=== 2. 200 SHUFFLE CONTROLS: STRICT MONOPHONIC M1 (ZERO BEAM CHOICE) ===",
    ]
    lm_checks: list[tuple[str, float, float]] = []
    for lbl, real_v, arr in [
        ("M1 Shuf-Key    LM/ch", m1_all[0], m1_sk_lm),
        ("M1 Shuf-Key    Cov5 ", m1_all[2], m1_sk_c5),
        ("M1 Shuf-Stream LM/ch", m1_all[0], m1_ss_lm),
        ("M1 Shuf-Stream Cov5 ", m1_all[2], m1_ss_c5),
    ]:
        mu, sd, mx, z, p = z_stats(real_v, arr)
        out.append(f"  {lbl}: real={real_v:.4f} vs ctrl={mu:.4f}+/-{sd:.4f} (max={mx:.4f}) -> z={z:+.2f}, p={p:.4f}")
        if "LM/ch" in lbl:
            lm_checks.append((lbl, z, p))

    out.append("")
    out.append(f"=== 3. 200 SHUFFLE CONTROLS: {len(poly_map)}-POLYPHONIC BEAM P5 (IDENTICAL BEAM=8 ON ALL CONTROLS) ===")
    for lbl, real_v, arr in [
        ("P5 Shuf-Key    LM/ch", p5_all[0], p5_sk_lm),
        ("P5 Shuf-Key    Cov5 ", p5_all[2], p5_sk_c5),
        ("P5 Shuf-Stream LM/ch", p5_all[0], p5_ss_lm),
        ("P5 Shuf-Stream Cov5 ", p5_all[2], p5_ss_c5),
    ]:
        mu, sd, mx, z, p = z_stats(real_v, arr)
        out.append(f"  {lbl}: real={real_v:.4f} vs ctrl={mu:.4f}+/-{sd:.4f} (max={mx:.4f}) -> z={z:+.2f}, p={p:.4f}")
        if "LM/ch" in lbl:
            lm_checks.append((lbl, z, p))

    passed = all(z >= 5.0 and p <= 0.01 for _, z, p in lm_checks)
    min_z = min(z for _, z, _ in lm_checks)
    max_p = max(p for _, _, p in lm_checks)
    verdict = "PASS" if passed else "FAIL"
    out.extend([
        "",
        f"DECISION: {verdict} (runtime {time.time()-t0:.1f}s; min_z={min_z:+.2f}, max_p={max_p:.4f}; threshold: all 4 LM/ch controls z >= 5.0 and p <= 0.01).",
    ])
    report = "\n".join(out) + "\n"
    (HERE / "validation.txt").write_text(report, encoding="utf-8")
    print(report)
    if not passed:
        sys.exit(1)


if __name__ == "__main__":
    main()
