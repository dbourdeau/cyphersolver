# Confirmation test: Harford Jones's code book = Entick's *New Spelling Dictionary* (1795/1796 setting)

Written 15 Nov 2026 by an AI agent (the confirm worker, Opus), before any re-reading of the manuscript and before
any look-up. All work by AI agents; no person has checked it. Local only. The sha256 of this file is recorded in
`TEST_PLAN.sha256` before the first crop is shown to any reader. One run; a miss stays a miss.

## What I knew when writing this

Read: their NOTES, `table_1798.tsv`, `align_1798.tsv`, `ct_49.txt`, `pt_51.txt`, `align.py` (worktree
`output/push_2026-11-15/wt-main-readonly/targets/jones1802/`, read only); our codebook, verify and digits notes,
`FROZEN_RULE.md`, the verifier's `TEST_PLAN.md`, `lookup_curated.tsv`, `common.py`, `position_test.py`. I have NOT
looked at any manuscript image of /49 or /212 at a scale where digits can be read. I noticed from their alignment
alone (no dictionary) that their DP shifts one place in "make a separate Peace? - This Question": `230,1` is skipped,
`2,2` = make, `338,31` = a, `272,62` = separate, `383,20` = peace. This plan does NOT correct it (their table is used
as it is); the effect is reported after the run.

## Claim

A group `p,n` of /49 is printed page p of Entick (setting of IA `..._1795_0`, = `..._1796`), printed line n under the
frozen rule R2 (`output/jones1802_verify_2026-11-15/FROZEN_RULE.md`, sha256 10cebc54...): column a lines 1..k_a top
to bottom with continuation lines counted, column b continuing at k_a + 1 (as implemented in the verifier's
`position_test.py`, r2 = na + i; k_a is 39 on almost every page). A third number picks a word within the line.

## Step 1: blind digits of /49 (all number groups)

- Images: `sources/raw/jones1802_digits_2026-11-15/IOR_L_PS_9_76_49.pdf`, page JPEGs as extracted by the digit
  worker (`output/jones1802_digits_2026-11-15/work/pages/p49_img2.jpg` = f. 1r, `p49_img3.jpg` = f. 1v, mapping
  checked by its cropping helper). Copied unchanged into this folder's `work/pages/` with checksums.
- Crops: `scripts/line_crops.py` cuts each page into one crop per written line by the horizontal ink profile
  (bands between ink minima, padded). I check the cut only on a down-scaled overview no wider than 300 px, at
  which digits cannot be read, and never open a crop at full size before the readings are saved. Crops get neutral
  names (k01, k02, ...) in a shuffled order (seed 20261115); the key (crop -> folio, line order) is kept by me.
- Readers R1, R2: two Opus helpers, separately, each given only a scratch folder holding copies of the crops and the
  instruction: "transcribe every number group digit by digit, with commas as written; where a digit could be two
  things give both, first choice first", plus a neutral output format (one line per crop; groups in order, separated
  by spaces; a doubtful digit as (4/2), first choice first; a group cut by the crop edge marked with ~; groups of the
  neighbouring lines that show partly at the crop edge are ignored). They are told nothing else: no earlier
  transcription, no dictionary, no claim, no word values.
- Saved and hashed (`work/readings.sha256`) before reconciliation.
- Reconciliation (mechanical, `scripts/reconcile.py`): for each crop the two readers' group sequences are aligned
  by edit distance on whole groups (first choices only). Equal groups = accepted. Any unequal or unpaired group =
  disputed. A third Opus reader R3, same instruction and format, reads every crop that holds a disputed group (whole
  crops, so R3 does not know which group is in dispute). R3's group at that place (by the same alignment) decides
  if it equals R1's or R2's first choice; otherwise the group is DOUBTFUL and leaves the test.
- The reconciled stream is aligned to the maintainers' token positions (`work/positions_49.tsv`, built from
  `ct_49.txt` + `align_1798.tsv` by `scripts/positions.py`) by a DP over groups (substitution cost = digit edit
  distance, gap cost fixed), in the crops' reading order. A maintainers' position with no blind group = DOUBTFUL.
- Reported: for every aligned position where blind != maintainers', the digit pairs (maintainers' digit -> blind
  digit) for fields of equal length, and "structural" changes (digits added or lost, comma placement) separately.

## Step 2: the test set

Every position of /49 that their alignment gives a `word` move (221 positions; letter moves of spelled names and
clear words are not test items), with the word their table gives it (their OVERRIDES applied: 169,25 government,
327,66 said). Then:
1. Leave out the positions whose MAINTAINERS' group is one of the verifier's 15 training groups (1,1; 22,33; 50,65;
   129,70; 156,56; 179,7; 217,30; 232,12; 236,35; 260,26; 275,12; 308,62; 330,16; 370,15; 382,28).
2. Leave out DOUBTFUL positions.
3. Leave out bare `p,2` groups (two numbers, the second 2) as BLINDLY read (Brice Dudout: not fixed values; the
   verifier excluded them too). A maintainers' `p,2` that the blind reading makes `p,4` etc. stays in.
4. One item per distinct blind group (page, line, third number if any). A blind group paired with two words takes
   the word with the higher count; a tie is excluded.
Provisional size from the maintainers' digits: 134 distinct groups after 1 and 3, 2 ties, so about 132 items; the
real count m is stated after Step 1. Numerals are tested in words ("15th" as "fifteenth").

## Step 3: look-up

- Book: IA `bim_eighteenth-century_enticks-new-spelling-di_entick-john_1795_0`, page images at scale 2 (as the
  verifier). This copy, not 1796, is the primary one because the verifier's blind counts (48 pages, 95 columns,
  0 disagreements) are on it and it found 1795_0 and 1796 in the same setting. Line counts: the verifier's
  `img_all_1795_0.tsv` where the page was counted; every other needed page is fetched (IA, one request at a time,
  >= 2.5 s apart, honest User-Agent, stop at the first 403 or 429, at most 300 requests) and counted by two blind
  Opus helpers (column halves cut by the verifier's `crop_columns2.py`; task: list every printed line of each
  column top to bottom with E = new entry / C = continuation and the first word; running head, page number,
  catchword and large letter headings not counted; no word or number is mentioned to them). A page where the two
  helpers differ in line count or E/C type in a column is resolved by me against the image, and recorded.
- 1796 check: for each test page the 1795_0 and 1796 machine lines (verifier's `mc_1795_0.tsv`, `mc_1796.tsv`) are
  compared (first and last headword of each column, one-letter tolerance). Where they differ, the item is ALSO
  scored on a counted 1796 page image, reported separately; the pass count uses 1795_0 only.
- Match rule (fixed): the verifier's `common.match` (word or its root by -s, -es, -ed, -d, -ing, -ly, -ness, -ation,
  -ies/-ied/-ily -> y, doubled consonant, had->have, went->go, made->make; one-letter tolerance for 6+ letters),
  applied to the line's first word; plus possessive 's dropped; plus, when the code group carries a written
  suffix (ing, ed, es, est, o), the word with that suffix removed (and with e added) is also tried. For a group with
  a third number, the word also counts as exact if it (or its root) occurs anywhere in the text of line n, which I
  read off the dictionary image after the helpers' count fixes the line.
- Score per item: EXACT (matches line n), WITHIN ONE (matches line n-1 or n+1, not n), ELSEWHERE ON PAGE (matches
  another line's first word on page p), NOT ON PAGE; NO PAGE if the page cannot be had (counted as a miss).

## Step 4: marks (set now)

- PASS = exact >= 60% of m AND the shuffled control mean < 10%.
- Shuffled control: the words are re-paired with the items' groups by uniform random permutation, 1000 shuffles
  (seed 20261115), each scored EXACT with the same matcher; report mean, 95th percentile, max.
- REJECTION reading: exact < 40% of m: the book or rule is still not shown. Between: not confirmed, not rejected.
- Secondary figures, reported but not used for the verdict: (S1) with the bare `p,2` groups included; (S2) without
  the 22 groups of the digit worker's disputed list D01-D22 (the groups that suggested 2-for-4); (S3) 1796 where it
  differs.

## Task B rules (only if PASS; stated now)

Third number k = the k-th word of printed line n counted from the line's first word, punctuation ignored, part-of-
speech abbreviations counted as words. Status per group: agrees (dictionary word = their word by the match rule) /
corrects theirs (dictionary word differs from their H value or from their table) / fills a gap (their value open, or
only a proposal M/L, and the dictionary line gives a word) / does not fit (no reading: page or line has nothing that
can be the word, or the group is bare `,2`). A word comes from the dictionary line or it is a hole. /212 digits are
re-read blind first by the same Step 1 procedure.

## Not done

No git, no posting, no email. Their files are not edited. Python is run with -I from `scripts/`, never from a
download folder. No scripted requests to qdl.qa.
