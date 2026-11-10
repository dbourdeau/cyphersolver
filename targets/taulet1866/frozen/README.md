# frozen/ - files hashed before the single held-out measurement (9 Nov 2026)

Byte-identical copies of the working files; check with `shasum -a 256 -c SHA256SUMS` from this folder.
PROTOCOLE.md and the comments of the scripts are in French (written before the test; not edited, so that the hashes hold).

- PROTOCOLE.md - protocol P01 (units, held-out set H = S33, frozen transcription and key, one measurement, criterion).
- transcription.txt - transcription of S01-S33 (the header mentions our image store; no image is included).
- KEY.tsv - key K_T built on S01-S32 only.
- measure.py - the measuring script (`python3 -I measure.py transcription.txt KEY.tsv ../../../lang/lexicons/es.json.gz --part H`).
- decode_T.py - plain decoder used for decryption.txt.
- MESURE.txt - output of the one measurement: car 0.981, best control 0.704, margin 0.277, "NON VALIDEE -> PARTIELLE".
