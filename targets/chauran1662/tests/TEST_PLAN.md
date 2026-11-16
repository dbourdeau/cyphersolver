# Test plan: the Spanish-vocabulary cipher of SP 84/165 (1662)

Written 15 November 2026, before either test was run and before I had opened the transcriptions of
the test items for anything but their line counts and the helpers' notes on where the gloss stands.

## What is tested

`work/key/table_v1.tsv`, sha256 `9619f6ef0896b5efd0b0b2a6b14dddd305df983b6b022249ac8b176c8e9cd029`.
Built only from ff. 189r and 260r-v (two blind transcriptions reconciled on the image; the period
gloss aligned to the groups by program and corrected by me line by line). 392 groups; the 355 with a
settled value (tiers firm, mixed, single) are "the table" in both tests. The 37 "unsettled" groups
count as not in the table.

Test items were each transcribed once by a helper who had no table (none existed) and was told not to
let the gloss decide a numeral. Struck-out groups are left out. D1 and D2 are read as D3; marks the
helper could not classify count as their own group (so they miss).

Values are compared after this normalisation, fixed here: lower case; v = u; y = i = j; ç = c; z = c
before e or i only; doubled letters single; h dropped; accents dropped.

## Test A: does the table predict the period gloss on letters it was not built from?

Items: the glossed lines of ff. 264r-265r and ff. 294r-295r (mostly glossed), and the glossed openings
of f. 187r (lines 1-5) and f. 243r (lines 1-4).

Gloss for a cipher line: `Lnn G` of the same line in the files for ff. 294 and 243; `L(nn-1) G` in the
files for ff. 264 and 187 (those helpers recorded each gloss under the line it physically follows and
say so in their notes). A line is "glossed" if its gloss has at least 10 letters.

Procedure for each glossed line: the gloss window is the line's own gloss with up to 15 letters of
the neighbouring glosses on either side (gloss and cipher lines do not break at the same place). The
groups of the line are laid along the window in order by dynamic programming. A group that is in the
table scores a hit if its table value (normalised) stands at its place in the window; otherwise it is
a miss and may cover 0 to 12 letters. A group not in the table covers 0 to 12 letters and is not
scored. Letters at either end of the window may be left over. The program takes the layout with the
most hits. This is generous (it looks for the best layout), so the same procedure is run with 200
shuffled tables: the same groups, their values permuted at random (seeds 1 to 200).

Reported: coverage (table groups / all groups on glossed lines), hit rate (hits / table groups on
glossed lines), per item and overall; the shuffled tables' mean and maximum hit rate; hit rate by
tier (firm, mixed, single).

**Pass mark, set now:** overall hit rate at least 70%, and above the highest of the 200 shuffled
tables. Each of ff. 264 and 294 separately at least 60%. The two openings are too short for a mark
of their own and are reported only. Coverage is reported, not judged; I expect 55 to 75%.
A hit rate between the shuffled maximum and 70% is a miss, reported as a miss.

## Test B: is each bare item in the same key?

Items: the bare lines of f. 187 (lines 6-53), f. 243 (r lines 5-23, v, 244r; and 244v-245v from the
second helper), f. 231r-v, f. 306r-v, f. 313r-314r, f. 315r-316r, f. 317r-318v. Also reported, not
judged: the bare lines of ff. 264 and 294.

Two measures for each item:

1. **Coverage:** share of the item's groups (tokens) that are in the table. If the item used
   another key, the groups it uses most would not be the ones this table happens to hold: the table
   holds 355 of about 2,000 possible groups (nine marks by 1 to about 220), so chance coverage is
   about 18%, somewhat more if numerals were unevenly used.
2. **Spanish score:** decode every table group; a group not in the table breaks the stream. Score =
   mean log-probability per letter of the decoded runs under a letter-trigram model (add-0.1
   smoothing, 27 symbols with word space dropped) trained on `work/tests/spanish_reference_corpus.txt`
   (seventeenth-century Spanish diplomatic readings from Daniel Bourdeau's repository, none from this
   volume). The same score is computed for 200 shuffled tables (values permuted among the same
   groups, seeds 1 to 200).

**Pass mark, set now, for each item:** coverage at least 45%, and the Spanish score higher than all
200 shuffled tables. An item that meets one condition and not the other is reported as "not shown".
An item that fails is not read; its probable system is described instead.

Control reported beside it: the same two measures on ff. 189 and 260 themselves (expected coverage
about 97%, a ceiling, not a test) and on the first four lines of f. 228 (the agent's French cipher,
expected to fail).

## One run each

Scripts `work/scripts/test_a.py` and `work/scripts/test_b.py` are written after this file and run
once. Outputs: `work/tests/test_a_result.txt`, `work/tests/test_b_result.txt`. If a script has a
plain bug (crash, wrong file), I fix the bug and say so; I do not change the measures or the marks.
