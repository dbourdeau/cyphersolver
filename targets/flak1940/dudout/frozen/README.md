# frozen/: the pre-registered test of the key on part 4 (11 Nov 2026)

These files are copied unchanged from the working folder; the French text of the protocol is the original.

| File | What it is |
|---|---|
| `PREREG-C02.md` | the protocol (French), written and hashed before part 4 was decrypted: the two keys, the one measurement, the controls and the pass criterion |
| `SHA256-PREREG.txt` | SHA-256 of the protocol, the scorer, the decryption helper, the decryption of parts 1, 2, 3 and 5, and the quadgram table, taken when the protocol was frozen |
| `measure_p4.py` | the scorer, run once (needs `dt.py` and the quadgram table `qg.bin`, not included: 1.8 MB, built from a Gutenberg German corpus by `../solver/mkqg.c`; its SHA-256 is in `SHA256-PREREG.txt`) |
| `dt.py` | the double-transposition helper used by the scorer |
| `dechiffre_P1235.txt` | the decryption of parts 1, 2, 3 and 5 with the frozen keys, as it stood before the test (first transcription) |
| `T863-867.txt` | the first transcription of the five parts (28 Oct 2026, codes N and R for two letter forms of hand 2), the one the scorer read; SHA-256 fbb80683c709cce5052e029c59f57244255837036de6a4ad286f52de83d512ff |
| `MESURE-P4.txt` | the output of the single run |

Summary of the protocol in English: the keys were found on parts 1 and 2 only and confirmed by parts 3 and 5; part 4
(frame 0866, 181 letters after the indicator group, SHA-256 of the string 7d0b9ed3...) was held out. One measurement:
decrypt part 4 with the frozen keys and score it (a) with German quadgrams, mean log10 per letter, and (b) as agreement
(1 minus edit distance over length) with the plaintext predicted from the teleprinter copy on frame 0862 (the Horb-Marbach
and Ichenheim-Hornberg lines, with the conventions of parts 1-3). Controls: 200 random key pairs of lengths 19 and 22
on the part-4 ciphertext, and the frozen keys on 200 random permutations of it (seed 20261111), 400 in all. Pass if
quadgrams >= best control + 0.5 and agreement >= 0.85 and agreement >= best control + 0.30.

Result (`MESURE-P4.txt`): quadgrams -4.993 per letter against -6.643 for the best of the 400 controls; agreement 0.989
against 0.227. Pass.

Declared deviation (in the protocol): on 11 Nov 2026, before the protocol was frozen, a command that inspected the NARA
OCR index printed the raw OCR of frame 0866 (about 110 characters of part 4). It was not analysed and played no part
in the key search, which used parts 1 and 2 only.

To re-run: put `qg.bin` (from `mkqg.c`) beside the scorer and the first transcription at `../../working/T863-867.txt`
relative to it, as in the working folder, then `python measure_p4.py`.
