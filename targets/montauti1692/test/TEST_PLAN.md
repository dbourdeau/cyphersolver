# Held-out test plan (written 13 Nov 2026, BEFORE any key was frozen). NOT RUN.

Planned test (as briefed): freeze a key built from interlined pairs, hold out one interlined passage not used in building,
require that at least 80% of its groups decode to the clerk's/recipient's reading, and compare with 200 keys made by
shuffling the plaintext values among the cipher groups (pass = real key above the 99th percentile of the shuffles and >= 80%).

Why it was not run: the only interlined crib found (Oversize Ms. Codex 531, not 536) is in a different cipher from the
bare passages in Codex 533 (and 534). Its groups are 1-3 digit numbers carrying superscript dots and circles; Codex 533 and
534 use run-on digits with a c- or w-shaped sign and no marks (see NOTES_montauti.md, "Two systems"). A 531 key, however
good, cannot read 533, so no key was frozen and the test would be empty. No sha256 exists because no key exists.

If the second system's key is found (Penn Ms. Coll. 180, Folder 114: "documents with diplomatic cipher codes, 1689 and
1694"), run the same test with the 534 bare passages as the held-out set only if some of them carry a decipherment;
otherwise test on unseen runs of 533 by a pre-stated readability measure (share of groups giving Italian words, judged
against 200 shuffled keys).

## Round 2 test (written 13 Nov 2026 after key_v1.json was frozen, BEFORE the held-out passage was read)

- Key: `systemB/key_v1.json`, sha256 8bedce853bb0d5d9d576117a6136c4024cb843e57302ef153ccff4c28686005f, built only from Codex 534 f. 14r.
- Held-out: the interlined System B groups of Codex 534 **f. 15r** (letter of 20 Nov 1690, a different letter, not used in building).
  The groups and the interlinear letters are transcribed into `systemB/heldout_534_f15r.tsv` first, then scored.
- Measure: among held-out groups that the key covers, the share whose key letter equals the interlinear letter.
  Also report coverage (the share of groups that the key covers).
- Pass: share >= 80% AND above the maximum of 200 shuffled keys (the same group set, with letter values randomly permuted among them).
- Second, softer check on Codex 533 (no decipherment there): decode the first-pass runs with key_v1, offset chosen per run,
  and report whether Italian words consistent with the surrounding clear text appear. Judged by eye; not a pass/fail test.

## Round 3 clean held-out test (written 14 Nov 2026 before transcription of the held-out passage)

- Key: `systemB/key_v2.json`, sha256 64783ab82d6e35fe68db16badd5a882ee80d66ab2686f3b1f1f4bd81375b8c20 (frozen; key v1 kept unchanged).
- Held-out: Codex 534 **f. 21r** (letter "Di Firenze 5 Xmbre 1690"), fully interlined in faint ink; not used for the key.
- Procedure: (1) transcribe the cipher groups from crops cut to the digit line only, interline excluded, and save as
  `systemB/heldout_21r_cipher.tsv` with its sha256 before any interline is looked at; (2) decode with key_v2;
  (3) only then read the interline letters from separate crops into `systemB/heldout_21r_interline.tsv`;
  (4) compare letter by letter over groups covered by the key.
- Pass: >= 80% agreement on covered groups and above the maximum of 200 shuffled keys (values permuted among groups).
- Groups not in key_v2 are reported as coverage loss, and their interline letters become new pairs for key v3.
