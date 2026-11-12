# fiedmond1779: Fiedmond, governor of Guiana, to the Navy minister, Cayenne, 19 July and 29 August 1779 (ANOM COL C14 51 ff. 5-10 and 16-23; catalogue 1201)

Status: read in part (Brice Dudout, 11 Nov 2026; integrated 12 Nov 2026). Strict read share, by the README read bar (certain words only): f9 with its postscript 508 of 754 cipher words = 67.4%; f16 1,876 of 2,650 = 70.8%; both letters 2,384 of 3,404 = 70.0%. The contributor's count, certain + probable, is 88.5% (f9) and 88.8% (f16). Both are under the 95% rule. Key partial: 70 of the 448 distinct numbers have no value. The extended key passed its one pre-registered held-out test (S = 0.703 against at most 0.644 for 400 controls); the verdict recorded is "weak" (118 groups, margin +0.059, and only 6 of the 59 context-only values occur in the tested portion). See "Integration check (12 Nov 2026)" below.

Contributed by Brice Dudout (Europe chiffrée). Key proposed by Claude Fable 5.2 (Anthropic) in one API run; transcription,
earlier key, held-out validation, word-by-word reading and write-up by Claude Opus 5.5 agents. Catalogue entry **1201**
(Calames/Biblissima/FranceArchives sweep, vetted 3 Nov 2026, verdict "open"). No decipherment of the time is known for these two
letters ("pièce chiffrée non traduite", "passage chiffré non traduit" in the ANOM calendar). No image is included.

## Documents

Aix-en-Provence, Archives nationales d'outre-mer, COL C14 51 (Guiana, correspondence 1779), IREL views:
- **f9** = ff. 5-10, views 009-014: duplicate ("Dup.ta") of a letter of Jacau de Fiedmond to the minister, headed in clear
  "Approvisionnement et troupes" and dated in clear **"Du 19 juillet 1779"**, with a postscript (view 014 left, lines 11-18).
  Ciphered summary, then cipher with long clear passages (Mingy, Desprez, Rochin, M. Baron, the chevalier de Besner, La Serre).
  1,556 groups. *Catalogue correction*: entry 1201 dates f9 "13 Jul 1779"; the letter is dated 19 July in clear; "le 13 de ce
  mois" in its first sentence is the arrival of the convoy.
- **f16** = ff. 16-23, views 018-025: letter of 29 August 1779 (pencil "Guyane 1779"; "vingt" struck out), signed Fiedmond,
  "Deffence de la colonie". Ciphered title and summary of ten heads, repeated as underlined headings in the body. 5,277 groups.
  The cipher runs to view 025 (not 023).

## System and key (`key.tsv`, CC BY 4.0)

A French numerical nomenclator with numbers from 5 to 888 (448 distinct in the two letters; "about 1-800" in the PR; corrected
12 Nov 2026: 800, 801, 851 and 888 occur), mixed (no alphabetical order in either half): letters (404 s, 505 r,
10 l, 30 e, 604 n, 785 t), syllables (734 ti, 347 on, 301 re, 333 te, 277 ne, 744 ment, 232 tion) and words (600 de, 72 la,
25 le/les, 575 pour, 233 colonie, 642 artillerie, 247 ouvrages, 18 hommes, 134 Monseigneur, 149 isle, 798 Cayenne), probably a
few homophones; the end of a word is often left unenciphered (297 nécessaire/nécessité, 42 peut/peu). 448 distinct numbers in
f9 + f16. It is **not** the Guiana code of 1757-62 (`targets/orvilliers1759/dudout/key.tsv`, numbers up to about 500: tested,
does not fit) nor Bouillé's Martinique codes of 1778-79; it is the same code in 1779 and 1780.

The key was learned in two steps:
1. **K-Guy1780b** (29 Oct 2026, 401 values): aligned on two pairs of the time in the same series: the cipher letter C14 51
   ff. 102-111 (no. 44, 1 Sep 1779) with its clear copy ff. 98-101, and C14 52 ff. 15-16 (29 Apr 1780) with its "Déchiffrement"
   ff. 17-19v.
2. **K-Guy1780c** (11 Nov 2026, 454 entries): proposed by Claude Fable 5.2 in one API run on f9/f16 (held-out portion removed
   from the copies it was sent), adding corrections and values restored from context, each with a status. Frozen before the
   measurement. `key.tsv` = the frozen file with an English header; `frozen/K-Guy1780c.tsv` = the file byte for byte.

## Validation (`validation.txt`)

K-Guy1780b had failed two held-out tests against clears of the time (0.758/0.647 and 0.805/0.707 under 0.85/0.75, far above
controls) and a third measurement was null. K-Guy1780c was measured **once** on the portion held out since 28 Oct (f9
postscript + last 5 lines of f16, 118 groups), under a protocol hashed before the run: strict lexical reading S = **0.703**
against at most 0.576 (200 permuted keys) and 0.644 (200 length-shuffled keys), rank 1/401, threshold 0.656 calibrated
beforehand on training windows -> PASS. Declared limits: 118 groups (our rule asks for 300 cipher characters or 150 groups; only
the first is met), margin +0.059, a lexical reference rather than a clear of the time, and an incident (the held-out groups were
displayed by a `diff`, not decoded, after the key was frozen). Verdict recorded: **weak**.

## Reading (`reading.md`, `translation.md`, `words_f09.tsv`, `words_f16.tsv`)

Word-by-word count by Daniel's rule (certain + probable only), on real French words; elision joined to its word. The
segmentation is checked by script against the frozen transcription (every group and clear passage used once; a certain word must
equal its key values letter for letter).

| text | words | certain | probable | restored | unresolved | read |
|---|---|---|---|---|---|---|
| f9 + postscript | 754 | 508 | 159 | 63 | 24 | **88.5%** |
| f16 | 2,650 | 1,876 | 477 | 246 | 51 | **88.8%** |

- **Count used on the site (integration, 12 Nov 2026): certain words only, 67.4% (f9) and 70.8% (f16).** The last column of the
  table is the contributor's count (certain + probable); see the integration check for the reason.
- A stricter count, where the 24 (f9) and 56 (f16) words that are probable only because the encipherer left out or doubled a
  letter ("ordnner", "constrire", "boois") are put with the restored words, gives 85.4% and 86.7%.
- The automatic counts of the key proposer (87.6% and 85.8%) were made on mechanical fragments (857 and 3,044 "words"); this
  count replaces them.
- **Value 398**: the key has "ils" (prob); the held-out portion reads [ap]prouvoit and two other places read [ap]prentifs:
  398 is very probably "ap". Other values contradicted by the sense (all counted restored): 461 = ef reads "fe"; 182.633 reads
  "deffence" (bigram rule outside the frozen key; 182 or 183 to be checked on the image); prob values 550, 53, 151, 603, 39, 719,
  790, 250, 608, 578; sure values 303 (in peu-ue-nt), 601 (reads "vaincre" in v024g l07), 525 (in continuée); 338 gives two
  incompatible readings in v024d l05-06.
- **Content.** f9: the convoy under the corvette l'Hirondelle has arrived; orders of the Court carried out imperfectly (gibernes
  forgotten); the repair of the works of the place (to restore their state of 1771) stopped by the abbé Terray and unfinished; no bomb-proof powder magazine; arsenal
  and port without workmen, timber or sailors; one gunboat sent instead of two, two bad apprentices instead of "six good"
  carpenters; gunboats like the one built in 1772 are best; La Serre given the service of the coasts; Desprez, Mingy; artillery
  company to be raised. P.S.: ships bound for the colony should make a recognition signal off the island. f16: report under ten
  heads on the defence of Cayenne island against an expected attack: gunboats and carpenters, powder magazine, artillery,
  recruits (drunkenness, desertion), a critique of the defence memoir of "the author worthy of Monseigneur's confidence"
  (La Serre), the impossibility of guarding every cove (Remontabo, Remire, Mahury), the enemy's likely manoeuvres (landing far
  from the town, the Mahury islet, the Cabassou creek), fire precautions in a wooden town, a retrenchment on the port side,
  retreat of the garrison, resistance "jusqu'à l'impossible" and then in the country after the project of 1762.
- `reading_review` **B** for both texts: read as French sentences by AI agents only; no human has read the reading against the
  images; not re-read blind.

## Integration check (12 Nov 2026)

The PR (#420) was verified independently on 11 Nov 2026 and integrated on 12 Nov 2026. What was checked, and what changed:

- **Counts reproduce.** Key: 454 rows (225 sur, 161 prob, 8 corrige-paire, 6 corrige-contexte, 53 restitue*, 1 irresolu), 453
  usable. Groups: f9 1,556, f16 5,277 (the contributor's tokenizer; the decryption file lists 6,832 group=value pairs), 448
  distinct, lowest 5, highest 888. Transcription hashes match. Word tables: f9 754 = 508 / 159 / 63 / 24; f16 2,650 = 1,876 / 477 /
  246 / 51. A second decoder gives the same value for every group of `decryption.txt` (0 real differences).
- **Which figure is the read share.** The README read bar counts a word only if it is not a hole, not guessed, not supplied, and
  not a code value given by the sense alone. A "probable" word ({x} in `reading.md`) is one that rests on a "prob" or
  "corrige-paire" value, a doubtful group, a chosen word division, or a letter the encipherer left out. 127 of the 159 probable
  words of f9 and 370 of the 477 of f16 contain a "prob" value, and the key's own header rates "prob" values (121 of the 161 have a single
  aligned occurrence in the pairs) right about 55% of the time in cross-validation: such a word is accepted because it makes sense, which
  is what the bar excludes. The strict read share is therefore **certain words only: f9 508/754 = 67.4%, f16 1,876/2,650 = 70.8%,
  both 2,384/3,404 = 70.0%**. The contributor's figure (certain + probable) is 88.5% and 88.8%. `profile.json` carries the
  strict figure (`read_share`, `fraction_read`). The class is read in part under either count.
- **The held-out test** (section Validation) passed its own rule, and the figures re-run: S = 0.695 (82/118) with the repository
  lexicon alone against 0.703 (83/118) with the contributor's lexicon, which adds the words of training clears not in the PR;
  best controls 0.559 / 0.636; rank 1/401; 0 of 2,000 further controls reach it (highest 0.661). It is a weak test of the
  extension: only 8 of the 118 held-out groups carry a context-only value, and these are 6 values (26, 134, 138, 149, 453, 717)
  of the 59 that the key takes from context (53 restored + 6 context-corrected). With the pair-derived values alone S is 0.619.
  The test shows that the code is the right one and that these six values fit a new passage; it does not test the other 53. The
  lexical measure is lenient (the control keys average 0.446 and 0.511 in `frozen/measure_result.txt`).
- **Order of events.** The key freeze at 14:07 CET, the held-out portion fixed on 28 Oct and the `diff` incident are by the
  contributor's record: the PR is a single commit of 11 Nov 2026 21:49 CET, and there is no outside timestamp.
- **Time of the protocol.** `frozen/AVENANT-C09.md` says it was written "à 21 h 20 CET", but the freeze file that hashes it is
  stamped 21:18:04 and the measurement 21:18:10. The text cannot have been written two minutes after it was hashed: "21 h 20" is
  a rounded or mistaken time in the protocol's own header. The frozen file is left as sent (it already differs from its hash by
  the declared removal of storage paths); the order hash -> measurement stands on the two stamped files.
- **Not in the repository (gap).** The two cipher/clear pairs the key was aligned on (C14 51 ff. 102-111 with the clear copy
  ff. 98-101; C14 52 ff. 15-16 with the "Déchiffrement" ff. 17-19v), the earlier key `K-Guy1780b.tsv`, the four training clears
  and the French corpus are not in the PR. So `frozen/measure.py` cannot be run as sent, and the pair-derived values (K-Guy1780b's
  401; 394 of them remain in the frozen key as sur, prob or corrige-paire) **could not be verified from the repository**. They
  carry the whole strict reading. Ask, recorded here and not yet sent: the transcriptions of the two pairs and `K-Guy1780b.tsv`.
- **Transcription against the images.** The verifier compared 336 groups on views 009 and 014 (f9 lines 1-27, the end of f9 and
  the whole held-out postscript): 336 agree; the two places marked doubtful (334?, 178?/172) are visibly overwritten. At
  integration one page of f16 was checked at full resolution, view 022 left page, lines 1-7 and 27-30: **102 groups, 102 agree**;
  "800?" (l27) is a clear 800 on the image. One clear-text slip: l03 reads «on peut faire usage», not «ou peut faire l'usage»
  (the frozen transcription is left unchanged). The other f16 views were not checked at full resolution, and the 182/183
  question was not settled: 182.633 stands on views 010, 012, 023 and 024, and the ANOM image route answered HTTP 403 to this
  session on 12 Nov 2026 (it had served the verifier's script on 11 Nov). Next time: Chrome.
- **Which key failed which test.** `validation.txt` gives both failed tests of 29 Oct to K-Guy1780b; `profile.json` (from the
  contributor) gives the first, on the end of f102, to the earlier K-Guy1780 of 296 values and the second to K-Guy1780b. The
  page follows the profile, which is the more specific.
- **Content corrected.** The reading says the repair of the works, meant to put the place back in its state of 1771, was
  stopped by the abbé Terray and is unfinished; "stopped since 1771" in the PR's content note and text summary was not what it
  says, and both were reworded.
- **Other code.** The Guiana key of 1757-62 (`targets/orvilliers1759/dudout/key.tsv`) gives S = 0.10 on f9 and f16, under its own
  permuted controls (0.15): a different code, so a separate target is right.
- **Catalogue.** Entry 1201 dated f9 "13 Jul 1779"; the letter is headed "Du 19 juillet 1779" (confirmed on view 009). The entry
  is taken out of the catalogue with this write-up (both items read in part); the README row carries the corrected date.
- **Reading.** `python docs/_check_reading.py fiedmond1779`: `reading.md` 0.814, readable, 302 of 371 sentences. Both letters
  were read through as French sentences against the translation at integration: administrative French that construes with the
  clear passages, with marked holes; grade B stands.

## Prior art

- Catalogue 1201 (vetting of 3 Nov 2026): no DECODE record, nothing on cryptiana, Lasry or HistoCrypt, no edition of
  Fiedmond's 1779 reports found. Not on our site before this PR.
- Our check (28 Oct-11 Nov 2026): no gloss in C14 51 views 001-035; the minister's dispatch of 22 March 1779 (ff. 192-194) and
  La Serre's papers of July-August 1779 (ff. 251-256, views 302-314) are clear texts on the same matters but not versions of
  f9/f16. The minister's answers (series B) were not seen.

## Remaining gaps

- 75 unresolved words (24 in f9, 51 in f16): numbers absent from the key (552, 444, 403, 626, 778, 723, 430, 652, 441, 582, 192, 132, 219, 188, 256, 605, 695, 71, 189; in f16 576, 375, 289, 126, 112, 698, 765, 255, 155, 118, 245, 472, 274, 800, 740, 727 ...) and the river names 102, 515, 271, 720 - blocker: open-codes; most occur once or twice in the corpus and no table of this code is known
- 636 probable words (159 in f9, 477 in f16; most rest on a "prob" value, usually a single aligned occurrence in the pairs, about 55% reliable) - blocker: no-key-material; the two pairs give too few occurrences, a further text of the time in this code would confirm or correct them
- 309 restored words (values from context only, numbers read by the sense, values contradicted by the sense such as 398 = ils read "ap" and 461 = ef read "fe") - blocker: no-key-material; a third text of the time in this code (a decipherment of f9/f16, or the minister's answer in ANOM series B) would test them; not online
- doubtful groups of the transcription (182/183 in 182.633 on views 010, 012, 023, 024; 801?/301, 605, 695, 71, 189) - blocker: illegible; overwritten or ambiguous figures, to be re-read blind on the images; 438 groups checked so far (views 009, 014, part of 022), the rest of f16 not checked at full resolution; the ANOM image route answered 403 on 12 Nov 2026
- the two cipher/clear pairs of 1779 and 1780 and the earlier key K-Guy1780b.tsv are not in the repository, so the pair-derived values of the key cannot be verified here - blocker: no-key-material; held by the contributor, to be asked for (C14 51 ff. 98-111 and C14 52 ff. 15-19v transcriptions, K-Guy1780b.tsv)
- 53 of the 59 context-only values of the key are untested by the held-out portion, which is now used up - blocker: no-key-material; no other untouched text in this code is known

## Escalation

- [x] siblings: C14 51 surveyed view by view (376 views) and C14 52 (338 views): cipher pieces f9, f16, f102 (+ clear copy) and
  the 1780 pair; no other cipher piece, no table
- [x] clear-pages: f102's clear copy (ff. 98-101) and the 1780 "Déchiffrement" (C14 52 ff. 17-19v) used as key material; the
  dispatch of 22 Mar 1779 and La Serre's papers checked as cribs (not parallel texts)
- [x] known-keys: Guiana 1757-62 (orvilliers1759), Bouillé's Martinique codes B (K1, K6, K8) and the minister's code M of 1777
  tested: none applies
- [x] print: no edition found (catalogue vetting, our searches)
- [x] key-rebuild: K-Guy1780b from the two pairs, K-Guy1780c proposed by Claude Fable 5.2 and frozen, measured once
- [x] retry: every group re-decoded with the extended key K-Guy1780c and every word regraded (words_f09.tsv, words_f16.tsv); the blind re-reading of the doubtful groups on the images is not done yet, and the minister's answers in ANOM series B are not online
