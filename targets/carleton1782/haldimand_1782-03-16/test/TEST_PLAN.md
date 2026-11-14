# Test plan, written before running (13 Nov 2026)

Hypothesis: the "J. R." letter (PCC item 51 vol. 2 p. 227) is in the Haldimand-Clinton line-letter cipher:
number before the point = line of the Army List title page, number after = place of the letter in that
line counted from the left (letters only, & counts), no Q on the page so Q has a mark (here a circled dot).

Frozen inputs (sha256):
- key: `key/armylist_titlepage_1778.txt` 07e09b455f1ff4a43f95f268de16ea1ba15b519ee12497bb3a3d13bf837793c3
  (copied unchanged from the carleton1782 worktree; built from Haldimand's own key sheet, not from this letter)
- ciphertext: `transcription_reading.txt` 63b4021d1d0c9bd0687a7460f043e93a0549a76fb9986ecd4d03fcd95dcb0c8c
  (pass-1 transcription; one override: the box ".29 .14 .17 .9" in column 2 is taken as line 18, chosen from the
  crib "your" before the key file was opened; the test is also run without it)
- crib key: `key_work.json` eeb66761cd53edbc02791d31c33cb6f584758853e4679eb1e602d2e12a4e19fd
  (63 cell values solved from the clear words and word patterns alone, before the Army List file was opened)

Measures, for the real key and for each control:
1. agreement: share of the 63 crib-solved cells whose letter the key gives.
2. words: share of the 64 enciphered words (excluding the signature) whose full decode is a word in
   /usr/share/dict/words (lower case; words with a hole count as failures).

Controls (fixed before running):
- C1 line shift: line L read as line L+1 (29 wraps to 1).
- C2 place shift: place P read as P+1.
- C3 shuffle: letters of each line shuffled independently, 200 seeds (0-199); report mean and maximum.
- C4 the 1778 title page with lines reversed (line L read as line 30-L).

Pass if the real key scores agreement >= 0.9 and words >= 0.7 and every control's maximum is below half of each.
