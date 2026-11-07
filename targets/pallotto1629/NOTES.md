# Pallotto to Barberini, 1629 — ciphered despatches of the nuncio at Vienna

Status: in progress (22 Oct 2026, reread batch b01: 22 of 28 sheets read as sentences with English translations, fraction_read 0.80; R291, R300, R301, R302, R304, R313 read in part). Earlier: read — contents in print (Kiewning 1897); key = the Biermann–Bosbach key of Barb.lat. 6956 (DECODE R215, 2018), identified for 6960 by George Lasry

**22 Oct 2026, reading audit** (George Lasry's test: can a reader build coherent sentences and translate them?):
* **Read**: R286, from Kiewning 1897 Nr. 153 (the Roman decipherment in print; `crib153.txt`). English translation
  still to be written.
* **Decoded, not read**: R287-R313. The automatic decode with the 6956 key (`texts/R*_decrypt.txt`) has garbled
  strings and open three-digit groups in most clauses (2-24% of sentences clean); their counterparts in Kiewning
  have not been matched.
* Class already solved kept; method read with known key -> read from existing decipherment (parts); 0.95 withdrawn
  as a reading figure (0.030 = R286's share). "every record decodes to running Italian" below is withdrawn.

**22 Oct 2026, reread batch b01** (REREAD_BRIEF; Claude Opus 5.5 as coordinator, R290 read by it, the other sheets by six
reader agents of the same model; `research/reading_audit/reread_b01.py` applied the profile changes):
* **A better decode** (`reread_b01_decode.py`): the nulls 1 and 8 never sit inside a group (no key group contains them;
  `key6956/apply.py` let unknown groups such as [983] swallow them); 2/3-digit segmentation chosen by an Italian 5-gram
  model; DECODE's uncertain digits kept as alternatives; DECODE's frequent misreading of this hand's null 8 as 0 modelled
  (seen on the R286, R290 scans). Output `reread_b01/R*_dec.txt`.
* **Every sheet matched to Kiewning** (`reread_b01_match2.py`, 9-letter hits) and aligned with the print chunk by chunk
  (`reread_b01_align.py`, `reread_b01/R*_align.txt`). Kiewning prints R286, R287, R289, R306, R307, R311, R312 verbatim and
  parts of most others; the rest is German regest.
* **Key extended**: 125 nomenclator groups missing from the 6956 key, each with its evidence, in
  `reread_b01/extra_groups.json` (e.g. 577 = N. S./the Pope, 592 principe, 595 principe d'Echembergh, 743 far, 744 fatto,
  544 negotio, 639 re di Francia, 290 Cardinal di Richelieu, 207 consiglieri secreti, 440 Gesuiti). Key entries corrected:
  776 = tutto (not "quanto"); 567 = occasione (sometimes ordinatione); 677 = "S. S." of either the Pope or a cardinal.
  The three-digit groups are roughly alphabetical (2xx A-C ... 9xx S-V, 7xx common words). "Magno" is spelled out 62 99 96.
  Unknown groups in the decodes: about 5,000 -> about 800.
* **Readings** `texts/R*_reading.md`, translations `_en.md`, logs `_reread_log.md`, DECODE digit and clear-text corrections
  `_corrections.tsv` (DECODE's clear-text transcriptions are mostly unusable; re-read on the scans). R286 translated
  (`texts/R286_en.md`). Clean-sentence shares 0.53-0.94 (target 0.81).
* **Records and dates corrected**: the volume runs 4 Aug - 29 Sept 1629 ("7mbre" = September; DECODE's November dates and
  "1627"/"1679" are misreadings). One despatch spread over several records: R286+R287 (Nr. 153), R289+R290 (Nr. 156),
  R292-R294 (Nr. 160), R297+R299 (Nr. 164), R302+R303 (Nr. 167), R306+R307 (Nr. 176), R311+R312 (Nr. 184). R298 is 11 Aug
  (Nr. 158), R304 28 Aug (Nr. 168), R309 = Nr. 178 (16 Sept in Kiewning). R300 p. 2 (image 2532) was never transcribed by
  DECODE: transcribed in `texts/R300_p2_digits.txt`. R301's continuation (register p. 78) and register pp. 81-82 are not
  among the DECODE images. R287's docket "Decif.ta li 22" matches Kiewning's Roman decipherment date: these sheets may be
  the originals received in Rome rather than register copies (open).
* Kiewning slips the figures correct: R291 "duca Alberto" (regest "Alfons"); R307 "aiduchi" (print "arciduchi"); R313 "sotto
  li quindici" (regest "25. September").

## Update, 21 Sept 2026: the key exists, and it is the 6956 key

George Lasry wrote (relayed by Daniel): *"Barberiniani Latini 6960 uses the same key as Barberiniani Latini 6956
(which was found by Norbert Biermann and Thomas Bosbach) — I found this years ago, but the DECODE DB was never
updated."* Checked and confirmed.

* The key is filed on **DECODE R215** (Barb.lat. 6956, first sheet) as documents, not as a key record, which is why
  the metadata harvest never saw it: `DOC_R215_D1506` (Biermann's key, March 2018), `D1507` (Bosbach's), `D1508`
  (merged), `D1505` (a codebreaker.py decryption of R215). Copies in `key6956/`.
* The system: **two-digit homophones** for letters (a = 00/02/20, e = 09/30/90, i = 05/40/50, o = 03/07/70 …),
  two-digit groups for syllables and short words (47 che, 52 con, 57 per, 69 di, 73 la …), **three-digit
  nomenclator groups 200–999** for names and titles (360 Duca di Mantova, 460 Imperatore, 670 Sua Maestà …), and
  the digits **1 and 8 as nulls / word separators**. Doubles are often written once (33 = d or dd).
* Applied to DECODE's transcriptions of all 28 ciphertexts by DP segmentation (`key6956/apply.py`; output
  `key6956/decrypt_6960.txt`, unedited). R286 opens **"ho riceuto la risposta datami in scritto …"** — Kiewning
  Nr. 153 word for word — and every record decodes to running Italian. About 2,000 nomenclator groups resolve from
  the key; **about 1,750 three-digit groups are not in the 6956 key** and stay open (they could be filled from
  Kiewning's text, not done here), and ~200 digits fit no code (transcription slips).

**What this does to the analysis below.** The measurements stand; the conclusion drawn from them did not go far
enough. §5's "deterministic groups of varying length" was right, and it is exactly this key: one-digit nulls,
two-digit homophones and three-digit groups in one contiguous stream, so every fixed-width alignment slipped phase
at the first null or nomenclator group — which is why the crib run died at letter 28 and the corpus search found
nothing. **The key was not recovered by this project.** It was recovered in 2018 by Biermann and Bosbach for
6956, and matched to 6960 by Lasry; DECODE still lists R286–R313 as "Non-decrypted".

The sibling volume 6956 (catalogue 236, DECODE R215–R285, R318) is therefore also solved by others (R215–R225
are marked "Partially decrypted" on DECODE) and was removed from the catalogue.

BAV, Barb.lat. 6960 — 28 ciphered passages in the register of Monsignor Giovanni Battista Pallotto,
archbishop of Thessalonica, nuncio to the Emperor, 4 August – 29 November 1629.
DECODE records R286–R313 (28 ciphertexts) plus R315 (the whole volume), all "Non-decrypted".

The catalogue entry said "what the cipher hides is not known". It is known, and has been in print since 1897.

## What the target actually is

The manuscript is free on DigiVatLib: <https://digi.vatlib.it/view/MSS_Barb.lat.6960>, 194 pages,
IIIF manifest at `/iiif/MSS_Barb.lat.6960/manifest.json`. Those images are small — the IIIF `info.json`
gives a maximum of **748 × 1088 px** per page, an old bitonal microfilm scan, and anything larger the server
returns is an upscale. **DECODE has better scans of the same leaves**: `IMG_R286_I2489_P1.png` and
`IMG_R286_I2490_P2.png` are **1491 × 2066**, four times the pixel area, behind the login (cookie recipe in the
`decode-access` memory). Use DECODE's images, not DigiVatLib's, for any transcription work here.

DECODE's `additional_information` gives each record's page range in that same DigiVatLib pagination,
so DECODE page *n* = canvas *n*. Ranges are in `decode_records.txt`.

The volume interleaves **ciphered sheets** (full-width, dense numerals, e.g. pp. 5–6) with **clear text**
(written in a narrow right-hand column with a wide left margin, e.g. pp. 3–4, 7–9, 13). The clear pages are
not decipherments written against the cipher; they are the register's fair copies and the enclosures.

## The content is already published

Hans Kiewning (ed.), *Nuntiaturberichte aus Deutschland nebst ergänzenden Aktenstücken. Vierte Abteilung:
17. Jahrhundert, Band 2: Nuntiatur des Pallotto 1628–1630, 2: 1629* (Berlin 1897).
Full text on archive.org, item `4-2_20200807` (`4,2_djvu.txt`), saved here as `ed/pallotto_bd2_1629.txt`.

Kiewning prints Pallotto's despatches from the Rome-received copies in **ASV, Nunz. di Germania 119**, and
heads each ciphered one "**dechiffr.**" with the date the Roman office deciphered it — i.e. he prints the
*contemporary decipherment*. The Italian is given verbatim for the substantive passages, with German
regesta for the rest. Some forty Pallotto "dechiffr." despatches of 1629 are printed.

Two independent confirmations that Barb.lat. 6960 carries the same texts:

* **R286 = pp. 5–6 = 4 August 1629 = Kiewning Nr. 153** (*Arch. Vatic. Nunz. di Germ. 119 fol. 11–19*).
  The cipher sheet is headed, in clear, `Di Vienna 4 di Agosto / Ill.mo et R.mo Sig.r Card.le P.rone`
  followed by a struck-out opening line. The clear pages around it run continuously *through* the cipher
  sheet — p. 4 ends `...non haver facoltà di accettar altro partito, che'l proposto in` and p. 7 resumes
  `nome del suo Rè` — and that sentence is Kiewning Nr. 153 word for word.
* **p. 13** is the enclosure Kiewning prints as Nr. 153 *Beilage II, Propositione P. Valeriano per Sabran*
  (`Bibl. Barber. LXIX 60 fol. 122`), again verbatim: `...il quale aggiunse di più, che fatta la pace,
  quando S. Sta ... proponga una lega et unione di questi eserciti, affine di abbatter il Turco commune
  nemico del nome christiano, che S. Mtà mandaria plenipotentiarii in Italia, acciò N. Sre potesse
  concludere così gran negotio, con che il demonio resteria ingannato e burlato.`

So the despatches are about the Mantuan succession crisis in the summer and autumn of 1629: Pallotto's
attempts, through P. Valeriano Magno and the imperial minister Eggenberg (Echembergh), to mediate between
the Emperor and the French envoy Sabran over Casale, Susa and the Grisons passes.

## The cipher

Numeric, written as an unbroken stream of digits with decorative spacing. Transcriptions of all 28
ciphertexts were made for DECODE in 2019–20 by volunteers and are downloadable as `DOC_R*.txt`
(saved in `decode/`, fetched with the cookie recipe in the `decode-access` memory).
112,805 digits in total; R286 alone has 3,573 (measured with `docs/_check_profile.py --measure`).

Digit frequencies are strongly uneven (0 = 16.1 %, 4 = 4.8 %), and adjacent digits carry ~0.18 bits of
mutual information — so the stream is structured, not random.

**What was ruled out.**

* *Fixed two-digit codes.* No phase preference at all: index of coincidence 0.01462 at phase 0 versus
  0.01466 at phase 1; the even-position and odd-position digit distributions agree to within 0.2 %.
  Same for three-digit codes at all three phases. Under a genuine fixed-length code the correct phase
  should stand out.
* *Crib-free homophonic solve.* Fixed-multiset simulated annealing over the 100 two-digit codes,
  5,000 codes of text, scored by a space-free Italian 5-gram model built here from
  `lang/corpora/it-renaissance.txt` + `it-gutenberg.txt` (12.0 M characters, `it_clean5.npy`),
  reaches −3.54 log-prob per character against −1.5 for real Italian. Not a solution.
  (Note for reuse: the shared `lang/` corpus `it-nunziature.txt` is OCR garbage — it scores a string of
  twenty-four `i` better than real Italian. Do not build models from it.)
* *Syllabic two-digit nomenclator.* Aligning two-digit codes to plaintext spans of 1–4 letters against the
  known plaintext collapses back to single letters for every well-attested code, so there is no evidence
  for a syllable table.

**What looked like evidence, and is not.** The opening of R286 does align letter-for-letter with the known
opening of Nr. 153:

```
55 70 83 65 03 29 00 69 38 73 11 36 50 23 22 07 92 20 86 72 52 06 38 97 12 33 23
H  O  R  I  C  E  V  U  T  A  L  A  R  I  S  P  O  S  T  A  D  A  T  A  M  I  I
```

27 letters with two independent repeat confirmations (38 = T twice, 23 = I twice). I first read that as roughly
a 1-in-180 coincidence. **It is not: 27 is below chance.** See the run-length test below — random controls on this
material reach consistent runs of 36 to 39 letters. The opening match is unremarkable and should never have been
presented as support. Re-read on DECODE's better scan the line is essentially the same (two substitutions, no
length change), so the break at letter 28 is not a transcription artefact either. Iterating a banded DP aligner
over the whole of R286 reaches about 55 % code→letter consistency, which the held-out test below shows is worthless.

## Why the key is not recovered — measured, with controls

Two experiments were run after the first pass, and they change the earlier conclusion.

**1. Held-out test. The "key" recovered from R286 carries no information.**
Learn a table on the first 55 % of R286 against the crib, freeze it, then align the remaining digits to the
remaining crib and count confirmations (a confirmation = the code was already in the table and agrees).
Against eight controls that keep the same table but shuffle the letters among the codes:

| | confirmations per letter | DP score |
|---|---|---|
| learned key | 0.355 | −3266 |
| shuffled controls (mean of 8) | 0.359 | −3313 |

No separation. The same test for a "2-digit codes + nulls, no digit slips" model gives 0.440 against a control
mean of 0.431 — again nothing. **The ~55 % consistency reported in the first pass was the aligner fitting the
crib, not a key.** Any claim of a partial key here would have been wrong.

**2. Positive control. The pipeline works; this material defeats it.**
Encipher the same crib with a random two-digit homophonic key, damage the digit stream with single-digit
insertions and deletions at a given rate, and run the identical learner. Fraction of the true key recovered:

| digit error rate | key recovered |
|---|---|
| 0 % | 100 / 100 |
| 0.5 % | 87 / 100 |
| 1.7 % | 7 / 100 |
| 4 % | 19 / 100 |

So the method is sound, and it needs a transcription accurate to better than about **0.5 % of digits**. Above
roughly 1 %, a two-digit key cannot be recovered from this much text even when the plaintext is known, because
each inserted or dropped digit flips the code phase for everything after it.

**Correction to the first pass.** It said the images top out at 748 × 1088 px and that DECODE's transcription of
p. 5 line 1 differs from a fresh reading by about six digits in seventy-four including a length difference. Both
statements were wrong, and the error was mine:

* 748 × 1088 is DigiVatLib's maximum, but **DECODE serves its own scans of the same leaves at 1491 × 2066** —
  four times the pixel area (`IMG_R286_I2489_P1.png`, `IMG_R286_I2490_P2.png`, behind the login).
* Re-read on that better scan, line 1 differs from DECODE's transcription in **two digits out of seventy-four,
  both substitutions, with no length difference** (they read 93 where the scan shows 73, and 30 where it shows
  38). My earlier six-digit discrepancy was my own misreading of the low-resolution image. On line 2 the two
  readings differ by a digit or two and possibly in length, so the transcription still cannot be assumed exact —
  but DECODE's is better than the first pass credited, and no length error is demonstrated.

**3. Run-length test: there is no alignment signal at all.**
A crib aligner can fake a fit, but a long *consistent* run cannot be faked easily: inside one window a repeated
code must carry the same letter and the map must stay a function, so a false run dies at its first repeat
conflict. Scan every (digit offset, crib offset) pair in a band, extend each run while it stays consistent under
two-digit codes, and take the longest:

| | longest consistent run |
|---|---|
| real R286 against the plaintext of Nr. 153 | **39 letters** |
| control: crib letters shuffled (5 runs) | 39, 39, 36, 38, 36 |
| control: cipher reversed | 39 |
| synthetic two-digit cipher, same text, 1.7 % digit noise | **207 letters** |
| synthetic two-digit cipher, clean transcription | 2705 letters |

The real material sits exactly on its own chance baseline. The synthetic cipher at the *same* noise level as the
real transcription is five times longer. This method also recovers 81 of 100 key codes from the noisy synthetic
text, where the earlier DP learner managed 7 — so it is not that the tool is too weak.

**4. Corpus search: the ciphertexts do not encipher anything in the printed volume.**
The run-length test compares one ciphertext with one crib. This one compares four ciphertexts with the *whole*
edition at once, exactly. For a substitution, equal codes force equal letters, so take a window of the cipher,
list every pair of positions in it holding the same code, and require the plaintext to repeat at exactly those
offsets. Checked over 1,161,303 letters of Kiewning with one bitmask per gap (`hunt.py`).

Calibrated by planting the true plaintext in the corpus and enciphering it with a random key:

| | windows hitting the true position | false positives |
|---|---|---|
| synthetic, clean transcription | 253 / 254 | 0 |
| synthetic, 1.7 % digit noise | **16 / 254** | 0 |

So at the real noise level about 6 % of windows still give an exact hit, with no false positives at all. Then:

| record | width 2 | width 3 | width 4 |
|---|---|---|---|
| R286 | 0 / 266 | 1 / 261 | 0 / 256 |
| R292 | 0 / 460 | 0 / 456 | 0 / 452 |
| R306 | 0 / 710 | 2 / 705 | 0 / 700 |
| R311 | 0 / 510 | 1 / 505 | 0 / 500 |

The four apparent width-3 hits are artefacts: every one lands in the edition's index of Roman numerals
(`XIUXXUXXUIXXUIIXXUIII…` at corpus position ~1,137,400), a degenerate stretch where any repeat pattern matches.
Genuine hits: **none**, anywhere.

Expected under the hypothesis: with ~130 windows per record per phase and a 6 % per-window hit rate, a real
fixed-width encipherment of printed text should have produced of the order of eight zero-false-positive hits on
R286 alone. Observing none puts the probability at roughly e⁻⁸.

**5. What the cipher IS: deterministic code groups, not homophones.**
Every test so far is negative. This one is positive, and it constrains the system. Count repeated digit
substrings across all 28 ciphertexts (112,805 digits) against an independent control with the same digit
frequencies:

| substring length | repeats in the cipher | iid control | ratio |
|---|---|---|---|
| 4 | 105,170 | 102,865 | 1.0× |
| 6 | 64,083 | 9,590 | 6.7× |
| 8 | 28,519 | 91 | 313× |
| 10 | 12,109 | 1 | 12,000× |
| 16 | 966 | 0 | — |
| 24 | 39 | 0 | — |

Thirty-nine repeated twenty-four-digit strings where chance gives none. **A well-made homophonic cipher cannot
do this** — homophones exist precisely to destroy repetition. This is the signature of a code or nomenclator in
which a given word or syllable is written the same way every time. It also explains why every homophonic attack
above failed, and why no phase preference shows: deterministic groups of *varying length*.

Segmenting the corpus by BPE gives 266 token types over 44,816 tokens, mean 2.5 digits per token, lengths
spread over 1–7 — syllable-scale, and not a fixed width.

**6. Two more hypotheses ruled out.**

* *Polyphonic, one digit per letter.* The repeat spectrum of R286 matches the crib's at roughly 1:1 (3,570
  digits against 3,359 letters), which would mean one digit per letter — impossible for 21 letters over 10
  digits unless the cipher is polyphonic, each digit standing for several letters. Then *equal letters force
  equal digits*, the reverse of every test above. Longest consistent letter→digit run: **17 letters**, against
  shuffled controls of 18, 19, 18. Chance.
* *BPE tokens as word codes.* Encipherment preserves order, so a repeated token should land on the same
  plaintext word each time. Token types whose occurrences share a common word: 16 of 74, against shuffled
  controls of 13, 12, 13. Not significant.

**A correction.** Earlier I reported the absence of phase preference at widths two and three as evidence against
fixed-width codes. That reading was too strong: at the observed ~1.7 % digit error a 3,570-digit document
carries ~60 slips, each flipping the phase for the rest of the line, which would wash out a genuine phase signal
on its own. The phase test is inconclusive. The sound version of that claim is the corpus search in §4, which is
calibrated against exactly this noise.

**7. A far better crib source, which I should have found first.**
DECODE's transcriptions carry `<CLEARTEXT>` and `<PLAINTEXT>` annotations, and I had only skimmed the head of
R286. Across the 28 files there are **~640 clear-text annotations** and, in five records, `<PLAINTEXT>` lines —
DECODE's mark for *a decipherment written on the document itself*:

| record | clear-text marks | on-page decipherment |
|---|---|---|
| R298 | 68 | |
| R296 | 63 | |
| R305 | 54 | In un lungo discorso |
| R307 | 53 | |
| R292 | 51 | |
| R301 | 40 | |
| R309 | 35 | Con l'ord(ina)rio passato intendo che fu scritto da S. M.tà à … |
| R308 | 22 | restati più contenti della risolutione |
| R313 | 14 | Nel particolare |
| R286 | 4 | (struck-out) … la risposta |

This reframes the target. Most of these despatches are **mixed letters**: short ciphered runs embedded in clear
Italian, sentence by sentence — not wholly enciphered texts. R308 reads, in the manuscript,

> `Non sono` · **369092022550852359029255082700852173166 2 8** · `circa il particolare de` · **6680650 …**

with the contemporary decipherer's gloss written above the figures: *restati più contenti della risolutione*.
That is an exact crib with known boundaries, in the right register, and it is not in Kiewning at all. It also
explains why the Kiewning crib could never have worked for records like this one: the ciphered passage is a
clause, not a despatch.

**What the R308 crib says.** 41 digits for 34 letters. Verified against DECODE's own 1523 × 2088 scan
(`img/dec_R308.png`): the digits are as transcribed and the gloss is as read. Exhaustively searched, with both
the two-way constraint (deterministic code, no homophones — what §5 implies) and the one-way constraint:

| model | result |
|---|---|
| fixed width 1, 2 or 3 | no fit (41 is not divisible by 2) |
| deterministic letter code, groups of 1–2 digits | 0 solutions (exact, `exact.py`) |
| deterministic letter code, groups of 1–3 digits | 0 solutions (exact) |
| 2-digit groups, syllables of 1–3 letters, two-way | 0 solutions (exhaustive, 4.0 M nodes) |
| 2-digit groups, syllables of 1–3 letters, homophones allowed | 0 solutions (exhaustive, 7.3 M nodes) |

So either the gloss does not align exactly to that run — the decipherer may have glossed only part of it, or run
on into the next — or the system is more complex than any of these. This is where the work stands.

**Where that leaves it.** Transcription noise is no longer a sufficient explanation. On this evidence
**the ciphertexts are not fixed-width (2, 3 or 4 digit) substitutions of any text printed in Kiewning's 1629
volume** — not of Nr. 153, and not of any other despatch in it. Two possibilities survive, and they are now the
whole question:

1. The system is **not fixed-width** — a nomenclator with variable-length groups, in which no fixed-width
   alignment can ever match however good the transcription. The absence of any phase preference at widths two
   and three points the same way.
2. The sheets encipher **text that is not in the edition**: Kiewning prints the substance in Italian but
   summarises the rest in German regesta, and those passages exist nowhere in print.

The repeat spectrum in §5 makes the first the strong favourite: deterministic, variable-length groups are
exactly what produces 39 repeated 24-digit strings. And the second is entirely live, because the clear pages of
the volume do **not** contain the ciphered passage — pp. 3–4 and 7–9 run continuously *through* the cipher sheet
— so the Italian of what pp. 5–6 encipher may survive only in ASV, Nunz. di Germania 119, which is not
digitised. If so, no work on this crib can succeed, however good the transcription or the solver. The contents of the despatches are unaffected by any of this — they rest
on Kiewning and on the register's own clear pages, not on any decipherment made here.

**The concrete next step**, and the reason this is worth returning to: DECODE's 1491 × 2066 scans are good enough
for a careful transcription, and the plaintext of every passage is already known from Kiewning. A transcription
of one sheet at better than 0.5 % digit error would settle it either way. Doing that by eye is slow and my own
attempt was not clearly better than DECODE's; the repository's existing approach for this — glyph segmentation
and clustering, as used for the Sormano and Gramont leaves — is the tool to build.

## Files

* `decode/R286.txt` … `R313.txt` — DECODE's 2019–20 digit transcriptions (28 ciphertexts).
* `decode_records.txt` — DECODE record → DigiVatLib page range, date, length.
* `ed/pallotto_bd2_1629.txt` — Kiewning 1897, Band 2 (1629), full OCR text from archive.org.
* `crib153.txt` — hand-corrected Italian text of Nr. 153 (4 Aug 1629), 3,359 letters, used as the crib.
* `solve.py`, `align2.py`, `align3.py`, `align4.py`, `soft.py`, `walk.py`, `syll.py` — the aligners tried.
* `hill2.py`, `it_clean5.npy/.json` — the space-free Italian 5-gram model and the annealing solver.
* `manifest.json` — the DigiVatLib IIIF manifest. Images are git-ignored (`img/`).

## Next

The sibling volume, **BAV Barb.lat. 6956** (catalogue entry 236, DECODE R215-R318, seventy ciphered
sheets of the same nunciature for 1628), was broken by Biermann and Bosbach in 2018 (key on DECODE R215); see the
update at the top. Open here: the ~1,750 three-digit groups of 6960 missing from that key. Kiewning's **Band 1, Nuntiatur des Pallotto 1628**
(Berlin 1895) covers exactly those months and is the first place to look. Not checked here.

**23 Oct 2026, verification 5 (plain bar; research/reading_audit/VERIFY5_BRIEF.md)**: '## Reading' headings added after the header rule of texts/R294, R295, R299, R303 and R308_reading.md (the sweep had scored the English headers with the bodies): bodies plain 0.806-1.0, explicit 0.833-1.0. Rescored with research/reading_audit/v2_score.py (plain word-list share and explicit-hole share); both figures are in each entry's reading_review note. Keeps read.

## Remaining gaps

- R291 (11 Aug, Nr. 157), read in part - blocker: no-key-material; groups 750, 405, 796, 573, 557, 690, 697, 762, 279, 440, 966, 239, 469 and some garbled letter stretches; Kiewning has a regest only; the sheet breaks off at p. 4
- R300 (25 Aug, Nr. 165), read in part - blocker: illegible; p. 2 (never transcribed by DECODE) has 3/5/9, 2/7, 6/8 not separable on the scan; p. 1 has single-group holes
- R301 (25 Aug, Nr. 166), read in part - blocker: no-key-material; single groups and unresolved stretches; right edge of p. 2 cut on the scan; continuation (register p. 78) not among the DECODE images (needs-physical-access)
- R302 (28 Aug, Nr. 167), read in part - blocker: no-key-material; the Conti/Duca di Poli paragraph has many unidentified groups and one line of regest
- R304 (28 Aug, Nr. 168), read in part - blocker: no-key-material; first paragraph's middle and the "requisito consensu" formula; not every break checked on the scan yet (workable)
- R313 (29 Sept, Nr. 185), read in part - blocker: no-key-material; groups 964, 209, 644, 665, 932, 552, 936; the struck clear paragraph on p. 2 read only at its frame
- Read sheets keep scattered open groups (listed in each texts/R*_reread_log.md) - blocker: no-key-material
- R286-R290, R292-R299, R303, R305-R312: closed 22 Oct 2026 (read, texts/R*_reading.md); R286 English translation written

## Escalation

- [x] siblings: the whole 6960 series read together; groups learnt across all 28 sheets; Barb.lat. 6956 key used
- [x] clear pages: clear words re-read on the DECODE scans for every sheet
- [x] known keys: 6956 key (Biermann/Bosbach, DECODE R215), extended by 125 groups
- [x] print: Kiewning 1897 (Nuntiaturberichte IV/2) aligned with every sheet
- [x] key rebuild: nomenclator groups learnt from the print alignments and contexts
- [ ] retry: R304 scan check of every break; groups open across the series could be fixed from Kiewning Bd. 1 (1628) and the 6956 sheets
