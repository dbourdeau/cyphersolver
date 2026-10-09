This audit uses only the supplied files. All positions below are zero-based cipher-group positions; source file lines are one-based. `review_analysis.py` and `context_simulation.py` write exclusively into this directory and never import or execute the claimant's programs. `input_sha256.tsv` identifies the source snapshot.

Independent structure test

`independent_pairs.tsv` records every local alignment with its cipher position, source line, and literal clear-text quotation. There are 98 distinct normalized group/reading pairs, 95 after removing three explicitly multiword title labels; 87 ordinary pairs are Dutch. These are a small manual sequential-alignment sample, not a comprehensive, blinded gold alignment. Ambiguous ordinal matches and inflection differences are retained, not corrected or rejected because of alphabetical order. French sampling is intentionally sparse: its word/syllable segmentation makes a naive one-group/one-word alignment invalid. The published table never enters this test. The reviewer saw the claimant's hypothesis and programs before selecting fragments; therefore this is computationally independent reconstruction, not preregistered discovery.

| Layout | Global Spearman, 95 ordinary pairs | Within fixed 500-number blocks |
|---|---:|---:|
| Ordinary numeric / row-wise numbering | .857764 | .350504 |
| 4 columns, 100 rows | .848573 | .566970 |
| 5 columns, 100 rows | .873963 | .799373 |
| 6 columns, 100 rows | .842357 | .644843 |
| 10 columns, 100 rows | .828350 | .799373 |
| 100 columns, 10 rows | .783339 | .053847 |
| 5 columns, 100 rows, one-based | .873963 | .799373 |

The Dutch-only five-column result is global .869270, within .780625. Including all three title labels gives global .835860, within .705487. These are sensitivity checks, not competing estimates of a perfectly known alignment.

Spearman uses averaged ties, unlike the claimant's insertion-order-dependent ranking. Within-block scores weight blocks by sample size and exclude blocks having fewer than four observations. Ten thousand within-block label permutations, taking the maximum over all seven tested layouts, give null p99.9=.368032 and no exceedance (plus-one p=.000100). This tests association conditional on these sampled pairs, not the probability that this exact historical physical codebook existed. Pair dependence, manual fragment selection, and layout searches outside the tested family remain limitations.

The five/ten-column within-block tie is mathematical, not accidental: with the half-thousand fixed, both mappings order by `line`, then `hundreds`. The statistic cannot choose between them. Five columns wins the tested global ordering, which does use cross-half boundaries; the advantage over ordinary numeric order is only .0162 in this sample. Zero/one-based interpretations also tie here. Sparse ordered fragments cannot establish physical sheets, a single complete bilingual list, or an exact cutoff at alphabetical position 3150.

Homophone evidence survives: the independent ordinary pairs include en=541/641/841/941, whose proposed positions are 705/706/708/709, and of=1550/1650 at 1750/1751. Observed adjacent/repeated values support local runs; unobserved intervening cells are not independently established. Names/titles such as 3273 and 3610 map to 3367 and 3551, but a few examples do not locate a sharp boundary. The threshold is an alphabetical index, not a raw cipher number.

Circularity and validation leakage

* `blocktest.py:5,26-27` computes the advertised association from `pairs_v1.py`, excluding six mappings with five name labels (including Salonika). The header of `pairs_v1.py` asserts pre-hypothesis alignment; the available files do not prove its chronology. It would be incorrect to claim this particular .80 statistic was computed from the final monotone table.
* Independently recomputing **all 95 early pairs, without exclusions**, gives five-column global .828310, within .601750 (numeric within .166328; four-column .386491; six-column .494026; ten-column .601750). The same seven-layout, 10,000-permutation null has p99.9=.367727, no exceedance. Removing the explicitly named entries reproduces .803619 within-block on 89 pairs. Thus association survives the no-exclusion attack, with a materially weaker effect.
* `core.py:1` explicitly says CORE was chosen using slot fit. `boot2.py:54-65` reinserts CORE, admits other candidates only if slot cost <=.3 and one-to-one, then takes a weighted monotone subsequence. Final-table correlations and confidence counts consequently cannot independently validate alphabetical order.
* `holdout.py:11-20` derives the test reference alignment using **full-data anchors**. Lines 31-37 temporarily remove held CORE values only from a local seed. `boot2.py:54-56` then reinserts the module's complete CORE on every build. The first held segment contains 74 distinct CORE keys / 143 occurrences; all 13 held segments collectively contain 265 CORE occurrences. These counts describe reintroduced candidates, not guaranteed retained/graded predictions after the monotone filter.
* `holdout.py:22-24` accepts prefix matches of length >=3 as correct: the published “exact” precision is not exact-word accuracy. It reports precision conditional on prediction class, not accuracy over every held token. Its slot comparison additionally accepts prefixes and compares to an unconditional token-frequency sample of crib words, not a grammar/context-matched alternative. Neither 94% nor 74% versus 2% is a leakage-free predictive validation. This audit does not fabricate replacement percentages.
* `parse.py` splits the doubtful token `2?4?` in R2121 cipher line 57 into two groups, 2 and 4; preserving it as one unknown gives 630 groups versus its 631. All earlier witness positions cited here are unaffected. Its late segment offsets must be reassessed.

Slot widths and selection

`slot_audit.tsv` lists bounds, neighbouring codes, cell gaps, every finite-vocabulary candidate, and strict/prefix compatibility for all requested context readings. The Dutch observed vocabulary has 516 normalized forms; the claimant-style mixed vocabulary has 994 normalized forms / 1024 surface forms. Both contain editorial material and are **not Dutch dictionaries**. Counts are inclusive lexical-form counts for these finite vocabularies, not estimates of all Dutch words. Prefixes, compounds, variant spellings, and syllabic encodings can expand possibilities further; actual codebook inventories may instead exclude many corpus words.

| Target / reading | Normalized neighbours | Dutch observed / mixed forms | Strict fit |
|---|---|---:|---|
| R2131 verklaard | verbinden–verkriigen | 6 / 9 | yes |
| heeft | hebben–heeren | 4 / 5 | yes |
| gedurende | gedaane–geeft | 6 / 10 | yes |
| deze | dewiil–dezelve | 2 / 2 | yes |
| Franschen | fasse–gantsch | 4 / 19 | yes |
| sig | ses–sincerement | 0 / 4 | yes |
| den, position 31 | demarches–denkt | 2 / 3 | yes |
| neutraliteit | negociations–niet | 2 / 5 | yes |
| houden | houd–iaar | 5 / 6 | yes |
| R2122 verlangen | verkriigen–verzoek | 10 / 18 | yes |
| ontrent | onderhandeling–ook | 3 / 9 | yes |
| -er | entrer–est | 2 / 9 | yes |
| negociatie | negociations–niet | 2 / 5 | **no** |
| in | in–informee | 1 / 4 | yes |
| moeten | moest–moiiens | 4 / 7 | yes |
| laaten | la–landen | 1 / 3 | yes |

A chosen word may fit while being absent from the finite vocabulary (e.g. verklaard, heeft, deze, sig, ontrent, laaten). Thus the counts must not be misread as full option counts including every claimed word. `vocab.py:4-28` explicitly adds Franschen, neutraliteit, verlangen and other contextual possibilities in EXTRA; their appearance among candidates is not independent discovery. `negociatie` falls below `negociations`; spelling `negotiatie` would fit, which makes spelling uncertainty a required explicit hypothesis, not a disproof of the general negotiation theme. In the Dutch crib `negociatie` already occurs at clear line 20; it has not been lost merely to modern normalization.

Code 745 has no entry in the final table: its neighbours are `entrer` and `est`. `readings.py:24` explicitly overrides its target rendering to `-er` at R2122 position 194; the early `pairs_v1.py` instead proposed `men`. The key passage repeats en=641 after both “verlangen” and “moeten”; treating these as suffixes requires a new segmentation, not silently removing twice-attested groups. The supplied output includes no separate `[de]` before Republicq or `[den]` between aan and Envoyé. R2131 also has unresolved 591 after “verklaard”, and 319/502 before “neutraliteit”. These gaps prevent treating the complete proposed prose as an already coherent decrypted sentence.

What the simulations do and do not show

1. At original clause anchors and original slot bounds, 100,000 uniform random draws from eight explicitly listed diplomatic/grammatical choices at each of three variable positions give R2131 548 fitting clauses (exact enumeration 3/512=.586%) and R2122 834 (exact 4/512=.781%). Exhaustive adaptive selection finds all three/four. With 1000 independent attempts, stipulated success probabilities are 99.720% / 99.961%. Examples: “gedurende deze Oorlog met de Franschen” and “... met de Friezen”; “het verlangen/verzoek van Porta ontrent het doen eener negotiatie/negotie in de Republicq”. Friezen is a grammatical nationality alternative, **not evidence for historical involvement**. Spellings are not independent semantic alternatives. These are deliberately illustrative clause-level rates, not estimates of how often real analysts hallucinate an entire letter.
2. Whole-passage accounting: R2131 positions 15–34 has 20 groups, 8 A/B, 1 title, 7 C, 3 weak, 1 unresolved. R2122 positions 184–203 has 20 groups, 11 A/B, 2 titles, 7 C. Therefore even accepting all A/B grades provisionally, only 40% / 55% of these key spans are fixed A/B cells; titles raise that to 45% / 65%. These are group counts, not probabilities or percentages of correctly read words.
3. A second simulation preserves the **full** 20-cell lengths, fixed A/B/title counts, and unknown-slot widths using grammatical diplomatic sentence templates. Each trial assigns independent random circular lexical intervals of those widths; an analyst can choose the best word from every role's listed synonyms. Each template yields **0/200,000** full completions (model-specific zero-hit 95% upper bound .00150%). This is evidence that tight slots can be highly restrictive for a fixed grammar template. It does **not** support a claim that arbitrary full diplomatic sentences routinely fit. Templates, dictionaries and interval distributions are stipulated; they do not reproduce the actual anchors or unconstrained human reading process. A defensible analyst false-reading rate still needs blinded readers, withheld cribs, preregistered slot/spelling rules and a larger independent lexicon.

Full files: `context_simulation.json`, `full_sentence_simulation.json`. No false-positive frequency from either toy model is transferred to the historical claims.

Independent attestations of requested words

| Value | Cipher witness | Contemporary clear witness | Assessment |
|---|---|---|---|
| 1764 Oorlog | R2121 #486, line 44, `1764 1650 421 1012 ...` | R2121 clear line 57, “Oorlog of andere groote Schepen” | Strong local alignment, **one** occurrence. Context is warships, not proof that the target describes a war against France. |
| 1518 met | R2121 #10, line 5 | Clear line 6, “onderhandeling met den Reis Effendi” | Strong local witness; further cipher occurrences #93,119,602. |
| 86 de | R2053 #5, cipher line 2 | R2053 clear line 1, “Articles de la Lettre ...” | Direct de; R2121 #11 / clear line 6 actually has **den**, so article inflection is not strictly one-to-one. |
| 3373 Porta | R2121 #180, cipher line 16 | R2121 clear line 23, “dat de Porta vooraf ...” | Local title identification. |
| 3273 Porte/Ottoman Porte | R1947 #42, cipher line 6; R2053 #28, line 4 | R1947 clear line 10 “la Porte Ottomanne, lui”; R2053 clear line 1 “à la Porte Ottomanne un certain ...” | Strong referent; literal extent and Dutch Porta spelling remain uncertain. |
| 3610 envoy title | R1947 #407, cipher line 39; R2053 #9, line 2 | R1947 clear lines 36–37 “Mons= l'Envoijé de Prusse”; R2053 clear line 1 “l'Envoyé de Prusse” | Envoy referent well supported; exact entry could include “de Prusse” and articles. A bare generic ENVOYE is not uniquely established. |

The complete occurrence lists are in `results.json`. These are source alignment claims, not new documentary verification against manuscript images.

Word assessment policy and historical sanity

SOLID means a strong local crib correspondence or visible plaintext, allowing documented inflection; PLAUSIBLE means compatible grammar/slot or uncertain entry extent, not directly proved; SPECULATIVE means semantic content chosen by context, an unsupported insertion, or a contradiction requiring extra assumptions. Neither dictionary rank nor contextual naturalness alone makes a reading SOLID.

R2121 clear lines 39–43 explicitly discuss a loan of 7–8 million and its interest. A financing/negotiation theme for a January 1789 continuation is therefore plausible, not a decipherment. R1947 discusses wars and mediation (clear lines 13–14,32–38). R2131's date is supplied only by its transcription header here; these files give no independent statement of the claimed February 1793 French-war/neutrality message. No external chronology or travel-time assumption is used to rescue the reading.

Publication fixes: independently re-align and adjudicate every crib token (including doubtful groups and multiword titles); freeze the code inventory, spelling rules and allowable segmentation before testing; rebuild anchors within each fold without full CORE or full-data alignment; score exact words separately from prefixes and report coverage separately from conditional precision; test entirely unseen documents; compare global and within-block layout scores with a prespecified family; publish corpus-limited slot alternatives and identify all contextual insertions. The output's whole-letter A/B coverage is 103/255=40.4% for R2122 and 14/46=30.4% for R2131, before title/context additions. The advertised 55%/63% are transcription-group coverage including guesses, not validated word accuracy.
