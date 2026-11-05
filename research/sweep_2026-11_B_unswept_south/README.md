# Sweep B, unswept south (4 Nov 2026): Dubrovnik/Balkans, Turin, Genoa, Naples, Palermo, Rome (ARSI, Propaganda), Malta

Scope from the coordinating session: the archives `research/COVERAGE.md` lists as never swept. Nothing outside this folder was edited;
no commit. Rows are leads (`candidates.json`, 21 rows, schema of the Oct 2026 BRIEF, ids assigned at merge), all `seen: catalogue`:
none was viewed on an image, because none of the holders' own sites could be reached.

**Result: 21 rows (6 of them pre-1500), 74 Genoese key leads (TSV), about 25 further key and trivial-cipher notes.** The yield is thin where the archives are
walled (Dubrovnik, Malta, Propaganda: 0 rows) and surprisingly useful from two side doors: the **ICCU Manus Online API** (manuscripts in
Italian libraries, including the Gregorian University's Council of Trent volumes) and the **Wayback Machine as a proxy for the blocked
`*.cultura.gov.it` inventory PDFs** (Genoa, Palermo; Turin partly).

## Route test log (4 Nov 2026, this machine)

| Host | Result |
|---|---|
| `*.cultura.gov.it` and `*.beniculturali.it` (Turin, Genoa, Naples, Palermo, SIUSA, `inventari-san`, `sias-archivi`, `san.beniculturali.it`, `dati.beniculturali.it`, `archivi.beniculturali.it`) | curl: timeout 12-15 s or immediate reset. Chrome (own tab, Turin): fell back to `chrome://newtab`, `get_page_text` refused. **WebFetch also gets `ECONNRESET`**, so it is not just this network: the hosts refuse non-Italian clients or are down. `www.archiviodistatonapoli.it` answers 301 but redirects to the blocked host. Retried once as asked; still out. |
| `web.archive.org` (CDX API + `/web/<ts>if_/<url>`) | **Works as a proxy** when a snapshot exists: 177 Genoa inventory PDFs, 355 old-host Turin PDFs, 892 Palermo (`saassipa`) PDFs, 39 Naples (all admin, no inventories). Not archived: Turin "Lettere ministri" and "Negoziazioni" inventories (the PDFs the search engines show). Rate limit: 429 after about 40 requests in a few minutes; one request per 6-8 s with 45 s back-off is fine. Several Turin `Inventario_NNN.pdf` are image scans (no text layer). Script: `wb_grep.py`. |
| Manus Online (`manus.iccu.sbn.it`) | **Works with curl**: `POST /o/manus-api/titles-search-post` (form fields `monocampo`, `n=v`, `monocampo:tipo=ONLY`, `page`) and `GET /o/manus-api/title?id=<id>` for the full record (the HTML detail page is JS only). The Venice sweep had used it for Venice records only. Scripts: `manus_all.py`, `manus_detail.py`, `manus_detail_ids.py`. |
| `arsi.jesuits.global` | Answers; publishes five PDFs (summary inventories of Antica and Nuova Compagnia, Fondo Gesuitico Generale, index of fonds, Danieluk article). Grepped: one hit (below). No item-level catalogue. |
| `vhmml.org` | Record pages `/readingRoom/view/<id>` **open in Chrome with no Turnstile** (the Turnstile sits on the search form). The Malta AOM series 9 records (AOM 1200-1648) are volume-level with one shared series summary, so cipher cannot be searched; thumbnails exist (`/image/thumbnail/READING_ROOM/NLM AOM 01201/...`). A search by term needs a person to pass Turnstile. |
| `dad.hr` (Dubrovnik State Archives) | 200; WordPress; annual plans and reports only, no item-level catalogue. `arhivdubrovnik.hr`, `arhinet.arhiv.hr` do not resolve. |
| `hrcak.srce.hr` | Chrome shows a "move your mouse" interstitial ("Confirm you're not a robot"); not passed (rule). WebFetch of its PDFs: HTTP 418. |
| `archive.org` full text (`services/search/beta/page_production?service_backend=fts`) | Works but page-level; two-term queries match different pages of one book (the "Lettere di Levante" hit in a Hungarian book proved to be a false lead: spying duties of Ragusa, not cipher). |
| Google Books API | `429`, daily quota 0 without a key. |
| OPenn (Penn) | curl works for the HTML page; WebFetch times out. |
| `openn`, `memoriedigitaliliguri.it`, `um.edu.mt` | answer. |

## Terms and counts

* **Manus** (mode ONLY, exact word or phrase): cifra (862 records), cifrario, cifrari, cifrata/o/e/i, decifrazione, decifrata/o, in cifra (93), lettere in cifra, lettere cifrate, scrittura cifrata/segreta, alfabeto cifrato, crittografia, zifra, zifre, nomenclatore, segni convenzionali, cifre (3,447) and in cifre (2,746) (both numeral noise, capped at 60 pages and not screened), and 12 others that returned 0-7. 2,426 records harvested; **detail records read for 506** (all Roman, Neapolitan, Genoese, Palermitan, Turin, Trieste, Cagliari, Monreale, Messina, Catania, Aosta, Cassino, Perugia, Arezzo, Ferrara, Pisa, Cesena, Trento, Padova, Prato, Bologna, Parma, Cremona, Brescia, Bari, Campobasso, Milan, Mantua, Modena records and all hits of the specific terms). Not read: the 349 Bergamo and 241 Florence hits matched by "cifra" alone (Bergamo's catalogue uses "cifra" for numerals; the Florence ones are the Carte Machiavelli (other sweeps cover them; their cipher passages carry Machiavelli's own interlinear decipherments) and Ginori Conti 29, whose 19 records were read and gave the rows above). About 55 genuine cipher mentions remained; 8 became rows here, the rest are key leads or trivial.
* **Wayback inventories**: 28 Genoa PDFs (11 Instructiones, 31 Trattati, 32 Buste Paesi, 34 Archivio Segreto, 41bis Manoscritti restituiti dalla Francia, 26 Pandetta, 79 Fieschi and others; five over 5 MB skipped), 20 Palermo, about 12 Turin; terms cifr, decifr, chiffr, cipher, zifra.
* **Web searches** (about 25, English, Italian, Croatian): Ragusa/Dubrovnik, Zrinski-Frankopan, Slovenia, Zadar/Kotor, Savoy, Genoa, Palermo, ARSI, Propaganda Fide, Malta AOM, Contarini, Cervini, Zacchia, Ubaldini, Varia 244. Nothing on any cipher in the Dubrovnik, Malta or Propaganda archives.
* `known.py` run on every shelfmark and correspondent before a row was written (hits listed in each row's `prior_art`).

## Ranked leads (rows)

1. **APUG (Concilio di Trento) 690rec, 1546-47**: G. B. Cervini (Rome) -> Cardinal Marcello Cervini at Trent, 83-leaf register "Lettere in cifra", cipher list on f. 83r. https://manus.iccu.sbn.it/o/manus-api/title?id=724628
2. **BNCF Ginori Conti 29.132, .125bis, .136 (1484-1490), .104 (1492), .141, .137: Medici-circle letters with cipher, images online** at `teca.bncf.firenze.sbn.it` (ids in each row). **Oldest, and the only rows of the sweep with open images.** Not in the repo before (the Venice sweep listed the Manus hits without making rows). The key sheets of the same fund (29.114.a, below) are a ready key lead.
3. **APUG Concilio di Trento 242rec, 1541**: Contarini -> Farnese from Regensburg, 34 copied despatches, cipher at pp. 172-173, 180 (oldest ciphertext of the sweep). id 750696
4. **Casanatense Ms. 1309, 1621**: Zacchia (Venice) -> Ludovisi, register with cipher lines and enciphered names; **sibling copy Penn Ms. Codex 553 is open on OPenn**. https://openn.library.upenn.edu/Data/0002/html/mscodex553.html
5. **Turin, Biblioteca Reale, Varia 244, 1704-06**: Ottoboni/Naples immunities, cipher letters with the decipherment scheme on c. 172 (key and text in one volume). id 1871606
6. **BAV Vat. lat. 14673 cc. 122r-129v, 1606**: eight cipher letters of Roberto Ubaldini (pointer from the Rome BNC record; DigiVatLib not reachable).
7. **ASPa Miscellanea archivistica I serie b. 68 and I.67, 1848-49**: Sicilian revolutionary government's cipher with versions attached (cipher/clear pairs).
8. **APUG 608rec, 588rec, 1562-63**: Trent bundles with "Cifra sopra il luogo del conte di Luna" (13 ff.) and "cifre a parte" (cc. 243-253).
9. **Moreniana Bigazzi 303**: second copy of the intercepted Bichi letter already in the catalogue as 1345.
10. **ASTo 1588**: Charles Emmanuel I's second, cipher instruction to Secretary Corte at Rome (Bianchi 1876).
11. **BNC Gesuitico 204**, **ASGe Spagna mazzo 76**, **ASGe Manoscritti restituiti dalla Francia** (16 volumes of the Paris legation 1746-94 with cipher and two keys), **BU Bologna Marsili 75/C c. 91**.

## Key leads (keys and tables, no ciphertext; they unlock ciphertext elsewhere)

* **ASGe Archivio Segreto, Materie politiche, Instructiones et relationes (n. 2707)**: 74 cipher keys given to Genoese envoys and governors, 1467-1694, listed in `key_leads_genova_instructiones.tsv` (date and description from inventory n. 11, Wayback copy). **Pre-1500, with a ciphertext partner in Milan** (Genoa was under Sforza governors 1464-78, so the governors' letters to Milan sit in ASMi Potenze estere/Genova and on DECODE Sforzesco): 2707 B 9 (18 Apr 1467, Sagramoro Visconti to Giovanni Giustiniani and G. F. Spinola at Milan, instructions with cifrario), B 15 (cifrario naming the Venetians, the people of Milan, the King of France and the Florentines), B 15 bis, B 20 (4 Sep 1469, Corrado di Fogliano to Bracelli and Doria at Venice), B 57 (30 Aug 1475, Chios question, to Milan), B 71 (9 Jan 1477, credentials and cifrario, envoy to the Pope), B 142 (19 Feb 1485, cifrario for the envoys to Rome), B 176 (27 Jun 1493, Chios). Later: C 11 (1502 Spain), C 93 (18 Mar 1511, Alessandro Lercari to the Sultan of Egypt), and a run to 1694.
* **BNCF Ginori Conti 29.114.a, Florence (15th c.): a bundle of cipher key sheets** - a general cifrario (alphabet, double letters, abbreviations, names of eminent Florentines, offices, a word list: artiglierie = 'prudenzia', vettovaglie = 'vita'), two sheets of the **Otto di Pratica** ("Cifre dell'octo"), one of the **Dieci di Balia** ("Cifra de X di Balia"), one marked "Di [...] Lorenzo", and one with syllables; images at https://teca.bncf.firenze.sbn.it/ImageViewer/servlet/ImageViewer?idr=BNCF0003826932. Date not given (Lorenzo's time). Also 29.138 (Lorenzo to Guidantonio Vespucci, 22 Jun 1479) carries a contemporary note "Ex cifre Laurentii de Medicis ... Cirferatura di lett(ere) di L(orenz)o de Medici", i.e. a decipherment copy; 29.111 (Ridolfi to Soderini, 1507-08) has an interlinear decipherment in another hand; 29.41 (1513) mentions four ciphered originals from Blois.
* ASGe inventory 31 (Trattati): cifre/cifrari at nos. 229, 237, 249 (Viganego, Turin), 294, 299 (1691). ASGe inventory 34: "Cifrarii di istruzioni" (Materie politiche mazzo 9 A); the general guide `Genova.pdf` lists "Raccolta cifrari" b. 1 and "Istruzioni del governo ai suoi ministri" bb. 10 (1350-1798) with an inventory of the cipher collection; Lettere Ministri Francia mazzo 79 ("Cifrari per il Ministro", 1772), Inghilterra 17 A, Olanda mazzo 5.
* ASGe, Diversorum Communis Ianue filze 3021-3130 (to 1528): "lettere patenti, cifrari e istruzioni" (Instructiones inventory); Airaldi, "Paleografia e criptografia nella storia genovese del Quattrocento", *Studi e documenti su Genova e l'Oltremare* (1974), pp. 111-152, is the study to read first (not found online).
* **ARSI, Fondo Gesuitico 679, Theca 4a, no. 21: "Cifraria S. I., s. XVI-XVII"** (Fondo-Gesuitico-Generale.pdf, line 2057): Jesuit cipher key(s) of the 16th-17th c., not online.
* Manus: Rome Angelica ms. 1888 (16th c., cc. 18v-19v and 22v-25v "Zifra Philippi Prevot canonici et archidiaconi ... cabilonensis"); Cascia Ms. 4 c. 337r (key, vowels to figures 1-5, 1576-1625); San Severino Marche ms. 20 cc. 66r-68v (cifrario of Virgilio Puccitelli, secretary of Wladyslaw IV of Poland, with a 19th-c. explanation); Brescia Queriniana I.IV.28 (1707, key sheet for "caratteri o Zifre" of princes); Pavia Aldini 159 (1733 Venetian ducal commission naming "Zifra piccola"); Prato Roncioniana U.IV.12 ("Cifra della Corte di Roma discifrata da Urbano VIII", 18th-c. copy, 6 ff.); Genoa BU ms. G.IV.8 (two cifrari, pp. 188-191, 1651-1700); Milan Ambrosiana G 309(32) inf. cc. 43v-52r (Federico Borromeo, "schemi di scritture cifrate"); Milan Trivulzio 2246 ("Extractus Zifre ... Domini Vincancellari ad Illustrissimum Ducem Mediolani", 13 Feb 1499; Milan sweeps); Naples BNN XII.E.57 (1739 manual of 48 cipher alphabets).
* Turin ASTo, Carte Nicomede Bianchi: a "matrice per la corrispondenza in cifra del 1859 Matteucci, inviato a Berlino" and a cipher minute to Count Balbo at Madrid (14 Jan 1818).

## Dead ends and already read

* Naples ASN: DECODE's whole ASN block (R9532-R9590, 59 records, 1790-1869) is either in the repo (Castelcicala target) or DECODE status Decrypted; R9542-R9548 (Naples-Vienna 1790-98) are "Decrypted" on DECODE yet "open" on Cryptoole, so they are a read-from-existing-decipherment task, not an open cipher.
* Genoa Diocesan Archive 1422 (DECODE R2791): Decrypted. Trivial vowel-shift colophon ciphers, not texts: Ferrara Ariostea Cl. I 215, Pisa Cathariniana 156 (1441-60), Vallicelliana B 116, Florence Palatino 504 (1475), Turin BNU Nuove accessioni TIV2 (1450), Ambrosiana A 118 inf. (catalogue 1347), Rovereto ms. 20, Bergamo MMB 210.
* Turin, Carte Nicomede Bianchi: Kossuth's ten partly ciphered letters to Giuseppe Carosini (1849-51) were deciphered by L. Hegedus and printed in *Budapesti Szemle* 1934.
* Palermo: the 19th-century "Repertorio Luogotenenziale" series carry no cipher mention; "Percorso-Cifrari" is a school worksheet.
* Dubrovnik/Zagreb/Ljubljana: web searches (English, Italian, Croatian) found only the Vrancic literature already in the repo; the Zrinski-Frankopan conspiracy ciphers are not documented online. Ragusa as a relay for Habsburg despatches (1685) is in Kerekes's book, not a cipher source.
* Cardinal Alemanni "segretario della Cifra" volumes (Corsini 188, 190, 193): office name only.

## What remains (and how)

* **Dubrovnik** (Lettere di Levante/Ponente, Litterae et commissiones, Diplomata, Zadar, Kotor): no item-level catalogue reachable. Next: the Croatica 2018 survey of Croatian cryptography and Polic Bobic, "Tajna diplomacija u Dubrovniku u XVI. stoljecu" (2011), via Hrcak with a person passing its interstitial; ask DAD whether it holds "šifra" bundles.
* **Malta**: vHMML view pages open but are volume-level; the only route to a cipher letter is a person searching Turnstile-protected vHMML by term, or Malcolm, *Agents of Empire* (2015; archive.org lending copy, `agentsofempirekn0000malc`) read by hand.
* **Propaganda Fide**: no online inventory found; Kowalsky's inventory not on archive.org.
* **ARSI** item level (Epistolae Externorum, Hisp., Ital.): none online. The MHSI volumes on archive.org print letters with "(in cifra)" marks; a volume-by-volume grep is the next step.
* **Turin**: the "Lettere ministri" and "Negoziazioni" PDFs are not in the Wayback; of the old-host Turin PDFs only 8 had a text layer and were read (Calderini, Bianchi papers, Coardi, Entremont, Inventario 207 and others; one real mention, the Bianchi papers' 1859 and 1818 cipher items); `Inventario_100.1/101/117.1/130.1/131/133` are image-only scans, and the n. 180 (Lettere Principi, Duchi e Sovrani) and Lettere Cardinali inventories were not reached before the Wayback rate limit stopped the run (stopped by hand at the end of the session). **Naples**: no ASN item-level inventory in the Wayback.
* **Manus**: rerun after the Florence sweep if Bergamo/Firenze "cifra" hits matter; the 3,447 "cifre" and 2,746 "in cifre" sets were not read.
* DigiVatLib (Vat. lat. 14673) needs another network.
* Suggested COVERAGE.md edits (not made): move Turin/Genoa/Palermo from "never swept" to "swept at inventory level via Wayback, ciphertext not itemised"; Rome (ARSI) to "finding aids grepped, one key"; Malta to "volume level only".

## Files here

`candidates.json` (21 rows), `make_candidates.py` (source of the rows), `key_leads_genova_instructiones.tsv` (74 keys), `fts.py` (archive.org full-text helper), `wb_grep.py` (Wayback PDF fetch and grep), `manus_all.py`, `manus_detail.py`, `manus_detail_ids.py` (Manus harvest and detail), `battery1.py`. Downloads, Wayback text, Manus JSON and raw full-text hits are in git-ignored `_dl/` and `raw_hits.jsonl`.
