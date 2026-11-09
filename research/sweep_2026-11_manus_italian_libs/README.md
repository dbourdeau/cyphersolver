# Sweep manus_italian_libs (9 Nov 2026): Manus Online "cifra/cifre" screen, Italian public and church libraries

Task: screen the ~6,000 Manus "cifre" records COVERAGE.md listed as unscreened. Result: **1 candidate row, 3 key leads**. The set
is almost pure noise (numerals, foliation, shelf numbers, "a sum of money"); everything real was already in the repo from sweep B.

## Route (worked, curl/urllib, no Chrome needed)
* Search: `POST https://manus.iccu.sbn.it/o/manus-api/titles-search-post` (form fields `monocampo`, `n=v`, `monocampo:tipo=ONLY`, `page`; 20 per page).
  Detail: `GET /o/manus-api/title?id=<id>` (full record, JSON). Rate 1 request/s, no 429. `harvest.py`, `detail.py`, `screen.py`, `show.py` here;
  raw data in `_dl/` (git-ignored; 4,361 search hits, 4,359 detail records, about 2.3 h of fetching).
* Terms run (ONLY mode, exact word; count): cifra 862, cifre 3,448, in cifra 93, cifrato 25, cifrata 14, cifrati 7, cifrate 12, cifrario 3,
  cifrari 1, decifrato 47, decifrata 52, decifrati 6, decifrate 29, decifrazione 27, decifrare 28, lettere cifrate 2, lettere in cifra 1,
  scrittura cifrata 5, alfabeto cifrato 3, scrittura segreta 1, dispacci cifrati 1, zifra 2, zifre 3, nomenclatore 2, segni convenzionali 5,
  crittografia 6, crittografico 3, crittografica 2, lettera in cifra 1, scritto in cifra 1, scritti in cifra 1 (0 hits: alfabeto segreto, carte cifrate,
  dispaccio cifrato, ziffra, cifre segrete, caratteri convenzionali, lettera cifrata, scritta/scritte in cifra, parti in cifra, passi in cifra, passi cifrati, parti cifrate, decifrazioni).
  Union: 4,361 records; **all 4,359 reachable detail records were read by script** (regex screen for in cifra, cifrat*, cifrari*, zifra, crittogr*, nomenclator*,
  decifr* only with cipher context, "lettere ... cifre", with a noise filter for cartulazione/numerazione/cifre arabe/sums of money/shelf numbers), then the
  ~150 survivors by eye. Second pass on other vocabulary (numeri convenzionali, scrittura segreta/occulta, cifrista, indicati con numeri, chiffr*, cipher, criptat*): 17 hits, nothing new.
* Library mix of the noise: Modena Estense (518 "cifre", all foliation), Roma BNC, Mantova Teresiana, Ferrara Ariostea, Cesena Malatestiana,
  Casanatense, Cassino, Palermo Bombace, Laurenziana, Angelica, Vallicelliana, Bergamo (shelf-number "cifra"), Arezzo Casa Vasari (sums of money), Napoli BN
  (handwriting "decifrare"). None of these libraries produced a cipher row from the "cifre" set.

## Libraries that produced rows
* **Firenze, Biblioteca Moreniana** (Palagi Libri 432 ins. 64): the one new row (Mélanie Double to Guglielmo Libri, 1853-60, ciphered passages; names as numbers).
  Also the Moreniana Carte Libri 9 (Libri's own "sistema crittografico", marginal notes) as a key lead.
* Key leads: Roma APUG 222 (key to Jansen's cipher in the Saint-Cyran letters), Moreniana Carte Libri 9, Firenze BNCF Conventi Soppressi B.III.1613 (recipe cipher key).

## Everything else that surfaced was already in the repo (sweep B, Milan, Venice, Florence sweeps) or excluded
* Already there: APUG Concilio di Trento 690rec, 242rec, 588rec, 608rec; Casanatense Ms.1309; Torino Reale Varia 244; BNC Gesuitico 204; Vitt.Em.1680 (Ubaldini);
  Bologna Marsili 75/C; Moreniana Bigazzi 303; Ambrosiana G 275 inf. (Castaldo, catalogue), A 118 inf., G 309(32) inf.; Angelica 1888; Trivulzio 2246 (Zifra 1499);
  Pavia Aldini 159; Queriniana I.IV.28; Genova BU G.IV.8 and C.IX.30; Cascia Ms. 4; San Severino ms. 20; Ginori Conti 29.x and the Carte Machiavelli (decipherments in the volumes).
* Excluded, not ciphertext: Brescia Queriniana ms. B.V.10-12 (Bagni, nuncio in France, "Registro di lettere e cifre", 1644-45: a register copy of dispatches, deciphered text; edited nunciature, no cipher text expected);
  BNCF Galileiani Gal. 12 (Niccolini/Galileo trial letters with interlinear contemporary decipherment, in the Edizione Nazionale); Roma Sessoriano 380 ("in cifra" is foliation); Duomo di Milano M 33
  (20th-c. shorthand notes); Napoli XII.E.57 and Pavia/Genoa cifrari (key-type, already noted by sweep B); Riccardiana 3490 ("Cifrista della Segreteria delle Cifre" is a post); decorative/ownership colophon ciphers
  (Pisa Cathariniana 156, Ferrara Ariostea Cl. I 215, Vallicelliana B 116 and F 26, Rovereto 20, Torino TIV2: one-line vowel shifts, not correspondence).
* Not rows because the Manus text is one passing mention in a volume record with no folio: Firenze Deputazione di storia patria Missive I cancelleria 37/266 (1448, "cifra da utilizzare in caso di bisogno", key only).

## What remains
* Manus indexes descriptions only where cataloguers wrote them; volumes with cipher letters but no mention stay invisible. A text-level route (Internet Culturale full text, 28,624 hits for "cifra", per COVERAGE.md) is the next step and needs Chrome.
* Libri row needs photographs from the Moreniana; no digital copy exists online.
* COVERAGE.md edit (not made): the line "About 6,000 Manus cifre records unscreened" can be removed; Manus "cifra/cifre" family now fully screened (9 Nov 2026).
