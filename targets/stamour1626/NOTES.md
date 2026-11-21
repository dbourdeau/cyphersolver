# stamour1626: the period cipher table Besançon BM Ms 1580, f. 239 and the letters of the Count of Saint-Amour to the Count of Cantecroy, 1626

Status: in progress (EXISTING: a period key and passages already deciphered at the time; our pre-registered test of the table on the letters FAILED). Next step: read the cipher passages of Ms Granvelle 62 against the table, the code numbers and the contemporary interlinear decipherments.

## Sources

- **Bibliothèque municipale de Besançon, Ms 1580, f. 239** (catalogue: "Traduction du chiffre pour les lettres du comte
  de Saint-Amour", undated). Scan sent free of charge by the library for research on 18 Nov 2026. **No image is
  included**: the library's consent is needed to publish its images, and its notices ask that any publication of
  unpublished documents be notified to it. Cite as "Bibliothèque municipale de Besançon, Ms 1580, f. 239".
- **Bibliothèque municipale de Besançon, Ms Granvelle 62, ff. 322-334**: letters of the Count of Saint-Amour to the
  Count of Cantecroy, "du camp", 12 Oct, 3 Nov, 20 Nov, 7 Dec and 18 Dec 1626, with ciphered passages. Online on the
  library's Mémoire Vive (views 373-390, cited here as img373-img390). No image included.

## The table (EXISTING)

A one-page cipher table headed "de Madrid 101" and "pour les lettres / Le Comte de St Amour": a monoalphabetic table
with a few homophones (`key.tsv`, `key_f239.json`): A 24, B □, C #, D ▽ (and T above), E 13 (and ⊖ above), F ♀,
G +, H · (dot), I/J 16 (and ‡ above), L =, M V, N Λ, O 15 (and △ above), P ∝, Q ω, R ϱ, S φ, T XX, U/V 14, X k; no
sign for Y or Z. A user's notes at the top left add a = 12 and e = 18 (and "puis 25"). Transcribed twice independently
(`transcription/f239_pass1.tsv`, `f239_pass2.tsv`): full agreement on the table; the only difference is a note at the
top right, not used. The letter values come from the sheet itself: nothing here is recovered by us.

**Small marks above letters, seen and not used.** At the top right of the sheet, the second pass
(`transcription/f239_pass2.tsv`) saw small marks written above a few letter signs: a small *x* above the *k*
(consistent with X = k), a *φ* above an *R* (in the table φ is the sign of S and R has a ρ-like sign, so this pairs φ
with R against the table), an *N* above the *Λ* (lambda without bar; consistent with N = Λ), a small *c* (or *t*)
above the *#* (consistent with C = #), and a *∝* above two strokes *═* (the signs of P and L; role unknown). The first
pass noted the same group (x/k, ϙ over R, ═, N/Λ, c/#); the two passes differ only on the sign above R (ϙ or φ). They are recorded as seen; none is used in `key.tsv`
or in the decode.

Which letters it serves is already in the library's title ("pour les lettres du comte de Saint-Amour"). What we add is
the match with a particular set of letters, Ms Granvelle 62 ff. 322-334, and the observation that their ciphered
passages also carry code numbers (22, 75, 99, 101 ...) that the table does not cover.

## The test on Ms Granvelle 62 (FAILED)

A test was pre-registered and hashed before the cipher passages were transcribed (`test_ms62/PREREG-MS62-K239.md`,
SHA-256 in `PREREG-MS62-K239.sha256`); the passages were then transcribed blind by a fresh agent that did not see the
table (`transcription/ms62_cipher_blind.tsv`, 474 signs, hashes in `ms62_SHA256.txt`), and the measuring script was
hashed before it was run (`test_ms62/measure.py`, `measure.sha256`). The single measure, the share of decoded letters
covered by an optimal segmentation into words of an early-modern French lexicon, gave **M = 0.710 against at most 0.685
for 200 shuffled-value controls (mean 0.605): FAILED** under the frozen criterion (M ≥ 0.85 and M ≥ max + 0.30)
(`test_ms62/MESURE-MS62.json`, `RESULTAT-MS62-K239.md`). The design was wrong for this material: 160 of the 474 signs are
code numbers or shapes off the table, so the decoded text falls into segments of one to four letters that any key
covers with two-letter words. The portion is now spent; this result is reported as a failure, not as a validation.
(The lexicon file used, 409 KB, is not included; its SHA-256 is in the pre-registration.)

## What the identification rests on instead

Agreement with decipherments already on the pages, observed after the measure and not counted as evidence by the
test: the mechanical decode (`decryption_ms62.txt`, made by `decode.py`) gives words such as *les raisons*, *servir*,
*plus de*, *paix*, *offert*, *artifice*, *mal*, *volonté*, *tirer*, *avec la pate*, *la commission de l'ambassade n'est*,
*faveur*, *grand*, *fille*, which coincide with the interlinear words of a period hand on img379-381 (*battront*,
*paix*, *offert*, *artifice*, *mal*, *volonte*, *de tyrer*, *du feu avec la pate du chat*;
`transcription/ms62_interlinear_period.tsv`) and with marginal notes of a later hand on img382 and img390 (*La Royne
est grosse*, *La commission de l'ambassade n'est*, *faueur en espagne*). So the table is the cipher of these letters,
and the passages are **EXISTING**: deciphered, at least in part, at the time and later. No new reading is claimed.

## Files

| file | content |
|---|---|
| `key.tsv`, `key_f239.json` (+ `.sha256`) | the period table, with the signs named as in the blind transcription |
| `transcription/f239_pass1.tsv`, `f239_pass2.tsv` | the two transcriptions of the table (French, as written) |
| `transcription/ms62_cipher_blind.tsv`, `ms62_notes.md`, `ms62_SHA256.txt` | blind transcription of the cipher passages of Ms Granvelle 62 (French notes, as written) |
| `transcription/ms62_interlinear_period.tsv` | the period interlinear and marginal decipherments, kept apart |
| `decode.py`, `decryption_ms62.txt` | mechanical decode with the table, passage by passage, no correction |
| `test_ms62/` | pre-registration, hashes, measuring script, result (FAILED) |

## Remaining gaps

- The code numbers (22, 75, 99, 101 ...) and the shapes off the table are not identified (blocker: open-codes).
- No reading of the passages has been made (blocker: open-codes). 160 of the 474 signs are code numbers or shapes that the
  table does not cover, and no list of these codes is known: the sheet carries none, and the period interlinear words gloss
  only some passages (img379-381). A reading now would fill a third of the signs by sense alone.

## Escalation
- [x] siblings: the five letters of Oct-Dec 1626 in Ms Granvelle 62 ff. 322-334 transcribed; other Saint-Amour letters (1624-1628) not searched for cipher
- [x] clear-pages: period interlinear words and later marginal notes transcribed apart
- [x] known-keys: the period table itself (Ms 1580 f. 239)
- [x] print: web search (CCFr records of the Saint-Amour letters, Granvelle cipher literature): no edition or decipherment found
- [n/a] key-rebuild: the key is the period table; the code numbers are left open
- [n/a] retry: the pre-registered portion is spent; a reading against the interlinear decipherments is the next step

## Method

Claude (Opus 5.5) agents for Brice Dudout, 18 Nov 2026. The table was asked for on 04 Nov 2026 as the probable key of
the Saint-Amour letters, which had been downloaded earlier from Mémoire Vive.
