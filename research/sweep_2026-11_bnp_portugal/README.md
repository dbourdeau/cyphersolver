# Biblioteca Nacional de Portugal (BNP, Lisbon) sweep, Nov 2026

Sweep of the BNP for enciphered documents 1350-1950 that are unsolved or possibly unsolved and not yet in the repo.
Brief: `research/archive_sweep_2026-10/BRIEF.md`. Output: `candidates.json` (see counts below). The Portuguese
national archive (Torre do Tombo) was swept separately (`research/torre_do_tombo/`); this sweep covers the national
library only. An earlier pass reached BNP item records only through Manuscriptorium (`research/swiss_austrian/`,
leads 1236-1242: Spinola 1618, Ribeiro Saraiva 1827-31, Correia de Abreu 1731-34, Cascais 1643, the Nisa/Gama
codices, the Motim de Madrid 1766, Luís da Cunha 1742); those are not repeated here.

## Method

| source | route | what it gave |
|---|---|---|
| BNP catalogue (Horizon ipac20) | `https://catalogo.bnportugal.gov.pt/ipac20/ipac.jsp?profile=bn&menu=search&index=.GW&term=<q>` (keyword; `*` truncates, e.g. `cifr*`), `&limitbox_1=COL01+%3D+<RESMAN or RESARQ or RESERV ...>` for a collection, `&page=N` (10 hits a page). Full record: `...&uri=full=3100024~!<bib>~!0`. Stable link `http://id.bnportugal.gov.pt/bib/catbnp/<bib>`. Plain curl with a browser User-Agent works, no session needed | the main source: item-level records of Reservados Manuscritos (COD., MSS., PBA.) and of the archive fonds (Arquivo Tarouca A.T., Fontes Pereira de Melo FPM, Visconde de Santarém PSS, Casa Pombal AP, Almada/Forjaz ALB/ROMA) |
| Manuscriptorium (castor API) | as in `research/swiss_austrian/manu.py`, records with id `BNDPL_*` | the same BNP manuscript records with full notes; re-run with 45 Portuguese/Spanish terms (`manu_bnp.py`) to catch records whose long CONTEM note the Horizon keyword index misses |
| BND (Biblioteca Nacional Digital) | `https://bndigital.bnportugal.gov.pt/records?search=<q>` (`&fulltext=1`, `&refine[Collection][]=Reservados Manuscritos`); item `/records/item/<id>`; viewer `/viewer/<id>/` holds `/api/viewer/lgiiif?url=...`, whose JSON lists every page; page image `/i/?IIIF=/<a>/<b>/<c>/<d>/<uuid>/iiif/<stem>.tif/full/!1800,1800/0/default.jpg` (`bnd.py`) | 5,751 digitised Reservados Manuscritos, but almost none of the cipher items are digitised; the only one is PBA. 614 (viewed) |

Scripts (this folder): `harvest.py` (catalogue keyword x collection -> `hits.jsonl`), `details.py` (full records ->
`details*.jsonl`), `crawl.py` (page a whole fonds and fetch every record), `manu_bnp.py` (Manuscriptorium, BNP only),
`bnd.py` (BND page list and one page image), `show.py` / `summ.py` (cipher mentions in the saved records),
`specs.py` + `build_rows.py` (rows from the records), `addrow.py` (hand-vetted rows). Page images viewed are in the
git-ignored `img/`.

Catalogue terms (all, then each of RESMAN, RESARQ, RESESP, RESERV): cifr* (411 all / 102 RESMAN / 60 RESARQ),
decifr*, contracifra, contra-cifra, chiffr*, dechiffr*, cyfr*, zifr*, cifer*, criptogr*, cryptogr*, steganogr*,
notis, arcan*, caracteres, algarismos, numeros, segredo, secreta, secreto, occult*, chave, clave, alfabeto,
abecedario, abedecedario, jerogl*, hieroglif*, enigma*, sinais (stopped part-way: the server began to return 503s;
carateres and characteres were left out, Manuscriptorium covered characteres). 1,616 hit lines; about 1,350 full
records fetched. Every cipher mention was read in the record.

**The Horizon keyword index misses part of the long CONTEM notes** (COD. 6916, COD. 13553 and the PSS Santarém record
carry "em cifra" but do not come up for `cifr*`). So the fonds that turned out to describe cipher letters volume by
volume were crawled: the Arquivo dos Condes de Tarouca (A.T.: 1,336 records in RESARQ; the 734 with
correspondence-type titles fetched in full, escrituras, certidões, sentenças etc. skipped), the Forjaz papers
(ALB/ROMA, 829 records, 494 fetched) and the Fontes Pereira de Melo archive (FPM, 409 records, 387 fetched). These
crawls found **no cipher record beyond those the keyword search had already returned**: for these fonds the cipher
notes sit in NOTAS or in short CONTEM fields that the index reaches.

Dedup: `known.py` on every name and shelfmark rowed (Tarouca, Alegrete, Corte-Real, Abrantes, Teles da Silva, Nuno da
Cunha, Soure, Santarém, Asseca, Cipriano Ribeiro Freire, Aragón/Segorbe/Gamarra, Barredo, Fontes Pereira de Melo,
Saldanha, Tavares de Andrade, Casa Pombal, PBA. 614, COD. 1617, 2356, 6916, 7212, 13502). None is in the repo or on
DECODE (DECODE holds no BNP record among these), except that the catalogue already has the Torre do Tombo Tarouca
series (catalogue 394, N-V-28, different letters) and Assumar's copy-books.

## Results

`candidates.json`: **62 rows** (1611-1650: 3, 1651-1700: 4, 1701-1800: 47, 1801-1900: 7, 1901-1950: 1; class A 1,
B 42, C 19; `needs_archive_scan` yes 60, partly 1, no 1). 49 of them come from the Arquivo dos Condes de
Tarouca (41 volumes of four series plus 8 single volumes), one row per volume as the BNP catalogues them. One row carries a complete `vetting` block with verdict
`open`: **PBA. 614, f. 33-34v** (scans viewed; passes `vetting_problems` in `docs/_check_catalogue.py`). Every other
row is catalogue-only (`seen: "catalogue"`), since the BNP has not digitised these items. Rows are built by
`build_rows.py` from `specs.py` and the saved records; the PBA. 614, Soure, railway, Aragón, Santarém, Ribeiro Freire
and Goa rows were written by hand (`addrow.py`).

### Best leads

1. **Manuel da Silva SJ, provincial of India → Pedro Barredo SJ, 1759** (PBA. 614, f. [33-34v], Pombalina; BND scans
   pba-614_0067-0070 viewed). A Jesuit provincial's coded orders, copy certified at Tellicherry on 2 Dec 1759 (João
   Lourenço Veloso) and attested by Wm Taylor on 2 Jan 1760, kept in Pombal's own papers. About 30 lines, each a
   margin letter, a run of code groups (numerals, syllables, symbols) and a Latin catchword, under the headings Maim,
   Goa, Hispanha, Inglaterra, Franca. No decipherment on or with it; nothing found in print. Vetting complete
   (verdict open). Possible aid: the Jesuit name cipher found at the Faro college in 1759 (COD. 10566//3, key lead).
2. **The Arquivo dos Condes de Tarouca** (A.T., bought 1971, never on DECODE): 47 volumes of 1681-1737
   correspondence of João Gomes da Silva, 4th conde de Tarouca (plenipotentiary at Utrecht, The Hague and Vienna),
   each catalogued as "partes do texto em cifra": his official copy-books with secretary of state Corte-Real (A.T.
   26//3-22, 1712-37, folios of the cipher letters given for several), his letters to and from his brother the 2nd
   marquês de Alegrete (A.T. 164//2-19 and 163//2-17, 1711-31), the Abrantes (Madrid) exchange of 1726-29 (A.T. 157,
   159), letters to Luís da Cunha (A.T. 165), Corte-Real's despatches (A.T. 109a, 180//2, 180//3), and the
   Heidelberg/Vienna/Madrid embassy volumes 1681-1732 (A.T. 229//1-3). **Key material is in the same library**: the
   Tarouca embassy cipher of 1707-09, "Cifra por que se hade escrever", in COD. 4418, f. 16-23, and "parte da chave
   da cifra" bound in A.T. 164//11. One volume (A.T. 158//2, 1699-1713) carries the decipherments of its cipher
   letters and is left out; it is the place to recover a key. Rows are class B for this reason. None digitised.
3. **António Teles da Silva, governor-general of Brazil, letters from Bahia 1643-48, parts in cipher** (A.T. 128, 5
   documents). Dinnissen & Araújo (HistoCrypt 2022, "Prey to a Privateer") read two of his 1649 ciphers from keys in
   the Nationaal Archief (WIC) and say ciphers were issued in Portuguese Brazil from 1638: those keys come first.
4. **Padre Nuno da Cunha ↔ João IV, Rome 1643-47** (A.T. 140, 31 documents, some text in cipher): the Restoration
   negotiation at the Curia.
5. **João IV and the regency → the 1st conde de Soure, governor of arms in the Alentejo** (COD. 6916, letters
   "algumas em cifra"; original withheld, microfilm F. 731).

Also: Spanish letters of 1669 to Pedro Antonio de Aragón, "muchas estàn en zifra" (COD. 1617, incl. Gamarra and
Fernández del Campo); Cipriano Ribeiro Freire's Madrid letter-book 1801-05, "ofícios (alguns cifrados)" (COD.
7212-7217, marked digitised by the BNP but not public on BND); Santarém → Asseca, a confidential cipher letter of 30
May 1829 (PSS/Cx. 04-Mc. 10, doc. 78); the Goa Vedor da Fazenda letter-book 1745-49 (COD. 2356); Ribeiro Saraiva's
diary 1831-45 with its own key (MSS. 169, n. 13); a 1873 informer's letter and two cipher telegrams of 1859 and
1871 in the Fontes Pereira de Melo archive; the railway company's Paris telegrams of 1894 (COD. 13502); a Casa
Pombal bundle with a cipher piece (AP/Mc. 110); and the composer Carlos Augusto Tavares de Andrade's notebook in an
invented alphabet (EMUS13 27, 1900-30).

### Key leads (keys or tables, no ciphertext rowed)

- **COD. 4418, f. 16-23**: "Cifra por que se hade escrever", the cipher issued to Tarouca with his 1707-09
  instructions for Holland/Utrecht. First key to try on the A.T. rows.
- **A.T. 164//11** (1721-22): "parte da chave da cifra (?)" bound with Tarouca's letters to Alegrete.
- **A.T. 158//2** (1699-1713): cipher letters with their decipherments (f. 45-47, 54-55, 71-72, 77-79, 85-86, 92-93,
  106-107v, 113-117, 149-151, 154-155v, 183, 188, 220-222, 227-228, 324): a key can be rebuilt from the pairs.
- **MSS. 201, n. 26, f. 20**: a 20th-c. copy of Luís Álvares Ribeiro's letters from The Hague, Jun-Jul 1659, to
  Francisco de Melo, "uma cifra na f. 20 para decifração de algumas cartas": the key of the Torre do Tombo MMCG
  Álvares Ribeiro letters (Torre do Tombo sweep, best lead 4). Also MSS. 206, n. 108 (copies of his Aug-Sep 1659
  letters).
- **COD. 10566//3**: "Cifra de nomes antigos" found in the letter-book of the Jesuit college at Faro, 1759, a code
  dictionary the Jesuits used between houses.
- **MSS. 223, n. 29**: "Abedecedario con que ha de entenderse y escribirse la cifra", Spanish, 1750-1801, 4 f.
- **MSS. 169, n. 13**: "[Cifra do diário]", the key of António Ribeiro Saraiva's diary (rowed with the diary).
- **COD. 9193, doc. 12**: the cipher used by the Miguelist Junta and the guerrilla leader Remexido (1830s), in a
  report on Miguelist plots.
- **ALB/ROMA/32310-32429**: "cifra de alfabeto" and "Instruções para cifrar com a carta alfabética" (c. 1810-11,
  papers of Miguel Pereira Forjaz, secretary of war).
- **ALB/ROMA/25012-25016**: "Documentação sobre cifras, com nota explicativa e cadernos de cifrante e decifrante",
  Palmela and others to Forjaz, 1818-20.
- **COD. 1806, f. 154-158**: a "Cifra" interleaved with a paper of D. João da Silva to Pedro II (late 17th c.).
- **COD. 13553, f. 56v-57**: "segredo para se escrever em cifra" (a recipe, after 1754).
- **MSS. 146, n. 840**: Serpa Pinto to the governor-general of Mozambique on the telegraph ciphers (1890 ultimatum).

### Notes for the existing BNP leads (1236-1242)

- None of them is digitised: the catalogue records list no BND copy (COD. 7164 and PBA. 636 are on microfilm F.R.
  220 and F. 3236). They stay `needs_archive_scan: yes`.
- Lead 1240 (Nisa codices): COD. 7162's record cites Delfim de Sousa Correlo, *Estudos das cartas em cifra de El-Rei
  D. João IV ao Conde da Vidigueira* (Estado-Maior do Exército, 1970; BNP P. 3844 V.), a 22-page study of exactly
  these ciphers; it must be read before that lead (and the Torre do Tombo MSLIV 1016/1017 rows) count as open.
- MSS. 13, n. 19-23 (cipher plus decipherment pairs, 1643) and MSS. 41, n. 3 / n. 5 doc. 1 (Zúñiga 1613, Spinola
  1614, with contemporary decipherments) were rightly left out as read; they give keys for the siblings.

### Left out

- Items with their decipherment: A.T. 158//2; COD. 4419 and COD. 6441 (Cunha Brochado, "Cartas em cifra ...
  decifradas"); COD. 8721 (Sousa Coutinho, Turin 1799-1801, "Chifra Nº 2/3" with clear text); FPM-Cx. 02, n. 161 and
  n. 180 (telegrams "em cifra e respectivas traduções").
- MSS. 23, n. 27, doc. 8 (1735): a covering letter about a cipher letter sent via "Guilherme Mamon"; the cipher letter
  itself is not in the item.
- Music: hundreds of hits for cifra = figured bass or tablature (EMUS11 489, 1081, M.M. ...); "assinatura não
  decifrada" (illegible signatures, MSS. 146 Ennes letters); charades "com a decifração" (COD. 600, COD. 589//13);
  printed cryptography manuals ("Cifra maravilhosa", 1851).

## Not reached / blockers

- The BNP server slowed and returned 503/504 when three request streams ran at once; one stream at about one request
  a second works. The keyword harvest was stopped during "sinais".
- Records with non-correspondence titles in the crawled fonds (about 600 A.T. deeds, certificates and sentences,
  335 Forjaz and 22 FPM records) were not fetched. Other archive fonds of the BNP (Arquivo Reservados: Casa Pombal
  AP, Visconde de Santarém PSS, Lavradio, Barca, Sousa Coutinho ...) were reached only through the keyword search,
  not crawled; the Manuscritos Reservados (COD., MSS., PBA.) were reached through the keyword search and
  Manuscriptorium, not crawled (tens of thousands of records).
- No catalogue item except PBA. 614 has public scans, so the other rows cannot be vetted from here: the BNP
  Reservados reading room or a reproduction order is needed (most items "Reservado, sob autorização"; COD. 6916,
  7212, PBA. 614 originals "Sem acesso").
- Not checked: the printed *Correspondência do 2.º Visconde de Santarém* (for the 1829 Asseca letter), Correlo 1970,
  the Tempos Históricos 2019 article on Nuno da Cunha, Graça Sousa's 2022 Évora thesis (Soure letters).

## Merge and vetting (main session, 5 Nov 2026)

The sweep's 62 per-volume rows are kept in `candidates_volumes.json`. `consolidate_vet.py` folded three Tarouca series
into one row each, as catalogue #394 does for the Torre do Tombo Tarouca series: the Corte-Real copy-books (A.T. 26,
16 volumes), the Alegrete ↔ Tarouca letters (A.T. 163 + 164, 22 volumes, one correspondence and one key) and the
embassy volumes (A.T. 229, 3 volumes). The result is 24 rows in `candidates.json`. The script also wrote "not online"
vetting blocks from this session's checks:

- PBA. 614 (scans viewed): code groups with Latin catchwords, no decipherment.
- Ackel 2025 (*LaborHistórico* 11) and Dinnissen & Araújo 2022 study only the 1649 Teles da Silva ciphers in the
  Hague WIC papers, not A.T. 128.
- Gatti 2019 (*Tempos Históricos* 23) on Nuno da Cunha cites Ajuda and Vatican codices, not A.T. 140, and quotes no cipher.
- No study of the Tarouca ciphers was found. Cluny, *O Conde de Tarouca e a diplomacia na época moderna* (2006), uses
  the archive and was not seen.

Merged as leads 2261-2284 (and KB lead 2285). Promoted to the catalogue: 2261-2264, 2266-2269, 2272, 2273, 2276-2284
(19 entries). The other five rows were kept as leads because they did not meet the vetting bar:

| Lead | Item | Why not promoted |
|---|---|---|
| 2265 | Santarém → Asseca 1829 | the printed Santarém correspondence is unchecked |
| 2270 | Ribeiro Saraiva diary | only the key is described |
| 2271 | FPM letter of 1873 | name letters (Z, O), not a ciphertext |
| 2274 | Tavares de Andrade notebook | the catalogue summarises the content, so the cataloguer may have read it |
| 2275 | Casa Pombal AP/Mc. 110 | which of the 761 folios carries cipher is not stated |
