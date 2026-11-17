# lewenhaupt1706: Charles XII to Adam Ludvig Lewenhaupt, Jan-Mar 1706 (Uppsala UB, F 470), three-figure "class A" cipher

Contributed by Brice Dudout (agents: Claude Opus 5.5), 17 Nov 2026. New target, not in the catalogue.

**Status: read in part.** The key was rebuilt from the decipherments of the time, frozen, and passed one
pre-registered measurement on an unseen letter **with a reserve**: the absolute threshold was set at 0.60 instead of
the default 0.85 (declared, with its calibration, before the measurement). An earlier measurement on another letter,
with a different metric, failed. The two letters without a decipherment of the time are read at 83% and 79% of words
(sure + probable), below the 95% bar.

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
the glosses on 182 and 188 is in `readings/classC_partial_table.md` (19 of about 22 codes; 206 not reread).

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

### v2, held-out L3: passed with a reserve (`protocol/PREREG-v2.md`, `protocol/MEASURE-v2.json`)
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
- **Deviation from the default bar, declared before the measurement:** absolute threshold **0.60 instead of 0.85**. On
  this scale 0.85 means genuine text with at most about 2% wrong letters, which even K2's own fitting letters do not
  all reach (names, foreign words); 0.60 corresponds to about 5% wrong letters. The margin over the best control
  (+0.30) is the default one.
- **Result: N(K2, L3) = 0.695; 200 permuted keys mean 0.057, max 0.294; thresholds 0.60 and 0.594: passed.** It clears
  the lowered absolute threshold and the default margin; it does **not** reach the default 0.85. Informative only: 200
  shuffles of the group order max 0.008; 10.6% of L3's groups unknown to K2; word coverage 0.50 against controls max
  0.56 (the lexical metric does not separate, as in v1).
- `rerun.sh` reruns the v2 measurement from the files as filed here and gives the same figures (checked 17 Nov 2026).
- No fresh portion of this cipher is left in F 470: L1-L4 are all used or burned.

## Reading (after the measurement, outside the protocol)

- Key K3 (`key/key_K3_after_measure.json`, `key.tsv`, 244 codes) = K2 plus about 30 values taken from L3 and the
  context (509 den, 680 wäl, 199 ne, 652 samma, 597 magasin, 721 Lifland, 744 Riga, 548 garnison, ...). Not validated
  by a measurement.
- Decryptions: `L3_21feb1706_decryption.txt`, `L4_2mar1706_decryption.txt` (`tools/make_texts.py`). Readings in Swedish
  (`readings/*_reading_sv.txt`) and English (`readings/*_translation_en.md`). Marks: plain = sure, {word} = probable,
  [word] = supplied, ‹…› = unread; a word with an unread part counts as unread.
- Word counts (counted mechanically from the reading files):

| letter | words | sure | probable | supplied | unread | sure | sure + probable | state |
|---|---|---|---|---|---|---|---|---|
| L3, 21 Feb 1706 | 323 | 234 | 34 | 1 | 54 | 72.4% | 83.0% | read in part |
| L4, 2 Mar 1706 | 123 | 90 | 7 | 0 | 26 | 73.2% | 78.9% | read in part |

- Cipher groups given a value by K3: L3 745 of 780, L4 278 of 292 (1,023 of 1,072, 95.4%); many valued groups still do
  not join into words, so the share of words read is the figure that counts.
- Content: L3 answers Lewenhaupt's letters of 24 Nov, 7 Dec, 13 and 26 Jan on the disorder in Livonia: if the Muscovites
  withdraw from Courland and Samogitia, he is to march into Courland with his troops and battalions of the Riga and
  Pernau garrisons, then join the army or turn to Polish Livonia; the small magazine at Riga will not last; the king
  recalls his letter of 21 Jan (Grodno passed, part of the enemy shut in, almost cut off from Lithuania) and orders a
  push into Courland and a detachment into Samogitia to drive the enemy out. L4 reports a detachment sent towards Sadowa
  that found the enemy, Russian artillery with Wiśniowiecki and Ogiński and the Lithuanian troops, a march towards
  Vilna, and expects Lewenhaupt to be on the march towards Lithuania.
- Doubtful values: 154 (le/lu), 96 (fe; L1 Grodno wants g), 174 (re/ra), 614, 629, 661, 520/522; names 721, 744, 738
  set from the context and the alphabetical order.
- Copy variants in L3: 109/103, 45/75 (B's 75 = u, "undfått", is right), 676/776.
- The standard statistical check (`docs/_validate.py`) could not run on 17 Nov 2026: the sv-gutenberg corpus download
  returned HTTP 503. `validation.tsv` (K3 values per group, L3 then L4) is filed for it.

## Remaining gaps
- L3, 54 unread words (code groups 614, 616, 520, 522, 661, 571, 240, 262, 282, 405, 454, 557, 629, 638, 738 and undivided letter runs) - blocker: open-codes; most occur once or twice, no decipherment of the time for this letter
- L4, 26 unread words (codes 629, 681, 544, 580, 233, 376 and undivided runs) - blocker: open-codes; single copy, no gloss
- Riksregistraturet 1706 copies of 21 Feb and 2 Mar 1706 - blocker: needs-physical-access; the Riksarkivet search answers with an anti-robot check, which we do not pass
- class C letters, images 179-206 (two-figure table, 1704-1705) - blocker: not-attempted; partial table only, 206 not reread

## Escalation
- [x] siblings: all class A letters of F 470 used (L1-L4, both copies of L2 and L3); class C letters looked at (different table)
- [x] clear-pages: 293 right page is the decipherment of L1, 295-297 carry an interlinear gloss of L2; both used for the key
- [x] known-keys: stade1710 (Charles XII, 1710) compared, 0 of 131 shared codes agree; no Swedish key of 1700-1730 is held in the repository (SE/RA/202/5 not online to us)
- [x] print: Carlson 1893 (no letter to Lewenhaupt), Uddgren 1950 (orders of 21 Jan and 19 Feb 1706 quoted in clear from the Riksregistraturet; 21 Feb and 2 Mar not found there by keyword); Riksregistraturet itself not consulted
- [x] key-rebuild: key extended by the alphabetical bracketing of the nomenclator and the context (K3, +26 codes)
- [x] retry: every unread group of L3 and L4 rerun with K3 and regraded
- [ ] Riksregistraturet 1706: to be checked by a person (anti-robot check)

## Credits
- Decipherment of the time of L1 (image 293) and the gloss of L2 (295-297): the Swedish chancery or Lewenhaupt's
  secretary, 1706 (key material).
- Images: Uppsala University Library (Alvin).
- Pointers: Carlson 1893 (system description, corpus), Uddgren 1950 (Riksregistraturet).
- Transcription, key, measurements and readings: Brice Dudout's agents (Claude Opus 5.5), 17 Nov 2026.
