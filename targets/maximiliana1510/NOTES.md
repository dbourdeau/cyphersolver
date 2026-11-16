# Maximilian I's envoys in cipher, 1510-1512 (Unsolved Catalogue 495)

Status: in progress

HHStA Wien, RK Maximiliana: 24 reports catalogued as "Teilweise chiffriert" / "Chiffriert", plus three de Burgo
siblings noted as glossed (25-2-25, 25-2-27, 25-1-36). The AIS IDs, dates, places and extents are in `items.json`;
images from the AIS viewer (`fetch_ais.py`, git-ignored `img/`). Catalogue row in
`research/central_archives/candidates.json` (Oct 2026 HHStA sweep).

## What the documents are

| writer | items | place, date | system |
|---|---|---|---|
| Andrea de Burgo | 22-2-55, 22-3-5, 22-3-18, 23-5-17, 26-5-31, 27-1-5 (+ 25-1-36, 25-2-25, 25-2-27) | Blois, Grenoble, Valencia [Valence], Milan; Jun 1510-Apr 1512 | letter signs with word signs, vowels often dropped |
| Paulus de Laude (to de Burgo / Maximilian) | 26-3-50, 26-4-6, 26-4-9, 26-4-10, 26-4-15, 26-4-24, 26-4-25 | Blois, Jan-Feb 1512 | de Burgo's cipher |
| Veit von Fürst | 22-2-51, 22-2-56, 22-3-8, 22-3-42, 23-2-62, 23-3-6, 23-5-25 | Rome, Bologna; Jun 1510-Feb 1511 | single words in glyph letters inside clear Latin, plus sign-names |
| Mercurino Gattinara | 23-5-4, 23-5-47 | Seville, Feb 1511 | digit/symbol letters with dot separators, name signs |
| Giovanni Colla | 26-5-10 | Rome, 9 Mar 1512 | own letter-sign alphabet, fully ciphered |
| N.N. | 26-5-7 | Modena, 8 Mar 1512 | rounded signs plus number codes (370, 398) |

The catalogue row's date range "Jun 1510 - Mar 1516" is wrong: the items run 25 Jun 1510 to 2 Apr 1512.

## Main finding: read at the time

Every page was surveyed (`survey_batch1.md`, `survey_batch2.md`). Of about 2,100 cipher lines, nearly all carry a
contemporary decipherment written between the lines (word by word for Fürst and Gattinara, a running Latin line for
de Burgo, de Laude and Colla). There are no separate decipherment leaves. The catalogue premise ("no decipherment
noted"; only 25-2-25/25-2-27/25-1-36 glossed) is wrong: AIS simply does not record the glosses on the other items.
The two items described as fully ciphered (26-4-24, 26-5-10) are fully glossed too.

So the bulk of catalogue 495 is an existing decipherment. The open work is the residue the glossator skipped:

| piece | size | state |
|---|---|---|
| 26-4-9 img 04 (fol. 14), de Laude 5 Feb 1512, closing "Δ." paragraph | 195 signs, 6 lines | no gloss; in a water stain; read 17% firm (26% with uncertain words), fifth pass |
| 26-4-10 img 07 l. 29 | 16 signs | the gloss of l. 28 runs on into it: "sunt conformia suprascriptis" (read at the time) |
| 23-5-47 img 04 postscript ll. 4-5, Gattinara | 39 signs | l. 4 6/19 (ends "maiore [?]"), l. 5 1/20 (Maiestas) |
| 23-5-4 img 07 l. 17, three groups after "sit matrimonium" | 3 groups | "sit matrimonium principis Caroli [q̃ ?] Maiestat[-?]" (2/3) |
| Fürst's unglossed groups (22-2-51, 22-2-56, 22-3-8, 22-3-42, 23-3-6, 23-2-62) | 59 groups | 40 read firmly (18 are split-word halves of a glossed word, 17 had a gloss the survey missed), 13 in part, 6 open (`reading_veit.md`) |
| glosses lost to stains/holes (26-4-9, 26-4-10, 26-4-24, 26-4-25) | a few lines | not tried |

## Keys

- **De Burgo / de Laude** (`key_delaude.md`, `key_deburgo.md` in progress): one sign per letter with 2-3
  homophones for common letters, many dropped vowels (consonant skeletons), word signs `ro` = et,
  `g t 4 a ŧ o` = quod, `93` = Cesar / Maiestas Vestra, ⊞ = pro, `cc` (underlined) = Andreas de Burgo. De Laude
  uses de Burgo's cipher: every value checked agrees. Control on two held-out glossed lines: 31/37 letters (84%).
- **Fürst** (`key_veit.md`): substitution with glyphs, every letter that occurs has a value (all but h, k, y, z), homophones
  for u/v, s, q; words split across line ends with the gloss over one piece. Control: armata, presens, Nam, vendicare
  decipher letter for letter. 22-2-51 (25 Jun 1510) and 23-2-62 (Dec 1510) use other alphabets, only partly rebuilt.
- **Gattinara**: in progress.

## Prior art

Not printed that we found (web search 27 Oct 2026). Leads not yet checked: Andreas Zajic and Herbert Krammer
(Vienna) gave a talk on ciphers in Maximilian I's circle at the Wuppertal Geheimschriftenzoom, 24 Oct 2025; the
Regesta Imperii XIV (Wiesflecker) calendars Maximilian's correspondence and may summarise these reports from the
glosses; Penn Libraries (colenda 81431-p35718d9c) holds 1512 letters incl. 13 from de Burgo to Alberto Pio, "a few in code".

## Remaining gaps

- 26-4-9 img 04 "Δ." paragraph (195 signs, 17% firm) - blocker: open-codes; the five-sign group `ꝸ ꝑo f -u- ʒ` that opens D4 and D5 looks like a name/code word, and about 24 tokens (`ꝑo`, `-u-`, `⊐`, `ł`, `ψ`, `—2`, `bc`) have no glossed value yet. Still workable: unsearched glossed lines (25-2-27 ll. 5-12, 15; 22-3-18 img 08 ll. 19-21 and img 15; 25-2-25 img 08; 22-2-55 img 08; 22-3-5 img 04; the de Laude letters 26-4-10, 26-4-15, 26-4-24) may gloss them.
- 26-4-9 img 04 D0 and right half of D1 - blocker: illegible; water stain, crossed forms and hooks not separable on the AIS scan (needs a raking-light/UV image of fol. 14).
- 23-5-47 img 04 postscript ll. 4-5 (Gattinara) - blocker: open-codes; 11 signs with no glossed instance in the rows aligned so far; rows 23-5-4_07 y850-1000, _11 y1320-1840, _12 y1445-1550 and the 23-5-47 main text not yet aligned.
- 23-5-4 img 07 l. 17 `q̃` - blocker: open-codes; clear abbreviation or the Maiestas case group, unsettled.
- Fürst's 6 open groups (22-3-8 img 02 l. 18 `h/ d n ɏ`; 22-3-42 img 01 l. 20 cursive tail; 22-2-51 img 02 l. 18 `ɱ V`; 23-2-62 img 10 margin `θ - ꞇ 8`; 23-3-6 img 09 l. 21 `ꟿtra`; 23-3-6 img 02 `ʒ23 6`) - blocker: too-short; one to four signs each with no second occurrence, two of them in alphabets (25 Jun 1510, Dec 1510) not rebuilt; each sits beside a glossed clause. 13 further groups read in part (`reading_veit.md`).
- Glosses lost to stains/holes (26-4-9 imgs 01-02 lowest lines, 26-4-10 img 02 bottom 2 lines, 26-4-24 img 02 l. 1 right half and img 03 l. 1, 26-4-25 imgs 04, 06) - blocker: not-attempted; the cipher survives under most of them and can be read with the keys.

## Escalation

- [x] siblings: all 27 items in the series surveyed page by page (`survey_batch1.md`, `survey_batch2.md`); not on DECODE, so no DECODE siblings; de Laude shown to use de Burgo's cipher.
- [x] clear-pages: no separate decipherment leaves or clear copies in any item; the interlinear glosses are the decipherment and are the key source; 26-4-10 l. 29 turned out glossed via the run-on gloss of l. 28.
- [ ] known-keys: none in DECODE or print found; still to try: ask Andreas Zajic / Herbert Krammer (Vienna), who work on ciphers in Maximilian I's circle; Penn colenda 81431-p35718d9c (de Burgo to Alberto Pio, 1512, some in code).
- [ ] print: web searches (27 Oct) found no edition of these reports or their cipher; Regesta Imperii XIV printed volumes stop before 1510 and the online database was not searched; Tomokiyo has no Maximilian 1510 page found.
- [x] key-rebuild: de Burgo/de Laude table 43 rows (control 15/17 letters, 88%), Gattinara 31 signs (control 8/9 then 5/8), Fürst 15 signs; Latin LM used to rank consonant skeletons only.
- [ ] retry: unread groups retried after each pass (five passes on the Δ. paragraph); a retry after the remaining glossed lines are aligned is still to do.

## 14 Nov 2026 full-texts audit

The profile had no `outcome.texts`. The folder holds no full transcription of any report: the work so far is the page survey, the keys, and worksheets on the unglossed residue. What exists is now listed, each file standing as both transcription and decode because each holds the signs and their values side by side:

- de Burgo: `bt_alignment.md`, state `not prose` (alignment worksheet for the key);
- de Laude: `reading_delaude.md`, state `decoded, not read` (26-4-10 l. 29 read by alignment with the gloss; the closing paragraph of 26-4-9 not read);
- Fürst: `reading_veit.md`, state `not prose` (table of the 59 unglossed groups);
- Gattinara: `reading_gattinara.md`, state `decoded, not read`.

Not listed, and still documents without texts: **Colla (26-5-10)** and **the Modena letter (26-5-7)**. Neither has a line of signs or of gloss transcribed in the folder (the survey quotes a few gloss words only). They were not transcribed in this pass: both are graphic-sign ciphers in alphabets of their own with no sign inventory here (Colla about 66 lines, Modena about 14), and the AIS images were not fetched in this session.

The target is classed "read in part" by "read from existing decipherment" with `fraction_read` 0.99, an estimate from line counts: the text that is "read" is the contemporary interlinear gloss on the images, and none of it is transcribed here. That is stated in `outcome.notes`; it means the full-texts list cannot show the reading itself until the glosses are typed.
