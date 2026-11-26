"""Decode the sign transcription of doc. 192 with key.tsv and 192-repairs.tsv.

    python3 decode.py --raw      # unedited output of the key (192-literal.txt, after its two header lines)
    python3 decode.py            # the same with the declared repairs of 192-repairs.tsv applied
    python3 decode.py --tokens   # one token per row: location, sign, value, status

Status per token: key (value from the key as transcribed), alt (a {a/b} sign, first alternative used),
repair (read differently from the transcription, see 192-repairs.tsv), open (no value), del (struck).
"""
import csv
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def load_key(path=HERE / "key.tsv"):
    key = {"vowel": {}, "base": {}, "bare": {}, "word": {}, "code": {}, "number": {}, "open": {}}
    for line in path.read_text().splitlines():
        if line and not line.startswith("#"):
            kind, sign, value, *_ = line.split("\t")
            key[kind][sign] = value
    return key


def load_rows(name):
    rows = []
    for line in (HERE / name).read_text().splitlines():
        if line and not line.startswith("#"):
            label, *tokens = line.split()
            rows.append((label, tokens))
    return rows


def load_repairs(path=HERE / "192-repairs.tsv"):
    with path.open() as f:
        return {(r["line"], int(r["index"])): r for r in csv.DictReader((l for l in f if not l.startswith("#")), delimiter="\t")}


def value(token, key):
    """Value of one unambiguous token, or None when the key has none."""
    if token.startswith(".") and token.endswith("."):
        return "#" + token.strip(".") if token.strip(".") in key["code"] else None
    if token.startswith("="):
        return token if token in key["number"] else None
    if token in key["code"] and token.isdigit() and len(token) > 1:
        return "#" + token
    if token in key["number"] and token.isdigit() and len(token) > 1:
        return "=" + token
    if token in key["open"]:
        return None
    if token in key["word"]:
        return key["word"][token].replace(" ", "")
    if "^" in token:
        base, sup = token.split("^", 1)
        if base in key["base"] and sup in key["vowel"]:
            return key["base"][base] + key["vowel"][sup]
        return None
    return key["bare"].get(token)


def decode_row(label, tokens, key, repairs):
    out = []
    for i, token in enumerate(tokens, 1):
        status, sign = "key", token
        if (label, i) in repairs:
            rep = repairs[(label, i)]
            if rep["as_transcribed"] != token:
                raise ValueError(f"repair at {label}:{i} expects {rep['as_transcribed']!r}, transcription has {token!r}")
            out.append((token, rep["read_as"], "repair"))
            continue
        if token == "[del]":
            out.append((token, "", "del"))
            continue
        if token.startswith("{"):
            inner, _, suffix = token[1:].partition("}")
            sign, status = inner.split("/")[0] + suffix, "alt"
            if sign == "[del]":
                out.append((token, "", "alt"))
                continue
        v = value(sign, key)
        out.append((token, "?" if v is None else v, "open" if v is None else status))
    return out


def decode_all():
    key, repairs = load_key(), load_repairs()
    rows = load_rows("192-transcription.txt")
    used = set()
    result = []
    for label, tokens in rows:
        dec = decode_row(label, tokens, key, repairs)
        used |= {(label, i) for i in range(1, len(tokens) + 1) if (label, i) in repairs}
        result.append((label, dec))
    if used != set(repairs):
        raise ValueError(f"unused repairs: {sorted(set(repairs) - used)}")
    return result


def decode_raw():
    key = load_key()
    return [(label, decode_row(label, tokens, key, {})) for label, tokens in load_rows("192-transcription.txt")]


if __name__ == "__main__":
    for label, dec in (decode_raw() if "--raw" in sys.argv else decode_all()):
        if "--tokens" in sys.argv:
            for i, (token, v, status) in enumerate(dec, 1):
                print(f"{label}:{i}", token, v, status, sep="\t")
        else:
            print(label, " ".join(v for _, v, _ in dec if v))
