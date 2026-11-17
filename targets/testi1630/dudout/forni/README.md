# Forni cipher (Lettera F cc. 53, 54, 72): key from c. 54r, held-out test on c. 53r

Brice Dudout (dudout), 17 Nov 2026. WAINUT's target and readings are unchanged. WAINUT found that the Forni letters use a separate table, and their annealing on a rough copy of c. 53 failed (NOTES.md). This folder builds on that finding.

## What was done
1. **c. 54r** is Forni's reply (Florence, 25 July 1634). It has cipher in Forni's hand with clear words between the passages, and at the head of the page a clear text that renders the cipher. The cipher was transcribed twice from full-resolution IIIF crops: `transcription_c54r_pass1.txt` and `transcription_c54r_1634-07-25.txt` (pass 2). It was aligned with the clear (`alignment_c54r.txt`). This gives `key_forni.tsv`: a homophonic substitution of about 37 signs, Greek and Latin-like shapes. Two dots over a sign double the letter, and a caret does the same in 1636. One sign, the tau-like U, serves for both f and z. The key was frozen before c. 53 was opened (SHA-256 844b6343893db14505d86aa90027862dab75416d7fbd523199cd181ea12491fc).
2. **Preregistration** (`PREREG.md`, SHA in `PREREG.sha256`) was written before c. 53 was transcribed or decoded. The held-out portion is all the cipher of c. 53r. The thresholds were car ≥ 0.85 and car ≥ the best of 200 controls + 0.30.
3. **c. 53r** was transcribed twice, with the second pass made without the first. The passes were arbitrated on the image (`transcription_c53r_pass1.txt`, `_pass2.txt`, final `transcription_c53r_1634-07-22.txt`, 566 signs). The arbitration was:
   - pass 2 had used "T" for the tau-like sign, which was relabelled U after comparison with c. 54r;
   - one blotted sign was set to N1, which is unknown.
   The final text was frozen and then measured once with `measure.py`. The score is the share of decoded characters covered by words of the Testi letters as printed by Doglio (1967), against 200 random permutations of the key values.
4. **Result** (`MEASURE.txt`): car **0.884**, best control 0.422, margin **0.462**, so the key is **VALIDATED**. In-sample calibration on c. 54r gave 0.859 against 0.410. c. 53r is now burnt as test material.
5. **c. 72r** (1 Feb 1636) is a three-line cipher postscript with word gaps. It was decoded after the measure with the same key and reads at once.

## Readings (count by an independent blind AI reader given only the raw decryptions; Daniel's rule)
| Leaf | Date | Words | Read by sense | State |
|---|---|---|---|---|
| c. 53r | 22 Jul 1634 | 125 | 123 (98%) | read |
| c. 54r | 25 Jul 1634 | 130 | 128 (98%) | read; there is a period decipherment on the page, and this page is the training text |
| c. 72r | 1 Feb 1636 | 16 | 16 (100%) | read |

The content is the "Cioli business". Andrea Cioli, the Grand Duke of Tuscany's secretary of state, sounded Forni, the Modenese agent in Florence, on a matter not named. The duke tells Forni to say he has no instructions and to refer everything to Modena. Forni answers that he told no one. The 1636 postscript asks for a full report, sent in cipher.

## Not done
- c. 53v, c. 54v and c. 72v: no further cipher was seen at 25 %.
- Ottonelli c. 4 and cc. 5-6 (1642, 1647): digits, another system, not attempted.
- The person behind "Curegui/qurequi" (c. 54r) and the sign H at the end of c. 53r are not identified.

## Files
- `key_forni.tsv`, `alignment_c54r.txt`.
- `transcription_*`, `decryption_*`, `reading_*`, `translation_*`.
- `PREREG.md` / `PREREG.sha256`, `MEASURE.txt`.
- `measure.py`. The lexicon is built from the djvu.txt OCR of Doglio, *Lettere*, vols. 1-3, on archive.org (236/237/238TestiLettere…). The OCR is not included, and the path in the script is local.

The images (Biblioteca Estense, CC BY-NC-SA) were used for study only and are not included.
