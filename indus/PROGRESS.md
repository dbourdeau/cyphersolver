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
| 1 | V meaning, checked | share of sign tokens read as sense and checked against archaeological evidence: the object's iconography (copper tablets, seal motifs), its function (weights, tags, pottery), its find context, West Asian texts naming Meluhha. Numerals reported beside it (their sense is the count). | 0.008% (4 copper-tablet signs); numerals 16.6% |
| 2 | C positive-control gate | a method proposing sound values or readings must first recover a known answer (Linear B -> Greek). Methods that passed / were run | 1 passed (set 179); key bench failed (Ventris's Linear B key beaten by 11-41 of 100 shuffles, `linb_control.md`); rebus search not run |
| 3 | U vault | share of tokens in texts never used to fix the values (B's new lines; later, newly excavated finds) read as sense with values fixed beforehand | 0 (no sound value has passed) |
| 4 | A archaeological consistency | readings or structure hold across sites, periods, duplicates and sealings of the same seal | supporting: fish/520 signal holds at all sites and periods (set 196) |
| 5 | L language, against genre-matched decoys | the typology narrows the field (L world); a language claim must beat typology-matched decoys of the same genre | L world 81.3% / 68.3%; no candidate beats the decoys inside the fifth (set 198) |
| 6 | WORD task | hide a name body in a held-out line; rank all training bodies; top-1 / top-10 against frequency | 0% / 3.0% (frequency 0% / 1.3%) |
| 7 | SIGN task | hide one sign; rank the 150 commonest signs; top-1 / top-5 against frequency | 36.2% / 58.4% (frequency 9.6% / 22.4%) |
| - | diagnostics | S bits/sign, R roles, G margin, M+ | S 4.685, R 81.3%, G 46.2 / 34.7, M+ 41.4% |

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
| S structure | held-out bits per sign on a fixed 80/20 split (seed 2026) of the distinct lines, best registered model | lower |
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
2026): the loops continue until 10 consecutive loops make zero progress.

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
