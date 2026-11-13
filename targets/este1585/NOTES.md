# este1585: two cipher pages in Cardinal Luigi d'Este's cipher, Rome 1584-85 (BnF Cinq Cents de Colbert 338, pp. 517 and 523; catalogue 1572)

Status: **p. 517 read** (Brice Dudout, 13 Nov 2026; 223 of 231 words = 96.5%; key K-C02 validated by one pre-registered held-out measurement, M5 0.509 against 0.067). **p. 523 read in part** (5 Nov 2026; 177 of 200 words = 88.5%; key K-C01, partial by our protocol, M5 0.457 against 0.078).

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

The page is written up at `docs/este1585.html` (5 Nov 2026) with two crops of the Gallica scan (`docs/este1585_lead.jpg`, `docs/este1585_page.jpg`), credited to the BnF via Gallica (BnF crops allowed with credit, George Lasry, 22 Sept 2026). No full image is kept in the repository. No portrait: neither the writer nor the correspondent is named on the page (`docs/_explore_skip.json`).

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
5. **Only pp. 517 and 523 are read** (p. 517 added 13 Nov 2026, see below). pp. 435-438, 453-454 and 504 were used to fix the
   shapes (their ciphers read as French, but they were deciphered at the time and we do not count them); pp. 513 and 518, and the
   other letters of entry 1572 (pp. 433, 459, 491, 503, 511 ff.), are **not read**. Entry 1572 stays open apart from pp. 517 and 523.
6. **p. 517 thresholds changed before its test**: 0.45 instead of 0.60 for M5, declared in the pre-registration with the reasons
   (validation.txt, section 3). Under the old 0.60, p. 517 (0.509) would also be "partial".

## Remaining gaps

- 22 unresolved words, mostly line 1 (the prince's name: code word y, two barred dumbbells) and the ends of lines 3-4 - blocker: open-codes; y has no value in the table or in our key.
- The barred dumbbell (e or null; p. 517 L1 and L29 favour null) and the Venus sign (o, a or [faire]) - blocker: open-codes; needs a separate, hashed key amendment and a fresh glossed page.

Not gaps of this reading: pp. 513, 518 and the other letters of entry 1572 (pp. 433, 459, 491, 503, 511 ff.). They are other documents of the volume, not transcribed in this round (no reserve with a literal gloss is left in this volume to test a new key); this target is pp. 517 and 523 only.

## Escalation

- [x] siblings: the neighbouring pages of Colbert 338 (pp. 435-438, 453-454, 504) opened and used for shapes; Clairambault 348 ff. 304-305 checked (the same letter as Clairambault 349 f. 3, already read).
- [x] clear-pages: the clear lines at the foot of pp. 436-437 and 453 checked as decipherments (V3, V5).
- [x] known-keys: Tomokiyo's d'Este key (the series' key) applied; it fits the whole file.
- [x] print: no edition of Colbert 338 or of fr. 16041-16042 found; Favalli 2024 (CHMO 49/2) read in full text: it covers 1569-1580 and does not mention this request; Favalli's thesis (Teramo / École des chartes 2021, HAL tel-03435435, 1559-1580) not read in full (HAL blocked our fetch), its abstract covers 1559-1580 only.
- [x] key-rebuild: probable words placed on the training pages (aj = f); newt = nn found by reading; K-C02 (sig = m, A = [fait]) on 13 Nov, validated on p. 517.
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

## p. 517 (added 13 Nov 2026)

**Document.** p. 517 (Gallica view 272, right page): the whole page in cipher, 29 lines, 1,094 signs, no gloss, no signature; the
letter runs on to p. 518 (about 17 cipher lines, not transcribed). Same hand and system as p. 523.

**Key K-C02** (`key-p517.tsv`). K-C01 plus four changes made only on pages already seen: sig = m ("mesmes" twice, "Maiesté", "de Mets",
"s'em-", p. 436), A = [fait] (seven places on pp. 436, 438, 453, 523), Venus sign = [faire] (one place, p. 523), newt = nn. Frozen and
hashed before p. 517 lines 4-29 were transcribed.

**Validation** (`validation.txt`, section 3). Pre-registration hashed before transcription; block = p. 517 lines 4-29 (979 signs; lines
1-3 had been seen in October and were left out); two transcription passes, 17 differences settled on the image, frozen before decoding;
one run: **M5 = 0.509** against **0.067** for the best of 200 shuffled keys; thresholds >= 0.45 and >= +0.30, fixed before from the clear
texts of the volume (which themselves score 0.50-0.73) and from a sensitivity test (5% wrong tokens already give a median of 0.35).
**Validated.** After the measurement, the reading contradicts one change: the Venus sign is o in L1 and a in L28, not [faire].

**Reading** (`reading-p517.md`, `translation-p517.md`). 231 words: 201 certain, 22 probable, 3 restored, 5 unresolved = **96.5%: read**
(`reading_review` grade A). Each probable word is justified in the reading file. The writer heard that the pope was told, from the court of
‹T…›, that "this duke" had letters from the King of [Spain] urging him to make war on Henri III and protect Marshal de Montmorency
(Damville); he doubts it, explains Montmorency's fears of Joyeuse around Clermont-de-Lodève and his letters to [Spain], and hopes that
Poigny's mission has calmed him, as the levy of 4,000 foot in the State of Milan has melted away. "Spain" is the code word `y`
(also on p. 523, unread there), restored by sense only and not counted.

**Prior work for p. 517.** No edition of Colbert 338 found (see above); one web search on Poigny, Montmorency, Joyeuse and
Clermont-de-Lodève in 1584 found nothing printing this advice. Tomokiyo's table is again the key; we claim only the transcription, the
added values and the reading.

## Credits

- `tomokiyo`: key or decipherment used (the table; we do not claim the key).
- `dudout`: transcription, shape names, the added values, the test and the reading.
- `bourdeau`: pointer (catalogue entry 1572).

## Files

`transcription.txt`, `decryption.txt`, `key.tsv`, `validation.txt`, `reading.md`, `translation.md`, `profile.json`; for p. 517: `transcription-p517.txt`, `decryption-p517.txt`, `key-p517.tsv`, `reading-p517.md`, `translation-p517.md`.
