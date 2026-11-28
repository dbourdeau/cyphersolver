#!/usr/bin/env python3
"""Statistical validation of key_mdp384_witness.tsv on ASF MdP 384, c. 78r (catalogue 2339).

Tests the strictly witness-attested key (zero c. 78r-only entries) against 200 class-preserving
shuffled keys and 200 shuffled token streams on:
  1. Full c. 78r (L01-L27)
  2. Revisited subset L12-L18 (originally reserved by Brice Dudout, later examined on the scan)

Uses the repository's DenseLM (order=5, scheme='early', spaces=False) trained on pre-1650 Italian
target texts (excluding farnese1547 itself) and the repository Italian lexicon (lang/lexicons/it.json.gz)
with zero target-specific word boosts. Writes validation_78r.txt alongside this script.
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

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import decrypt_78r as dec  # noqa: E402


def _find_repo() -> pathlib.Path:
    for cand in [HERE.parents[1], HERE.parents[2] / "cyphersolver_repo", pathlib.Path.cwd()]:
        if (cand / "lang" / "lm.py").is_file() and (cand / "lang" / "lexicons" / "it.json.gz").is_file():
            return cand
    raise FileNotFoundError("Cannot locate cyphersolver repo root containing lang/lm.py")


REPO = _find_repo()
sys.path.insert(0, str(REPO))
from lang.lm import DenseLM, alphabet, norm  # noqa: E402

IT_WORDS_FILTER = set(
    "che di la il non per con si se et le della delle del dello alla alle quello questo questa sua suo "
    "ma sono essere da dal dalla come anche ancora tutto tutti molto piu cosa cose nostro vostra signore "
    "stato haver havere fatto quale quali questi quelli loro noi voi lui lei gli una uno mi ti ci vi ne "
    "lo li ha hanno era erano sia siano perche poi qui qua ogni altro altra altri senza sopra sotto "
    "dopo prima tanto quanto bene male dio papa imperatore francia roma parma piacenza eccellenza santita maesta".split()
)
EN_DE_STOP = set(
    "the and of to in is that for with on was as by this from are not be it have or an which were been "
    "der die das und ist nicht von zu den dem des mit auf ein eine".split()
)


def build_italian_lm(exclude_target: str = "farnese1547") -> tuple[DenseLM, int]:
    """Train order-5 early-Italian nospace DenseLM from pre-1650 repository texts, excluding this target."""
    chunks = []
    targets_dir = REPO / "targets"
    # If running inside a minimal sandbox with only one target, fall back to full repo targets if available.
    if targets_dir.is_dir() and len(list(targets_dir.glob("*/profile.json"))) < 5:
        for par in HERE.parents:
            alt = par / "cyphersolver_repo" / "targets"
            if alt.is_dir() and len(list(alt.glob("*/profile.json"))) >= 5:
                targets_dir = alt
                break
    for pj in sorted(targets_dir.glob("*/profile.json")):
        if pj.parent.name == exclude_target:
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
        tdir = pj.parent
        cand_files = set()
        for t in d.get("outcome", {}).get("texts", []):
            for k in ("decryption", "contemporary", "reading"):
                fn = t.get(k)
                if isinstance(fn, str) and fn.endswith(".txt"):
                    cand_files.add(tdir / fn)
        for fn in sorted(tdir.glob("*.txt")) + sorted(tdir.glob("texts/*.txt")):
            if any(w in fn.name.lower() for w in ("reading", "plaintext", "decryption", "cleartext")):
                cand_files.add(fn)
        for fp in sorted(cand_files):
            if not fp.exists():
                continue
            txt = fp.read_text(encoding="utf-8", errors="ignore")
            for line in txt.splitlines():
                line_clean = re.sub(r"\[[^\]]*\]|\{[^}]*\}|[?*_#`<>|]", " ", line)
                words = re.findall(r"[A-Za-zÀ-ÿ]+", line_clean.lower())
                if len(words) < 6:
                    continue
                it_hits = sum(w in IT_WORDS_FILTER for w in words)
                bad_hits = sum(w in EN_DE_STOP for w in words)
                if it_hits >= 1 and it_hits >= 2 * bad_hits:
                    chunks.append(line_clean)
    txt_ns = norm("\n".join(chunks), scheme="early", spaces=False)
    lm_ns = DenseLM.build(txt_ns, order=5, alpha=alphabet("early", spaces=False), meta={"name": "it_early_nospace_o5"})
    return lm_ns, len(txt_ns)


class LexiconScorer:
    """Word-DP segmentation coverage over lang/lexicons/it.json.gz (no target-specific boosts)."""

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


def load_normalized_key() -> dict[str, str]:
    raw_key = dec.load_witness_key(dec.KEY_PATH)
    clean_map = {
        "S.S.ta": "sua santita",
        "S.M.ta": "sua maesta",
        "Re": "re",
        "Principe": "principe",
        "Signor": "signor",
        "Duca": "duca",
        "Vescovo": "vescovo",
        "Ambasciatore": "ambasciatore",
        "Fiorenza": "fiorenza",
        "Italia": "italia",
        "Francia": "francia",
        "Inghilterra": "inghilterra",
        "Ferrara": "ferrara",
        "Parma": "parma",
        "Piacenza": "piacenza",
        "Napoli": "napoli",
        "per il quale": "per il quale",
        "NULL": "",
    }
    return {k: norm(clean_map.get(v, v), "early", False) for k, v in raw_key.items()}


def load_line_tokens() -> dict[str, list[tuple[str, str]]]:
    lines_toks: dict[str, list[tuple[str, str]]] = {}
    for raw in dec.TRANS_PATH.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^(L\d{2})\s+(.*)$", raw)
        if not m:
            continue
        lbl, body = m.group(1), m.group(2)
        toks = []
        for part in re.split(r"(<<.*?>>)", body):
            if not part.strip() or (part.startswith("<<") and part.endswith(">>")):
                continue
            toks.extend(dec.tokenize_run(part))
        lines_toks[lbl] = toks
    return lines_toks


def eval_subset(
    label_list: list[str],
    lines_toks: dict[str, list[tuple[str, str]]],
    key_dict: dict[str, str],
    lm_ns: DenseLM,
    lex: LexiconScorer,
    n_ctrl: int = 200,
    seed: int = 1547,
) -> dict:
    toks = [t for lbl in label_list for t in lines_toks[lbl]]

    def _decode(seq: list[tuple[str, str]], kd: dict[str, str]) -> str:
        out = []
        for b, f in seq:
            v = dec.lookup(b, f, kd)
            if v:
                out.append(v)
        return "".join(out)

    plain = _decode(toks, key_dict)
    mapped = sum(1 for b, f in toks if dec.lookup(b, f, key_dict) is not None)
    distinct_types = len({f for _, f in toks})
    lm_real = lm_ns.per_char(plain)
    cov4_real, cov5_real = lex.segment(plain)

    rng = random.Random(seed)
    # Class-preserving key shuffles: permute within 1-digit, 2-digit 1-char, and 2-digit multi-char classes separately
    keys1 = [k for k in key_dict if len(re.sub(r"[^0-9]", "", k)) == 1]
    keys2_1ch = [k for k in key_dict if len(re.sub(r"[^0-9]", "", k)) == 2 and len(key_dict[k]) == 1]
    keys2_multi = [k for k in key_dict if len(re.sub(r"[^0-9]", "", k)) == 2 and len(key_dict[k]) != 1]
    vals1 = [key_dict[k] for k in keys1]
    vals2_1ch = [key_dict[k] for k in keys2_1ch]
    vals2_multi = [key_dict[k] for k in keys2_multi]

    lm_shuf_keys, cov5_shuf_keys = [], []
    for _ in range(n_ctrl):
        v1 = list(vals1); rng.shuffle(v1)
        v2a = list(vals2_1ch); rng.shuffle(v2a)
        v2b = list(vals2_multi); rng.shuffle(v2b)
        kd = dict(zip(keys1, v1))
        kd.update(zip(keys2_1ch, v2a))
        kd.update(zip(keys2_multi, v2b))
        p = _decode(toks, kd)
        lm_shuf_keys.append(lm_ns.per_char(p) if len(p) > 10 else -9.0)
        cov5_shuf_keys.append(lex.segment(p)[1] if len(p) > 10 else 0.0)

    lm_shuf_toks, cov5_shuf_toks = [], []
    for _ in range(n_ctrl):
        st = list(toks); rng.shuffle(st)
        p = _decode(st, key_dict)
        lm_shuf_toks.append(lm_ns.per_char(p) if len(p) > 10 else -9.0)
        cov5_shuf_toks.append(lex.segment(p)[1] if len(p) > 10 else 0.0)

    def _stats(real_v: float, arr: list[float]) -> tuple[float, float, float, float, int, float]:
        m = sum(arr) / len(arr)
        sd = math.sqrt(sum((x - m) ** 2 for x in arr) / max(1, len(arr) - 1))
        z = (real_v - m) / sd if sd > 1e-9 else 0.0
        ge = sum(1 for x in arr if x >= real_v)
        p = (ge + 1) / (len(arr) + 1)
        return m, sd, max(arr), z, ge, p

    return {
        "n_toks": len(toks),
        "mapped": mapped,
        "types": distinct_types,
        "n_chars": len(plain),
        "lm_real": lm_real,
        "cov4_real": cov4_real,
        "cov5_real": cov5_real,
        "lm_vs_shuf_keys": _stats(lm_real, lm_shuf_keys),
        "cov5_vs_shuf_keys": _stats(cov5_real, cov5_shuf_keys),
        "lm_vs_shuf_toks": _stats(lm_real, lm_shuf_toks),
        "cov5_vs_shuf_toks": _stats(cov5_real, cov5_shuf_toks),
        "sample": plain[:160],
    }


def main() -> None:
    lm_ns, n_corpus = build_italian_lm(exclude_target="farnese1547")
    lex = LexiconScorer()
    key_dict = load_normalized_key()
    lines_toks = load_line_tokens()

    all_lbls = sorted(lines_toks.keys())
    held_out_lbls = [f"L{i:02d}" for i in range(12, 19)]

    out = [
        "# Statistical validation of ASF Mediceo del Principato 384, c. 78r (catalogue 2339)",
        "# Script: validate_c78r.py (seed=1547, n_ctrl=200)",
        "# Inputs: transcription_78r.txt (2,244 cipher digits) + key_mdp384_witness.tsv (69 witness-only entries; zero c. 78r-only entries)",
        f"# Model: DenseLM order=5, early-Italian nospace trained on {n_corpus:,} chars of pre-1650 Italian targets (farnese1547 excluded); lexicon lang/lexicons/it.json.gz (no target boosts)",
        "# Note: Brice Dudout's frozen c. 76r held-out validation remains untouched in validation.txt.",
        "",
    ]

    passed = True
    fail_reasons: list[str] = []
    for name, subset in [("FULL c. 78r (L01-L27)", all_lbls), ("SUBSET c. 78r (L12-L18, revisited)", held_out_lbls)]:
        r = eval_subset(subset, lines_toks, key_dict, lm_ns, lex, n_ctrl=200, seed=1547)
        out.append(f"=== {name} ===")
        out.append(
            f"tokens={r['n_toks']} (mapped={r['mapped']}/{r['n_toks']} = {100*r['mapped']/r['n_toks']:.1f}%), "
            f"distinct_types={r['types']}, decoded_chars={r['n_chars']}"
        )
        mk, sdk, mxk, zk, gek, pk = r["lm_vs_shuf_keys"]
        out.append(f"LM/char vs 200 shuffled keys:    real={r['lm_real']:.4f} | mean={mk:.4f} sd={sdk:.4f} max={mxk:.4f} | z={zk:+.2f} | >=real={gek}/200 (p={pk:.4f})")
        m, sd, mx, z, ge, p = r["cov5_vs_shuf_keys"]
        out.append(f"Cov>=5  vs 200 shuffled keys:    real={r['cov5_real']:.4f} | mean={m:.4f} sd={sd:.4f} max={mx:.4f} | z={z:+.2f} | >=real={ge}/200 (p={p:.4f})")
        ms, sds, mxs, zs, ges, ps = r["lm_vs_shuf_toks"]
        out.append(f"LM/char vs 200 shuffled streams: real={r['lm_real']:.4f} | mean={ms:.4f} sd={sds:.4f} max={mxs:.4f} | z={zs:+.2f} | >=real={ges}/200 (p={ps:.4f})")
        m, sd, mx, z, ge, p = r["cov5_vs_shuf_toks"]
        out.append(f"Cov>=5  vs 200 shuffled streams: real={r['cov5_real']:.4f} | mean={m:.4f} sd={sd:.4f} max={mx:.4f} | z={z:+.2f} | >=real={ge}/200 (p={p:.4f})")
        out.append(f"Cov>=4: {r['cov4_real']:.4f}")
        out.append(f"sample: {r['sample']}")
        out.append("")
        if pk > 0.01 or zk < 5.0:
            passed = False
            fail_reasons.append(f"{name} shuf-keys LM z={zk:+.2f}, p={pk:.4f}")
        if ps > 0.01 or zs < 5.0:
            passed = False
            fail_reasons.append(f"{name} shuf-streams LM z={zs:+.2f}, p={ps:.4f}")

    if passed:
        out.append("DECISION: PASS (all subsets satisfy z_lm >= 5.0 and p <= 0.01 against 200 class-preserving shuffled keys and 200 shuffled streams).")
    else:
        out.append("DECISION: FAIL (" + "; ".join(fail_reasons) + ").")
    report = "\n".join(out) + "\n"
    (HERE / "validation_78r.txt").write_text(report, encoding="utf-8")
    print(report)
    if not passed:
        sys.exit(1)


if __name__ == "__main__":
    main()
