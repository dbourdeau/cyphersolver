# Aid to Siena in Philip’s dispatch of 6 October 1552

Two consecutive cipher lines on folio 34r match the passage about aid to Siena on the Spanish sheet kept with Prince Philip’s dispatch from Monzón to Ferrante Gonzaga, governor of Milan. The two exact fragments scored **15** together. The highest of 1,000 shuffled tables scored **10**. Brice Dudout had identified the dispatch, and #828 had already identified the accompanying clear witness on 33r–v. This comparison concerns lines 2 and 3 of 34r within that known document. The earlier word-sign and terminal-line studies sampled other lines. Modena, Biblioteca Estense Universitaria, Autografoteca Campori, Lettera F, Felipe II, sfasc. I, cc. 32–34. [Manuscript](https://edl-jarvis.cultura.gov.it/meta/iiif/897e61b7-4957-4f07-b4d2-debae54659a1/manifest) · [Prior findings, witness transcriptions and key attribution](../NOTES.md)

## What the signs yield

The readers independently marked 26 positions on the second line and 25 on the third. All 51 positions paired. At 31 positions both recognized the same published label at medium or high confidence. Thirty emitted a unique non-null value (58.8%), giving 54 letters. Zero-based, end-exclusive offsets below refer to the normalized reference with spaces removed. [Aligned signs](34r/positions.tsv) · [Exact reference](34r/reference.txt) · [Mechanical streams and results](results/34r/result.json)

| Cipher line | Exact letters | Reference span | Location on the clear sheet |
| --- | --- | --- | --- |
| 2 | `conci` | [16, 21) | First five letters of *conciertos* |
| 3 | `corroquepo` | [56, 66) | Begins inside *soccorro* and ends after the first two letters of *podia* |

The third line emits `lsocorroquepo` without a break. Six signs give `so | co | rr | o | que | po`. The clear sheet reads *el soccorro, q[ue] podia*, “the help he could give.” The mechanical spelling *socorro* has one fewer *c* than the clear reading *soccorro*. One complete reference word lies inside the scored spans, *que*, at the agreed single sign at x=320 on line 3. The companion sheet supplies both word boundaries. The count of newly established free-standing cipher words is zero, and the comparison adds no key value. [Reader A](34r/reader_a/reading.tsv) · [Reader B](34r/reader_b/reading.tsv)

## Registered comparisons

All four comparisons used 1,000 controls each. The 32v repeats used larger images of previously studied lines and fresh readers. The fourth-line test used an interval predicted from anchors on either side. Its score counts the longest exact fragment, while each two-line score counts ordered, non-overlapping reference spans.

| Folio and lines | Shared labels | Usable signs | Exact fragment(s) | Score | Higher / tied | Maximum | Decision |
| --- | ---: | ---: | --- | ---: | ---: | ---: | --- |
| 32v, 2–3, repeat | 28 | 26/45 | `ritosob`, `godemen` | 14 | 10 / 4 | 16 | Miss |
| 32v, 4, prediction | 14 | 11/25 | `dello` | 5 | 1 / 8 | 6 | Miss |
| 32v, 5–6, repeat | 30 | 26/47 | `porser`, `termino` | 13 | 31 / 12 | 17 | Miss |
| 34r, 2–3, new pair | 31 | 30/51 | `conci`, `corroquepo` | **15** | **0 / 0** | **10** | **Pass** |

The smaller-image 32v trials had also missed. Lines 2–3 scored 14 with 19/46 usable signs (maximum 16, nine higher, one tied). Lines 5–6 scored 0 with 5/49 (maximum 16, 116 higher, 884 tied). The native repeats each emitted 43 letters. The fourth-line fragment on 32v enclosed one word of the predicted text against a requirement of two and fell below the eight-letter and 55% coverage thresholds. The 34r control frequencies were 886 scores of 0, 109 of 5, four of 6 and one of 10. The page, its earlier anchors and the accompanying Spanish were already known when the reference window was chosen. Independence applies to the two new sign readings. [32v lines 2–4 plan](32v_2_4/PLAN.md) · [32v lines 5–6 plan](32v_5_6/PLAN.md) · [Saved results and controls](results/)

## Freeze and replay

Before the two independent readings, the 34r plan fixed the rows, Spanish window, score, table, plate index, six aliases and seed 1552100633. Readers saw only the native strips and value-free numbered plates. The scorer paired reciprocal nearest centers on an 800-unit grid within ten units. Only agreed medium/high labels could contribute. Unresolved values broke a run, and confirmed nulls were silent. To pass required at least 55% usable positions, 20 letters, two ordered spans of at least five letters each, at least 14 letters combined and a score exceeding every shuffled table. The six joined plate labels had identical historical values on both sides (*que*, *y*, *nu*, *da*, *di*, *tra*). The first printed component represented each join in both real and shuffled tables. [Six exact aliases](34r/crosswalk.tsv) · [34r plan](34r/PLAN.md)

| Plan | SHA-256 |
| --- | --- |
| 34r, 2–3 | `4379b94f2184cd7d037524335c1222ed14f4f17a5f824eeebf04a68043e7d761` |
| 32v, 2–4 | `f363b78a709f29cf513ad1b5ae90642a8947681b53db369c8760bf3a17dcf786` |
| 32v, 5–6 | `135e5e8a24d16761f8aae6a3ea0471f0ce1219830bc6a9f861d9016274cfb367` |

The 34r plan and scorer were frozen at 06:12:47 UTC on 20 November 2026 and both finished reader files at 06:14:57 UTC. All four comparisons were evaluated once under their respective plans. For an offline reproduction from this directory run `python3 verify.py`. It stages the frozen inputs in temporary storage, checks the repository’s unchanged K4 and shape index, and compares each result, position table and ordered vector of 1,000 scores with the original. The stored control text wraps 25 scores per line. The 34r position display uses `?` for blank fields. Source image bytes are available separately through the archive. The native 34r crop geometry and row-image hashes are preserved with the freeze. [Source region URLs and SHA-256](sources.tsv) · [34r freeze](34r/FREEZE.json) · [Reader freeze](34r/INPUT_FREEZE.txt) · [Crop geometry](34r/strips.py)

AI agents did this work; no person has checked it.
