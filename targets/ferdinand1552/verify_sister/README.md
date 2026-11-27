# Blind check of the sister-letter transcription, 27 Nov 2026

Twelve lines of at least 18 signs drawn at random (seed 1332) from transcription_13oct/18oct/22oct.txt. Each was cut
from the scan, enlarged 2x, and given with sign_inventory.md (and the names of the added signs Nx, Mx, H6, Q1) to a
separate AI agent that saw no transcription, key, reading or decryption. Its answer is blind_answer.tsv (its ? marks
dropped); our labels are sample_ours.tsv.

- Signs: 258 of 273 agree in order (94.5%). Most differences are between nulls (Eo, m:, Eb, q:) or where it left a
  null out.
- Letters after key.tsv: 255 of 260 agree in order (98.1%). The four lines that differ:
  - 45v.8: ours litteris de-; blind limieris ie- (it split the numeral 12 into I: z).
  - 13v.23: blind adds cc, a faint 3 at the left edge that it took as part of the line.
  - 45v.14: ours regnicola; blind regnichla (* read as K).
  - 9v.9: ours sinistr-; blind sinidtr- (S read as d).
  In each case the blind reading is not Latin and ours is. No disagreement changes a word of the reading.
- The checker is an AI model, like the transcriber; no human palaeographer has checked these letters.
