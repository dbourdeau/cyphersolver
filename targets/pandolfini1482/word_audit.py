#!/usr/bin/env python3
"""Programmatic cipher-words-only extent and polyphonic sure-word audit for Pierfilippo Pandolfini -> Lorenzo de' Medici
(ASFi MAP XXXVIII doc. 418 = Cat. 2574; ASFi MAP LIII doc. 13 = Cat. 2559).

Computes two complementary measures and writes sure_words.tsv:
1. Unambiguous sure cipher words ("Only sure words count", cf. targets/edmondes1594/scripts/sure_words.py):
   A plain cipher word is SURE only when it aligns verbatim with the Grade-1 mechanical decryption (key_pandolfini1482.tsv)
   AND at most one expansion of its polyphonic slots (II=a/o, 9=e/l, sig=t/d, pi=t/b, d=c/g) is an attested Italian word
   in lang/lexicons/it.json.gz (count >= 10, folding u/v and j/i). Plain words where >=2 expansions form attested Italian
   words (e.g. la/lo, a/o, cosa/casa, questo/questa, et/ed) rely on sense and are classed as "key, by sense" (probable).
   Unbracketed orthographic/abbreviated departures (#2574 L25 qelo, L26 qo, L30 sea) are classed as "departure".
2. Explicit-hole share (mirroring research/reading_audit/v10_relabel.py with clear_markup=⟨⟩ on #2574).
"""
from __future__ import annotations

import collections
import csv
import gzip
import itertools
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
KEY_PATH = HERE / "key_pandolfini1482.tsv"
OUT_TSV = HERE / "sure_words.tsv"

OPEN_NOM_HOLES = {"{oo?}", "{B?}", "{invT?}", "{Hcr?}", "[...]"}
OPEN_LAT_HOLES = {"{?ocusa}", "{?grandis}", "{?grandes}"}
OPEN_STREAM = {"B", "invT", "H_cr", "M", "inf"}
ACCENTS = str.maketrans("àáèéìíòóùú", "aaeeiioouu")
ORTHO_DEPARTURES = {"quelo": ("qelo", "qo"), "sia": ("sea",)}
LEX_MIN_FREQ = 10


def _find_repo() -> pathlib.Path | None:
    cur = HERE
    for p in [cur, *cur.parents]:
        if (p / "lang" / "lexicons" / "it.json.gz").is_file():
            return p
        alt = p / "cyphersolver_repo"
        if (alt / "lang" / "lexicons" / "it.json.gz").is_file():
            return alt
    return None


def norm_it(w: str) -> str:
    return w.lower().translate(ACCENTS).replace("v", "u").replace("j", "i")


def load_italian_lexicon() -> set[str]:
    repo = _find_repo()
    if repo is None:
        raise FileNotFoundError("Could not locate lang/lexicons/it.json.gz in repository parents")
    raw = json.loads(gzip.open(repo / "lang" / "lexicons" / "it.json.gz", "rt", encoding="utf-8").read())
    out = set()
    for w, cnt in raw.items():
        if cnt >= LEX_MIN_FREQ and (len(w) > 1 or w in ("a", "e", "i", "o")):
            nw = norm_it(w)
            out.add(nw)
            out.add(re.sub(r"([bcdfglmnprstz])\1", r"\1", nw))
    return out


def load_key() -> dict[str, tuple[str, str, str]]:
    out = {}
    with KEY_PATH.open(encoding="utf-8") as fh:
        for row in csv.DictReader((r for r in fh if not r.startswith("#")), delimiter="\t"):
            tok = row["token"].strip()
            if " " not in tok:
                out[tok] = (row["kind"].strip(), row["value_m1"].strip(), row["value_poly"].strip())
    return out


def parse_cipher_segments(in_name: str, key: dict[str, tuple[str, str, str]]) -> list[list[tuple[str, int, str, tuple[str, ...]]]]:
    """Split emitted letter slots across inline <<...>> clear anchors."""
    segs: list[list[tuple[str, int, str, tuple[str, ...]]]] = []
    cur = None
    for raw in (HERE / in_name).read_text(encoding="utf-8").splitlines():
        m = re.match(r"^(L\d{2})\t(.*)$", raw)
        if not m:
            continue
        lid, body = m.groups()
        tok_idx = 0
        for seg in re.split(r"(<<.*?>>)", body):
            seg = seg.strip()
            if not seg:
                continue
            if seg.startswith("<<") and seg.endswith(">>"):
                cur = None
                continue
            if cur is None:
                cur = []
                segs.append(cur)
            toks = seg.split()
            i = 0
            while i < len(toks):
                tok_idx += 1
                if i + 1 < len(toks) and (toks[i], toks[i + 1]) in {("o", "o"), ("V", "t"), ("V", "3")}:
                    tok_idx += 1
                    i += 2
                    continue
                t = toks[i]
                if t.startswith("LAT_") or t in OPEN_STREAM:
                    i += 1
                    continue
                if t in key:
                    kind, vm, vp = key[t]
                    if t in ("tf_lig", "Rx") or kind == "null" or vp == "NULL":
                        i += 1
                        continue
                    if kind == "polyphonic" and "/" in vp:
                        pts = tuple(p.strip() for p in vp.split("/") if p.strip())
                        cur.append((lid, tok_idx, t, pts))
                    elif t == "V":
                        cur.append((lid, tok_idx, t, (vp.split("/")[0].strip(),)))
                    elif t == "H":
                        cur.append((lid, tok_idx, t, (vp,)))
                    elif t == "D":
                        pts = tuple(p.strip() for p in vp.split("/") if p.strip())
                        cur.append((lid, tok_idx, t, pts))
                    elif vm not in ("NULL", "?"):
                        cur.append((lid, tok_idx, t, (vm,)))
                i += 1
    return segs


def extract_reading_body(text: str) -> str:
    m = re.search(r"^## Reading[^\n]*\n(.*?)(?=^## |\Z)", text, re.S | re.M | re.I)
    body = m.group(1) if m else text
    return "\n".join(l for l in body.splitlines() if not l.lstrip().startswith("#"))


def classify_hole(tok: str) -> str:
    if tok in OPEN_NOM_HOLES:
        return "open_nomenclator"
    if tok in OPEN_LAT_HOLES:
        return "open_latin_cover"
    if tok.startswith("[?"):
        return "contextual_or_uncertain"
    return "grade2_or_scribal_slip"


def audit_document(doc_id: str, reading_fn: str, transcript_fn: str, strip_clear: bool, key: dict, it_lex: set[str]):
    raw_text = (HERE / reading_fn).read_text(encoding="utf-8")
    body = extract_reading_body(raw_text)
    r_parts = [p.strip() for p in (re.split(r"⟨[^⟩]*⟩", body) if strip_clear else [body]) if p.strip()]
    c_segs = parse_cipher_segments(transcript_fn, key)
    if len(c_segs) != len(r_parts):
        raise AssertionError(f"Segment count mismatch in {doc_id}: {len(c_segs)} cipher vs {len(r_parts)} reading")

    rows = []
    counts = collections.Counter()
    hole_cats = collections.Counter()

    for seg_idx, (slots, rpart) in enumerate(zip(c_segs, r_parts), 1):
        tok_rx = re.compile(r"\[[^\]]+\]|\{[^}]*\?[^}]*\}|[^\W\d_]+")
        toks = tok_rx.findall(rpart)
        pos = 0
        for t in toks:
            if t.startswith("[") or t.startswith("{"):
                counts["hole"] += 1
                hc = classify_hole(t)
                hole_cats[hc] += 1
                rows.append((doc_id, f"S{seg_idx:02d}", t, "hole", hc, ""))
                if t.startswith("[") and t != "[...]":
                    clean_h = re.sub(r"[^a-zA-Zàáèéìíòóùú]", "", t)
                    pos = min(len(slots), pos + max(0, len(clean_h) - 2))
                continue

            w = norm_it(t)
            found = None
            for start in range(max(0, pos - 5), min(len(slots), pos + 25)):
                if start + len(w) <= len(slots) and all(w[k] in slots[start + k][3] for k in range(len(w))):
                    found = (start, start + len(w), "exact")
                    break
            if not found and w in ORTHO_DEPARTURES:
                for alt in ORTHO_DEPARTURES[w]:
                    for start in range(max(0, pos - 5), min(len(slots), pos + 25)):
                        if start + len(alt) <= len(slots) and all(alt[k] in slots[start + k][3] for k in range(len(alt))):
                            found = (start, start + len(alt), f"departure:{alt}")
                            break
                    if found:
                        break
            if not found:
                raise AssertionError(f"Could not align plain word {t!r} in {doc_id} segment {seg_idx}")

            pos = found[1]
            sl = slots[found[0] : found[1]]
            coord_str = " ".join(f"{lid}:{tidx}:{sym}={'/'.join(opts)}" for lid, tidx, sym, opts in sl)
            if found[2] != "exact":
                counts["departure"] += 1
                rows.append((doc_id, sl[0][0], t, "departure", found[2], coord_str))
            elif not any(len(x[3]) > 1 for x in sl):
                counts["sure_mono"] += 1
                rows.append((doc_id, sl[0][0], t, "sure", "monophonic", coord_str))
            else:
                exps = sorted({"".join(p) for p in itertools.product(*[x[3] for x in sl])})
                valid = [e for e in exps if e in it_lex]
                if len(valid) >= 2:
                    counts["by_sense"] += 1
                    rows.append((doc_id, sl[0][0], t, "key, by sense", "/".join(valid), coord_str))
                else:
                    counts["sure_poly_unique"] += 1
                    rows.append((doc_id, sl[0][0], t, "sure", "polyphonic_unique", coord_str))

    sure = counts["sure_mono"] + counts["sure_poly_unique"]
    plain_v10 = sure + counts["by_sense"] + counts["departure"]
    tot = plain_v10 + counts["hole"]
    return {
        "doc": doc_id,
        "sure": sure,
        "sure_mono": counts["sure_mono"],
        "sure_poly_unique": counts["sure_poly_unique"],
        "by_sense": counts["by_sense"],
        "departure": counts["departure"],
        "holes": counts["hole"],
        "plain_v10": plain_v10,
        "tot": tot,
        "sure_share": sure / max(1, tot),
        "v10_share": plain_v10 / max(1, tot),
        "hole_cats": hole_cats,
        "rows": rows,
    }


def main() -> None:
    key = load_key()
    it_lex = load_italian_lexicon()
    r2574 = audit_document("2574", "reading_2574.md", "transcript_2574.txt", True, key, it_lex)
    r2559 = audit_document("2559", "reading_2559.md", "transcript_2559.txt", False, key, it_lex)

    all_rows = r2574["rows"] + r2559["rows"]
    tot_sure = r2574["sure"] + r2559["sure"]
    tot_sense = r2574["by_sense"] + r2559["by_sense"]
    tot_dep = r2574["departure"] + r2559["departure"]
    tot_holes = r2574["holes"] + r2559["holes"]
    tot_words = r2574["tot"] + r2559["tot"]
    tot_v10 = r2574["plain_v10"] + r2559["plain_v10"]

    header = [
        "# Written by word_audit.py; rule: 'Only sure words count' (cf. targets/edmondes1594/scripts/sure_words.tsv).",
        f"# Lexicon filter: lang/lexicons/it.json.gz entries with count >= {LEX_MIN_FREQ} (u/v and j/i folded).",
        f"# Cat. 2574 ({r2574['tot']} cipher words): sure {r2574['sure']}/{r2574['tot']} ({r2574['sure_share']:.3f}) "
        f"[monophonic {r2574['sure_mono']}, unique polyphonic {r2574['sure_poly_unique']}]; "
        f"key, by sense {r2574['by_sense']}; unbracketed departures {r2574['departure']}; explicit holes {r2574['holes']} "
        f"(v10 plain-word share {r2574['plain_v10']}/{r2574['tot']} = {r2574['v10_share']:.3f}).",
        f"# Cat. 2559 ({r2559['tot']} cipher words): sure {r2559['sure']}/{r2559['tot']} ({r2559['sure_share']:.3f}) "
        f"[monophonic {r2559['sure_mono']}, unique polyphonic {r2559['sure_poly_unique']}]; "
        f"key, by sense {r2559['by_sense']}; unbracketed departures {r2559['departure']}; explicit holes {r2559['holes']} "
        f"(v10 plain-word share {r2559['plain_v10']}/{r2559['tot']} = {r2559['v10_share']:.3f}).",
        f"# Combined ({tot_words} cipher words): sure {tot_sure}/{tot_words} ({tot_sure/tot_words:.3f}); "
        f"key, by sense {tot_sense}; departures {tot_dep}; explicit holes {tot_holes} "
        f"(v10 plain-word share {tot_v10}/{tot_words} = {tot_v10/tot_words:.3f}).",
        "doc\tsegment_or_line\tword\tstatus\tdetail\tcipher_slots",
    ]
    with OUT_TSV.open("w", encoding="utf-8") as fh:
        fh.write("\n".join(header) + "\n")
        for r in all_rows:
            fh.write("\t".join(r) + "\n")

    for r in (r2574, r2559):
        print(f"=== Cat. {r['doc']} ===")
        print(
            f"  Unambiguous sure : {r['sure']}/{r['tot']} -> read_share = {r['sure_share']:.3f} ({100*r['sure_share']:.1f}%) "
            f"[mono={r['sure_mono']}, poly_unique={r['sure_poly_unique']}]"
        )
        print(f"  Polyphonic sense : {r['by_sense']} ('key, by sense'); unbracketed departures: {r['departure']}")
        print(f"  v10 plain share  : {r['plain_v10']}/{r['tot']} -> {r['v10_share']:.3f} ({r['holes']} explicit holes)")
        for k in ("open_nomenclator", "open_latin_cover", "contextual_or_uncertain", "grade2_or_scribal_slip"):
            print(f"    - {k:24s}: {r['hole_cats'][k]}")
    print(
        f"=== Combined ===\n  Unambiguous sure : {tot_sure}/{tot_words} = {tot_sure/tot_words:.3f} "
        f"(key, by sense={tot_sense}, departures={tot_dep}, holes={tot_holes}; v10 plain={tot_v10}/{tot_words} = {tot_v10/tot_words:.3f})"
    )


if __name__ == "__main__":
    main()
