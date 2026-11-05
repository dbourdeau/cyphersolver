# este1585: a cipher page in Cardinal Luigi d'Este's cipher, Rome 1584-85 (BnF Cinq Cents de Colbert 338, p. 523; catalogue 1572)

Status: read in part (Brice Dudout, 5 Nov 2026; 177 of 200 words = 88.5% without restorations; key: Satoshi Tomokiyo's table, partial by our protocol on this volume, M5 0.457 against 0.078 on the held-out page).

Contributed by Brice Dudout (Europe chiffrée), with Claude Opus 5.5 agents. Catalogue entry 1572 (BAM sweep: "Luigi, card.le
d'Este, 9 lettres en partie chiffrées"). **The key is not ours**: it is Satoshi Tomokiyo's reconstruction of "Cardinal
d'Este's Cipher (1584-1586)" on Cryptiana, made from BnF fr. 16041-16042 (Luigi d'Este to Villeroy). Colbert 338 is not cited
there.

## Document

Paris, BnF, Cinq Cents de Colbert 338, p. 523 (Gallica btv1b10033937d, view 275, right page). The whole page is in cipher:
22 lines, 777 signs, no contemporary gloss, no signature on the page. The surrounding pages (about pp. 430-525) mix letters
of Cardinal Luigi d'Este, protector of France at Rome, and French dispatches from Rome of 1584-85, in the same cipher. The
writer of p. 523 reports to a correspondent ("vous") who is to inform "le Roy" (Henri III). Date: not on the page; 1584-85
by the file.

**No image, crop or thumbnail is included** (Gallica scans used for research only).

## Key (`key.tsv`)

Tomokiyo's table, with our names for the shapes (fixed on pp. 435-438, 453-454 and 504 of this volume against their
glosses) and three changes of ours: alpha with a descending tail = f (probable words "differer / difficultes"), the large
looped rho = a, and the barred dumbbell = e (a null in Tomokiyo's table: **left open**). After the measurement the reading
added newt (thin c + barred t) = nn. Code words: th = [Roy], Xs = [le pape], Z7 = [qui], MR = [Monsieur], venT = [faire],
BIGA = [pour] (doubtful). M and Z are nulls. `key.tsv` gives the measured and the reading value of each token.

## Validation (`validation.txt`)

1. **Against the glosses of the volume** (29 Oct): five tests, none passing (V2 p. 504: 0.777 on characters vs 0.332 for
   the best control, thresholds 0.85 / 0.75); the last two not admissible because the glosses are not literal. All five
   pieces are used.
2. **One held-out page** (5 Nov): key K-C01 frozen, p. 523 transcribed by shapes and hashed before decoding, one
   measurement: **M5 = 0.457** against **0.078** for the best of 200 shuffled keys (gap 0.379). Our thresholds: >= 0.60 and
   >= +0.30. **Partial by our protocol.** We declared before the measurement that the period glosses themselves score
   0.50-0.73 on M5, so 0.60 is near the ceiling.

## Reading (`reading.md`, `translation.md`)

| words | certain | probable | restored | unresolved | certain + probable | with restored |
|---|---|---|---|---|---|---|
| 200 | 146 | 31 | 1 | 22 | 177 = 88.5% | 89.0% |

Under 95%: **read in part** (`reading_review` grade B). A blind shape sheet of 14 questions, answered by Brice Dudout, settled
"l'a", "il", "premier" and removed one stray sign (86.6% before). The pre-registered maximum of that sheet was 89.4%.

**Content.** A prince ("le Roy d'{y}", name in a code word not read) had the pope asked for the title of king; the pope
flatly refused, and the prince turned to the emperor. To the objection that the emperor could not grant it without his
electors, the writer was told that the emperor alone gave Cosimo of Florence his grand-ducal title. He asks that the King
be told, and that no one learn the news came from him, since it reaches him through "people of the pope's".

## Declared deviations

1. **The key is not validated by any of our tests**: five gloss tests failed or were not admissible, and the held-out
   page gives "partial" (0.457 < 0.60).
2. **Three remarks on the shape sheet were not foreseen** by its pre-registration and were applied as written: q05 ("it is
   shape 1 of question 8") made L1 t1 = m; q01 ("p") made a new sign p with no value; q02 ("a stroke from below, then an s:
   two signs mixed") set the stroke aside and left s with no value. None changed a count.
3. **The barred dumbbell is e in our key and a null in Tomokiyo's**: not settled; it touches lines 1 and 22.
4. **One reader**: an AI agent transcribed and read; Brice Dudout answered the shape sheet only. No palaeographer checked
   the page.
5. **Only p. 523 is read.** pp. 435-438, 453-454 and 504 were used to fix the shapes (their ciphers read as French, but
   they were deciphered at the time and we do not count them); pp. 513 and 517-518, and the other letters of entry 1572
   (pp. 433, 459, 491, 503, 511 ff.), are **not read**. Entry 1572 stays open apart from p. 523.

## Remaining gaps

- 22 unresolved words, mostly line 1 (the prince's name: code word y, two barred dumbbells) and the ends of lines 3-4 - blocker: open-codes; y has no value in the table or in our key.
- The barred dumbbell (e or null) - blocker: open-codes; needs a separate, hashed key amendment and a fresh glossed page.

Not gaps of this reading: pp. 513, 517-518 and the other letters of entry 1572 (pp. 433, 459, 491, 503, 511 ff.). They are other documents of the volume, not transcribed in this round (no reserve with a literal gloss is left in this volume to test a new key); this target is p. 523 only.

## Escalation

- [x] siblings: the neighbouring pages of Colbert 338 (pp. 435-438, 453-454, 504) opened and used for shapes; Clairambault 348 ff. 304-305 checked (the same letter as Clairambault 349 f. 3, already read).
- [x] clear-pages: the clear lines at the foot of pp. 436-437 and 453 checked as decipherments (V3, V5).
- [x] known-keys: Tomokiyo's d'Este key (the series' key) applied; it fits the whole file.
- [x] print: no edition of Colbert 338 or of fr. 16041-16042 found; Favalli 2024 (CHMO 49/2) read in full text: it covers 1569-1580 and does not mention this request; Favalli's thesis (Teramo / École des chartes 2021, HAL tel-03435435, 1559-1580) not read in full (HAL blocked our fetch), its abstract covers 1559-1580 only.
- [x] key-rebuild: probable words placed on the training pages (aj = f); newt = nn found by reading.
- [x] retry: every unresolved word retried with the reading key after the shape sheet.

## Prior work

Catalogue 1572 was open, and there was no target, PR or issue for Colbert 338 p. 523, when checked through the GitHub API
(origin/main e2315f8a, 5 Nov 2026). Cryptiana (Tomokiyo, henryiii.htm, re-read 5 Nov 2026) uses fr. 16041-16042 only and
gives the table, no edition of a letter, and nothing on a royal title. Alessandra Favalli, "Questo titolo conosciuto da
tutto il mondo…", *Cuadernos de Historia Moderna* 49/2 (2024): full text read; it treats the Este-Medici precedence quarrel
up to 1580 and does not mention a request for a royal title in 1584-85, Luigi d'Este's dispatches of those years, or any
cipher. Favalli's doctoral thesis *Il rango e la dinastia* (Teramo / PSL École nationale des chartes, 2021; HAL
tel-03435435): **not read** (the HAL page blocked our fetch, and the API lists no file); its abstract covers 1559-1580.
WAINUT and Brackx have no part in this target. No edition of fr. 16041-16042 found. If either source prints this advice,
we will credit it.

## Credits

- `tomokiyo`: key or decipherment used (the table; we do not claim the key).
- `dudout`: transcription, shape names, the added values, the test and the reading.
- `bourdeau`: pointer (catalogue entry 1572).

## Files

`transcription.txt`, `decryption.txt`, `key.tsv`, `validation.txt`, `reading.md`, `translation.md`, `profile.json`.
