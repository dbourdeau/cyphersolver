# Two-hundred-and-eighty-second registered predictions: decipherment loop 107, frozen restorations against Mahadevan 1977

- H-1042 817 2 220 ??? 923 740: M77 231; predicted 231 220 233 235 240.
- H-1816 413 575 335 ??? 33 740: M77 717; predicted 717 705 740 760 706.
- H-246 240 233 ??? 804 400: M77 740; predicted 740 741 520 233 705.
- L-78  503 ??? 740 90: M77 615; predicted 615 17 460 2 220.
- M-1783 215 ??? 2 3 425: M77 872; predicted 861 877 740 817 820.
- M-168 920 60 ??? 705 277 31: M77 741; predicted 741 742 2 740 233.
- M-636 216 ??? 2 32 220 235 555 527: M77 861; predicted 861 820 817 2 390.
- M-646 817 2 ??? 440 760 740: M77 176; predicted 240 233 176 220 235.
- M-1397 360 ??? 705 167: M77 904; predicted 904 900 171 368 906.
- M-1650 550 ??? 33 32 760 740 400: M77 861; predicted 705 60 706 240 220.
- H-1035 632 ??? 435 400: M77 255; predicted 255 740 705 140 2.
- M-2045 503 ??? 752 740: M77 615; predicted 615 17 460 1 2.
- M-2109 415 220 ??? 400: M77 740; predicted 740 520 845 705 320.
- M-2111 415 220 ??? 400: M77 740; predicted 740 520 845 705 320.
- - 255 13 744 ??? 740: M77 892; predicted 892 760 100 740 240.

## MR1 top-1 matches the M77 reading in 25%+ of 10+ cases
- 12 of 15.
- **MR1 holds.**

## MR2 top-5 contains it in 50%+
- 13 of 15.
- **MR2 holds.**

## MR3 top-1 beats the frequency baseline (740)
- top-1 12 against 3.
- **MR3 holds.**

## MR4 progress rule: MR1 and MR3 (tier 3 gains its first line)
- MR1 True, MR3 True.
- **MR4 holds.**

## Summary

Held: MR1, MR2, MR3, MR4. Failed: none.

## Audit after the test (added before recording)

8 of the 15 cases are circular: the gap line completed with M77's sign is itself a distinct line of the training data
(H-246, L-78, M-636, M-1397, H-1035, M-2045, M-2109, M-2111; copies of the same text, or the M77 text as an
addition), so the model had seen the answer and M77's 'reading' may be that copy's. Tier 3 counts only texts never
used to fix the model. On the 7 clean cases top-1 matches 4 (H-1042 231, H-1816 717, M-168 741, 255 13 744 [892] 740)
and top-5 holds 5; M-1783 (872) and M-1650 (861) are missed. 7 is below the registered minimum of 10: the set is
withdrawn as evidence for tier 3 and no progress is recorded. H-1816's M77 line also has near-copies (four M77 lines).
