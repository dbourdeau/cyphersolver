# trezzo1464: Antonio da Trezzo's cipher slip of 8 Sept 1464 (BnF italien 1590, f. 392; catalogue 1320)

Status: in progress

Catalogue **1320**. BnF, italien 1590 (Archivio Sforzesco), f. 392: an enclosed slip from Antonio da Trezzo, Milanese
ambassador with King Ferrante, to Francesco Sforza (or Cicco Simonetta): clear "Signore.", 13 lines of sign cipher, clear
foot "dat(um) ut in l(itte)ris. 8 Sept. / Idem servus Antonius". The covering clear letter of the same day is f. 393
("1464. 8 7bris"). Gallica microfilm btv1b10037390v, view 393; images through openapi.bnf.fr IIIF (Gallica itself
answers 403 to scripts): `https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b10037390v/f<view>/full/max/0/default.jpg`.
No images are committed.

The catalogue brief pointed this work at `targets/sforza1597/`, which is a different target (the ASMi cart. 1597 key
sheets and letters); this folder is the one-target folder for catalogue 1320.

## Prior art (14 Nov 2026)

As in the catalogue vetting of 11 Nov 2026: no DECODE record for italien 1590 or Trezzo; nothing in Tomokiyo or Lasry;
*Dispacci sforzeschi da Napoli* has no volume for 1464 to mid-1465 in print. No folder, PR or issue in this repository
covers italien 1590. No printed decipherment of f. 392 is known.

## Key material in the volume

- **ff. 283r-284r**: a cipher letter of Trezzo, "ex felicibus castris regiis prope Penam die xvj July 1464", in the same
  sign system, with clear passages at its end ("alla quale me racomando. Jo so stato presente alla [cipher] come V. Ex.
  intendera da miss. Antonio Cicinello").
- **ff. 281r-282r**: its contemporary translation, headed in a later hand "1464 16 Juillet, traduction des chiffres",
  ending "... alaquale per debito mio ho voluto advisare del tucto, e alaquale me reco(mando). Io so stato presente alla
  deposicione ha facta el canc(elliere) de miss. [?] Caldora, come V. Ex. intenderà da d. Antonio Cicinello. Ex campo
  regio apud Pienaz die xvj ...". Both texts start and end together: the key can be rebuilt from this pair.
- **f. 285**: a 6-line Trezzo slip with a word-level interlinear gloss ("questa novella e stata cazata da Brochardo ...
  tagliato la testa ... suspicione"), loosely placed; not used.
- **DECODE**: one of the ASMi Sforzesco cart. 1597 key sheets R5329-R5344 is "Antonio da Trezzo" (targets/sforza1597);
  those sheets are 19th-century reconstructions of 1450s Naples ciphers. Record pages need a DECODE login; not tested.
  The user's DECODE search listed R5329, R5333, R5344 (one page each), without images.
- **Cerioni, La diplomazia sforzesca (1970)** prints a reconstructed Trezzo cipher table (catalogue vetting); not online,
  not opened.

## The system (as far as seen)

Continuous signs, no word division, about 1.7 clear letters per sign: some signs stand for a letter, many for a
syllable or common word (the aligner gives qa = et, t = che, h' = non, Lu = per, 4π = er, 4e = es, ar = en, 8 = al,
δπ = in, z = ad, hr = ell, L^a = sua, L^u = la S.V.). Vowel-like strokes are written after or above a base sign
(L^a, L^u, Lo; δa, δu, δo; 4e, 4o, 4a). Heavy dots, vertical strokes and the opening triangle are left out as marks.
The labels in the transcriptions describe shapes; one label can cover more than one sign of the key (the label `p`,
167 tokens, aligns with t, r and p alike), which is the main weakness of this pass.

## Files

| file | what it is |
|---|---|
| `c392.txt` | f. 392, 13 lines, 398 sign tokens, one pass (before any key) |
| `c283.txt`, `c284.txt` | the 16 July 1464 letter: f. 283r (40 lines), f. 283v (39), f. 284r (11, with clear passages); one pass |
| `c_full_aligned.txt` | 283r-284r.10 joined, to the clear "alla quale" (2,792 tokens): the cipher side of the alignment |
| `t281_full.txt` | ff. 281r-282r, the contemporary translation, expanded, to "del tucto" (4,677 letters); `t281_part.txt` lines 1-22 |
| `lines.py` | cuts a (deskewed) page into line strips |
| `align.py` | wraps the soft-EM aligner `targets/duben1764/fb.py` (unchanged) |
| `control.py` | synthetic syllabic-code controls of the same plaintext |
| `key_full_v1.json` | the aligner's key: up to 3 values per sign with expected counts |
| `refine.py` | chooses one value per sign for a text by it-cinquecento score plus the key prior |
| `decode392_keytop.txt`, `decode392_refined.txt`, `refine_choice_l3.json` | f. 392 decoded with the key's top values / refined (lambda 3) |

## Results (14 Nov 2026)

- Aligner on the whole 16 July letter (cipher 283r-284r against translation 281r-282r, both ends fixed): top-share
  **0.589** after 25 iterations. Controls, same plaintext in a synthetic 70-sign syllabic code at the same length:
  20 % misread signs 0.787, 40 % misread signs 0.611. The real alignment is at the 40 %-noise level: the key holds for
  the frequent signs and is unreliable for the rest.
- On part of the letter only (lines 1-26 against translation lines 1-22) the aligner fails (0.33): with one end loose
  it cannot recover even a 20 %-noise control (0.30). Recorded in WORKLOG.
- **f. 392 decoded with this key (not used to build it)**: fragments of Italian that fit the context, e.g. "...amente",
  "restitutione", "quali hanno effecto", "desiderio essere", "alcuno che", "la S.V.", "amici", "nella"; but no
  sentence holds. State: **decoded, not read**. Method: key recovered based on adjacent plaintext (the sibling letter of
  16 July 1464 and its contemporary translation in the same volume). No reading is claimed; no strict count is made.

## Remaining gaps

- f. 392 reads in fragments only - blocker: none outside; workable. The transcription labels lump shapes that the key
  distinguishes (`p`, `q`, `pz`, `o~`), so the key is noisy. Next pass: re-transcribe 283r-284r and 392 with a sign
  inventory drawn from the alignment (where one label aligns with two values, look at the shapes), re-run, re-decode.
- The DECODE Trezzo key sheet (one of R5329-R5344) is untested - blocker: needs a DECODE login (the user's).
- Cerioni 1970's Trezzo table is unopened - blocker: print, not online.
- The short cipher run on 284r.10-11 (translated "deposicione ha facta el cancelliere de miss. [?] Caldora") is not in
  the alignment - workable, minor.
- One reader, one pass for every transcription; nothing checked by a palaeographer or a second reader.

## Escalation

- [x] siblings: ff. 283r-284r with its contemporary translation 281r-282r used to rebuild the key; f. 285's gloss seen, too loose to use
- [x] clear-pages: f. 393 (the covering clear letter) is not a translation of the slip (catalogue vetting); f. 286 is a clear letter of 17 July
- [ ] known-keys: DECODE R5329-R5344 (Trezzo sheet) and Cerioni 1970 not tested (login / print)
- [x] print: no printed volume of the *Dispacci* for 1464 (vetting of 11 Nov 2026 and this session)
- [x] key-rebuild: soft-EM alignment of the whole sibling letter against its translation (key_full_v1.json)
- [ ] retry: re-transcription with finer sign distinctions, then re-alignment
