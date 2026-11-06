# Riksarkivet western Diplomatica and the Stedingk fonds, volume pass (6 Nov 2026)

Source key `riksarkivet_west`. Goal: sheet every digitised Diplomatica volume outside Turcica/Polonica (Muscovitica,
Gallica, Italica, Hollandica, Anglica, Danica, Germanica, Americana, Maroccana) and the diplomatic papers of Curt von
Stedingk (ambassador at St Petersburg 1790-1811), and find cipher, above all cipher with no decipherment. **7 rows** in
`candidates.json` (`make_candidates.py`); the per-volume record is `findings.md`.

## Method

1. `nad_enum.py`: NAD API, `text=*`, `only_digitised_materials=true`, facet `PartOfArchive:<series>`, for 26 Diplomatica
   series names and `Stedingkska arkivet` -> `enum.json`. Digitised volumes found: Muscovitica 16 (incl. Cosacica),
   Gallica 9, Italica 6, Hollandica 4, Anglica 3, Danica 2, Germanica 1, Americana 3, Maroccana 19, Stedingk 164. No other
   Diplomatica series (Hispanica, Lusitanica, Helvetica, Saxonica ...) has digitised volumes.
2. `build_units.py` -> `units.json` (118 volumes, 32,459 images): image-series ids from sweep D's `rik_vols.json` or the
   APE EAD `<dao>`; skipped Courtin 11/14 (sheeted 2 Nov), Cosacica 2 and 1a (viewed by sweep D), the Orlik diploma, and
   in Stedingk the Pomeranian family papers, accounts, rolls and print (59 of 164 kept: drafts of despatches, royal letters,
   correspondence 1788-1814, state papers).
3. `batch.py` -> `rik_sheet3.py`: 15 images per volume from image 2, **600 px a tile, 3 columns**. A first pass at 300 px,
   6 columns (`rik_sheet.py`, the earlier sweeps' size) was abandoned after it hid a page of mixed digit groups and words
   (Muscovitica 3/b/602 image 108); every volume was re-sheeted at 600 px. Diplomatica sheets were viewed at full size;
   the Stedingk sheets at half scale (four to a composite).
4. Suspects at 900-1200 px (`rik_pick.py`); every cipher page cropped at 2400-3200 px (`rik_zoom.py`) to look for faint
   interlinear decipherment before calling it bare; neighbouring images paged for deciphered copies; extra sheets for the
   two volumes with bare cipher.
5. `known.py` on every shelfmark and correspondent: no hits (see findings.md, Notes).

Route as in `sweep_2026-11_riksarkivet_turcica`: lbiiif with `Referer: https://sok.riksarkivet.se/`, about one request a
second. No bot check, no Chrome.

## Results

118 volumes sheeted (59 Diplomatica, 59 Stedingk). Cipher in 9 volumes, 7 rows:

| Row | Volume | Images | Decipherment |
|---|---|---|---|
| Ludwig Camerarius, The Hague 1626-30, Latin numeric nomenclator | Hollandica I/5/7 (R0003234) | bare: 426, 432, 442, 460 (2400 px); 428 bare (3200 px) but duplicates glossed 427 | **partly bare** (class B); glossed 109, 427, 498, 215 (second system) |
| Consul P. C. Wulff, Salé 1764-66, unbroken digit strings | Maroccana II/I (R0003632) | 11, 12, 13, 14, 18, 24 | **bare** (class C): none seen at 2400-3000 px; same style as Molinari, Tunis (lead 2260) |
| Commissary Adolf Ebers, Moscow 1662-66 | Muscovitica 3/b/602 (R0003225) | 106, 108, 121, 138, 160 | glossed (class A) |
| Resident Johan von Lilienthal, Moscow 1665-67 | Muscovitica 1/36/82 (R0000814) | 38, 47 | glossed (class A) |
| Envoy Carl Bonde, Paris 1674-78 | Gallica I/A/24/54 (R0003797) | 113, 335, 446, 520 | glossed (class A) |
| Lt col. Abraham von Stauden, Morocco 1772-75 | Maroccana I/I (R0003619) | 76 | glossed, two lines bare (class A) |
| H. G. von Müllern to Palmquist and Gyllenborg 1710-16 | Hollandica I/26/301 (40006086), Anglica I/26/214 (40006088) | 89, 152; 133 | glossed (class A) |

Clear-text crib sources: Stedingk's drafts mark ciphered postscripts (E 6601 image 108, `Apostille en Chiffre`, 1805;
E 6588 image 60, 1790); the ciphered originals are not digitised.

## Sheeted, no cipher seen

Muscovitica: du Moulin 1649-50, Bergenhielm 1698-1700, Kock 1684-90, Cederhielm 1725-26 (two volumes), Teusina border
commission 1595-96, Karl Filip election 1613-15, Prontsichev protocol 1683, tsars' letters, Stedingk/Skjöldebrand 1809
(two). Gallica: Grotius (7/8, 7/9, 7/10), Cling 1651, Palbitzky 1652-54, Courtin 11/15, French memorials 1738-48. Italica:
all six Piranesi volumes 1782-98. Hollandica: Vellingk to Palmquist 1711-12. Anglica: Scotica 1562-1650, Protectorate
letters 1645-60. Danica (two border volumes), Germanica (Kleihe instruction 1655), Americana (three). Maroccana: 16 of 19
(the naval missions 1777-95, consuls Wenström and Wijk, accounts, petitions). Stedingk: all 59. A 15-image sample per
volume catches only volumes where cipher is common: "no cipher seen" is not "no cipher".

## Not reached

- Full paging of the cipher volumes (Camerarius 535 images, Wulff 167, Bonde 557, Ebers 172, Lilienthal 137) for a list of
  every ciphered letter and whether it is glossed.
- Wenström 1775-87 and Wijk 1787-1809 (Maroccana II/II-IX, II/X) were sampled at 15 images only; given Wulff's bare cipher
  they deserve paging.
- DECODE, Tomokiyo, Lasry and the editions were not searched for the seven rows (only known.py). For Camerarius: Schubert
  (1955) and the Munich Camerariana; for Wulff: the Kanslikollegium consular cipher books.
- Stedingk's other 105 digitised volumes (family papers, accounts, print), Ludvig von Stedingk's papers, and the other
  private fonds named by the 2 Nov sweep (Barthelemy, De la Gardie, Tessin, Reuterholm, Ericsberg).
