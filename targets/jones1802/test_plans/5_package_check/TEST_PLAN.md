# Test plan: independent check of the jones1802 Entick package

Written Sun 15 Nov 2026 16:15 EST (clock from `date`: "Sun Nov 15 16:15:26 EST 2026"), before opening any
image or any background note. Checker: Claude (Opus), working for Andrew Beling. Package under test: worktree
`output/push_2026-11-15/wt-jones1802-entick`, branch `jones1802-entick-beling`, commit 3ba4e36a3,
folder `targets/jones1802/`. Read-only on the worktree. All my files live in
`output/jones1802_pkgcheck_2026-11-15/` (this folder, "OUT").

## Check A: the dictionary line table (`entick_lines.tsv`)

Sample frame: the data rows of `entick_lines.tsv` (lines not starting with `#`, header row removed), in file order,
indexed from 0.

Sample (fixed now, drawn by `OUT/sample.py` after this plan is hashed):
- 12 random rows: `random.Random(20261115).sample(range(N), 12)` on the frame (N = number of data rows).
- 12 targeted rows, the rows behind these claimed corrections: Superintendent, Silver, Mine, Bishop, Body, Gain,
  Fortify, Frontier, Winter, Daniel (page 442 line 55), David (442,56), Joseph (443,48). For each word, take
  the first row of `entick_212.tsv`, else `entick_49.tsv`, whose `dictionary_line_n` column equals the word
  (case-insensitive); page,line = the first two numbers of its `group` field; then the `entick_lines.tsv` row
  with that page and line. If a targeted word is already among the random 12, it is still counted once in each
  half (24 rows total, possibly 23 distinct); if a word cannot be found, say so and draw a replacement with the
  same generator continuing.
- Before giving anything to a reader I note only page and line number (no word) in `OUT/A_tasks.tsv`.

Reading: a helper reader (Opus, medium effort) gets ONLY the local page image path(s) and this rule:
"printed lines of column a are 1-39, column b 40-78, every printed line counts including continuation lines
(lines that carry on the definition of the entry above); the running head / page header and catchword are not
lines", and the line number(s). It writes the first word on that line and whether it is a new entry or a
continuation, plus the first word of the line before and after. The reader is told not to open any other file.
Images: the local Internet Archive copies of the 1795 item (`sources/raw/jones1802_confirm_2026-11-15/img1795_0`
or `jones1802_verify_2026-11-15/img1795_0`); a page not held locally is fetched from the Internet Archive into
`OUT/ia/` (one request at a time, at least 2 s apart, at most 30 requests, honest User-Agent, stop at the first
403, 429 or challenge).

Mark: a row MATCHES when the reader's first word on that line equals the table's `word` after lower-casing and
removing punctuation, hyphens and spaces, with long s read as s (and the reader's type, entry or continuation,
not required to agree but reported). A MISS is anything else. Pass: at least 22 of 24 match. For every miss
I report the page, what the reader read on the lines either side, and whether a count off by one line
(the table's word on line n-1 or n+1) explains it. If the reader's word differs only by an obvious misread
spelling of the same word (one letter), I count it a match but list it.

## Check B: the re-read digits of /49 (`reread_49.tsv`)

Sample frame: data rows of `reread_49.tsv` whose `group_reread` differs from `group_ct` and whose `doubtful`
column is not "yes" (the changed groups), in file order, indexed from 0. Sample:
`random.Random(20261115).sample(range(M), 20)` (a fresh generator, separate from Check A).

Locating: the PDF `sources/raw/jones1802_digits_2026-11-15/IOR_L_PS_9_76_49.pdf` (page images extracted
locally with Python reading the file under `-I`; no request to qdl.qa). Locating a group needs the manuscript
line number from the transcription, so I crop WHOLE manuscript lines (the line holding each sampled group,
with a margin), knowing the transcriptions myself; the reader sees neither. The reader gets only the crop and:
"Write out every figure and mark in this strip of handwriting, left to right, as you read it, groups separated
as they appear; mark anything you cannot read with ?". Neutral, no hint about 2 versus 4.

Mark: for each sampled group, I find its position in the reader's line by its neighbours and score it
REREAD (reader's digits equal `group_reread`), THEIRS (equal `group_ct`), or NEITHER (or unlocatable). A miss
is anything other than REREAD. Pass: at least 16 of 20 REREAD. I report the full count of all three.

## Check C: arithmetic and script

- Copy `targets/jones1802/` to `OUT/run1/` and `OUT/run2/`; run `python3 -I entick.py` in each copy (cwd = the
  copy). Compare every output file with sha256 against the committed file and between runs.
  Pass: byte-identical to committed and to each other.
- Recount from the committed tables every figure stated in NOTES.md (dated section) and the draft body:
  98 of 326 and 4 doubtful; 126 figures 2 to 4; 9 of 580; grade H 57 agree / 18 differ, M 13 / 10, L 2 / 16;
  six gaps filled; /217: 18 of 28, 15 on uncounted pages, 66 of 85 letter groups; read shares 0.984, 0.923,
  0.769. Report stated versus recounted; any difference is a miss.

## Check D: statements

(a) The claim that the 1796 copy "puts the same words on the same lines" versus the later sentence that it was
not compared page by page: search our folders (output/, research/, sources/raw/ SHA256SUMS and meta) for
what was compared and by whom, and say what wording the evidence supports.
(b) "no earlier file of this folder is changed": `git diff --stat origin/main HEAD` and `--name-status` in the
worktree; for NOTES.md and profile.json, test whether any earlier line is removed or altered (diff of the two
blobs via `git diff origin/main HEAD -- <file>` read-only, which is a single two-revision diff, not
`git log -p`).
(c) Read the appended NOTES.md section and the draft body against the files; list overstatements, numbers
that differ between the two texts, unexplained abbreviations.
(d) profile.json: maintainers' entries intact, via `git show origin/main:targets/jones1802/profile.json`; if the
blob is missing, say so and skip.

## Order

Plan, hash, samples drawn by script, then the blind reading (A and B), then C, then D, and only then the
background notes. Nothing in the worktree is changed; no git write; nothing posted.
