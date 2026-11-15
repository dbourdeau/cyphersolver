# Test plan: third test of the lee1779 rule, Arthur Lee to Henry Laurens, Paris, 7 December 1778

Written 15 Nov 2026, about 04:20 UTC, before the images of this letter were fetched or seen by me, and before any gloss
on it was read. Worker: Claude (Opus 5.5). Transcribers: two fresh Opus 5.5 agents.

**This is the third attempt.** The first two tests, on 71 groups glossed in Lee's letters of 1778-79 (Papers of the
Continental Congress, item 83), missed the 80% mark: 54 of 71 (76%) and 55 of 71 (77.5%). Most misses were misread
figures. This test is designed to separate the reading of the figures from the rule, and it is run once whatever it shows.

## Document

University of South Carolina, South Caroliniana Library, digital collection "American Revolution" (amerrevsc), item
1888: "Letter, 1778 December 7, Paris, France, Arthur Lee to Henry Laurens", two pages (CONTENTdm page pointers 1886,
1887). Upstream lead 1435 in `research/leads.json` of Daniel Bourdeau's repository; its vetting (29 Oct 2026, not by us)
counts about 12 code groups on page 1 and 5 on page 2, with the plain word written above each group by a contemporary
hand. The New York Public Library item cited in the same lead (Arthur Lee to Samuel Adams, 27 Apr 1779, "Cyphers A.L.
to S.A.") is a numbered list of names, not this letter, and is not used.
Checked before writing this plan: no file of ours (research/, output/) records any reading or look-up of this letter
(grep for "amerrevsc" and "7 Dec 1778": only sweep triage rows and the lead itself).

## Frozen rule (unchanged)

Entick, *New Spelling Dictionary*, London 1776; "page, column, line" = the Nth headword entry counted down that column,
skipping running head, letter headings and run-over lines; pages 454-455 Christian names in columns a-e; endings after
the group are inflections. Frozen in `targets/lee1779/check/BLIND_FREEZE.txt` (sha256 8f31b439...4e3fb34 in the first
test plan). Look-ups use the 1776 page images of the Internet Archive copy
(`bim_eighteenth-century_the-new-spelling-diction_entick-john_1776`); pages not on disk are fetched one at a time.

## Procedure (one run)

1. **Fetch** the two page images (CONTENTdm IIIF, one request at a time, 1.1 s apart, stop at the first 403 or 429).
   Raw copies with SHA256SUMS in `sources/raw/lee_laurens_17781207/`.
2. **Strips that hide the glosses.** I locate the code groups on a copy reduced to about 300 px wide, at which the
   interlined words cannot be read, and cut strips at full size from just under the interlined line to below the
   group's line. Each strip is checked to show no gloss letters; any strip that shows one is recut before use. I do not
   view the full-size page or the glosses until step 6.
3. **Two blind transcriptions.** Readers C and D (fresh Opus agents, own folders) transcribe page, column, line and
   ending of every group from the strips, with zoom, figure by figure. Seeded with gloss2 strips S09 and S31
   (required: 81,b,XX; 165,a,VII; 99,b,XXX; 335,b,VI; 255,a,XX; 96,b,XX); a reader missing a required seed is replaced.
   Each freezes its file (sha256, time).
4. **Settle disagreements on the strips, before any look-up.** Where C and D differ, I look at the strip (zoomed) and
   record the figure the image supports, or "unsettled" with both candidates. Frozen as `figures_settled.tsv`.
5. **Look-up.** Each settled group (and each candidate of an unsettled one) is looked up by the frozen rule on the 1776
   page image. Controls on the same settled figures: C1 page +1, C2 page -1, C3 the other column (not on 454-455).
   Frozen as `lookup3.tsv` before step 6.
6. **Glosses.** Only now I view the full pages, write the gloss over each group into `glosses3.tsv`, and score.

## Scoring and pass mark (fixed now)

- Same = the headword is the glossed word; other form = same headword, another form the writer intended (plural,
  tense, derived word); one off = entry directly above or below; different = anything else. Hit = same + other form.
- An unsettled group counts as a hit only if its first-listed candidate (C's reading) hits.
- **Pass: hits in at least 80% of the group occurrences found; each control (C1, C2, C3) under 10% hits.**
- Also reported (not part of the pass mark): the score of each reader's own figures, unsettled; agreement of C and D;
  groups that recur in the 1779-80 letters or in the first two tests (not new evidence about the rule).
- If fewer than 10 groups can be read from the images, the test is reported as too small and not scored.

## Addendum, 15 Nov ~04:35 UTC, before any gloss was read

The page images are faint (light brown ink); at 320 px I could see where the writing is but not place the code lines
reliably, and an ink profile did not separate the interlined words from the lines. Change to step 2: the strips are cut
by a separate Opus agent (the "cutter"), who views the full pages, cuts strips that show each line holding code groups
with the interlined words above it excluded, and checks every strip for gloss letters. The cutter is told to report only
strip names and pixel boxes, never what any interlined word or group says, and writes no transcription. I then check
the strips myself (they hide the glosses). I have viewed the pages only at 320 px. Everything else is unchanged.

## Seed result and redo, 15 Nov ~04:50 UTC (before any look-up or gloss)

Both readers C and D read the S09 seed 81,b,XX as 84 (81 as alternative): seed missed, both rejected. Redone once by
two fresh Opus readers (E, F), same strips, with the added sentence "in some hands the 1 has a hooked or flagged top and
is not a 4". C and D's frozen files are kept and reported but not used for the score.
