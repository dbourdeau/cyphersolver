# Andrea da Birago → Francesco Sforza, Pavia, 28 February 1448 (BnF italien 1585 f. 33)

Status: written up 29 Oct 2026 (docs/birago1448.html): read from existing decipherment (the clear duplicate f. 32), checked sign by sign with Birago's own key, DECODE R5316

Lead 1546 (research/leads.json). The lead was found on 29 Oct 2026 in the leaf-by-leaf check of BnF ital. 1584-1585
(`research/venice_milan_print/ital1584_copies.md`, lead 1316). It was the only cipher leaf of the 1447-48 Milan series
with no decipherment filed beside it. BnF italien 1585 (Archivio Sforzesco), Gallica ark `btv1b52525947w`: canvas 62
holds ff. 32 and 33 on one mount, and canvas 64 holds the address of f. 33.

## Result

- **f. 33 is the ciphered duplicate of f. 32.** f. 32 is a clear letter from the same writer, on the same day, mounted
  above it. The cipher gives the same text word for word, in looser Lombard spelling.
- **The key is Birago's own.** ASMi Carteggio Sforzesco cart. 1597 no. 16 (DECODE R5316, "1450", undescribed) is
  headed "Andreas Biragus": a simple substitution, one sign per letter (no sign for b), plus a sign for *et* and one for
  "Francisco Piccinino". `key_R5316.tsv`.
- **Every sign is on the key.** The 513 cipher signs in 11 lines (the first on the salutation line) are 22 distinct
  signs, all of them on the key (`decode.py` on `texts/f33_cipher.txt`). Two signs are uncertain in shape: L06 c/g in
  "darghelo", and L09 i in "milano". The decryption (`texts/f33_decryption.txt`) reads as sentences throughout. Its
  differences from f. 32 are spelling and small word forms (`texts/f33_vs_f32.md`, 35 items): "rolando" for orlando,
  "ilche" for siche, "caxa", "concluxo", "auixo".
- **The cipher settles one word of f. 32.** f. 32's hard word after "Senza" is "incharicho" (= incarico). The cipher has
  "carigo" there, so the phrase reads "senza carigo de la quale gli daro questo adiuto": I shall give him this help at no
  charge to Your Excellency (*senza carico*, without burden; "without your commission" is a less natural reading).
- **Piccinino is the one name in code.** The cipher writes Francesco Piccinino with the key's code sign. It is the only
  code group in the letter.

Content: two servants of Orlando Pallavicino come to Birago at Pavia with a letter of credence. Sforza has come to terms
with Orlando and urges him to go home, and Orlando asks for help and escort on the way. Birago will give it, and has
encouraged Orlando, all the more because he hears the Milanese (the Ambrosian Republic) mean to give Francesco
Piccinino whatever he asks, especially all his lands. Orlando would be better off at home than at Milan. Birago writes
"for your information": he will give the help at no charge to Sforza. English: `texts/f33_en.md`.

Why both copies: a clear letter and its ciphered duplicate sent the same day, presumably by two routes so that one
would get through. No other copy was found.

## Remaining gaps

- Two sign shapes uncertain (L06 c/g, L09 i) - blocker: illegible; small cramped strokes on a microfilm-derived scan, and the sense fixes both.

## Escalation

- [x] siblings: ital. 1585 ff. 31-34 and the 1447-48 Milan series checked (ital1584_copies_B.md); f. 32 is the clear duplicate.
- [x] clear-pages: f. 32 is the clear text.
- [x] known-keys: ASMi cart. 1597 nos. 1-40 (DECODE R5301-R5340) headings read; no. 16 is Birago's.
- [x] print: no edition of the letter known (Mazzatinti 1887 lists it under Amidani).
- [n/a] key-rebuild: the key sheet is complete for the signs used; every sign of the letter is on it.
- [n/a] retry: nothing unread.

## Sources

- BnF italien 1585, Gallica https://gallica.bnf.fr/ark:/12148/btv1b52525947w (canvases 62, 64; IIIF via openapi.bnf.fr).
- Key: Archivio di Stato di Milano, Carteggio Sforzesco cart. 1597 no. 16, DECODE R5316 https://de-crypt.org/decrypt-web/RecordsView/5316 (image not public domain).
- G. Mazzatinti, *Inventario dei manoscritti italiani delle biblioteche di Francia* II (1887), ital. 1585.
