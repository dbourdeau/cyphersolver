# Archives Portal Europe sweep (2 Nov 2026)

Portal: www.archivesportaleurope.net, "Search in archives" (item/unit descriptions). Read in the user's own Chrome (Claude in
Chrome), in a tab opened for this sweep, as same-origin `fetch` calls to the portal's own `/get-results/` JSON endpoint (the
one the result page itself calls), one request every 2.5 s, 10 records per page. No Cloudflare page, CAPTCHA or login appeared;
nothing was clicked through. Rows are leads, not catalogue entries: all 28 are scored from the portal description only
(`seen: catalogue`); no scan was viewed and Tomokiyo, Lasry and the editions were not searched.

Output: `candidates.json` (28 rows, built by `make_candidates.py`, every field `merge.py` REQUIRES; region, period, cls and
the 1-5 scores checked against `merge.py`'s vocabularies). Raw harvest (3,273 records) sat in that Chrome profile's
localStorage (`apedb`, `apest`), not on disk; the transfer to disk by a local POST was blocked by Chrome and abandoned.

## Counts

3,273 distinct records fetched over 85 queries. 2,043 carry a cipher stem in title or description; 1,599 of those are unique
by title and date and dated 1950 or earlier or undated. Roughly two thirds of the 1,599 are (by eye, not counted) the WWII Auchinleck "cipher message"
typescripts (Rylands), Portuguese interwar telegrams, Spanish AGS "carta cifrada" series already held by the PARES sweep, and
French Archives nationales consular letters (AE/B/I) whose calendar entries summarise the content (so already read). After
`known.py` on shelfmarks and correspondents, 28 rows remained; the rest were tracked (Lemaire/Alger 1752, Villeneuve 1737,
Decury 1747, Martinique C8 A 77, Landsberg-Velen/Türkenlouis, Hatzfeldt, Lucchesini, Gyllenstierna, Mörmann, Taquet,
Convento da Graça, Hautefort, Sf 35) or deciphered.

The portal's `chiffre` hits are mostly "chiffre d'affaires"; `cijfer`, `Ziffer`, `Schlüssel` likewise. Pages read per term
(total hits on the portal / pages of 10 read / records matching the stem):

| Term | Portal total | Pages | Stem hits |
|---|---|---|---|
| cifrada | 607 | 25 | 200 |
| cifrado | 100 | 10 | 87 |
| cifra | 554 | 15 | 136 |
| chiffre | 7,864 | 12 | 120 (noise) |
| lettre chiffrée / lettres chiffrées | 1,168 / 141 | 15 / 15 | 146 / 59 |
| dépêche chiffrée | 101 | 10 | 71 |
| déchiffrée / déchiffré / déchiffrement | 51 / 36 / 204 | 6 / 4 / 10 | 28 / 15 / 77 |
| "en chiffre" | 86 | 9 | 29 |
| cifrario / cifrate / cifrata | 20 / 1 / 0 | 2 / 1 / 1 | 20 / 1 / 0 |
| chiffriert / chiffrierte | 55 / 137 | 6 / 10 | 26 / 80 |
| Geheimschrift / Geheimschriften | 340 / 88 | 15 / 6 | 149 / 56 |
| Chiffrenschlüssel / Chiffreschlüssel / Chiffrierschlüssel | 6 / 9 / 21 | 1 / 1 / 3 | 5 / 7 / 13 |
| Ziffer / Schlüssel | 3,095 / 3,282 | 10 / 10 | 100 / 100 (noise) |
| cijferschrift / cijferschrift gezant | 57 / 5 | 6 / 1 | 44 / 4 |
| cijfer / "in cijfer" | 10,591 / 7,492 | 3 / 5 | 30 / 36 (noise, stopped) |
| chifferskrift | 5 | 1 | 2 |
| шифр | 263 | 9 | 39 (mostly Estonian Soviet-era files) |
| şifre | 3 | 1 | 1 |
| szyfr | 69 | 7 | 67 |
| šifra / šifreeritud | 31 / 65 | 4 / 6 | 16 / 60 (Estonian "Šifra" is a given name) |
| rejtjel | 74 | 4 | 10 |
| cipher / cypher / ciphered | 435 / 180 / 1 | 20 / 15 / 1 | 200 / 120 / 1 |
| decipher / deciphered | 138 / 41 | 14 / 5 | 80 / 15 |
| en cifra | 284 | 10 | 38 |
| cipher dispatch | 12 | 2 | 12 |
| chiffre Constantinople / ambassadeur / Turquie | 50 / 119 / 97 | 5 / 8 / 5 | 11 / 16 / 6 |
| en chiffre ambassadeur | 113 | 6 | 15 |
| cifrada / cifra Constantinopla | 2 / 1 | 1 / 1 | 2 / 1 |
| Chiffre Gesandter / Chiffre Konstantinopel | 4 / 2 | 1 / 1 | 2 / 0 |
| cijferschrift gezant | 5 | 1 | 4 |

Zero-result queries (the portal is thin there): cifra Constantinopoli, cifra bailo, cifra Ragusa, cifra ambasciatore, cifra
Venezia, cipher Constantinople, Chiffre Internuntius, rejtett írás, šifra Dubrovnik, šifrirano, šifrovaný, šifrovací, šifra
Carigrad, šifras, κρυπτ (the portal does not stem; Greek roots not tried further), cijferbrief, cijfer Konstantinopel, "dépêche en
chiffre". Run as exact phrases (quotes) the portal matches the phrase; unquoted multi-word queries are ANDs.

## What the portal yielded

The portal is strong on French (Archives nationales), Spanish (AGS, AHN, AHNOB, AGI), Dutch, German (Archivportal-D
mirror), Portuguese (Torre do Tombo) and UK catalogues, and nearly empty for Italian, Ottoman-side, Hungarian-language,
Croatian, Czech and Greek material. No new Venetian bailo, Ragusan, Habsburg internuncio or English/French Constantinople
cipher letter turned up that is not already in the catalogue: the French Constantinople letters (AE/B/I/386-448: Villeneuve
1737 "non déchiffrée", Vergennes 1758 and 1761, Castellane 1744, Saint-Priest 1773 and 1776, Des Alleurs 1714) are in the
catalogue or described with a content summary. The best new rows are the two untranslated William Watts cypher runs of 1757
(BL Mss Eur G37/8/4 ff.54-66), the Van Aylva letters with their key in the same inventory (Gelders Archief 0439 nos.
124-126), the Verdugo / Van den Berg letter of 1594 with a transcription of one piece, the Antwerp siege letters of 1585, and
the Nassau family letters (7-02, 7-03, 7-06).

## Key leads (bare keys, not rows)

Gelders Archief 0439-126 (key to nos. 124-125); Quai d'Orsay 166PO/A/131 "Table du chiffre du marquis de Villeneuve";
Trento prince-bishop's chancery series (portal code IT-TN0213, record IT-ASTN-F890500232) (sixteen mid-16th-century cifrari, 1303_06 to _22, including
"Cifra con Turca", Fabrizio Colonna, Cardinal of Carpi, Duke Maurice of Saxony; portal code IT-TN0213); HU-MNL-OL P 396 nos.
379 and 11345 (Rákóczi keys); Nationaal Archief 1.05.01.01-44 (Abraham de Pina Forao gives the key, May 1646), 2.21.227-336
(keys in Lodewijk van Toulon's hand), 1.10.40-14 (Geldermalsen cipher 1674), 1.10.26-104 (Dumas, 1776), 3.01.19-2315-2317;
Hull DDHO/3/19 and /30 (notes on Reichenbach's cypher, c.1730); GB/2495/CS1/5.0 (Southampton cipher, c.1590); NLA ST Rep. 32
Nr. 194 (Busbeck, Paris, ciphered and deciphered reports 1581-88); BayHStA Kurbayern Äußeres Archiv 195 (keys to Maximilian's
correspondence 1620-48); Jülich-Berg II Nr. 2041, 1938 and 1940 Bl. 42 (Chiffrenschlüssel, 16th century).

## What blocked, what was not reached

- Nothing was blocked by Cloudflare or a CAPTCHA. The `fetch` to the portal worked from a tab on its origin without a
  challenge. A POST of the harvest to a local server (127.0.0.1) hung in Chrome's local-network permission and was dropped; the
  data reached disk only as the 28 rows below.
- Every term was capped (10 to 30 pages of 10 records, stop after two pages with no stem hit). So "cifrada" (607) was read to 250,
  "cipher" (435) to 200, "Geheimschrift" (340) to 150, "chiffre"/"Ziffer"/"Schlüssel"/"cijfer" were sampled only. Records
  beyond those pages were not seen; the AGS "carta cifrada" run (about 240 unique records) was not triaged against the PARES
  sweep and is not in the rows.
- The portal exposes no date filter that I could find (guessed parameter names changed nothing); dates were filtered afterwards.
- The Russian-language, Hungarian, Czech, Croatian, Baltic and Ottoman-side holdings that the brief prioritised returned
  almost nothing: Estonian (ERA, EAA) hits are Soviet-era "шифр" file numbers and the given name Šifra; the one Latvian hit is a
  ministry office; Hungarian hits are the Rákóczi keys and the Maffeo/Sadoleto/Caprili images already in the repo.
- Not run: Czech (`šifra` returned zero Czech or Croatian cipher letters), Polish beyond `szyfr`, Greek, Turkish (`şifre` 3
  hits, a 20th-century sketchbook), Hungarian `titkosírás`, Swedish `chiffer`/`chiffrerad`, Danish `chiffreret`, Portuguese
  `cifrada`, Catalan `xifrada`. The French Constantinople calendar (AE/B/I) was not read beyond the entries the cipher terms
  returned.
- Only descriptions were read; no record page and no scan was opened. The record link in each row is the portal result URL
  (built from the repository code, term and record id the result list gave); it should be opened once to confirm it resolves.
