# Halphen 1889 against the cipher: 9 Nov (f. 33) and 22 Nov (f. 46r)

Check of 14 Nov 2026 (Brice Dudout with Claude Opus 5.5). Source: E. Halphen (ed.), *Lettres inédites du roi
Henri IV à M. de Béthune, ambassadeur de France à Rome, du 18 octobre au 24 décembre 1601* (Paris, 1889),
HathiTrust `iau.31858014633857`, pp. 8–34, consulted by a person in a browser (the page needs a human check). The
edition is cited here, not reproduced: HathiTrust asks that its copy not be redistributed.

## What Halphen prints

Halphen prints each letter from the original in BN fr. 3484 ("Orig."), **as continuous clear text, with the ciphered
passages given in clear and not marked as cipher**:

| Halphen | date | BN 3484 | this target |
|---|---|---|---|
| pp. 8–15 | 9 Nov 1601 | f. 30 | item 6, ff. 30r–31v. NOTES' leaf map calls it **8 Nov**. Halphen prints its dating clause as *"le neuviesme jour de Novembre"*. Its six glossed passages are part of `corpus_v2.txt` |
| pp. 16–18 | 9 Nov 1601 | **f. 33** | item 7, the page entirely in cipher. **The whole ciphered passage is in print** (pp. 16–18), from *"le Roy d'Espagne a pris en sa protection le Duc de Modane…"* to *"…aux prudens avis des dicts Cardinaux."* |
| pp. 19–21 | 10 Nov 1601 | f. 34 | item 8 (already read from the minute f. 36) |
| pp. 22–32 | 18 Nov 1601 | f. 38 | (no cipher noted) |
| pp. 33–40 | 22 Nov 1601 | **f. 46** | item 12, the whole letter with its postscript (pp. 35–40 consulted after pp. 33–34) |

Where Halphen took the clear for passages that carry no decipherment on the leaf is not stated in the pages read. The
copy register Cinq cents de Colbert 346 (NOTES) is the likely source. The pre-registered measurement below shows that
the cipher agrees with his text.

## One measurement (pre-registered, frozen before any decoding against Halphen)

PREREG SHA-256 `2e3d17070c33e426b4a780e5558c54d8c2678a1bda41109ca4c3c5fb0a71516b`, script SHA-256
`ce5daf652d752248fcf81efd110ccc2b88d4ddf5c7b1bbdceb1648a61b65bcd6`.

* **Key:** frozen as `key.tsv` stood after the f. 53r pass (first listed value per symbol, word signs and figures as
  listed, no language model).
* **Portion:** f. 33, the whole 970-token run of `ct_f33_v2.txt`, transcription of Sept. 2026 unchanged. It did not
  build the key. Caveat: two `key.tsv` rows cite f. 33 as supporting evidence (ff = e, m, = ment).
* **Reference:** Halphen's text of the same passage, normalised (lower case, no accents, j→i, v→u, y→i), 1,460 letters.
* **Metric:** 1 − Levenshtein / max(length), against 200 keys whose letter and word values were shuffled
  (seed 20261114).

| | score |
|---|---|
| frozen key | **0.507** |
| best of 200 shuffled keys | 0.291 |
| mean of shuffled keys | 0.251 |

**Primary threshold (≥ 0.85 and ≥ best control + 0.30): not met.** This was expected, given the transcription ceiling
measured in September (oracle 71 % of letters). **Secondary threshold (key signal, ≥ best control + 0.15): met**
(+0.22). The key and transcription carry Halphen's text well above chance, so his print is the decipherment of this
leaf. f. 33 is now used up for any further measurement.

## Strict count, 9 Nov (f. 33), words of the printed clear against the cipher

Each of Halphen's 353 words is classed by the share of its letters that the frozen-key decode matches in an
edit-distance alignment:

| class | rule | words | share |
|---|---|---|---|
| sure (cipher confirms) | ≥ 75 % of letters matched | 130 | 0.368 |
| {probable} | 40–75 % | 105 | 0.297 |
| [restored from the print] | < 40 % | 118 | 0.334 |

Most of the [restored] words are short function words and the open code groups, which the frozen key decodes as
nothing. Read by sense, the letter is the printed text: the 9 Nov letter counts as **read from an existing decipherment
(printed edition)**, with the cipher independently supporting two thirds of its words.

## Code groups fixed by the print (alignment of clear frames and decoded runs)

| group | value | evidence |
|---|---|---|
| 12 | le Grand Duc (de Toscane) | f. 46r l. 2 *avec le Grand Duc de Toscane*; l. 9 *le dict Grand Duc vous a dit*; l. 15 |
| 20 | la Seigneurie de Venise | f. 46r l. 15 `20 x f, S 12` = *la seigneurie de Venise et le Grand Duc* |
| 28 | Espagne | f. 46r l. 11 *par la voye d'Espagne*; f. 33 l. 16 *qu'à l'Espagne* |
| 26 | France | f. 33 l. 16 *enclin à la France* |
| 27 | Italie | f. 33 l. 8 *des gens en Italie* |
| 44 | Prince(s) | f. 33 l. 5 *les Princes de la Mirande*; f. 46r l. 10 *du Prince de la Mirande* |
| 45 | Duc | f. 33 l. 4 *le Duc de Modane* |
| 70 | partant | f. 33 l. 11 *Partant vous en confererez* |
| 69, 67 | tous?, sans? | low |

Still open: 62, 3, 5, 8, 2, 9, 31, 80.

## Corrections to `reading_22nov.md` (clear text of f. 46r)

Halphen gives the clear of f. 46r, and the September transcription of it has errors. Some examples:

* l. 10: *"[et] par consequent"* should read *"et pareillement"*.
* l. 24: *"que 2 deux"* should read *"que je veux"*.
* l. 4: *"que de vous ay faict"* should read *"que des commandemens que j'ay faict"*.

`reading_22nov.md`'s clear text should be corrected against Halphen pp. 33–40 (not done here: the edition is not reproduced).

## 22 Nov 1601, ff. 46v–47v (Halphen pp. 34–40): the rest of the letter

Halphen pp. 35–40 print the rest of the 22 Nov letter, again with the ciphered passages in clear and unmarked. They
run from the end of f. 46r (*"…la ville d'Annonay, du Diocese du dict Archevesché…"*) to the postscript (*"j'ay avisé
de preferer l'Evesque de Clermont à l'archevesque de Vienne…"*). The ciphered runs carry the substance of the
letter: three French candidates for the cardinalate (the Bishop of Évreux, the old Archbishop of Vienne, the Bishop of
Clermont); the idea of binding Cardinal Aldobrandini to France by giving him the protection of French affairs, then
held by Joyeuse; the Pope's words about the King's protection of his family after his death; Cardinal San Giorgio
leaning towards Spain.

### Second measurement, on a fresh portion (pre-registered)

* **Key K':** the key of the f. 33 measurement plus the groups fixed since then from f. 33 and f. 46r ll. 2–18
  (12, 20, 26, 27, 28, 44, 45, 67, 69, 70). It was frozen before decoding: PREREG SHA-256
  `5ad234e51a69ccdcaae155b8d314ea24ef83beeb3a04c072ac0a326c728d5346`, script `3b538fb8…`, segmentation `5d08e293…`.
* **Portion:** 34 chunks, 1,062 tokens, from ff. 46v–47v and f. 46r l. 31. None of them built K'.
* **Segmentation:** each chunk's span of Halphen was set from the clear frames alone, before decoding. Four runs were
  excluded beforehand: two whose transcription is marked incomplete, and two whose frame is ambiguous.
* **Metric:** the same as for f. 33.

| | score |
|---|---|
| K' | **0.535** |
| best of 200 shuffled keys | 0.319 |
| mean | 0.276 |

**Default bar (≥ 0.85 and ≥ best + 0.30): not met. Key-signal bar (≥ best + 0.15): met (+0.22).** This is the same
picture as on f. 33, now on a portion that never built the key. (The script was run a second time by mistake, through
an import, with the seed fixed. It gave the same figures.)

### Strict count, 22 Nov

On the 371 printed words of the measured chunks, compared with the K' decode:

| class | words | share |
|---|---|---|
| sure (cipher confirms) | 136 | 0.367 |
| {probable} | 107 | 0.288 |
| [restored from the print] | 128 | 0.345 |

The other runs (f. 46r ll. 2–28 and the four excluded runs) have their text in Halphen as well.

## Target-level count

| letter | tokens | text | cipher support (sure + probable) |
|---|---|---|---|
| 10 Nov (f. 34) | ~750 | clear minute f. 36 | read (key built on it) |
| 9 Nov (f. 33) | 970 | Halphen pp. 16–18 | 235 / 353 words (0.67) |
| 22 Nov (ff. 46r–47v) | 1,879 | Halphen pp. 33–40 | 243 / 371 words on the fresh part (0.65) |

Every cipher token of the three letters now has a contemporary or printed clear: the target is **read, from an
existing decipherment** (Halphen 1889 for 9 and 22 Nov). On its own, the cipher supports about two thirds of the
words. That is below the 95 % bar, so without Halphen the 9 and 22 Nov letters would remain read in part.
