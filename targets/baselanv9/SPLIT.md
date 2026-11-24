# SPLIT: baselANV9 (recorded 24 Nov 2026, about 22:40 Brisbane, before any key building)

Track: adjacent plaintext. Outcome category if it works: key recovered from adjacent plaintext.
Canvas numbers are the manifest order (work/canvases.tsv); folio = the pencil foliation on the leaf.

## TRAIN (aligned with the clear copy; the key is built from these only)
| folio | canvas | page id | clear counterpart |
|---|---|---|---|
| 4r | 11 | 5353230 | f. 101r (canvas 209) and on |
| 4v | 12 | 5353231 | f. 101r-101v (canvas 209-210) |
| 5r | 13 | 5353232 | f. 101v-102r (canvas 210-211) |

## HELD-OUT (decoded once, after FREEZE_KEY; never aligned with the clear copy before that)
| id | folio | canvas | page id | why | how scored |
|---|---|---|---|---|---|
| H1 | 15r | 33 | 5353252 | Book 1 text page: rule "first undamaged full text page at least ten leaves after the training leaves"; f. 14r (canvas 31) was passed over because its lower right corner is torn away (seen at contact-sheet size only) | against the clear copy (passage located after the decode) and by the judge |
| H2 | 159r | 325 | 5353544 | Septem sigilla, "Sigillum Iovis"; different quire and part of the volume | against the clear copy f. 167r (canvas 341), same layout; and by the judge |
| H3 | 34r | 71 | 5353290 | pentacle rim inscriptions (pentacles 3 to 8); the clear copy has no drawings per Steinmann, so no clear counterpart is expected | judge only (unaligned) |

Scope set before transcription of the held-out leaves (about 23:35 Brisbane, still before any key building):
H1 = f. 15r lines 1-12 (the first twelve lines; the rest of the page is not transcribed); H2 = the whole of f. 159r;
H3 = the rim inscriptions of pentacles 3 and 4 (the two upper circles of f. 34r). TRAIN was cut to ff. 4r and 4v
(f. 5r is not transcribed): 44 lines, about 1,300 signs.

Rules: the clear counterparts of H1 and H2 are not transcribed or read closely until the key is frozen.
I have seen f. 167r (H2's clear page) at contact-sheet size during the screen and the first look (its first two lines
are legible there: "Sigillum Iovis fit ex optimo anglico stanno, habens in una parte figuram ..."). That is a known
limit on blindness for H2's first lines, stated here before the decode.

Quarantine: canvases 199-206 (ff. 97-99: the pasted key leaves ff. 98-99 per Steinmann and swisscollections) are not
fetched or viewed until FREEZE_KEY.txt exists.
