# Check of the contributor's key and reading (8 Nov 2026)

What an AI model (Claude) checked of the submission by Harumi-Matsuba (issue #204, repository `fossey1710-public`, commit 4197d83).
The Beinecke images are not reachable from the project's environment (collections.library.yale.edu is refused by the network
policy), so **no transcription was compared with an image by the project**, and the spot check of the 9-or-g and 1-or-long-s places
promised on the issue could not be made. No human has checked the transcription, as the contributor says.

## 1. The reading is the key applied to the transcription

The key of nine letters (1 a, 2 e, 3 i, 4 o, 5 u, 6 l, 7 m, 8 n, 9 r) was applied to `data/transcription/` line by line and
compared with `data/reading/`: 547 of the 553 lines are identical; the other six are the contributor's comment lines (in
Japanese) that mention image numbers written in digits. The consolidated files `transcription.txt` and `reading.txt` keep the
one-block-per-image order.

## 2. Control: does the key make the notebook's own vocabulary?

The contributor's control (1,000 shuffled keys, none reached the real key) is in `contributor_method.md`. A different control was run
here, because a word list of common English words does not separate keys when only nine letters are replaced and the rest of
every word stands as written (it covers 0.484 of the decoded letters with the key and 0.411 with the best of 300 shuffled keys,
which is no evidence either way). The notebook itself offers a better test: 242 words stand in clear inside the cipher lines
and 1,640 plain tokens (424 types) stand outside them. Each of the 1,107 tokens that contain a digit was decoded and looked up among
the words written in clear anywhere in the notebook. With the key 55.4% of them are such words; the best of 1,000 shuffled
keys (the nine letters permuted over the nine digits) reaches 22.0% and the mean is 5.0%. This is a check that the key makes
the notebook's own words, with the same material the key was read from (images 18 and 19), so it is not independent proof.

## 3. What the project did not check

- Any image, including the heading of image 18 and the cipher line of image 19 on which the key rests.
- The 13 places where the digit 9 and the letter g are written alike, where "the reading that makes a word was taken" (`g9.tsv`);
  the contributor reports 3,359 of 3,490 symbols (96.2%) with that step and 3,332 of 3,492 (95.4%) without it.
- The second readings (`contributor_second_reading.md`): Claude Sonnet agrees with the first reading on 90.2% to 90.7% of the
  decoded characters over all 36 images and OpenAI Codex on 91.3%, from the images alone. Two models agreeing on a letter does not
  make it right, and 9 against g and 1 against the long s remain places where both could be wrong the same way.
- Whether the six lines of the Latin drug names listed as open could be read from a reference text.
