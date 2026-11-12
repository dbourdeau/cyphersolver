# sanchez1522 — dudout/ (Brice Dudout, 12 Nov 2026)

Status: read in part (R9607, 14 May 1522: 1,121 of 1,555 words sure = 72.1 % by the README rule; 79.5 % in the contributor's count with 116 probable words resolved by sense on look-alike signs; 2 restored, 316 unresolved; the folder key validated on a held-out passage of R9632). Next step: second letter-by-letter pass on R9607's unresolved spelled runs, then R9633.

Daniel's Status line in `../NOTES.md` is untouched. Work by Claude Opus 5.5 for Brice Dudout, from DECODE images of
lot 1 (R9594, R9607, R9616, R9617, R9626, R9631, R9632, R9633, R9636, R9639, R9651). **No image is reproduced here**;
cite DECODE R… (<https://de-crypt.org/decrypt-web/RecordsView/9607> etc.). Originals: Real Academia de la Historia,
Colección Salazar y Castro.

## 1. Triage — `TRIAGE_lot1.md`
Cipher/clear/mixed, duplicates (R9616 = R9617; R9626 = R9627; DECODE's R9632 P2 = P3, one opening missing), prior art
(Tomokiyo's opening lines; CSP Spain 2). Only R9607 and R9633 are uncalendared; R9594 = CSP 396 has a surviving
contemporary decipherment (existing decipherment).

## 2. One pre-registered measure of the key — `protocol/`
- `protocol/PREREG.md` frozen by SHA-256 before any decoding (`protocol/SHA256SUMS`), with the held-out portion
  `protocol/HELDOUT_R9632_f200r_l07-25.txt` (R9632 f. 200r ll. 7-25, 386 tokens, transcribed blind; R9632 used for no
  key adjustment) and the scorer `protocol/measure.py`. The PREREG names its training text by a path in our working
  dossier: it is the Project Gutenberg *Don Quijote* (SHA-256 27f5064a…036429e); the file is kept verbatim so the hash holds.
- Measure: decode with `../key_codes.tsv` unchanged, mean 4-gram log-probability per character against 400 controls
  (200 permuted keys, 200 token shuffles). Thresholds set in advance: ≥ 300 characters, above every control, z ≥ 5.
- **Result: PASS** — 593 characters, S = −2.471 against controls mean −3.106 (sd 0.112), best control −2.766, z = 5.68
  (`protocol/MEASURE_OUTPUT.txt`). The decode reads "despues los de esta republica nos enbiaron a llamar al embaxador de
  Inglaterra … para respondernos a lo que postreramente les …", the matter of CSP 473. Daniel's key (Tomokiyo 2025 +
  Daniel's additions) is confirmed on a passage no one had used.

## 3. R9607 read in part — `R9607_signs.txt`, `R9607_reading.md`, `R9607_en.md`
Alonso Sánchez to Charles V, Venice, 14 May 1522 (Salazar 9/24 ff. 65r-67v), 146 cipher lines, uncalendared, no
decipherment imaged. Transcribed blind by sign shape and frozen (SHA-256 in `protocol/SHA256SUMS`), decoded with the key
unchanged (`scripts/declines.py`), read by sense. Content: Venice's armament after the French defeat in Lombardy
(galleys at Venice and in Candia; French soldiers come from Milan to Padua), the state of Cremona, Lautrec and Prospero
Colonna; Sánchez's demand that the Signoria declare itself released from its capitulation with France; reports of the
Turk's fleet from Corfu (letters of 5 April) and of the King of France coming in person; the Hungarian ambassador's
departure; the Signoria's minute of its answer, "esta bien conforme a aquello". Tomokiyo printed the first line; our
reading agrees with it.
Count per page in `R9607_reading.md`: 79.5 % (S + P, the contributor's count; 72.1 % sure only by the README rule), so **read in part**. Most unresolved words are spelled runs
mis-transcribed on look-alike signs; 63 code groups absent from the key are listed, none added to the key.

## Not done
The other ten lot-1 records are triaged, not read. No new key value is proposed.
