# Southeast sweep: Hungarian National Archives databases and the "never swept" southeast (11 Nov 2026, cloud)

Result: **19 rows** in `candidates.json` (built by `make_candidates.py`), **9 with a complete `open` vetting block**
(all `seen.kind` "not online": no image was viewed anywhere in this sweep). 6 entries in `key_leads.json`.
16 rows are MNL OL G 15 (the archive of Francis II Rakoczi, part taken into exile); 3 are fonds-level leads from the
Greek General State Archives inventory. Nothing citable came out of Romania, Croatia, Slovenia, Serbia, Bulgaria, Malta
or Cyprus: their item-level portals did not answer from this network.

## The find: MNL AdatbazisokOnline, database "II. Rakoczi Ferenc fejedelem leveltara, Emigracioba vitt resz" (G 15)

`adatbazisokonline.mnl.gov.hu` answers curl. Search is `GET /search?term=<base64 of {"q":"...","fq":[],"sort":"score"}>&P=<page>`;
the hits are an inline `var searchResults = [...]` JSON array, 10 a page (`mnl_search.py`). Wildcard `*` works.
Datasheets are `/adatbazis/<db>/adatlap/<id>`; their content is loaded by JavaScript and they carry **no images**.

The G 15 database is item-level and its note field says, letter by letter, whether cipher is deciphered and by whom
("Thaly altal megfejtett", "egykorulag megfejtett", "megfejtetlen"). 825 G 15 records carry a cipher note
(`mnl_g15_cipher_hits.json`); **100 are marked undeciphered in whole or part**. Of those, the ones in fascicles that
DECODE already holds (Caps. C Fasc. 33, 36, 39; D Fasc. 80; E Fasc. 109; G/H Fasc. 226) were left out; the rest are the
16 rows. DECODE's MNL holdings were listed in full (320 records; G 15 only from Caps. C 23/33/36/39/43/44, D 80-81,
E 109, H 226, J 256), so Caps. A1, A2, B and most of D-H are not on DECODE.

Vetted rows (no named edition could cover them, or none was found):
1. A1 Fasc. 11 fol. 111-136: twelve French letters of 1708 in undeciphered signs, three to "Nathanael Siluer" (Rakoczi).
2. A1 Fasc. 11 fol. 26-27: a fourth Henter letter (the repo read R496 in `targets/henter1707`).
3. A1 Fasc. 11 fol. 39-42: secretary Hoger, German, with its cipher alphabet enclosed.
4. A1 Fasc. 10 fol. 227-228, Fasc. 11 fol. 10, 20: three letters "perhaps Bercsenyi's 1704 key".
5. A1 Fasc. 10 fol. 52, Fasc. 11 fol. 36-37, 44-47, 54-55, 71-72: six anonymous number-cipher letters.
6. A1 Fasc. 20 fol. 40-43: Thokoly, with deciphered siblings in the fascicle.
7. A1 Fasc. 22 fol. 19-24: to "Pompeius Cettoni" (key R639 reads the sibling R902 in `targets/rakoczi1707`).
8. A1 Fasc. 3 fol. 42-46: Stibar, German, 1707.
9. E Fasc. 111: seven French letters of Rakoczi's wife from Jaroslaw (the couple's key is Lang T.Rad.73).

Leads without a block (a named edition was not opened): Nedeczky 1708 (E Fasc. 113; item level for **lead 1911**,
Zsemlye 2025 not opened), Brenner 1710 (H Fasc. 230), Karolyi 1706-11, Horvath and Papai Gaspar 1707-10, a mixed row
(Szent-Ivany, Klement "Rosenau", Daniel, Fierville, Bercsenyi, Rakoczi to Cantacuzino and Korbe: split before vetting),
loose French letters (E Fasc. 112-113, D Fasc. 83), Gyorgy I Rakoczi c. 1646-47 (A1 Fasc. 11 fol. 87-92).

Reading of the notes: "reszben Thaly altal megfejtett titkosirassal" means partly in cipher, deciphered by Thaly;
only "megfejtetlen" / "feloldatlan" records were taken.

### Terms run on adatbazisokonline (documents)
rejtjeles 91, rejtjel* 265, titkosir* 363, sifr* 147, chiffr* 40, cifr* 768, zifr* 35, megfejtetlen 99, Ziffern 21,
ziffer* 95, clavis 14, "titkos iras" 177, szamjegyes 19, ciffr* 127, zyfr* 1, cziffr* 366, szamjel* 757, megfejt* 1117,
titkosjel* 39; kriptogr*, cyfr*, cyphr*, ciphr* 0. The run of czifr*, cyfra, rejtjelkulcs*, cifris, ziffris was cut off
by a container restart and not redone. Outside G 15 nearly all hits are 20th-century (MTI news, party minutes, census
OCR). Other early databases: Karolyi P 396 (10 records, already rows of `sweep_2026-11_hungary_czech`), DL-DF
(DF 293290 key, DL 46150: known), 1848-49 operations (a cipher telegram of 24 Jun 1849 with its decipherment: excluded).
The E 190, Batthyany missiles, Transylvanian princes and Reformation databases returned no cipher hit.

### Excluded
- Bisterfeld to Zsigmond Rakoczi 1649-50 (E 204 Kamarai misszilisek, 10 letters "Titkosiras is"): printed deciphered
  in MTT III/10-13 (Lang 2015 C.Bist.01-17, "a szovegkiadas megfejtve kozli").
- G 15 items in DECODE fascicles (e.g. C Fasc. 33 fol. 77-78, C Fasc. 36 fol. 3-4 and 11-12, C Fasc. 39/a fol. 171-172
  and 212, D Fasc. 80 fol. 1-5 and 28-29, E Fasc. 109 fol. 45-47, G Fasc. 226 fol. 50-55): check them against DECODE's
  status when the DECODE dump is at hand; several are "Non-decrypted" there and marked undeciphered here too.
- Records where only a date figure is unresolved (D Fasc. 95 fol. 18-19, E Fasc. 113 fol. 96-97, F Fasc. 189 fol. 47-48).

### Prior-art sources used
- DECODE: `decode_search.py` (`RecordsList?cmd=search&search=...&recperpage=100`, later pages `?page=n` with the cookie).
- Lang 2015 (Hungarian original with a text-layer repertory): `https://real-d.mtak.hu/922/7/dc_758_13_doktori_mu.pdf`,
  pdftotext works; T. rows are keys, C. rows ciphertexts. Lang 2018 (Real Life Cryptology): archive.org
  `oapen-20.500.12657-28452/1001507_djvu.txt` (the appendix tables are rotated and unreadable in the OCR; library.oapen.org is 403).
- Tomokiyo: index page and `unsolved.htm` have no Rakoczi or Hungary article. Lasry: only the repo copy `GL.htm` was searched.
- Three web searches (Sarolta Amalia; the aliases; the G 15 database): no edition or reading found.

## The southeast portals

| Source | Result from this network |
|---|---|
| arhivelenationale.ro, cautare.arhivelenationale.ro | connection reset; not swept |
| arhivamedievala.ro | http answers with an Oracle ADF JavaScript shell; headless Chromium got a network error; not swept |
| dspace.bcucluj.ro (Cluj) | works: cifrat 855, rejtjeles 112, titkosiras 22, criptograma 22, "scriere cifrata" 2, "scrisoare cifrata" 3, Geheimschrift 4. Printed books and newspapers only, no manuscript |
| arhinet.arhiv.hr (Croatia) | does not resolve / 502; not swept |
| dad.hr (Dubrovnik) | no catalogue; the 2026 general inventory PDF (fonds level) has no cipher word |
| digitalna.nsk.hr, dizbi.hazu.hr | work (`indigo_search.py`, `?pr=l&msq=`): sifra, sifre, sifrirano/a/i, tajnopis, "tajno pismo", kriptogram, cifra, chiffre, cifrato: 0-7 hits, all printed books |
| siranet.si, arhiv.gov.si, vac.sjas.gov.si | connection reset; sistory.si search 403; not swept |
| arhiv.gov.rs, arhiv.rs, digitalna.nb.rs | 502 / reset; arhivyu.rs and arhiv-beograda.org load but were not searched (no item search found) |
| isda.archives.government.bg (port 84) | no connection; not swept |
| arxeiomnimon.gak.gr | reset / 503; not swept |
| greekarchivesinventory.gak.gr (AtoM, fonds level) | works (`atom_search.py`): κρυπτογραφ* 17 fonds, συνθηματικ* 2. Three lead rows (Melas 1904, Petimezas 1941-46, Chotzis) and key leads; Plastiras [1935] notes are described as read; Filiki Eteria diplomas use the known alphabet |
| searchculture.gr | advanced-search GET returns 400; not swept |
| Malta: nationalarchives.gov.mt 403, vhmml.org reset, maltalibraries (JS catalogue, printed books) | not swept |
| Cyprus: cyprusdigitallibrary.org.cy | no connection; not swept |
| hungaricana.hu | 403 (as in the brief) |

No bot check was met; the failures are network level, so the next try needs another network or the user's Chrome.

## What remains
- Order scans of G 15 Caps. A1 Fasc. 10, 11, 20, 22 and E Fasc. 111 (the vetted rows), about 80 leaves.
- Open the editions named in the unvetted rows (Zsemlye 2025, Bankuti-Meszaros, Archivum Rakoczianum, Fiedler, Szilagyi),
  then vet or close them; split the mixed row by writer.
- 123 G 15 records read "reszben megfejtett ..." (taken here as "partly in cipher, deciphered"); if the scans show
  that some mean "cipher only partly deciphered", they are further leads. Not gone through one by one.
- The dropped MNL terms; the E 190 and Batthyany databases by browsing rather than by cipher word.
- GAK: ask for item lists of the Melas and Petimezas archives.
