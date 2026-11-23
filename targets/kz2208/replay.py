"""Replay the 43 group positions against the words or stems in the period copies."""
import csv
from pathlib import Path

from deslide import transform

TARGET = Path(__file__).resolve().parent
DIVIDED = True
POLYPHONY = {}
SOURCES = {"key": "deslide.py and the attested entries in reading.tsv",
           "transcription": "cipher_groups.txt", "reading": "aligned_plaintext.txt"}

# Canonical forms corresponding to the independently attested VB entries.
# The period wording in aligned_plaintext.txt retains the telegram's inflections.
VALUES = {
    "35343": "Chef der Hochseeverbände", "65775": "Unternehmung",
    "37477": "ein", "65873": "Unterseeboot", "52880": "mitgeben",
    "29678": "ansetzen", "29788": "angestrebt", "37823": "Einnahme",
    "39430": "ist zu erwarten", "63324": "Teilnahm", "60728": "Seestreitkräfte",
    "36817": "dortig", "67651": "Verwendung", "32427": "befindlich",
    "70237": "zurück", "19673": "Ostsee", "30077": "Armee",
    "41981": "gebraucht", "30736": "aufgestellt", "51245": "Luftschiff",
    "40282": "feindlich", "46853": "Kanal", "14185": "englisch",
    "28692": "Abwehr",
}


def mechanical():
    """Read observed groups only. A damaged or unattested group has no output."""
    with (TARGET / "reading.tsv").open(encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream, delimiter="\t"))
    observed = (TARGET / "cipher_groups.txt").read_text(encoding="utf-8").split()
    assert len(rows) == len(observed)
    return [(row["index"], [[(group, VALUES.get(transform(group)))]])
            for row, group in zip(rows, observed)]


def reading():
    lines = (TARGET / "aligned_plaintext.txt").read_text(encoding="utf-8").splitlines()
    return dict(line.split("\t", 1) for line in lines)
