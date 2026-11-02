# Blind check of f. 29 lines 8-10 (30 Oct 2026)

One image agent transcribed lines 8-10 from the 2x crops and the key files only (`BRIEF.md`; no exemplar, no earlier
transcription, no `*` crib values). Its output: `blind_lines_08-10.txt`, `blind_labels.txt`. Compared with the
crib-assisted values of `../f29_lines_08-13.txt` for the same lines, and both scored against the exemplar segment
*consilio et auxilio ... Millesimo qui* (149 letters; same global alignment as `align_f29.py`).

| | tokens | matched | mismatched | unknown / crib | match of scored |
|---|---|---|---|---|---|
| crib-assisted (earlier) | 143 | 128 | 1 | 10 | 99.2% |
| blind | 144 | 70 | 44 | 16 | 61.4% |

Token by token the two transcriptions agree on 61 of 142 values (43%); the blind one has 18 `?` and 1 `^` and
differs on 106. The agent reported that circle-on-stem signs (u, e/ae, t) could not be told apart in the crops and
that it could not place word breaks.

What it shows. Chance agreement of a letter with the exemplar is about 8%, so 61% blind, from a key brief the agent
had never applied to this page, confirms that the R367 sign family reads this text without help from the crib. It also
shows the earlier 97.7% overstated the independent fit: on the ambiguous signs the earlier values had been moved
towards the exemplar. Use the blind figure (about 60% on three lines, one noisy transcriber) as the independent
estimate, and treat the crib-assisted values as a reading of the exemplar's text, not a measurement of the key.
Not done: a second blind transcriber, or a blind run on the sign shapes with the label table of
`../f29_label_values.tsv` (the stable labels would likely score higher).
