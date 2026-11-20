# Re-check of the corpus's own model-made transcriptions (20 Nov 2026)

Prompted by round two (`RESULTS_round2.md`): which corpus transcriptions sit in the hands the benchmark found hard?
Scripts: `recheck_fetch.py`, `recheck_direct.py`, `recheck_prep.py`, `recheck_passes.py`. Passes: `passes3_recheck/`.

## A. Ours against DECODE's human transcription of the same record
Digit streams. Not fully independent: the notes show ours were at some point checked against DECODE's.

| record | target | human signs | all differences | digits read differently | only in ours | only in human |
|---|---|---|---|---|---|---|
| R922 | rakoczi1704 | 2,004 | 0.8% | 7 (0.35%) | 1 | 8 |
| R483 | rakoczi1711 | 7,090 | 2.1% | 25 (0.35%) | 109 | 16 |
| R852 | rakoczi1704 | 1,390 | 7.3% | 13 (0.9%) | 58 | 30 |
| R912 | rakoczi1704 | 4,420 | 4.7% | 81 (1.8%) | 95 | 31 |

Most of the difference is coverage (groups one side has and the other lacks), not digits read differently. Two DECODE
transcribers differ by about 2% (`human_ceiling.json`).

## B. One fresh blind Fable pass against ours

| record | target | our signs | pass vs ours | note |
|---|---|---|---|---|
| R740 | papai1706 | 456 | 0.2% | |
| R7482 | turculet1709 | 603 | 0.8% | |
| R7481 | turculet1709 | 889 | 2.9% | the pass reads the hand's flagged 6 as 5 and 3 as 8; ours documents the trap and was checked against the contemporary decipherment |
| R852 | rakoczi1704 | 1,418 | 3.3% | pass vs human 10.5% |
| R912 | rakoczi1704 | 4,484 | 7.4% | pass vs human 11.2%; the pass agent called its own R912 low-confidence (very small hand) and used the interlinear text |

The passes saw interlinear decipherments on the same tiles and used them, so they are blind to our files but not to
the page's own plaintext.

## Reading
- R740, R7481, R7482, R922, R483: hold up.
- R852: ours is closer to the human transcription than a fresh pass is; the difference from the human one is mostly
  coverage. R852 is read from its clear copy, so the reading does not rest on the figures.
- R912: the weakest. 1.8% of digits differ from the human transcription and a fresh pass differs from both; the target
  notes already class R912 as decoded, not read, with holes on p. 2.
- Not doubtful after checking the records: papai1706 (ten of eleven letters are DECODE's transcriptions), balbases1677
  (tokens largely DECODE's), turculet1709 (checked against the interlinear decipherment), henter1707 (clear text).
- Not re-checked: papai1710 R731 (graphic signs, no comparable labels) and the four BNE Madrid manuscripts
  (aragon1676, olivares1626, dormer1694, coloma1622): BNE Digital blocks scripts, needs Chrome.
