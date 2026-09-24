# Linear A: first research pass, 23 September 2026

**Status: in progress. No new decipherment, language identification or lexical translation.**

The useful result of this pass is a reproducible corpus audit and an accounting test that distinguishes established interpretations from misleading numerical coincidences. Linear A remains undeciphered in the recent scholarly sources consulted, including [Salgarella 2025](https://doi.org/10.1017/9781009520041). Conventional Latin-letter readings are provisional sound labels; displaying them is not translating the language.

## Data and reproducibility

The working source is Robert Hogan's [Linear A Explorer repository](https://github.com/mwenge/lineara.xyz), which draws on GORILA, George Douros's tabulation and John Younger's commentary. `source_manifest.json` pins commit `43fe7cf1abc8e6bb1ea3228c3a1bd5938709620a` and the downloaded file's SHA-256. The analysis reads glyph strings and encoded numerals; supplied English glosses are removed. A static parser handles the JavaScript data format without executing it.

This snapshot contains **1,722 records, 1,721 distinct record names, and 436 records marked Tablet**. These are software records, not independent artefact counts. Faces, fragments and other supports matter. The schema has two KH101 records, one with an empty transcription; KNZg57b has a glyph array but no matching transliteration array.

Comparing the physical-line transcription field with the concatenated segmented-word field gives:

| Relationship, ignoring whitespace | Records |
|---|---:|
| Identical | 610 |
| Empty transcription field, populated segmented field | 886 |
| Only placement/number of damage markers differs | 130 |
| Other differences needing classification | 96 |

**These counts are not error counts.** Differences include fraction composition, ligature treatment, editorial ordering and omitted marks. For example, HT9a has separate J+E signs in one field and their 3/4 equivalent in the other. HT10a reorders an entry. Source fields must not be silently treated as interchangeable.

The repository's measurement utility counts 8,290 encoded Linear A signs and Aegean numeral code points, 345 distinct, in the segmented snapshot export. Numerals, fractions and ligatures are included; damage markers, dividers and private-use characters are excluded. This is neither the size of the ancient sign inventory nor an independent archaeological corpus census.

## Accounting experiment

The first search deliberately applies a simple rule without assigning English meanings: test whether a multi-sign group followed by an integer has that integer equal to the sum of preceding numeric entries. It excludes non-tablets, duplicate-name records and sections containing damage or fractions; a horizontal rule starts a new section. At least two earlier numeric entries are required.

There are 44 qualifying opportunities across 38 candidate sign groups. KU-RO produces two exact matches in four opportunities. SA-RU produces one match in one opportunity. The latter is the accidental-looking equality 10 + 10 = 20 on HT95a. On HT95b, SA-RU is instead the first entry after the heading; HT86a places it among other recurring labels. **The isolated equality does not justify translating SA-RU as “total.”** The follow-up was chosen after seeing the result and is not a blind holdout test.

The screen also misses known totals when its section boundaries are wrong. On HT88, summing the whole preceding tablet gives 39, whereas the appropriate KI-RO-headed section gives six. HT119's displayed earlier entries sum to 159 while its total is 160. Neither failure alone refutes the established KU-RO interpretation.

## A controlled structural reading

Three deliberately selected, previously interpreted lists have the following structure:

| Tablet | Heading contains | Unit entries | Closing expression | Arithmetic |
|---|---|---:|---|---|
| HT88 | KI-RO | 6 | KU-RO 6 | 6 = 6 |
| HT94b | KI-RO | 5 | KU-RO 5 | 5 = 5 |
| HT117a | KI-RO | 10 | KU-RO 10 | 10 = 10 |

These span two attributed scribes, both at Haghia Triada. GORILA-derived facsimiles were inspected for the layout and numerical structure; comparison is with published drawings, not autopsy of the tablets. John Younger's commentary already identifies these lists. This is replication, not discovery.

A defensible partial rendering of HT88's lower section is therefore:

> KI-RO [meaning unresolved here]: six named or labelled entries, each 1; KU-RO [total]: 6.

The experiment supports a heading or scope-setting use of KI-RO. It does not decide whether the list records deficits, absences, obligations or another category. Across the snapshot's tablet records, 16 identifiable KI-RO occurrences have varied contexts: seven immediately precede quantity signs, two precede damaged quantity strings, six precede another sign group, and one ends a damaged record. Some KI-RO readings themselves carry damage. Context categories are not lexical meanings.

## A constraint that fails

HT123+124a offers a more demanding check on the proposed relation between quantities labelled OLIV, *308 and KI-RO. For its first two rows, suppose KI-RO is additive to *308, both rows use one conversion ratio r, and the repeated fraction sign X has one value:

```
31 r       = 8 + E + 1 + X
(31 + J) r = 8 + J + E + X
```

Subtracting cancels E and X: `J r = J - 1`. With the conventional `J = 1/2`, the ratio is `r = -1`. Thus **no positive common ratio can satisfy this whole bundle of assumptions and readings**. Selecting a different X value cannot repair it. This does not individually disprove the deficit interpretation: the numerical reading, uniform-ratio assumption or additivity could fail. Younger already discusses the underlying discrepancy; the algebra here is a reproducible formulation of that existing problem.

HT13 is another caution: its displayed entries total 131 but KU-RO is followed by 130½, with damage around the first quantity. Younger's commentary explicitly notes the mismatch. It must not be “corrected” just to make a preferred interpretation work.

## Next research step

Create an independently collated set of accounting sections with sign-level uncertainty, commodity scope, physical line breaks and explicit boundaries. Preserve each alternative reading. Then compare candidate functions using whole tablets reserved for validation, and separate same-scribe, cross-scribe and cross-site evidence. Only after those controls should an association be promoted to a proposed lexical meaning. Ritual formulae provide another route, but need their own genre-specific corpus and uncertainty treatment.

## Run locally

From the repository root:

```
python lineara/fetch_corpus.py
python lineara/fetch_collation.py
python lineara/analyze_accounting.py
python docs/_check_profile.py --measure lineara/data/corpus_symbols.txt
python docs/_check_profile.py lineara
```

Raw texts, commentary and images stay in the ignored `data/` cache. `collation_manifest.json` lists the exact retrieved comparison sources and hashes. `accounting_results.json` records every qualifying candidate case and KI-RO context. The objective remains open.

## References used

- [Salgarella, Linear A (2022)](https://www.repository.cam.ac.uk/items/f50c0df4-f355-4bc0-be2a-8e960b2bb5da).
- [Steele, Exploring Writing Systems and Practices in the Bronze Age Aegean (2023)](https://crewsproject.wordpress.com/wp-content/uploads/2023/10/steele-2023.pdf), especially the accounting discussion and HT13 illustration.
- John Younger, commentaries on HT1, HT13, HT30, HT37, HT88, HT94, HT95, HT117, HT119 and HT123+124, preserved in the pinned source repository; exact links in `collation_manifest.json`.
- [SigLA, Salgarella and Castellan](https://sigla.phis.me/), identified as an independent comparison source; its full dataset has not been imported in this pass.
- [Tsirkas, corpus-validation-for-undeciphered-scripts-linear-a (2026)](https://github.com/ChristosTsirkas/corpus-validation-for-undeciphered-scripts-linear-a), encountered before testing; its numerical claims were not adopted as verified findings. Prior work already includes arithmetic and morphology experiments.
