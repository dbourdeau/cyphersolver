"""Find adjacent equal strings required by the last four Munich signs."""

from itertools import product


def squares(text):
    for start in range(len(text)):
        for width in range(2, (len(text) - start) // 2 + 1):
            middle = start + width
            if text[start:middle] == text[middle:middle + width]:
                yield start, text[start:middle]


if __name__ == "__main__":
    notes = [
        "alocus" + word + "domusdominicus" + divine + "cella"
        for word, divine in product(("ceroficon", "cerosicon"), ("dei", "di"))
    ]
    for note in notes:
        print(note, list(squares(note)))
    for first, second in product(notes, repeat=2):
        print(first, second, list(squares(first + second)))
