# lewenhaupt1706: Charles XII to Adam Ludvig Lewenhaupt, Jan-Mar 1706 (Uppsala UB, F 470), three-figure "class A" cipher

Contributed by Brice Dudout (agents: Claude Opus 5.5), 17 Nov 2026. New target, not in the catalogue.

**Status: read in part.** The key was rebuilt from the decipherments of the time and frozen; it is **not validated at
the programme's bar**. One pre-registered measurement on an unseen letter passed an absolute threshold of 0.60, not
the programme's 0.85. Order: the first measurement (v1, another letter, another metric) failed; the metric and the
0.60 threshold of v2 were then chosen, after K2's decodes of its own fitting letters had been seen, and written into
`protocol/PREREG-v2.md`, hashed before the measurement (`protocol/PREREG-v2.sha256`). The two letters without a decipherment of the time are read at **73.7% and 76.4% of
their words, sure words only** (cipher words; measured on our copy, 18 Nov 2026), below the 95% bar; with probable words
84.2% and 82.1%. The gloss of the time of letter 108 (1707) confirms 80 values of the key and gives four more (section
"Letters 108 and 119", 18 Nov 2026); a measurement on letter 119 failed.

## Source

- Uppsala University Library, **F 470** (Alvin record 634917): "Coll. Mss. Regis Gustavi III:ii vol. 60, Äldre svenska
  originalhandlingar T. II 1703-1707", fols. 1-279. Alvin images, full-resolution TIFF. The images were used for study
  only and are neither attached nor reproduced here; image numbers below are Alvin's.
- Letters of Charles XII from his field chancery to General Adam Ludvig Lewenhaupt (Riga), 1706. Several letters were
  sent in two or three copies ("Doublet") enciphered with different homophones, which is what allowed the alignment.

| letter | date, place | images | copies | help of the time |
|---|---|---|---|---|
| L1 | 21 Jan 1706, Schalabova near Grodno | 286-287, 289-290, 292-293 | 3 | full decipherment on 293 (right page); gloss on 286 l. 1; 292-293 partly in clear |
| L2 | 19 Feb 1706, Zaludek | 295-297, 298-299 | 2 (298-299 carry the same groups) | word-by-word interlinear gloss on 295-297 |
| L3 | 21 Feb 1706, Saludek (no. 87, "Riga prod. d. 6 marty 1706") | 301-303, 306-308 | 2 (same groups, copied, not re-enciphered) | none |
| L4 | 2 Mar 1706 (no. 89, "Prod. d. 13 marty 1706") | 310-311 | 1 | none |

A second system ("class C", two-figure, Dec 1704-Jan 1705, images 179-206) is a different table; a partial table from
the glosses on 182 and 188 is in `readings/classC_partial_table.md` (19 of about 22 codes; 206 not reread). The class C
letters are not part of this target and are not listed among its gaps.

## System

Swedish nomenclator with homophones, numbers 1 to about 810, in alphabetical order: 1-99 letters (two series, the second
= first + 35) and a few digraphs (ch, ll, sk, st); 85-227 syllable blocks consonant + vowel by fives (c 85-89, d 90-94,
f 95-99, k 148-152, l 153-157, m 158-162, n 163-167, r 173-177; second series k 183-187 ... w 223-227); 400-810 words and
names in alphabetical order (433 af, 452 armée, 516 Eder, 537 fiende, 542 för, 605 med, 619 och, 663 som, 669 til,
678 wår); nulls (3, 82). Clear words are interspersed. This matches Carlson's description (1893, introduction) of the
"tresiffrig tabellchiffer" in Charles XII's letters to Rehnsköld deciphered by R. Torpadie.

## Prior work

- No printed edition of the F 470 letters found. Carlson, *Konung Karl XII:s egenhändiga bref* (1893), has no letter to
  Lewenhaupt. Uddgren, *Karolinen Adam Ludvig Lewenhaupt* II (1950), quotes the king's orders of 21 Jan and 19 Feb 1706
  (and 11 Aug 1705) in clear from the **Riksregistraturet** (registered copies, Riksarkivet), and says nothing of a
  reading of this cipher; for 1704 he notes that Lewenhaupt lacked the key.
- **Not checked:** whether the Riksregistraturet 1706 holds the clear texts of **21 Feb (L3) and 2 Mar 1706 (L4)**.
  sok.riksarkivet.se answered with an anti-robot check, which we do not pass; no volume was consulted. If those copies
  exist, L3 and L4 are not first readings.
- L1 and L2 are read by the decipherment and gloss of the time; we used them as key material, not as new readings.
  Part of L3 (passage 2) recalls L1.
- Repository (17 Nov 2026, origin/main d19e4dba3): no target, catalogue entry, lead, issue or pull request mentions
  Lewenhaupt, F 470 or Alvin 634917. The stade1710 key (Charles XII, 1710) is a different table: 0 of 131 shared codes
  have the same value.

## Protocol and measurements

Rules: portion held out and frozen by SHA-256 before any key work on it; key frozen by SHA-256 before the measurement;
one measurement against 200 controls, thresholds written beforehand; a measured portion is burned. Two measurements
were made, each on a different letter.

### v1, held-out L4: failed (`protocol/PREREG-v1.md`, `protocol/MEASURE-v1.json`)
- Key K (`key/key_K_v1.json`, 176 codes) fitted on L1 and L2; L4 (292 groups, two transcription passes) held out.
- Metric: lexical coverage by a word list (`corpus/Lx.txt`). Result S = 0.723 against permuted keys mean 0.677,
  max 0.790; thresholds 0.85 and max + 0.30: **failed**. Cause: the word list has many short words and covers random
  strings at about 68%; also 18% of L4's groups were missing from K. L4 is burned and was used afterwards as key
  material only.

### v2, held-out L3: passed a lowered threshold, not validated at the programme's bar (`protocol/PREREG-v2.md`, `protocol/MEASURE-v2.json`)
- L3 copy A (301-303, 780 groups) transcribed and frozen before any change to the key (SHA fd85444f...); copy B
  (306-308) read separately as the second pass; 5 differences settled on the TIFF (`transcription/L3_ARBITRAGE.md`).
- Key K2 (`key/key_K2_frozen.json`, 218 codes, SHA faf24a30...) fitted on L1, L2 (with 297 and the glosses) and the
  burned L4, never on L3; changes listed in `protocol/K2_changes.tsv`.
- Metric: letter 5-gram model (`tools/ngram.py`) trained on Carlson 1893 and Swedish Wikisource pages in old spelling
  (`corpus/corpus_train.txt`, one block in ten held out). N = (L - U) / (R - U): about 1 for genuine Swedish of the
  period, about -2.5 for uniform random letters.
- Calibration (on L1, L2, L4, the corpus and random strings, never on L3): the clear decipherment of the time of L1 scores
  0.987; with 2% of its letters replaced at random 0.83; with 5% 0.65 (min 0.45); with 10% 0.36. K2's decodes of its own
  fitting letters score 0.68-0.88; 1,000 permuted keys never reached 0.37.
- **Order of the steps.** The metric and the threshold of v2 were set **after** the v1 failure and **after** K2's decodes
  of its own fitting letters (0.68-0.88, above) had been seen; they were not fixed before any result was known.
- **Frozen before the measurement:** `protocol/PREREG-v2.sha256` = `16cd415569738998c5542d02acc211055165c686c5cdf8fdc672eb13e124dfa0`,
  the SHA-256 of the filed `protocol/PREREG-v2.md` (which carries the SHA-256 of the L3 transcription, fd85444f..., and of
  K2, faf24a30...). By the file times of our working copy it was written on 17 Nov 2026 at 00:49:19 UTC, 12 s before
  `MEASURE-v2.json` (00:49:31 UTC); these are local file times, not a third-party timestamp, and no commit precedes the
  measurement (the first commit is 3f62ef11c). `protocol/PREREG-v2.part1.sha256` (`4ed5060f...`, 00:37:48 UTC) is the
  hash of an earlier text of the file, not of the filed one.
- **Deviation from the programme's bar, declared before the measurement:** absolute threshold **0.60 instead of 0.85**. On
  this scale 0.85 means genuine text with at most about 2% wrong letters, which even K2's own fitting letters do not
  all reach (names, foreign words); 0.60 corresponds to about 5% wrong letters. The margin over the best control
  (+0.30) is the default one.
- **Result: N(K2, L3) = 0.695; 200 permuted keys mean 0.057, max 0.294; thresholds 0.60 and 0.594: passed.** It clears
  the lowered absolute threshold and the default margin; it does **not** reach the programme's 0.85, so the key is
  **not validated at the programme's bar**. Informative only: 200
  shuffles of the group order max 0.008; 10.6% of L3's groups unknown to K2; word coverage 0.50 against controls max
  0.56 (the lexical metric does not separate, as in v1).
- `rerun.sh` reruns the v2 measurement from the files as filed here and gives the same figures (checked 17 Nov 2026).
- No fresh portion of this series is left in F 470: L1-L4 are all used or burned. Letter 119 (1707), measured on
  18 Nov 2026 with the table from letter 108 (v3, below), is burned too.

## Reading (after the measurement, outside the protocol)

- Key K3 (`key/key_K3_after_measure.json`, 244 codes) = K2 plus about 30 values taken from L3 and the
  context (509 den, 680 wäl, 199 ne, 652 samma, 597 magasin, 721 Lifland, 744 Riga, 548 garnison, ...). Not validated
  by a measurement.
- Key K4 (`key/key_K4_with_gloss108.json`, `key.tsv`, 256 codes, 18 Nov 2026) = K3 plus 12 sure values read in the
  gloss of the time of letter 108 (below). The decryption files and `validation.tsv` are regenerated with K4
  (`python3 -I tools/make_texts.py key/key_K4_with_gloss108.json`).
- Decryptions: `L3_21feb1706_decryption.txt`, `L4_2mar1706_decryption.txt` (`tools/make_texts.py`). Readings in Swedish
  (`readings/*_reading_sv.txt`) and English (`readings/*_translation_en.md`). Marks: plain = sure, {word} = probable,
  [word] = supplied, ‹…› = unread; a word with an unread part counts as unread.
- Word counts, measured on our copy (counted mechanically from the reading files, 18 Nov 2026, after the K4 values).
  The read share follows the rule of 16 Nov 2026 (PR #728): cipher words only, and only sure words count as read;
  probable, supplied and unread words are holes. A word counts as sure only when it reads as sense in its sentence
  (read by the sense), not because its groups have values.

| letter | words | sure | probable {x} | supplied [x] | unread ‹…› | **sure (read share)** | sure + probable (not the bar) | state |
|---|---|---|---|---|---|---|---|---|
| L3, 21 Feb 1706 | 323 | 238 | 34 | 1 | 50 | **73.7%** | 84.2% | read in part |
| L4, 2 Mar 1706 | 123 | 94 | 7 | 0 | 22 | **76.4%** | 82.1% | read in part |
| together | 446 | 332 | 41 | 1 | 72 | **74.4%** | 83.6% | read in part |

  On 17 Nov (K3) the counts were L3 234 sure / 54 unread (72.4%), L4 90 / 26 (73.2%); the 8 new sure words are
  520 eller (twice) "eller och" = "or else", 557 han, 629 parti in L3, and 629 partiet (twice), 629 parti, 544 fram in L4.
- Cipher groups given a value by K4: L3 749 of 780, L4 282 of 292 (1,031 of 1,072); many valued groups still do
  not join into words, so the share of words read is the figure that counts.
- Content: L3 answers Lewenhaupt's letters of 24 Nov, 7 Dec, 13 and 26 Jan on the disorder in Livonia: if the Muscovites
  withdraw from Courland and Samogitia, he is to march into Courland with his troops and battalions of the Riga and
  Pernau garrisons, then join the army or turn to Polish Livonia; the small magazine at Riga will not last; the king
  recalls his letter of 21 Jan (Grodno passed, part of the enemy shut in, almost cut off from Lithuania) and orders a
  push into Courland and a detachment into Samogitia to drive the enemy out. L4 reports a detachment sent towards Sadowa
  that found the enemy, Russian artillery with Wiśniowiecki and Ogiński and the Lithuanian troops, a march towards
  Vilna, and expects Lewenhaupt to be on the march towards Lithuania.
- Doubtful values: 154 (le/lu), 96 (fe; L1 Grodno wants g), 174 (re/ra), 614, 661, 522; names 721, 744, 738
  set from the context and the alphabetical order. (629 and 520, doubtful on 17 Nov, are now glossed in letter 108.)
- Copy variants in L3: 109/103, 45/75 (B's 75 = u, "undfått", is right), 676/776.
- The standard statistical check (`docs/_validate.py`) could not run on 17 Nov 2026: the sv-gutenberg corpus download
  returned HTTP 503. `validation.tsv` (K3 values per group, L3 then L4) is filed for it.

## Letters 108 and 119 (1707), 18 Nov 2026

Two later letters of Charles XII to Lewenhaupt in F 470 use the same table. Files: `protocol/PREREG-v3-letter119.md`
(written and hashed before any transcription, `protocol/PREREG-v3.sha256`; in French, like the v1 and v2 files),
`protocol/FROZEN-v3.sha256` (the transcriptions, T108 and the result, under their working names), `tools/v3/`.

- **Letter 108** (Altranstädt, 5 Jan 1707, images 366-367): every cipher group carries a word-by-word interlinear
  gloss of the time. It is therefore **read from an existing decipherment** (EXISTING), not a new reading, and it is
  not counted in the figures above. Groups and glosses: `transcription/L108_5jan1707_366_367_gloss.txt` (one passage
  struck out by the encipherer, not counted). Table T108 (`protocol/T108_gloss_letter108.tsv`, `.json`), built from
  the glosses alone, with no value taken from K2 or K3 (K2 was seen during the prior-art check; declared in the
  PREREG): 101 codes, 94 sure, 7 doubtful.
- **Confirmation of the key.** T108 shares 86 codes with K3: **80 have the same value**, and the 6 others differ in
  spelling only: 23 m / mm, 36 s / ß, 225 wij / wi, 556 hafwe / hafwer, 669 til / till, 10 ch / x? (the gloss of 10 is
  doubtful; "hemsöcht" in 108 wants ch). This is an independent check, by a decipherment of the time, of values K2 and
  K3 had set from L1, L2 and the context.
- **Four codes of K3 that were open** are glossed in 108, all sure: **520 = eller, 629 = parti, 544 = fram,
  557 = han**. They read 8 more words in L3 and L4 (table above). Other new sure values, which do not occur in L3 or
  L4: 38 str, 84 bu, 98 fö, 511 det, 543 först, 593 läger, 634 proviant, 668 straxt (all in K4).
- **Doubtful, not used:** 10 (x?, ch by the sense), 90 (da / dä), 105 (ha / hå), 106 (glossed "fr", but "hemligit",
  "hemsöcht" in 108 and "förnödenhet", "nödwändighet" in 119 want he; found after the measurement), 143 (hw?), and
  85 (glossed la, once, against the alphabetical block c 85-89 where 87 is ci and 88 co; left out of K4). 160 (mi?)
  and 575 (icke?) are doubtful glosses that agree with K3.
- **Letter 119** (Altranstädt, 30 Apr 1707, images 397, 399, 400; addressed "Till Gen. och Gouverneuren Graf Adam
  Lejonhufvud"), no gloss: held out, its 421 groups transcribed and frozen (SHA-256 9dbce6a8...) before T108 was
  applied. **One pre-registered measurement (v3), failed:** T108 alone, words read by the sense in one pass,
  152 words: 50 sure, 16 probable, 64 supplied, 22 unread; P = (sure + probable) / words = **0.434 against the
  threshold 0.60** fixed beforehand (`protocol/MEASURE-v3-letter119.json`, `protocol/H119_reading_measure.tsv`).
  Mechanical coverage 61.8%. Cause: 119 uses mostly the other homophones (39 a, 108 t, 59 n, 67 r, 47 e, 125 de,
  53 i, 68 s), which do not occur in 108. The measurement does not test K3. **Letter 119 is burned.**
- Letter 119 is therefore **not counted as read**: only a partial reading outside the measurement exists (the
  measurement file above; with supplied words 85.5%, but the supplied values rest partly on the series A key). It is
  not filed as a reading here and is not a document of this target.
- No fresh portion of this cipher is left in F 470 for a further measurement.

## Remaining gaps
- L3, 50 unread words (code groups 614, 616, 522, 661, 571, 240, 262, 282, 405, 454, 638, 738 and undivided letter runs) - blocker: open-codes; most occur once or twice, no decipherment of the time for this letter, and the gloss of letter 108 does not cover them
- L4, 22 unread words (codes 681, 580, 233, 376 and undivided runs) - blocker: open-codes; single copy, no gloss, not covered by the gloss of letter 108
- Riksregistraturet 1706 copies of 21 Feb and 2 Mar 1706 - blocker: needs-physical-access; the Riksarkivet search answers with an anti-robot check, which we do not pass

## Escalation
- [x] siblings: all class A letters of F 470 used (L1-L4, both copies of L2 and L3); class C letters looked at (different table); 1707 letters 108 (glossed, used for the key) and 119 (measured, failed) added on 18 Nov 2026
- [x] clear-pages: 293 right page is the decipherment of L1, 295-297 carry an interlinear gloss of L2; both used for the key
- [x] known-keys: stade1710 (Charles XII, 1710) compared, 0 of 131 shared codes agree; no Swedish key of 1700-1730 is held in the repository (SE/RA/202/5 not online to us)
- [x] print: Carlson 1893 (no letter to Lewenhaupt), Uddgren 1950 (orders of 21 Jan and 19 Feb 1706 quoted in clear from the Riksregistraturet; 21 Feb and 2 Mar not found there by keyword); Riksregistraturet itself not consulted
- [x] key-rebuild: key extended by the alphabetical bracketing of the nomenclator and the context (K3, +26 codes)
- [x] retry: every unread group of L3 and L4 rerun with K3 and regraded
- [ ] Riksregistraturet 1706: to be checked by a person (anti-robot check)

## Credits
- Decipherment of the time of L1 (image 293) and the gloss of L2 (295-297): the Swedish chancery or Lewenhaupt's
  secretary, 1706 (key material). Interlinear gloss of letter 108 (366-367), 1707: the same hand or office (key
  material, 18 Nov 2026).
- Images: Uppsala University Library (Alvin).
- Pointers: Carlson 1893 (system description, corpus), Uddgren 1950 (Riksregistraturet).
- Transcription, key, measurements and readings: Brice Dudout's agents (Claude Opus 5.5), 17 and 18 Nov 2026.
