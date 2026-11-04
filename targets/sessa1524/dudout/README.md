Status: read in part (94 %) (Brice Dudout, 4 Nov 2026; BNE MSS/20214/52-7, ciphered part 630 of 670 words read, 40 unresolved).

# BNE MSS/20214/52-7: Sessa to Charles V, Rome, 24 July 1524, read in part

Contribution by Brice Dudout. Daniel's files in the parent folder are unchanged.

## The piece

Biblioteca Nacional de España, MSS/20214/52-7 (Gayangos papers; Biblioteca Digital Hispánica, CC BY 4.0). Luis
Fernández de Córdoba, Duke of Sessa, imperial ambassador in Rome, to Charles V, Rome, 24 July 1524. Incipit (in clear):
"De los xiiij del presente es la ultima que a V. M. tengo escripta…". Three pages almost wholly in the cipher of this
folder (views 000-002; 003 blank, 004 address); 1,340 code groups and 531 words in clear. No period decipherment with it.
Read from the BNE digitisation; no image is reproduced here.

## Prior work

- Not in Bergenroth, CSP Spain vol. 2: July 1524 has nos. 661-663 only, none of 24 July.
- DECODE R9893 (RAH Salazar A-31 ff. 483-485, also 24 July 1524) is a different, short letter ("Estando escriviendo
  para V. M. con el correo ordinario…"), two cipher passages with their clears; 52-7 is probably the long letter sent
  "con el dicho ordinario" that R9893 announces.
- DECODE R9894 (A-31 ff. 504-510) is another letter, Rome 29 July 1524 = CSP Spain ii no. 663.
- No clear of 52-7 is known (BNE, RAH, CSP).

## Method

- Key KS4 (`key_KS4.tsv`, 305 entries): your key (`key_working.md`, read only) extended and corrected only from
  contemporary cipher/clear pairs: R9873 aligned with its period clear BNE 52-1 (14 Apr 1524), then BNE 52-10 (12 Jul
  1525), DECODE R9893 A/B, BNE 52-14 (17 Apr 1526) and 52-4 (7 May 1524), each with its clear. Corrections include
  gul = quando, hay/hag = porque, ges = es, gam = quanto, kel = mayor (sources per value in the file).
- Validation, written and hashed before any computation: KS4 frozen, then the held-out pair BNE 52-6 / its clear
  (4 Jun 1524, same year as the target, 371 groups, transcribed after the freeze, never used for the key), one
  measurement: characters 0.860, words 0.772; 200 shuffled-key controls max 0.274 / 0.174. Thresholds fixed in
  advance: 0.85 / 0.75. Passed (`validation_52-6.txt`). Two earlier keys (KS2 on 52-10, KS3 on 52-14) failed their
  held-out tests and were not used for a reading.
- 52-7 then transcribed (`bne52-7_transcription.txt`), decoded with KS4 unchanged, and read by your rule
  (`bne52-7_reading.md`, `bne52-7_count.txt`). The r-like sign has three forms; a pre-registered blind plate of 12
  sign shapes answered by Brice Dudout settled that the closed-loop form is u (8 of 8), and the v2 transcription
  classified all 100 occurrences on the images before decoding. A second plate (7 signs, 4 Nov 2026) confirmed four
  probable words (con, embaxador twice, papa); it could not add more than one word read.

## Count (ciphered part only)

670 words: 590 certain, 33 probable, 7 restored, 40 unresolved → 630/670 = 94.0 %, under 95 %, so "read in part".
Counting the letter's plain text as certain: 96.7 % of 1,198 words. Recurring unresolved groups: rob, 3om, 3im, boc,
boz, dup, bie, 3cp, gab, yac, car; none occurs in any of the five BNE pairs or in R9893.

## Content (summary)

The Pope's words, reported by Sessa: everything in Italy is confused since the viceroy left; the Pope is pressed to
join a league (England wants it) and has not consented and will not; news "by way of Monsieur de Bourbon" on what was
proposed to the Emperor ("to make war on him"); the French, suspicious and fearful, will use whom they can; the datary
(Giberti) and the archbishop of Capua; the bishop of Bayeux (Canossa) now an avowed French ambassador; Sigismondo
(not identified) with the French ambassador; Casale's going to England; Alberto Pio da Carpi back from Viterbo; the
confirmation of the league "as Your Majesty's advocate advised"; a letter from Lyon copied and sent; Pescara takes the
marquisate of Saluzzo, the army without pay. English working translation: `bne52-7_en.md`.

## Limits

- One reader, images at 120 ppi; simple signs remain uncertain in places.
- The two unresolved runs of V1dL16 (‹ka ϑ g x›, ‹ϑ g x ges›) are left open; reading them would give 94.3 %.
- `qob` reads "ellos" in the held-out 52-6 but stays unresolved here (the plate kept q); not changed after the
  measurement.
- A clear of 52-7, or a fresh 1524 pair (RAH, Simancas), would be needed to close the 40 words.

## Files

`bne52-7_transcription.txt`, `key_KS4.tsv`, `validation_52-6.txt`, `bne52-7_reading.md`, `bne52-7_count.txt`,
`bne52-7_en.md`.
