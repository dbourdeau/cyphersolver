Status: in progress (R9660 ff. 141v-146v re-read sign by sign; 78.7% of tokens sure or probable by the 95% rule, up from 72.0%; still under the bar, R9660 stays decoded, not read). Next step: the ~100 unattested code groups (no-key-material) and the doubtful signs listed below.

# R9660 ff. 141v-146v: sign-by-sign re-read (Brice Dudout, 12 Nov 2026)

Work by Claude Opus 5.5 for Brice Dudout. It builds entirely on Daniel Bourdeau's b34 transcription and reading
(`../reading_r9660_b34.txt`), his sessa1524 key and his `measure_read.py`; the images are DECODE R9660 (not included,
not reproduced). Nothing here changes his files. This is the step his NOTES named for these pages: "a sign-by-sign
re-transcription at full size, as done for f. 141r in b34".

## What was done

1. **Image round.** The seven DECODE R9660 images (3408 x 2543) cut into line strips; every line of ff. 141v-143r
   checked against b34 (a), and on ff. 143v-146v every line with an Ɉ, a "ges" or a spelled run that does not form a
   word. The b34 (b) readings had been seen before the round, so the check is of the signs, not a blind reading.
   Not checked: 143v l16, 145v l11, 146r l8 (b34 kept).
2. **Frozen before decoding.** `r9660_141v-146v_transcription_reread.txt` (SHA-256
   `50f3ad94a14c97e768c8131f4bb56bd14f0171c5558f5e2fc14d6591740063de`), `r9660_changes.tsv` (`d39bb603...`),
   `r9660_doubtful_signs.tsv` (`5b7119cc...`) and `scripts/make_reread.py` (`5eec17cd...`), 12 Nov 2026 12:16, before
   any re-read line was decoded. `make_reread.py` builds the transcription from b34 (a) and asserts every old value.
3. **One pre-registered measure** (`PREREG_measure.md`, SHA-256 `8ba71fa1...`, frozen 12:18 with
   `scripts/measure_reread.py` and `scripts/align.py`).
4. **Reading**: the words the new signs change were re-read as patches on b34 (b) (`scripts/reading_patches.py`,
   each old text asserted) and counted with the 95% rule.

## Sign changes

| b34 | re-read | value | examples |
|---|---|---|---|
| ꝍ (part 1), one sign | ɞ, a 6 with a top bar | r | (as b34's r) |
| ꝍ (part 1), same name | ꝛo, a z-hook over o (part 2's ꝛo) | s | pensar, Pascua, empresa, suspende, les dio, suspicion, conservarlos |
| ꝺ (part 2 only) | ɞ | r | notation only: part 2's ꝺ is part 1's r sign |
| Ɉ (part 2), g, ꝑ | ꝗ, a flat-topped g with a flag | d | pudiera, pedir, sin duda, credito, auditor, podra, pidiendo, sucediere, despedir |
| Ɉ (part 2) | ꝺ, a looped open ∂ | u / v | Volterra, restitucion, vez, sigue, deve, escusa, motivos |
| 3, ⅄, Ɉ | ɔ, a reversed c with a stroke | q | asiento que, conquistar, quisto, ynquietud |
| ⅄, L | ∠ | ñ | compañia, engañados, dañaria, cuñado |
| ges (part 2) | qes | es | es justo, es estrecho, esperanças, a vezes, restitucion, estiman |
| ꝺ, 6 | 6 | e | cupiere, pertenece, sucediere |

Other single changes (Jep -> Jez, ter -> ler, sit -> sir, x 3 -> xir "cardenales", ...) are in `r9660_changes.tsv`.
The 25 doubtful signs, with 2-3 options each, are in `r9660_doubtful_signs.tsv`.

## Measure (pre-registered)

One fixed key for both transcriptions: code groups take b34's own most frequent value (`b34_align_table.json`, from
the (a)/(b) lines whose counts agree); the single signs take the values above. Statistic: per-character score of the
decoded portion (124 lines) on es-golden-age. Controls: 200 permuted letter keys, 200 within-line shuffles, seed 1523.

| run | re-read | b34 (a) | max of 400 controls | criteria |
|---|---|---|---|---|
| frozen script | -2.423 | -2.453 | -2.728 | both pass |
| quote bug fixed | -2.507 | -2.518 | -2.793 | both pass |

The frozen script tracked clear-text quotes across lines; in b34 a quote left open at a line end closes there, so
about half the portion was skipped. The fixed run (`scripts/measure_reread_fix.py --per-line-quotes`) is reported
beside the frozen one, not instead of it. The gain over b34 under one key is small: the measure says the re-read
is not worse and carries the Spanish; the gain is in the readings below. `measure_result.txt` has both runs.

## Reading, 95% rule

Sure + probable count as read; restored and unresolved are holes (`count95.txt`, word test of
`../../sessa1524/measure_read.py`). No letters were restored.

| | tokens | sure | probable | unresolved | read |
|---|---|---|---|---|---|
| re-read lines, b34 | 2509 | 1704 | 66 | 739 | 70.5% |
| re-read lines, this re-read | 2540 | 1859 | 172 | 509 | 80.0% |
| ff. 141v-146v, b34 | 3556 | 2479 | 82 | 995 | 72.0% |
| ff. 141v-146v, this re-read | 3587 | 2634 | 188 | 765 | 78.7% |

`docs/_check_reading.py --file` does not move: clean share 0.175 -> 0.167, hole rate 0.227 -> 0.226 (b34 (b) vs this
reading, ff. 141v-146v). The gained words are scattered; few sentences close, because an unattested group or a
spelled run still sits in most of them. By George Lasry's test R9660 is still decoded, not read.

Probable = a word that holds a value used from context in this letter only: x = r (resolve, restante, Volterra,
restitucion), ε / Є = i (hizieron, pidiendo), 9 = d (ynquietud), ɞ = c (Petru[cci]), xir = cardenal. These are not
added to the key. One word is worse than in b34: 142v l16 "por ve-r-u V.Md." becomes "por [bog]-r V.Md." (the sign
read as ꝺ is the f~ switch).

## Still open

- About 100 code groups with no attestation in a deciphered Sessa page (no-key-material); they make most of the 765
  unresolved tokens.
- The doubtful signs in `r9660_doubtful_signs.tsv`; 143v l16, 145v l11, 146r l8 not checked.
- Spelled runs still without sense, e.g. 141v l11 "con-e-i-g-h-o-n-es", 141v l20, 142r l14, 145r l7.

## Files

`r9660_141v-146v_transcription_reread.txt` (re-read (a) lines), `r9660_changes.tsv`, `r9660_doubtful_signs.tsv`,
`r9660_141v-146v_reading_reread.txt` (b34 (b) with the patches), `b34_lines.json` (b34 (a)/(b) for ff. 141v-146v,
`scripts/parse_b34.py`), `b34_align_table.json`, `PREREG_measure.md`, `measure_result.txt`, `count95.txt`, `scripts/`.
No image or crop is included.
