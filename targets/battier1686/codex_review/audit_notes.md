# Audit scope and reproducibility

Run `python3 -B audit.py`, then `python3 -B interpretation_audit.py` from this directory. No supplied program is imported or executed. Only the literal assignments in letters.py are extracted with Python AST. Dictionary rows are parsed independently. All outputs stay in this directory.

This verifies the proposed key against already transcribed tokens. It cannot independently establish the shapes of cipher marks, the accuracy of dictionary image transcription, handwriting, authorship, dates, or archival identification. The closing dates are taken from the supplied inventory. No network or image re-reading was performed. Supplied prose and validation reports were inspected as evidence of the original analysis, not as independently authenticated decipherments.

The decoder takes the first explicitly transcribed alternative, strips trailing uncertainty signs, treats bare numbers above 98 as series 1, preserves internal question marks, and never fills a gap from context. It gives explicit zz_corrections.tsv entries priority; otherwise it takes the first entry in lexicographic file order and preserves every competing value in tokens.tsv. Thus the computation does not use reading values to decide its own output.

## Agreement and provenance

All 991 focus token positions and line labels align with reading/*.tsv. Exact agreement is 986/991, case-insensitive agreement 988/991. Four matching placeholders are included in those field-comparison totals and MUST NOT count as decoded sense. Of the 987 tokens with an available literal mapping, 984 match case-insensitively.

The five exact disagreements:
- s092L:17, 12:969?: independent getwist; supplied [Turck(en)?]. The latter is contextual, not in this code's dictionary entries.
- s099R:1, 10:126: paltzgraaf versus Paltzgraaf.
- s100R:123, 11:215: sakee(?) versus sake; both dictionary variants exist.
- s108R:25, 12:401?: gesworen versus geswooren; both variants exist.
- s108R:110, 10:487: president versus President.

Literal provenance requires the SAME code/letter and supplied value, not just that the word occurs somewhere in the dictionary. Any explicitly supplied token alternative can support it. Dictionary entries need an explicit scan/side/column reference. Letter tokens use letters.py's table-level scan references; it has no individual column references. No genuine letter provenance is being invented.

Unattested supplied values:
- 19 December: none.
- 4 December: s092L:17, [Turck(en)?].
- 12 February: s099R:68 [3:374], s099R:70 [1:512], s100R:52 [11:710].
- April: s108L:14 [12:6?0].

The notes mention bylegger, afkomste and soeckinge for the three February gaps, but these code/value pairs are absent from dict/*.tsv. A note asserting a key reading is not a dictionary entry.

All H-labelled focus TSV values have matching key-file provenance. That does NOT validate normalized prose: 81 remains literal i even where prose silently becomes e. Original global grade totals reproduce 2,325 tokens: H 2,153, C 129, M 9, I 34; H 92.6%, H+C 98.2%, H+C+M 98.5%. These percentages describe labels, not an independently tested semantic success rate.

## Separate literal and semantic metrics

The requested strict provenance percentage is literal_attested/n in metrics.tsv: 100%, 99.5%, 98.9%, 99.7%. These are NOT sufficient evidence of sense: getwist and navale maght can be perfect key lookups in broken sentences.

To test the stronger claim, the separate strict sense SCREEN starts from attested H+C, excludes I/M, then excludes specific unkeyed corrections or insecure contextual meanings. It accepts genuine transcribed alternatives: s107R:46 can become r via explicit alternative 49, so this does not incur another exclusion. The screen is a disclosed editorial sensitivity analysis, not an objective gold standard; unexamined sentence-level issues can remain. Missing letters and supplied word boundaries are not additional cipher tokens.

- 19 December: 186, with no further exclusions. The single C reading syn is dictionary-attested; alternative mark recognition remains unverified.
- 4 December: baseline 203 H+C, minus four insecure C meanings: Hofmeester (s091R:12), gesoubconneert and gouverneren in the broken construction (s092L:81–82), and Sex. (s092L:87). Result 199/211. Moving these judgments back changes the result to 203/211; the threshold is therefore interpretation-sensitive. The references to a Queen Mother and secrecy are not established by “oude Sex.” and “voor seker aardigh hout.”
- 12 February: baseline 259, minus seven i→e changes, overgedragen→overdragen, and the letter correction in grandmaeitre. Result 250/271. Remaining problems include the incomplete ischyt and the broken gesoubconneert/rotgesel passage; this count should not be promoted to fully established historical meaning.
- April: baseline 321, minus three i→e changes and five further letter substitutions (moniere, montiuey, presisence, gtand, maeistue). Result 313/323. The uncertain Osuna deletion is already excluded as M. Normal ae spelling and the separate word is after Grana need no emendation.

Generous H+C+M ceilings are 186, 204, 262, 322. They accept the author's contextual supplies, possible deletions and uncertain readings. H+C alone is 186, 203, 259, 321. In particular April's claimed 99.4% is accurately reproduced as 321/323, but it is the label arithmetic rather than a purely key-derived corrected-text rate.

December's s092L L06–L08 and February's s099R L07–L08 / s100R L04, L07, L09–L10 concentrate unresolved meaning. A high pooled token rate, weighted by many easy individual letters, does not prove “only scattered open codes.”

## Dictionary consistency

There are 1,617 rows and 1,393 distinct codes. Twenty-four codes have differently written values: seven case-only, seventeen otherwise (including spelling and spacing variants, not seventeen contradictory meanings). Six have explicit correction-file resolutions. Focus-used non-case variants are 15:325 was/wat (two occurrences), 4:565 eens/dus, 12:401 gesworen/geswooren, and 11:215 sakee(?)/sake. The first two are substantive and have explicit corrections. Both are also useful alphabetical checks: dus is out of place around eens; was precedes rather than follows wasdom. The correction to wat fits.

alphabetical_inversions.tsv lists adjacent observed NUMBER keys after correction precedence and lexical normalization (case/accent/punctuation removal). It includes 404 inversions: 365 in series 1–15 and 39 in names series 16. Ninety-six touch focus tokens. alphabetical_all_variants.tsv also tests obsolete and competing values and lists 423 inverted pairs. This is an exhaustive local-adjacency screen over the available entries, not over all missing codebook rows.

Do not automatically repair these inversions. E.g. vinden → gevonden, sweren → gesworen, and willen → gewilt are grouped inflections; the Spain entries around 11:782–854 and other ruler/country groups are thematic, not lexical. Historical i/y and u/v spelling, titles and articles also change order. Candidates such as 6:96 hofken/hoffen (unused here) require image re-reading. Alphabetical order alone cannot identify the right reading.

The asserted range 99–999 is also an oversimplification: the supplied index switches from series 1:997 to series 2:1 in the same column, and many attested focus codes are below 99 within later series (4:90, 6:5, etc.). Numbers 2–98 are letters only when unmarked.

Only two dictionary rows lack a full scan/column reference: core.tsv's conjectural 2:279 bemoeyen? and zz_corrections.tsv's 13:119 van hem. Both have fully referenced alternatives elsewhere. Neither causes a focus provenance failure.

## 81 and validation

81_context.tsv enumerates all 17 cases: 14 contextual e, three genuine i. Focus letters contain 13: February eight (seven e, one i), April five (three e, two i); neither December letter contains 81. The other four are s097R:54 and s101R:36,62,112, all contextual e. Thus a CONDITIONAL i/e practice is plausible, but blanket 81=e would damage sich and presidence.

There are ZERO 81 tokens in the two fully validated letters, across s030R, s031L, s041R, s042L, s044R. They cannot validate that practice. The partial s101R interlinear report contains hem and opponeren, which is compatible with two such corrections, but no independently inspected image or complete aligned transcript was supplied here to certify the habit.

Three s099R 81 tokens (34,85,97) remain H, with e-correction notes attached to 36,86,93 instead. Other shifted notes include s099R:5 referring to Monsieur at token 3, and s099R:54 referring to overgedragen at token 53. s100R:85 describes a written 6 although the token is 7. Confidence counts should be regenerated after linking annotations to actual token IDs.

The validation documents acknowledge consultation of the contemporary decipherment while correcting token readings. Their “key-alone” column is therefore not a blinded holdout experiment. Likewise control.py tests segmentation of curated spelled runs with a custom name/loanword lexicon; it does not test mark choices, word-code readings, proper-name identification, or the prose claims. The shuffle experiment was not rerun in this audit.

## April Dutch and historical claims

See april_reading.md for an independent lightly normalized reading and statement grades. The register and mixed Dutch/French administrative vocabulary are internally plausible; this is a linguistic assessment, not independent dating or attribution. Much of the numerical/project context appears in supplied CLEAR-text comments rather than being recovered from cipher.

All generated token metrics are in summary.json and metrics.tsv. input_integrity.json verifies that the 47 files read by the decoder retained the same hashes at the end of computation.
