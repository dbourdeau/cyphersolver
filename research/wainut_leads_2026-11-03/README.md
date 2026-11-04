# WAINUT leads, 3 Nov 2026: Estense, Berlin, Munich and Copenhagen sweeps, plus status notes on worked items

Contributed by WAINUT. The sweeps and the image work were done with AI language-model agents. No human palaeographer
has checked any sign. Output follows `research/archive_sweep_2026-10/BRIEF.md`.

**Result: 31 rows in `candidates.json`.** They come from three sweeps:

| Sweep | Source | Rows here |
|---|---|---|
| Biblioteca Estense, Modena (Lodovico Media Library / Estense Digital Library) | record search and IIIF manifests | 11 |
| Staatsbibliothek zu Berlin (SBB); Herzog August Bibliothek (HAB) not reached | Kalliope SRU, Handschriftenportal API | 8 |
| Bayerische Staatsbibliothek (BSB, on MDZ), Collectio Camerariana; Royal Danish Library | Halm's printed catalogue on MDZ, Primo API | 12 |

The rows are leads. None carries a `vetting` block: prior-art checks were short (see each row's `prior_art`), and
DECODE, Tomokiyo and Lasry were checked only through the dumps and searches named there. 14 rows were looked at on
the scans (`seen: image`); 17 are scored from a catalogue description.

Below the rows: status notes on catalogue entries we worked on 3 Nov 2026 and could not solve (with proposed
corrections; `catalogue.json` is not touched), key leads, dead ends and what was not reached.

## Dedup

Each row was checked against `catalogue.json` and `research/leads.json` at the base of this branch (41ee71653) and
against the same two files on `main` as of 3 Nov 2026 (06a14562b): normalised shelfmark, Estense manifest uuid or MDZ
id, and DECODE ids. No hits. Sender names and shelfmark terms were also grepped in `targets/*/NOTES.md`,
`CATALOGUE.md`, `SOLVED_CATALOGUE.md` and `README.md`. Related, not the same item:

- Ercole II cc. 39-41 (row 2) is a sister of catalogue 1566 (`targets/ercole1559`: cc. 50-51 and Ariosto c. 1).
- Camillo Capilupi cc. 17-19 and 44-47 (row 6) are sisters of catalogue 1565 (`targets/capilupi1545`: cc. 15-16, 48, 49-50).
- Gallio to Dandini, 4 Apr 1580 (row 0) is the same correspondence as `targets/dandini1580` (ASV Francia 283C), but this
  letter is filed in Modena, wrongly under Paolo Giovio, and is not in the repo.
- Ranke's Brussels excerpts (row 17) are not catalogue 526 (Ranke Nachlass Segment III, Bl. 1, the 1547 letter).
- Hurtado de Mendoza 1549 (row 4): the open PR #216 (`mendoza1548`) has a Hurtado de Mendoza key of 1548. Not tested.

Left out because WAINUT submits them separately as targets: Saint-Mauris 1547-48, Gondi 1649, Marignano 1546,
Francesco d'Este 1546, Selvatico Estense 1719 and Rinaldo d'Este 1697 (all Estense); Camerarius to Solms 1621-22
(Clm 10397 n. 129-210, with n. 194) and its key source n. 63 in Clm 10398; Rákóczi's *mandata* of 1632 (Clm 10401 n. 139).
A note on our own sweep: it first put the Solms series in Clm 10398. Halm's p. 92 lists n. 129-210 before "Vol. 48. n. 1",
so the series is in Clm 10397 (Cam. 47).

## Best leads

1. **Lodron to Ferrante Gonzaga, Dec 1549** (row 1). Two letters, about 15 cipher runs, most with a contemporary
   decipherment above them. Worked on 3 Nov: not a simple substitution (two glossed pairs conflict), probably homophonic
   with syllable or null signs. A transcription job.
2. **Alvaro de Sande, c. 59** (row 8). About 24 lines of cipher on 59r, roughly 1,000 signs, with one letter written above
   each sign. A transcription job.
3. **Gallio to Dandini, 4 Apr 1580** (row 0). Cipher on c. 7, decipherment on c. 5. Not started.
4. **Clm 10382 scans 470 and 476-477** (row 30). Long two-digit cipher passages with interlinear decipherments
   ("Radziwill", "Littaw", "Großfürsten", "Hungarn", "Schweden"). Halm's wording, as far as we checked it, does not call these
   pieces cipher. Found while paging the volume; not transcribed.
5. **Fegraeus at Helsingør, 11 July 1632** (row 25) and **Pawel's report, 15 Nov 1624** (row 22). Located (Clm 10406 scan 284,
   Clm 10382 scans 181-182). Code numbers with glosses. Neither is the Camerarius code of 1621-22; for Pawel that is not settled.
6. **Jablonski to Ráday, 1704-07** (rows 11-13) and **to Rákóczi, 1712** (row 14). Berlin draft books with the key sent in
   no. 62 of 1704 and cipher written above the Latin in 1705. No SBB images were found; single drafts of these books are
   online as PDFs at UCF STARS (PRINT Migration Network), not yet matched to the numbers. Benda's edition of Ráday's
   papers may print the received letters in clear: not checked.
7. **"Francesco Rota" to "Mr. Vatron", The Hague, 8 Apr 1624** (row 19). Viewed: Italian clear text with run-together
   two-digit numbers and the letters g, p, t, c, x and & as signs. No decipherment on the page. Ciphertext only.
8. The other Camerariana pieces (rows 20, 21, 23, 24, 26-28), Ercole II 1547 and 1559, Hurtado 1549, Federico II 1537,
   Camillo Capilupi 1545. Lower: Del Carretto 1576, Donati 1617 (decipherments only; cipher leaves cc. 3-4 not found online),
   Lucrezia Borgia 1510 (cipher not confirmed, no scans), Grebner 1573 (prophecies "in Chiffreschrift", not digitised),
   Fragm. var. 575, Ms. theol. lat. oct. 184, Gøhr 1750 (a cipher with its key, no images found).

## Status notes on items we worked and did not solve (3 Nov 2026)

These are catalogue entries or leads. Changes are proposals for you to apply or not.

- **Catalogue 1637 (HStA Darmstadt D 4 Nr. 376/4). Key only, no ciphertext found; date is 1685-1704.** All 102 images
  were surveyed (a survey, not a line-by-line reading). Image 100 is a key: a two-row letter-swap alphabet
  (`a m o r e b c d f g h i` / `k l n p q s t u w x y z`), numeral signs and a worked example ("der Hector wird in p. ckxqo von
  Tripoli fqx pqzbqo"). Image 101 is a cover-name table for 15 persons of the Württemberg court and five places. No letter
  in the file is written in the key. The "continuous symbol script" noted at vetting is ordinary German cursive filmed
  upside down (Landgravine Elisabeth Dorothea, 1686-87). The finding aid gives 1685-1704 and the film shows 1685-1699; the
  persons in the table point to about 1697-98 (our inference). **Proposed:** year 1635 → 1685-1704; status "key and
  cover-name table, no ciphertext located in the file", like D 4 Nr. 141/2 (issue #207). Cover names or swap-alphabet words
  could still sit inside clear letters; Schroeder 1698 (images 21-27) names people in clear where checked.
- **Catalogue 1555 (Ippolito Capilupi, Campori cc. 80a-80h). Digit code, not solved.** c. 107 is transcribed by shape in two
  passes (886-907 signs, 96.4% agreement). One sign per letter, digit pairs on a fixed grid and a polyphonic model were
  tested and ruled out or unsupported; repeats are few. Small letters stand above some digits (8 carries *i* at all five
  places, 7 *a* twice, Q *n* twice): a partial contemporary gloss or the writer's aids, probably labelling groups of
  digits. **Proposed:** (a) the suggested key source, Capilupi's letter of 18 June 1544 in the Ercole Gonzaga fonds
  (sfasc. III cc. 88-92), is not a key for this cipher: its cipher side, c. 89r, is in Cardinal Ercole's letter table
  (catalogue 1556, `targets/ercole1544`), so Ercole's office re-enciphered the letter; (b) "no decipherment" → "no
  decipherment; small superscript letters over some digits"; (c) the address "Vicere di Sicilia" and the dockets
  ("da Civita Vecchia, 17 mayo"; "di Roma alli 10 di maggio") put the letters no later than 1546; 1544 is not confirmed.
- **Catalogue 1563, second letter (Juan Manrique, Rome, 6 Jan 1554, c. 16r). Not solved.** 282 signs of 65 kinds,
  transcribed in two passes. The siguenza1554 table, applied through a shape mapping, does not fit: 180 of 200 shuffled
  tables score as well or better on a Spanish model. The sign set looks like the same Spanish chancery family, so a
  sibling key is likely; the same table is not. Limit: the siguenza images were not seen, only the sign names in that folder.
- **Lead 1568 (letters to Giuseppe Riva). The 1722 letters use a second table.** WAINUT's separate Selvatico 1719
  submission builds a key from the 1719 letters' interlinear gloss. That key does not decipher Selvatico's four Vienna letters of 1722
  (cc. 21-22, 23-24, 25-26, 35-36) or the undated cc. 2-3 and 14-15: their groups run mostly 50-95, the 1719 alphabet sits
  in 1-35, it covers 33% of the groups as letters and gives no words, and shifts of 30, 50 and 60 give nothing. Two untuned
  annealing runs did not converge. Two sign passes of these letters exist (1497 of 1664 groups agree). Repeated runs for a
  crib: `60 7_ 50 52_ 64_` (three times), `3_ 92 50 81 5`, `6 72_ 80 91`. The five Starhemberg letters in the lead were not worked.
- **Catalogue 1772 and 1773 (Dorffler, Poland).** Not worked. Their catalogue descriptions give 2-3 digit numbers up to
  about 320, so they are not in the 4-digit code of catalogue 1771 (Höpken and Carlson, 1739-41) and do not share its key.
- **Camerarius n. 106** and **Clm 10382 scans 470, 476-477**: rows 19 and 30 above.
- **Gallio to Dandini 1580**: row 0, not started.

## Key leads (keys or decipherments without their own ciphertext)

- **Royal Danish Library, NKS 1416 4to**: "Chiffernøgle til en del danske og fremmede Ministres og Generalers
  Chifferskrift", early 18th century, 55 leaves (Gigas II, 1906, p. 222). A book of keys to Danish and foreign ministers'
  and generals' ciphers. Not digitised as far as the record shows; not in the repo.
- **Estense decipherment sheets** that could read letters already listed:
  - Ercole Gonzaga, sfasc. I, c. 112, "Decifrato di un brano di una lettera", next to Brice Dudout's seven cipher letters at cc. 113-120.
  - Ercole Gonzaga, sfasc. III, cc. 51-53: decipherments of enclosures of 8 and 11 May 1544.
  - Ippolito Capilupi, sfasc. III, cc. 41-42, 47, 48: "probably the decipherment of a cipher passage in a letter of Ippolito
    Capilupi". Worth testing against catalogue 1555 (cc. 80a-80h). Not tested.
  - Francesco I, duca di Modena, c. 147: decipherment of a passage from an unidentified 17th-century letter.
  - Scipione Piattoli, c. 50: names and terms "cifrati o dissimulati sotto pseudonimo" (Poland, about 1790).
  - Gualteruzzi, cc. 57-58r and 63v-76: copies of deciphered letters of Marcello Cervini, June 1540 (clear text only).
- **Jablonski 11,2/14: 62 (24 Jun 1704)**, the letter that sends the key, is kept inside row 11.
- **Clm 10398 n. 63, Clm 10401 n. 139, Clm 10406 n. 74/77, Clm 10382 n. 46**: decipherments with their ciphertext
  (n. 63 and n. 139 are in the separate target submissions; the others are rows here).

## Method

All requests went one at a time, about 1.1 s apart, with a User-Agent naming WAINUT. No logins, no bot checks met
except where noted. No images are in this folder.

- **Estense.** `https://lodovico.medialibrary.it/media/ricercadl.aspx?keywords=<term>&rictip=documenti manoscritti`, paged;
  records at `media/schedadl.aspx?id=<uuid>`; IIIF at `https://edl-jarvis.cultura.gov.it/meta/iiif/<uuid>/manifest`. Terms
  and manuscript hits: cifra 19, cifrata 91, cifrate 1, cifrato 7, cifrati 2, cifre 8, decifrata 17, decifrato 19, decifrati 2,
  decifrazione 6 (133 distinct records); plus the sender folders Saint-Mauris (8), Sande (31), Hurtado de Mendoza (96) and
  Lodron (11). 47 records were already in the catalogue, leads or Dudout's list. Many hits use *cifra* for a digit of a date.
- **Berlin.** Kalliope SRU (about 2,300 records for cipher terms in German, French, Italian and Latin; 56 SBB, 0 HAB) and the
  Handschriftenportal JSON search (44 terms, about 560 objects; 47 SBB, 0 HAB). Most SBB hits were noise (*chiffres* as
  foliation, *Ziffer* as an illegible date digit).
- **Munich.** MDZ full-text search finds printed catalogues; the IIIF content search
  (`https://api.digitale-sammlungen.de/iiif/services/search/v1/<bsbid>?q=<term>`) searches inside one. K. Halm, *Verzeichniss
  der handschriftlichen Sammlung der Camerarii* (1874, bsb11184610), gives 13 entries "in Chiffern" and one "chiffrirt".
  Collectio Camerariana vol. N = Clm 10350+N. Every volume is digitised on MDZ from microfilm.
- **Copenhagen.** Primo public API, manuscripts facet (`soeg.kb.dk/primaws/rest/pub/pnxs`). The old manuscript portal is gone;
  the COP syndication API returns 0 manuscripts for every query.

Scripts are in `scripts/` (standard library; raw hit files were not kept). `scripts/estense/`: `fetch.py`, `harvest.py`,
`records.py`, `manifests.py`. `scripts/hab_sbb/`: `kalliope_sru.py`, `hsp_search.py`. `scripts/bav_kb/`: `fetch.py`,
`kb_cop.py`, `kb_primo.py`, `mdz_catalogues.py`.

## Dead ends and excluded items

- SBB Ms. lat. qu. 157 (two Latin recipes in cipher, key on 69r, solved in place); Ms. germ. oct. 681 (1932); Ms. germ. qu.
  2052 (telegraph codes); Mus.ep. Mozart (known family cipher); Serbian *tajnopis* notes (known system, published).
- BSB Clm 10403 n. 6 (only the signature in cipher); Clm 10379 (cipher numbers only for writers' names); medieval recipe books
  with vowel substitution in the Cgm catalogues.
- KB Copenhagen: "Kongens Chiffer" hits are the royal monogram. GKS 510 fol. (Urban VIII conclaves, "cifra" somewhere in the
  record) was not followed up.

## Not reached

- **HAB Wolfenbüttel**: `diglib.hab.de` and the Braunschweig OPAC timed out on three tries. Heidelberg's images of HAB letters
  served a bot check, so we stopped there.
- SBB digital collections (a JavaScript app with no plain search URL); the full run of Jablonski draft books (11,2/11-17).
- Estense letters with cipher that the record does not mention (the Saint-Mauris folder shows they exist); the "unità
  archivistiche" record type; the cipher leaves of Donati's decipherments.
- Halm's main Clm catalogue beyond the Camerariana and the Cod. gall./ital./hisp. catalogues; a scan-level pass through
  Clm 10375, 10420-10423 and 10431.
- KB printed catalogues (Gigas, Abrahams), served as page images without full text.
