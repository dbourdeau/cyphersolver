# ferdinand1473: Ferdinand of Aragon to John II, cipher letters of 1473 and 1474 (BNE MSS/20211/64 and /73)

Catalogue #857. Contributed by Michael Brackx (work done with Claude Code under his direction), 29 Oct 2026.

Both cipher passages read: 1473 except two signs, 1474 with two doubtful words; the 1470 sibling /56 transcribed
only. Every remaining gap has an outside blocker (see Remaining gaps).

## Status

- **d64**, MSS/20211/64 (bdh0000186643), Ferdinand, king of Sicily, to his father John II, Hostalric, 5 June
  1473 (catalogue #857): the cipher passage, nine lines of the recto (201 signs), is read except two signs. Key
  rebuilt from the interlinear notes of a second hand (words and single letters) and extended by sense.
- **d73**, MSS/20211/73 (bdh0000186628), the same to the same, Zaragoza, 3 Nov 1474 (not in the catalogue): the
  cipher passage (eleven lines, 310 signs, a different cipher) is read. Its plaintext is the clear paragraph at
  the foot of the same page; the key was first read from the interlinear letters, then aligned on that paragraph.
- **d56**, MSS/20211/56 (bdh0000186631), Dueñas, 12 Nov 1470: a third cipher (numbers and signs, probably
  syllabic) with a faint modern pencil decipherment; transcribed (`transcription/d56_transcription.md`), not
  attacked. Not in `profile.json` documents.

Prior work: Galende Díaz, "La escritura cifrada durante el reinado de los Reyes Católicos y Carlos V", *Cuadernos
de Estudios Medievales y Ciencias y Técnicas Historiográficas* 18-19 (1994) 159-178, lists /56 and /73 as ciphered
letters of Ferdinand to John II, with no key; /64 is not in his list. No edition or decipherment of /64 or /73 was
found (web search, 29 Oct 2026).

## Sources

BNE Digital (images CC BY 4.0, Biblioteca Nacional de España). The "high" PDF of each record holds one JPEG per
page: /64 1085 x 1187 px, /73 1114 x 1510 px, /56 1117 x 1485 px. Read in the pdf.js viewer at 4-16x and on a
re-rendering of the page cut into line strips. BNE Digital blocks a client that requests many records quickly:
fetch one record at a time.

## d64 (1473)

**System.** Homophonic letter substitution, 39 kinds of sign as transcribed (about 30 with a value), set inside
the clear text: several signs for each vowel and for *c*; one place sign (`FI`, long s and i joined, with a
cross-bar), noted *barçna*, Barcelona. No other nomenclator sign. Signs that looked alike were separated at 12x
(`3` *h* / `3-` *y*; `-o-` *i*, `o-` *a*, `ooo` *ll*; `T` *r* in 8 of 8, `TT` *s* in 13 of 13). Key: `key_1473.md`.

**Decode.** `python3 dec1473.py transcription/d64_transcription.md` (no hand corrections; where a sign has two
values both are printed) -> `decryption/d64_decode.txt`. Reading `decryption/d64_reading.md`, English
`decryption/d64_en.md`.

**Content.** Ferdinand reports the troops he brings for the relief of Perpignan: his *continos* and men from
Castile, more than 500 horse from Aragon, the Valencians (some already at Barcelona, the rest within the week),
800 horse in all with 100 men-at-arms.

## d73 (1474)

**System.** Homophonic letter substitution of its own (not d64's alphabet): bar signs (`-o-`, `-+-`, `o-`),
dotted signs, a null (`A` without dots), a sign for *qu* (`me`). The `4` sign gives *a*, *r* and *c*: probably
three look-alike signs. Key: `key_1474.md` (counts per sign).

**How it was read.** A 19-sign key read from the interlinear letters alone decoded *no res menos se*, *…matrimoni…
in / fanta mi hermana no se*, *mossen s…*, *se fa..na…*; the same words begin the clear paragraph at the foot of
the recto ("No res menos senyor yo he sabido…", `decryption/d73_clear.md`). `align1474.py` then aligns the 310
signs with the paragraph's 325 letters and re-estimates the key (`decryption/d73_alignment.txt`); `dec1474.py`
decodes with it (`decryption/d73_decode.txt`). Reading `decryption/d73_reading.md`, English
`decryption/d73_en.md`.

**Content.** Ferdinand is astonished that the marriage of the infanta Juana, his sister, "no se es rompido" as
negotiated, and asks that if anyone is sent to Naples on the matter it be Mossèn Santcliment, so that his own
affairs are handled with the others. (Juana married Ferrante I of Naples in 1476-77.)

## Tried and ruled out (do not repeat)

- The 1473 key on /73 and /56: different alphabets.
- A `p` split by shape (hooked top = *o*, plain = *c*) in d64: the plain p also stands for *o* (*ochocientos*,
  *ciento*); dropped.
- *complido* for *rompido* in d73 on the strength of the cipher's first sign (`2`, *c* elsewhere): the clear text
  and the interlinear letter both give *r*; kept *rompido*.

## Remaining gaps

- d64 L05, two signs `H C` in `P H C qo` after *de Castilla* (*c-m-?-o*; `C` occurs only here) - blocker: open-codes; sense wants *con migo* or similar
- d64, the σ-like `6` (*a* in four words, *i/j* in *mios* and *juntos*) and the plain `p` (*c*, *o*, once *a*): values chosen by sense - blocker: illegible; the 1085-px scan does not separate the forms
- d73, *rompido* (cipher first sign `2`, *c* elsewhere) and *promendo* (so in both texts; sense not settled) - blocker: illegible; a better image would settle the letters
- d73, the place sign `fi` near *a Napols* (Barcelona in d64) and the signs met once or twice - blocker: too-short

## Escalation

- [x] siblings: /56 and /73 (Galende 1994) found and transcribed; /73 read
- [x] clear-pages: /73's clear paragraph found to be the plaintext; /64 has no clear copy on its three images
- [n/a] known-keys: no key of Ferdinand and John II in Galende 1994 or in the BNE records
- [x] print: Galende 1994 checked; no edition found
- [x] key-rebuild: d64 from the notes; d73 aligned on the clear text
- [x] retry: transcription re-read at 8-16x after each round; decodes re-run without hand corrections
- [ ] other Ferdinand -> John II letters in MSS/20211 (/57 1471, /80, /82 1475, /99 1476, /105 1477, /120,
  /123 1478) not checked for cipher

## Next steps (ranked)

1. Ask BNE for better images of /64 (L05 and the σ- and p-signs) and /73 (*rompido*, *promendo*).
2. Check the other MSS/20211 letters for cipher in the d64 or d73 alphabet.
3. /56 (not part of this target's reading): read its pencil decipherment on a better image and rebuild its key.

## Files

`transcription/d64_transcription.md`, `d73_transcription.md`, `d56_transcription.md` (sign tables and the
interlinear notes); `key_1473.md`, `key_1474.md`; `dec1473.py`, `dec1474.py`, `align1474.py`;
`decryption/` (decodes, alignment, clear paragraph, readings, translations).
`validation.tsv`: the d73 pairs from `align1474.py` for `docs/_validate.py` (verdict "not applicable": polyphony
0.2, the `4` and `q` signs carry more than one value).

## Checker output (29 Oct 2026)

- `docs/_check_profile.py ferdinand1473`: valid (4 unknown fields: homophones per letter, nomenclator size, nulls).
- `docs/_check_reading.py ferdinand1473`: d64 reading 7/8 sentences clean, holes 0.11; d73 reading 3/7 sentences
  clean, holes 0.19 (probably the Catalan-Aragonese spellings *senyor*, *fechos*, *facan*, *bueltas* against
  the Spanish model; not checked). Both translated.
- `docs/_check_writeup.py ferdinand1473`: INCOMPLETE. Missing: the docs/ write-up surfaces (page, manifest, README
  row, portrait, snip, reveal, keys.json), which are for the maintainer on merge, and the `reading_review` of each
  reading, which is the reviewer's.
