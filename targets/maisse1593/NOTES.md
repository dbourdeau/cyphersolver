# Henri IV to Maisse (Venice), 8 February and 27 April 1593, in Maisse's Cipher (1592-1593) — BnF fr. 16093 ff. 406, 410

Status: read from the contemporary clear copies (Brienne 13); the cipher itself not deciphered on these leaves. Written up as docs/maisse1593.html.

Split on 14 Oct 2026 from `maisse1592` under the one-key rule (George Lasry, 14 Oct 2026): one entry per key. The old
entry (catalogue 17) joined four leaves of fr. 16093 that Tomokiyo assigns to two different ciphers. ff. 370 and 373
(November 1592) are in Maisse's Cipher (1592), a numerical cipher, which is a different cipher, with its own page
([`targets/maisse1592/`](../maisse1592/), docs/maisse1592.html). This folder keeps **ff. 406 and 410** in
**Maisse's Cipher (1592-1593)**, with their twins f. 404 (partial interlinear decipherment) and f. 412. The full
working record of the catalogue item (folio and canvas maps, the pièce-number route, the scripts) stays in
`../maisse1592/NOTES.md`; the fetch scripts (`fetch.py`, `fetchr.py`, `fetchb.py`) and the git-ignored images are there.
Tomokiyo's key image for this cipher is `src/henryiv_Maisse2.png` (moved here).

This entry was contributed (Arya Sanketbhai Patel, PR #7) as part of maisse1592.

## The leaves

| target | date on the original | pièce | Brienne 13 (NAF 6984) | canvas / page | confirmed by |
|---|---|---|---|---|---|
| **f. 406** (canvas 457) | Chartres, 8 Feb 1593 | 247 | fol. **171r** | 176 right | heading *"Coppie de lettre du Roy audict sieur de Maisse de Chartres le huictiesme febvrier 1593, receue le viii.e d'Avril"*; preamble identical |
| **f. 410** (canvas 461) | Mantes, 27 Apr 1593 | 251 | fol. **193v** | 199 left | heading *"Mante le vingt huictiesme Avril 1593, receue le vingt douxiesme May"* |

Twins: **f. 404** (canvas 455) is the same despatch of 8 Feb 1593 as f. 406, sent by the other route ("double voye"),
with a partial interlinear decipherment; Brienne 13 copies the letter once, at fol. 171r, under pièce 247. **f. 412**
is the duplicate of f. 410 (Tomokiyo). The four leaves of catalogue 17 are four despatches in two ciphers; f. 404 is
not one of the four (corrected 22 Sept 2026 in the maisse1592 notes).

## The cipher

Observed on f. 404 at native resolution: letter-shaped symbols (w, d, l, p, b, y, g, z, long-s and others) carry the
letters, two-digit figures carry the nomenclator; 27, 10, 26, 23, 19, 21, 22, 24 and 8 are the commonest figures on
f. 404. Tomokiyo's key, *"Maisse' Cipher 2 (BnF fr.16093, f.344 etc.)"* (`src/henryiv_Maisse2.png`), is homophonic and
carries word codes (*vous, ceulx, est, faict, de, des, fort, par, pour, que, qui, advis, ces, comme, bon, avec, et,
jay, les, luy, moy*). This is the key Henri IV calls "le double du chiffre que j'ay envoyé aud. de Brèves" in the clear
text of f. 404 itself, which is why Tomokiyo finds the same cipher in the Savary de Brèves correspondence of
1593-1596 and again between Brèves and Beaumont in 1602.

## What the letters say

- **f. 406 / f. 404** (8 Feb 1593, Chartres). The King has answered every despatch and docketed the dates so Maisse can
  tell what is lost; the Spanish insolence and the Pope; Pisany and Cardinal Gondi should not leave Rome; their going
  would be of importance, and their entry among those of the League could breed division.
- **f. 410** (27/28 Apr 1593, Mantes). Acknowledges Maisse's letters of 20 Feb, 7 and 23 Mar; the duc de Nevers held
  one courier in Champagne; warm assurance that Maisse's absence will cost him nothing in the King's favour; and that
  experience has proved Maisse's long-standing judgement of "les affaires de Rome" right.

## What is not done

The key is in hand but not applied: neither leaf is transcribed group by group, so nothing here verifies the cipher
on ff. 406/410. The text comes from the Brienne copies (and, for f. 406, the interlinear decipherment on f. 404).

## Log

- 2026-09-19: Brienne copies located through the pièce numbers (PR #7, as part of maisse1592); f. 406 = f. 404.
- 2026-10-14: split from `maisse1592`.

## Assumptions for George's review

- The outcome is "read from existing decipherment", class read, with `fraction_read` 1.0 carried from the parent entry
  as the share of content obtained from the clear copies; no token of the cipher was deciphered with Tomokiyo's key
  here. If the read bar should require a sign-level decipherment, this entry is "read in part" or "not applicable".
