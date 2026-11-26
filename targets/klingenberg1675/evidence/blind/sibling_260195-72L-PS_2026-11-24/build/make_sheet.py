"""make_sheet.py: neutral label sheet for kling72. Forms copied from the 16 Nov 41R sheet (siblings/klingenberg1675/
260195-41R/blind_packet/SHEET.md); key sign names replaced by S01.. in an order shuffled with seed 72 (no value order).
Writes ../packet/SHEET.md and ../sheet_to_key.tsv (outside the packet). No key value is read here."""
import random, os
H = os.path.dirname(os.path.abspath(__file__))
rows = [  # (key sign name as in decode SIGN / upstream transcriptions, form)
 ("#", "large hash sign with TWO bars across (double-barred #); count the bars on every hash-like sign"),
 ("H", "small hash-like sign with ONE bar (H-like); count the bars on every hash-like sign"),
 ("-", "a dash standing as a token on its own between commas"),
 ("A", "plain lambda / caret (^ shape, no extra stroke)"),
 ("K", "lambda / caret with an extra hooked stroke"),
 ("B", "beta / sharp-s-like looped sign"),
 ("C", "bracket '[' with NO middle bar"),
 ("V", "Gamma / '[' sign with a top bar (no middle bar)"),
 ("E", "E-like sign WITH a middle bar"),
 ("D", "d with a cross stroke"),
 ("w", "w-shaped sign"),
 ("d", "plain d-like sign with no cross stroke"),
 ("F", "q-like sign with a STRAIGHT descender and a cross on it"),
 ("Q", "q-like sign whose tail is CROSSED (crossed tail)"),
 ("G", "g-like sign with a curled tail (like a script 9 or g)"),
 ("I", "I-like single stroke standing as a sign"),
 ("J", "']'-like sign (closing bracket)"),
 ("L", "small L-like sign"),
 ("M", "pi / m-like sign with three stems"),
 ("O", "big O (letter-sized circle)"),
 ("o", "small o"),
 ("0", "an O written exactly like the digit zero (use this label, not the digit 0)"),
 ("P", "single plain cross (+)"),
 ("PP", "cross with two bars (double cross, like a dagger with two bars)"),
 ("T", "big T-like sign"),
 ("⊥", "inverted T"),
 ("U", "reversed bracket (like ⊐)"),
 ("X", "plain saltire (large x-shaped cross)"),
 ("x", "small cursive x"),
 ("y", "y-like sign"),
 ("Z", "small 2-like sign"),
]
idx = list(range(len(rows))); random.Random(72).shuffle(idx)
lab = {}
for n, i in enumerate(idx, 1):
    lab[i] = f"S{n:02d}"
open(os.path.join(H, "..", "sheet_to_key.tsv"), "w", encoding="utf-8").write(
    "# sheet label -> key sign name (upstream klingenberg1675 sign names as decode_once.py's SIGN reads them). KEEP OUT OF packet/.\n"
    "label\tkey_sign\n" + "".join(f"{lab[i]}\t{rows[i][0]}\n" for i in sorted(lab, key=lambda i: lab[i])))
tab = "".join(f"| {lab[i]} | {rows[i][1]} |\n" for i in sorted(lab, key=lambda i: lab[i]))
sheet = f"""# Label sheet (names only, no values)

You are writing down what is on the page, not what it means. This sheet gives neutral names (S01, S02 ...) for the
drawn signs. The names are in no particular order and carry no information. Do not try to work out any value.

## What a cipher run looks like

A rough draft in a 17th-century German hand. Clear German alternates with runs of numbers (mostly 2-3 digits) and
drawn signs, separated by commas. Several words are struck out or blotted.

## How to write tokens

- Numbers: write the digits exactly as seen (`78`, `414`, `507`). Do not "correct" a figure.
- Drawn signs: write the label from the table below (S01 ... S{len(rows):02d}), exactly as given.
- Separate tokens with a single space. Keep the writer's order. Do not copy the commas. Ignore row-end hyphens.
- `~` straight after a token = you are unsure of it (e.g. `S07~`, `459~`). `?` alone = unreadable token.
  `?5?` = number with unreadable figures. `BLOT` = a group hidden by an ink blot.
- `"` after a token = two dots (umlaut-like) written over it.
- Struck-out words, numbers and filled blots are deletions: write `[struck]` at their place (with what you can
  see inside the brackets if legible) and carry on.
- Inserts (between lines) with a mark: write them where the mark puts them, as `[insert: ...]`; without a mark,
  put them at the end of the page as `[margin: ...]`.
- Show-through from the other side of the leaf (mirror writing) is not text: skip it.
- A sign not on this sheet: describe it briefly in braces, e.g. `{{small t with crossbar}}`.

## Sign labels (form only)

| label | form |
|---|---|
{tab}
Look-alike sets (check each one under zoom): the hash-like signs (count the bars); the two q-like signs (straight
descender with a cross vs crossed tail); the bracket signs (no bar / top bar / middle bar / reversed); the lambda
signs (plain vs hooked); big O, small o and the O written like a zero; the two x signs (large saltire vs small
cursive). If you cannot tell two labels apart, write the likelier one with `~`.
"""
open(os.path.join(H, "..", "packet", "SHEET.md"), "w", encoding="utf-8").write(sheet)
print("labels", len(rows))
