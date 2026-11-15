# Test plan: Arthur Lee to Richard Henry Lee, 1779-80, dictionary code

Written 14 November 2026 by Claude (AI agent) before any of the 166 groups was decoded, except that
three of Tomokiyo's own example groups (243a17, 426b28/29, 330b13) were looked at while fixing the rule.
The SHA-256 of this file is recorded in `FREEZE.txt` the moment it is written.

## 1. Edition (frozen)

- **Key book:** John Entick, *The New Spelling Dictionary*, London: Edward and Charles Dilly, **1776**,
  Internet Archive `bim_eighteenth-century_the-new-spelling-diction_entick-john_1776` (an Eighteenth Century
  Collections Online scan). Printed page = scan leaf number + 2 (`/page/n<page-1>.jpg`).
- **Why this edition:** the edition the Lees and Jay used was the 1777 London edition (Tomokiyo, from Jay;
  Burnett 1917 "probably 1777"). No digitized 1777 copy was found (see `NOTES_arthur_lee_1779.md`). Of the
  editions available (1766, 1772, 1773, 1776, 1781 on the Internet Archive), the 1776 is the only one that
  puts the large majority of Tomokiyo's identified groups on the right word:
  - Tomokiyo groups read directly from translated letters (Jay's code without offsets, Lee's 1778 letter,
    Lee's 1779 "minister"): 12 groups; in 1776, **9 exact**, 1 off by one line (court), 1 right line but the
    other column (force), 1 miss (told).
  - Groups Tomokiyo derived from Jay's offset letters on pages 36-276: 18 of 20 exact, 2 off by one line
    (because, expectation). On pages 372-384 (the, their, that, them, this, those, terms, troops) all miss;
    there his reversed-line formula is itself uncertain (for "the", 1776 has The at 373a34, which is what his
    alternative formula 61 - 27 gives).
  - The 1781 and 1772 editions have different pagination (minister on p. 249 and p. 255 respectively); the
    1773 edition has the same page breaks where checked but differs by a line in several places (for example
    Channel, Congress).
  - Full table: `edition_anchor_check.tsv`.
- The 1776 edition is therefore a **stand-in** for the 1777. Readings one line away from the frozen line are
  expected now and then and are graded down, not hidden.

## 2. Counting rule (frozen)

- Group `P a N` (Lee writes `P, a, roman N`): printed page P, column a (left) or b (right), N-th **entry** from
  the top of the column.
- Count entries (lines that begin with a headword at the column margin). Do **not** count: the running head
  and page number; section headings such as "I." or "Y."; continuation lines (the indented second line of a
  long entry).
- Fixed on Tomokiyo's groups: Majesty 233b29 and Loan 229a37 are right only if continuation lines are
  skipped; I 196a28 is right only if the section heading is skipped. (Court 108a10 would need the
  continuation line counted: the one direct conflict, recorded.)
- Pages 454-455, "Most usual Christian Names of Men", have five columns; the same rule is applied with the
  columns lettered a to e from the left and the letter headings skipped. This extension is not fixed by
  Tomokiyo's groups; it is checked inside the decoding (does it give names of the right persons?).
- A dictionary gives the base word only. Plural, tense and other endings are the reader's; Lee's written
  endings (`-s`, `-d`, `-ed`) are added and marked.

## 3. The test (one run)

**Real arm.** Every group whose page, column and line are legible (doubtful readings included, using the
first reading), looked up in the frozen edition by the frozen rule, read by eye on the page image.

**Control arms** (on a fixed random sample of 30 non-doubtful groups, drawn with seed 17791779 before any
reading, listed in `work/control_sample.tsv`; pages 454-455 excluded from the sample):
1. same column and line, page + 1;
2. page - 1;
3. page + 7;
4. page - 7;
5. same page, column and line in a wrong edition: the 1772 Dilly edition (Internet Archive
   `bim_eighteenth-century_the-new-spelling-diction_entick-john_1772`).

The real arm is also scored on the same 30 sampled groups, so the comparison is like with like.

**Judgement.** For each lookup: does the entry found give a word that, with at most an ordinary ending
added, fits the grammar and sense of the clear text on either side of the group in the letter? Scored Y or N.
The control lookups are read with the same strip images; to limit bias the 180 candidate words of the
sample (30 real + 150 control) are written into one shuffled sheet with their contexts and judged in one
pass with the arm labels hidden (`work/judge_sheet.tsv`; key in `work/judge_key.tsv`). Honest limitation:
the judge is the same agent that extracted the words, so the blinding is partial.

**Pass mark (written before the run).** The code is read with this edition and rule if, on the 30-group
sample,
- the real arm fits in at least 60 per cent of groups (18 of 30), **and**
- every control arm fits in at most one third of the real arm's count, **and**
- across all legible groups (real arm, full set), at least 60 per cent fit.

If it fails, nothing is presented as a reading; the result is reported as a failed test.

## 4. Grading of the full decoding

- **Firm:** the frozen line gives a word that fits, or a name on pages 454-455 that fits the persons in the
  clear text.
- **Guess:** the frozen line does not fit and an entry one line up or down (or the other reading of a
  doubtful digit given in the transcription) fits; or the frozen line fits only loosely. The alternative used
  is recorded as a transcription or edition doubt.
- **Unread:** nothing within one line fits, or the group is illegible.
