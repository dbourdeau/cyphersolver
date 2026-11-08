# Comparison with the earlier reading (WAINUT)

Earlier work: the reading by WAINUT (https://github.com/WAINUTAI), folder `targets/barlow1807` of the Cyphersolver catalogue, [#231](https://github.com/dbourdeau/cyphersolver/issues/231). Compared at origin/main c9e114cb8. The figures come from `python3 src/compare.py <path to targets/barlow1807>`. WAINUT's files are not in this repository.

## Order and independence
- The first commit here, 59a41ec, is dated 2026-11-02 01:45 UTC; WAINUT's first commit, a36b00240, is dated 2026-11-03 21:19 UTC. **Both are commit dates, not third-party timestamps.** This repository was not public until 4 November 2026, so what can be checked from outside is that WAINUT published first (2026-11-03 23:05 UTC).
- This reading was made without sight of WAINUT's. It was read only after the reading and figures here were measured, and the transcription, key and reading were not changed afterwards. That rests on our own records and cannot be checked from outside.

## Comparison
| Item | Here | WAINUT |
|---|---|---|
| Cipher words | Of 639 (codes and nulls excluded): 595 read (93.1%), 25 with letters that do not fit, 19 uncertain | Of 666: 479 read with no letter changed (71.9%), 119 with a letter changed, 68 doubtful |
| Headline figures | 96.3% per cipher token, 92.4% per word (cipher tokens only) | 1192 of 1379 words (86.4%), 95.1% counting changed letters (clear words included) |
| Agreement with Sonnet's reading (values) | 93.3% (of 3,915) | 93.4% (of 3,932) |
| Agreement with Codex's reading (values) | 91.3% (of 3,927) | 91.2% (of 3,938) |
| How the key was set | From context, seeing the whole text | Annealed on images 1-13, frozen, tested on 14-19 |

The first two rows are **not the same yardstick**. WAINUT froze the key and counts a misfit as a change. Here the key was set seeing the whole text, with relaxations (19 is a or e, 56 is y or w, 10 and 12 may be skipped; `docs/METHOD.en.md`). WAINUT has a held-out test of the key; this work has none. More of the text is read here, but this comparison does not show that the reading is more correct.

## Transcription
The two transcriptions agree at 97.9% in values, 97.8% in names (of 3,934), with 75 differences (`docs/comparison_transcription.tsv`). Agreement with the other readers does not separate them (table above). At the 49 one-to-one differences, Sonnet sides with this repository 16, WAINUT 27, neither 6; Codex with this repository 19, WAINUT 21, neither 9. **The transcription here cannot be called the more correct one, and at these 49 places the answers lean towards WAINUT.** The differences have not been judged on the images, and the transcription here has not been changed for them.

## Key
Of 79 shared signs, 59 have the same value and 20 differ (output of `src/compare.py`). 80=c and 99=b, which WAINUT itself lists as errors in its frozen key, are the values here. 58=m is in this key and not in WAINUT's frozen key. The word codes 4990 (India) and 5650 (British) agree. 4845 is Fort William here and left open by WAINUT (from context in both cases; it occurs once).

## Reading
Aligned word by word there are 101 differences (`docs/comparison_reading.tsv`): 52 marked uncertain only by WAINUT, 8 only here, and 41 that mix differences of spelling, division and code notation with differences of the word itself (not counted apart). Examples of different words: elements / limits, privileges / prejudices, consecrated / inscribed, concerns / interests, purity / piety, a system directed / [?that] [?restricted]. **Which is right has not been checked.**

## New here
- A reading of p03 (which WAINUT calls "in effect not read"). Uncertain words remain on p03 here too.
- Readings of words WAINUT leaves as holes on p08 and p18 (or secret enemies, state [?might] be employed, facility of accomplishing).
- A key corrected with the whole text in view (including 80, 99, 58).

## In WAINUT's work and not here
- The transcription of the letter to Tierney (in clear).
- The held-out test of a frozen key, and a blind reading of three pages.
