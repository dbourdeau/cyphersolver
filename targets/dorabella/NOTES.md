# Dorabella cryptogram (Elgar to Dora Penny, July 1897)

Status: in progress (written up 28 Oct 2026 as not solved, attempted, open; hypothesis loop continuing, see runs/loop.md)

Famous target (`FAMOUS` in `docs/_check_writeup.py`): no profile.json, not in the paper data.
Survey context: `research/top50/NOTES.md` row 26.

## Ciphertext

`ct.txt` is the majority-consensus transcription of Hauer, Choi, Hindle, Smallwood & Kondrak,
"Dorabella Cipher as Musical Inspiration", arXiv 2509.17950 (Sept 2025), Fig. 2 (`src/hauer2025.pdf`,
CC BY-SA 4.0). They compared five transcriptions (Schmeh 2018, Hartmeier 2017, Pelling 2012, two of their own).
Token = orientation A–H + number of arcs 1–3. Lines 29 / 31 / 27 = 87 tokens.

Statistics (28 Oct 2026): 20 of 24 possible symbols used; IoC 0.0585 (English ≈ 0.066, flat 24 ≈ 0.042);
F2 11, C2 8, F3 8, A3 7; doubles F2 F2 (twice), E3 E3, D1 D1; repeated trigram F2 C2 G2 and C2 G2 F3 (twice each);
no repeated 4-gram. Orientation F carries 23/87.

## Prior work checked (28 Oct 2026)

- No accepted solution as of Oct 2026 (web search). Wase, "Dorabella unMASCed", *Cryptologia* 2023
  (doi 10.1080/01611194.2023.2271466): solvers that break 87-letter English/Latin substitutions ~98.7% fail on it.
- Hauer et al. 2021/2025: enciphered-music hypothesis; a melody "decipherment" used as compositional inspiration,
  not presented as a solution.
- Belanger 2025 (dearcipher.space): "Like to the Damask Rose" rose-key proposal, self-rated moderate, untested.

## Steps (28 Oct 2026)

1. **Elgar's notebook alphabet family** (`elgar_layout.py`). Every key that lays a 24-letter alphabet in order
   around the 8 orientations × 3 arc counts (8 starts × 2 directions × orientation- or count-major × arc order
   reversed or not × all 325 two-letter merges), × 26 Caesar shifts × forward/reversed: 1,081,600 readings.
   Best −5.06 per char (en-modern order 4); English text scores −1.5 to −2. **Ruled out.**
2. **Substitution solver with calibration** (`solve.py`). Annealing on order-4 no-space models; controls =
   87-letter passages of the model's own corpus enciphered at random; nulls = shuffled Dorabella.
   First bug: with homophones unrestricted the search collapses to "eeee…" (spurious −1.30); fixed by capping
   each letter at 2 symbols, and in strict mode by letting unused letters enter the key.
   en-modern strict one-to-one: Dorabella −2.878; controls −1.71 to −1.76 at 98–100% key recovery;
   nulls −2.94 to −3.36. Dorabella scores as a shuffle, not as English. Reproduces Wase 2023.
3. **Language batch** (`runs/<model>[--reverse][--injective].txt`; 30 restarts, 10 controls, 10 nulls).
   English, Latin, French, German, Italian, Spanish, each forward and reversed, strict key and ≤2 homophones.
   In all 24, Dorabella's score falls inside or at the edge of its shuffled-null range, and the readings are
   gibberish; controls are recovered at ≥ 0.9 accuracy in most runs (strict key: en 10/10, it 10/10, es 9/10, la 9/10,
   fr 5/5; homophonic mode is weaker, es 3/10). Strict-key Dorabella vs null range: en −2.829 (−3.24..−2.79),
   la −2.504 (−2.96..−2.73), fr −2.763 (−3.15..−3.00), de −3.131 (−3.39..−3.05), it −2.864 (−3.51..−3.35),
   es −2.690 (−3.06..−2.83). Dorabella sits a little above the nulls in several languages, which is the sequential
   structure noted under step 7, not a reading: nothing approaches the controls (−1.5 to −2.2).
   Note: from 13:57 another process in this checkout (not started from this session) re-ran the strict fr/de/it/es
   files with 20 restarts and 5 controls and overwrote them; same hypothesis, same outcome.
   **Transpositions** (`transpose.py`; ~150 reorderings: reversals, boustrophedon, column reads of the three lines,
   decimations, rail fences, columnar widths 2–29, then substitution). Best non-null: reverse −2.128 (homophonic),
   lines-reversed-each −2.769 (strict), decimate-by-2 −2.688 with a space symbol; nulls −2.27..−2.53, −2.97..−3.25,
   −2.90..−3.35 respectively. All readings gibberish; the margins are what ~150 tries buy. **Ruled out** at this level.
4. **Transcription noise sensitivity** (`solve.py --noise`). English controls, strict key, symbols misread at
   random: 5% (4 symbols) → 4/8 still broken (acc ≥ 0.90), the rest −2.6 to −2.85; 10% (9 symbols) → 2/8 at
   acc ≥ 0.83, scores −2.35 to −3.05, overlapping Dorabella's −2.88. So "not a simple substitution" holds only
   if the transcription is within a few symbols of right. Wase's and our negative do not cover a ~10% misread rate.
5. **Misread-tolerant solver** (`edits.py`): key plus up to K orientation slips (neighbouring orientation, same
   arcs), 4 nats per edit. K=6: Dorabella −2.743 (gibberish), nulls −2.80 to −2.97, controls with 6 seeded
   slips recovered 1/6. K=10: Dorabella −2.697, nulls −2.83 to −3.00, controls 0/6. **Underpowered** — the
   joint search does not recover seeded controls, so it neither finds nor excludes a misread substitution.
6. **Misread-tolerant, alternating** (`edits2.py`: anneal key, greedy slips worth > 4 nats, re-anneal, ×3).
   K=6: controls 1/6 clean (0.95) + 1 partial (0.74); Dorabella −2.705 with 4 slips (positions 4, 31, 39, 77),
   gibberish; nulls −2.78 to −3.00. K=9: controls 1/6. Better than step 5, still weak. Conclusion: at 87
   symbols, more than ~5 misreads put a simple substitution beyond what n-gram search can establish or refute.
7. **Cribs** (`crib.py`): 50 personal/situational words (dorabella, dora, penny, wolverhampton, alice, elgar,
   forli, malvern, thank you, weekdays, kiss, love …) at every isomorphic offset (short ones sampled), rest of
   the key annealed. 343 placements; best "kiss"@53 −2.838, gibberish around it; best null placement −3.235.
   No crib produces readable context. Nulls (4 shuffles, same procedure): best −3.136 to −3.320, so Dorabella's
   best crib fit beats every shuffle by ~0.3 — explained by the next line, not by a reading.
   **Sequential structure**: 19 repeated-bigram excess against a shuffle mean of 11.15 (P = 0.004, 2,000 shuffles);
   doubles 4 against 5.0 expected (P = 0.76). The symbol order is not random: something language-like or
   system-like orders it. That makes "meaningless doodle" unlikely and is the strongest positive fact here.
8. **Orientation-rotation polyalphabetics** (`rotate.py`): periodic dial key p = 1–8 (IoC-maximising shifts,
   exhaustive p ≤ 3) and linear progressions o − a·i, a = 1–7, then strict substitution. Dorabella's best is the
   identity (−2.878); periodic keys −2.94 to −3.07; linear progressions push IoC to 0.038–0.056 (towards flat) and
   score −3.2 to −3.9. Shuffles under the same procedure reach −2.69 to −2.99. **Ruled out**: the orientation is
   not stepped; the symbols behave as fixed, which leaves a substitution-like system on an unusual plaintext.

9. **Attested transcription variants** (`variants.py`, `disputes.json`). Schmeh's 2017 transcription and the
   Elgar-key letter reading on Cipher Mysteries, aligned symbol by symbol to the consensus, disagree at 11
   positions: 12 F1/G1, 21 F2/G2, 22 B1/C1, 23 H1/G1, 25 H1/G1, 77 C1/B1, 84 B1/C1, 85 H1/A1, and three where Schmeh
   reads a separate symbol type (24 H2, 37 A3, 50 G2). Key and all 2^11 readings annealed jointly, 20 restarts.
   Dorabella −2.449 (alternatives at 22, 25, 84): "zledwardogysinsussallsangraymrsrandofdesse…" — "edward" at 2–7
   is chance (the crib run placed "edward" at every isomorphic offset without a top score), the rest gibberish.
   Nulls −2.315 to −2.630 (8 shuffles carrying their alternatives); controls with half the disputes wrong:
   3/8 recovered at 0.95–0.99 (−1.67 to −1.90), the rest −2.26 to −2.47. **Negative**: no combination of the
   readings the transcribers actually disagree on yields text.
10. **Original lost.** Dora Penny lent the note to Methuen for the 1937 memoir and it was not returned; every
   image derives from that reproduction. A better scan of the original cannot be obtained; the 1937 print (and
   the 1947/1949 editions, which commenters say differ by a dot on line 2) is the best source.

11. **The 1937 plate, measured** (`src/memories1937/`, `measure.py`, `reclass.py`). The first edition is open
   on archive.org (in.ernet.dli.2015.155431, Digital Library of India); the cipher is on p. 98 (scan page 137,
   2911 × 4373 px; crop `cipher_full.png`, 2720 px wide, ~6× the Wikimedia image). The appendix text: enclosed in a
   letter from Alice Elgar to Mrs Penny, "Miss Penny" on the back, after the July 1897 Wolverhampton visit
   (p. 9: five days; kites at Boscobel by King Charles's Oak; Lux Christi, Bavarian Highlands, Caractacus sketches).
   Binarised scan; every glyph is one connected stroke: 87 components, 29/31/27, the consensus count exactly.
   Opening angle per glyph = ink centroid → centroid of (convex hull − ink). Sorted by angle, the consensus labels
   run A H G F E D C B round the circle, offset ~35° clockwise by Elgar's slant. Leave-one-out nearest class
   (same arc count) reclassifies 17 glyphs (`ct_measured.txt`); four of them land on the alternative a human
   reader gave: #21 F2→G2 and #77 C1→B1 (Elgar-key reading), #22 B1→C1 and #23 H1→G1 (Schmeh).
   Strict en-modern on `ct_measured.txt`: −2.853, nulls −2.89 to −3.34, controls −1.63 to −1.92 (8/8 ≥ 0.97).
   Joint search over all 23 disputed positions (`disputes_merged.json`): −2.407, nulls −2.38 to −2.57,
   controls 2/8 recovered (0.92, 0.97). **Negative** on the best image there is.
12. **Systems Elgar read in 1896** (`research_pallmall/`: the four Pall Mall "Secrets in Cipher" parts, Jan–Apr
   1896, archive.org sim_pall-mall-magazine_1896-0[1-4]_8_3[3-6], OCR + page images; `systems.md` lists 37
   systems). He solved the Part IV Nihilist challenge (key COURAGE, "he who fears is half dead": his Courage cards).
   The structural match is Roe's nine-figure cipher: 8 groups of 3 (abc def ghi klm nop qrs tuw xyz) × 1–3 marks =
   24 signs, i.e. orientation = group, arcs = place. Alone it is a simple substitution (already out), so tested
   with the series' second layers (`pallmall.py`):
   A. Roe grid (16 dial orders × 2 arc orders) + periodic keyword shift p = 1–12 (chi-square key) or running dial
      shift: Dorabella best −5.211 of 1,120 keyed readings; nulls −4.85 to −5.28; controls (English, Roe grid,
      random 5-letter key) −3.72 to −4.76, partly readable. **Negative.** Untested: non-cyclic group orders (8!).
   B. Nihilist-style additive key on both coordinates (orientation mod 8, arcs mod 3), p = 1–8, unknown grid,
      IoC-chosen shifts then strict substitution: Dorabella −2.784; nulls −2.84 to −2.93. **Negative.**
   C. Roe grid with ANY group order (`roe_perm.py`): pi(0) fixed (a rotation only adds 3k to the key), 5,040
      orders × 2 arc orders × (keyword p = 1–12, or dial a = 1–23) = 352,800 keyed readings per text;
      chi-square keys, top 300 refined by n-gram coordinate ascent. Controls (random non-cyclic order; three dial
      keys, one 5-letter keyword) 4/4 recovered at 1.00 (−1.73 to −2.44). Dorabella −3.415 (gibberish);
      nulls −3.266 to −3.441 (6 shuffles). **Negative.**
13. **Sibling texts** (`research_siblings/siblings.md`). Elgar's notebook key table (Elgar Birthplace Museum; Padgett
   photo 2021, Sams tracing): A=A1 B=A2 C=A3 D=B1 … I/J=C3 … U/V=G2 W=G3 X=H1 Y=H2 Z=H3, confirmed on its practice
   lines (MARCO ELGAR, A VERY OLD CYPHER, DO YOU GO TO LONDON?) — a member of the step-1 family. Liszt fragment
   (1886, 18 signs) and the "Cryptogram" card (~18 signs) are the only other texts in the system: too short to
   test a key on. Courage cards (first one has ~10 Dorabella-like signs): no transcription online.
14. **Elgar's own register** (`build_elgar_corpus.py`; lang/ source `en-elgar-powell1937`, model `en-elgar`):
   23 letters + 379 quoted speeches from the 1937 memoir (48,782 chars, "wigorously … wunce a week"), ~10% weight
   over en-gutenberg. Strict: consensus −2.770 (nulls −2.76 to −3.14), measured −3.007 (nulls −2.89 to −3.33);
   homophonic: −2.255 / −2.273 (nulls −2.17 to −2.47). Controls 0.92–1.00 (Gutenberg text; Elgar's letters are in
   the model, so no held-out control in his register). **Negative.**

15. **Null signs** (`nulls.py`): each orientation, each arc count, and the six rarest symbols dropped in turn,
   remainder solved strict on en-modern. Dorabella sits above its shuffles in several drops (F: −2.356 vs
   −2.54..−2.76; C: −2.487 vs −2.73..−2.86; 1-arc −2.393 vs −2.52..−2.62), the sequential structure again, but every
   output is gibberish and none reaches its controls. **Negative.**
16. **Motor signature / "doodle"** (`doodle.py`, 5,000 shuffles). Not a doodle: consecutive signs turn *more* than
   chance (mean orientation step 2.33 vs 2.01, P = 0.010), no ±45° sweeps at all (longest 1 vs 2.07). **New
   structure: opposite orientations.** 180° steps 27 vs 12.6 expected (none of 5,000 shuffles ≥ 27, P < 0.0002);
   90° steps fewer (11 vs 18.4, P = 0.02). Mostly F↔B and C↔G. English under Elgar's own table (the Roe order
   with most opposition) gives 15.4 (P(≥27) = 0.0005); the best letter→orientation layout for English yields at most
   24.7 expected over 86 pairs, below Dorabella's 27. Not a pairing artefact: 17 even / 10 odd start positions,
   longest chain 3. So whatever produced the orientations favours flipping to the opposite side more than any
   substitution of English can.
17. **Axis hypothesis** (`axis.py`): orientation mod 4 × arcs = 12 signs, direction ignored, polyphonic (~2 letters per
   sign), grouping annealed, Viterbi on en-modern order 3. Dorabella −1.983; nulls −1.93..−2.03; controls 0.02–0.30
   accuracy. **Inconclusive**: a 12-sign polyphonic cipher of 87 signs makes English-like text from anything.
18. **Word initials** (`initials.py`). (a) Initials model (order 3, 4.9 M words): Dorabella −2.618, nulls −2.61..−2.68,
   controls −2.47..−2.67 at 0.01–0.48 accuracy: **no power**. IoC of English initials 0.0718 vs Dorabella 0.0585 (running
   text 0.066): mildly against. (b) Acrostic of a known text: every 87-word window of KJV, Shakespeare, Bulchevy's English
   verse and en-gutenberg (4.9 M windows): best one-to-one fit 30/87, shuffles 29–34. **Negative** for those texts.
19. **Pall Mall facsimile systems**: Guise/Condé (3–4 homophones per letter), Charles I's shorthand and the musical
   cipher are fixed symbol tables, covered by steps 2–3 and 15. Sign pairs as Polybius coordinates: 39 of 43 pairs
   distinct at either phase, IoC 0.0044 = shuffles (P = 0.35); a pair code for letters would give ~18 distinct.
   **Negative.**
20. **Melody crib: the Lullaby Elgar played that week** (`melody_crib.py`). From the Bavarian Highlands op. 27 no. 3,
   alto solo bars 23–38 ("Sleep, my son … sleep, my son"), 33 notes read by eye from the SHORCHOR 2019 vocal score
   (D major, 3/4; ties merged; durations shorter/quarter/longer as Hauer). The NWC Scriptorium file (decoded by
   `nwc_melody.py`; NWC 2 binary) is a 2005 orchestral arrangement whose sections and keys do not match the published
   score, so it was not used. Every segment ≥ 4 notes at every offset; longest fit explained by one mapping:
   structured (pitch → orientation, duration → arcs) 5, shuffles 5.0 (P = 0.85), random melodies 5.0; free
   ((pitch, duration) → symbol) 9, shuffles 10.5, random melodies 9.7. **Negative.** Not tried: the piano
   introduction theme, Lux Christi, Caractacus (need reading from IMSLP scores).
21. **Turn encoding** (`ct_turn_arcs.txt`, `ct_turn_darcs.txt`; `solve.py --ct`): the letter as the change between
   consecutive signs (orientation step × arcs of the second sign, or × arc change), 86 tokens, 22 types; the commonest
   turn (180° with 2 arcs) is 16% of the text, e-like. Strict en-modern: −2.941 (nulls −2.80..−3.13) and −3.116
   (nulls −3.03..−3.52); controls 5/6 ≥ 0.97. **Negative.**
22. **Flips as word breaks** (`flipwords.py`): split at every 180° step and line end → 29 "words", mean 3.0 signs,
   24% of length 1 (English: mean 4.1, 6% one-letter). Strict substitution with those spaces, en-modern with spaces:
   −3.414 ("q ptach dal rm on w …"); nulls −3.61..−3.81; controls with their real spaces recovered word for word
   (−1.27..−1.46). **Negative.**
23. **Shorthand**: no source links Elgar to Pitman or any shorthand (searched); Sams 1970 only says the signs suggest
   it. Pitman's curves are single quarter-arcs in ~4 directions with thick/thin for voicing; Dorabella has 1–3 arcs,
   8 directions, no weight contrast. The testable content (signs = sounds) is step 24.
24. **Phonetic English** (`phonetic.py`; CMU Pronouncing Dictionary, en-gutenberg converted word by word, 3.8 M
   phonemes, no word breaks, order 4). 39 phonemes: Dorabella −3.263, nulls −3.27..−3.68, controls 0.11–0.47
   accuracy — **no power** (more sounds than signs). Merged to 25 classes (AO/AH→AA, IY/Y→IH, UW→UH, ER→R, Z→S,
   DH→TH, ZH→SH, NG→N, JH→CH, OY→OW, AW→AY, V→F): controls 6/6 at 0.99–1.00 (−1.74..−2.09); Dorabella −3.011,
   nulls −2.85..−3.28. **Negative**: the signs are not English sounds under a one-to-one key.
25. **Second Lullaby crib**: soprano bars 43–46 "Vainly play zithers gay! Here I stay all the day" (F♯ E A | A G♯ B |
   G♯ F♯ B | F♯ E E, rhythm dotted-quarter/eighth/quarter each bar). Structured fit 4 (shuffles 4.2, P = 0.97);
   free fit 10 at offset 30 (shuffles 9.1, P = 0.33; random melodies 6.9, P = 0.01 — the tune's own repetition, not
   Dorabella). **Negative.** The piano introduction is chords and figuration; no single line before bar 9 to read.

26. **Hypothesis loop, 27 rounds** (`hyp.py`, `rounds.py`, `run_round.py`; map in `HYPOTHESES.md`; one line per
   round in `runs/loop.md`; every number in `runs/ledger.tsv`). Each hypothesis scored on Dorabella, shuffles (or
   pair-keeping shuffles) and English put through the same system. All decidable branches negative or excluded.
   Key findings: Dorabella's key-invariant statistics are typical of English letters and Elgar's letters (R 11);
   neither a pseudo-writer nor English under a random key reproduces them, but English under a flip-heavy key does
   (R 25–26); Playfair, sign-offs and Elgar-table-plus-transposition are excluded by logic (R 10, 12, 18); key changes,
   heavy misreads and polygraphic units cannot be decided at 87 signs (R 15, 16, 27).

27. **Padgett's reply and Bauer ch. 3 (pp. 129-140), 29 Oct 2026** (`padgett_test.py`, `padgett_controls.py`,
   `attempts_test.py`; Padgett email of 29 Oct 2026; Bauer, *Unsolved!* 2017, figs 3.3-3.15, read from the author's
   own copy). (a) Padgett's claim that the notebook key turns the note into Spanish words is reproducible as a
   string fact: the consensus tokens under the notebook table read `BPECAHTCKYFRQDRIRRHPPRDXYXGFSTRTHXCKLCERREHGQTRFRHUSQDXKKXFSESHUSEDUWGSERHUQSGCPGSHCDXC`,
   and PECA (2-5), Y, IR, CERRE (38-42), SE/ES, SED (65-67), SER (71-73) are all in it (EDU at 66-68 is his
   dotted-D). But it is not evidence of Spanish: best non-overlapping parse into a 30,500-word Spanish lexicon covers
   30 of 87 signs, against a mean of 29.4 (P = 0.47) for random bijective keys on the same sign sequence. Shuffles of
   the signs give P = 0.005, because they destroy the sequence's letter skew; that is the wrong null. English, French,
   Italian, Latin, German under the same key and nulls: no language stands out (P 0.4-0.9 against random keys). His
   in-order list of eight words is not a disjoint parse (SE and ES share a letter). The row-length and dot layers
   (C-E-A, "C BAB JIG", E/A/D/G, AMDG, K.147) have a free choice at every step; not tested further.
   (b) Bauer p. 135 states that the notebook key gives gibberish on Dorabella and on the Liszt fragment: agrees with
   step 1. (c) The three solutions Bauer prints: Palmer 2007 is a near-consistent substitution (83 of 87 signs on one
   symbol-to-letter map, four conflicts she resolved by hand) whose raw text needs back-slang and re-spelling; Roberts
   2009 explains 58 of 87; Sams 1970 has 94 letters for 87 signs. None reads as text. (d) Elgar's Schooling cards
   (figs 3.12-3.15) give his keywords TRUTH and MERCURY (TYRANT is Schooling's); added with MARCO, EDU, CAE, BAB, JIG,
   AMDG to the round 3 and 23 key lists: negative (R3 -5.68 vs controls -2.4..-1.8; R23 -5.94). Bauer's cards 1-4
   are the Schooling challenge solution (key family COURAGE); cards 5-6 (pp. 141 on) not yet seen here.

28. **Liszt fragment under the same key** (`ct_liszt.txt` = consensus + Padgett's 18-sign Liszt reading as a fourth
   line; `solve.py --injective`, `runs/liszt_joint_*.txt`). If the 1886 fragment and the 1897 note share one table,
   105 signs should solve where 87 did not. en-modern −3.043, en-elgar −3.023; shuffles −3.02..−3.37; controls 6/6
   recovered (0.90-1.00). **Negative**: no shared simple-substitution table, at the transcription available.

29. **The "Cryptogram" card at 2527 px** (Padgett's blog, Jan 2025, from Chris Bennett; `research_siblings/siblings.md`
   section 3). Middle line `A3 B2 C2 D2 E2 F2 G3 H2 A2 A1`: all eight orientations in clockwise order, then back to A.
   That makes it an alphabet exercise in the same sign system, not a message. It fits an orientation-major table
   (step 12, Roe grid), but the arc counts it uses are not the 1-2-3 order, so it gives no key values. Closes the
   "second text" lead for this card. Bauer's cards 1-4 (pp. 139-140) are the Schooling solution; this is card 6.

30. **Notebook key with turned signs** (`rotlattice.py`, `runs/rotlattice.txt`). If Elgar used his notebook key but
   sometimes drew a sign turned round (the excess of 180-degree flips suggests it), each sign stands for 2-4 letters;
   exact order-4 Viterbi picks the best path (I/J, U/V both allowed). Variants: turned 180, any 90, mirrored left-right,
   top-bottom, rotate-180 + both mirrors. Controls (English under the notebook key, 35% of signs turned): 0.90-1.00
   recovered in every variant except any-90 (0.70-0.84, partial). The note: inside random keys on the same signs in every
   variant (P 0.47-0.96, en-modern and en-elgar, 200 nulls each), far below controls (best any-90 -2.25 vs -1.51..-1.72),
   gibberish. Any-90 beats shuffles (P 0.015) only through the known sequential structure. **Negative**.

## Where it stands (29 Oct 2026)

Unchanged by rounds 68-72 (Padgett's reply, Bauer ch. 3): every branch decidable with the material in hand is NEG, X
or NP. Next movement needs a better image of the note or a second text, both outside this checkout.

### As of 28 Oct 2026

Not deciphered. Outcome: not solved (attempted, open).

What this session establishes, beyond Wase 2023:
- The negative for simple substitution now covers six languages, forward and reversed, strict and homophonic keys,
  ~150 transpositions, a word-space symbol, the whole family of Elgar's own ordered-alphabet layouts, rotating-dial
  polyalphabetics, and 50 situational cribs — each calibrated against enciphered controls and shuffled nulls.
- The symbol order is not random (repeated bigrams, P = 0.004), so the note encodes something sequential.
- The negative is conditional on the transcription. With ~5% of symbols misread (4 of 87) half of all English
  controls still break; at ~10% most do not, and their scores overlap Dorabella's. Two misread-tolerant solvers
  (`edits.py`, `edits2.py`) recover only 1 in 6 controls with 6 seeded slips, so a substitution hidden behind 5–10
  misreads can be neither found nor excluded by n-gram search at this length.

## Remaining gaps

- Transcription: all attested disputes and the 1937-plate measurements tried (steps 9, 11). Blocker: the
  original is lost; the 1937 first-edition scan is binarised. A greyscale scan of the 1937/1946/1949 plate
  would sharpen the angle measurement. Found 29 Oct 2026: archive.org `edwardelgarmemor0000mrsr` is the 1947 edition,
  scanned 2022 in greyscale JP2 (196 images), lending-only (access-restricted); a borrowed view can be screenshotted
  for the plate, then `measure.py`. Tried 29 Oct 2026: the archive.org sign-in did not complete in the user's Chrome, and
  the user closed this route. Still open for a later session; the plate would only refine the 1937 measurement.
- Second texts: Liszt fragment (step 28, negative jointly) and Cryptogram card (step 29, an alphabet exercise); the rest of
  the nine-card Schooling series untranscribed. Blocker: no
  text long enough to check a key on two documents; the Courage cards need museum access.
- Plaintext register: the Elgar model has only 49k chars of his words and no held-out control. Blocker: his
  collected letters (Moore 1987, 1990; Young 1956) are in copyright/lending-only.
- Systems: Roe grid searched over all group orders (step 12C). Pall Mall facsimile tables
  (Guise/Condé, Charles I shorthand, the musical key) not yet transcribed from the page images.

## Escalation

- Siblings: searched (step 13); none usable. Known keys: Elgar's notebook table (steps 1, 13). Print: Wase,
  Hauer 2021/2025, Pelling, Schmeh, Sams, Padgett read. Clear pages: none exist. Key rebuild: steps 2–9, 11, 12, 14.
- Retry paths: greyscale plate → `measure.py` → `variants.py`; Courage-card transcription → test as a second
  text; facsimile key tables in `research_pallmall/downloads/img/` → implement → `pallmall.py`.

## Language and transposition batch, strict key (28 Oct 2026, rerun)

Per-char score: Dorabella / controls / shuffled nulls. All gibberish; no language separates from its nulls.
en −2.83 (rev −2.77) / −1.63..−2.21 / −2.79..−3.24; fr −2.76 (rev −2.89) / −1.46..−1.92 / −2.87..−3.16;
de −3.13 (rev −3.10) / −1.67..−2.71 / −2.93..−3.39; it −2.94 (rev −3.11) / −1.60..−1.89 / −3.08..−3.74;
es −2.69 (rev −2.72) / −1.79..−2.20 / −2.91..−3.10. Dorabella sits slightly above the nulls in every language
(the bigram structure noted in step 7), far below the controls.
Transpositions (`transpose.py --injective`, 60 reorderings): best "lines-reversed-each" −2.769, identity −2.801,
nulls −2.97..−3.25; with a space symbol best −3.49, nulls −3.91..−4.48. No readable output.
