# LJS 51 — why 22r.1 and 61r.3 resist a blind solver, and a word-level solver

Verification only. No reading or key file of `ljs51corpus` is changed. This follows the blind character-level run in `../blind-confirmation/` (#1055), where 22r.1 (167 signs) and 61r.3 (113 signs) stayed at chance (0.11 and 0.10), while chains of 56-60 signs passed.

## 1. Diagnosis (exploratory; both chains are spent for a blind test)

The two chains were opened with the existing keys (`keys_eye/22r.1.json`, `keys_eye/61r.3.json`, base d8ac608093). Files are in `diagnosis/`.

**The keys and the plaintexts are not at fault.**
- Counts match: 167 signs = 167 letters and 39 groups = 39 words (22r.1); 113 = 113 and 38 = 38 (61r.3).
- Consistency is 99.4 % and 99.1 %. The keys decode the plaintexts word for word.
- There are no nulls, no word transposition and no second hand. The only breaks are the ones already listed in the key files: `e` = ع/ز (22r.1) and `S16` = ش/س (61r.3).

**The search is not at fault either: the model is.** Under the #1055 objective (4-gram log P − 8 × surplus classes), the wrong blind decoding beats the true plaintext. See `objectif_tout.tsv`.

| chain | log P of the plaintext | log P of the blind decoding | gap |
|---|---|---|---|
| 22r.1 | −484.1 (−2.36/symbol) | −431.7 (−2.11) | −52 |
| 61r.3 | −435.6 (−2.90/symbol) | −304.5 (−2.03) | −131 |

The same solver was run on 7 shuffled controls per chain (`temoins_ancien_modele.txt`). They score −2.33 to −2.49 per symbol on 22r.1, so the true plaintext (−2.36) is at the level of a control. They score −2.18 to −2.45 on 61r.3, so the true plaintext (−2.90) is below every control.

**There are two different causes.**
- **22r.1**: heavy homophones and rare vocabulary. It has 32 classes for 23 letters: 10 singletons, three shapes each for ل and ع, two each for ت, ن, و and ش. Its ṭawīl verses use rare words such as التهاتر, كالليوث and الخوادر.
- **61r.3**: the genre of the plaintext. It is a list of 38 opposite imperatives (صل / اقطع، مر / انه، ابك / اضحك …), 3 letters per word on average, with almost no article or function word. It has no homophones.

**Things that do not explain it.**
- A 4-gram model trained on nine times more text (26 M symbols) does not help: the plaintexts score −2.355 and −2.956.
- Lām-alif is written as a single sign (`LA`, twice in 22r.1), which a one-letter-per-class solver cannot represent. This costs only a few nats.

**What predicts the outcome.** Across the 15 divided chains of #1055, the per-symbol log P of the true plaintext predicts the result:
- at −2.23 or above, 7 of 9 chains pass;
- at −2.28 or below, none of 7 passes, except 20r.8+47r.1 (336 signs).

## 2. Hypothesis and single measurement

The protocol is in `freeze/PREREG.md` (French, frozen). Manifest sha256: `3674e420234eeef1ee8fd3366b85ac2fae9e729a8397f80ab006fcae530e5bca`, frozen 2026-11-28T19:57:32Z and posted on #1023 (issuecomment-7244936167) before the run. The run took 19:58:27Z → 20:41:18Z.

**Hypothesis.** A word-level objective breaks more long divided chains than the character-level solver of #1055, under the same search settings. It is supported if, on 10 fresh chains, the word-level solver validates at least 2 more chains.
- Each group scores log((c+0.5)/N) if it is in a lexicon of 124,376 attested forms (9 OpenITI texts, `model/CORPUS-LM2.txt`; Ibn Nubāta and Ṣubḥ al-aʿshā excluded).
- Otherwise it scores 4-gram log P + ρ.
- The settings are ρ = −5 and λ = 8, tuned only on the 16 divided chains already spent in #1055 (`devgrid1.txt`).

**Fresh chains.** These 10 chains were never measured. The selection rule is in `scripts/selection2.py`: the longest eligible chains, with a 12-gram leak of 5 % or less against both corpora.

**Rule.** For each chain and each solver: character agreement with the compiler's plaintext ≥ 0.85, and ≥ the best of 200 shuffled-ciphertext controls + 0.30.

| chain | signs | classes | word-level | best control | pass | char-level | best control | pass |
|---|---|---|---|---|---|---|---|---|
| 87v.8 | 130 | 22 | 0.93 | 0.35 | yes | 0.98 | 0.37 | yes |
| 96r.2 | 128 | 22 | 0.72 | 0.37 | no (1st/201) | 0.18 | 0.34 | no (chance) |
| 83r.13 | 100 | 23 | 0.93 | 0.36 | yes | 0.84 | 0.39 | no |
| 77v.9 | 94 | 21 | 0.86 | 0.35 | yes | 0.78 | 0.36 | no |
| 84r.12 | 93 | 24 | 0.91 | 0.31 | yes | 0.92 | 0.31 | yes |
| 104v.2 | 90 | 19 | 0.98 | 0.39 | yes | 0.98 | 0.40 | yes |
| 1v.3 | 90 | 20 | 0.87 | 0.37 | yes | 0.88 | 0.38 | yes |
| 43v.11 | 89 | 23 | 0.96 | 0.36 | yes | 0.96 | 0.35 | yes |
| 86r.9 | 89 | 23 | 0.39 | 0.35 | no | 0.26 | 0.33 | no |
| 94r.3 | 89 | 22 | 0.94 | 0.36 | yes | 0.96 | 0.34 | yes |

**Result: the word-level solver validates 8 of 10 chains, the character-level solver 6 of 10. The hypothesis is supported, at exactly the pre-registered threshold.**
- The word-level solver loses no chain that the character-level solver validates.
- It lifts 96r.2 from chance (0.18) to first of 201 (0.72).
- Where both pass, it is sometimes a few points lower (87v.8: 0.93 against 0.98).
- 86r.9 fails with both solvers.

Full rows are in `results/RESULTATS.tsv`.

## Limits

- The sign classes were made with knowledge of the plaintext, as in #1055.
- The lexicon comes from texts that may contain verses of the volume. The 12-gram control rules out whole verses, but not single rare words.
- The margin is the minimum that counts (+2 on 10 chains). It is one run only.
- 22r.1 itself is not re-measured: it is spent. In development the word-level solver reached 0.56 on it, against 0.11. 61r.3 stays at chance (0.17), as predicted for its genre.
- The freeze uses a posted hash rather than `tools/holdout/freeze.py` (#1014), for the same reason as #1055.
- The lexicon binary (`lex.bin`, 1.5 MB) and the character model (`../blind-confirmation`, not versioned) are not committed. Their sha256 values are in the manifest.
- The scripts contain the local absolute paths they were frozen with.

Credit: dudout (verification). Keys, transcriptions and plaintexts are D. Bourdeau's (`keys_eye/`, `chains_all.json`).
