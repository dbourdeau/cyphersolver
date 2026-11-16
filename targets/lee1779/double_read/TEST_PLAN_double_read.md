# Test plan: double reading of every figure in the 166 groups of lee1779

Written 14 Nov 2026, about 23:00 EST (15 Nov 04:00 UTC), before any crop for this check was cut and before any reader
was started. Worker: Claude (Opus 5.5). Readers: two separate Opus 5.5 agents.

## Why

Two tests on 71 groups glossed in 1778-79 missed the 80% mark (54 of 71, then 55 of 71). In both, most misses were
misread figures (the clerk's 4 read as 1, 3 as 5, 2 as 3, a dotted x), not wrong look-ups. The same weakness must be
assumed in our own transcription of the 166 groups. This check measures it.

## What is frozen (our current transcription, "reading O")

Worktree `output/push_2026-11-14/wt-lee1779`, branch `lee1779-beling` e27ac0a42.

| File | sha256 |
|---|---|
| targets/lee1779/decoding.tsv (column `group_as_written` is reading O) | a0f26f085f5994ad8bb8dec101fdb8c14c1cd3636399a7c3c9032575c2fb93d0 |
| targets/lee1779/transcription.md | dc189d3c18112c74ef997b6128f0effcfc00e08f0cdf7ae0eb6f9d50bebc9b4c |
| targets/lee1779/key.tsv | 5d7e2cdedeef96348c41744fb0bc7637208b0aba2b5708bbad053914d4e135a9 |
| targets/lee1779/received/received_copies.tsv | 39e0cc26806ce777795bfe8d35752468a03808d8d7a61a57b4238a0a263d7dcc |

## Images

Papers of the Continental Congress (National Archives microfilm M247), item 102 vol. 3, Arthur Lee's letter book
(National Archives catalog 502968528), images 0019, 0027, 0035, 0041, 0042, 0122, 0123, 0183, the 1610-pixel copies
already on disk in `sources/raw/sweep_pcc3_2026-11-14/full/502968528/`. Nothing is re-fetched (all eight are present).

## Readers and blinding

- Reader A and reader B: two Opus 5.5 agents started fresh, each with its own folder. Each is given only overlapping
  horizontal strips of the letter region of each page (full page width, about 360 px high, about 80 px overlap, the
  letter book has no interlined words), a small zoom script, and these instructions. They are told nothing about the
  content, the dictionary, our reading, the other reader, or how many groups to expect.
- They are told not to open any file outside their own folder (no `targets/`, no `output/push_2026-11-14/`, no other
  reader's folder, no notes).
- Each transcribes every code group in reading order: page number, column letter, line numeral as written (roman or
  arabic) and its value, any ending after a dash, the plain word just before the group (for alignment only), firm or
  doubtful, and alternatives.
- Two batches per reader: batch 1 = letters 1-3 (images 0019, 0027, 0035); batch 2 = letters 4-6 (images 0041, 0042,
  0122, 0123, 0183). Each reader freezes each batch file (sha256 and time) before I open it.

## Seeds (known figures; a batch that misses one is rejected and redone by a fresh Opus reader)

Strips cut below the glosses in the second gloss test (`output/push_2026-11-14/lee1779_push_work/gloss2/strips/`), from
Lee's letters of 1778-79 in item 83, figures settled on the image and by the gloss in that test. They are mixed in as
sections of their own, not labelled as seeds.
- Batch 1: S09 (81,b,XX; 165,a,VII-a; 99,b,XXX-d) and S06 (356,a,XXIX-d; 382,b,XXVIII required; 259,b,XXXI and
  43,a,XXIII recorded but not required, as they were misread in the second test and settled only after a second look).
- Batch 2: S31 (335,b,VI; 255,a,XX; 96,b,XX required; 348,b,XIII not required, value unsettled) and S18 (332,b,XXVIII;
  389,a,XVIII; 82,b,V-s).
- Required: page, column and line all right (ending not required); batch 1 five groups, batch 2 six groups.

## Comparison (after both readers have frozen both batches)

1. Align each reader's groups to reading O, letter by letter (sequence alignment on the figures and the word before).
2. Three-way table for all 166 groups: O, A, B, and for letters 2-4 the received copy (C, from
   `received/received_copies.tsv`, read 14-15 Nov by an earlier agent who had seen O; a separate document, so a
   further witness, but not a blind reading).
3. Every group where any two of O, A, B differ in page, column or line: I look at the image (1610 px and, where it
   exists, the full-size copy in `sources/raw/lee1779_push_2026-11-15/lb102v3/`), look up each candidate in the 1776
   dictionary (page images where on disk, else the OCR line table), and record what the image shows.
4. Rule (fixed now): a group is **firm** only if at least two independent readings (O, A, B; C counts as a further
   witness for letters 2-4) agree on page, column and line AND the entry so found fits the sentence. If the readings
   give two possible words, both are printed (`[a / b]`) and the group is doubtful. A group is never settled by sense
   alone. My own look at the image settles which candidate the image supports but does not count as a reading.
   A group with no candidate that both has two agreeing readings and fits is doubtful (if a word fits) or unread.
5. Grades already lower than firm stay at least as low unless the rule above makes them firm.

## Measures reported (fixed now)

- Agreement A with B: share of the 166 groups on which they agree in all three parts.
- Agreement of each reader with O.
- **Figure-reading error rate of O**: share of the 166 groups where O's `group_as_written` differs in page, column or
  line from the figure settled by the rule (groups where O gave the figure as doubtful with an alternative count as
  wrong only if neither O's main reading nor its alternative is the settled one; counted separately). Groups that end
  doubtful or unread are reported apart (not counted as right or wrong). Per letter.
- For letters 2-4: every place where the letter book (settled) and the received copy differ.
- What the rate implies for letters 1, 5 and 6 (no received copy): the expected number of figure errors left there
  after this check.

## One run

The comparison is made once. Nothing in the readers' frozen files is changed. Later second looks are recorded apart.

## Addendum, 15 Nov 04:30 UTC (after both readers froze batches 1 and 2; I had seen only the group counts per section and the last eight rows of reader A for section sec03)

My strips of image 0019 stopped at y = 1450; letter 1 runs to about y = 1820. Both readers returned 30 groups for that
section, where our transcription has 44. Correction, made before looking at any reading: a batch 3 for both readers,
section sec12 = image 0019, y 1370-1830 (overlapping the last strip of batch 1, so the groups cut at its lower edge are
read again), with seed sec11 = gloss2 strip S27 (314,a,XXVIII and 99,a,XVII required). Groups read twice by a reader
take the batch-3 reading where the batch-1 strip cut them.

## Seed result and redo, 15 Nov ~04:50 UTC

Seed check: batch 2 and batch 3 passed for both readers. Batch 1 FAILED for both: on S09 both read 84,b,XX (81 given
only as an alternative; reader A also read 163,a,VII, 165 as alternative). The same seed was also read 84 by both
readers of the third test. On the image the figure is an 8 followed by a 1 with a hooked top, which in that hand is a 1
(the second test's transcriber read it 81, and 81,b,XX gives the glossed word). As the plan requires, batch 1 is
rejected for both readers and redone once by two fresh Opus readers (A2, B2), same strips and seeds, with one added
sentence for all redo readers: "in some hands the 1 has a hooked or flagged top and is not a 4". If a redo misses a seed
again, that is reported and the batch is used with the failure stated.
