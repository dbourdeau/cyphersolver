# Louis XIII to Brûlart de Léon, ambassador in Venice, 1615 and 1617 — BnF fr. 18043 f. 83–84, fr. 18044 f. 109–110 (DECODE R2785, R2786) — NOTES

Split on 14 Oct 2026 from `louis1615` under the one-key rule (George Lasry, 14 Oct 2026). The old entry (catalogue
191) grouped these two letters with Louis XIII's letter of 1631 to Melchior de Sabran because DECODE lists all three
with Louis XIII as author. The Sabran letter is in another cipher, solved by George Lasry, with its own entry:
[`targets/sabran1631/`](../sabran1631/NOTES.md), page `sabran1631.html`. The old slug `louis1615` is a stub page
pointing to both.

**Outcome: read from existing decipherment.** Satoshi Tomokiyo reconstructed the key of the Brûlart de Léon cipher
(1615–18) and read both letters with it (DECODE records uploaded August 2021, status "Partially decrypted"); his
key is on cryptiana louisxiii.htm and attached to both records. Nothing about the text is added here and his key was not
re-applied. Session 2026-09-21; split and written up 2026-10-14.

## The letters

| record | shelfmark | date | route | DECODE status |
|---|---|---|---|---|
| R2785 | BnF fr. 18043 f. 83–84 | Poitiers?, 15 Sep 1615 | Louis XIII (countersigned Brûlart de Sillery) → Léon Brûlart, ambassador in Venice | Partially decrypted |
| R2786 | BnF fr. 18044 f. 109–110 | Paris, 25 Jul 1617 | same | Partially decrypted |

- DECODE lists 3 pages for each record; one image of each was fetched (`IMG_R2785_I17344_P1.jpg`,
  `IMG_R2786_I17348_P1.jpg`, git-ignored in the main checkout, `C:\Users\dbour\cypher\targets\louis1615\decode\`).
  The R2785 image is a text page: clear French with cipher runs, and most runs carry a decipherment written above
  them in what looks like a contemporary hand ("Marini", "retirer a Gennes", "domestiques", "aucun ombrage"). The writer is still
  held in the town by the illness of his eldest sister, which fits the court at Poitiers in September 1615. The R2786 image
  is the address leaf ("A Mons. de Leon conseiller en mon conseil d'Estat et mon ambass. a Venise").
- The DECODE files `DOC_2785_…png` and `DOC_2786_…png` are one image (same MD5): Tomokiyo's key table "Brulart de
  Leon's Cipher (1615-1618)". Alphabet of letter-like signs with two or three homophones for most letters; numbers
  with a virgule for words (2 amytie, 20 de, 97 pour …); numbers with an overbar for syllables and short words
  (5 pre, 7 que, 18 roi, 37 vous …); dotted vowels for princes (ö duc de Savoye, ä duc de Mantoue); a delete sign
  and a repeat sign.
- Residue, from Tomokiyo's notes on DECODE: R2785 "Some passages are not deciphered … They may be partially or totally
  nulls"; R2786 "Some symbols are not deciphered. At least some of them are insignificant (because of cancelling
  symbols)".
- The volumes hold many more letters to Brûlart de Léon partly in cipher, from Louis XIII, Marie de Médicis and
  Puysieux (fr. 18043, 1615–16; fr. 18044 ff. 20, 168, 184, 283, 315, 1617–18). Not opened here.

## Sources

- Tomokiyo, "French Ciphers during the Reign of Louis XIII", https://cryptiana.web.fc2.com/code/louisxiii.htm,
  "Brûlart de Léon" (the key). Copy in the main checkout's `targets/louis1615/` (git-ignored).
- DECODE R2785, R2786 (uploader Tomokiyo, Aug 2021): key file and notes on the undeciphered residue.

## What was done

1. 21 Sept 2026: fetched the two record views and one image of each with the shared DECODE cookie.
2. 21 Sept 2026: fetched louisxiii.htm; the key and the reading are Tomokiyo's. The entry was closed without applying
   the key.
3. 14 Oct 2026: split from louis1615; the R2785 image and the key file were looked at to describe the letter.

## Still open (here)

Tomokiyo's reading leaves some symbols undeciphered, probably nulls or cancelled signs (his notes). This project
made no transcription and did not apply his key, so it has no check of its own and no sign-level replay. The other
two pages of each record were not fetched.

## Escalation (record)

- [x] siblings: the other Brûlart de Léon letters in fr. 18043 / fr. 18044 identified from Tomokiyo; not opened
- [x] clear-pages: contemporary interlinear decipherment on the R2785 text page
- [x] known-keys: Tomokiyo's 1615–18 key is the key of these letters
- [x] print: louisxiii.htm checked
- [n/a] key-rebuild: the key exists (Tomokiyo); nothing rebuilt here
- [n/a] retry: no reading of our own to retry
