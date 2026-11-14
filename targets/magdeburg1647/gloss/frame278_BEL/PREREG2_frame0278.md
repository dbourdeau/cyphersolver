# Pre-registration 2: frame 0278 glosses as a second check of the frozen key

Written 11 Nov 2026 (evening), before the frame-0278 transcription files or any scoring script exist.

## Material
Frame 0278 (f. 242), right page: "Signatura catalogi sive clavis". Two kinds of pair, both written by the period hand:
- (A) catalogue entries: symbol, a name spelt in cipher letters, and a clear name written above it (e.g. "Mylonius");
- (B) words in the cipher text below the grid that carry a legible clear word written above them.
Only pairs where I can read both the cipher spelling and the clear word go in. A pair goes in or out on legibility
alone, decided while transcribing the cipher, before any decryption.

## Order of work
1. `transcription/f0278_cipher_as_seen.tsv`: id, cipher as seen (glyph rules as PREREG.md: 2→z, 1/dotless i→i, W-like→W kept as W).
2. `transcription/f0278_gloss_as_seen.tsv`: id, clear word as seen (normalised as PREREG.md: lower case, umlauts dropped, v→u, j→i, spaces dropped).
3. Hash both into `results/frozen_inputs_0278.sha256`.
4. `scripts/check_0278.py`: decrypt with the frozen key `e638f434…` **unchanged** (letters not in the key → `?`).

## Score and threshold (same as the first test)
Pooled SequenceMatcher matched characters / clear characters; null = 200 shuffled keys (values permuted over the key's
cipher letters), seed 278. Pass if ≥ 0.85 and margin ≥ 0.30 over the best shuffle. One run; whatever it gives is recorded.
Also reported, labelled as descriptive and not the test: the same score with the two declared extensions from f. 6
(cipher x → m, W → p).

## Known weaknesses, stated now
- Not blind. I had already looked at this page, and decoded four or five of the names by eye (Mylonius, Lampadius,
  Secretarii, contribution) before writing this. The glyph readings may lean towards the key.
- The page is badly stained; the sample will be small (expect 10-25 pairs).
- Plain m and p letters are expected misses under the unchanged key, which lowers the score.
