# ASF Florence sweep (6 Nov 2026)

Follow-up of `research/sweep_2026-11_italian_state_retry/` (same day), which found 6 MAP rows, now leads 2307-2312 (not
repeated here). curl only, no browser, about one request a second. Images and inventory texts are in the session
scratchpad (`asf/`), not committed. `make_candidates.py` writes `candidates.json` (12 rows, A/B, merge-valid) and
`keys.json` (3 key-only sheets, cls K; `merge.py` accepts only A/B/C, so they are kept apart for the key ledger).

## Routes (all curl, no login, no bot check)

| Source | Route |
|---|---|
| MAP images | as in the retry README: `/map/ricerca/ricerca-su-filza/?f=<filza>&d=<doc>&c=` lists the filza; IIIF `/iipsrv/iipsrv.fcgi?IIIF=/data/iip-data/asfi/mediceo_avanti_principato/001000FF/A0000NNN.ptif/full/<w>,/0/default.jpg` |
| **MAP printed inventory vol. 4** (filze CI-CLXV, 1963) | not on archive.org, but the MAP site serves its 442 page images: `/map/inventario/?id=001A0004/<p>`, IIIF `.../mediceo_avanti_principato/001A0004/A0000NNN.ptif` (1376 x 2000). Downloaded and OCR'd locally with the Windows OCR engine (`Windows.Media.Ocr`, en-US, PowerShell WinRT): clean text on this print. |
| **Carteggio universale di Cosimo I inventory** (17 vols, filze 329-659A, 1536-1574 + appendix) | PDFs with a text layer on ASF "Inventari on-line": `/asfi/strumenti/inventari-on-line/inventari-m/mediceo-del-principato-carteggio-universale-di-cosimo-i` (files `/asfi/fileadmin/risorse/allegati_inventari_on_line/s27-*_inv.pdf`, `s9-*.pdf`; vols XI, XII, XVI on regione.toscana.it). This replaces the Google Books snippet plan of the retry run. Notes are footnotes (vols I-VI, VIII) or per-filza endnotes (vol. VII); the text layer is column-ordered, so each hit was placed by rendering its page (pymupdf) and reading it. |
| **PAD, Mediceo del Principato Carteggio universale** | `/archividigitali/complesso-archivistico/?id=17` lists 147 units = **filze 330-460 only (1537-1557)**; filze 461-659 are not on PAD. Unit page `/archividigitali/unita-archivistica/?id=<ua>` lists carte ("c. N R/V") with riproduzione ids; each `/archividigitali/riproduzione/?id=<id>&ua=<ua>` names the file `mdp_carteggio_universale/<filza>/<seq>_C_<carta>_<R|V>.ptif`; image: `/iipsrv/iipsrv.fcgi?IIIF=/data/iip-data/asfi/mdp_carteggio_universale/<filza>/<file>/full/<w>,/0/default.jpg` (2000 px max; spaces in "394 A" as %20). The `?DeepZoom=` URL in the viewer HTML 301s to the WordPress page; use iipsrv. |

Other PAD fonds seen (not swept): Minute di lettere 1536-1671 (id 16), Signori 1308-1554 (id 20), Legazioni e commissarie 1393-1530 (id 21).

## 1. MAP inventory: vol. 4 OCR and a recheck of vols 1-3

- Vols 1-3 regrepped with de-hyphenation and OCR variants (`c[il1í]fr`, `in c?fra`, `zif`, `decif`): no hit beyond the retry run's list.
- Vol. 4 OCR, regex `c[il1í]fr|cifer|zifr|ziffr|decif|chiave|cifrar|alfabet`: 6 hits.

| Filza / no. | Inventory | Result |
|---|---|---|
| CXXXVII 252 | "Lettera cifrata di anonimo ad anonimo. s. l., 1478 gen. 13" | opened: **bare**, head "+ adì 13 di gennaio 1478", same sign set and hand as Mazzinghi 89/142 (lead 2307). **Row.** |
| CXXXVII 63 | "Poscritto cifrato anonimo. s. d." | opened: 8 lines, **bare**, signs like the 1478 set. **Row.** |
| CXXIV 184 | "S. f. Cifrata. s. d." | opened: cipher letter with **interlinear decipherment** (Naples barons: conte di Conza, conte di Capaccio, Salerno, "rebellione", so c. 1485-86); verso to "Piero [da Bibbiena?] cancelliere". Key source; no bare letter matched yet, so no row. |
| CXIX 115-127 | "Cifre della segreteria di Lorenzo il Magnifico col duca di Urbino, col duca di Calabria, con Giovanni Tornabuoni, con l'ambasciatore di Venezia, Paolo Antonio Soderini, con Lodovico Sforza, con Piero Medici, con Costanzo Sforza, con Dionigi Mortellas, con Giovan Battista Centurioni, con Pellegrino (Rossi) da Forlì, con Ranuccio (Farnese)" | **key sheets** (13), not opened. With LXXII 178-188 the second Laurentian key set to try on leads 2309-2311 and the rows below. |
| CXLVI (p. 375) | "Copia del decifrato di una lettera scritta da Jacopo Corojo, cancelliere di messer Agostino Fregoso ..." (c. 1502) | clear decipherment copy; not a cipher. Not opened. |
| CV 114 | "Firma cifrata", 1515 | cipher signature only. Not opened. |

## 2. MAP LXXII 178-188, key sheets (opened; `keys.json`)

| Doc. | Content | May unlock |
|---|---|---|
| 178 | small alphabet with homophones, doubles; endorsed "Alamanni Piero" | Alamanni letters 1489-92 |
| 179 | ser Andrea da Bologna: a-g = 1-9, h-y = Greek letters, doubles, nomenclator (Papa, Riformando, Duca, Lorenzo, Sforza ...) | lead 2310 (LXXII 213-214: digits + Greek-like signs) |
| **180** | "« Cifra »": two homophones per letter, particles, and a **Romagna nomenclator of the 1424-25 war** (Agnolo della Pergola, Secco da Montagnana, Niccolò Guerrieri, Opicino d'Alzate, Cristoforo da Lavello, Taliano, messer Pandolfo, Niccolò Piccinino; Castrocaro, Oriolo, Forlì, Imola, Faenza, Cesena, Bologna) | **catalogue 337 / `targets/medici1425`** (Averardo de' Medici and Piero Guicciardini, Faenza, 27 Oct 1425; NOTES: "No key known"). Agnolo della Pergola died 1428. |
| **182** | "Cifra d'Averardo con Astore": alphabet + **Lucca-war nomenclator** (Signore di Lucca, Baldaccio d'Anghiari, Piccinino, Pietrasanta, Motrone, Camaiore, Nozzano, Montecarlo, Rinaldo degli Albizzi, Cosimo, Averardo, Astore), c. 1430 | Averardo de' Medici's cipher family (medici1425); Lucca-war letters of 1430 (Dieci Responsive, MAP) |
| 181 | Baccio Ugolini: nomenclator (Re Ferrando, Duca di Calabria, Piero and Giuliano di Lorenzo ...) | Naples letters of the 1480s |
| 183 | Paolantonio Soderini: alphabet with 3 homophones, nulls, numbered nomenclator | Venice/Rome letters 1480s-90s |
| 184, 185 | Biliotti and Lionetto; Andrea Cambini: alphabets, doubles, "Nihil importantes", nomenclators | |
| 186 | "Cifra indiavolata": alphabet with 4-5 homophones (cc. 218-219) | |
| 187 | scribbled trial sheet with a few cipher lines | |
| 188 | "Diverse cifre" (cc. 222-229): alphabet, doubles, nulls, long code list | |

Also from the coordinator (vetting of leads 2307-2312), MAP LXXII pieces the inventory does not flag, opened here:
- **171** (inventory "Anonimo, de Spagna, 1479 ago. 31"): full page of cipher with clear words to a Magnifico in Florence, "1479" at the foot, **bare**. **Row.**
- **211**: ~10 lines cipher with clear words, verso "D(omi)no Lionardo ... in Pisa", **bare**. **Row.**
- **216**: "Magnifico Lorenzo ... lettere da Napoli ...", two sides mostly cipher; a later hand wrote scattered letters (e, o, t, so, an) over some signs, not a running gloss. **Row** (B, noted as partly glossed).
- **215**: code with "/" separators and full **interlinear decipherment** ("siamo adì 6 d'aprile 1514", Svizzeri, Lombardia, Inghilterra, Francia): key for the Pandolfini 1514-15 system (France); its sign set does not match 213-214. No bare letter matched, so no row.

## 3. Mediceo del Principato (Carteggio universale di Cosimo I)

Inventory footnotes mentioning cifra: about 700 across 17 volumes; blocks without "decifr" about 210. Vol. IV (Arrighi 1992)
never notes decipherments (1 "decifr" in the volume), so its "In cifra" items were all opened. Opened on PAD (images seen):

| Filza, cc. | Inventory | Seen | Verdict |
|---|---|---|---|
| 394 A, 1150-1153 | Medoro Nucci to Pagni, Venice 1549 Oct 23 (two letters), In cifra | 1000 px | figures, **bare** → Nucci row |
| 395, 130-131 | Nucci to Cosimo, Venice 1549 Dec 8, In cifra | 800 | **bare** → Nucci row |
| 401, 177-178 | Nucci to Cosimo, Venice 1551 Jan 13, In cifra | 800 | **bare** → Nucci row |
| 413, 624-627 | Nucci 1553 Feb 9 (partly in cifra) + two "Lettera in cifra" | 1600 | figures, **bare** → Nucci row |
| 427, 37-38 | Nucci, Venice 1554 Jun 2 | 800-1600 | **bare** → Nucci row |
| 400, 311-312 | Luigi Capponi amb., Blois 1550 Nov 24, In cifra | 1600 | c. 312 figures, **bare** → row |
| 406, 615 | "Cifra", Dec 1551 | 800 | four-letter groups, **bare** → row |
| 407, 86-87 | "Cifra", Jan 1552 | 1600 | figures, **bare** → row |
| 398, 191-192; 399, 639-644 | anonymous to Cosimo, 1550, In cifra | 800-1600 | figures (dots under groups on 398 c. 192), **bare**; 398 c. 191 and 399 cc. 639-643 clear → row (B) |
| 426, 159-160; 427, 48; 427, 237 | "Informazioni [in cifra]", "Biglietto in cifra", "Lettera in cifra", May-June 1554 | 1600 | figures, **bare** → row (B) |
| 457, 592 | Informazione on Card. Rodolfo Pio, 30 Jan 1556/7, "In cifra ... usata da Bongianni Gianfigliazzi e Giordano Orsini; Cifrari II serie F. III" | 1600 | figures with marks, **bare**; key held at ASF → row |
| 394 A, 882-884 | Pagni to the bishop of Forlì, 1549 Oct 13, In cifra | 800 | **glossed** (interlinear) |
| 402, 280-286 and 522 | Bernardo Giusti, Amboise 1551, In cifra | 800 | **glossed** |
| 402 A, 688-689 | bishop of Forlì, Augsburg 1551 May 10, In cifra | 800 | **glossed** |
| 402 A, 676-678 | Fabrizio Ferrari, s.d., In cifra | 800 | mostly clear at this size; not classified |
| 391 A, c. 601 | Giovanni Gerolamo de Rossi, 1548 Jan 25 "Lettera in cifra" (vol. III plate list) | - | PAD's 391 A ends near c. 519; not found |

Glossed by the inventory's own note (not opened): 410 c. 1006 "Informazione in cifra ... probabilmente di Averardo Serristori con
decifrazione interlineare"; vols I-III, V, IX, XV-XVII items marked "con decifrazione interlineare" or "A c. N decifrazione".

Key information in the inventory: ASF **Cifrari II serie, "Chiavi delle cifre del Carteggio di Cosimo I dal 1536 al 1573"** (3 filze;
F. III names the ciphers of Marcello Griffoli, Francesco Babbi, Bongianni Gianfigliazzi and Giordano Orsini); vol. III: key of
Giannantonio Guarnaschelli (F. 380 c. 61); vol. V: key for Bernardo Vecchietti (c. 261); vol. VIII: cifrario with Bernardino de Mendoza (Naples).

### Not opened (bare per the inventory; filza from the page heading)
- PAD filze, "Parzialmente in cifra" with no decipherment noted: 333, 335 (x3, one "prevalentemente in cifra"), 337 and 353 ("Barzalona"),
  347, 349, 357 ("Cifra"), 361, 366, 384 (incl. "Copia di capitolo di lettera. In cifra", "Copia di una lettera in cifra", "Avviso in cifra Roma 1547"),
  385, 387, 391, 391 A, 392, 393, 401, 402 A (Babbi insert), 404 A, 408, 418 ("Due righe in cifra"), 425, 426, 427 (c. 521 fragment to the pope),
  430, 433, 443 (endnotes 21 and 40: "In cifra", Griffoli cipher; the entries were not located), 444-446 (Francesco Babbi "avvisi in cifra";
  his key is in Cifrari II serie), 448, 450 A, 460.
- **Not on PAD** (filze 461-659, no images online): 470 ("In cifra"), 475, 484, 493, 494, 502 (three "messaggio cifrato"), 508 ("Lettera in cifra"),
  529 A, 541 A, 542 ("Lettera in cifra per Bartolomeo Concini", c. 432), 547 (x3), 558, 568, 572 ("In cifra"), 596, 603 (c. 771 "lettera in cifra"),
  611 ("Informazione in cifra"), 614 (x5), 617 (c. 50 "informazione in cifra"), 639, 644, 649 (two "In cifra"), 650 (x8), 651 ("La c. 125 è in cifra"),
  652 (x9), 653, 656, 657 ("Quasi tutta in cifra"). The vol. XVII appendix (filze 600-659A) is the densest cipher block (209 mentions).
  Needs another image source (MIA, login) or ASF photos.

## 4. Prior art (known.py)
"Medoro Nucci", "Mediceo del Principato 394/406", "Bernardo Giusti", "Luigi Capponi", "Fabrizio Ferrari", "Gianfigliazzi", "Cifrari II serie",
"filza CXXXVII", "LXXII, doc. 171", "Spagna, 1479", "Mortellas", "Centurioni": no hits. "Rodolfo Pio" hits only `targets/carpi1548`
(Carpi to Granvelle, a different correspondence). "Mazzinghi" hits leads 2307/2309 only. No catalogue, lead or target duplicate.
DECODE, Tomokiyo and Lasry not searched beyond the repo dumps.

## Whole-filza paging
Per the coordinator's lesson (the MAP inventory misses cipher), MAP filza LXXIV (Lyon/Vigevano 1493-94) was paged at 300 px (263 rectos,
`thumbs/f74`). At that size embedded cipher passages cannot be told from clear text, and no all-cipher page showed. Paging needs about
800 px per recto (roughly 1 s per image): not done for LXXII-LXXV, LXXXIX or CXXXVII in this run.

## Not reached
- MAP: CXIX 115-127 key sheets (inventory only); the paired 1493-94 and 1514-15 letters in LXXII/LXXIV/LXXV; whole-filza paging at a readable size.
- Mediceo del Principato: the "not opened" lists above; Minute di lettere (PAD id 16); filze 461-659 (no images).
- Signori / Legazioni e commissarie / Dieci on PAD (ids 20, 21).
- `targets/medici1425`: MAP I nos. 89-207 (Averardo's Faenza file, 1425) still unviewed; with key sheet LXXII 180 now known they are the next check.

## For COVERAGE.md
- ASF MAP inventory vol. 4 is searchable (page images + local OCR); vols 1-4 done for cipher terms.
- Carteggio universale di Cosimo I inventory: all 17 volumes online as text PDFs at ASF; PAD images cover filze 330-460 only.
