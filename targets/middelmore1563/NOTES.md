# Henry Middelmore to Secretary Cecil, 19 and 26 July 1563 (BL Add MS 4136 ff. 155-157, DECODE R9246, R9247) — NOTES

Status: no write-up

**Verdict: closed, already in print.** Session 2026-09-21. Both letters are printed in full, with the ciphered words
already deciphered, in Patrick Forbes, *A Full View of the Public Transactions in the Reign of Q. Elizabeth*, vol. II
(1741), from the Paper Office originals:

- Rouen, 19 July 1563: Forbes ii 470-75 ("Sir, repayrynge to the prince the xvi of this present…"). In the
  archive.org OCR used for smith1562 (`targets/smith1562/forbes2.txt`), lines c. 38345-38600.
- Vallemont, two leagues from Fécamp, Monday 26 July 1563: Forbes ii 490-92 ("Sir, yf the ample expressynge to youe
  of my grief and sorrows…"). OCR lines c. 39800-39960.

Nothing new is added here, so catalogue entry 91 is removed and there is no site page.

## The records

Add MS 4136 is Forbes's own deciphering file (see `targets/smith1562/NOTES.md`). He copied only the ciphered stretches of each
despatch and numbered them.

- R9246, 3 images = ff. 155-157. f.155 top: passages (16)-(22) of the end of a previous letter (a different cipher,
  with clear words "notwithstanding", "because", "apres"). f.155 foot to f.157 top: Middelmore, 19 July 1563,
  passages (1)-(46). f.157 middle: Middelmore, 26 July 1563, passages (1)-(26). f.157 foot: Sir Thomas Smith to the
  Queen, 17 Jan 1562/3 (read in smith1562, R9248).
- R9247, 1 image: byte-identical to R9246 image 3 (f.157). A duplicate record of the 26 July letter's page.
- DECODE says "Non-decrypted"; dates blank on the records; place "London" in the catalogue is wrong (Rouen and
  Vallemont, Normandy, during the siege of Newhaven/Le Havre).

## The cipher, checked against Forbes

A simple substitution of about 25 signs (digits 4-8 with dots and colons, λ, ω, ⊐, ⊏, ∓, ʜ, Ə …), words kept apart,
plus code signs. Middelmore did not use Smith's key (R9261). No key for it is on DECODE (key records R9260-R9262 are
Throckmorton, Smith/Croft, Throckmorton).

Spot-check on the 26 July letter:

- (1) and (6), identical, `∓λ ω4λ8⊏7` = "my grief" (Forbes: "of my grief", "those my grief"): ∓=m, λ=y/i, ω=g, 4=r,
  8=e, ⊏=f; the final 7 probably s ("griefs").
- (2) `7445407` = "sorrows" (7=s, 4 serving for o and r with different pointing).
- (4), (9), (22) `∞` = Newhaven (Forbes: "to Newhaven", "fyndynge Newhaven"); (12) ends "… o ∞".

The fit is consistent; the full key was not rebuilt, since the printed text gives every passage.

## DECODE corrections to queue

Status → Decrypted (reading in print, Forbes ii); dates 19 Jul 1563 (R9246 main letter) and 26 Jul 1563; place Rouen /
Vallemont; language English; R9247 duplicates R9246 image 3; f.155 top belongs to an earlier letter.

## 14 Nov 2026: full-texts audit, the missing transcription

The 19 July letter (R9246, 46 passages) was listed without a transcription. In order: (1) the
folder has only `transcription_26jul.txt`, seven passages of the 26 July letter; (2) the DECODE record (public API
and record page) carries three images, no transcription; (3) the images could not be fetched: DECODE serves the images of this record only to a signed-in session (an anonymous request to `decrypt-custom/filesrv` returned the `forbidden.png` placeholder, 17,947 bytes; the 200 px thumbnails are public and useless for signs). No DECODE session is available in this checkout and the images an earlier session fetched were git-ignored and are gone. So
`transcription_missing` is recorded on the 19 July entry. What unblocks it: the three images through a DECODE
account, then a transcription checked by decoding against `texts/R9246_19jul_forbes.txt`. Nothing else changed.
