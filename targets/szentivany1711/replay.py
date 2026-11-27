"""Adapter for the repository word-level comparison of the four cipher runs."""

from decode import HERE, value

DIVIDED = False
POLYPHONY = {}
SOURCES = {"key": "decode.py", "transcription": "transcription.txt", "reading": "reading.md"}


def mechanical():
    lines = (HERE / SOURCES["transcription"]).read_text(encoding="utf-8").splitlines()
    text = "\n".join(line for line in lines if not line.startswith("#"))
    for index, run in enumerate(text.strip().split("\n\n"), 1):
        units = []
        for token in run.split():
            plain = value(token)
            # The guessed whole word stays outside the independently keyed replay.
            units.append((token, None if plain.startswith("[") else plain))
        yield str(index), [units]


def reading():
    body = (HERE / SOURCES["reading"]).read_text(encoding="utf-8").split("## Reading\n", 1)[1]
    return {str(index): line for index, line in enumerate(body.strip().split("\n\n"), 1)}
