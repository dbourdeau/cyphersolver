# Held-out test on Eaton to Madison, 22 October 1802 (T303 roll 2, frame 0320 ff.)

Written 2026-11-10T18:36:05-05:00, before either blind transcription or the edition text had come back.

**Frozen key:** `frozen_key_v1.tsv`, 311 groups, sha256 `e88b2c7f792e0759a38b56f9f14a8809aeaa3f464f06db687edfde379f7e55f4`.
Order of precedence where sources overlap: Tunis single-group words, Tunis syllables serving two or more words,
Bourdeau's Code 16 key at commit c14c822 (plain alphabetic values only), Lear 1813 single-group interlines.
Nothing from the 22 October letter went into it. The Tunis enclosure of 9 October did; it is a different document on frames 0299-0303.

**Transcription:** two agents transcribe the numerals independently, with no key and no access to project files.
Reported first: the share of groups on which they agree. The test uses groups where A and B agree; the rest are listed.

**Truth:** the Madison Papers editors' printed decipherment of the letter (fetched by a third agent, kept from the transcribers).

**Measure (one run):** for each coded stretch, take the edition's words for that stretch (located by the clear text on either side),
letters only. Take the key values of the covered groups in order. Count the largest number of them that can be laid on the
text in order as substrings, where a matched value must start within 12 x (k+1) letters of the previous match's end, k being
the number of groups skipped since that match. Score = matched / covered. Also reported: covered / all groups.

**Baseline:** the same computation with the frozen key's values dealt at random to its groups, 200 shuffles; mean and maximum.

**Read as a pass** if score >= 0.85 and score minus shuffled maximum >= 0.30 (Dudout's convention in cyphersolver).
Whatever the number is, it is reported.

## Outcome and replacement test (added 2026-11-10T18:59:42-0500)

The 22 October passage proved to be Eaton's repetition of his 9 October postscript, so it is not new text.
Result recorded in `output/eaton_heldout_2026-11-10/heldout_result.json`: the two blind readers agreed on 85 of 92 groups;
score 0.898 (44 of 49 covered groups), shuffled mean 0.119, maximum 0.224. None of the postscript's alignment was in the frozen key.

**Replacement test on new text, declared before its transcription has come back:** Pinckney's Code 16 re-encipherment of
his 21 July 1795 passages, with Taylor's interlinear (NARA M31 roll 7, frames 0018, 0019, 0021), being transcribed by an
agent with no access to any key. Same frozen key (`frozen_key_v1.tsv`, sha256 above). Measure: over interlined groups that
the key covers and whose interlinear placement the transcriber marked clear, the share where the key value equals the
interlinear word or is a contained piece of a multi-group word (letters only). Baseline: key values dealt at random to the
key's groups, 200 shuffles, mean and maximum. One run. Pass if share >= 0.85 and share minus shuffled maximum >= 0.30.

**Second replacement test, declared 2026-11-10T19:02:51-0500 before any image of it was opened:** Eaton to Madison, 25 May 1801
(RG 59, Consular Despatches, Tunis, vol. 2 pt. 1; about 109 coded words with Wagner's interlinear, per the Madison Papers).
Whether it is in Code 16 at all is not known; if its groups do not use 663/1518/1490 for the/of/to the test is reported as "different code".
Same frozen key, same measure and pass rule as the Pinckney 1795 test above.
