# solver/: how the key of 4 June 1940 was found

| File | What it is |
|---|---|
| `decrypt.py` | decrypts `../transcription.txt` with the keys (and re-enciphers to check) |
| `in12b.txt` | the input of the K2 search: parts 1 and 2 (indicator removed, first transcription) each beside an approximate plaintext taken from the teleprinter copy on frame 0862 and fitted to the letter count of the part |
| `kpw.c` | K2 search independent of K1: after undoing the right K2, neighbouring letters are plaintext letters K1 apart; simulated annealing on K2 with a score over the pairs at distance k1 (tolerance +-1 for misplaced X), for every pair (k1, k2) |
| `grid.sh` | runs `kpw` for k1 = 15-30 and k2 = 15-32; `grid_R.txt` = with the plaintext, `grid_S.txt` = the same with the plaintext shuffled (control) |
| `ana.py` | ranks the (k1, k2) pairs by the margin R - S: (19, 22) alone, 0.267 against 0.093, margin 0.174 where the mean margin is 0.004 and its standard deviation 0.019 (about 9 standard deviations); four independent runs gave the same K2 |
| `k1s.c` | K1 by simulated annealing on German quadgrams with K2 fixed, over parts 1, 2, 3 and 5 (part 4 held out) |
| `mkqg.c` | builds the quadgram table `qg.bin` from a normalised German corpus (CH written Q, X between words); the table and the corpus are not included |
| `parts.txt` | the ciphertext of parts 1, 2, 3 and 5 given to `k1s` (part 4 left out) |

Compile with `cc -O2 -o kpw kpw.c -lm` and `cc -O2 -o k1s k1s.c -lm`. The usage line is at the top of `main` in each file.
