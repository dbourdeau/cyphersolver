# marignano1546: independent decoder and a split of the two-valued sign names on the image (Brice Dudout, Claude Opus 5.5, 14 Nov 2026)

## Decoder
`verify_dudout_20261114.py targets/marignano1546` reads only `key.tsv`, `transcription_c13r.txt` and
`reading_marked_c13r.txt` (not `scripts/decode.py` or `scripts/check_marks.py`). 239 sign units on M01-M10; every line
aligns unit for unit with the marked reading. 238 of 239 (99.6%) give a letter that is a key value of the sign name.
The one exception is the marked *pu{b}lica* (M09, `o?`). Same result as `check_marks.py`.

## Image check
Images: Estense IIIF, canvas 1 (c. 13r), full-size tiles of the cipher block (CC BY-NC-SA, not stored here). The
open point in NOTES ("merged shapes ... not split on the image") was checked sign by sign on crops. Six of the seven
two-valued names are two different shapes on the page. Each shape has one value:

| name | value | shape on c. 13r | where |
|---|---|---|---|
| `+` | g | plain cross, horizontal bar | guerra (M01), grando (M05), già (M08) |
| `+` | h | open "4": the left arm slants up to the stem | ho (M04) |
| `g` | s | g with a closed lower loop | provisione (M02) |
| `g` | q | q-like bowl with a long straight descender | quanto (M03), quale (M08) |
| `o` | s | small round o joined after `d` / `dd` | cossa (M01), posso (M03), professione (M07) |
| `o` | m | tall upright dark oval, like a zero | primo (M06), me (M09) |
| `N` | f | N with a small loop at its top right | fa (M07) |
| `N` | c | N led in by a loop at its top left | facia (M09) |
| `f` | r | tall long-s with crossbar, ascender and descender | guerra (M01) |
| `f` | t | open bowl at x-height into a descender hooked left | actende (M02), auctore (M10) |
| `e` | e | epsilon | luterani, per, ale, et, ne, noscerà, e (7) |
| `e` | i | round Latin e | provisione (M02), li (M03) |

`q` (t in luterani, f in professione): both are a bowl with a descender. In luterani the tail sweeps down and to the
left; in professione it is straight. Possibly two signs; not settled here.

The `f` of actende and auctore is the same shape in both places. It has a bowl that the null sigma `s` (ale,
provisione, li) does not have. So the open question in NOTES ("`f` or sigma `s`") looks like neither: a third sign
for t.

### One reading point
`tenir` (M08, `D Z X e a`): the fourth sign is the **epsilon**, which is *e* in all seven other places. The round e
is the *i* sign. The signs give **tener**; the reading has *tenir* from c. 14r. *tener* is a normal form, and the
cipher keeps other spellings of its own (*grando*, *auctore*). We suggest reading *tener* (or marking the i as
supplied) and noting c. 14r's *tenir*. This does not change the sense or the count.

Also: in cossa, posso and professione the double s **is** written (`d o`, `dd o`), unlike the other double letters.
`d o` / `dd o` may be one sign group for *ss*, like `Lo` and `1o` for *d*.

## Read bar (README)
`research/reading_audit/v10_relabel.measure` on `reading_c13r.md` gives **0.977** (341 words), against `read_share` 1.0
recorded. The words counted include the notes below the reading. The holes are the marks `[?l]`, `[?a]`, `{b}` and the
`[?mi ne] [?faccia]` quoted from c. 14r in the notes. Both figures are above 0.95, so the class is not affected.

Key correction: none to the values. The split above would let each sign name carry one value. It was not written into
`key.tsv` or the transcription; that is left to the maintainer.

## Not done
`u`|`v` not checked. Not checked by a human palaeographer. c. 14r not re-read.
