# The cipher in Thomas Fossey's notebook of veterinary recipes (1710–1716)

Beinecke Rare Book and Manuscript Library, Yale University, GEN MSS VOL 855.
A notebook of farm and veterinary remedies in which parts of the recipes are written
with digits mixed into the English. This repository records the key and the reading.

**Status: a full reading.** All 38 images that carry cipher digits have been transcribed, and
**the reading of all 36 is published.** Of the 3,490 cipher symbols (occurrences of the digits 1–9),
3,359 (**96.2%**) fall in words that make sense. That figure includes the thirteen places where the
digit 9 and the letter g are written alike and the reading that makes a word was taken
(listed in `data/g9.tsv`); without that step the count is 3,332 of 3,492 (95.4%). What is left is concentrated in Latin drug
names, personal names, text hidden under pasted slips, and struck-through passages
(`docs/OPEN.en.md`). In a control of 1,000 shuffled keys, none reached the real key.

## Relation to earlier work

Daniel Bourdeau's catalogue of unsolved ciphers (item 818) already records, as of
28 October 2026, that "vowels [are] replaced by digits, trivially readable".
**The identification of the method is therefore not ours.** What this repository adds is:
that the substituted letters are not only the vowels but nine letters (a e i o u l m n r);
a transcription and reading of all 38 cipher images; the control; and the list of what is
still unresolved. We do not claim to be the first to solve it. See `docs/PRIOR_CHECK.en.md`.

## The method and the key

Nine common letters of English are replaced by digits; every other letter stands as written.

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|
| a | e | i | o | u | l | m | n | r |

Word division, capitals and punctuation are unchanged. w is written uu, as the notebook
spells it elsewhere (b6455 = blouu = blow). The digit 0 never occurs.

**The substitution is not applied consistently.** Words written out in full appear inside
the same lines (for example "that" in p.19 "f49 1 h49s2 that 3s p93ck'd", "halfe" in p.25
"18d 1 halfe"). Counted over the cipher lines: 1,295 words contain digits, 242 do not.

## Evidence for the key

Image 18 carries this heading in plain English:

> for a blow in a horses eye to eat of y[e] Cell

The second line of cipher on image 19 begins with the same phrase:

> f49 a b6455 38 a h49s2s ey2 → for a blouu in a horses eye

The same phrase, in the same hand, in both plain and cipher. That fixes
2=e, 3=i, 4=o, 5=u, 6=l, 8=n, 9=r; the next line gives 18d = and and C9217 = Cream,
fixing 1=a and 7=m. Evidence per value is in `data/key.tsv`.

A second, independent support is on image 70, a page of pen practice. It carries a table
of exactly the nine letters a e i o u l m n r, and a memorandum
"Receved of eight men of y{e} first = or : n …" in which letters stand for numbers.
The nine letters of that page are the nine letters the key assigns.

## Samples of the reading

- p.36 `1s y45 sh166 th38k fit b21t 3t 38t4 529y f382 p45d29`
  → *as you shall think fit beat it into uery fine pouder* (how to make the powder of honey and lime)
- p.21 `a 72d3c82 f49 the B3t2 4f 1 71d D4g` → *a medicne for the Bite of a mad Dog*
- p.25 `S3x b5ſh26 of 716t: w366 B9255 f459 h4gsh21d of S7166 B229`
  → *Six bushel of malt: will Breuu four hogshead of Small Beer*
- p.56 `C94c5572t26 4957` (Crocus Metallorum), `D31p28t52` (Diapente), and other drugs of the period

The whole text is in `data/transcription/` (as written) and `data/reading/` (decoded), one file per image.

## Numbers

| | |
|---|---|
| Images carrying cipher digits | 38 (36 transcribed; the other 2 photograph the same leaves with the pasted slips moved) |
| Lines transcribed | 625 |
| Cipher symbols (digit occurrences) | 3,490 (fragments cut off by a pasted slip are not counted) |
| Symbols in words that make sense | 3,359 (96.2%); 3,332 of 3,492 (95.4%) without the 9/g step |
| Control (1,000 shuffled keys) | 0 reached the real key (real 96.8%, best shuffle 55.9%) |
| Calibration | none available; no contemporary decipherment or printed edition exists (`docs/METHOD.en.md`) |
| Agreement with an independent second reading | 90.7% over all 36 images (Claude Sonnet) and 91.3% (OpenAI Codex). The lowest page is 70.6%. Every run's figure is given in `docs/VERIFICATION.en.md` |

## Human checking

**No human has checked this transcription.** Both the transcription and the reading were
made by AI. Agreement between AI readers is not a substitute for a human check.

## Use of AI

Finding the source, fetching the images, the transcription, recovering the key, the control
and this write-up were done by AI (Anthropic Claude). A second reader, OpenAI's Codex CLI,
was given the same images independently (`docs/VERIFICATION.en.md`). The human directed the
work and decided to publish.

## Contents

- `data/key.tsv` — the key with the evidence for each value.
- `data/transcription/`, `data/reading/` — per-image transcription and decoding.
- `data/verified.tsv`, `data/verified_auto.tsv` — every place where a reading was changed after
  checking the full-resolution image, and the places where a proposed change was rejected.
- `data/g9.tsv` — places where the digit 9 and the letter g are written alike and the reading
  that makes a word was taken.
- `data/materia.txt` — period spellings and drug names not in a modern dictionary, with the evidence.
- `controls/` — the shuffled-key control and the count of meaningful symbols.
- `src/` — the programs. `docs/` — method, open questions, prior art, verification.
- `SOURCES.en.md` — the source.

Japanese versions are the files without `.en`.
