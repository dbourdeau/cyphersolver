"""Print the provenance of each complete word in the frozen October word ledgers."""
import argparse
import csv
from pathlib import Path
import sys

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--inputs", type=Path, default=Path(__file__).resolve().parent)
base = parser.parse_args().inputs


def values(name):
    with (base / name).open() as f:
        return dict(line.split()[:2] for line in f if line.strip())


initial = values("diez_gloss.tsv")
july_extra = values("july_extensions.tsv")
oct8 = values("oct8_training_values.tsv")
oct14 = values("oct14_training_values.tsv")
july = {**initial, **july_extra}
assert {**july, **oct8} == values("candidate.tsv")
keys = [initial, july, {**july, **oct8}, {**july, **oct8, **oct14}]
assert keys[-1] == values("candidate15.tsv")
stages = ("July 26 entries", "expanded July", "October 8 training", "October 14 hypotheses")
out = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
out.writerow(["day","run","reading","groups","July_26","expanded_July","through_Oct8","through_Oct14",
              "first_complete_stage","October14_hypotheses_used","context"])


def emit(day, run, reading, codes, context):
    end = 3 if day == 15 else 2
    forms = ["".join(k.get(c, "?") for c in codes) for k in keys[:end+1]]
    assert "?" not in forms[-1]
    earliest = next(i for i, form in enumerate(forms) if form == forms[-1])
    predicted = ",".join(c for c in codes if c in oct14) if day == 15 else ""
    out.writerow([day, run, reading, " ".join(codes), *forms,
                  *(["not yet fitted"] if day == 14 else []), stages[earliest], predicted, context])


contexts = {"Laredo":"Clear destination.", "plaza":"Exact group sequence occurs on training sheet.",
            "en":"Within possible cancelled clear parallel.", "tren":"Clear parta otro precedes."}
with (base / "oct14_words.tsv").open() as f:
    for row in csv.DictReader(f, delimiter="\t"):
        if row["status"] == "sure":
            emit(14, row["run"], row["editorial"], row["emissions"].split(), contexts.get(row["editorial"], ""))
runs = [line.split() for line in (base / "oct15.runs").read_text().splitlines()]
with (base / "oct15_words.tsv").open() as f:
    for row in csv.DictReader(f, delimiter="\t"):
        words = row["core_sure_words"].split()
        if words:
            run = int(row["run"])
            parts = [runs[0][:2], runs[0][2:]] if run == 1 else [runs[run-1]]
            assert len(parts) == len(words)
            for word, piece in zip(words, parts):
                note = {"está":"Accent and word division editorial.", "mandé":"Accent/editorial choice of tense.",
                        "destruida":"Echoes October 14.", "relevo":"Follows clear esperar."}.get(word, "")
                emit(15, run, word, piece, note)
