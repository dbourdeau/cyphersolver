Audit method and reproducibility

Run, in this order (Python 3, standard library only):

```sh
python3 audit.py
python3 image_sample.py
python3 transcription_audit.py
python3 reconcile.py
```

Run the scripts from this directory or supply their absolute paths. Inputs are resolved relative to the scripts, not the shell working directory. All outputs go beside the scripts. Nothing outside review/ is written. No package installation, OCR, or source-file alteration is required. `explore.py` is the earlier read-only parsing diagnostic.

Outputs and scope

- `review.md`: verdict, under 400 words.
- `gaps.md`: all ten literal blank Founders gaps, graded individually, with supporting passages and qualifications.
- `metrics.json`: counts, sensitivity calculations, and SHA-256 digests of the principal input files.
- `token_audit.tsv`: every aligned token, its normalized value, exact-value recurrence, external support, leave-one-occurrence-out support, and sensitivity flags.
- `value_recurrence.tsv`: every unqualified numeric group/value pair, count and supporting locations. Unknown/conjectural and nonnumeric placeholder values remain visible in the full token ledger.
- `march_segments.tsv`: human-selected segmentations of independent March plaintext. Each row's exact code sequence is asserted to occur in `erving_groups.txt`. `external_evidence.tsv` expands it with source lines and original context.
- `wagner_audit.tsv`: the entire 47-type comparison, including the 584/943 indeterminacies and values in both key and alignment.
- `image_sample.tsv` and `image_metrics.json`: all 53 human visual readings, source runs, comparisons, and crop hashes.
- `transcription_positions.tsv` and `transcription_differences.json`: the 1,147 retained source positions and changes/omissions in the 1,145-token alignment.
- `reconciliation.json`: gap counts, denominator-adjusted scores, and key inventory checks.

What the percentages mean

The denominator for reproducing the claim and comparing support is the 1,145 entries in `aligned.txt`. This is not silently treated as a verified count of every manuscript token. `transcription.txt` repeats the seven-code acceptance passage under both 0362.3b and 0363L.1; the latter is retained once. Annotation removal preserves numeric parentheses, removes struck groups, uses the first stated alternative, and retains uncertain numeral positions. Two placeholders, at 0367L.2 after `1114.244` and at 0367R.1 before `all`, have no counterpart in `aligned.txt`. Whether both represent real missing manuscript code groups remains uncertain; counting both is the conservative denominator sensitivity, not proof of their contents.

Additional transcription-to-alignment changes are material: the `120.{1}285` reading becomes `120X#.285` (speci-men); the uncertain `{16?}51` becomes `X51#=re`; `{..}50` is restored as `250#=time`. These are editorial decisions, not unaltered transcription. `key_pinckney.tsv` also gives 584=na whereas `aligned.txt` gives 584=nation. A literal key lookup does not reproduce the published reading unmodified.

External support

A case-insensitive exact syllable/value match is required, allowing an explicit caret/triangle plural to lose its final s and apostrophe normalization. Alternatives recorded in Wagner are retained as alternatives. Question-mark Wagner readings are not confirmations. Values with X or a question mark in August are not counted as externally supported or leave-one-out supported. A fully numeric identity whose prefix is reconstructed may enter the support calculation, but all `#` cases are removed in the stricter image-position sensitivity.

The March file supplies code runs against word-level plaintext, not an authenticated code-to-syllable key. The review therefore publishes its manual segmentations explicitly. These are evidence of compatibility across documents, and can be disputed at syllable boundaries; they are not 716 independent correctness trials. Some nearby March alignments are approximate (as NOTES.md warns), so ambiguous runs were not forced to match the August key. The final conservative compatible count is 716 tokens / 141 types. Unsegmented or conflicting overlaps are not automatically successes. The generous ceiling of 790 counts any numeral occurring anywhere in the supplied March or Wagner data, even uncertain Wagner labels; it is only an identity-overlap ceiling. At least 355 August token occurrences lack even that overlap. Other Pinckney letters are mentioned in NOTES.md, but a bibliographic pointer without aligned values supplies no additional attestation. Neither this review nor the original files establish a unique exact external-support percentage beyond the documented matches and overlap ceiling.

Leave-one-out

The requested support check removes one occurrence, not an entire type. It asks whether the same normalized group/value pair remains elsewhere or is externally matched. There are 855 same-value recurrent tokens and 716 externally supported tokens; their union is 908. The separate value table and full token ledger make each decision reviewable. This is an audit of support, not a rerun of a solver trained without Founders. Repeated occurrences were aligned with the same edition and can repeat the same mistake. Holding out every occurrence of a value would require the external evidence, not recurrence. The original looser formula gives 922: normalized group count at least two OR presence among Wagner's shared labels. It includes X-like identities and changing values; it does not demonstrate independent validation.

A code number can be reused with incompatible fitted values, e.g. 310 ceiv/liev, 66 ing/in/West, 665 change/were, 943 er/ly. These could reflect manuscript coding mistakes, transcription uncertainty, or wrong alignment; the present data cannot uniquely decide. They cannot be treated as confirmation that one fixed value reads every occurrence. Repeated spelling variants, plural markers and harmless case differences are a separate matter.

Wagner and chance

The 47 shared type labels are reproducible directly from the supplied files; the associated August occurrences total 358. Forty-five types have at least one compatible, unqualified Wagner value. That permissive type-level success does not validate every occurrence: only 346 August tokens match definite Wagner values under the documented normalization. 584 has a guessed `nations?` reading and inconsistent August representations; 943's Wagner entry is literally `?(friend-943-ship)`, not a plaintext value. Neither counts as an established match or an established independent disproof.

The toy expected match count is computed exactly: for each of the 45 types with definite Wagner values, compare its August alternative set to every definite Wagner value set, then divide total compatible pairings by 45. This is 46/45 = 1.0222 expected matches if those value sets are uniformly permuted. The model ignores language, context, fitting, inspection and selection; it is NOT a defensible null for this reconstruction. No conditional chance probability or meaningful independent-test p-value can be derived without a training/holdout history and a specified contextual inference process. Agreement could be genuine evidence of the shared cipher while still offering no blinded validation of the new gap fills. Most proposed gap syllables are outside Wagner's tested inventory.

Images

The reviewer visually inspected the seven sample crops used by `image_sample.py`, plus additional gap/ambiguity crops. The 53 sampled positions are distinct manuscript positions and agree digit-for-digit with their source transcription runs, including all three 549 spellings in Hanover. The image observations are hard-coded separately from source tokens; the script verifies the comparison, not the human reading itself. This purposive sample emphasizes legible runs and is neither blind nor random, so 0/53 must not be generalized to a zero full-transcription error rate or used for a random-sample confidence bound. Crops also show the actual 310 in “deceive” and 1154 in “resist”/“resort”; no contextual relabeling is mistaken for a digit correction.

Read bar and classification

The supplied project threshold is about cipher tokens that read as sense, not merely how many have non-X strings. The edition-assisted reading is mostly intelligible and its stated flags give 1,125/1,145 = 98.2533%; including both omitted positions gives 1,125/1,147 = 98.0820%. But that flag count is not an independently scored sense/accuracy test. Remove the 37 partially hidden groups as well (accounting for overlaps with unread/conjectural flags) and 1,090 remain; additionally exclude the nine unflagged occurrences in the five explicit collision classes listed by `audit.py` and 1,081 remain. Against 1,147 positions this is 94.2459%. This is a declared conservative sensitivity analysis, NOT a measured error rate, and does not prove that the excluded readings are all wrong. Conversely, passing the nominal 95% threshold does not establish that the partial key is 95% accurate on unseen text. An editorial “read” label is defensible if restorations/emendations are accepted and disclosed; an independent ≥95% cryptanalytic accuracy claim is not established.

The category is **key recovered based on plaintext from external sources**, qualified as partial, plus collation of a previously published decipherment. The main narrative is already in Founders; the genuinely added information is limited to the corroborated repairs. “Read from existing decipherment” describes the narrative reuse, but misses the additional cipher-to-plaintext alignment and limited gap recovery. It is not ciphertext-only cryptanalysis. The category definitions and project-specific nature of the bar were checked against the project's primary documentation: [glossary](https://dbourdeau.github.io/cyphersolver/glossary.html) and [README](https://github.com/dbourdeau/cyphersolver). No claim is made here to have seen Lasry's private email.
