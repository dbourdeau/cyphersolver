# Linear A: source collation and word-form constraints

23 September 2026. Status: in progress. This continues the first accounting report; it does not claim a decipherment.

## Result

A conservatively collated sample contains more one-sign extensions of existing word forms than either of two simple randomized models predicts. It gives a short list of relationships worth examining, but does not establish affix meanings, grammatical cases, or a language family. The apparent excess of suffixes over prefixes is not supported by these tests.

## An independently maintained source

Imported the public [SigLA dataset](https://sigla.phis.me/), by Ester Salgarella and Simon Castellan, under CC BY-NC-SA 4.0. The snapshot contains 802 document records and 5,144 sign attestations: 4,712 labelled confident, 44 doubtful, and 388 without an identified sign label. The binary snapshot and retrieval receipt are retained locally. Both binary payloads pass their declared byte-length and object-count checks.

The positional layout was initially located through Christos Tsirkas's existing decoder, not discovered independently here. However, its `bounds_of` function labels an embedded pair as boundary states. That interpretation is inappropriate for this dataset: the pair is **position within word, word index**. On HT13 the first four signs have pairs `(0,0), (1,0), (2,0), (3,0)` and form KA-U-DE-TA. The final two syllabograms have `(0,7), (1,7)` and form KU-RO. SigLA's published word pages confirm these groupings. All 1,401 recovered groups have contiguous offsets from zero.

Six checks against SigLA's own static pages validate two word groups, three sign functions, and a doubtful reading. The doubtful NA at HT37 occurrence 17 carries the HTML class `unsure-reading`; extracting text alone hides this qualifier. Evidence links and content hashes are in `sigla_collation_results.json`.

**Limits:** confidence concerns a sign identification, not its phonetic value or whether the containing word is complete. SigLA's inventory omits ordinary integer quantity strokes; it cannot supply every uncertainty needed for arithmetic. Both corpora predominantly descend from GORILA, so agreement is corroboration of transcription, not independent confirmation of an ancient meaning.

## Sample construction

We align sequences of multi-sign groups in source order, using standard sign identifiers rather than sound values. Variant letters are collapsed for basic sign-identity comparison. Only uniquely matched document names are used; aliases such as HT123a / HT123+124a are left unresolved rather than guessed.

| Filter | Count |
|---|---:|
| SigLA word groups | 1,401 |
| SigLA multi-sign groups | 1,094 |
| Confident, unerased, non-ghost multi-sign groups | 943 |
| Shared unique document names | 685 |
| Multi-sign tokens aligned exactly across the editions | 824 |
| Matched tokens with confident/unmarked SigLA signs and no extra damage characters in the other edition's group | 612 |
| Distinct word forms in that final sample | 420 |

There are only five stone-vessel tokens in this conservative intersection. It is unsuitable for drawing strong conclusions about the ritual formula; a separately collated ritual corpus is still needed.

## Experiment

For each distinct word form W, count relations W → W+S and W → S+W where S is one sign and W has at least two signs. Count distinct form pairs, not repeated tokens. All forms and tests are exploratory: the families were inspected before simulation.

Two randomized baselines are used:

1. Shuffle each sign-position column separately within each word-length class, preserving length and position-specific sign frequencies.
2. Shuffle signs within each word, preserving each word's sign inventory and length.

Both reject collisions within each length class, so every simulated vocabulary has exactly the observed number of distinct forms at each length. This improves on a preliminary run which allowed duplicate shuffled forms to reduce the vocabulary size. Only the corrected run is reported below.

There are 5,000 replicates per model and subset, with random seed 20260923. The complete output reports 48 tests: eight statistics, two models, three subsets. Reported adjusted p-values use Bonferroni correction across all 48. These nulls assess ordered string structure, not whether a particular linguistic interpretation is correct.

| Sample / statistic | Observed | Position-by-length null mean | Within-word null mean |
|---|---:|---:|---:|
| All 420 types: prefix or suffix extensions, base ≥2 | 42 | 23.11 | 25.93 |
| All types: extensions, base ≥3 | 5 | 0.68 | 0.55 |
| Excluding HT104: extensions, base ≥2 | 41 | 22.52 | 25.19 |
| Haghia Triada tablets only: extensions, base ≥2 | 21 | 12.05 | 15.32 |

For all types and bases ≥2, both adjusted Monte Carlo p-values are approximately 0.0096. Removing HT104 retains the broad signal (adjusted p approximately 0.0192 and 0.0096). The Haghia Triada-only results do **not** clear the 48-test correction. This could reflect reduced power, sampling differences, or pooled effects; it is not evidence that the site lacks morphology.

The full sample has 24 suffix and 18 prefix relations. Its difference of six is ordinary under these nulls; it does not justify calling the language predominantly suffixing. The longer-base result is also sensitive to the model and subset. All statistics, including these limitations, remain in `word_extension_results.json`.

## Specific candidates and a failed inference

The five longer-base relations are listed below using conventional sound labels for readability. The computation uses sign IDs. All these forms are previously published; no discovery of a new inscription or lexical reading is claimed.

| Relation | Useful witnesses | Unresolved issue |
|---|---|---|
| DA-KU-SE-NE / DA-KU-SE-NE-TI | HT103, HT104 | TI may instead be a separate ideogram; Younger explicitly notes this alternative on HT104. |
| RU-MA-TA / RU-MA-TA-SE | HT29, HT99b, ZA20 | Different sites and contexts; extension need not be inflection. |
| PA-RA-NE / A-PA-RA-NE | HT115a/b, HT96a/b | Two artefacts, not four independent witnesses; both assigned to HT Scribe 8. |
| SI-KI-RA / A-SI-KI-RA | HT8a, KH20 | Cross-site and commodity context changes. |
| TA-NA-TE / A-TA-NA-TE | ZA10a | Same tablet, both ordinary entries with quantities. |

The PA-RA-NE family suggests a tempting hypothesis: A- marks a heading. Its unprefixed form occurs as an entry on HT115 while A-PA-RA-NE forms part of headings on HT96. **That general rule fails on ZA10a**, which has TA-NA-TE 2 and A-TA-NA-TE 1 in equivalent entry positions. A-SI-KI-RA also occurs with a quantity-bearing commodity entry on KH20. This does not exclude a grammatical use of A-, but the function cannot be assigned from one pair.

The HT104 case prevents a second overreach. Each of its three item labels ends in TI. That distribution fits either a repeated ending or a common following sign serving another function. The alternative is explicitly recorded in [Younger's HT104 commentary](https://github.com/mwenge/lineara.xyz/blob/43fe7cf1abc8e6bb1ea3228c3a1bd5938709620a/commentary/HT104.html). Corpus agreement about grouping does not settle the ancient syntax.

## What this changes

The next analysis can use verified word positions, function classifications, and explicit sign uncertainty rather than treating all digitized strings alike. The priority hypotheses are the functions of A- and terminal TI, with their counterexamples preserved. Statistical structure alone cannot choose among morphology, related names, compounds, spelling conventions, or imperfect segmentation.

No new English translation is warranted. The full goal of reading Linear A remains unachieved.

## Reproduce

```
python lineara/sigla_decode.py
python lineara/collate_sigla.py
python lineara/test_word_extensions.py
python docs/_check_profile.py lineara
```

The decoder implements the relevant [OCaml serialization format](https://github.com/ocaml/ocaml/blob/5.3/runtime/caml/intext.h) and never executes downloaded JavaScript. Raw and derived corpora remain in ignored `data/`; SigLA-derived data retain its attribution and CC BY-NC-SA 4.0 terms. See `sigla_manifest.json`, `sigla_collation_results.json`, and `morphology_source_manifest.json` for provenance. The [SigLA methods paper](https://doi.org/10.36824/2020-graf-salg) and [interface help](https://sigla.phis.me/help.html) explain the original database.
