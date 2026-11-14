# hintze1903: groups re-read on the images; decoder and page model re-run; a split for 3707/49641 that fits the order (Brice Dudout, Claude Opus 5.5, 14 Nov 2026)

`verify_dudout_20261114.py` (run from `targets/hintze1903/`; plain Python, no numpy). It reads only `code_values.tsv`,
the two transcriptions, `m0003_contemporary.txt` and `m0003_decryption.txt`. The work credited here is WAINUT's
contribution; this note only checks it.

## Image check

The four images of PT/TT/CAM/M15 were fetched from the DigitArq JSON backend (`/api/rdigital/<docId>`, then
`/api/rdigital/dissemination?fileId=`) and read in crops (kept privately; not copied here).

- All 29 groups of m0001 and all 25 of m0003 read as transcribed, with the clear words and the address and header
  strips. The stray stroke after 60134 and the retouched 5 of 53251 are as described.
- The decode of the time under the strips and on the back (m0004) reads as in `m0003_contemporary.txt`. *divorciado*
  and *contestar* are clear enough on a contrast-enhanced crop; *Livorno* is a smudged word beginning with a looped
  capital (L) and ending *-orno*: the reading stands, still with its [?].
- The Paris stamp of m0003 does not settle the day for me (the figures read "1 1/2" or "1 12"); the header day 11 stands.

## Decoder

- Telegraph word count, five figures or fewer = one word, punctuation not counted: m0001 12 + 63 = 75, m0003
  9 + 37 = 46, both the header figures.
- `code_values.tsv` applied to m0003 gives the published decryption for 25 of 25 groups (41285 written "V. M." there).
- Between the clear words the groups fall 1, 3, 5, 4, 8, 1, 1, 2, as in `code.py`. Only 41285 of m0001 has a value.

## Page model, refitted independently

Page = n // 100, pages below the split reflected, lines kept. Best rho 0.957 (any split from 350 to 376 gives it),
21 of 24 values in alphabetical order; 500 shuffles of the 24 words, split refitted each time, give a median of 0.277
and a maximum of 0.697. This reproduces the contribution's figures.

**3707 and 49641.** The decode reads "visita Presidente da Rep. franceza. Mm. dos Estrangeiros": five units for the
five groups 63416 50554 3707 49641 43322 if "Presidente da Rep." is one unit and the full stop that the decoder wrote
after *franceza* is a unit too. Then 50554 = *Presidente da Republica* (a phrase filed under *presidente*), 3707 =
*franceza* (between *falta* and *hoje* in the reversed half) and 49641 = a word between *ministro* and *presidente*:
*ponto* (the decoder's full stop) or *o*. With this split, 23 of 24 values are in order (rho 0.969); without
Livorno, 23 of 23 (rho 1.000). It needs no unwritten word. Not adopted in the files; left to the maintainer.

**A block of place names.** The three highest groups seen, 67033, 67394 and 67398, are the decoded *Livorno* and two
m0001 groups that stand right after the clear prepositions *em* and *a* ("EM 67033", "A 67394"). So the groups above
the v-words are likely place names filed at the end of the book, which explains why Livorno is "out of order" and
supports the contribution's guess 67394 = *Lisboa* (filed just before *Livorno*). Still a guess.

## Read bar

`v10_relabel.share` gives 0.793 on `m0003_reading.md` (46 words, 12 holes): the 12 holes are the articles and
prepositions supplied in brackets ([veio], [á], [das], ...), the known artefact. Counting only the decoded units,
all 25 groups have a word, the two doubtful ones (Livorno, contestar) as probable: 1.0, as recorded. m0001 stays not
read (1 of 29). No class changes.

## Key correction

None. The 3707/49641 split above is a proposal, not a correction.

## Not done

- The Diário da Câmara dos Pares for about 11 May 1903 (would confirm Livorno and contestar) was not consulted.
- No new value for m0001.
