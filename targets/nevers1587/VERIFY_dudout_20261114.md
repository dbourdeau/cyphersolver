# nevers1587: independent decode and an image check of f. 28v (Brice Dudout, Claude Opus 5.5, 14 Nov 2026)

## Decoder
`verify_dudout_20261114.py targets/nevers1587` reads only `key.md` (alphabet with the key's column and "this
writer's forms", small-word capitals, numbered names) and `ciphertext.txt`, and compares with `reading.tsv`
(`dec.py`, `edits.py`, `enum_readings.py` not used). **24 of 27 units** take a value that the key or the writer
column allows. The three others are the ones NOTES already argues: dateline `z` read n (both columns of `key.md`
give q; NOTES: "2 and z are one shape" in the sibling), dateline `ι` read d (not in `key.md`; the writer's dotted-i
form of d), and run `ƥ` taken as a null against its key value a. No new disagreement. One small point: `key.md`'s
writer column does not list `z` under n or `ι` under d, though the reading uses them so.

## Image check (Gallica btv1b90605473, canvases 53 and 56, full size)
f. 28v (14 lines of clear text, the dateline and the closing) read against `reading.md`:
- l. 2: the `[?]` after *quelques jours* is not an unread word. A word is heavily struck through after *quelques*
  and *jours* is written above it: "il y a quelques ~~…~~ jours, ce n'est". Corrected (the hole removed).
- l. 7: "sans avoir **eu** cest heur que de vous entretenir": *eu* is on the leaf and was missing. Corrected.
- the rest of the page agrees (spelling differences only, e.g. *jusqu'a cest heure* for *jusques a ceste heure*).
- dateline `C ∞ 6 ƥ z ι ◊ é ι ⊕`: the signs are as transcribed; the last ⊕ is struck through, as NOTES says.
f. 30r ll. 2-7 (clear text, agrees) and the run `π ^ ꭓ é ∞ ƥ F ƨ h Ŧ ◊ 7 o`: as transcribed; nothing on the image settles `ƥ`.

## Read bar (README)
`v10_relabel.measure` on `reading.md`: 0.992 recorded, 0.992 recomputed before the corrections, 0.993 after. By
letter (the README counts per document): f. 28 0.989 -> 0.991, f. 30 0.997. v10 counts the bracketed code
expansions (*[le marquis]* …) as supplied words; without them both letters are 0.998 / 1.0. Both stay read.

Key correction: none.

## Not done
f. 28r (the first page of the letter) was not re-read on the image; the sibling fr. 3413 f. 102 was not re-checked.
