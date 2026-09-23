# Oldest-cipher candidates: what could beat 1497

Research session of 18 September 2026. Question: which undeciphered ciphertexts dated before 1497 could this
project realistically read, given what has worked here (homophonic and syllabic ciphers in Romance languages and
Latin, read from digitised images, keys recovered by crib-seeded annealing, by sibling letters, by printed key
collections, or by contemporary interlinear decipherments)? Four research sweeps: cryptiana/DECODE/Schmeh;
Spanish and Aragonese archives; Italian Quattrocento states; France/Burgundy/England/Empire and the medieval layer.

## The records to beat

| Who | Oldest previously-unread ciphertext read | How |
|---|---|---|
| This project | BnF Esp. 318 no. 95, 8 Jan **1497** (partial); Vich **1511–12** and Adrian **1521** in full | annealing; sibling key; printed decipherment |
| Lasry / Kopal / Megyesi (DECRYPT) | nothing before 1500 in print; earliest solves 1550s–1578 | |
| Jaime, Tapia Cruz & Cowan 2026 | Ayala → Ferdinand & Isabella, 25 July **1498** (Renaissance Studies, doi 10.1111/rest.70019) | key reconstruction |
| Somogyi 2016 | Maffeo da Treviglio, Buda 22 Nov **1489** | key from cipher/clear pairs |
| Simonetta c. 2002 | Federico da Montefeltro, 14 Feb **1478** | by hand from Cicco Simonetta's *Regule* |
| Parisi 2021–22 | Montefeltro → San Marino, **1451** and 1459 | key lookup in BAV Urb. lat. 998 |
| Domnina 2018 | Tranchedini postscript, Florence 23 Feb **1449** | partial coeval decipherment + substitution analysis |
| Senatore, *Dispacci sforzeschi da Napoli* | every ciphered Naples letter **1451–59** lacking a coeval decipherment | reconstructed keys, printed in the Tavole |

So anything read here before 1449 would be the oldest ciphertext-only or key-reconstruction read anyone has
published, and anything before 1497 beats the project's own record.

The pre-1497 pool is thin. DECODE has 616 records dated 1300–1496, but 608 are keys (Cremona Albertoni 97,
ÖNB Cod. 2398, ASF, Urb. lat. 998). cryptiana's unsolved list, Schmeh's Top 50 and Dunin's list have nothing
before 1497 that is a text cipher. The candidates below are what is left.

## Tier A: could set a record, images in hand or obtainable

### A1. Queen María of Castile → Alfonso V, Valencia 5 Aug 1435 (ACA, Cancillería, reg. 3225 f. 59r)
- DECODE R10171, public, image fetched without login and saved here as `ACA_reg3225_f59r_1435.jpg`
  (https://de-crypt.org/decrypt-web/RecordsView/10171).
- Catalan register copy, one page; four short cipher runs of digit-like and letter-like signs, about 40 signs in all,
  inside a clear text: "…a poder instancia dels [cipher] los daquest Regne veents la gran necessitat he treballat
  que [cipher] es continuada daci a tots sants. E [cipher] a [cipher] es stat exseguit e complit tot quant per
  vostra senyoria es stat manat…". The date is the day of the battle of Ponza; the queen is lieutenant-general
  in Valencia. Cribs: a truce or levy "continued until All Saints"; the estates (braços) of the kingdom.
- Too short for a blind solve on its own. Route: (1) the same register and its neighbours (María's lieutenancy
  registers, ACA Cancillería 3100s–3200s) should hold more letters in the same cipher; PARES has ACA
  Cancillería registers imaged, so sweep reg. 3225 for other cipher runs; (2) test the two printed Aragonese keys
  of the decade, Alfons V's Castile-war key of 1429 (Cortés & Pons, *Saitabi* 28, 1978) and the Montcada/Amat
  embassy key of 18 Mar 1437 (Aragó, *Cuad. Arq. Hist. Ciudad* 12, 1968); (3) crib-seeded annealing over the
  pooled runs.
- If read: **1435**, the oldest anyone has published.

### A2. ~~Luis Fernández from Rome, April 1424 (BRAH 9/31 ff. 128–131)~~ — RULED OUT 2026-09-18: it is 1524
- DECODE R9877–R9883 carry a typo'd date. The series continues as R9888–R9895 "1524", the senders are Luis
  Fernández de Córdoba, **Duke of Sessa**, and Lope Hurtado de Mendoza (1499–1558), and RAH 9/31 is Salazar A-31,
  calendared by Bergenroth in CSP Spain vol. 2 for April–May 1524. Siblings R9881/R9884/R9890 are "Decrypted"
  (contemporary interlinear decipherments), so it is an ordinary key-from-sibling read. See `sessa1524/NOTES.md`.

### A3. ACA, Reserva 12, "ca. 1420" (DECODE R10170) — RULED OUT, read in 1931
- Deciphered and printed in full by Xavier de Salas, "Una lletra xifrada en català", *Estudis Universitaris
  Catalans* 16 (1931), 374-377, with facsimile (fig. 7); article saved as `Salas1931_lletra_xifrada_EUC16_374-377.pdf`
  (ARCA). Not a substitution: a columnar transposition of slash-delimited word chunks, read down the lines of
  each block (blocks marked by dots in the left margin). Verified on the image, see `reserva12_1420_SOLVED_1931.md`.
- Salas dates the content 1413-1416 (Ferdinand I); "ca. 1420" is his palaeographic guess. DECODE cites the
  article yet still lists the record as non-decrypted.

### A4. Heidelberg, Cod. Pal. germ. 597, "Alchymey teuczsch", East Bavaria 1426 — RULED OUT (read 1869)
- Checked 2026-09-18, see `heidelberg597/NOTES.md` and the write-up (heidelberg597.html). Wattenbach broke the
  sign alphabets in 1869 (Anzeiger NF 16, cols. 264-268, facsimiles and plaintexts of ff. 1r, 5v, 6v); Eis
  1957/1982 printed extracts; the 2014 Heidelberg catalogue (pp. 257-260) gives its cipher quotations resolved.
  DECODE R2876 "Non-decrypted" is stale. "ff. 70-71" was Bischoff's 1954 item numbering, not folios.
- The struck alphabets on f. 1r and f. 91v/6v were recovered and checked against the printed plaintexts. What
  remains is a transcription of the recipe leaves, of philological value only.

## Tier B: solid reads that would beat 1497 but not 1449

### B1. BnF Italien 1583 (?), ff. 75–158, dated 4 May 1446: fourteen one-page ciphertexts
- DECODE R7899–R7915 "Non-decrypted", senders "Angelus", "S… N…", mixed signs, letters and numerals; DECODE names
  the volume only "1583", almost certainly BnF Italien 1583 (Sforza papers carried to Paris in 1499). Check the
  date (it may be the volume's, not the letters') and whether Gallica has the volume. Milan chancery keys 1450–1555
  are in DECODE (Carteggio Sforzesco scat. 1598 ledger, R5594–R5611 ff.) and Cerioni 1970.
- If read: **1446**.

### B2. ASMo Ambasciatori Ungheria b. 1/10, Nicolò Sadoleto, Buda 1483 (DECODE R1107–R1118) and b. 1/13,
Cesare Valentini, Pozsony 1486 (R1119, R1121); Beltrame Costabili, Esztergom 1491–93 (R1162–R1168, R1095–R1097)
- Italian, homophonic with nomenclator, 2–7 pp. each, "Partially decrypted"; sibling letters in the same buste are
  "Decrypted" (keys and cribs). Images in DECODE (login) and the Vestigia database (https://www.vestigia.hu).
- If read: **1483**.
- **Checked 19 Sept 2026 (`sadoleto1482/`): closed.** 1482: R1102 read in gist here; R1101, R1106 read at the time. 1483 (R1107–R1118): every letter has a contemporary decipherment (filed copies or clear slips pasted on the leaf). Valentini and Costabili not checked.

### B3. ASMi Carteggio Sforzesco, Potenze Estere, Ungheria b. 642/645/650: Maffeo da Treviglio and the Milanese
embassy at Buda, 1489–92 — **READ IN PART, 19 September 2026** (reclassified from read 22 Sept 2026: page 3 of the 1489
letter in patches, four signs unvalued, share read not measured; see `buda1489/`, site page buda1489.html)
- Done: the letters of 22 Nov 1489 (Vestigia 2831, four pages, only its first two lines ever deciphered) and 12 Jan 1490
  (DECODE R1098). Somogyi's key is printed only as numbers; her numbering follows first appearance in the letter of
  2 Apr 1490, which has a contemporary clear copy, so the numbers were matched back to the signs. **This beats the
  project's 1497 record with a reading in part: 1489.** R1155, R1147 and R1152 proved to have clear copies or to be clear drafts; R1146 and
  R1158 are in other ciphers and are still unread — the abbot of Forlì's cipher (R1146) has its crib in the printed
  "Extractus Cifare Abatis Forliviensis" and is the obvious next target here.
- DECODE R1098 (12 Jan 1490, 2 pp.), R1152, R1155 (Lanterio → Maffeo, 14 Sep 1492, 6 pp.), R1158 (1492, 4 pp.),
  R1146–R1147 (abbot of Forlì, 16 Oct 1491); "Partially decrypted". Somogyi 2016 (Verbum,
  https://www.epa.oszk.hu/05200/05289/00028/pdf/EPA05289_verbum_2016_1-2_195-217.pdf) reconstructed Maffeo's
  1490 key from five cipher/clear pairs. Images: DECODE (login) and Vestigia. Highest feasibility of anything here;
  the project's standard workflow.
- If read: **1489–92**.

### B4. RAH 9/7 and 9/8 ciphered letters, 1460–78 (Galende Díaz 1994, pp. 160–61)
- Juan II ↔ Bartolomé de Reus (Portugal), 24 Oct 1460, 9/7 f. 5; Pedro Ferriz → Coloma, Rome 23 Jul 1475, Latin,
  9/7 f. 173; Luis Despuig → Catholic Monarchs, Naples 3 Dec 1478, 9/7 f. 236; Archbishop Carrillo c. 1470, 9/8
  f. 114. No decipherment cited. RAH's digital library is bot-blocked; DECODE holds R9484 from this series
  (Eleanor 1476, read by Tomokiyo), so the rest may be there or obtainable. RAH 9/15 holds twelve keys of the
  Catholic Monarchs (Galende prints some).
- If read: **1460–78**.

### B5. BNE MSS/20211, Ferdinand → Juan II, 1470–79, on BDH (viewer id pattern bdh0000186543)
- Galende cites ciphered items /56 (12 Nov 1470), /73 (3 Nov 1474), /64, /94; DECODE R1172 (/123, 1478)
  "Non-decrypted". Tomokiyo reconstructed four keys from this series (two syllabic; academia.edu/37751652). Sort
  which letters lack an interlinear decipherment, then apply or extend his keys.
- If read: **1470s**.

### B6. Louis XI → Alberico Maletta, Saumur 11 Apr 1465, Latin, one cipher passage never printed
- Vaesen, *Lettres de Louis XI* II no. CLXIII: "(Suit un passage en chiffres.)"; Mandrot III also stops short.
  Original at ASMi, Potenze Estere, Francia; not online. Milan keys in DECODE. Needs a photograph from Milan.

## Ruled out or already read (so nobody re-searches)
- ACA Reserva 12 (DECODE R10170, "ca. 1420", public): read in full by Salas 1931 (EUC 16, 374-377, with facsimile);
  a word-chunk columnar transposition, content dated 1413-16. DECODE's "Non-decrypted" is stale despite citing the
  article. Lesson: read DECODE's References field first; EUC is on ARCA (whole-volume PDF, group 1527268).
- ACA Diversos, Sástago 193 Lío B nº 79 (DECODE R10172–R10175, "Non-decrypted", public): Ferdinand → Escrivà
  1495–96, all read by Parisi, *Pedralbes* 24 (2004); DECODE's status is stale. Residue: last ten lines of the
  31 Aug 1498 letter, a different cipher, still unread, not digitised.
- AGS Patronato Real leg. 52 (England, 1495–96): Bergenroth read everything; the 27 Apr 1496 syllabic note has
  its 1859/1867 Simancas decipherment on f. 379. Ayala 1498 read in 2026.
- CSP Milan 1461–97: every cipher passage carries a contemporary decipherment except a few groups in no. 511
  (London, 1 Oct 1496).
- Mandrot 1461–66, Senatore's Dispacci from Naples 1451–59, Venice Steno 1411, Fontana's booklet, Harley 2874:
  all read. Maximilian I's 1494–95 micro-cryptograms (Schmeh): 68 symbols total, too short; compare against ÖNB
  keys R2633/R2634/R2652 before any search. Santa Maria La Nova inscription, Voynich, Rohonc: not text ciphers of
  this kind.

## Scan of 23 Sept 2026: beyond DECODE (target: older than the 1425 reading)

Five sweeps (Iberia, Italy, Central/North, France-England-manuscripts, hard targets any date); notes in
`scan_2026-09-23/`. Result: **no unread pre-1425 ciphertext with images online.** Every earlier lead needs photographs:
- **Benedict XIII, ACB Barcelona, capsa "Documentos referentes a la familia Luna I"** (c. 1394-1417): autograph letter
  with cipher lines + ~3 folio pages of instruction largely in cipher (Meister 1906 pp. 22-23, from Ehrle).
  **RULED OUT 23 Sept 2026: read in 1920.** Puig y Puig, *Pedro de Luna* (1920), deciphered and printed 14 cipher
  letters to Francesc Climent, 1399-1416 (italics = deciphered), key rebuilt from Climent's own glosses; p. 475 is
  a facsimile of one page. Google Books CuOlkxWnk-EC. See `benedict1399/`, docs/benedict1399.html. Catalogue 334 removed.
- **Florence 1414**, Signori Responsive filza 1 (Meister 1902 p. 49; Gabbrielli partial key). Catalogue 335.
- **Siena 1421**, Concistoro 2308 fasc. 2 no. 1, one of 29 "partly deciphered" letters; Ilardi reel 1503 has keys only. Catalogue 336.
- Faenza 27 Oct 1425 (Averardo de' Medici), unreadable to Albizzi's office (Guasti II 457). Catalogue 337.
- Leads, no ciphertext known: Navarre key c. 1394-1406 (AGN Papeles sueltos leg. 178), Pisan key 1325 (ACA CRD Jaime II
  10044), Carrara-Ruprecht keys 1402, Teutonic Order OBA 2987 (1419, probably in Koeppen), Modena 1395 (three short
  passages), Milan 1428/1447 short passages (Osio).
- Ruled out: Lucca Guinigi 1404-06 (printed deciphered 1925), Venice "1441" (= Steno 1411), Hanse/Baltic/Hungarian/
  Imperial/Polish/Bohemian editions to 1450 (no cipher letters of their own), Rožmberk ciphers (16th c.), Portugal
  (nothing before 1532), medieval manuscript cryptograms (one-liners, read).

## Recommended order
1. **A1** (1435): pull reg. 3225 from PARES, find siblings, test the 1429 and 1437 keys, anneal. Cheapest shot at
   the oldest reading anyone has published.
2. ~~A2~~ ruled out (1524, Sessa; see above). It stays worth reading as an ordinary 1520s target.
3. ~~A3 (1420)~~ ruled out 2026-09-18: Salas read it in 1931 (see above).
4. **B3** (1489–92) in parallel as the sure thing: Somogyi's key plus sibling decipherments.
5. **B1** as a quick check (A4 is ruled out: read by Wattenbach 1869).

## Access notes
- DECODE public records serve full-resolution images without login at
  `https://de-crypt.org/decrypt-custom/filesrv/?file=IMG_R<record>_I<image>_P.jpg`; the image id is in the record
  page's thumbnail `TH_IMG_…` src. Authentication-required records need Daniel's login.
- PARES: ACA Cancillería registers are imaged; use the find endpoint and zoom 10 as in `adrian1521/pares.py`.
