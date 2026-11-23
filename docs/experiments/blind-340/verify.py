"""Run with Python 3 beside C.txt and C.json to replay the submitted solution."""
import hashlib
import json
import string
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMMITMENT = "e5950a9ca86c1b1f7f0d692c6ae04027494c2269978783d0c01d2f4febfa551d"
SYMBOLS = string.ascii_uppercase + string.ascii_lowercase + string.digits + "@"
LETTERS = "ulhieeektdlnltcoytsevnddteaowfasheopartehhneileamishgraeobnftir"


def decode(ciphertext):
    rows = [list(row) for row in ciphertext.splitlines()]
    if len(rows) != 20 or any(len(row) != 17 for row in rows):
        raise ValueError("Expected a 20 by 17 grid")
    rows[13].insert(4, rows[13].pop())
    symbols = []
    for start, height, step in [(0, 10, 1), (10, 8, 2)]:
        for i in range(height * 17):
            symbols.append(rows[start + (-i % height)][i * step % 17])
    symbols.extend(reversed(rows[19]))
    symbols.extend(reversed(rows[18]))
    key = dict(zip(SYMBOLS, LETTERS))
    return "".join(key[s] for s in symbols).upper()


if __name__ == "__main__":
    ciphertext = (HERE / "C.txt").read_bytes()
    recovered = decode(ciphertext.decode("ascii"))
    raw = (HERE / "C.json").read_bytes()
    if hashlib.sha256(raw).hexdigest() != COMMITMENT:
        raise ValueError("Answer file differs from the original commitment")
    answer = json.loads(raw)
    if hashlib.sha256(ciphertext).hexdigest() != answer["ciphertext_sha256"]:
        raise ValueError("Ciphertext differs from the committed input")
    if recovered != answer["normalized"]:
        raise ValueError("Decoded letters differ from the committed answer")
    print(recovered)
    print("340 of 340 letters match the committed answer.")
