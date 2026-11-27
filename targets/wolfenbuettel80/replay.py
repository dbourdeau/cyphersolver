"""Replay only supported values against the marked German reading."""
import csv
from pathlib import Path

HERE = Path(__file__).resolve().parent
DIVIDED = True
POLYPHONY = {}
SOURCES = {"key": "key.tsv", "transcription": "transcription.txt", "reading": "reading.txt"}


def mechanical():
    with (HERE / SOURCES["key"]).open(encoding="utf-8") as stream:
        key = {r["label"]: r["value"] for r in csv.DictReader(stream, delimiter="\t")
               if r["status"] == "supported"}
    words = (HERE / SOURCES["transcription"]).read_text().split()
    # The last word runs across the final line break.
    words[-2:] = ["".join(words[-2:])]
    return [("103v", [[(sign, key.get(sign)) for sign in word] for word in words])]


def reading():
    return {"103v": (HERE / SOURCES["reading"]).read_text(encoding="utf-8")}
