"""Verify the recorded eligibility, literal-word matches and two permutation runs."""
import csv
import random
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
WAINUT = HERE.parent / "wainut"
MAY = HERE.parent / "mcbratney_27may1549"


def rows(path):
    with path.open(encoding="utf-8", newline="") as stream:
        return list(csv.reader((line for line in stream if line.strip() and not line.startswith("#")), delimiter="\t"))


def words(text):
    text = "".join(c for c in unicodedata.normalize("NFD", text.casefold()) if not unicodedata.combining(c))
    text = text.replace("embaxador", "embajador").translate(str.maketrans("vj", "ui"))
    return re.findall(r"[a-z]+", text)


def verify_controls(name, table, slots, seed):
    def score(mapping):
        return sum(
            label in mapping and f" {mapping[label]} " in f" {text} "
            for label, text in slots
        )

    observed = score(table)
    rng = random.Random(seed)
    scores = []
    for index in range(1, 1001):
        alternatives = list(table.values())
        rng.shuffle(alternatives)
        scores.append([str(index), str(score(dict(zip(table, alternatives))))])
    if rows(HERE / (name + "_controls.tsv"))[1:] != scores:
        raise ValueError(f"{name} control scores differ")
    counts = Counter(int(row[1]) for row in scores)
    return [name, str(len(table)), str(len(slots)), str(observed), str(max(counts)),
            str(counts[observed]), str(sum(n for v, n in counts.items() if v > observed))]


def october():
    explicit = {"dide","quod","gien","em","gaces","mus","pollo","vela","inta","nep"}
    table = {label.lower(): " ".join(words(value)) for label,value,_ in rows(WAINUT / "key.tsv")
             if label.lower() in explicit}
    labels = Counter()
    for row in (WAINUT / "transcription_ch1549_0930_1120_blind.txt").read_text().splitlines():
        if re.match(r"^[KN]-\d+", row):
            labels.update(t for t in row.split()[1:] if re.fullmatch(r"\{[A-Za-z]+\}[_?]*", t))
    assert labels == {"{mo}":31, "{no}":13, "{no}_":1, "{mos}":1}
    assert not (set(table) & {token.strip("{}_?").lower() for token in labels})
    return verify_controls("october", table, [], 15521006)


def may():
    raw = defaultdict(list)
    for record in rows(HERE.parents[1] / "figueroa1534/validation/K4.tsv"):
        if len(record) != 3:
            continue
        label, value, source = record
        if source == "AGS" and re.fullmatch(r"\{[a-z]+\}", label):
            raw[label[1:-1]].append(value)
    table = {label: " ".join(words(values[0])) for label, values in raw.items()
             if len(values)==1 and values[0]!="NUL" and not any(mark in values[0] for mark in "[]/?«")}
    lines = (MAY / "27may1549_decipherment_12r.txt").read_text().splitlines()
    text = " ".join(line.split(" ",1)[1] for line in lines if line and not line.startswith("#"))
    first, rest = text.split("es muy bien tener",1)
    middle, last = rest.split("q dezis",1)[1].split("En lo de mas tocante",1)
    blocks = {"B1":first.split("alos ",1)[1], "B2":middle.replace(", para ", " ",1), "B3":last}
    blocks = {label:" ".join(words(s)) for label,s in blocks.items()}
    positions = [(b, ln, label[1:-1]) for b,ln,label,*_ in rows(MAY / "27may1549_ledger.tsv")
                 if label.startswith("{")]
    assert len(positions)==8 and len({label for _,_,label in positions})==7
    assert [(ln,label) for _,ln,label in positions if label=="ne"] == [("4","ne"),("15","ne")]
    slots = [(label,blocks[b]) for b,_,label in positions]
    assert [label for label,s in slots if label in table and f" {table[label]} " in f" {s} "] == ["em","nec"]
    return verify_controls("may", table, slots, 15490527)


if __name__ == "__main__":
    actual = [october(), may()]
    if rows(HERE / "scores.tsv")[1:] != actual:
        raise ValueError(f"Observed scores differ: {actual}")
    print("October: 46 braced tokens, zero eligible code types. All 1,000 controls tie at zero.")
    print("May: seven types in eight slots; two literal matches, six control ties, no higher score.")
    print("Both registered tests missed. All 2,000 stored control scores match.")
