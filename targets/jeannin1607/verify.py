"""Verify the Jeannin cipher passages and comparison samples with Python 3."""

import argparse
from pathlib import Path


# Used entries from George Lasry's System A chart. Shape names match
# TRANSCRIPTION.txt. The form 'ba' is normalized to the chart's r.
# The chart's u/v is represented as u at sign level.
KEY = {
    "u4": "si",
    "dd": "t",
    "Xlow": "o",
    "U3": "s",
    "longS": "t",
    "x^": "que",
    "84^": "nous",
    "fCurl": "c",
    "eps": "a",
    "U2": "u",
    "ba": "r",
    "96^": "on",
    "eq": "s",
    "56^": "leur",
    "fStraight": "se",
    "ro": "r",
    "94^": "ont",
    "c^": "par",
    "cross": "i",
    "no": "z",
    "hook^": "pour",
    "54^": "le",
    "dots3": "e",
    "zLoop": "n",
    "tallLoop": "h",
    "hook": "g",
    "uf": "e",
    "69^": "mais",
    "da": "et",
    "oDash": "y",
    "ff": "ent",
    "rComma": "de",
    "rr": "en",
    "aComma": "car",
    "95^": "ou",
    "74..": "avec",
    "23^": "guerre",
    "hCurl": "re",
    "oval": "a",
    "53^": "la",
    "dots4": "l",
    "51^": "je",
    "nn": "vous",
    "qStem": "p",
    "pComma": "con",
}

ATTESTED = {
    "3^": "quilz",
    "50^": "jay",
    "97^": "occasion",
    # Semantic label. The interlinear renders this group as either
    # le Roy d'Espagne or Espagnolz, depending on the occurrence.
    "11..": "<ESPAGNE>",
    "15..": "roydangleterre",
    "20..": "archiducz",
}
PROPOSED = {"90^": "nauire"}
TARGET = ("116v.4-tail", "116v.5", "116v.6")
FOLLOWUP = {
    "87r.5-tail": "quilznayentoccasiondesenca",
    "87r.6-head": "cher",
    "112v.sample": "quilzont",
    "113v.sample": "carjaysceu",
    "114v.sample": "quejay",
    "115v.sample": "occasion",
    "116r.sample": "ontoccasion",
    "116v.3-mid": "quilzsont",
    "88r.spain": "<ESPAGNE>pour",
    "112v.england": "ouavecleroydangleterre",
    "112v.archdukes": "quearchiduczont",
    "112v.spanish": "les<ESPAGNE>ou",
    "113v.england": "sileroydangleterre",
    "115v.spanish": "avecles<ESPAGNE>ou",
    "115v.archdukes": "lesarchiducz",
    "116r.spain": "guerreavec<ESPAGNE>",
}
CONTROLS = {
    "86r.11-tail": "maissinous",
    "86r.17-head": "etleurspartisans",
    "116v.3-head": "secourir",
    "h16june.91r.1": "deleursnauires",
    "113r.penultimate-tail": "anneesenlaque",
    "113r.last": "llejevousrepeterayquejesuyscontent",
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--published-only",
        action="store_true",
        help="Use Lasry's public chart only and show the added groups unresolved.",
    )
    args = parser.parse_args()
    source = Path(__file__).with_name("TRANSCRIPTION.txt")
    records = {}
    for line in source.read_text(encoding="utf-8").splitlines():
        if " | " in line:
            reference, tokens = line.split(" | ", 1)
            if reference in records:
                raise ValueError(f"Duplicate reference {reference}")
            records[reference] = tokens.split()

    key = KEY if args.published_only else KEY | ATTESTED | PROPOSED
    expected = dict(CONTROLS)
    expected.update({
        "116v.4-tail": "si",
        "116v.5": (
            "tostquenousscauronsqueleurs"
            + ("[90^]" if args.published_only else "nauire")
            + "sser"
        ),
        "116v.6": "ontpartizpourlesuenircharger",
    })
    expected.update(FOLLOWUP)
    if args.published_only:
        for reference, reading in FOLLOWUP.items():
            for token, expansion in ATTESTED.items():
                reading = reading.replace(expansion, f"[{token}]")
            expected[reference] = reading

    if records.keys() != expected.keys():
        raise ValueError("Unexpected or missing transcription rows.")

    for reference, tokens in records.items():
        values = []
        for token in tokens:
            if token == "loopCross":
                if not values:
                    raise ValueError(f"{reference}: repetition has no preceding sign")
                values.append(values[-1])
            else:
                values.append(key.get(token, f"[{token}]"))
        decoded = "".join(values)
        if decoded != expected[reference]:
            raise ValueError(f"{reference}: expected {expected[reference]!r}, got {decoded!r}")
        print(f"{reference} ({len(tokens)} signs)")
        print(" ".join(f"{token}={value}" for token, value in zip(tokens, values)))
        print(decoded)
        print()

    signs = [token for reference in TARGET for token in records[reference]]
    inherited = sum(token in KEY for token in signs)
    print(f"Dieppe target: {len(signs)} signs, {inherited} using published values.")
    print(f"Proposed group occurrences: {sum(token in PROPOSED for token in signs)}.")
    print("All expected line outputs matched.")


if __name__ == "__main__":
    main()
