# Mírka's Crypto-World survey, Tant's ARCSI pages, SNA inventories (9 Nov 2026)

**Result: 10 rows in `candidates.json`** (8 from Mírka's survey of the SOA Plzeň/Litoměřice family archives, 2 from the Slovak
National Archives), **5 key-only items in `key_leads.json`**. Built by `make_candidates.py`. All rows are `seen: catalogue` (no leaf
viewed; no images online). `known.py` run on all shelfmarks, inventory numbers and correspondents: no duplicates. This folder is
not in `merge.py`'s sweep list (outside this folder; add `sweep_2026-11_mirka_cryptoworld` before merging).

## The survey was found and read

Jakub Mírka, "Raně novověká šifrovaná korespondence ve fondech šlechtických rodinných archivů Státního oblastního archivu v Plzni",
printed in *Západočeské archivy* 2012 (pp. 44-73, not online; the soaplzen.cz PDF of that volume holds only the contents and
front matter) and reprinted in three parts in **Crypto-World**, free PDFs, no login:

| Part | URL | Contents |
|---|---|---|
| I | `http://crypto-world.info/casop14/crypto1112_12.pdf` (11-12/2012, pp. 12-28) | method, Trauttmansdorff fonds (Kurtz 1638-39, Lustrier 1625, Lisola/Tasselt 1645, Schönburg 1637, Blumenthal/Holzappel 1646) |
| II | `http://crypto-world.info/casop15/crypto0102_13.pdf` (1-2/2013, pp. 2-12) | Windischgrätz, Verdugo, Nostitz fonds, Beaufort-Spontin footnote |
| III | `http://crypto-world.info/casop15/crypto0304_13.pdf` (3-4/2013, pp. 2-14) | general survey of cipher use, interception, key sources; Clam-Gallas, Buquoy, Rožmberk |

Image appendices: `casop14/cast1.zip`, `casop14/cast2.zip`, `casop15/obr3.zip` (not fetched; page images are in the PDFs). The
`www.` https host of soaplzen.cz fails the TLS name check from curl on this machine; the plain `http://www.soaplzen.cz/...` URL works.
Texts extracted with pymupdf (scratchpad, not kept). Mírka's own statement of the odds (Crypto-World 1-2/2013, 3-4/2013 p. 9):
of ~40 ciphers studied he rebuilt a key for ~70% from a deciphered letter in the file, ~10% by a key elsewhere in the fonds, ~20% found
no key; the unread residue (about 12%) is exactly the lead list here.

## Rows from Mírka, and what was dropped

Kept (Mírka says "not deciphered" or reports no reading, shelfmark checked): Charles VI to Windischgrätz 1720/22; Gallas to Eugene of Savoy
1711; Colebrooke 1721-23; Lisola/Tasselt 1645; Erskine intercepted copy 1644; Schaffgotsch/Mayerberg/Zierowski to Nostitz (key held);
Zehentner 1686; Gaffarel Sauvans 1677 (box only).

Dropped, with reasons:
- Ferdinand III to Trauttmansdorff, 13 Nov 1634 (kart. 6 inv. 68): already in `catalogue.json`.
- Kurtz von Senftenau 1638-39 (kart. 10 inv. 200): already `targets/kurtz1639` / DECODE R3811-R3815.
- Rabenhaupt ze Suché to Amalie Elisabeth 1646 (inv. 125): read in 2020, published by Antal, Zajac, Mírka (HistoCrypt 2022); catalogue already notes it.
- Christian of Anhalt to Verdugo 1626-27 (inv. 13), Nostitz inv. 91 key, Nostitz-Planá inv. 306, burgrave of Donín inv. 148: already rows of `sweep_2026-11_czech_slovak`.
- Windischgrätz brothers 1721 (inv. 1433): DECODE R5029, catalogue entry 68.
- Rožmberk, Historica Třeboň 4834/36: already a row of `sweep_2026-11_czech_chrome`; edited by Veržovskij 1889.
- Blumenthal and Holzappel 1646 (inv. 122, 184), Lustrier 1625 (inv. 330), Solre to Verdugo 1627 (inv. 29), Zierowski 1681, Kinský to Kounic
  1697-99 (inv. 1395): plain text written in the letter or read by Mírka; these are key material, not rows.
- Schönburg (Madrid) 1637 with a copy of Rozas's ciphered letter (inv. 271) and Sieber (Hamburg) 1639 (inv. 274): no reading status given by
  Mírka and the ARON records have no cipher note; recorded here as unrated hints only. Gottlieb Windischgrätz's three ciphered relations from
  Copenhagen 1673 (inv. 1423): concepts with the clear text underlined.
- Buquoy letters at SOA Třeboň (Oñate, Dampierre, Spinola, 1618-20; RA Buquoyů sign. 172, 246, 69/1-2, KB 50 Q, KB 171 Q, KB 756/6): simple
  substitution; some printed in Documenta Bohemica belli tricennale illustrantia II (pp. 76, 82, 89, 92, 99, 133, 135, 138, 182). Which are
  printed and deciphered was not checked and the Třeboň portal has no item records, so no rows; a follow-up could check those pages.
- Archiv Národního muzea, Sbírka D, karton 9 (Rudolf/Matthias/Althann): Hanka printed and deciphered them in 1847 (all but one, which Maloch read 1858).
- Uppsala MS Slav. 60 (Mnišovský): a cipher manual, not a letter.

## Slovak National Archives (Antal et al., HistoCrypt 2023)

"Encrypted Documents and Cipher Keys From the 18th and 19th Century in the Archives of Aristocratic Families in Slovakia" (open PDF at
`https://ecp.ep.liu.se/index.php/histocrypt/article/download/689/595/706`) counts 96 ciphered documents in 13 boxes: Esterházy
(Čeklís branch, boxes 631, 634, 635, 636: 58 documents), Amade-Üchtritz (boxes 136-141, 150: 37), Pálffy-Daun (1). The authors state
which boxes carry plain text. I matched the boxes to the SNA finding aids (PDFs on minv.sk, `Esterhazi-cekliska_vetva_(1252)_1498-1939-inventar.pdf`,
250 pp., and `Amade-Uchtritz_z_Gabcikova_(1272)_1327_-_1916-inventar.pdf`, OCR text): Esterházy karton 634 = inv. 1612 (A-4),
karton 636 = inv. 1621 (A-13), 635 = inv. 1618-1620 (concepts with ciphered parts below plain text, not rows), 631 = inv. 1602 (H-1, one
4-page ciphered German letter of 1744, no status given). Rows: inv. 1621 (no plain text) and inv. 1612 (plain text in separate documents,
keys do not match).

Not rows: Amade-Üchtritz inv. 3009 (Senfft-Pilsach, Paris 1806-11, box 139), 3011 (Schulenburg/Griesinger/Einsiedel/Minckwitz 1815-24,
box 140), 3014 (Brühl to Fleming 1757-62, box 141), diary of Emil Üchtritz 1804-05 (box 150): plain text above or beside the cipher, or key matched;
inv. 3008 is a key (`key_leads.json`). The Pálffy-Daun fonds (one Charles VI letter, seven keys) was not located in the SNA list: the Pálfi
inventories searched (`palfi_pezinska_vetva_1247_1935`, `palfi_ustredna_sprava_majetkov_pezinskej_vetvy_II`, `Palfi-panstvo_Cerveny_Kamen_I`)
have no cipher entries. A Dorotheum blog ("The Empress's Code") describes a 1744 coded letter of Maria Theresa to Esterházy with a key in
Vienna; the page returned 403 and was not read; it is probably a separate item sold at auction.

## ARCSI / Tant

`arcsi.fr/doc/Tant/` numbers found from the page indexes (`/fichiers_Tant/Tant_*.php`): 358-383, 388, 407, 410, 414, 420-425, 427-428 and named files
(`Chalons`, `CardinalRohan`, `Poterat`, `16clesdechiffrement`, `Tables1750`, `EvequeCryptographe` ...). Fetched and read the cipher-related ones:
358 (Henri IV / Landgrave of Hesse key, from Valério 1896), 359-360 (Dralon key), 363 (émigrés 1793), 367-370 and 381 (Napoleonic codes,
all keys), 16clesdechiffrement (sixteen 17th-c. keys at Reims), CardinalRohan (Rome, 1 Jul 1721, partly deciphered in the file, Reims, carton XVI no. 49-50),
Chalons (1594, read), Poterat (Russia, 18th c.). **No cipher item outside France that is both a letter and unread**; the keys (Dralon, Hesse,
Napoleonic) are French-held or printed. Nothing added from Tant. (420 was done in `sweep_2026-11_france_departmental`.) The bulletin
"Les chiffres dans les archives" was not located on arcsi.fr (`bulletin.php` not read).

## Other surveys searched (not all fruitful)

- Hungarian: Láng, *Real Life Cryptology* (open access, AUP 2018; 300 keys, 1,600 ciphered letters, appendix lists) and his MTA thesis 2015 are already
  in `research/oldest/scan_2026-09-23/central_north.md` and the `hungary_czech` sweep; not re-read.
- Polish ("szyfry w archiwach"), Croatian, Slovenian surveys: no equivalent curated list found by web search (6 queries; no hits worth following).
- Slovak: besides Antal et al. 2023, Krajčovič's article on Maloch and Šusta (Crypto-World 1-2/2013, pp. 13-21) is about solvers, not new items.

## Blocked / not done

- `Západočeské archivy` 2012 print article (the PDF on soaplzen.cz is a stub of front matter); the image zips on crypto-world.info.
- ARON records for inv. 694, 77, 78, 289 (found), Beaufort-Spontin box 25 not located; SOA Litoměřice Clam-Gallas fonds has no item records.
- SNA scans: not online; the HistoCrypt authors (Antal, Zajac) hold photographs and plan HCPortal records.
- Dorotheum blog 403.
