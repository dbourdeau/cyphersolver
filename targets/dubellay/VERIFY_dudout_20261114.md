# dubellay: independent decoder of 16 June 1529; 22 Oct 1529 opening partly re-read on the Gallica leaves (Brice Dudout, Claude Opus 5.5, 14 Nov 2026)

## Decoder (16 June 1529, fr. 3078 p. 21)
`verify_dudout_20261114.py targets/dubellay` reads only `key_p21.tsv` and the sign part of each token in
`p21_signs.txt` (not the `=value` labels), then compares.
- 194 sign tokens; 191 give the value of their label; 3 are not in the key (line 7: ρ with a triangle foot, small x,
  the smudged sign).
- The decoded letters (216, u/v and b/f folded) all occur, in order, in `texts/16jun1529_decryption.md`. The
  decryption has letters that the signs do not carry: the v of *trouvez* (signs: *trouez*), the second l of *allée*
  (*alee*), *ue* after the que sign ⊑ (twice, a word sign), and *a le* at the end. These are normalisations of the
  edition, not errors of the key.

## Image check
Gallica IIIF (openapi.bnf.fr), public; crops kept outside the repository.
- fr. 3078 p. 21 (`btv1b9060311s`, f21), line 7: the smudged sign before *roy* is the open a cup (ɔ) under a blot. So
  the cipher has *ou sera*, and only *le* of Scheurer's *ou sera le Roy* is not enciphered (`ser[a le]` ->
  `sera [le]`). ρ-with-triangle, ȸ and the small x stay without value.
- fr. 3005 ff. 165v-166r (`btv1b90599952`, f260-f261), the 22 Oct 1529 opening, at full resolution, on the lines with
  unread stretches that carry `♀`, `ꝗ` or `‡◇` in `22oct1529_transcription.txt`. Three shapes must be kept apart:

| shape | value | where it was read here |
|---|---|---|
| cross with a slanted stroke at its foot | e | consentent (v24), de ses, enemys (v29), requeste (v25), vieillesse (v31), et (v27), en (w2) |
| closed q-head on a crossed stem (ꝗ) | t | saichant (v24), ont (v29), honteuse (v31), et madame (v27), avant (w1) |
| hooked stem, no closed head | s | passion (v27), vieillesse (v31) |

So the `ꝗ  t / s  conflicting` row of `22oct1529_corrections.tsv` is two signs, one value each.

Reading changes (all in f. 165v ll. 21-35 and f. 166r, the part that did not read):

| place | before | after (signs) |
|---|---|---|
| v24-v25 | saichant […] ne consentent de ces […] payne | saichant ne consentent de ceste reques[t]e suz payne: no sign stands between *saichant* and *ne*; v25 = t e r e q u e s e \| s u z (ʊ 8 j̈) \| p a i n e. The t of *requeste* is not written (as in *remons[t]rer*, v20). *suz payne de* = on pain of |
| v29-v30 | la fureur des [?ennemys] qui luy ont […] si tranportes | la fureur de ses enemys qui luy ont ainsi tranportes: d e s e s e n e m y s; after *luy*: 3 ◇+ ꝗ ᴗ —o ◇+ = ont ain, + *si* on v30 |
| w1 | si avant […] des deux | si avant des deux: the two signs after *ava* are its n and t |
| w2 | vous [?en] | vous en (slanted cross = e, ◇+ = n) |

Files: `texts/22oct1529_reading.md`, `_en.md`, `_transcription.txt`, `_corrections.tsv` (dated notes added).
Still open on these lines: v30 *ont mais* + r e ◇+? e ꝗ —o ⊡ e (*renetire*?), w2 *ce que* + 4 signs.

## Read bar (README)
- 16 June: `v10_relabel.measure` 0.989 = recorded. Unchanged.
- 22 Oct: the entry has no `reading` field, so `v10_relabel.measure` scores `ref/legrand3_p330_400.txt` (1.0, 15,048
  words): an artefact. On `texts/22oct1529_reading.md` `share` gives 0.913 (471 words, 45 holes) before and **0.922**
  (475, 40) after this pass. Below 0.95: the text stays *decoded, not read*; class unchanged.

Key correction: none to `key_p21.tsv`. The ꝗ row of `22oct1529_corrections.tsv` is split as above.

## Not done
f. 165r and f. 165v ll. 1-23 not re-read; ꝑ, ℋ, ꝏ and # not settled; Scheurer t. I not seen beyond snippets.
