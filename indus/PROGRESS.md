# Decipherment progress: the metric and the loop log

Started 24 September 2026 at the owner's request: loops of registered hypothesis tests aimed at deciphering the texts,
with a progress metric measured the same way every loop (`progress.py`, log in `results/progress_log.tsv`).

## Indus-prize tiers (owner's review, 24 September 2026)

The Tamil Nadu government's $1 million prize (announced 5 January 2025) goes to whoever deciphers the script "to the
satisfaction of archaeological experts"; no further rules are published. It was announced beside a study linking Indus
signs to Tamil Nadu graffiti marks and a research chair in Iravatham Mahadevan's name. The judges are therefore
archaeologists and epigraphists, and a Dravidian or Tamil reading will draw the closest scrutiny. The bench is ranked
by what such a panel would accept (`prizebench.py`); the structural components below are diagnostics.

| Tier | Component | What it measures | Now |
|---|---|---|---|
| 1 | V meaning, checked | share of sign tokens read as sense and checked against archaeological evidence: the object's iconography (copper tablets, seal motifs), its function (weights, tags, pottery), its find context, West Asian texts naming Meluhha. Numerals reported beside it (their sense is the count). | 0.008% (4 copper-tablet signs); numerals 16.6%; referent fixed by the picture (not read) 0.79% (11 texts; sign pairs on individually made tablets and across distinct moulded designs, pictured fragments included; sets 233, 237, 243, 254; part-texts merged). Caveat: these are local labels; they do not transfer between tablet types (1 of 40 cross-type predictions right, observation after set 243) |
| 2 | C positive-control gate | a method proposing sound values or readings must first recover a known answer (Linear B -> Greek). Methods that passed / were run | 3 of 6 passed: substitution-phonetics (set 179), character-LM key scorer (set 205), picture-referent method (sets 234-235); failed: key bench, blind key fitting (Linear B fits Sanskrit best, set 207) (Ventris's Linear B key beaten by 11-41 of 100 shuffles, `linb_control.md`); rebus search not run |
| 3 | U vault | share of tokens in texts never used to fix the values (B's new lines; later, newly excavated finds) read as sense with values fixed beforehand | 0 (no sound value has passed); sign restorations checked against an outside transcription (sets 283-284: illegible ICIT signs predicted by a model retrained without copies of the text, compared with Mahadevan 1977's readings: top-1 21 of 49 (43%), top-5 32 of 49, frequency baseline 6, context baseline (commonest sign between the same neighbours) 19 (set 285); lexical signs 10 of 29 against 7; a sign-level check, not meaning, and only narrowly better than a neighbour rule); picture vault: weak; leave-one-out 16.9% (p = 0.05), 13.6% with near duplicates together (p = 0.14), 49 of 50 splits above the null median (sets 201-203) |
| 4 | A archaeological consistency | readings or structure hold across sites, periods, duplicates and sealings of the same seal | supporting: fish/520 signal holds at all sites and periods (set 196) and on seals and tablets alike (set 230); Tamil Nadu graffiti composites are less ordered than Indus lines (70.5% against 88.0% order consistency, set 204); one grammar serves every site: learned at one city it parses the other nearly as well as its own (margins 43.8 / 46.1 against 44.8 / 44.6, set 227), across object types (seal grammar on tablets 43.6, tablet grammar on seals 48.1) and time (late Harappa grammar on the early levels 27.0; set 228); the cage and inner-stroke devices behave identically in both cities (set 229); the count-label slot is restricted in both (set 231); on unseen moulded tablets grammatical sign pairs go with more pictures than lexical pairs (0.45 against 0.28, set 240): the pictures confirm the grammar / lexicon split |
| 5 | L language, against genre-matched decoys | the typology narrows the field (L world); a language claim must beat typology-matched decoys of the same genre | L world 85.1% / 77.0% (no-prefix profile, set 220); no candidate beats the decoys inside the remaining groups (set 198) |
| 6 | WORD task | hide a name body in a held-out line; rank all training bodies; top-1 / top-10 against frequency | 0% / 3.4% (frequency 0% / 1.3%) |
| 7 | SIGN task | hide one sign; rank the 150 commonest signs; top-1 / top-5 against frequency | 39.7% / 61.8% (two-direction model, set 204; discounted contexts, sets 210-211; frequency 9.6% / 22.4%) |
| - | diagnostics | S bits/sign, R roles, G margin, M+ | S 4.635, R 86.3%, G 49.6 / 37.4, M+ 41.4% |

### The target: what a winning entry needs (estimate, 24 September 2026)

The prize text gives no threshold, so this is the bench's own estimate of what archaeological experts would accept,
built from what made Linear B, Maya and Ugaritic decipherments accepted.

| Tier | Winning level | Now |
|---|---|---|
| 1 V | 80-95% of sign tokens read as sense in one named language with a stated phonology, whole inscriptions as grammatical phrases; sense agrees with several independent kinds of outside evidence (iconography on the same object, copper-tablet pairs, object function, site, West Asian Meluhha records) far above chance | 0.008% |
| 2 C | the same method, with the same freedom, recovers a known script (Linear B -> Greek) and fails on shuffled keys and decoy languages | 1 of 3 methods |
| 3 U | values frozen and published before being applied to texts never used to set them (B's new lines; new excavations); sense far more often than decoy keys | 0% |
| P | values for the ~70 common signs that cover ~80% of tokens, few free parameters relative to the evidence (the key compresses the corpus) | 0 |
| - | reproduced and accepted by specialists who did not build it; method and data published | - |

Tiers 1-3 are what would win the prize and are near zero: the work so far is structural. The loop's progress rule is
unchanged (any component), but each loop now reports the tiers, and loops that can move tiers 1-3 come first.

## The metric

Decipherment happens in stages, so the metric is a vector, one component per stage:

| Component | What it measures | Direction |
|---|---|---|
| S structure | held-out bits per sign on a fixed 80/20 split (seed 2026) of the distinct lines, best registered model. Note (audit after set 223): the position and end components (set 125) are given the line's length, so S is bits per sign *given the length* and the end-of-line token is nearly free; constant since the baseline, so loop-to-loop comparisons hold, but the absolute value is optimistic | lower |
| R roles | share of sign tokens whose job is fixed by a tested rule (numeral, ending, closer, marker, heading, name head, counted sign ...) | higher |
| M meanings | share of sign tokens whose sign has an externally anchored meaning (numeral values, copper-tablet sign = picture equations) | higher |
| M+ meaning classes | M plus signs whose depicted class (Fairservis) is confirmed by use on held-out data (from loop 3) | higher |
| G grammar | share of distinct lines (progress.py's A lines; B check on the M77 additions) that `grammar.py` parses in full, heads learned from A only (from loop 16). From loop 18 the component is the **G margin**: share of real lines parsed by the stricter grammar G2 minus share of the same lines parsed after shuffling their signs (A; B check) | higher |
| P sound values | signs with a sound value that passed a registered held-out test (the prize) | higher |
| L language | candidate language families not yet excluded by registered tests | lower |
| L world | share of the world's language groups whose typology the Indus profile excludes (tolerant profile, majority rule; WALS genera, Grambank families as check; from loop 21, `lbench.py`) | higher |

A component moves only when a registered set supports the change. S and R are the tractable parts; M needs outside
anchors; P and L need outside evidence, and a real decipherment would show first as P > 0 with S falling (a reading
makes the texts more predictable) and M rising.

## Stopping rule (owner's goal, 24 September 2026)

The loops continue until 20 consecutive loops make no progress. A loop counts as progress if a metric component
improves, or if a new (non-replication) finding holds and is replicated on a held-out sample within the same loop.
The 'streak' column counts consecutive loops without progress. Revised by the owner after loop 23 (24 September
2026): the loops continue until 10 consecutive loops make zero progress. From loop 57 on, re-testing a finding already made within a subset (a city, an object type) is consistency evidence, not progress.

## Log

| Loop | Sets | S bits (explained) | R roles | M meanings | P | L open | Note (streak) |
|---|---|---|---|---|---|---|---|

| baseline | 1-175 | 4.712 (24.9%) | 56.2% | 16.6% | 0 | 4 | model tri + pos + end, discounted (set 125) |
| 1 | 176 | 4.712 (24.9%) | 72.9% | 16.6% | 0 | 4 | role / class / numeral-value components add nothing to S; slot-based modifier role adopted in R |
| 2 | 177 | 4.712 (24.9%) | 81.1% | 16.6% | 0 | 4 | variable-order model +0.005 only (not adopted); anchors 347/460 untestable on new objects; bare-line roles adopted |
| 3 | 178 | 4.712 (24.9%) | 81.1% | 16.6% (M+ 41.4%) | 0 | 4 | depiction of the head predicts the ending on B; human/tool/plant/fish classes enter M+ |
| 4 | 179 | 4.712 (24.9%) | 81.1% | 16.6% (M+ 41.4%) | 0 | 4 | substitution-phonetics test works on Linear B (p = 0.001); no published key passes on both samples |
| 5 | 180 | 4.712 (24.9%) | 81.1% | 16.6% (M+ 41.4%) | 0 | 4 | depiction keys per language: none passes both samples; lookup too noisy to compare languages |
| 6 | 181 | 4.712 (24.9%) | 81.1% | 16.6% (M+ 41.4%) | 0 | 4 | world-wide rebus search (503 languages): no language signal; simple rebus reading of depicted signs unsupported |
| 7 | 182 | 4.712 (24.9%) | 81.1% | 16.6% (M+ 41.4%) | 0 | 4 | substitutions not semantic either (only the fish family); no categories inferable |
| 8 | 183 | 4.712 (24.9%) | 81.1% | 16.6% (M+ 41.4%) | 0 | 4 | depiction groups are shape families; only fish (and tools weakly) are used alike |
| 9 | 184 | 4.712 (24.9%) | 81.3% | 16.6% (M+ 41.4%) | 0 | 4 | the cage (four small strokes) is a grammatical affix: caged signs replace the ending (0 of 92 followed by 740/520), B replicates |
| 10 | 185 | 4.712 (24.9%) | 81.3% | 16.6% (M+ 41.4%) | 0 | 4 | fish marks change the grammatical job (roof hat = attribute); with the cage, morphology inside the fish signs |
| 11 | 186 | 4.712 (24.9%) | 81.3% | 16.6% (M+ 41.4%) | 0 | 4 | strokes inside the jar turn the ending into a name element, B replicates (progress; streak 0) |
| 12 | 187 | 4.712 (24.9%) | 81.3% | 16.6% (M+ 41.4%) | 0 | 4 | doubled signs stand at text edges (A and B); brackets change nothing (progress; streak 0) |
| 13 | 188 | 4.712 (24.9%) | 81.3% | 16.6% (M+ 41.4%) | 0 | 4 | extra F lines make S slightly worse (4.719); no progress (streak 1) |
| 14 | 189 | 4.712 (24.9%) | 81.3% | 16.6% (M+ 41.4%) | 0 | 4 | strokes inside the U: plain 700 counted/final, 705/706 heads the closing formula; inner-stroke device generalises (progress; streak 0) |
| 15 | 190 | 4.712 (24.9%) | 81.3% | 16.6% (M+ 41.4%) | 0 | 4 | leaf attachments predict position, but on B only through the known heading; counted no progress (streak 1) |
| 16 | 191 | 4.712 (24.9%) | 81.3% | 16.6% (M+ 41.4%) | 0 | 4 | new component G: one explicit grammar parses 80.2% of A lines, 72.3% of B (B from A-learned heads); unparsed lines are the longer ones (progress; streak 0) |
| 17 | 192 | 4.712 (24.9%) | 81.3% | 16.6% (M+ 41.4%) | 0 | 4 | five rules for unparsed lines raise G (B 80.9%) but parse shuffled lines more readily; margin falls 30.7 to 25.5; bare-name rule barely specific (no progress; streak 1) |
| 18 | 193 | 4.712 (24.9%) | 81.3% | 16.6% (M+ 41.4%) | 0 | 4 | G becomes a margin over shuffled lines; stricter grammar G2 raises it A 43.3 to 46.2, B 30.7 to 34.7 (F 17.0 to 17.3) (progress; streak 0) |
| 19 | 194 | 4.697 (25.2%) | 81.3% | 16.6% (M+ 41.4%) | 0 | 4 | first S gain: context seen by graphic family (decade block) 4.712 to 4.697, replicates A to B; random families give nothing (progress; streak 0) |
| 20 | 195 | 4.697 (25.2%) | 81.3% | 16.6% (M+ 41.4%) | 0 | 4 | L bench: the Indus profile excludes 81% of WALS genera, 56% of Grambank families; strict coding drops some candidate languages, so the component is not adopted (no progress; streak 1) |
| 21 | 196 | 4.697 (25.2%) | 81.3% | 16.6% (M+ 41.4%) | 0 | 4 | L world enters: the Indus profile excludes 81.3% of WALS genera (Grambank 68.3% of families), both candidates kept; fish/520 class signal holds at Mohenjo-daro, Harappa and elsewhere (progress; streak 0) |
| 22 | 197 | 4.697 (25.2%) | 81.3% | 16.6% (M+ 41.4%) | 0 | 4 (L world 81.3%) | typology-matched decoys (Japanese, Turkish) fit Indus name structure worse than both South Asian candidates; Prakrit nearest, replicated on halves; genre caveat (progress; streak 0) |
| 23 | 198 | 4.697 (25.2%) | 81.3% | 16.6% (M+ 41.4%) | 0 | 4 (L world 81.3%) | genre control: with name lists on both sides, the Japanese decoy is nearest the Indus names; loop 22's candidate advantage was genre (no progress; streak 1) |
| 24 | 199 | 4.685 (25.3%) | 81.3% | 16.6% (M+ 41.4%) | 0 | 4 (L world 81.3%) | family 4-gram context lowers S 4.697 to 4.685 (test run 4.6842), replicated A to B; random families give nothing (progress; streak 0) |
| 25 | 200 | 4.685 (25.3%) | 81.3% | 16.6% (M+ 41.4%) | 0 | 4 (L world 81.3%) | prize tiers V 0.008%, C 1/3, U 0: picture anchors frozen on half the tablets predict 1 of 38 unseen tablets; pairing is whole-text, not sign-level (no progress; streak 1) |
| 26 | 201 | 4.685 (25.3%) | 81.3% | 16.6% (M+ 41.4%) | 0 | 4 (L world 81.3%) | tier 3: shared phrases predict unseen tablets' pictures (24.5%, p = 0.001; 18.6%, p = 0.03): elephant, tree (806 158), gaur; S gain is graphic, not generic classes (progress; streak 0) |
| 27 | 202 | 4.685 (25.3%) | 81.3% | 16.6% (M+ 41.4%) | 0 | 4 (L world 81.3%) | weighted phrases no better; a third split fails its null, so the picture vault is split-dependent; seals null (no progress; streak 1) |
| 28 | 203 | 4.685 (25.3%) | 81.3% | 16.6% (M+ 41.4%) | 0 | 4 (L world 81.3%) | picture vault by leave-one-out: 16.9% (p = 0.05), families 13.6% (p = 0.14); weak tendency, set 201's result was a favourable split (no progress; streak 2) |
| 29 | 204 | 4.685 (25.3%) | 81.3% | 16.6% (M+ 41.4%) | 0 | 4 (L world 81.3%) | SIGN top-1 36.2 to 37.9% (two-direction model, replicated A to B); Tamil Nadu graffiti less ordered than Indus (70.5% vs 88.0%, both big sites) (progress; streak 0) |
| 30 | 205 | 4.685 (25.3%) | 81.3% | 16.6% (M+ 41.4%) | 0 | 4 (L world 81.3%) | tier 2: a character-LM key scorer passes the Linear B gate (Ventris's key beats 100/100 shuffles on held-out lines; Sanskrit model 9/100): C 2 of 4; two-direction WORD does not replicate (progress; streak 0) |
| 31 | 206 | 4.685 (25.3%) | 81.3% | 16.6% (M+ 41.4%) | 0 | 4 (L world 81.3%) | no substantial published key reads its claimed language through the gate-validated scorer; Kak's 7-sign key passes only via 740 = sa at line ends (no progress; streak 1) |
| 32 | 207 | 4.685 (25.3%) | 81.3% | 16.6% (M+ 41.4%) | 0 | 4 (L world 81.3%) | blind key fitting fails the gate: fitted freely, Linear B fits Sanskrit best, Greek last/third, 0 of 30 Ventris values; free fitting cannot identify a language (no progress; streak 2) |
| 33 | 208 | 4.685 (25.3%) | 81.3% | 16.6% (M+ 41.4%) | 0 | 4 (L world 81.3%) | families from Parpola's descriptions also improve S (random none): graphic effect replicates with an independent definition; nothing beyond decade families (no progress; streak 3) |
| 34 | 209 | 4.685 (25.3%) | 81.3% | 16.6% (M+ 41.4%) | 0 | 4 (L world 81.3%) | closer-line bodies do not show the name-body pattern (sign before a closer no more often a head); no roles added (no progress; streak 4) |
| 35 | 210 | 4.675 (25.5%) | 81.3% | 16.6% (M+ 41.4%) | 0 | 4 (L world 81.3%) | discounted family 4-gram: S 4.685 to 4.675, replicated A to B; SIGN top-1 38.3% (progress; streak 0) |
| 36 | 211 | 4.635 (26.1%) | 81.3% | 16.6% (M+ 41.4%) | 0 | 4 (L world 81.3%) | discounted sign trigram: S 4.675 to 4.635 (largest single gain), replicated A to B; SIGN 39.7% / 61.8%, WORD top-10 3.4% (progress; streak 0) |
| 37 | 212 | 4.635 (26.1%) | 81.3% | 16.6% (M+ 41.4%) | 0 | 4 (L world 81.3%) | lighter (add-0.3) smoothing helps the fixed test, hurts A to B and SIGN: overfits, not adopted (no progress; streak 1) |
| 38 | 213 | 4.610 (26.5%) **withdrawn: leak, see correction** | 81.3% | 16.6% (M+ 41.4%) | 0 | 4 (L world 81.3%) | the line's opening sign as context: S 4.635 to 4.610, A to B -0.037; SIGN 39.8% / 62.1%, WORD top-10 3.9% (progress; streak 0) |
| 39 | 214 | 4.610 (26.5%; 4.594 with firstpos, not adopted) | 81.3% | 16.6% (M+ 41.4%) | 0 | 4 (L world 81.3%) | opening sign x position lowers S but SIGN / WORD slip (39.7% / 3.4%); prize tasks outrank S, not adopted (no progress; streak 1) |
| 40 | 215 | 4.610 (26.5%) | 84.2% | 16.6% (M+ 41.4%) | 0 | 4 (L world 81.3%) | the slot before a count is restricted in A and B (also without heading lines): new role 'count label', R 81.3% to 84.2% (progress; streak 0) |
| 41 | 216 | 4.610 (26.5%) | 84.2% | 16.6% (M+ 41.4%) | 0 | 4 (L world 81.3%) | LABEL-COUNT grammar rule: G margin A 46.2 to 46.6, B 34.7 to 35.1, F up; real more than shuffled (progress; streak 0) |
| 42 | 217 | 4.610 (26.5%; 4.573 with first2, not adopted) | 84.2% | 16.6% (M+ 41.4%) | 0 | 4 (L world 81.3%) | first two signs as context lowers S but SIGN falls (39.8% to 38.5%): not adopted (no progress; streak 1) |
| 43 | 218 | 4.610 (26.5%; 4.571 with posk/endk, not adopted) | 84.2% | 16.6% (M+ 41.4%) | 0 | 4 (L world 81.3%) | discounted position/end lower S but SIGN slips (39.8% to 39.5%): not adopted; S and SIGN now diverge (no progress; streak 2) |
| 44 | 219 | 4.610 (26.5%) | 84.2% | 16.6% (M+ 41.4%) | 0 | 4 (L world 81.3%) | tails after a count show no name structure beyond frequency-matched chance (no progress; streak 3) |
| 45 | 220 | 4.610 (26.5%) | 84.2% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | no-prefix L profile: L world 81.3% to 85.1% (WALS), 68.3% to 77.0% (Grambank); Burushaski out in WALS only (progress; streak 0) |
| 46 | 221 | 4.610 (26.5%) | 84.2% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | EDGE-DOUBLE grammar rule (set 187's doubling): G margin 47.2 / 35.9, F up; real more than shuffled (progress; streak 0) |
| 47 | 222 | 4.610 (26.5%) | 84.2% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | CAGED-POST grammar rule: G margin 47.3 / 36.0 (small; F unchanged) (progress; streak 0) |
| 48 | 223 | 4.610 (26.5%) | 84.2% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | tails after a mid-line ending are not second names (last signs avoid the head slot in A) (no progress; streak 1) |
| correction | 213 | 4.635 (26.1%) | 84.2% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | loop 38's opening-sign gain was a leak (position 0 conditioned on itself): withdrawn; S 4.635, SIGN 39.7% / 61.8%, WORD 3.4% (streak unchanged, 1) |
| 49 | 224 | 4.635 (26.1%) | 84.2% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | forward weight 0.7 lowers SIGN on both samples; design gain was noise (no progress; streak 2) |
| 50 | 225 | 4.635 (26.1%) | 84.2% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | the post-name tail's head avoidance (A) does not replicate on F (20 tails, p = 0.38) (no progress; streak 3) |
| 51 | 226 | 4.635 (26.1%) | 84.2% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | of Parpola's description families only fish are used alike in A and B (replicates set 183); M+ unchanged (no progress; streak 4) |
| 52 | 227 | 4.635 (26.1%) | 84.2% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | tier 4: one grammar across sites; learned at Mohenjo-daro it parses Harappa nearly as well as its own and vice versa; other sites 36.1 (progress; streak 0) |
| 53 | 228 | 4.635 (26.1%) | 84.2% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | tier 4: one grammar across object types (seal to tablet 43.6, tablet to seal 48.1) and time (late to early Harappa 27.0) (progress; streak 0) |
| 54 | 229 | 4.635 (26.1%) | 84.2% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | tier 4: cage and inner-stroke devices identical at Mohenjo-daro and Harappa (progress; streak 0) |
| 55 | 230 | 4.635 (26.1%) | 84.2% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | tier 4: fish/520 class signal on seals (60/120 vs 4/156) and tablets (14/33 vs 1/47) (progress; streak 0) |
| 56 | 231 | 4.635 (26.1%) | 84.2% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | tier 4: count-label slot restricted in both cities; policy: subset replications no longer count as progress (progress; streak 0) |
| 57 | 232 | 4.635 (26.1%) | 84.2% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | endings not more alike within graphic families than random (low power: 740 dominates) (no progress; streak 1) |
| 58 | 233 | 4.635 (26.1%) | 84.2% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | tier 1: 11 texts on individually made tablets have their referent fixed by the picture (p = 0.001); new V line 0.38% (progress; streak 0) |
| 59 | 234 | 4.635 (26.1%) | 84.2% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | Linear B control of the referent method: 143 words qualify (null 2), but the key was in the wrong ideogram convention; registered verdict stands (no progress; streak 1) |
| 60 | 235 | 4.635 (26.1%) | 84.2% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | tier 2: the picture-referent method passes a Linear B known-answer control (a-mo-ta ROTA, ko-wa MUL): C 3 of 6 (progress; streak 0) |
| 61 | 236 | 4.635 (26.1%) | 84.2% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | short lines of no genre are not bare names (A p = 0.81, B p = 0.051) (no progress; streak 1) |
| 62 | 237 | 4.635 (26.1%) | 84.2% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | tier 1: referent method at phrase level (validated level): 11 sign pairs qualify (null 0); referent line 0.38% to 0.61% (progress; streak 0) |
| 63 | 238 | 4.635 (26.1%) | 84.2% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | seal phrases qualify only with the default one-horned bull; none fixes another animal (no progress; streak 1) |
| 64 | 239 | 4.635 (26.1%) | 84.2% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | family 5-gram overfits (A to B worse); not adopted (no progress; streak 2) |
| 65 | 240 | 4.635 (26.1%) | 84.2% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | pictures confirm the grammar: grammatical pairs picture-diverse, lexical pairs picture-specific on unseen moulded tablets (p = 0.001) (progress; streak 0) |
| 66 | 241 | 4.635 (26.1%) | 84.2% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | pictures: closers untestable on moulded tablets; count-label pairs picture-specific (4 pairs); endings picture-diverse (p = 0.011) (no progress; streak 1) |
| 67 | 242 | 4.635 (26.1%) | 84.2% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | count labels as content words not replicated (3 pairs on tablets; seals alike) (no progress; streak 2) |
| 68 | 243 | 4.635 (26.1%) | 84.2% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | tier 1: 8 referent pairs across distinct moulded designs (gharial, tree 806 158, bull); referent line 0.61% to 0.84% (progress; streak 0) |
| 69 | 244 | 4.635 (26.1%) | 84.2% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | fish pairs more picture-diverse in both samples but not significant (small n) (no progress; streak 1) |
| 70 | 245 | 4.635 (26.1%) | 84.2% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | fish pairs not more animal-diverse on seals; tablet direction does not replicate (no progress; streak 2) |
| 71 | 246 | 4.635 (26.1%) | 84.2% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | phrases tied to object class: 5 pairs (4 tags, 1 pottery); **withdrawn after set 247**: the tag pairs are repeated Lothal sealings of two seals (no progress; streak 3) |
| 72 | 247 | 4.635 (26.1%) | 84.2% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | site-bound pairs all from Lothal sealings (two seals, partial transcriptions counted as distinct texts); artefact (no progress; streak 4) |
| 73 | 248 | 4.635 (26.1%) | 84.2% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | grammar prior in SIGN: +0.2 / +0.1 points, below threshold (no progress; streak 5) |
| 74 | 249 | 4.635 (26.1%) | 84.2% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | the sign before a bare 400 is not head-like (A, B) (no progress; streak 6) |
| 75 | 250 | 4.635 (26.1%) | 84.2% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | LOW-POST grammar rule (400 after a non-head): G margin 47.6 / 36.3, F up (progress; streak 0) |
| 76 | 251 | 4.635 (26.1%) | 84.2% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | SINGLE-DOUBLE and 550-END do not generalise to B or F (no progress; streak 1) |
| 77 | 252 | 4.635 (26.1%) | 84.2% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | tier 1: sign drawings do not match the object's picture (fish signs even avoid fish pictures); link is lexical, not pictographic (no progress; streak 2) |
| 78 | 253 | 4.635 (26.1%) | 84.2% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | sample D (damaged texts, 1,501 new signs): order, stroked jars, fish/520, count label replicate; consistency only (no progress; streak 3) |
| 79 | 254 | 4.635 (26.1%) | 84.2% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | tier 1: pictured fragments add 4 referent pairs (bull, goat, gharial); referent line 0.76% to 0.79% (progress; streak 0) |
| 80 | 255 | 4.635 (26.1%) | 84.2% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | tier 3: blind restoration vs CISI vol. 1 photographs not feasible; 14 of 15 gap signs examined, none legible at the scan resolution (no progress; streak 1) |
| 81 | 256 | 4.635 (26.1%) | 84.2% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | tier 6: names composed by the head-final grammar (2,657 new candidates) never reach the top 10; WORD top-10 stays 3.4%, head-first control identical (no progress; streak 2) |
| 82 | 257 | 4.635 (26.1%) | 84.2% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | tier 7: infill p(sign given both neighbours) takes a small weight on the development split but moves SIGN top-1 39.9% to 39.4%, top-5 61.8% to 62.2%; the two-direction model already holds the neighbours (no progress; streak 3) |
| 83 | 258 | 4.635 (26.1%) | 84.2% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | tier 3: frozen restorations against Parpola's CISI transcription (2 gaps he reads): both miss the top 5 (M-62: 700, predicted 840 60 2 233 3) (no progress; streak 4) |
| 84 | 259 | 4.635 (26.1%) | 84.2% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | S: anti-cache for non-adjacent repeats helps only on the design split; fixed test 4.6354 to 4.6369, A to B worse, SIGN 39.7 to 39.6% (no progress; streak 5) |
| 85 | 260 | 4.635 (26.1%) | 84.2% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | R: head + modifier frame before closers holds on A (pre-closer head-class 26% against 10%, p = 0.0004) but not on B (15% against 13%); roles unchanged (no progress; streak 6) |
| 86 | 261 | 4.635 (26.1%) | 84.2% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | G: CAGE-OPEN (a caged sign opens the line, a name follows) raises the margin A 47.6 to 47.9, B 36.3 to 36.5; MID-POST and NAME-NAME parse shuffles as well as real lines, rejected (progress; streak 0) |
| 87 | 262 | 4.635 (26.1%) | 84.2% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | G: END-PRONE (body + a sign that ends most of its lines: 405 407 526 298 215 423 64 137 136 155) raises the margin A 47.94 to 48.31, B only 36.47 to 36.48 (marginal replication); CLOSER-740 and TWO-BARE rejected (progress; streak 0) |
| 88 | 263 | 4.635 (26.1%) | 84.2% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | G: BODY-400 (3+ lexical signs + 400) and HEADING-BODY (heading unit + lexical body) raise the margin A 48.31 to 49.21, B 36.48 to 36.92; NUM-END lowers both (a count is not written after its label) (progress; streak 0) |
| 89 | 264 | 4.635 (26.1%) | 84.2% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | G: OPEN-PRONE (lexical line opened by an opening-prone sign, closed by a name head) raises the margin A 49.21 to 49.64, B 36.92 to 37.39; LABEL-ANY and NAME-TAIL parse shuffles, rejected (progress; streak 0) |
| 90 | 265 | 4.635 (26.1%) | 84.2% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | G: REVERSED lowers the margin A 49.64 to 32.04 (shuffles parse backwards far more often than real lines: the reading direction is confirmed, no slips recovered); BARE-2 and ENDP-POST add nothing (no progress; streak 1) |
| 91 | 266 | 4.635 (26.1%) | 84.2% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | G: COUNT-3 lowers the margin, HEAD-COUNT parses no new line, CAGE-MID adds 0.1 on A (below 0.3) (no progress; streak 2) |
| 92 | 267 | 4.635 (26.1%) | 86.1% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | R: edge roles from the new frames replicate on B (end-prone signs end 53% of their B occurrences, openers open 61%, 400 line-final 89%); R 84.2% to 86.1% (progress; streak 0) |
| 93 | 268 | 4.635 (26.1%) | 86.1% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | tier 7: a grammar prior (candidate completes a parsing line) takes full weight on the development split but moves SIGN top-1 39.9% to 39.8%, top-5 61.8% to 62.1% (no progress; streak 1) |
| 94 | 269 | 4.635 (26.1%) | 86.1% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | G: NUM-INFIX, OPEN-NUM, MULTI-COUNT each fail on A or B; numerals inside short lines follow no frame shuffles lack (no progress; streak 2) |
| 95 | 270 | 4.635 (26.1%) | 86.1% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | R: head roles in the new frames not supported: OPEN-PRONE last sign head-class on B only (8/21 vs 2/39), not A (2/16 vs 2/29); the sign before 400 is never head-class (0/16; fits LOW-POST) (no progress; streak 3) |
| 96 | 271 | 4.635 (26.1%) | 86.1% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | G: two-sign frames with strict heads parse nothing new (the bare rule already covers them); H-LOW lowers both margins (no progress; streak 4) |
| 97 | 272 | 4.635 (26.1%) | 86.1% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | S: modified Kneser-Ney trigram discounts (D1 0.79, D2 1.22, D3+ 1.22) no better than one D = 0.75 (4.6354 to 4.6357; A to B worse; SIGN 39.7 to 39.6%) (no progress; streak 5) |
| 98 | 273 | 4.635 (26.1%) | 86.1% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | G: NAME-COUNT and PRE-NAME lower both margins; TWO-400 raises A 0.27 (below the 0.3 threshold), B 0.19; not adopted (no progress; streak 6) |
| 99 | 274 | 4.635 (26.1%) | 86.1% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | tier 6: two-direction WORD scorer, top-10 8 to 10 of 232 names (3.4% to 4.3%), below the 1-point threshold; top-1 still 0 (no progress; streak 7) |
| 100 | 275 | 4.635 (26.1%) | 86.1% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | end-prone signs are not alternative name endings: their bodies are attested name bodies 1 of 15 (A), 0 of 21 (B), no more than before 400 (no progress; streak 8) |
| 101 | 276 | 4.635 (26.1%) | 86.1% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | R: the slot after the counted sign is not restricted (entropy 5.82 vs 5.95 on A, p = 0.16; 5.26 vs 5.39 on B, p = 0.20); no count-complement role (no progress; streak 9) |
| 102 | 277 | 4.635 (26.1%) | 86.1% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | G: closers, 400 / 90 and 740 / 520 do not open lines before names (all lower both margins); the cage alone does (no progress; streak 10: **stopping rule met**, 25 Sept 2026) |
| 103 | 278 | 4.635 (26.1%) | 86.1% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | new run (owner's goal, 25 Sept). tier 7: SIGN ensemble over decade and description families 39.8% to 39.5% top-1, 61.9% to 61.7% top-5 (no progress; streak 1) |
| 104 | 279 | 4.635 (26.1%) | 86.3% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | R: the heading is a two-sign unit on B too (83% of 817 / 820 / 861 openings take 2 / 60 / 1); its second sign gets the role, R 86.1% to 86.3% (small); heading-body last signs are not heads (A p = 0.45, B p = 0.56) (progress; streak 0) |
| 105 | 280 | 4.635 (26.1%) | 86.3% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | S: object-class prefix raises S (4.6354 to 4.6748), A to B much worse (the class splits sparse start contexts; B lines mostly unknown class), SIGN 39.7 to 39.5% (no progress; streak 1) |
| 106 | 281 | 4.635 (26.1%) | 86.3% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | R: doubled signs prefer line edges on A (62% vs 43%, p = 0.0004) but not significantly on B (56% vs 46%, p = 0.061); edge-double role not adopted (no progress; streak 2) |
| 107 | 282 | 4.635 (26.1%) | 86.3% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | tier 3: frozen restorations vs Mahadevan 1977 read 12 of 15 gaps top-1, but 8 cases are circular (the completed line is in the training data); clean cases 4 of 7 top-1, 5 of 7 top-5, below the 10-case minimum; withdrawn, no progress (streak 3) |
| 108 | 283 | 4.635 (26.1%) | 86.3% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | tier 3: restorations of ICIT-illegible signs, model retrained without copies of each text, against Mahadevan 1977: top-1 4 of 15 (27%), top-5 9 of 15 (60%), frequency baseline 3; meets the registered rule narrowly (progress; streak 0) |
| 109 | 284 | 4.635 (26.1%) | 86.3% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | tier 3: copy-free restorations replicate on 34 new M77-read gaps: top-1 17 (50%), top-5 23 (68%), baseline 3; 10 of the 17 hits are structural slots (heading 861 / 817 before 2, final 740 / 527), 7 lexical (progress; streak 0) |
| 110 | 285 | 4.635 (26.1%) | 86.3% | 16.6% (M+ 41.4%) | 0 | 4 (L world 85.1%) | tier 3 validation: against a context baseline (commonest sign between the same neighbours) the model wins narrowly, 21 against 19 of 49, lexical cases 10 against 7 of 29; the line stands with that caveat (no progress; streak 1) |
