"""Replay the R619 direct test and the May 20 sibling-letter key on no. 17."""

from pathlib import Path
import re


HERE = Path(__file__).resolve().parent
# First digit and mark classes attested on p. 1120. The editors query "hogy".
ROWS = {
    ".": dict(zip("13456789", "acdeéfgh")),
    ".~": dict(zip("1234568", "iklmnop")),
    ".ʼ": dict(zip("1234578", "rstuvyz")),
    "_": {"1": "ü", "2": "sz", "3": "[hogy?]"},
}


def value(token):
    match = re.fullmatch(r"(\d)(_?)(\d\d)(\.|\.~|\.ʼ|;)", token)
    first, underline, _, suffix = match.groups()
    return ROWS.get(underline or suffix, {}).get(first, f"[{token}]")


def main():
    text = (HERE / "transcription.txt").read_text(encoding="utf-8")
    passages = "\n".join(line for line in text.splitlines() if not line.startswith("#"))
    key_file = HERE.parent / "bay1706/keys/DOC_R619_D2585_2585.txt"
    numbers = set()
    for line in key_file.read_text(encoding="utf-8-sig").splitlines():
        if re.fullmatch(r"[\d|]+ - .+", line):
            numbers.update(line.split(" - ")[0].split("|"))
    for index, passage in enumerate(passages.strip().split("\n\n"), 1):
        tokens = passage.split()
        direct = sum(re.sub(r"\D", "", token) in numbers for token in tokens)
        print(f"{index}. R619 {direct}/{len(tokens)}")
        print(" ".join(f"{token}={value(token)}" for token in tokens))
        print("".join(map(value, tokens)))


if __name__ == "__main__":
    main()
