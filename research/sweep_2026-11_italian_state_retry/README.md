# Italian state archives retry (6 Nov 2026)

Retry of the `*.cultura.gov.it` hosts that `research/COVERAGE.md` lists as blocked (connection refused / timeout on 26 Oct,
28 Oct and 2 Nov). curl only, browser User-Agent, no Chrome in this run. Finished 6 Nov 2026, 08:20 UTC.

## Host status (curl, 6 Nov 2026, 07:53 UTC, first attempt)
| Host | Answer |
|---|---|
| www.cultura.gov.it | 301 -> cultura.gov.it (up) |
| archiviodistatofirenze.cultura.gov.it | 302 -> /asfi/ (up, home page 53 KB) |
| archiviodistatomilano.cultura.gov.it | 307 -> /home (up) |
| archiviodistatomantova.cultura.gov.it | 307 -> /home (up) |
| asmo.cultura.gov.it (Modena) | 307 -> /home (up) |
| archiviodistatocremona.cultura.gov.it | 200 (up, slow, 6.7 s) |
| siusa-archivi.cultura.gov.it | 302 -> archivinazionali.cultura.gov.it/it/ (SIUSA is now folded into Archivi Nazionali) |
| inventari-san.cultura.gov.it | 302 -> archivinazionali.cultura.gov.it/it/ |
| antenati.cultura.gov.it | 403 (CloudFront; bot check, not tried further) |
| archiviodistatotorino.cultura.gov.it | 200 (up) |
| archiviodistatogenova.cultura.gov.it | 307 -> /home (up) |
| archivi.cultura.gov.it | 307 -> /home (up) |
| www.archiviodistatovenezia.it | 301 -> /it/ (up) |
| www.archiviodistatofirenze.it | no DNS / no answer (not a real host) |

**The outage is over**: every `cultura.gov.it` host answered at the first attempt from this machine on 6 Nov.

## Florence (ASF): Mediceo avanti il Principato (MAP)

Route that works (curl, no login, no bot check):
- MAP viewer: `https://archiviodistatofirenze.cultura.gov.it/map/ricerca/ricerca-su-filza/?f=<filza>&d=<doc>&c=` redirects to
  `.../map/riproduzione/?id=<n>`; the page lists every image of the filza (`<li id="rip_<id>">doc. N r</li>`) and names the
  IIPImage file of the current one (`/data/iip-data/asfi/mediceo_avanti_principato/001000FF/A0000NNN.ptif`, FF = filza,
  NNN = position in the filza). Image id = first id of the filza + position - 1, so one page maps a whole filza.
- Images (IIIF 2, 1600 px max): `https://archiviodistatofirenze.cultura.gov.it/iipsrv/iipsrv.fcgi?IIIF=<ptif path>/full/full/0/default.jpg`.
- The printed MAP inventory (Morandini/d'Addario, 4 vols) is only page images on the ASF site, but **vols 1-3 (filze 1-100)
  have OCR text on archive.org** (`archivio-mediceo-avanti-il-principato.-inventario.-vol.-1`, `-vol.-2`, `-vol.-3_marc`,
  `*_djvu.txt`). Vol. 4 (filze 101-165, 1963) is not on archive.org; not text-searched.
- Script: `mapdoc.py <filza> <doc>` (scratchpad, not committed) downloads the images of one document.

Inventory grep (cifr/cifer/zifr/decifr/chiave/caratter, vols 1-3): about 40 cipher mentions in 9 filze. Most are letters with
their contemporary "decifrato" filed beside them (F. LXXII 1514-15 nos. 315/316, 330/331, 338/339, 320/321, 341, 343;
F. LXXIV-LXXV Lyon/Vigevano 1493-94 nos. 30/90, 32/31, 33/34, 35/36, 37/46, 40/41, 42/43, 51/47) and were not opened.
Keys (not rows): F. LXXII nos. 178-188 (Piero Alamanni; ser Andrea da Bologna; Baccio Ugolini; "Averardo con Astore";
Paolantonio Soderini; Agostino Biliotti and Lionetto; Andrea Cambini; "Diverse cifre"); F. LXXXII n. 142 (c. 443, names and
pseudonyms) and n. 72 (cc. 437-457, "Cifrario"); F. LXXXVII n. 414 (c. 551, Piero Capponi - Pier Vettori); F. XCVII n. 473
(Carlo Altoviti).

### MAP documents opened (images seen, 6 Nov 2026)
| Filza / doc | Inventory | Seen | Verdict |
|---|---|---|---|
| 89 / 142 (riproduzione id 94455-56) | "Giovanni Mazzinghi (cifrato). s.l., 1478 gen. 16" | yes, 1600 px | one full page of cipher with a few clear words; dated "+ ... di gennaio 1478" at the head; verso endorsed "1478 ... adi 16 di gennaio ... Gio. Mazinghi" and "Cifra". **Bare** (no interlinear, nothing beside it). Row 1. |
| 72 / 170 (id 79506-07) | "Anonimo (in cifra), ad anonimo. s.l., 1478 gen. 23" | yes, 1600 px | **same sign set as 89/142** (x, ‡, H, =, 5-like signs), one page, "+ ... di gennaio 1478"; **interlinear decipherment** in a second hand over almost every cipher run (Rome news: papa, palagio, Girolamo, conte ...). Key source for 89/142. Row 2. |
| 48 / 214 (id 60059-60) | "Documento cifrato. s.d." (filza XLVIII, 1482-83) | yes, 1600 px | ~20 lines, all cipher except "Poi ... 87"; symbol substitution with numerals; no date, no address, verso blank. **Bare.** Row 3. (The OCR printed this under filza XLVII; the page is in XLVIII; F47/214 is a clear letter of Ercole d'Este, 1473.) |
| 72 / 213, 214 (id 79620-23) | "Lettere in cifra" | yes, 800 px | two slips, all cipher (Greek-like signs, numerals, //), same sign set, no clear word, versos blank. **Bare.** Different sign set from 72/207. Row 4. |
| 73 / 371 (id 81019-20) | "Poscritto in cifra. s.d." | yes, 800 px | 8-line cipher postscript ending in a few clear words; verso blank. **Bare.** Row 5. |
| 17 / 211 (id 19271-72) | "Piero di Lorenzo Medici, ad un ambasciatore fiorentino presso il Re di Francia. (In parte in cifra), s.d." | yes, 1364 px (max) | two pages of cursive with only short code groups in the text (e.g. "zzz7?te"); dated at the foot "... 1459" or "1499" (unclear at this size). No gloss seen. Row 6, low. |
| 72 / 207 + 208 | Bernardo Rucellai, Milan 1482, and "Decifrato della n. 207" | yes | 207: clear opening and close, ~16 lines of dense cipher; 208: clear decipherment (Lodovico Sforza, Ascanio's return, Bernardo Largamente ...), ~10 lines, so possibly partial. Read at the time; not a row (key rebuild exercise only). |
| 73 / 354 | "Copia di cifrato" | yes | clear text only (a decipherment: the pope, messer Anello, the Genoese); not a cipher. |
| 75 / 106 | "Poscritto in cifra ad una lettera, con decifrato" | yes | 6 cipher lines with the clear decipherment written below; read at the time; not a row. |

Prior art: known.py finds nothing for Mazzinghi, MAP 89, MAP 72, MAP 48 or Rucellai; the only MAP hits are the inventory pointers in
`targets/medici1425` and `research/medici_bia` (Marco Vito's project on encrypted MAP letters of 1486-1491, "not yet decrypted":
it may overlap rows 3-5 if they date from 1486-91; check before working them). Google Books feed: the 1478 items appear only in the
inventory itself. DECODE, Tomokiyo and Lasry not searched in this run.

## Other hosts (all answered; 07:53-08:15 UTC)
| Archive | What is online | Result |
|---|---|---|
| **Modena** (asmo.cultura.gov.it) | Guida generale PDF (already read 2 Nov via Wayback); "Patrimonio online" lists only maps, herbal, gridario. ARCE (Archivio Ricerche Carteggi Estensi, `arce.beniculturali.it`), linked as the Este correspondence collection, has **no DNS** (also tried `arce.cultura.gov.it`). | No item-level inventory and no letter images online. 0 rows. |
| **Mantua** (archiviodistatomantova.cultura.gov.it) | `fileadmin/risorse/Inventari/Archivio_Gonzaga_2020.pdf` (220 pp., busta list, text layer). grep cifr/zifr/chiav: buste 423-425 = E.I.2 "Cifre sciolte ... A-L", "M-Z", "Cifre in libri" (keys, already a key lead in `italian_catalogues`). Torelli 1920 and Luzio 1922 PDFs on accademianazionalevirgiliana.org (not read). | Busta level only, no images. 0 rows. |
| **Milan** (archiviodistatomilano.cultura.gov.it) | inventories now direct under `/fileadmin/risorse/Patrimonio_archivistico/Fondi_e_Inventari/` (no Wayback needed). Digitised series moved to the **ICAR Archivio Digitale**: `archiviodigitale-icar.cultura.gov.it/it/183/istituto/82/` lists Carteggio Sforzesco (Carteggio interno + **Potenze sovrane**, incl. "Cancelleria segreta. Chiavi e cifrari"), Registri delle missive, Registri ducali, Cancellerie dello Stato. Unit records read by curl, e.g. scat. 1591 = `.../ricerca/detail/1128459` (82 cc., 1494-1736, same description as the 2 Nov Milan sweep), scat. 1458 = `.../detail/1020319`. Sub-level search: `ajax.php?pageId=185&ajaxTarget=Page&action=&controllerName=metacms_modules_solr_controllers_ajax_SolrSearchSubLevel&parentId=<id>&text=<term>&page=N` (direct children only). | The unit pages carry **no image link or viewer in the HTML** served to curl; the viewer is probably JS-loaded. **needs Chrome: https://archiviodigitale-icar.cultura.gov.it/it/185/ricerca/detail/1128459** (scat. 1591, the Italian-Wars cipher letters of the 2 Nov Milan row) and `.../detail/1020319` (scat. 1458 cipher lines). 0 new rows. |
| **Genoa** (archiviodistatogenova.cultura.gov.it) | `fileadmin/risorse/pdf/34_ArchivioSegreto202003.pdf` (176 pp., text layer). grep cifr: Lettere Ministri Francia 2256 (cifrari 1772), Inghilterra 2289 A (lettere e cifre del Governo al ministro Ageno 1761-63), Napoli 2332 (Casale/Molinelli letters and cifrario 1763), Spagna 2485 (Celesia, "lettere in cifre" 1795-97), Materie politiche 2716 A (cifrari di istruzioni, undated). Archivio digitale holds Archivio Segreto *Manuali-Decreti* and *Materie politiche*, not Lettere ministri. | Mazzo level, not digitised. Description-only leads listed here, not rows. |
| **Turin** (archiviodistatotorino.cultura.gov.it) | Banca dati `/Patrimonio`, `/digital-library/`, `/dbadd/dlredi.php?i=2`: **403 "Verifica del browser in corso"** (JS bot check, also on the `.beniculturali.it` mirror). | **needs Chrome: https://archiviodistatotorino.cultura.gov.it/Patrimonio** (search "Lettere ministri", "cifra"). 0 rows. |
| **Archivi Nazionali** (ex-SIUSA/SAN, archivinazionali.cultura.gov.it) | Liferay portal; `/it/risultati-di-ricerca?search=<term>` returns a page whose results are JS-rendered (no hits in the HTML); a Mirador viewer is bundled. | Endpoint not captured. needs Chrome (or XHR capture): `https://archivinazionali.cultura.gov.it/it/risultati-di-ricerca?search=cifra`. |
| Cremona | home page answers (200, slow). | Not swept (no cipher fonds known). |
| Venice ASVe | answers (301). | Not re-swept: `research/venice_archives` covered it on 28 Oct when it was up. |
| Antenati | 403 (CloudFront). | Not relevant (civil registers). |

## Terms and counts
- MAP inventory OCR (vols 1-3, 2.8 MB text): regex `cifr|cifer|zifr|ziffr|decifr|chiave|caratter` -> about 40 cipher-relevant lines in filze
  XVII, XLVIII, LXXII, LXXIII, LXXIV, LXXV, LXXXII, LXXXVII, LXXXIX, XCVII (the rest are "carattere"/Machiavelli noise). 16 documents opened.
- Google Books feed (`www.google.com/books/feeds/volumes`, curl) for MAP-inventory snippets: 9 queries; books.google.* in-volume search hit the CAPTCHA (429) and was not retried.
- Mantua Gonzaga 2020 PDF and Genoa Archivio Segreto PDF: `cifr|zifr|ziffr|chiffr|chiav`.

## Result
**6 rows** in `candidates.json` (`make_candidates.py`), all MAP, all seen on the image:
1. MAP LXXXIX 142, Giovanni Mazzinghi, 16 Jan 1478: full page of cipher, **bare**.
2. MAP LXXII 170, anonymous, 23 Jan 1478: same cipher, **interlinear decipherment** (key source for row 1).
3. MAP XLVIII 214, "Documento cifrato", undated (filza of 1482-83): full page, **bare**.
4. MAP LXXII 213-214, "Lettere in cifra", undated: two all-cipher slips, **bare**.
5. MAP LXXIII 371, "Poscritto in cifra", undated (c. 1491-94): 8 lines, **bare**.
6. MAP XVII 211, Piero di Lorenzo (per the inventory) to an ambassador in France, "in parte in cifra": short code groups, **no gloss seen**, low.

## For COVERAGE.md
- The `*.cultura.gov.it` outage is over (6 Nov 2026, curl from this machine): drop the "connection refused / timeout" row.
- ASF MAP: images by curl (route above); MAP inventory vols 1-3 searchable as archive.org OCR; vol. 4 (filze CI-CLXV) still unsearched.
  Not swept: Mediceo del Principato (no ASF image viewer found; MIA needs login), Dieci di Balìa / Otto di Pratica responsive and
  Signori legazioni (the ASF "PAD - Progetto Archivi Digitalizzati" at `archiviodistatofirenze.cultura.gov.it/archividigitali/` was not opened in this run).
- Milan: Potenze sovrane and Carteggio interno digitised on ICAR; image access needs Chrome.
- Turin: banca dati behind a JS browser check, needs Chrome.
- Modena, Mantua, Genoa: no letter images online; finding aids at busta/mazzo level only.

## Next route: Mediceo del Principato on PAD (found at the end, not swept)
ASF's PAD (`archiviodistatofirenze.cultura.gov.it/archividigitali/fondi/`) has full image runs of **Mediceo del Principato, Carteggio
Universale 1530-1737** (`complesso-archivistico/?id=17`) and **Minute di lettere 1536-1671** (`?id=16`), plus Signori, Legazioni e
commissarie 1393-1530 (`?id=21`, outgoing registers). PAD gives only unit-level descriptions. The item-level finding aid is the printed
*Carteggio universale di Cosimo I de Medici* inventory (Archivio di Stato di Firenze / Regione Toscana, 1982-, several vols), whose
entries say "In cifra", "Parzialmente in cifra con decifrazione interlineare", "Parte in cifra con decifrazione interlineare e codice"
by filza and carta (Google Books feed snippets: filze 343, 402 A, 410, 469 ...). Next sweep: get that inventory's text (Google Books
snippet ids -XgsAAAAYAAJ, hG8sAAAAYAAJ, dwmw8uYWpE4C, lHgsAAAAYAAJ, xXgsAAAAYAAJ, 8ncsAAAAYAAJ, t3csAAAAYAAJ), list "in cifra" items
**without** "decifrazione", and open them on PAD.

## Not reached
ASF PAD (Signori, Dieci, Otto) and the MAP inventory vol. 4; the MAP key sheets (LXXII 178-188 etc.) were not opened; DECODE, Tomokiyo and
Lasry not searched for the six rows; Milan ICAR images; Turin; Archivi Nazionali full-text search; Venice (swept before).
