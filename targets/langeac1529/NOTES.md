# Langeac, bishop of Avranches, Venice, to Montmorency, 14 January 1529 (BnF fr. 3083 no. 8; catalogue item 6, Avranches' cipher 1)

BnF fr. 3083 no. 8, ff. 20-21 (Gallica btv1b90601328, canvases 35-36; the cipher is on f. 21r, canvas 36). Read in the
session of 18 Sept 2026 under `targets/gramont1529/`.

**Split on 14 Oct 2026 from `gramont1529`** under the one-key rule (George Lasry): catalogue item 6 grouped four
letters to Montmorency in four different keys. This entry is the one letter in **"Avranches' cipher 1"**. The
others are different ciphers, each with its own page: Gramont 1529 (`gramont1529`), Gramont 1530 (`gramont1530`) and
the Mâcon letter of 1537, now with the cardinal's other letters in Mascon's cipher (`rome1536`). The Gallica tools
and the saved copies of GL.htm / francis.htm stay in `targets/gramont1529/`.

## Key and result

* Key: Lasry's "Avranches' cipher 1" (table dated 05/11/2023 on Tomokiyo's cryptiana GL.htm, copy
  `img/BnF_fr3083_f20.png`), equal to Tomokiyo's partial table from the sibling fr. 3005 f. 107
  (`img/francisAvranches1.png`). Simple substitution with a few homophones, LL and SS signs, an LE ligature and a
  macron for n. Lasry also decoded the letter in 2023, unpublished (his correction of 21 Sept 2026).
* `fr3083_no8_langeac.md`: **read in full apart from two short groups** (3-4 signs before *sans* in line 7, 2 signs
  before VNG in line 9). 442 plaintext letters are read in cipher against about 6 unread signs (counted
  14 Oct 2026 from the reading file; there is no alias file, so this is a plaintext-letter estimate).
* Saint-Pol asks Langeac to seek his leave (congé) from the Signoria; Venice refuses and protests it would ruin the
  enterprises (Milan, Spanish money arriving, spring coming); Langeac has written to dissuade him. January 1529,
  five months before Landriano. Year fixed by Saint-Pol's command and the clear news of Aquila retaken.
* Table refinements from the leaf: ɓ = P and I; long-tailed 9 = A and V; 8∞ = LE; macron over ∞ = en; the block
  opens with two nulls.

## 14 Nov 2026: the cipher lines transcribed sign by sign

The audit asked for a transcription of the cipher (none had been kept). Gallica image f36 fetched at full size
(openapi.bnf.fr IIIF) and the 11 lines read in line crops. Each sign is named by the cell of Lasry's table whose
drawing it matches (column letter, 1 or 2 for the upper or lower drawing): `texts/fr3083_no8_cipher_signs.txt`,
a single AI transcription, not checked by a person. 437 signs (counted by script; one struck sign in l. 6 left out).

Check: decoding the labels (A1, A2 = A, and so on) gives the text of `fr3083_no8_langeac.md` line for line. What the
signs show against that reading:

* l. 1 opens with two signs of Lasry's "Unknown" row (the large C and the A-shape) before MONSEIGNEVR; l. 9 opens with
  the same large C and a crossed c like SS (the "[E + crossed sign]" of the reading: the first is not an E).
* l. 1-2: RECH | ER SON, so the page has "recher son conge", not "rechercher".
* l. 2: the O of VOLV is a small 6-shaped sign, perhaps the fourth sign of Lasry's Unknown row (doubtful).
* ll. 4, 5: the N of EMPRINSES, EMPRINSE is a 7-shaped sign (the M shape) after a short dash, both times. l. 4 has
  RVIN DES EMPRINSES with no sign for the bracketed "[E]" or "[EN]" of the reading.
* l. 7: CROY ends in the y-shaped C sign. The three signs before the clear "sans" stay unidentified.
* l. 8: no clear S sign after TOV (two faint dots); the N of CONSENTEMENT is the ordinary N sign, not the b-shape
  (the "N?" of the key notes is not needed).
* l. 11: an extra T sign stands between TROP and DANGEREVSE.

None of these changes the sense. `fraction_read` recounted on signs: 428 of 437 = 0.979 (was 0.987 on letters).
The reading file itself was not edited.

## Remaining gaps
- a group of 3-4 signs before *sans* (line 7) and 2 signs before VNG (line 9) - blocker: too-short; isolated groups with no gloss or decipherment of the letter, and the context admits several words

## Escalation
- [x] siblings: the key's sibling fr. 3005 f. 107 (Tomokiyo) is the key source; no other letter in this key in the item
- [x] clear-pages: none; the clear text around the block (Aquila, the close) was read
- [x] known-keys: Lasry's Avranches' cipher 1 applied
- [x] print: Tomokiyo francis.htm, Lasry GL.htm: keys only, no plaintext
- [x] key-rebuild: table refined from the leaf (ɓ = P/I, 9 = A/V, 8∞ = LE)
- [n/a] retry: the two groups were re-read when the table was refined on 18 Sept 2026; not redone at the split

## Assumptions for George's review

- His prior-solution credit rests on his note of 21 Sept 2026 that he decoded all four item-6 letters in 2023.
- The key-or-decipherment credit here is for his "Avranches' cipher 1" table only.
