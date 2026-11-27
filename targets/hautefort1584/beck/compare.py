"""Run with Python 3.10+ in a checkout containing targets/hautefort1584."""
import csv
from collections import Counter, defaultdict
from hashlib import sha256
import json
from pathlib import Path
import unicodedata

HERE = Path(__file__).resolve().parent
TARGET = HERE.parent


def table(name):
    with (HERE / name).open(encoding="utf-8", newline="") as src:
        return list(csv.DictReader(src, delimiter="\t"))


def read_signs(path, folio=None):
    rows = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith(("f", "L")) and ":" in line:
            tag, signs = line.split(":", 1)
            if tag.startswith("f"):
                leaf, number = tag[1:].split()
            else:
                leaf, number = folio, tag
            rows[leaf, int(number[1:])] = signs.split()
    return rows


def norm(word):
    text = unicodedata.normalize("NFD", word.lower()).translate(str.maketrans("vjy", "uii"))
    return "".join(c for c in text if "a" <= c <= "z")


def replay_baseline():
    key = {r["glyph_label"]: r["fixed_value"] for r in table("key.tsv") if r["fixed_value"] != "?"}
    changes = {(int(r["line"]), int(r["position"])): r for r in table("amendments_207r.tsv")}
    streams, offsets = defaultdict(list), {}
    local = {}
    for r in table("transcription.tsv"):
        folio, line = r["folio"], int(r["line"])
        glyphs = r["baseline_glyphs"].split()
        local[folio, line] = glyphs
        stream = streams[folio]
        offsets[folio, line] = len(stream)
        translated = []
        for index, sign in enumerate(glyphs, 1):
            value = key.get(sign, sign if sign == "[?]" else f"[{sign}]")
            if folio == "207r" and (line, index) in changes:
                entry = changes[line, index]
                assert (sign, value) == (entry["old_label"], entry["old_value"])
                value = entry["new_value"]
            if folio != "207r":
                value = {"hm": "m", "2": "n"}.get(sign, value)
            translated.append(value)
        assert "".join(translated) == r["baseline_literal"]
        stream.extend(translated)
    totals, accepted, cursor = Counter(), Counter(), Counter()
    spans = {}
    for span in table("word_spans.tsv"):
        f = span["folio"]
        line, sign = int(span["start_line"]), int(span["start_sign"])
        start = offsets[f, line] + sign - 1
        stop = offsets[f, int(span["end_line"])] + int(span["end_sign"])
        assert cursor[f] == start < stop
        cursor[f] = stop
        literal = "".join(streams[f][start:stop])
        proposed = span["earlier_reading"]
        if f == "207r":
            totals[f] += 1
            accepted[f] += proposed != "?" and "[" not in literal and norm(literal) == norm(proposed)
        else:
            assert literal == proposed
            totals[f] += stop - start
            accepted[f] += (stop - start) * int(span["editor_accepted"])
            spans[f, line, sign] = span
    assert all(cursor[f] == len(stream) for f, stream in streams.items())
    assert [(accepted[f], totals[f]) for f in ("207r", "207v", "208r")] == [(160,198),(494,749),(546,798)]
    print("207r 160/198 fitted word slots; 207v 494/749 signs; 208r 546/798 signs")
    return local, spans


def checked_intersections(local, spans, upstream, key):
    reviews = table("hook_review.tsv")
    indices = {(r["folio"], int(r["line"]), int(r["sign"])) for r in reviews}
    assert indices == {(f, line, pos) for (f, line), signs in local.items()
                       for pos, g in enumerate(signs, 1) if g == "v"}
    counts = Counter()
    for r in reviews:
        f, line, pos = r["folio"], int(r["line"]), int(r["sign"])
        if r["status"] != "candidate":
            continue
        # The second transcript inserts a divider immediately before the hook
        # on 207r.20 and writes two signs for our 33 earlier on 208r.12.
        theirs = upstream[f, line]
        ix = pos - 1 + int((f, line) in {("207r", 20), ("208r", 12)})
        assert theirs[ix] == "v" and key["v"] == "qui", (f, line, pos)
        counts["matches"] += 1
        if f != "207r":
            s = spans[f, line, pos]
            assert s["earlier_reading"] in ("i", "il")
            counts["previously counted" if s["editor_accepted"] == "1" else "withheld"] += 1
    assert counts == {"matches":14, "withheld":8, "previously counted":2}
    join = upstream["207v", 1][-2:] + upstream["207v", 2][:3]
    assert "".join(key[g] for g in join) == "uenquir"
    assert upstream["207v", 2][1] == "v" and local["207v", 2][1] == "v"
    print("14/14 proposed broad-hook readings have Brice's v; 8 withheld spans and 2 revised spans on 207v/208r")
    print("Counterexample: 207v.2.2 in venir; Brice's v gives uenquir across the break (ue + nquir).")


def compare_codes(upstream, key):
    def decode(folio, line):
        return "".join(key.get(g, g) for g in upstream[folio, line])
    doubles = []
    for (f, line), row in upstream.items():
        if f in ("207r", "208r", "208v", "209r"):
            for i in range(len(row)-1):
                if row[i:i+2] == ["3","3"]:
                    doubles.append((f, line, i+1))
    assert doubles == [("207r",13,13), ("208r",12,24), ("209r",17,8)]
    assert "foispp e".replace(" ","") in decode("207r",13)
    assert "tantppquil" in decode("208r",12)
    assert "carilppfortacraindre" in decode("209r",17)
    assert "dictsieurdesdi" in decode("208v",4)
    assert "dessieursdeglandaige" in decode("208v",11)
    assert "lelcauitai" in decode("208v",3) and "lelcalign" in decode("209r",5)
    assert decode("208r",26).endswith("discoursquevousau")
    assert decode("208v",1).startswith("esentendusdicelui")
    assert decode("208v",25).endswith("eauesc") and decode("209r",1).startswith("ideuant")
    assert upstream["208v",2][12:16] == ["*","9","8","&"]
    assert decode("209r",25).endswith("rendrontpeutestreunpeupl")
    print("Paired 3 test outside our original photos: car il [est] fort a craindre (209r.17)")
    print("17: dict [17] at 208v.4; des [17]s de Glandaige at 208v.11")
    print("208r/208v: que vous au|es entendus d'icelui. 208v/209r: c|ideuant.")
    print("209r.25 transcription stops at 'un peu pl'; closing unchecked.")


def check_first_hand():
    source = read_signs(TARGET / "f158/read1.txt", "158r")
    key = json.loads((TARGET / "key_hand1_v3.json").read_text())
    assert source["158r",13][-4:] == ["15","17","9","8"]
    assert "".join(key[g] for g in source["158r",14][:11]) == "montpensier"
    assert source["158r",18][:7] == ["3","3","3","4","O","q","H"]
    print("158r.13/14: [15][17] de Montpensier. 158r.18: 3 3 + parti (different hand).")


if __name__ == "__main__":
    frozen = TARGET / "key_hand2.json"
    assert sha256(frozen.read_bytes()).hexdigest() == "3d3186f3bc073f9c9cf292ad3451145daaefb359b8e85bc67d5a8356d9d3f275"
    key = json.loads(frozen.read_text())
    upstream = read_signs(TARGET / "f207-209/transcription_fable.txt")
    upstream.update(read_signs(TARGET / "f207v/read_final.txt", "207v"))
    local, spans = replay_baseline()
    checked_intersections(local, spans, upstream, key)
    compare_codes(upstream, key)
    check_first_hand()
