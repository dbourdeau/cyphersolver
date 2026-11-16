# Vetting, ajbeling (16 Nov 2026)

Run by Andrew Beling (GitHub ajbeling) with AI agents, from his own computer and network. One catalogue entry,
1637 (HStA Darmstadt D 4 Nr. 376/4). No person has checked any reading below. Before starting, open pull requests
were searched for 1637, Darmstadt and 376 (16 Nov 2026): only #653, on another file (D 4 Nr. 113/9).

The result is not new. WAINUT reported it on 3 Nov 2026 (`research/wainut_leads_2026-11-03/README.md`, "Catalogue
1637") from a survey of all 102 images: a key with no ciphertext, the letters in German cursive filmed upside down, the
table pointing to about 1697-98. The catalogue row still has the earlier `open` verdict and the date 1635. This folder
adds a vetting block in the form the project applies, a measured test, a second reader on a random sample, and a
two-pass transcription of the key. Our agents had not read WAINUT's note when they did this work.

## Lead

- **1637** HStA Darmstadt D 4 Nr. 376/4: `not_cipher` (a key with no ciphertext). The supposed "symbol script" letters
  are clear German Kurrent; images 100-101 are a separate key, not shown in use. The block supersedes the `open` block of
  2 Nov 2026.

Count: not_cipher 1.

## What the file holds (images 000-101)

Writers and dates outside the letters read at full size come from contact sheets and the finding aid, and are
approximate.

| Images | What | Language, date |
|---|---|---|
| 000 | file cover "Landgräfin Dorothea Charlotte ... 1685/99" | German |
| 001-038 | courtesy and family letters (Eleonore Erdmuthe Luise of Saxony, Ansbach 1689; Margrave Johann Friedrich of Brandenburg-Ansbach and others; Landgrave Georg from Venice 1688; de Voss from Paris 1685; Jakob Schröder's reports on Württemberg, 1698, images 022-027) | German, French; 1684-1704 |
| 039-059 | Landgravine Elisabeth Dorothea to Princess Dorothea Charlotte, signed "dienstwillige treue Base, Mutter und ... Dienerin, Elisabetha Dorothea L. z. Hessen"; about half photographed upside down (text inverted above an upright address panel), heavy show-through | German Kurrent, clear; Darmstadt 1687 |
| 060-066, 069-079, 082-084, 089-099 | courtesy letters, letters of Landgraves Georg and Heinrich (Lisbon, 1690s), a receipt of Ambroise (1696), Vernezobre and others | German, French; 1690s |
| 067-068, 080-081, 085-088 | further letters of Elisabeth Dorothea, same hand | German Kurrent, clear; Butzbach 1693-1698 |
| 100 | key page: reciprocal alphabet, number signs, worked examples | German; undated |
| 101 | cover-name table: 15 persons and 5 places of the Württemberg court | German; same hand as 100 |

## Evidence that no letter is in cipher

1. **Pre-set test on letter 040** (`1637/TEST_PLAN.md`, sha256 in `1637/TEST_PLAN.sha256`, written before any decode;
   output `1637/test_run_output.txt`, run once). Two transcriptions of the letter, turned the right way up.
   - Measure 1 (share of transcribed words that are German or French words, illegible words counted as misses):
     164 of 222 (0.739) and 174 of 224 (0.777), **below the mark of 0.80 set in the plan**. The shortfall is illegible
     words (show-through, cut margins: 53 and 47 holes), not non-words; of the legible words, 97% and 98% are words.
   - Measure 2 (is the key used?): 6 odd words flagged by either pass; 0 of 6 decode to words with the frozen key;
     200 shuffled keys give at most 0.167 (mean 0.003). No pseudonym or place code from the table occurs. As set in the
     plan: key not shown in use.
   - Caveat: the lead transcription (`1637/i040_pass1_agentA.txt`) was finished after the helper's transcription
     (`1637/i040_pass2_helper.txt`) had arrived, so it is not fully blind to the helper's two flags; the file says so.
2. **Screen of the other letters**: 34 images, both halves, for roman-letter groups, lone capitals or numbers used as
   names, and table pseudonyms. None found; the few odd items are a Kurrent abbreviation, a classical name in clear
   ("Caton") and reader's reordering digits over six words.
3. **Second sample, uninformed reader** (`1637/CORROBORATION_PLAN.md`, sha256 in `1637/CORROBORATION_PLAN.sha256`,
   written before the images were viewed; answers in `1637/corroboration_result.md`). Three images drawn with
   `random.Random(1637)` from 039-059, 067-068, 080-081, 085-088 without 040: 043, 050 and 086. One helper reader, told
   nothing about the file, the key or our finding, judged **3 of 3 alphabetic German Kurrent with no cipher or code**
   (dated by it Darmstadt 22 Feb? 1687, Darmstadt 31 January 1687, Butzbach 7 November 1698), with partial
   transcriptions of the opening lines.

The key's own worked examples are roman letter groups ("xoku" = gnad, "ckxqo" = Tagen); no letter in the file has
groups of that kind.

## The key (images 100-101)

A transcription of a key page whose use in any letter is not shown: `1637/key_transcription.md`, made from two
passes (`1637/key100_pass1_agentA.txt`, `1637/key_pass2_helper.txt`) reconciled in `1637/key_reconciliation.md` and
frozen as `1637/key_frozen.json` (sha256 98b68164b40337e23e6cd78cb391766e7fbda58d2061b169d39f6d0fe982a789).

- Reciprocal alphabet, 12 pairs: a-k m-l o-n r-p e-q b-s c-t d-u f-w g-x h-y i-z (22 cells agreed in both passes).
- Number signs: 1 f, 2 h, 3 p, 4 l, 5 n, 6 o, 7 s, 9 m, 10 fx, 20 hx; 8 doubtful (g or q).
- Name table: 15 persons, letter, number and first pseudonym agreed in both passes (45 of 45 cells), e.g. Regierender
  Herzog L 24 Lisander; Herzog F. Carl A 12 Apollo; Fürst v. Zollern H 30 Hector. 5 doubtful items: Denira/Derrira,
  Menkingen/Menzingen, Andrein/Andreä, Waldebug/Waldeburg (perhaps Waldenbuch), Cabada/Cadoda.
- Date: about 1697-98, inferred from the persons listed (a reigning duke and duchess beside Duke Friedrich Karl, who
  died in December 1698, and a dowager duchess); WAINUT reached the same inference. Not tested.

The key is also listed in `key_leads.json`.

## Proposed correction to catalogue 1637

Not applied here (contributors do not edit `catalogue.json`). The block in `vetting.json` closes the entry as
`not_cipher`; as with D 4 Nr. 141/2 (issue #207), the file would stay a key-only lead until a ciphertext turns up. If
the row is kept anywhere, the proposed fields are:

- `year`: 1697; `date`: "about 1697-98 (inferred from the persons in the name table); file 1685-1704"
- `title`: "Hessen-Darmstadt house archive: Württemberg court code (reciprocal alphabet and cover-name table), filed
  with letters to Princess Dorothea Charlotte"
- `correspondents`: "Landgravine Elisabeth Dorothea of Hessen-Darmstadt and others to Princess Dorothea Charlotte"
- `period`: "1651-1700"; `place`: "Darmstadt / Württemberg"
- `folio_note`: "Images 100-101: key and name table; the letters (images 001-099) are in clear"
- `status`: "Key and cover-name table only; no ciphertext in the file. The letters once taken for a symbol script are
  clear German Kurrent, many photographed upside down (WAINUT 3 Nov 2026; vetting 16 Nov 2026)."
- `why`: "A Württemberg court code of about 1697-98 whose letters have not been found."
- `verify`: "Look for letters in this code in the Württemberg correspondence of the Darmstadt house archive (D 4) or in
  the Hauptstaatsarchiv Stuttgart."
- `vetting`: the block in `vetting.json`.

## Routes

| Route | Result from this network |
|---|---|
| digitalisate-he.arcinsys.de (image server) | 102 requests, 6 s apart, all 200, 3500 px; no challenge |
| archivportal-d.de item record | one fetch; licence given as CC BY 4.0 |

No image is included here; the image numbers and the record link above locate everything.

## What is left

- No person has checked the transcriptions, the test or the dating.
- Letters written in this code would be in other Württemberg correspondence (Darmstadt D 4, or Stuttgart); not searched.
