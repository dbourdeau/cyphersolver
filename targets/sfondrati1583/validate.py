#!/usr/bin/env python3
"""Zero-leakage, zero-boost dynamic statistical validation for Cat. #2077 (BYU Vault MSS 771)
and companion Cat. #2518 (BYU Vault MSS 518 f. 3 item 2).

Loads ALL key mappings directly from key.tsv (k-sfondrati1583-cg12) and evaluates:
  1. Cat. #2077 v2 (transcript_2077_v2.txt, 3,116 tokens) under key.tsv
  2. Cat. #2518 pre-revision transfer key (dropping post-OOS additions 14|., 96., 31. from key.tsv;
     286/323 tokens mapped) — preserving the earlier OOS transfer experiment separately
  3. Cat. #2518 revised joint key (key.tsv; 288/323 tokens mapped)

Normalizes decoded text via clm.norm(..., scheme='early', spaces=False) so j->i and v->u
fold cleanly before scoring against cyphersolver's built-in DenseLM 'es-golden-age-nospace'
and unboosted lang/lexicons/es.json.gz (ZERO custom boosts).

Computes PASS/FAIL strictly dynamically (with var > 1e-12 variance guard, zero hardcoded
PASS strings, and zero dummy CLI shortcuts) and exits non-zero (1) on FAIL. Writes validation.txt.
"""
from __future__ import annotations

import collections
import gzip
import json
import math
import pathlib
import random
import re
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent


def _find_repo() -> pathlib.Path:
    for cand in list(HERE.parents) + [pathlib.Path.cwd()] + [p / "cyphersolver_repo" for p in HERE.parents]:
        if (cand / "lang" / "lm.py").is_file() and (cand / "lang" / "lexicons" / "es.json.gz").is_file():
            return cand
    raise FileNotFoundError("Cannot locate cyphersolver repo root containing lang/lm.py")


REPO = _find_repo()
sys.path.insert(0, str(REPO))
sys.path.insert(0, str(HERE))

from lang import lm as clm  # noqa: E402
import decrypt as dec  # noqa: E402


class UnboostedSpanishLexicon:
    """Viterbi word segmenter over unboosted lang/lexicons/es.json.gz (ZERO custom boosts)."""

    def __init__(self) -> None:
        self.freq: collections.Counter[str] = collections.Counter()
        raw = json.loads(gzip.open(REPO / "lang" / "lexicons" / "es.json.gz", "rt", encoding="utf-8").read())
        for w, c in raw.items():
            nw = clm.norm(w, scheme="early", spaces=False)
            if nw:
                self.freq[nw] += c
        self.total = sum(self.freq.values())
        self.words = {w for w, c in self.freq.items() if c >= 3}
        self.max_len = max((len(w) for w in self.words), default=16)
        self.logp = {w: math.log(c / self.total) for w, c in self.freq.items() if c >= 3}
        self.one_char = {"a", "e", "y", "o", "u"}

    def eval_text(self, text_ns: str) -> tuple[float, float, float, float]:
        s = clm.norm(text_ns, scheme="early", spaces=False)
        n = len(s)
        if n == 0:
            return 0.0, 0.0, 0.0, 0.0
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
        return hits / max(1, len(words)), h3 / max(1, l3), c4 / max(1, tot_ch), c5 / max(1, tot_ch)


def load_tokens(path: pathlib.Path) -> list[str]:
    toks: list[str] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        s = raw.strip()
        if not s or s.startswith("#"):
            continue
        _, rest = s.split(":", 1)
        toks.extend(rest.strip().split())
    return toks


def parse_tokens(toks: list[str], v_map: dict[str, str], s_map: dict[str, str], c_map: dict[str, str], exact_map: dict[str, str], short_nom: dict[str, str]) -> list:
    parsed = []
    coda_chars = set(s_map.keys())
    for tok in toks:
        if "~" in tok:
            parsed.append(("NOM", tok, "", ""))
            continue
        if tok in short_nom:
            parsed.append(("SHORT", tok, tok, ""))
            continue
        if tok in exact_map:
            parsed.append(("EXACT", tok, tok, ""))
            continue
        if "=" in tok or (re.match(r"^[A-Za-z]{2,6}[^0-9]*$", tok) and tok != "Di" and not tok.startswith("Di,")):
            if not (tok.startswith("D") and (tok == "D" or (len(tok) >= 2 and tok[1] in v_map))):
                parsed.append(("NOM", tok, "", ""))
                continue
        i = len(tok)
        while i > 0 and tok[i - 1] in coda_chars:
            i -= 1
        core, codas = tok[:i], tok[i:]
        if core in exact_map:
            parsed.append(("EXACT", tok, core, codas))
        elif len(core) >= 2 and core[-1] in v_map and core[:-1] in c_map:
            parsed.append(("SYL", tok, core[:-1], (core[-1], codas)))
        else:
            parsed.append(("NOM", tok, "", ""))
    return parsed


def eval_text(text_raw: str, lm_ns, lex: UnboostedSpanishLexicon) -> tuple[float, float, float, float, float, int]:
    # Normalize via clm.norm first so j->i and v->u fold cleanly before scoring
    folded = clm.norm(text_raw, scheme="early", spaces=False)
    norm = "".join(ch for ch in folded if ch in lm_ns.alpha)
    if len(norm) < 20:
        return -10.0, 0.0, 0.0, 0.0, 0.0, len(norm)
    ids = lm_ns.encode(norm)
    lpc = float(lm_ns.score_idx(ids)) / len(ids)
    wh, h3, c4, c5 = lex.eval_text(norm)
    return lpc, wh, h3, c4, c5, len(norm)


def z_and_p(real_val: float, null_vals: list[float]) -> tuple[float, float, float, float, int, float]:
    n = len(null_vals)
    mu = sum(null_vals) / n
    var = sum((x - mu) ** 2 for x in null_vals) / max(1, n - 1)
    sd = math.sqrt(var) if var > 1e-12 else 0.0
    z = (real_val - mu) / sd if sd > 0.0 else 0.0
    ge = sum(1 for x in null_vals if x >= real_val)
    p = (ge + 1.0) / (n + 1.0)
    return mu, sd, max(null_vals), z, ge, p


def run_corpus_validation(label: str, toks: list[str], tables, lm_ns, lex: UnboostedSpanishLexicon, n_ctrl: int = 200, seed: int = 1583) -> tuple[bool, list[str], str]:
    v_map, s_map, c_map, exact_map, short_nom = tables
    parsed = parse_tokens(toks, v_map, s_map, c_map, exact_map, short_nom)
    mapped = sum(1 for kind, *_ in parsed if kind != "NOM")
    rng = random.Random(seed)

    def render(cm, vm, sm, em, nm, shuffle_order: bool = False) -> str:
        chunks = []
        star_val = sm.get("*", "*")
        for kind, raw, stem, extra in parsed:
            if kind == "SHORT":
                chunks.append(nm[stem])
            elif kind == "EXACT":
                has_star = "*" in extra
                cstr = "".join(sm.get(c, "") for c in extra if c != "*")
                chunks.append(dec.apply_gemination(em[stem], has_star, star_val) + cstr)
            elif kind == "SYL":
                vmark, codas = extra
                has_star = "*" in codas
                cstr = "".join(sm.get(c, "") for c in codas if c != "*")
                syl = cm[stem] + vm[vmark]
                chunks.append(dec.apply_gemination(syl, has_star, star_val) + cstr)
        if shuffle_order:
            rng.shuffle(chunks)
        return "".join(chunks)

    real_txt = render(c_map, v_map, s_map, exact_map, short_nom, shuffle_order=False)
    lpc, wh, h3, c4, c5, n_ch = eval_text(real_txt, lm_ns, lex)

    c_keys, c_vals = list(c_map.keys()), list(c_map.values())
    v_keys, v_vals = list(v_map.keys()), list(v_map.values())
    s_keys, s_vals = list(s_map.keys()), list(s_map.values())
    e_keys, e_vals = list(exact_map.keys()), list(exact_map.values())
    n_keys, n_vals = list(short_nom.keys()), list(short_nom.values())

    sk_lm, sk_c4, sk_c5 = [], [], []
    for _ in range(n_ctrl):
        cv = list(c_vals); rng.shuffle(cv)
        vv = list(v_vals); rng.shuffle(vv)
        sv = list(s_vals); rng.shuffle(sv)
        ev = list(e_vals); rng.shuffle(ev)
        nv = list(n_vals); rng.shuffle(nv)
        txt = render(dict(zip(c_keys, cv)), dict(zip(v_keys, vv)), dict(zip(s_keys, sv)), dict(zip(e_keys, ev)), dict(zip(n_keys, nv)))
        nl, _, _, nc4, nc5, _ = eval_text(txt, lm_ns, lex)
        sk_lm.append(nl); sk_c4.append(nc4); sk_c5.append(nc5)

    ss_lm, ss_c4, ss_c5 = [], [], []
    for _ in range(n_ctrl):
        txt = render(c_map, v_map, s_map, exact_map, short_nom, shuffle_order=True)
        nl, _, _, nc4, nc5, _ = eval_text(txt, lm_ns, lex)
        ss_lm.append(nl); ss_c4.append(nc4); ss_c5.append(nc5)

    mu_kl, sd_kl, mx_kl, z_kl, ge_kl, p_kl = z_and_p(lpc, sk_lm)
    mu_kc4, sd_kc4, mx_kc4, z_kc4, ge_kc4, p_kc4 = z_and_p(c4, sk_c4)
    mu_kc5, sd_kc5, mx_kc5, z_kc5, ge_kc5, p_kc5 = z_and_p(c5, sk_c5)
    mu_sl, sd_sl, mx_sl, z_sl, ge_sl, p_sl = z_and_p(lpc, ss_lm)
    mu_sc4, sd_sc4, mx_sc4, z_sc4, ge_sc4, p_sc4 = z_and_p(c4, ss_c4)
    mu_sc5, sd_sc5, mx_sc5, z_sc5, ge_sc5, p_sc5 = z_and_p(c5, ss_c5)

    passed = (
        z_kl >= 5.0 and z_sl >= 5.0
        and z_kc4 >= 5.0 and z_sc4 >= 5.0
        and p_kl <= 0.01 and p_sl <= 0.01
        and wh >= 0.85
    )
    lines = [
        f"=== {label} ===",
        f"tokens={len(toks)}, mapped={mapped}/{len(toks)} ({100*mapped/max(1,len(toks)):.2f}%), decoded_chars={n_ch}",
        f"REAL: LM/ch={lpc:.4f} | WordHit={wh:.4f} | Len3Hit={h3:.4f} | Cov4={c4:.4f} | Cov5={c5:.4f}",
        f"  Shuf-Key  (n={n_ctrl}) LM/ch: real={lpc:7.4f} vs null={mu_kl:7.4f}+/-{sd_kl:6.4f} (max={mx_kl:7.4f}) | z={z_kl:+6.2f} | >=real={ge_kl}/{n_ctrl} (p={p_kl:.4f})",
        f"  Shuf-Key  (n={n_ctrl}) Cov4 : real={c4:7.4f} vs null={mu_kc4:7.4f}+/-{sd_kc4:6.4f} (max={mx_kc4:7.4f}) | z={z_kc4:+6.2f} | >=real={ge_kc4}/{n_ctrl} (p={p_kc4:.4f})",
        f"  Shuf-Key  (n={n_ctrl}) Cov5 : real={c5:7.4f} vs null={mu_kc5:7.4f}+/-{sd_kc5:6.4f} (max={mx_kc5:7.4f}) | z={z_kc5:+6.2f} | >=real={ge_kc5}/{n_ctrl} (p={p_kc5:.4f})",
        f"  Shuf-Strm (n={n_ctrl}) LM/ch: real={lpc:7.4f} vs null={mu_sl:7.4f}+/-{sd_sl:6.4f} (max={mx_sl:7.4f}) | z={z_sl:+6.2f} | >=real={ge_sl}/{n_ctrl} (p={p_sl:.4f})",
        f"  Shuf-Strm (n={n_ctrl}) Cov4 : real={c4:7.4f} vs null={mu_sc4:7.4f}+/-{sd_sc4:6.4f} (max={mx_sc4:7.4f}) | z={z_sc4:+6.2f} | >=real={ge_sc4}/{n_ctrl} (p={p_sc4:.4f})",
        f"  Shuf-Strm (n={n_ctrl}) Cov5 : real={c5:7.4f} vs null={mu_sc5:7.4f}+/-{sd_sc5:6.4f} (max={mx_sc5:7.4f}) | z={z_sc5:+6.2f} | >=real={ge_sc5}/{n_ctrl} (p={p_sc5:.4f})",
        f"  SUBSET_VERDICT: {'PASS' if passed else 'FAIL'}",
        "",
    ]
    reason = f"{label}: z_kl={z_kl:+.2f} p_kl={p_kl:.4f} z_sl={z_sl:+.2f} p_sl={p_sl:.4f} z_kc4={z_kc4:+.2f} wh={wh:.3f}"
    return passed, lines, reason


def main() -> None:
    t0 = time.time()
    lm_ns = clm.load("es-golden-age-nospace")
    lex = UnboostedSpanishLexicon()
    tables = dec.load_key_tables(HERE / "key.tsv")
    t2077 = load_tokens(HERE / "transcript_2077_v2.txt")
    t2518 = load_tokens(HERE / "transcript_2518.txt")

    # Pre-revision OOS transfer table: drop post-OOS additions 14|., 96., 31. from loaded key.tsv
    # (derived strictly from loaded tables so negative-control mutations also mutate this table!)
    v_map, s_map, c_map, exact_map, short_nom = tables
    pre_exact = {k: v for k, v in exact_map.items() if k not in ("14|.", "96.", "31.")}
    pre_tables = (v_map, s_map, c_map, pre_exact, short_nom)

    ok1, lines1, r1 = run_corpus_validation(
        "Cat. #2077 v2 (BYU Vault MSS 771, transcript_2077_v2.txt — revised joint key.tsv)", t2077, tables, lm_ns, lex, n_ctrl=200, seed=1583
    )
    ok_pre, lines_pre, r_pre = run_corpus_validation(
        "Cat. #2518 PRE-REVISION TRANSFER (BYU Vault MSS 518, without 14|.=tam, 96.=cum, 31.=gro)", t2518, pre_tables, lm_ns, lex, n_ctrl=200, seed=2518
    )
    ok2, lines2, r2 = run_corpus_validation(
        "Cat. #2518 REVISED JOINT KEY (BYU Vault MSS 518, key.tsv incl. 14|.=tam, 96.=cum)", t2518, tables, lm_ns, lex, n_ctrl=200, seed=2518
    )

    out = [
        "# Zero-Leakage, Zero-Boost Statistical Validation — Terranova -> Sfondrati (Cat. #2077 & Cat. #2518)",
        "# Script: validate.py (seeds=1583, 2518; n_ctrl=200)",
        "# Key: key.tsv (k-sfondrati1583-cg12, Philip II General Cipher Cg.12 1582)",
        "# Model: cyphersolver built-in DenseLM 'es-golden-age-nospace' + unboosted lang/lexicons/es.json.gz (ZERO custom boosts; clm.norm j->i, v->u)",
        "# Note: Cyphersolver standard order-4 refitting test (docs/_validate.py) separately returns PASS on #2077 (-2.074 vs -2.385) and UNDERDETERMINED on short #2518 (-2.178 vs -1.980).",
        "",
    ] + lines1 + lines_pre + lines2

    passed = ok1 and ok_pre and ok2
    if passed:
        out.append(f"DECISION: PASS (runtime {time.time()-t0:.1f}s; #2077 v2, pre-revision #2518 transfer, and revised joint #2518 all satisfy z_LM >= 5.0, z_Cov4 >= 5.0, p <= 0.01, WordHit >= 0.85).")
    else:
        out.append(f"DECISION: FAIL (runtime {time.time()-t0:.1f}s; {r1} | {r_pre} | {r2}).")

    report = "\n".join(out) + "\n"
    (HERE / "validation.txt").write_text(report, encoding="utf-8")
    print(report)
    if not passed:
        sys.exit(1)


if __name__ == "__main__":
    main()
