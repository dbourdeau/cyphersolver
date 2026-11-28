"""Search ETCBC DSS 2.0.5 sign features for parallels to 4Q313 fragment 2."""

import argparse
import re
from pathlib import Path


FINALS = str.maketrans("ךםןףץ", "כמנפצ")
PATTERNS = {
    "line 1 preferred, three preceding traces": r"אמושגעו",
    "line 1 paleographic alternatives, all seven traces": r"א[מפ][הקרתונ]ש[גטר]ע[ות]",
    "line 1 left cluster, gimel and either terminal": r"שגע[ות]",
    "line 1 motif, madness noun": r"שגעונ",
    "line 1 comparison, heal them": r"רפאמ",
    "line 2 with proposed aleph and one intervening letter": r"שימ[א-ת]א",
    "line 2 with proposed aleph and an empty gap": r"שימא",
    "line 2 candidate, plene guilty": r"אשימימ",
    "line 2 candidate, defective guilty": r"אשמימ",
}


def feature_rows(path):
    """Read Text-Fabric node records and unvalued edges."""
    with path.open(encoding="utf-8") as file:
        for row in file:
            if not row.strip():
                break
        node = 0
        for row in file:
            fields = row.rstrip("\n").split("\t", 1)
            if len(fields) == 2:
                start, _, end = fields[0].partition("-")
                node = int(end or start)
                for index in range(int(start), node + 1):
                    yield index, fields[1]
            else:
                node += 1
                yield node, fields[0]


def slots(spec):
    for item in spec.split(","):
        start, _, end = item.partition("-")
        yield from range(int(start), int(end or start) + 1)


def scan(root):
    with (root / "otype.tf").open(encoding="utf-8") as file:
        ranges = {kind: (int(node_min), int(node_max or node_min))
                  for node_min, node_max, kind in re.findall(
                      r"^(\d+)(?:-(\d+))?\t(\w+)$", file.read(), re.M)}
    last_sign = ranges["sign"][1]
    line_min, line_max = ranges["line"]

    def feature(name, lower, upper):
        return {node: val for node, val in feature_rows(root / f"{name}.tf")
                if lower <= node <= upper and val}

    glyphs = feature("glyph", 1, last_sign)
    types = feature("type", 1, last_sign)
    reconstructed = feature("rec", 1, last_sign)
    scrolls = feature("scroll", line_min, line_max)
    fragments = feature("fragment", line_min, line_max)
    lines = feature("line", line_min, line_max)
    patterns = {key: re.compile(f"(?=({value}))") for key, value in PATTERNS.items()}
    counts = dict.fromkeys(patterns, 0)
    unrestored = dict.fromkeys(patterns, 0)
    previous_match = None
    pairs = []
    scanned = 0
    for node, spec in feature_rows(root / "oslots.tf"):
        if node > line_max:
            break
        if node not in lines or node not in scrolls:
            continue
        scroll = scrolls[node]
        fragment = fragments[node]
        if scroll.startswith("4Q313"):
            previous_match = None
            continue
        scanned += 1
        letters = []
        restored = []
        for sign in slots(spec):
            kind = types.get(sign)
            glyph = glyphs.get(sign, "")
            if kind == "cons" and re.fullmatch(r"[א-ת]", glyph):
                is_restored = sign in reconstructed
                letters.append(glyph.translate(FINALS))
                restored.append(is_restored)
            elif kind in {"missing", "unc", "punct"}:
                letters.append("|")
                restored.append(False)
        text = "".join(letters)
        label = f"{scroll} {fragment}:{lines[node]}"
        if previous_match and previous_match[0] == (scroll, fragment, node - 1):
            if "שימ" in text:
                pairs.append((previous_match[1], previous_match[2], label))
        anchor = re.search("ש[גטר]ע[ות]", text)
        previous_match = ((scroll, fragment, node), label, anchor[0]) if anchor else None

        for name, pattern in patterns.items():
            for match in pattern.finditer(text):
                counts[name] += 1
                start, end = match.span(1)
                supported = not any(restored[start:end])
                unrestored[name] += supported
                if name.startswith("line 1") or "guilty" in name:
                    status = "unbracketed" if supported else "restored"
                    excerpt = text[max(0, start - 7):end + 7]
                    print(f"{name}\t{label}\t{status}\t{excerpt}")
    print(f"Lines scanned: {scanned}")
    for name in patterns:
        print(f"{name}: {counts[name]} total, {unrestored[name]} unbracketed")
    print(f"Adjacent lines in the same fragment with the broad clusters: {len(pairs)}")
    for first, anchor, second in pairs:
        print(f"\t{first}\t{anchor}\t{second}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("tf_dir", type=Path, help="Path to the ETCBC tf/2.0.5 directory")
    scan(parser.parse_args().tf_dir)
