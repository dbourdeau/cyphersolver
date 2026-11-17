# Vetting wave 20, batch 06 (16 Nov 2026)

Proposals only. `proposals.json` is built by `add.py` from `p/<id>.json`, and every vetting block passes
`_check_catalogue.vetting_problems` on shape. `research/leads.json` and `catalogue.json` were not touched. Nothing was promoted
or committed. Tomokiyo `unsolved.htm` and Lasry `GL.htm` were fetched on 15 Nov 2026 (scratchpad copies). Tomokiyo's
`nevers.htm` was fetched today into `src/`.

| id | verdict | conf. | deciding fact |
|---|---|---|---|
| 2730 | open | medium | BnF notices: fr. 3329 nos. 78, 81, 82, 107, fr. 3409 no. 49 and fr. 4717 no. 49 are "avec chiffre" with no decipherment. Keys are in the volumes (fr. 3329 nos. 1-2, fr. 4717 no. 11). Several senders are mixed, so split by key. |
| 2749 | open | low | NAF 22330 ff. 107-112, "Lettres, en chiffres" to Breiffenstein/Riedet at Delft. Undated: the item sits between a 1585 deed and a 1631 warrant in an 18th-c. miscellany. |
| 2727 | open | low | fr. 3375 (not 3374), 4697, 4691: Guazzo's letter and notes are "avec chiffre" with no decipherment. Nevers's own pieces are minutes or copies marked "Chiffre", which may be clear drafts. Three keys mixed. |
| 2728 | open | medium | fr. 3422 nos. 27, 60, 62, 68, 69, 70 are "Lettre, avec chiffre" to Nevers, Apr-June 1589. Sibling fr. 3614 no. 60 (Tours, 1 June 1589) has a decipherment. |
| 2725 | key_lookup | high | The volume is fr. 3641, not 3057. Every piece is read (mendoza1589; decipherments nos. 4, 29, 44; Satoru nos. 50, 58) or already on CATALOGUE.md's key-lookup row (nos. 27, 48, former cat. 319). |
| 2729 | open | medium | Rescoped: fr. 3625 no. 55 is lauriere1593 (read), so dropped. Left: Marchant fr. 3624 nos. 47, 51, 67; fr. 3614 nos. 58, 61; fr. 3634 nos. 4, 45, 60, 80; fr. 3646 nos. 55, 67. Split by key. |
| 2736 | partly_read | medium | fr. 3575 f. 56r (catalogued as a key, "Chiffre") is ciphertext deciphered by Lasry (GL.htm, 99%). f. 43r (Ventadour, Pezenas, June 1598, viewed) has two short bare runs. fr. 3586 no. 57 is not online. |
| 2743 | read | high | Berger de Xivrey, Lettres missives V p. 746: original Ms. 8956 fol. 8 (= fr. 3457 no. 2), a copy in Ms. 8957 f. 20, printed in Amelot's Lettres d'Ossat V suppl. p. 39. |
| 2748 | none | - | NAF 3145-3146 bis: the notice names key sheets only ("differents chiffres" at the end of vol. II). Not digitised. Breval's DECODE R7952 (Lorraine 377) is solved. |
| 2737 | open | medium | fr. 3659 no. 24 (not 3638): Monteleon to Pedro de Toledo, 18 Oct 1617, copy, "avec chiffre"; neighbours in the volume are marked "et dechiffrement". |
| 2740 | open | medium | fr. 3796 no. 38: Louis XIII to Nevers, 28 Dec 1618, "avec chiffre", no decipherment. |
| 2738 | read | low | fr. 3693 (not 3689), Blainville embassy register, 1625 (not 1623). "Advis en chiffre" headings in a fair-copy register, most likely clear copies, as in fr. 4137 f. 128v. Not seen. |
| 2739 | partly_read | high | fr. 3758 nos. 100, 104 = louis1635/chatillon1635 (Lasry). fr. 3854 nos. 41-42 = conti1649 (Lasry). fr. 3837 no. 18 has its decipherment as no. 19. Only fr. 3837 no. 15 is left (key no. 3 in the volume): re-file it alone. |
| 2741 | read | high | Viewed fr. 4137 f. 128v-129r: "Memoyre ... envoye en chiffre" is a clear French register copy. |
| 2915 | partly_read | high | The source is fr. 23202 f. 23 (viewed). f. 23r is interlined over nearly every group, f. 23v partly. Chéruel's "sans traduction" is misleading. |
| 2745 | partly_read | medium | fr. 23202 letters mostly carry contemporary interlinear decipherments; key copy at ff. 1-2; DECODE R7894-7 solved. The bare runs are a key application. |
| 2747 | none | - | fr. 23227-23228: the notice names keys at ff. 1-6, not ciphered letters. Not digitised; needs a sample view. |
| 2751 | key_lookup | medium | NAF 4543 f. 180: Audibert's 1746 proposal for a music-notation cipher, a system filed with its explanation, not a correspondence. |

## Routes and notes
- BnF Archives et manuscrits notices by curl: `am.py` (saved under `am/`, git-ignored). None of the volumes here has a
  Gallica link except fr. 3575, 3641, 3758, 3854, 4137 and 23202.
- Gallica images: `gimg.py` (openapi.bnf.fr IIIF). fr. 3575: recto ≈ canvas 2f+3. fr. 4137 is photographed as openings,
  so canvas ≈ f+4. fr. 23202: recto ≈ 2f-5.
- Berger de Xivrey's "table de plusieurs lettres non imprimees" gives the old Bethune numbers (Ms. 8956 = Anc. 8956 = fr. 3457).
  It is a quick way to find printed texts of royal letters in the Omont-derived leads.
- Fair-copy registers ("Livre des lettres", "Ambassade de ...") with headings "envoye en chiffre" or "Advis en chiffre" hold
  clear text (fr. 4137 f. 128v seen). Treat such Omont rows as read unless a leaf shows figures.
- PARES was not used.

## Record errors found
- 2730: fr. 3329 nos. 81-82 are ff. 164-165, not 104-105, and no. 107 is missing. The governor of Peronne in 1577-78 was
  Jacques d'Humieres, not "Jean".
- 2725: the Gallica link and shelfmark are fr. 3057; the volume is fr. 3641 (btv1b52508089f).
- 2728: the end date is 27 June (no. 70), not 18 June.
- 2736: fr. 3575 no. 36 "Chiffre" is a ciphertext (deciphered by Lasry), not a key.
- 2738: the year is 1625 and the setting is England.
- 2739: the Chatillon letter is 1635, not 1633; fr. 3837 no. 18 has a decipherment (no. 19).
- 2915: the shelfmark is fr. 23202 f. 23. The leaf has an interlinear decipherment despite the edition's "sans traduction".
