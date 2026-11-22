"""Check consecutive glyph rows against the consonants of Psalm 45:2–3."""

from itertools import accumulate, product

from test_alphabet import B1, B2, FOLD


HEBREW = ("רחש לבי דבר טוב {say} אני מעשי למלך לשוני עט {scribe} מהיר "
          "יפיפית מבני אדם הוצק חן בשפתותיך על כן ברכך אלהים לעולם")
TARGUM = ("בעי לבי ממלל טב אימר אני עובדי למלכא ממלל לישני מוחי היך קולמוס ספרא רגיל "
          "שופרך מלכא משיחא עדיף מבני נשא אתיהיב רוח נבואה בספותך מטול כן ברכנך יי לעלמא")


def scan(text):
    words = text.translate(FOLD).split()
    letters = ''.join(words)
    boundaries = {0, *accumulate(map(len, words))}
    all_windows, whole_words = [], []
    for direction, first in product((1, -1), (B1, B1[1:])):
        signs = first[::direction] + B2[::direction]
        for start in range(len(letters) - len(signs) + 1):
            end = start + len(signs)
            key = {}
            conflicts = 0
            for sign, letter in zip(signs, letters[start:end], strict=True):
                # Each repeated sign occurs exactly twice in this transcription.
                conflicts += key.setdefault(sign, letter) != letter
            all_windows.append(conflicts)
            if start in boundaries and end in boundaries:
                whole_words.append(conflicts)
    return len(all_windows), min(all_windows), min(whole_words)


if __name__ == "__main__":
    print("text | windows | minimum repeated-sign conflicts | minimum with whole words")
    for say, scribe in product(('אמר', 'אומר'), ('ספר', 'סופר')):
        print(say, scribe, *scan(HEBREW.format(say=say, scribe=scribe)))
    print("Targum", *scan(TARGUM))
