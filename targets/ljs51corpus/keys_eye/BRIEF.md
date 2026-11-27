# LJS 51: by-eye key tables from the compiler's plaintext

Label every output: "by-eye key from the compiler's plaintext, not independently confirmed".
Project C:\Users\dbour\cypher (Windows, python 3.12 + PIL/numpy/cv2; PYTHONUTF8=1). Master TIFFs: output\ljs51\master\0084_NNNN.tif
(image = 6+2*(folio-1) for r, +1 for v). Chain records (the Arabic plaintext, cipher lines, by-eye sign counts):
targets\ljs51corpus\chains_*.jsonl. Crops go to output\ljs51\crops\eye_<chain_id>\ (git-ignored).
Do not edit segment.py, rekey.py, chains_*.jsonl, NOTES.md or any other file outside targets\ljs51corpus\keys_eye\.

Per chain:
1. Crop each cipher line from the master at full resolution (and 2x where signs are small). Read the signs right to left.
2. Label each distinct sign shape S1, S2 ... in order of first appearance, with a short drawing description and the crop path of a
   clear instance. Dividers (stem with three dots, or whatever this chain uses) are recorded as '|', not as signs.
3. Normalise the plaintext letters as the record gives them (alif forms -> ا, ة -> ه, ى -> ي; hamza kept; note lam-alif).
4. Alignment: assign signs to plaintext letters by position, word by word, using the dividers against plaintext word ends. Record the
   alignment itself as a list: [line, position in line, sign label, plaintext letter, word index]. Where a word has more or fewer signs
   than letters, record the mismatch (surplus sign / dropped letter) at the place you judge, and say why.
5. Key table: sign label -> letters seen with counts. Measures: signs total, letters total, aligned pairs, number of shapes, number of
   singleton shapes (seen once: cannot be checked), and consistency over REPEATED shapes only: share of repeated-shape occurrences that
   take that shape's majority letter; also the same at letter-skeleton level (ب ت ث ن ي / ج ح خ / د ذ / ر ز / س ش / ص ض / ط ظ / ع غ / ف ق).
   Also list letters written by two or more shapes (homophones / variants).
6. Red gloss chains: compare, sign by sign, your assigned letter with the red letter over the sign; report agreement count and every
   disagreement.
7. Verdict per chain: key consistent / partly consistent (say where it breaks) / inconsistent (plaintext or alignment likely wrong).
Write keys_eye\<chain_id>.json (fields: chain_id, label, signs, letters, shapes:[{label, description, crop}], alignment, key, measures,
red_check, verdict, notes) as each chain is finished, and append one summary row per chain to keys_eye\REPORT.md.
