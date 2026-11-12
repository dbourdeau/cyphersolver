# sosa1554: Álvaro de Sosa to the officials at Seville, Nombre de Dios, 4 July 1554 (catalogue 2192, letter 1 of 5)

Work by WAINUT (lccompany), 12 Nov 2026, with AI language-model agents viewing the images. No human palaeographer has
checked the text. An independent AI language-model agent reviewed the work blind on 12 Nov 2026 (see "Independent
review"); the changes made after it are listed there.

Status: in progress (not written up). Letter 1 is **decoded, not read**: the key is rebuilt from the clear copy and
validated on held-out paragraphs, but the mechanical text does not build clean sentences. Letter 2 is an attempt on its
heading only; letters 3-5 are not started.

## Documents

- **Cipher:** AGI, Indiferente General 737, N.171 (PARES description 300401), images 1-2: the first of the five cipher
  letters. A two-line heading, four paragraphs and a signature flourish; 41 transcribed lines.
- **Clear copy (crib):** AGI, Panama 29, R.6, N.23 (PARES 381859), images 1-2: "Copia de la carta que el gou[ernad]or de
  tierra firme escrivio a los officiales de Sevilla", the same four paragraphs, signed Alvaro de Sosa, "del nombre de dios
  a iiij de jullio de 1554". Transcribed in `clear_panama29_R6_N23.txt`. Image 5 there is a second clear copy and images
  8-9 are a second cipher copy; neither was used.
- **Image route:** `catalogo/show/<id>` with a cookie jar gives the list of `(txt_id_imagen, dbCode)` pairs. Then
  `ViewImage.do?accion=42&txt_descarga=1&dbCode=<d>&txt_id_imagen=<n>&txt_zoom=10&...` returns an 864 px JPEG, the largest
  size served. Both values must match: a dbCode alone returns image 1. Scans are not in git.

## System

The cipher is a letter substitution written in Latin-looking signs, with word gaps kept. A consonant sign takes a dot above
for a following *a* and a dot below for a following *e* (`c'` = da, `c,` = de, `co'` = ta, `m,` = ne, `3'` = va,
`r'` = ca, `N'` = ma, `g'` = ha). Other vowels have their own signs: e = `s`, i = a free dot, o = `B`/`ah`, u =
`o`/`w`/`3h`, a = `nh`/`g`. `D` with a dot, above or below, is *que*. There are some homophones (n = `m`/`N`,
c = `x`/`r`, l = `L`/`1`). No nulls or code words were found in this letter. The cipher writes numbers out in words where
the copy uses numerals. Five shapes (`2`, `b`, `d`, `e`, `p`; 49 tokens) have no value yet, and 7 tokens are unidentified.

## Key and held-out test

- The key was built from paragraphs 1-2 (lines 1.03-1.28) against the copy. I made a draft by hand from word pairs
  (`key_draft.tsv`), then tallied which letters each token aligns to (`scripts/em.py`, a Needleman-Wunsch letter
  alignment). The key was frozen as `key_frozen.tsv` (36 entries plus the two mark rules) before anything else was scored.
  `key.tsv` is the working key; it equals the frozen key (no change after freezing).
- Agreement with the copy, counted as letters of the copy matched by the mechanical decryption:
  - training, P1-P2: 1124 / 1408 = 79.8%;
  - **held out, P3-P4: 447 / 587 = 76.1%**, with P4 scored against the copy's numerals written out as words (P4n in
    `clear_panama29_R6_N23.txt`). Against the copy as written it is 400 / 535 = 74.8%.
  - The two-line heading is not part of the copy's letter text and was not used to build the key. It decrypts to
    `?pia de l cart qeu governdor deuie??a eirma escrivio alos oeiuaicials de vi?a`, which is the copy's title "Copia de
    la carta que el gobernador de tierra firme escrivió a los oficiales de Sevilla".
- Most misses come from my sign readings at 864 px (dots, `o` against `s`, `N` against `m`), not from the key.

## Reading

- `decryption_ind737_letter1.txt`: the mechanical output, with no repairs (`scripts/decrypt.py`).
- `reading_ind737_letter1.md` (`scripts/reading.py`): each cipher word is written either as its mechanical output or as
  `{mechanical/clear}` where it departs from the copy. `scripts/check_marks.py` passes (39 lines of paragraphs 1-4,
  0 unmarked departures).
- Word counts, by cipher word: **409 words, 161 read verbatim from the signs, 248 gloss-only.** A gloss-only word is one
  where the mechanical output departs from the copy and the reading writes the copy's form (many differ by one letter or
  a shifted word boundary). The signs do not give those words; their form and sense come from the copy. The reading
  shows 0 holes only because every miss is filled from the copy.
- `docs/_check_reading.py --file` on the mechanical decryption: auto-detect 40 sentences, 0 clean, hole rate 0.599;
  forced to Spanish, 37 sentences, 0 clean, hole rate 0.611. **Clean share 0.0.** The reading file scores higher only
  because it carries the copy's words inside the marks and the copy's paragraphs; that is not a reading from the signs.
- **State: decoded, not read** (confirmed by the independent review). The letter's text is already known from the copy,
  so this document adds the key and its validation, not new content.
- `translation_ind737_letter1.md` translates the clear copy, not the cipher.
- The amount in P4 is my reading of the copy's "ccLxxvU" as 275 thousand. The cipher's spelled-out number decrypts to
  `dosientos y setnta y cin co ni? pesos`, so the "mil" there rests on a partly unread word.

## Independent review (12 Nov 2026)

An AI language-model agent that did not take part in the work reviewed it blind. It copied four lines (1.06, 1.21, 1.32,
2.07) from its own 4x crops of the scans before it opened the transcription, re-ran the scripts, and re-measured the
held-out test.

- Signs: roughly 85% of base shapes agree; the differences are mostly dots and a few sign identities (listed under
  Remaining gaps). This fits the quarter of letters that fail.
- `scripts/check_marks.py` passes; `scripts/decrypt.py` with `key_frozen.tsv` rebuilds the decryption exactly.
- Held-out: P1 651/810, P2 473/598, P3 260/333, P4n 187/254, P4 140/202, so 447/587 = 76.1% and 400/535 = 74.8%, as
  claimed. Every key entry occurs in P1-P2; no key token occurs only in the held-out lines. With pass 1 alone (made
  before the key) the held-out score is 443/587 = 75.5%, so pass 2 did not inflate the test.
- Baselines with the same scorer: the correct decryption against the wrong part of the copy scores 0.39-0.41; 20 shuffled
  keys score 0.384 on average (0.419 at most). 76% is far above chance.
- The heading of letter 1 decrypts to the copy's title, and the same key gives a partly legible heading for letter 2, in
  another hand. Both are independent support for the key.
- State: decoded, not read, agreed. Letter 2 is not a decoded document and is recorded only as an attempt (below).

Changes made after the review: the 248 repaired words are described as gloss-only words (here, in `profile.json` and in
the reading's header); letter 2 is folded into this folder as an attempt, not a separate text; `profile.json` is put into
the repository schema, with the clear copy credited as "key or decipherment used"; the reviewer's different sign
readings and the unused second cipher copy are recorded as open points. No sign, key value or mark was changed.

## Other letters in the unit

- **Letter 2 (images 5-6, another hand): attempt on the heading only.** The docket on image 8 begins in clear "Relación
  de los navíos de la flota". One transcription pass of lines 1-8 of image 5, decrypted with `key_frozen.tsv` unchanged,
  is in `work/letter2_attempt/`. The heading decodes in part (mechanical output): `relcion delos navios enquevinia ...
  ylos navios que han ar? ... re no han uerado ... enla mar ... enla mapnera sig?`. Lines 5-8 do not decode, because the
  second hand forms several signs differently (`w`, `s c o g`, the reversed c) and their values are open. This is
  evidence for the letter-1 key, not a decoded document.
- The letters on images 9-11, 13-15 and 17-26 (lists and accounts) were not transcribed.

## Remaining gaps

- Sign readings at 864 px, letter 1 - blocker: illegible; dots above and below are hard to see, and lines 1.01-1.28 and
  2.07-2.10 had one pass only. The blind reviewer read these places differently, and both readings are kept open until
  they are checked on a better image or on the second cipher copy:
  - 1.06: transcription `i u, o`, reviewer `i w o`; transcription `g r a" c q`, reviewer `a" a, q`.
  - 1.21: transcription `D' D N | c B 1`, reviewer one D, `D N c B | 1`; transcription `s o s y,`, reviewer `w o s y`.
  - 2.07: transcription `/` after `c r`, reviewer a dotted i; transcription `e' q`, reviewer `c' q`.
  (2.07 is the 6th line of image 2; the file numbers image 2 from 2.02.)
- Second cipher copy of letter 1, Panama 29 R.6 N.23 images 8-9 - blocker: not-attempted; not compared; the cheapest way
  to settle the doubtful dots.
- Shapes without a value (`2`, `b`, `d`, `e`, `p`; 49 tokens) and 7 unidentified tokens - blocker: not-attempted; rare
  in letter 1.
- The "mil" of the sum in P4 - blocker: illegible; rests on a partly unread word.
- Letter 2 (images 5-6) - blocker: not-attempted; everything after line 8 of image 5, all of image 6, a second pass, and
  the second hand's sign values.
- Letters 3-5 (images 9-11, 13-15, 17-26) - blocker: not-attempted; not transcribed.
- Prior art: Lohmann Villena, "Cifras y claves indianas" (1954) - blocker: not-attempted; may print this key or a
  related one.

## Escalation

- [x] siblings: the clear copy in Panama 29 R.6 N.23 gave the key; letter 2 of the same unit tried with it (heading only)
- [x] clear-pages: Panama 29 images 1-2 used as the crib; image 5 (second clear copy) not used
- [ ] known-keys: no other key of the Tierra Firme correspondence of the 1550s tried
- [ ] print: one web search only; Lohmann Villena (1954) not checked
- [ ] key-rebuild: the five shapes without a value and the second hand's values not rebuilt
- [ ] retry: doubtful signs not retried against the second cipher copy (Panama 29 images 8-9)

## Prior art (checked 12 Nov 2026)

- Catalogue vetting, 4 Nov 2026: the letters are not on DECODE, there is nothing in Tomokiyo's pages, and no study of
  Indiferente 737 N.171 was found.
- One web search on 12 Nov 2026 ("Alvaro de Sosa" Tierra Firme 1554 cifra carta cifrada Indiferente 737) found no edition
  or decipherment. The clear copy in Panama 29 is named in the archive's own description, and it is the crib used here.

## Files

- `transcription_ind737_letter1.txt` (reconciled), `_pass1.txt`, `_pass2.txt` (held-out lines only); `SIGN_CONVENTIONS.md`.
- `clear_panama29_R6_N23.txt`: the clear copy, by paragraph (P4n with the numerals written out, for scoring).
- `key_draft.tsv`, `key_frozen.tsv`, `key.tsv`.
- `decryption_ind737_letter1.txt`, `reading_ind737_letter1.md`, `translation_ind737_letter1.md`.
- `scripts/`: `decrypt.py`, `em.py` (alignment and scores: `python scripts/em.py key_frozen.tsv P1,P2,P3,P4n,P4`), `reading.py` (marked reading), `check_marks.py`, `common.py`.
  Run from this folder.
- `work/letter2_attempt/`: letter 2, lines 1-8 of image 5, one pass and its mechanical decryption.

## Images

- Cipher: https://pares.cultura.gob.es/ParesBusquedas20/catalogo/description/300401 (letter 1: images 1-2; letter 2:
  images 5-6, docket on image 8)
- Clear copy: https://pares.cultura.gob.es/ParesBusquedas20/catalogo/description/381859 (images 1-2 and 5; cipher copy on
  images 8-9)
