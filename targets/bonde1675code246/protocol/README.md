# Protocol files (French originals, frozen)

Written and frozen by SHA-256 before each step, in this order (14 Nov 2026); `shasum -a 256 -c *.sha256` checks them.
They are kept as written, in French, so the hashes still hold.

1. `PREREG-CODE246.md`: before any transcription. Units, the held-out portion (113R lines 19-33), one test against 200
   shuffled keys, success only at 0.85 and best shuffled key + 0.30.
2. `PREREG-CODE246-ADDENDUM-1.md`: before any key. The gloss runs ahead of the cipher (about 2.2 letters per number),
   so the reference for the held-out lines becomes gloss G05-G20; thresholds unchanged.
3. `PREREG-CODE246-ADDENDUM-2.md`: before the Fable run. Fable's gloss reading becomes a reference only after a blind
   check (10% of sure letters, all doubtful ones; rejected above 10% disagreement); resubstitution must reach 0.85
   before any test.
4. `PROTOCOLE-VERIF.md`: before the draw of the blind-check items (seeds, options, arbitration).
5. `METHODE-CLE.md`: before the key was built (training data, alignment, majority vote).
6. `PREREG-CODE246-ADDENDUM-3.md`: before the third pass of the numbers (which positions, two blind readers and an
   arbiter, fixed abbreviation list, the scoring); thresholds unchanged.
7. `CONVENTIONS-TRANSCRIPTION.md`: how the hand writes its figures, and the TSV format.

`H-secret/H_final.tsv`, named in these files, is the frozen transcription of the held-out lines 113R L19-L33. It is
not in this folder: the test was never run, the lines were never decoded, and they are kept aside for a future test.
Only its gloss column (the ink gloss over those lines) was used, as the protocol allowed: `../gloss/113R_G19-G33_subagents.tsv`.
