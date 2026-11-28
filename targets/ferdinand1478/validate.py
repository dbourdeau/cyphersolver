#!/usr/bin/env python3
"""Zero-leakage, zero-boost statistical validation for Zaragoza AHPZ C_CRAR/000001/0024
(catalogue 2854, King Ferdinand II of Aragon -> King John II of Aragon, Seville, 9 June 1478).

Tests key_ferdinand1478.tsv applied deterministically to transcript_2854.txt against
200 shuffled keys and 200 shuffled token streams using cyphersolver's built-in
DenseLM 'es-golden-age-nospace' and unboosted lang/lexicons/es.json.gz (+ ca.json.gz
at 0.1 weight, ZERO target-specific word boosts).

Computes PASS/FAIL dynamically (requiring z_lm >= 5.0 and p <= 0.01 on both 200-shuffle
LM controls) and exits non-zero (1) on FAIL. Writes validation.txt.
"""
from __future__ import annotations

import collections
import csv
import gzip
import json
import math
import pathlib
import random
import statistics
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent


def _find_repo() -> pathlib.Path:
    for cand in [HERE.parents[1], pathlib.Path.cwd()] + [p / "cyphersolver_repo" for p in HERE.parents]:
        if (cand / "lang" / "lm.py").is_file() and (cand / "lang" / "lexicons" / "es.json.gz").is_file():
            return cand
    raise FileNotFoundError("Cannot locate cyphersolver repo root containing lang/lm.py")


REPO = _find_repo()
sys.path.insert(0, str(REPO))
from lang import lm as clm  # noqa: E402


class UnboostedSpanishLexicon:
    """Viterbi word segmenter over unboosted lang/lexicons/es.json.gz + ca.json.gz (ZERO custom boosts)."""

    def __init__(self) -> None:
        self.freq: collections.Counter[str] = collections.Counter()
        es_raw = json.loads(gzip.open(REPO / "lang" / "lexicons" / "es.json.gz", "rt", encoding="utf-8").read())
        for w, c in es_raw.items():
            nw = clm.norm(w, scheme="early", spaces=False)
            if nw:
                self.freq[nw] += c
        ca_path = REPO / "lang" / "lexicons" / "ca.json.gz"
        if ca_path.is_file():
            ca_raw = json.loads(gzip.open(ca_path, "rt", encoding="utf-8").read())
            for w, c in ca_raw.items():
                if c >= 10:
                    nw = clm.norm(w, scheme="early", spaces=False)
                    if nw:
                        self.freq[nw] += max(1, c // 10)
        self.total = sum(self.freq.values())
        self.words = {w for w, c in self.freq.items() if c >= 3}
        self.max_len = max((len(w) for w in self.words), default=16)
        self.logp = {w: math.log(c / self.total) for w, c in self.freq.items() if c >= 3}
        self.one_char = {"a", "e", "y", "o", "u"}

    def segment_and_eval(self, text_ns: str) -> tuple[float, float, float, float, int]:
        s = clm.norm(text_ns, scheme="early", spaces=False)
        n = len(s)
        if n == 0:
            return 0.0, 0.0, 0.0, 0.0, 0
        dp = [-1e18] * (n + 1)
        back = [0] * (n + 1)
        dp[0] = 0.0
        unk_pen = math.log(1e-8)
        for i in range(n):
            if dp[i] <= -1e17:
                continue
            lim = min(n, i + self.max_len)
            for j in range(i + 1, lim + 1):
                sub = s[i:j]
                L = j - i
                if L == 1:
                    if sub in self.one_char:
                        cand = dp[i] + self.logp.get(sub, -6.0) - 0.5
                    else:
                        cand = dp[i] + unk_pen - 4.0
                elif sub in self.logp:
                    cand = dp[i] + self.logp[sub] + 0.55 * L
                else:
                    if L <= 8:
                        cand = dp[i] + unk_pen - 2.2 * L
                    else:
                        continue
                if cand > dp[j]:
                    dp[j] = cand
                    back[j] = i
        words = []
        idx = n
        while idx > 0:
            prev = back[idx]
            words.append(s[prev:idx])
            idx = prev
        words.reverse()
        hits = l3 = h3 = c4 = c5 = tot_ch = 0
        for w in words:
            ok = w in self.words
            L = len(w)
            tot_ch += L
            if ok:
                hits += 1
                if L >= 4:
                    c4 += L
                if L >= 5:
                    c5 += L
            if L >= 3:
                l3 += 1
                if ok:
                    h3 += 1
        return hits / max(1, len(words)), h3 / max(1, l3), c4 / max(1, tot_ch), c5 / max(1, tot_ch), len(words)


def load_key(path: pathlib.Path) -> dict[str, str]:
    km: dict[str, str] = {}
    with path.open(encoding="utf-8") as fh:
        rows = csv.DictReader((r for r in fh if not r.startswith("#")), delimiter="\t")
        for row in rows:
            tok = row["token"].strip()
            val = row["value"].strip()
            km[tok] = "" if val in ("?", "NULL") else clm.norm(val, scheme="early", spaces=False)
    return km


def load_tokens(path: pathlib.Path) -> list[str]:
    toks: list[str] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        s = raw.strip()
        if not s or s.startswith("#"):
            continue
        _, _, body = s.split("\t", 2)
        toks.extend(body.split())
    return toks


def eval_key(tokens: list[str], key_map: dict[str, str], lm_ns, lex: UnboostedSpanishLexicon) -> tuple[float, float, float, float, float, int, int]:
    pt = "".join(key_map.get(t, "") for t in tokens)
    seq = lm_ns.encode(pt)
    if len(seq) == 0:
        return -99.0, 0.0, 0.0, 0.0, 0.0, 0, 0
    lpc = float(lm_ns.score_idx(seq)) / len(seq)
    wh, h3, c4, c5, n_w = lex.segment_and_eval(pt)
    return lpc, wh, h3, c4, c5, len(pt), n_w


def z_stats(real_v: float, ctrls: list[float]) -> tuple[float, float, float, float, int, float]:
    mu = statistics.mean(ctrls)
    sd = statistics.stdev(ctrls) if len(ctrls) > 1 else 0.0
    z = (real_v - mu) / sd if sd > 1e-12 else 0.0
    ge = sum(1 for x in ctrls if x >= real_v)
    p = (ge + 1) / (len(ctrls) + 1)
    return mu, sd, max(ctrls), z, ge, p


def main() -> None:
    t0 = time.time()
    lm_ns = clm.load("es-golden-age-nospace")
    lex = UnboostedSpanishLexicon()
    key = load_key(HERE / "key_ferdinand1478.tsv")
    tokens = load_tokens(HERE / "transcript_2854.txt")
    obs_toks = sorted(set(tokens))
    mapped = sum(1 for t in tokens if key.get(t, ""))

    real = eval_key(tokens, key, lm_ns, lex)
    rng = random.Random(1478)
    real_vals = [key.get(t, "") for t in obs_toks]

    sk = ([], [], [], [], [])
    for _ in range(200):
        perm = list(real_vals)
        rng.shuffle(perm)
        km = dict(zip(obs_toks, perm))
        r = eval_key(tokens, km, lm_ns, lex)
        for i in range(5):
            sk[i].append(r[i])

    ss = ([], [], [], [], [])
    for _ in range(200):
        shuf_t = list(tokens)
        rng.shuffle(shuf_t)
        r = eval_key(shuf_t, key, lm_ns, lex)
        for i in range(5):
            ss[i].append(r[i])

    out = [
        "# Zero-Leakage, Zero-Boost Statistical Validation — Zaragoza AHPZ C_CRAR/000001/0024 (Cat. 2854, Seville 9 Jun 1478)",
        "# Script: validate.py (seed=1478, n_ctrl=200)",
        f"# Inputs: transcript_2854.txt ({len(tokens)} tokens, {len(obs_toks)} distinct types) + key_ferdinand1478.tsv ({mapped}/{len(tokens)} = {100*mapped/len(tokens):.2f}% mapped)",
        "# Model: cyphersolver built-in DenseLM 'es-golden-age-nospace' + unboosted lang/lexicons/es.json.gz (+ ca.json.gz x0.1, ZERO custom boosts)",
        "",
        "=== 1. STRICT ZERO-CHOICE DETERMINISTIC KEY EVALUATION ===",
        f"tokens={len(tokens)}, mapped={mapped}/{len(tokens)} ({100*mapped/len(tokens):.2f}%), decoded_chars={real[5]}, viterbi_words={real[6]}",
        f"REAL: LM/ch={real[0]:.4f} | WordHit={real[1]:.4f} | Len3Hit={real[2]:.4f} | Cov4={real[3]:.4f} | Cov5={real[4]:.4f}",
        "",
        "=== 2. 200 SHUFFLED-KEY & 200 SHUFFLED-STREAM NULL CONTROLS ===",
    ]

    passed = True
    fail_reasons: list[str] = []
    for lbl, idx, arr in [
        ("Shuf-Key  (n=200) LM/ch  ", 0, sk[0]),
        ("Shuf-Key  (n=200) WordHit", 1, sk[1]),
        ("Shuf-Key  (n=200) Len3Hit", 2, sk[2]),
        ("Shuf-Key  (n=200) Cov4   ", 3, sk[3]),
        ("Shuf-Key  (n=200) Cov5   ", 4, sk[4]),
        ("Shuf-Strm (n=200) LM/ch  ", 0, ss[0]),
        ("Shuf-Strm (n=200) WordHit", 1, ss[1]),
        ("Shuf-Strm (n=200) Len3Hit", 2, ss[2]),
        ("Shuf-Strm (n=200) Cov4   ", 3, ss[3]),
        ("Shuf-Strm (n=200) Cov5   ", 4, ss[4]),
    ]:
        mu, sd, mx, z, ge, p = z_stats(real[idx], arr)
        out.append(f"  {lbl}: real={real[idx]:7.4f} vs null={mu:7.4f}+/-{sd:6.4f} (max={mx:7.4f}) | z={z:+6.2f} | >=real={ge}/200 (p={p:.4f})")
        if idx == 0 and (p > 0.01 or z < 5.0):
            passed = False
            fail_reasons.append(f"{lbl.strip()} z={z:+.2f}, p={p:.4f}")

    out.append("")
    if passed:
        out.append(f"DECISION: PASS (runtime {time.time()-t0:.1f}s; both 200-shuffle LM controls satisfy z_lm >= 5.0 and p <= 0.01).")
    else:
        out.append(f"DECISION: FAIL (runtime {time.time()-t0:.1f}s; " + "; ".join(fail_reasons) + ").")

    report = "\n".join(out) + "\n"
    (HERE / "validation.txt").write_text(report, encoding="utf-8")
    print(report)
    if not passed:
        sys.exit(1)


if __name__ == "__main__":
    main()
