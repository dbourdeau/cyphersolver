# sanchez1522 — dudout/ (Brice Dudout, 12 Nov 2026)

Status: read in part (R9607, 14 May 1522: 79.9 % of 1,555 words after the frozen re-check of lot 2, was 79.5 %; R9610, 2 June 1522: 691 sure + 211 probable, 2 restored, 233 unresolved of 1,137 words = 79.3 %; the folder key validated on a held-out passage of R9632 and unchanged since). Next step: R9614, R9640 and R9647 (the longest letters left), and a second letter-by-letter pass on the label errors of R9607 and R9610.

Daniel's Status line in `../NOTES.md` is untouched. Work by Claude Opus 5.5 for Brice Dudout, from DECODE images of
lot 1 (R9594, R9607, R9616, R9617, R9626, R9631, R9632, R9633, R9636, R9639, R9651) and lot 2 (R9603, R9604, R9608-R9612, R9614, R9618, R9620, R9623, R9624, R9628, R9630, R9640, R9647, R9657). **No image is reproduced here**;
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
Count per page in `R9607_reading.md`: 79.5 % read (S + P), so **read in part**. Most unresolved words are spelled runs
mis-transcribed on look-alike signs; 63 code groups absent from the key are listed, none added to the key.

## 4. Lot 2 triage — `TRIAGE_lot2.md`
17 records: all Sánchez letters uncalendared and without imaged decipherment, except R9624, a third copy ("triplicada")
of the 7 Aug letter (R9626/R9627, CSP 462). R9628 is a copy of R9629. R9623 is dated in clear 7 [?] Aug, not 19 July,
and its last paragraph, which Tomokiyo gives as decrypted, is in clear in the letter. R9612 is mixed. R9657 is not
Sánchez but Lope Hurtado de Mendoza (another cipher). R9606, R9637, R9655 have no image online.

## 5. R9610 read in part — `R9610_signs.txt`, `R9610_decode.txt`, `R9610_reading.md`, `R9610_text_es.md`, `R9610_en.md`
`protocol/PREREG_lot2.md` was frozen before decoding: key unchanged, no value added, so **no new measure** (the R9632
held-out passage is spent and not reused); declared look-alikes; the R9607 re-check rule; the counting rule. R9610
(2 June 1522, 9/24 ff. 132r-134r, 130 cipher lines) was transcribed blind, frozen, decoded (`scripts/decode_lot2.py`)
and read by sense: 691 S + 211 P, 2 R, 233 I of 1,137 words = **79.3 %, read in part** (`scripts/count_reading.py`).
Of the unresolved, 96 words (marked †) read only if a sign label is corrected after decoding (my q for the l-sign, oo
for OO = g, Z for ∂ = d, P for the m-sign); with them 87.8 %, but they are not counted. Content: the 24,000 ducats for
Prospero Colonna through Venetian lands, safe-conducts, the King of France's letters from Lyon, Lautrec leaving for
France, Cremona, the Turk's ambassador and armament, the Turks before Knin. Tomokiyo's opening line agrees.

## 6. R9607 re-check — `R9607_recheck.md`, `R9607_recheck_output.txt`, `scripts/recheck_r9607.py`
By the frozen rule (PREREG_lot2 s. 3): 625 unresolved runs, 268 unique, 49 ambiguous, 308 without fit; 5 words accepted
(ahi, ayer, toma, tener, tenian). R9607: 79.5 % -> **79.9 %**, still read in part. Code proposals from both letters
(dud = vino, sod = govierno, lud = presente, cid = xxii) are listed with their contexts; none is added to the key.

## Not done
R9603, R9604, R9608, R9609, R9611, R9612, R9614, R9618, R9620, R9623, R9628, R9630, R9640, R9647 are triaged, not read;
so are the ten lot-1 records other than R9607. No new key value is applied.
