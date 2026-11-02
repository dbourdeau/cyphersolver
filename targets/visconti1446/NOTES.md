# Filippo Maria Visconti to Francesco Sforza, cipher slips of Nov 1446 - Mar 1447 (BnF italien 1583, 1584)

Status: read in part, written up 29 Oct 2026 (docs/visconti1446.html), revised the same day after merging a parallel
session's work. Key matched from DECODE (R5323; a second copy is R1857 image 17): 15,033 of 16,637 cipher signs (90.4%)
over 19 slips. Sixteen slips have a decipherment of the time or a later copy (all of ital. 1584 next to the slips;
ital. 1583 ff. 110 and 136 in BnF ital. 1597); only ff. 130, 154 and 158 are deciphered with no clear text reached.
f. 15 (key R5324) is targets/visconti1447/.

**Correction, 29 Oct 2026.** The first write-up said nine slips had no clear text. Wrong for six: ital. 1584 f. 25 is
the contemporary decipherment of ff. 23/24, f. 73 a later copy of f. 72, f. 103 the contemporary decipherment of
f. 102 (taken here for a "parallel letter"); f. 38, f. 84 and f. 95 are contemporary decipherments of ff. 36/37, 83 and
94 too (only later copies had been noticed). ital. 1583 ff. 110 and 136 have 19th-c. copies in ital. 1597, made by
deciphering the slips. Found by the parallel session's survey (`peer/slips.tsv`), checked on the images.
The blind readings of ff. 23/24, 72, 102 agree with those clear texts on 83-88% of words (with spelling variants;
64-73% exact; `texts/compare_clear.py`, `texts/f25_clear.md`, `f73_clear.md`, `f103_clear.md`).

## State of the reading (29 Oct 2026; read share = read tokens / non-null tokens, as measured by the workers)

| slip | date | key | read | clear text filed with it | reading independent? |
|---|---|---|---|---|---|
| 1583 f. 110 | 1 Nov 1446 | R5323 | 89.1% (recto 96.5%, verso 69.6%; parallel session's pass 2) | ital. 1597 f. 123r-v, 19th-c. copy made by decipherment | no, aligned with the copy (blind pass G: 32%) |
| 1583 f. 130 | 25 Nov 1446 | R5323 | 88.2% (≈80% as sense) | f. 131 "Traduzione" (not reachable) | yes |
| 1583 f. 136 | 29 Nov 1446 | R5323 | 95.7% (parallel session's pass) | ital. 1597 f. 154, 19th-c. copy made by decipherment | no (blind pass A: 91.5% by sense, 68% of words match the copy) |
| 1583 f. 154 | 12 Dec 1446 | R5323 | 80.4% (≈70% as sense) | none reachable | yes |
| 1583 f. 158 | 31 Dec 1446 | R5323 | 89.4% | none reachable | yes |
| 1584 f. 5 | 10 Jan 1447 | R5323 | 96.5% | f. 6 Traduzione (contemporary): 96.5% agreement | check |
| 1584 f. 8 | 11 Jan 1447 | R5323 | 97.8% | f. 9 Traduzione (contemporary): 96.9% | check |
| 1584 f. 15 | 23 Jan 1447 | **R5324** | split out: `targets/visconti1447/` (one key, one entry) | | |
| 1584 f. 24 / f. 23 | 5 Feb / dup. 24 Feb | R5323 | 95.0% / 96.7% | f. 25 contemporary decipherment; f. 26 later copy | yes, checked after: 84.1% / 83.2% of words |
| 1584 f. 30 / f. 31 | 9 Feb / dup. 24 Feb | R5323 | 95.5% / 96.6% | f. 29 later copy (of f. 31) | no, read with copy in view |
| 1584 f. 36 / f. 37 | 12 Feb / dup. 25 Feb | R5323 | 98.4% / 98.8% | f. 38 contemporary decipherment; f. 35 later copy | no |
| 1584 f. 64 / f. 65 | 6 Mar / dup. same day | R5323 | 96.9% / 98.9% | f. 63 later copy | no |
| 1584 f. 72 | 7 Mar 1447 | R5323 | 86.1% (≈80% as sense) | f. 73 later copy | yes, checked after: 88.3% of words |
| 1584 f. 83 | 11 Mar 1447 | R5323 | sample 8%, 91.2% | f. 84 contemporary decipherment; ff. 82r-v, 85r later copy: 99.2% | sample deciphered first |
| 1584 f. 94 | 18 Mar 1447 | R5323 | sample 18%, 94.9% | f. 95 contemporary decipherment; f. 92 later copy: 98.5% | sample deciphered first |
| 1584 f. 102 | 23 Mar 1447 (dup.) | R5323 | 94.2% | f. 103 contemporary decipherment; f. 101 later copy | in part (f. 103 used as a guide in the retry): 87.5% of words |
| 1583 f. 145 | 1 Dec 1446 | ? | not reached (not on DECODE; ital. 1583 not digitised) | ital. 1597 canvas 160, 19th-c. copy | |
| 1583 f. 112 | 7 Nov 1446 | - | not a cipher (clear letter) | | |

## The documents

Twenty-one parchment slips wholly in cipher from the last months of Duke Filippo Maria Visconti (d. 13 Aug 1447) to
his son-in-law Count Francesco Sforza, in the Archivio Sforzesco codices taken to France in 1499-1500 (BnF italien
1583-1596; Mazzatinti, *Inventario delle carte dell'archivio sforzesco*, 1883/1887, which marks each "In cifre:
membran."). Images: Gallica, IIIF via `openapi.bnf.fr/iiif/image/v3/ark:/12148/<ark>/f<canvas>/...` (Gallica's own
viewer blocks scripts; the presentation manifest returns an error, the image API works).

| volume | folio | date (Mazzatinti) | canvas | decipherment filed |
|---|---|---|---|---|
| ital. 1583 (`btv1b10033686w`) | 110 | Milan 1 Nov 1446 | ? | - (DECODE R7902) |
| | 130 | Milan 25 Nov 1446 | ? | f. 131 "Traduzione" (DECODE R7904) |
| | 136 | Milan 29 Nov 1446 | ? | - (R7907) |
| | 145 | Milan 1 Dec 1446 | ? | - (not on DECODE) |
| | 154 | Milan 12 Dec 1446 | ? | - (R7914) |
| | 158 | Cusago 31 Dec 1446 | ? | - (R7915) |
| ital. 1584 (`btv1b100373864`) | 5 | Abbiategrasso 10 Jan 1447 | 9 | f. 6 "Traduzione" (same mount) |
| | 8 | Abbiategrasso 11 Jan 1447 | 11 | f. 9 "Traduzione" (same mount) |
| | 15 | Cusago 23 Jan 1447 | 17 | f. 16 clear letter of the same day on the same mount: decipherment? |
| | 23, 24 | Milan 5 Feb 1447 | 24 | - |
| | 30, 31 | Milan 9 Feb 1447 | 30 | - |
| | 36, 37 | Milan 12 Feb 1447 | 34 | - |
| | 64, 65 | 6 Mar 1447 | 62 | - |
| | 72 | Milan 7 Mar 1447 | 69 | - |
| | 83 | Milan 11 Mar 1447 | ? (c. 80-84) | - |
| | 94 | Milan 18 Mar 1447 | 91 | - |
| | 102 | Milan 23 Mar 1447 | 98 | f. 103 clear letter dated 23 Mar on the same mount: decipherment? |

**Clear copies in a neat later hand (prior decipherments?).** Mazzatinti lists f. 92 as "Lettera del Duca a Fr.
Sforza (Milano 18 marzo). Copia moderna: manca l'originale" — the cipher slip of that day is f. 94. Unlisted pages in
the same neat hand sit next to other slips: f. 29 (canvas 29, "Altra simile", Milan 9 Feb 1447 "duplicata die vigesimo
quarto", next to the 9 Feb slips ff. 30-31) and a two-page letter on canvases 80 and 82 dated Milan 11 Mar 1447 (the
slip f. 83 of 11 Mar is the cipher page on canvas 80 right; f. 84 on canvas 81 is a 15th-c. clear letter of the same
day). If these are clear texts of the slips, someone deciphered or copied them before this project: to establish for
each slip (prior-solution field). Also: ital. 1584 f. 78 (Iacopo, ducal notary, Milan 9 Mar 1447, in cipher) with
f. 79 "Traduzione" — a further pair, cipher system not yet checked.

**ital. 1583 images.** The ark `btv1b10033686w` given for ital. 1583 on the BnF record saved in targets/it1583 is a
1456 volume (folio headers "1456 Septembre ... Décembre"), and `btv1b10037385p` (computed predecessor of 1584's ark) is a
later copy volume. The six ital. 1583 slips are worked from the DECODE images (R7902-R7915, `img/decode/`); the
translation f. 131 and the slip f. 145 (not on DECODE) are not reached.

Found by the Oct 2026 Venice/Milan sweep (`research/venice_milan_print/`, row 0; `research/venice_milan_decode/`,
row 0). DECODE has the six ital. 1583 slips as Non-decrypted records with no names; ital. 1584 is not on DECODE.

## Key

`key.md`. ASMi Carteggio Sforzesco cart. 1597 no. 23 = DECODE **R5323**, an 18th-c. copy headed "Filippo Maria Duca di
Milano" (DECODE: key record, N/A, no names, dated 1450-1555). Found 28 Oct 2026 by re-fetching the 15th-c. keys of
cart. 1597 (R5301-R5340, `fetch_keys.py`) and reading the headings: nos. 23 and 24 carry the Duke's name; no. 23 fits.
Homophonic letters (up to six signs), a full vowel+consonant syllable table, 12 word signs, ~14 names, 12 nulls.
targets/it1583 had downloaded all 208 Sforza keys in Sept 2026 but was looking for a Maino/Amidani key and did not
try the Duke's on these slips.

Check: f. 8 line 1 deciphers sign for sign to the f. 9 translation ("Come altre volte ve habiamo avisato ne pare"),
including the syllable signs ab, am, av, is, at, ar and the e homophones ÷ ·‖· ⊢.

## Method / log

- 29 Oct 2026, worker F (subagent): **f. 130 (25 Nov 1446) 88.2%** of non-null tokens, re-transcribed (worker D's raw rows
  dropped left-margin signs): brief to "the Magnificent Messer Federico", Sforza's brief of 14 Nov brought by Perino da
  Cotignola, Cosimo de' Medici's goodwill, the Duke begs Sforza to come at once. **f. 158 (Cusago 31 Dec 1446) 89.4%**:
  Thomase "da [Roma]" (name sign N) sent to France for help after the rout of the Duke's men-at-arms, nothing from Savoy,
  the Dauphin willing; Asti offered to the Dauphin. gꝓ = qua; ꝯ° = d (never a name sign). `texts/key_additions_F.md`.

- 28-29 Oct 2026, worker A (subagent): f. 8 vs translation f. 9 96.9% token agreement (627/641 tokens read); f. 5 vs
  f. 6 96.5%; f. 15 is in the **second Duke key R5324** and matches the clear f. 16 (same mount) at 96.0%; f. 23 half
  read; f. 24 is a second encipherment of f. 23. Disagreements are almost all the translator normalising Lombard
  spellings. `texts/key_additions_A.md`.
- 29 Oct 2026, worker B (subagent): ff. 30/31, 36/37, 64/65 read 95.5-98.9% of non-null tokens. **Each pair is one
  letter sent twice** (the duplicate enciphers "duplicata die ..."), and **each pair has a full clear text in a later
  hand on the leaf before it** (ff. 29, 35r-v, 63, each with "Altra simile" and the duplicate date;
  `texts/clear_ff29_35_63.md`). Worker B found them before deciphering, so these six were read with the clear text in
  view: a check of those clear texts, not an independent decipherment. f. 29 was made from the duplicate f. 31 (only
  f. 31 has its wording). Name sign Á = Cosimo de' Medici (blank label in the key copy). `texts/key_additions_B.md`.
- 29 Oct 2026, worker C (subagent): all 1447 slips use R5323. **ff. 23/24 (5 Feb) read with no clear text**: 91.7% /
  89.4% of non-null tokens, f. 24 a fresh encipherment of f. 23 (the pair fixes alternative homophones). **f. 102 (23
  Mar) read 84.5%** with no decipherment: f. 103 on the same mount is a 15th-c. clear letter of the same day and matter
  in fuller wording (≈94% parallel), not its decipherment. f. 83 (11 Mar): neat-hand copy on ff. 82r-v, 85r follows the
  cipher word for word (sample 274 tokens, 99.2%); f. 94 (18 Mar): Mazzatinti's "copia moderna" f. 92 (pencil 93) is its
  text (sample 223 tokens, 98.5%) — his "manca l'originale" is wrong, the slip is the original. The neat copies (ff. 29,
  35, 63, 82/85, 92) are one 18th-c.-style italic hand. f. 72 not read beyond line 1. Unread closing group of 6-12
  signs after the title on ff. 5, 8, 23, 83, 94 (left out of the copies). `texts/key_additions_C.md`.
- 29 Oct 2026, worker D: ital. 1583 (DECODE). All five cipher slips (ff. 110, 130, 136, 154, 158) are in key
  **R5323**. f. 136 (29 Nov 1446) deciphered blind, 91.5% of non-null tokens given a value (`texts/f136.md`): Zohane
  del Maino sent with full powers; Sforza's men-at-arms in Cremona/Cremonese gone over to the enemy camp. f. 130
  read in part (date with the year in words, intitulatio, Cosimo named twice; body raw, `texts/f130.md`). ff. 110,
  154, 158 key-identified only; f. 112 (R7903) is a clear letter, not cipher (`texts/f110_158_154_status.md`).
  f. 110 P2 and f. 154 P1 are cipher versos (continuations). `texts/key_additions_D.md`.
- 29 Oct 2026, worker E (subagent): **f. 72 (7 Mar) read in part with no clear text**, 86.1% of non-null tokens
  (713 tokens; ~40 of the read tokens sit in words not yet identified): the Duke answers Sforza's briefs of the 18th and
  21st of Feb and Marcolino Barbavara's letter; on Sforza binding himself to the Pope/Church and the King of Aragon [?];
  Pietro da Pusterla sent to Ferrara; letters to Rome; Angelo Simonetta's message; date "Dato Mediolani septimo Marcii".
  Gaps re-read: f. 23 91.7% -> 96.7%, f. 24 89.4% -> 95.0%, f. 102 84.5% -> 94.2%. **f. 23 L15 = "duplicata die vigesimo
  quarto eiusdem"** (f. 23 is the 24 Feb duplicate, f. 24 the original); f. 102 also ends with a duplicate note. The
  closing groups after the title are padding (vowel homophones / alphabet runs), `texts/closing_groups.md`.
  `texts/key_additions_E.md`.
- So far every slip checked has a clear text filed with it (contemporary "Traduzione" ff. 6, 9; clear f. 16; later
  clear copies ff. 29, 35, 63, 92). What is new here is the key identification (R5323, R5324 on DECODE, unlabelled) and
  any slip with no clear text: being checked (ff. 23/24, 72, 83, 94, 102; ital. 1583).
- 29 Oct 2026, merge of the parallel session (Visconti-Sforza cipher letters 1446; its branch writeup-visconti1446,
  0148c6e1c, not pushed; files in `peer/`, see `peer/README.md`). Taken: its f. 110 pass 2 aligned with the ital. 1597
  copy (`texts/f110_transcription.tsv`, recto 96.5%, verso 69.6%), its f. 136 pass (95.7%), the copies
  `texts/*_copy1597.md`, the second key copy R1857 image 17 with its corrections (`peer/key.md`, `peer/working_key.md`),
  its survey `peer/slips.tsv`, the failed LM control `peer/lattice.py` (55.6% of ambiguous signs right on f. 136) and the
  print check (Osio III, 1872: none of the Duke's cipher letters). `texts/import_peer.py` converts its transcriptions.
  This folder's readings of ff. 130, 154, 158 stand (fuller than its). The survey overturned the "no clear text" claim
  for six slips (see the correction under Status); ff. 25, 73, 103 transcribed and compared by a subagent.
- 28 Oct 2026: target opened (Opus 5.5). Canvases mapped from thumbnails (`img/`, git-ignored). Key R5323 found and
  checked on f. 8/9 line 1.

## Remaining gaps
- f. 110 (1 Nov 1446): 292 of 2,689 non-null signs unread, 231 of them on the cramped verso where signs run together - blocker: illegible; binarized DECODE image, ital. 1583 not digitised (microfilm MF 16151); the 1597 copy gives the sense of the gaps
- f. 154 (12 Dec 1446): parts of 14 lines (19.6% of non-null signs) - blocker: illegible; same DECODE resolution, page bent; two baseline-tracked passes done
- ff. 130, 158: scattered stretches that give values but no words (11.8%, 10.6%) - blocker: illegible; DECODE images, no copy in ital. 1597; f. 131 (translation of f. 130) not digitised
- f. 72: the name signs < and est - blocker: open-codes; the key copy leaves both labels blank and the later copy f. 73 leaves < blank too; the rest of the text is in f. 73
- ital. 1583 f. 145 (1 Dec 1446) and the translation f. 131 - blocker: needs-physical-access; not on DECODE, ital. 1583 not digitised (BnF AeM record: microfilm MF 16151; btv1b10033686w is ital. 1587); a 19th-c. copy of f. 145 is ital. 1597 canvas 160

## Escalation
- [x] siblings: all 21 slips of the series mapped (ital. 1583, 1584); duplicates read side by side (ff. 23/24, 30/31, 36/37, 64/65)
- [x] clear-pages: decipherments ff. 6, 9, 25, 103 and copies ff. 29, 35, 63, 73, 82/85, 92 transcribed and compared; ff. 38, 84, 95 identified as decipherments; ital. 1597 canvases 116-182 and ital. 1598 checked for copies of the 1446 slips (ff. 110, 136, 145 found); f. 16 belongs to f. 15 (visconti1447)
- [x] known-keys: the 15th-c. keys of ASMi cart. 1597 (R5301-R5340) read by heading; R5323 fits, R5324 does not (it reads f. 15); R1857 image 17 is a second copy of R5323, images 11 and 19 do not fit
- [x] print: Mazzatinti 1883/1887; Osio, Documenti diplomatici III (1872); Tomokiyo's Cryptiana; web search: none prints the Duke's letters; Cerioni 1970 covers the later Sforza keys
- [x] key-rebuild: name signs (Cosimo, Marchese di Mantova, Dux Mediolani) and homophones added from use (texts/key_additions_A-H.md, peer/working_key.md); LM lattice decoder for the glyph classes the scans merge failed its control on f. 136 (peer/lattice.py)
- [x] retry: ff. 23, 24, 102 re-read (worker E, 84-92% -> 94-97%); f. 154 re-transcribed on traced baselines (72.8% -> 80.4%); f. 110 second recto pass and verso show-through removal (38.7% recto -> 39.2%; verso 0 -> 15.0%)

