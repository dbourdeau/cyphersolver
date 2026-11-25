# 1643 letter (23 Jan 1643, inv. 1141 copy 2): first pass, figure of record (written 25 Nov 2026 ~21:15 UTC, before any gloss was opened)

- Freezes: method frozen/FREEZE_METHOD_1643.txt (21:09:15 UTC, METHOD e2dd2163..., run_1643.py 23cfd4c3...); transcription frozen/FREEZE_T1643.txt
  (21:13:20 UTC, T1643 md5 2c36b774..., sha256 bca33dfa...). Decode run once at 21:13:27-21:13:34 UTC (decode_1643_output.txt).
- Coverage: 82/86 groups keyed = 95.35%. Unkeyed: 12 (x1), 39 (x1), 74 (x2) = 4 occurrences; 82 + 4 = 86.
- FIGURE OF RECORD: 59/86 groups covered by dictionary words = 68.60% (>= 65%). Per page: 901 49/59 = 83.05%; 902 0/5 = 0%;
  905 10/18 = 55.56%; 906 0/4 = 0% (49 + 0 + 10 + 0 = 59; 59 + 5 + 18 + 4 = 86). Runs fully covered 10/21.
- Key shuffle: seed 20261112 0/5,000 >= 59 (max 48 = 55.81%, mean 21.98 = 25.56%); seed 7 0/5,000 (max 45, mean 22.05).
- Matched control (ciphertext shuffled, real key): seed 20261112 0/5,000 >= 59 (rank 1 of 5,001; max 54 = 62.79%, mean 36.14 = 42.02%);
  seed 7 0/5,000 (rank 1 of 5,001; max 55 = 63.95%, mean 36.07 = 41.94%).
- PASS on all three pre-set criteria (>= 65%; 0/5,000 key shuffles; 0/5,000 ciphertext shuffles) on 86 groups. Margin over the best
  ciphertext shuffle is small (59 vs 55, 4 groups), so this is a modest pass.
- Decoded words (DP segmentation): geuen, negotie, rycx, ontseyt, ses, winst, tonnen, uoor, iapan, noort; first run 'd aduis ? n uyt'.
- Failing runs: single numbers between letter-cipher signs (21, 21, 24, 2, 2, 1 21, 12 16, 24 20: 12 groups that by rule can never score);
  902.4 '2 12 10 20 24' -> n?aow (probably a clear list of numbers, doubt flagged before the decode); 905.3 '24 39 17 30 16 5 50 20' -> w?ippbno (unread).
- Error in the frozen file header (not changed): it says "21:10-21:30" UTC for the transcription; the work ran about 21:09-21:13 UTC (freeze at 21:13:20).
- Exposure: as listed in METHOD_1643.md. Second transcription: none yet (owed). Not blind in the strict sense: the transcriber had KEY_v2 in context.
