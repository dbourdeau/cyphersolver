# PREREG: which Entick printing fits the Cossit/Summer code and the f.347 glosses

Written 12 Nov 2026, before any candidate printing is scored. One scoring run.

## What I have already seen (disclosed, not evidence)
- The 12 Nov readings (`../../research_2026-11-12/haldimand_cossit/readings.md`), which used the 1781 London (Dilly)
  printing, IA `11280377bsb`, and an OCR-derived row grid.
- One page by eye before writing this: 1781 p. 10. Counting the right column from the top by eye, row 28 is
  "Alarm or Alarum, s." and row 34 is "Albion" (row 32 "Alb", row 33 "Albeit"). So the 12 Nov grid was one row
  off on that page. This suggests some "1-2 rows off" claims may be grid errors, not edition differences.
- A rough OCR word search (no scoring) on the candidate files, which only showed that the OCR is noisy.
- The f.347 glosses re-read on the frame: Lameness[?], ten, Liable, being, left / Combat, 1, pray, formidably /
  "them" above 13-13. They are in the same hand as the cipher figures.

## Candidates (all Internet Archive, reachable by curl)
1772 `bim_eighteenth-century_the-new-spelling-diction_entick-john_1772`; 1773 `..._1773`; 1776 `..._1776`;
1781 `11280377bsb` (baseline); 1782 `bim_eighteenth-century_the-new-spelling-diction_entick-john_1782`;
1787, 1788, 1790, 1791 `bim_eighteenth-century_enticks-new-spelling-di_entick-john_<year>`; 1790 `10582072bsb`.
(Google Books and HathiTrust could not be searched by curl: API quota / JS page / Cloudflare check.)

## Anchors (fixed now): `anchors.tsv`
- Set A (79): pairs marked [V] in the 12 Nov readings; target = the 1781 headword named there.
- Set B (28): pairs read [I] by sense or said to be 1-2 rows off in 1781; target = the intended word's headword.
- Set C (9): the f.347 glosses; target = the gloss word. Combat (312), pray (215), ten (96) and them (13) cannot
  be at those pages in any alphabetical Entick of about 470 pages, so they are expected to miss everywhere;
  they stay in the set as written.

## Row rule
Row = the line's number counted down its column from the first printed line below the running head (1..38),
counting every printed line. Either column. Counted by eye on the page image (band crops with row labels whose
alignment is checked on a crop of the top rows of the same column).

## Scoring
Stage 1 (page screen, automatic, OCR): for each candidate X and each set-A anchor, is the target a line-initial
headword on printed page P of X? (normalised: lower case, long s/f merged, letters only; exact for words of
<= 4 letters, edit distance <= 1 for longer). PageScore_A(X) = count.
Stage 2 (rows, by eye) for every X with PageScore_A(X) >= 0.5 * PageScore_A(1781): for every anchor in A, B
and C, look at page P of X and record the row (L or R) of the target, or "not on page".
- Exact hit: target (or a headword with its stem) at row r, either column.
- Near: on page P within 1-2 rows of r. Page: on page P further away.
- EncScore(X) = exact hits in A + exact hits in B.  GlossScore(X) = exact hits in C.

## Decision rule
- Best fit for the encoders = highest EncScore. Another printing beats 1781 only if its EncScore is at least
  3 higher than 1781's; otherwise 1781 (or an identical setting) stands.
- A printing fits the glosses if GlossScore >= 4 of the 5 alphabetically possible glosses (Lameness, Liable,
  being, left, formidably). It beats 1781 for the glosses only if its GlossScore is at least 2 higher.
- If no scanned printing passes stage 1 except 1781, report that the other scanned printings are re-set
  (different pages) and the gloss question stays open.

## Not allowed after seeing results
No change to the anchors, targets, row rule, thresholds or candidate list. Re-reading a pair during the
later decipherment is reported separately as [I]/[V] reading work, not as part of this score.
