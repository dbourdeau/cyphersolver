# Brief — blind shape transcription, c. 1v + c. 2r (PREREG-O3 §3)

You are a blind transcriber. You transcribe SHAPES only. You never decode.

## Files you may open (and NOTHING else)
- `input/SIGNS.md` — sign names and shape descriptions.
- `input/CONVENTIONS-SHAPES.txt` — shape conventions decided on another page (c. 1r) of the same letter. The row numbers in
  it (L07, L18...) refer to that other page, not to yours. Reuse its names (incl. N1-N8) when a shape matches.
- `input/crops/` — row crops: `1v_L01.jpg` ... `1v_L26.jpg` (c. 1v: L01-L22 main block, L23-L26 lower block) and
  `2r_L01.jpg` ... `2r_L09.jpg` (c. 2r). For each row: full row (red triangle on the left marks the row to transcribe; the row
  centred in the crop — neighbours above/below are partly visible, ignore them) + `_a` (left half, x1.6) + `_b` (right half,
  x1.6; halves overlap by ~300 px, do not count the overlapping signs twice). Overviews with row numbers:
  `1v_overview.jpg`, `2r_overview.jpg`. You may crop/zoom these files further with Python PIL (write any temporary
  file only under your output folder).
Do NOT open any other file or folder of this dossier or elsewhere (no key, no decode, no other transcription, no scans/, no
o2-2311/, no wainut/, no other passe-*/ folder, no HANDOFF). Do not search the web. Do not guess plaintext: no letter values.

## Rules (SIGNS.md)
One token per sign, separated by spaces; raised mark glued to its base (`3o`, `4o`, `12`, `x3`, `mx2`, `4s`); `.` as its own
token; `/` and `(` as written. Unknown shape: next free name N9, N10... (N1-N8 reused when they match the description of
CONVENTIONS-SHAPES), described once at the end. Doubtful: `?` suffix. Struck: `_` suffix.
**Ignore the small letters written above / between the lines in another ink (later glosses)**: do not transcribe them, and do not
use them. They sit in particular above 1v L17, L21, L22 and 2r L01, L06, L07.

## Output
Write one file `<your folder>/transcription_pass<X>.txt`:
```
# header: who/when, method, conventions you added, N-shapes you added (shape only), uncertainties
1v L01: tok tok tok ...
...
1v L26: ...
2r L01: ...
...
2r L09: ...
```
Exactly 35 rows, in this order, prefix exactly `1v L01:` / `2r L01:`. Then reply with: number of rows, number of tokens,
N-shapes added, main doubts. Work carefully sign by sign; check each row twice (count signs on the full row against the halves).
