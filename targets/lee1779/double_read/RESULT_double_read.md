# Double reading of every figure: result (15 Nov 2026)

Plan: `TEST_PLAN_double_read.md` (sha256 in `PLAN_FREEZE.txt`, written before any strip was cut; two addenda, both
before the comparison). Worker: Claude (Opus 5.5). Readers: Opus 5.5 agents. All image readings were made by AI
agents; no person has checked them.

## What was done

- Our transcription ("O", `decoding.tsv` column `group_as_written`, frozen at e27ac0a42) against two blind readers,
  A and B, who saw only strips of the 1610-px letter-book images (Papers of the Continental Congress, microfilm M247,
  item 102 vol. 3, National Archives catalog 502968528, images 0019, 0027, 0035, 0041, 0042, 0122, 0123, 0183), not our
  reading and not each other's (`strip_key.tsv` gives every strip's source box; the strips themselves are not
  committed).
- Batch 1 (letters 1-3) was redone: both first readers misread the seed 81,b,XX as 84 (81 only as an alternative), so
  the plan rejected the batch. Redo readers A2 and B2: A2 read every seed right; B2 again read 84 and is used with that
  failure stated. Batches 2 and 3 passed their seeds for both readers. Reader A = A2 (batch 1) + A (batches 2-3);
  reader B = B2 (batch 1) + B (batches 2-3). The rejected batch-1 files are kept (`readerA_batch1.tsv`,
  `readerB_batch1.tsv`).
- Batch 3 was added because my strips of image 0019 stopped short of the end of letter 1 (addendum 1).
- Alignment by sequence (`../scripts/double_read_align.py`), then every group where any two readings differ was looked
  at on the image and each candidate looked up in the 1776 dictionary (`../scripts/double_read_settle.py`,
  `double_read_settled.tsv`).

## Numbers

| Measure | Result |
|---|---|
| A and B agree on page, column and line (a figure one reader marks as lost counts as agreeing) | 162 of 166 (differ: 59, 158, 163, and 161 where B could not read the line) |
| A agrees with O | 161 of 166 (differ: 18, 44, 59, 128, and 144 where both readers leave the blotted column open) |
| B agrees with O | 159 of 166 (differ: 18, 44, 128, 144, 158, 161, 163) |
| All three agree | 158 of 166 (150 on the raw alignment; eight rows were alignment or order slips, checked by hand) |
| **O wrong (settled figure differs from O's main reading)** | **1 of 166 (0.6%)**: id 128, 455,d,XXVII (O wrote "455?a27"; A, B and the received copy d) |
| O's alternative right, main reading wrong | 1 (id 44, 63,a,XXXII) |
| Unsettled after the check | 4: ids 18, 59, 113, 158 |

Per letter, O wrong / O alternative right / unsettled: letter 1 (29 Mar 1779) 0 / 1 / 1 of 44; letter 2 (22 Apr)
0 / 0 / 1 of 16; letter 3 (27 Apr) 0 / 0 / 0 of 23; letter 4 (21 May) 1 / 0 / 1 of 56; letter 5 (27 Sep) 0 / 0 / 1 of
24; letter 6 (29 Feb 1780) 0 / 0 / 0 of 3.

## Groups changed

- 18 (letter 1) charges -> [charges?]: first figure at the gutter; O 82, both readers 12 (no entry at 12b37: the
  1776 dictionary has no arabic page 12). 82b37 Charge rests on O alone.
- 59 (letter 2) exertions -> [exertions?]: page under a blot; O and B "2", A 102 (Continuous, no fit); 152b9 only
  on the received copy.
- 113 (letter 4) contempt -> [contempt?]: the letter book reads 100,b,XXXVI on all three readings (Conspicuously,
  no fit); the received copy 101,b,XXXVI (Contempt). The two copies differ.
- 158 (letter 5) [Thomas?] -> [Gerard? Thomas?]: middle figures under a blot; O and A 455,a,XIV (Gerard), B 445; the
  e of 455e14 (Thomas) rests on one earlier look.
- Counts: 151 firm, 11 doubtful, 4 unread -> **148 firm, 14 doubtful, 4 unread**.

## Where the two copies differ (letters 2-4, settled letter book against the received copy)

Figures differ in two groups: 67, letter book 82,b,XXI (Chaplain) and received copy 82,b,XXXI (Character); 113,
letter book 100,b,XXXVI and received copy 101,b,XXXVI. Elsewhere the received copy fills a digit or letter that is
lost or blotted in the letter book (56, 59, 106, 120, 128) or is itself blotted (62, 81, 89, 91); the received copy
of letter 4 has one group more (454,a,V-s). Details in `../received/received_copies.tsv`, column `diff`.

## What the rate implies for letters 1, 5 and 6 (no received copy)

On this check our transcription of the clerk's figures was wrong in 1 group of 166 and right only as an alternative
in 1 more; in letters 1, 5 and 6 (71 groups) no figure of ours was overturned, one was settled from its alternative
and two stay unsettled. This measures disagreement among readers, not truth: the seed showed that five of six Opus
readers can misread the same figure the same way (81 as 84), and a misreading shared by all three readings would not
be caught. The letter-book hand is far easier to read than the hand of the letter Lee sent to Laurens (the third gloss
test found seven misread figures in its 19 groups). For the three letters without a received copy we therefore expect few remaining
figure errors, of the order of one or two groups, most likely among those already marked doubtful, but the number is
not measured and no person has checked the images.
