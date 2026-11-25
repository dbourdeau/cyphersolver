# Brief — blind shape transcription, letter of 12 Mar 1548, portion P of PREREG-O4 (§2)

You are a blind transcriber. You transcribe SHAPES only. You never decode.

## Files you may open (and NOTHING else)
- `input/SIGNS.md` — sign names and shape descriptions (WAINUT).
- `input/SHAPES-KEY-NAMES.md` — shape descriptions of further names (WAINUT), shapes only.
- `input/crops/` — row crops of the cipher rows of portion P: `<page>_L01.jpg` ... (page = 5r, 5v, 6r; plus, only if PREREG-O4 §2 extends the portion, the next page in order), each with a full row
  (red triangle on the left marks the row; neighbours partly visible, ignore them) + `_a` (left half, x1.6) + `_b` (right half,
  x1.6; halves overlap, do not count the overlapping signs twice), and `<page>_overview.jpg` with row numbers. You may crop /
  zoom these files further with Python PIL (temporary files only under your output folder).
Do NOT open any other file or folder (no key, no decode, no other transcription, no scans/, no o2-2311/, o3-2511/, wainut/,
no other passe-*/ folder, no HANDOFF, no cyphersolver clone). Do not search the web. Do not guess plaintext: no letter values.

## Naming rules
- One token per sign, separated by spaces; raised mark glued to its base (`3o`, `4o`, `12`, `x3`, `mx2`, `4s`, `N7o`);
  `.` as its own token; `/` and `(` as written.
- Use a name of SIGNS.md or SHAPES-KEY-NAMES.md only when the shape matches its description.
- **Any other shape: YOUR OWN name `t1`, `t2`, `t3`... — never `N1`, `N2`... (the `N` names belong to the reference list).**
  Describe each `t` shape once at the end of your file (shape only). This replaces the line of SIGNS.md that says
  "Unknown shape: `N1`, `N2`, ...".
- Doubtful: `?` suffix (`4o?`). Struck / cancelled: `_` suffix. A sign you cannot make out at all: `t?` (one token).
- Ignore the small letters written above / between the lines in another ink (later glosses), and any clear (plain-language)
  text: they are cropped out where possible; if a piece is visible, do not transcribe it and do not use it.

## Output
One file `<your folder>/transcription_pass<X>.txt`:
```
# header: who/when, method, t-shapes you added (shape only), uncertainties
5r L01: tok tok tok ...
...
```
Exactly the rows of the crops, in page order, prefix exactly `5r L01:` etc. Then reply with: number of rows, number of
tokens, t-shapes added, main doubts. Work sign by sign; check each row twice (count signs on the full row against the halves).
