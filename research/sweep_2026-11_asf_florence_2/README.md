# ASF Florence sweep, second pass (6 Nov 2026)

Continues `research/sweep_2026-11_asf_florence/` (same day; routes, tools and inventory sources are described there). curl only,
no browser, about one request a second. Images in the session scratchpad (`asf2/`), not committed. `make_candidates.py` writes
`candidates.json` (22 rows, A/B, fields and vocabularies checked against `merge.py`) and `keys.json` (6 key items, cls K, kept
apart because `merge.py` accepts only A/B/C). Leads 2307-2312 and 2320-2331 are not repeated. `research/archive_sweep_2026-10/merge.py`
does not yet list this folder in `SWEEPS`.

Work list: every "in cifra" / "parzialmente in cifra" item on PAD (Mediceo del Principato filze 330-460) that the first pass did
not open. Each footnote mentioning cifra in inventory vols I-VIII was split into single notes (61 without "decifr"), and each was
placed on its entry by rendering the inventory page (vols I-II and IV-VI footnotes; vols III and VII per-filza endnotes, matched by
note number). Every item was opened on PAD at 900 px (2000 px for the doubtful ones), with the carte before and after checked for a
filed decipherment (the chancery's usual practice: a clear slip with no salutation, often headed "Deciferato").

## 1. Mediceo del Principato: verdicts

### Rows (bare cipher; one row per correspondent/system)

| Filza, cc. | Inventory | Verdict |
|---|---|---|
| 331, 70-71 | Noceto to F. Campana, Bagnone 2 May 1537; c. 71 "Informazione", "Cifra allegata a c. 70" | full page of figures, bare → **A** |
| 333, 225 | Giovanni Lanfredini, Lyon 4 Aug 1537, Parz. | 12 lines figures + signs, bare → B |
| 335, 181-183 | Card. Innocenzo Cibo, Nice 25 May 1538, "Prevalentemente in cifra. Duplicato" | five sides of figures, bare (c. 180 a wrapper) → **A** |
| 335, 132, 139 | Averardo Serristori, Barcelona 23 Mar 1538, Parz. | figure runs, water-stained, bare → B |
| 335, 570 | Luzio Calvelli to G. Masolini, 24 Dec 1538, Parz. | 8 lines, bare → B |
| 337, 330; 347, 597; 349, 42; 353, 337 | Gerolamo del Vezzo ("Barzalona" = Modena; Piacenza) and Niccolò Campana (Bologna), 1539-41, Parz. | figure runs and letter-pair codes, bare → **A** (one row) |
| 366, 39-40, 42 | Cristiano Pagni, Tortona 4 Jun 1544, Parz. | 4 lines of figures after the date (c. 42v), bare → B |
| 384, 78 | (Card. Alessandro Farnese) to (Pier Luigi Farnese), copy, "Copia di una lettera in cifra" | full page of figures, bare (2000 px) → **A** |
| 391, 287; 392, 47-49; 393, 261-263 | G. G. de' Rossi, bishop of Pavia, Milan, Dec 1548 - Apr 1549, Parz. | "+"-separated figures, full-page insert 392 c. 49, bare → **A** |
| 425, 192-195 | Serristori amb., Rome 9 Apr 1554, "Duplicato, parzialmente in cifra" | c. 193 "Inserto", full page of figures, bare (2000 px) → **A** |
| 427, 521 | brano to the pope?, s.d. | 5 lines, bare → B |
| 433, 797 | brano [Jul 1554] | slip, 4 lines, bare → B |
| 436, 900 | avviso, Gualtiero Rollo and the French ambassador in Switzerland [Dec 1554] | 8 lines, bare → B |
| 443, 678-679 | Baldovino del Monte, Rome 14 Mar 1555 | sign cipher, bare; key from 436 cc. 849-851 → **A** |
| 443, 315; 451, 25-26 | Marcello Griffoli, Siena 1555-56 (Griffoli key, Cifrari II F. III) | full page + block, bare; key from 443 c. 317 → **A** |
| 402 A, 675; 444, 127; 445, 386 | Francesco Babbi, avvisi in cifra (Babbi key, Cifrari II F. III) | three full pages, bare; key from 445 c. 367, 444 c. 113 → **A** |
| 444, 315 | [...] to Cristiano Pagni, s.d., "In cifra" | full page, mixed digits/letters, bare → **A** |
| 448, 549-550 | Mario Sforza to Sforza Sforza, Santa Fiora 27 Nov 1555, Parz. | 10 lines, bare → B |

### Glossed (decipherment on the page or on the next carta): README only

- 384 c. 70 (Valerio Amanio to Pier Luigi Farnese, Venice 3 Aug 1547): decipherment c. 71 ("Deciferato di M. Valerio di Venetia").
- 384 c. 76 (+ top of c. 77; copy of a chapter of the French ambassador's letter, Rome 10 Aug 1547): decipherment c. 79 (same heading).
- 384 c. 147 (Avviso in cifra, Rome 1547): decipherment c. 148 (inventory).
- 401 cc. 136-137 (Vincenzo de Nobili, Rome 12 Jan 1551): c. 137 headed "Deciferato".
- 402 A cc. 676-678 (Fabrizio Ferrari): the clear text is written between the figure lines (interlinear decipherment, checked at 2000 px).
- 436 cc. 849-850 (Baldovino del Monte, 21 Dec 1554): decipherment c. 851 (inventory note 117). Key source for the Baldovino row.
- 443 cc. 78, 85 (Baldovino, 6 Jan 1555; inventory: "Tale cifra non corrisponde a quella attribuitagli ... Cifrari II serie F. III"):
  c. 79, the clear unsigned "Informazione sull'atteggiamento del Papa ...", filed between the two cipher carte, is very likely its decipherment.
- 443 cc. 316-318 (Griffoli, 2 Feb 1555): decipherment c. 317. 445 c. 368 (Babbi): decipherment c. 367. 444 c. 113 (Babbi): interlinear.
- 456 c. 281 (avviso of Pero Gelido) and 410 c. 1006 (Serristori): interlinear, per the inventory (not opened).
- 357 c. 568 (Vincenzo Fedeli): decipherment c. 588 (inventory).

### No cipher seen at 900 px / too short / not on PAD

- No cipher visible: 386 c. 103 (Prospero dal Forno to Campana, copy), 388 c. 15 (Lelio Torelli), 408 c. 191 (Guarino),
  413 cc. 614-615 (Nucci, 9 Feb 1552/3; coordinator's request: clear on all four sides; the cipher of that date is cc. 624-627, lead 2325).
- Too short: 418 c. 433 (Bernardo Giusti, Rome 30 Jan 1554, "Due righe in cifra"; Giusti's cipher is glossed in 402).
- 361 c. 10 (Lorenzo Pagni, 9 Jun 1543): three lines of figures reporting Rimini news; not made a row (short; compare with the Campana-network figures).
- Not on PAD: 357 cc. 556-565 (Campana network June 1542: c. 558 "Cifra", c. 564 del Vezzo "In codice"): PAD unit 1033 (357 parte II)
  lists no images. 391 A cc. 601 and 926-927 (de' Rossi): PAD's 391 A stops at c. 517 (1036 images).
- 402 A c. 845 (Giovannantonio "il Sarto", Bologna 17 May 1551, "Allegato un inserto in cifra di F. Babbi"): c. 845 clear; the insert is
  not at c. 846 (a clear sommario); not found.

### Notes for existing leads (no new rows)

- **2325 (Nucci)**: one more bare Nucci letter, 404 A cc. 893-894 (to Cristiano Pagni, Venice 14 Oct 1551): about nine lines of figures
  at the head of c. 893r, rest clear (inventory vol. V p. 36, notes 59-60). PAD unit 995, ids 545618-545621.
- **2330 (427 cc. 48, 237)**: inventory vol. VI p. 127 puts c. 48 ("Biglietto in cifra") after c. 47, Bartolomeo Spatafora de Moncata to
  Pero Gelido, "di casa", 2 Jun 1554 (clear), with note 8 "Testo in cifra probabilmente si riferisce alla carta precedente": a likely
  sender/recipient for c. 48. cc. 236 and 238 are unrelated clear letters; no decipherment beside c. 237.
- **2329 (399 cc. 639-644)**: c. 643 (pencil "V.o di Pavia (?)", "Cifra n. 58") is continuous figures without separators; the
  bishop of Pavia's 1548-49 cipher (row above) joins groups with "+". So either a different system or a different key period;
  the bishop attribution is not confirmed by the hand of the figures. c. 639 begins mid-sentence on the French and Siena (no salutation),
  consistent with a filed decipherment, but cc. 639-642 look longer than 643-644 would decipher to; not testable without the key.
- **2323 (LXXII 211)**: the MAP inventory gives it to Bernardo Rucellai, Milan, 3 June 1482; it belongs to the Rucellai row below,
  whose three glossed siblings give the key.

## 2. MAP filza LXXII, docs. 160-240, paged leaf by leaf (900 px, rectos and versos)

160-169 clear (Medici family and agents). 170, 171 leads. 172 glossed (key item). 173-176 clear. 177 glossed (key item). 178-188 key
sheets (first pass). Then the "Cifere" run:

| Doc. | Content | Verdict |
|---|---|---|
| 189 (cc. 230-231) | Piero Dovizi da Bibbiena, Venice 8 Sep 1512, clear with many sign runs | bare → **A row** |
| 189 bis | partial cipher alphabet strip | key item |
| 190 / 191 | Roberto Acciaiuoli, Amiens 23 Oct 1513: cipher letter / "Copia di lettera di Ruberto Acciaioli ..." in clear | glossed pair (key source) |
| 192 | Acciaiuoli, Amiens 23 Oct 1513, two sides of homophonic cipher | bare → **A row** |
| 193-195 | Latin legal copy; Campofregoso copy (Genoa 1482); clear letter | clear |
| 196, 200, 202, 206 | Bernardo Rucellai, Milan, 3 Jul, 19 Jul, 11 Jul, 4 Sep 1482 | bare → **A row** (one) |
| 201 | Rucellai, 15 Jul 1482 | interlinear glosses over many groups (key source) |
| 204 / 205 | Rucellai, 30 Aug 1482 / its clear text ("Noi diremo che noi contraffacciamo ...") | glossed pair (key source) |
| 207 / 208 | Rucellai 1482 / "Decifrato della n. 207" | glossed pair (key source) |
| 209 / 210 | cipher slip (other Rucellai system) / clear decipherment | key item (vetting n10) |
| 197-199, 203 | clear (anonymous; Rucellai 27 Aug 1482 clear) | clear |
| 211-216 | leads 2323, 2310, 2324; 212 clear; 215 glossed (first pass) | - |
| 217-240 | medical recipe (217), account of 1462 (229), clear letters and copies of 1460s-1520s | no cipher seen |

The wrapper "Cifere 1478-1513" (vetting n10, c. 201 in the old numbering) matches this run: Rucellai 1482 to Acciaiuoli 1513.

## 3. MAP filza CXIX, docs. 115-127 (opened at 900 px)

Twelve key sheets (115-125, 127; `keys.json`, one item) and one cipher text, **126**: a full page of sign cipher with no clear word,
verso blank, filed among the keys (row). Legible endorsements: 116 "Cum duca Calabriae (1485)", 127 "Cum ... Ranuccio". The inventory's
twelve names were not matched sheet by sheet.

## Prior art (known.py)

Run on every row's filza and correspondent: "Mediceo del Principato 331 ... 451", Noceto, Lanfredini, Innocenzo Cibo, Calvelli, del
Vezzo, Campana, Cristiano Pagni, Alessandro Farnese, vescovo di Pavia, Gerolamo de Rossi, Baldovino, Griffoli, Babbi, Mario Sforza,
Gualtiero Rollo, Mendoza, "LXXII, doc. 189/190/192/196/200/202/206/172/177", Rucellai, Acciaiuoli, Bibbiena, Dovizi, Amiens,
"filza CXIX", Mortellas, Centurioni. Hits only on: the first pass's README (Serristori 410, Babbi, Griffoli, de' Rossi 391 A); lead
2325 (Cristiano Pagni as Nucci's addressee); lead 2329 (vescovo di Pavia); catalogue entries for XLVIII 214 (Rucellai 1483, a different
sign set, whose vetting already noted the 207/208 pair) and targets/vatican5 (Card. Alessandro Farnese's 1541-42 cipher, a possible
family for 384 c. 78); the 1580s Bernardino de Mendoza entries (a different man from the 1555 Naples Mendoza). No duplicate.
DECODE, Tomokiyo and Lasry not searched beyond the repo dumps.

## Not reached

- MAP filze LXXIII-LXXV at about 800 px (LXXII 160-240 and CXIX 115-127 done; LXXII 1-159 and 241-444 not paged).
- Sheet-by-sheet attribution and transcription of the CXIX keys; matching them and LXXII 178-188 against CXIX 126 and the LXXII rows.
- Mediceo del Principato filze 461-659 (not on PAD); 357 parte II; 391 A beyond c. 517.
- First-pass list items that resolved elsewhere: "385" is 386 c. 103, "387" is 388 c. 15, "450 A" is 451 cc. 25-26, "460" is the
  vol. VIII index entry for 456 c. 281, "430" is an index line for glossed avvisi ("Avvisi in cifra con decifrazione").

## For COVERAGE.md

- ASF Carteggio universale di Cosimo I, PAD filze 330-460: every inventory "in cifra" item now opened (first and second pass).
- ASF MAP LXXII 160-240 and CXIX 115-127 paged at a readable size.
