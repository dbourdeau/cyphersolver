# donjuan1577: Don John of Austria to the ambassadors in Genoa, Namur, 6 and 7 August 1577 (catalogue 753, AGS Estado 1410,77 and 1410,135)

Status: already solved (contemporary decipherments found in the same legajo); key of the 1577 Genoa syllabary checked on a fresh pair.

## Documents

- **1410,135** (PARES 3578951, "Carta completamente cifrada", 1 p.): cipher copy. Its cipher heading reads "copia de carta del
  señor [don Juan] para los embaxadores de Genova del castillo de Namur a 7 de agosto 1577". The decipherment is **1410,110**
  (PARES 3577630, "Copia de carta de Juan de Austria a Juan de Idiáquez y Pedro de Mendoza ... sobre la toma de Charleroi",
  Namur, 7 Aug 1577). PARES does not link the two.
- **1410,77** (PARES 3576845, "Carta totalmente cifrada", 3 pp.): cipher copy of the letter of 6 Aug 1577. The decipherment is
  **1410,111** (PARES 3577649, "Copia de carta descifrada del Sr don Juan para los embaxadores de Genova ... del castillo de
  Namur a 6 de agosto 1577"): same first words ("Son tan varios los successos de por aca") and last words ("de lo que sucediere
  les avisare"). PARES does not link the two.
- So two of the eight items of catalogue row 753 are not open ciphertexts. Images: PARES (not copied here).

## System and key

The numerical syllabary of the Spanish embassy at Genoa in 1577 (see `targets/perez1578`, `targets/idiaquez1577`), in the hand
of the clerk who made the copies for Don John. `key_frozen.json` was adapted from the Genoa key (K5, validated on the pair
1410,78/79) on 1410,77 against 1410,111 only, and frozen (SHA-256 in `key_frozen.sha256`) before 1410,135 was transcribed.
`scripts/decode.py` applies it; `decryption_1410_135.txt` is its output.

## Held-out test (one measurement, 14 Nov 2026)

`transcription_1410_135.txt` (15 cipher lines, 247 units, two passes) was frozen (SHA-256 3558ee69...) before 1410,110 was
opened; `plaintext_1410_110.txt` was transcribed afterwards. `scripts/heldout.py`:

- frozen key: 80.2% of 106 words, 89.2% of 437 characters;
- 200 controls (100 permuted consonant values, 100 shuffled unit orders): at most 18.9% words, 47.8% characters;
- criterion written beforehand (characters >= 0.85 and >= best control + 0.30): met.

The misses come from the copy, not the key in general: 26 is *fi* in this hand (*firme*) but *v* in 1410,77; 14 (*gu*) is
written with a cross (*seguara*); a 10 with a caret where the sense needs *on*; and the cipher has three words the
decipherment leaves out ("las novedades **que cada dia** se ofrecen"). One limit: some ambiguous signs were settled by sense
while transcribing (before the decipherment was opened), so the test measures key and reader together.

## Content (from 1410,110)

Don John expects Charlemont, an important place on the French frontier, to fall to the States, which would be a great loss
because of the powder and artillery in it; he is negotiating to take it "por trato" within three days, and if that works he
will go there and wait for what comes, leaving a German garrison at Namur, unless those of Luxembourg force him elsewhere;
from one hour to the next nothing is certain.

## Not done

- 1410,77 was not re-transcribed at full quality; it is read from 1410,111.
- The other six items of row 753 (1381,143 and 180; 1418,47, 50, 81, 82) were not examined here.

Note: `key_frozen.json` and `transcription_1410_135.txt` are kept byte for byte as frozen (SHA-256 529dd45a...9db and
3558ee69...149), so their comment lines (`_doc`, `#` header) are in French.
