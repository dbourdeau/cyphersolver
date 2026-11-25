# Sir Nicholas Throckmorton to the Regent Moray, Greenwich, 20 July 1569 (BL Add MS 33531 ff. 79–80; DECODE R8348) — NOTES

**Verdict: read at the time and calendared, but a water stain has faded half of the decipherment, so every cipher passage is read again here (`reading.md`, write-up `docs/throck1569.html`).** Catalogue entry 83 ("... (England) to
Lorde Regent of Scotlande, 26 Jul 1569") is resolved and removed. Checked in one session on 2026-09-21.

## Identification

- DECODE R8348 leaves the sender blank and dates the letter 26 July 1569. The letter itself ends "At Grenew. the
  20th of July 1569" (f. 80v, top) and is signed in cipher. The address on the dorse is "Lorde Regent of Scotlande".
  A later hand at the head of f. 79 has "ane Cipher lre from England in ye yeir 1569". So **26 July is a DECODE
  slip for 20 July.**
- Bain, *Calendar of Scottish Papers* ii (1900), no. 1103, p. 661 (archive.org
  `CalendarStatePapersMaryQueenOfScotsVol2`): "July 20. Throkmorton to Murray. Add. MSS. 33,531, fol. 79. His
  position is thoroughly understood here by Mr John Wood's narration, and by a letter sent from Lethington on the
  same matter absolutely and briefly. [Goes here into detail on matters, and ends] by strongly urging him to advise
  with and trust Lethington ... Greenwich. Signed (in cipher): N. Throkmorton. 3 pp. In cipher deciphered.
  Addressed: 'Lorde Regent of Scotlande.'" Same shelfmark, date, address and page count.
- Tomokiyo (cryptiana, `mary.htm`, "Throckmorton-Moray Cipher (1569)", "Sir Nicholas Throckmorton to the Regent,
  Greenwich, 20 July 1569, f.79r-80v") reconstructs the key; DECODE holds his key image as the record's DOC_ file
  (`DOC_8348_2024-Sep-18-20-55-18_48126.png`, uploaded 18 Sept 2024).

## The document

Four images (ff. 79r, 79v/80r, 80r, 80v), fetched with the shared DECODE cookie into the git-ignored
`targets/throck1569/img/` of the main checkout. English, partly in cipher: the letter alternates clear sentences and
cipher phrases. Every cipher line carries a contemporary interlinear decipherment in a Scots hand. A water stain
across the right half of ff. 79r and 80r has faded much of that gloss, but the cipher ink is dark and legible.

## The cipher

Letter-for-letter substitution of Latin-looking letters and a few invented signs, word division kept, a few
homophones, and single signs for persons (N = the Queen of Scots, L = your Lordship, and others unglossed). Tomokiyo's
key, checked on the page (plain → cipher): a q/ħ, b r/K, c B, d ε (t-shaped), e α/ε, f a, g б, h c, i ∂/4, l f,
m g, n ɧ (h-shaped), o 7/i, p k, r m, s n, t o, u p/Δ (w = pΔ or Δp), x y, y x.

Checks, all against surviving glosses: "qht" = *and*, "ocα" = *the*, "xipm" = *your*, "amαhtn" = *frends*,
"zhoαhεαε" = *intended*, "mαn7fΔαε" = *resolved*, "Bihεαmh4hб" = *concerning*, "mαnoqΔmqo47ɧ" = *restauration*,
"ħn" = *as*, "ε4nk7n4o47ɧ" = *disposition*, "qa7mαnq4ε" = *aforesaid*, "87hεαnεαhε" = *condescend*,
"б7iε 7kk7mo4ho4x aim αyαBpo47ɧ" = *good opportunitie for execution*, "ncipfε" = *should*, "fimε" = *lord*,
"f4εε4hбoih" = *Liddington* (Lethington).

## What the stained passages say

Read from the cipher where the gloss is faded, p. 1 (f. 79r): "What was intended and resolved here concerning
the Queen of Scots, [answer?] for her restauration, as for the disposition of her in marriage, your Lordship ...
thoroughly understand by Mr John Woodes narration. Since which time you did hear also by a letter sent from me to
the Lord of Liddington in [your absence?] of the same matter absolutely and breefly ... How your frendes which here
aforesaid were of a contrarie minde for the whole, were violently constrained, and by great necessitie urged to
condescend thereunto. So as now, my good Lord, the matter is not in state of deliberation but rather requires
expedite ... good opportunitie for execution. With further by all convenient meanes I doe wishe that you should
concurre with your frendes here who see so far into your case, and are so content for the same, as they desire
nothing so earnestly as your Lordship's pr[ocuring?] in that matter ..." The full reading of all four pages is in `reading.md`.

## Related

- [targets/moray/NOTES.md](../moray/NOTES.md): the unsolved Moray–Wood cipher of 1568 (Add MS 32091 f. 213), whose symbol
  set differs from this one.
- [targets/throckmorton/](../throckmorton/): Throckmorton's 1560–63 letters to Cecil and the Queen (Add MS 4136), a
  different cipher.

**23 Oct 2026, v6 spelling check (research/reading_audit/v6_spelling_files.txt; REREAD_BRIEF step 3-4: no modern spelling in a reading)**: reading.md was listed because its header mentions modernised spelling. It is a false hit: the reading keeps the cipher's and the clear text's own spelling and modernises only a cipher word whose spelling cannot be read from the figures. Nothing changed.

## 14 Nov 2026: full-texts audit, the missing transcription

R8348 was listed without a transcription of the cipher passages. In order: (1) the folder holds only
`reading.md` (the deciphered letter) and the few cipher words quoted above; (2) the DECODE record (public API and
record page) carries four images and Tomokiyo's key image, no transcription; cryptiana `mary.htm` has the key image
only; (3) the images could not be fetched: DECODE serves the images of this record only to a signed-in session (an anonymous request to `decrypt-custom/filesrv` returned the `forbidden.png` placeholder, 17,947 bytes; the 200 px thumbnails are public and useless for signs). No DECODE session is available in this checkout and the images an earlier session fetched were git-ignored and are gone. So `transcription_missing` is recorded. What unblocks it: the four
images through a DECODE account; the cipher is Latin-looking letters with a few signs, so it can be transcribed
and checked by decoding against `reading.md`. Nothing else changed.
