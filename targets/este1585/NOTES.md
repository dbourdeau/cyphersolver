# este1585: five cipher passages in Cardinal Luigi d'Este's cipher, 1584-85 (BnF Cinq Cents de Colbert 338, pp. 513, 517-518 and 523; BnF fr. 16041 f. 271; catalogue 1572)

Status: in progress (the gaps can still be worked: a contemporary clear copy of the whole letter pp. 517-518 stands on p. 515 (found at the integration check of PR #557, 14 Nov 2026) and can settle its probable and unresolved words; the probable words of p. 523 could be settled by a palaeographer; a blind shape sheet, second reader on shapes only, settled the doubtful signs of pp. 518 and 513 on 14 Nov 2026). All five passages read in part (README read bar applied strictly: sure words only; probable, restored and unresolved words are holes): **p. 517 203/231 = 87.9%** (201/231 = 87.0% at the check of 13 Nov; the two 'Espagne' words count as sure since y is attested, see the integration check of PR #557), **p. 523 146/200 = 73.0%**; pp. 518 and 513: **p. 518 87/108 = 80.6%**, **p. 513 39/47 = 83.0%**; BnF fr. 16041 f. 271: **136/160 = 85.0%**. Key: Satoshi Tomokiyo's table; K-C02 passed its pre-registered held-out test on p. 517 (M5 0.509 against 0.067, bar 0.45), K-C01 was partial on p. 523 (M5 0.457 against 0.078, bar 0.60), K-C03.1 passed on fr. 16041 f. 271 by 0.001 (M5 0.451 against 0.077, bar 0.45). The frozen files of these tests are not in the repository: the order of events is by the contributor's record.

Contributor's status line (Brice Dudout, counting certain + probable words): **p. 517 read** (Brice Dudout, 13 Nov 2026; 223 of 231 words = 96.5%; key K-C02 validated by one pre-registered held-out measurement, M5 0.509 against 0.067). **p. 523 read in part** (5 Nov 2026; 177 of 200 words = 88.5%; key K-C01, partial by our protocol, M5 0.457 against 0.078). **p. 518** (end of the p. 517 letter, 13 Nov 2026): 103 of 108 words = 95.4% (after a blind shape sheet, 14 Nov 2026), so the **letter pp. 517-518 is read (326 of 339 words = 96.2%)**. **p. 513** (cipher block of a letter of 2 January 1585, 13 Nov 2026): 43 of 47 words = 91.5%, read in part; its margin carries a contemporary decipherment, which agrees with our reading. **BnF fr. 16041 f. 271 read** (14 Nov 2026; 152 of 160 words = 95.0%; key K-C03.1 validated by one pre-registered held-out measurement, M5 0.451 against 0.077).

Contributed by Brice Dudout (Europe chiffrée), with AI agents. Catalogue entry 1572 (BAM sweep: "Luigi, card.le
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

Strict share (README read bar, integration check of 13 Nov 2026): 146/200 = **73.0%** (certain words only). The 88.5% above is the contributor's figure (certain + probable).

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
5. **Only pp. 513, 517-518 and 523 are read** (p. 517 added 13 Nov 2026; pp. 518 and 513 the same evening, see below). pp. 435-438, 453-454 and 504 were used to fix the
   shapes (their ciphers read as French, but they were deciphered at the time and we do not count them); the
   other letters of entry 1572 (pp. 433, 459, 491, 503, 511 ff.) are **not read**. Entry 1572 stays open apart from pp. 513, 517-518 and 523.
   Outside Colbert 338, only BnF fr. 16041 f. 271 is read (14 Nov 2026, see below).
6. **p. 517 thresholds changed before its test**: 0.45 instead of 0.60 for M5, declared in the pre-registration with the reasons
   (validation.txt, section 3). Under the old 0.60, p. 517 (0.509) would also be "partial".

## Remaining gaps

- p. 523: 22 unresolved words, mostly line 1 (the prince's name: code word y, two barred dumbbells) and the ends of lines 3-4 - blocker: open-codes.
- p. 523: the code word y (twice) not re-read with its attested value Espagne ("le Roy d'Espagne"?); the content, who seeks the royal title, would change - blocker: not-attempted.
- p. 523: a contemporary clear copy elsewhere in Colbert 338 (as p. 515 is for pp. 517-518) not searched - blocker: not-attempted.
- The barred dumbbell (e or null; p. 517 L1 and L29 favour null) and the Venus sign (o, a or [faire]) - blocker: open-codes; needs a separate, hashed key amendment and a fresh glossed page.

- p. 517: 22 probable words, 1 restored word (que) and 5 unresolved words (end of L4, last words of L29) - blocker: not-attempted; the contemporary clear copy on p. 515 gives the text of the whole letter and can settle them word by word (not yet done; e.g. the unresolved "court de ‹t…›" is "court de Savoye" there). The two "Espagne" words of y are no longer holes (y attested, integration check of PR #557).
- p. 523: 31 probable words - blocker: not-attempted; as for p. 517.
- p. 518: 16 probable, 1 restored and 4 unresolved words (L3, L8, L11, L16 end) - blocker: not-attempted; they rest on the new shapes of p. 518, whose values are probable only (`key-p518-513.tsv`), but the clear copy on p. 515 gives the text: "suivant" for `suldant`, "fermer" before "mes letres", "m'a donné de tant plus grand suspect" for `docue de tant`, "en tel pays" at the end, "[Sa] Saincteté" as restored (spot checks at integration, not a word-by-word comparison).
- p. 513: 4 probable and 4 unresolved words (Espagne for y now sure), mostly the first words of the cipher block (end of L7, start of L8; first sign cut at the margin) - blocker: open-codes.
- fr. 16041 f. 271: 16 probable, 3 restored and 5 unresolved words (line 1, the start of the page continuing f. 271 r, and two line ends; "d'Espagne" now sure) - blocker: not-attempted (the start of the letter on f. 271 r is not transcribed); ff. 271 r and 272-273 of the same letter (cipher, partly glossed between the lines) are not transcribed.
- The frozen files of the three tests (PREREG-KC02 with the hashed key file and the frozen block bab39c61...; PREREG-KC03 and the K-C03 key b734cb37...; PREREG-KC03b, AVENANT-1, K-C03.1 eddc33b7..., the frozen f. 271 block 1bd8bb77... and the tool mlex2.py) - blocker: not-attempted; still not in the repository after PR #557: the committed `key-p517.tsv` quotes the frozen hash aa7d73db in its own header and hashes to 98ef85f6, and `key-f16041-271.tsv` and `transcription-f16041-271.txt` carry headers and do not hash to the stated values, so they are copies, not the hashed files; the contributor can send them.

Not gaps of this reading: the other letters of entry 1572 (pp. 433, 459, 491, 503, 511 ff.). They are other documents of the volume, not transcribed in this round (no reserve with a literal gloss is left in this volume to test a new key); this target is Colbert 338 pp. 513, 517-518 and 523 and fr. 16041 f. 271 only. The many other cipher letters of fr. 16041 (ff. 269-280) and fr. 16042 (1585-86) are not gaps of this reading either.

## Escalation

- [x] siblings: the neighbouring pages of Colbert 338 (pp. 435-438, 453-454, 504) opened and used for shapes; Clairambault 348 ff. 304-305 checked (the same letter as Clairambault 349 f. 3, already read).
- [x] clear-pages: the clear lines at the foot of pp. 436-437 and 453 checked as decipherments (V3, V5).
- [x] known-keys: Tomokiyo's d'Este key (the series' key) applied; it fits the whole file.
- [x] print: no edition of Colbert 338 or of fr. 16041-16042 found; Favalli 2024 (CHMO 49/2) read in full text: it covers 1569-1580 and does not mention this request; Favalli's thesis (Teramo / École des chartes 2021, HAL tel-03435435, 1559-1580) not read in full (HAL blocked our fetch), its abstract covers 1559-1580 only.
- [x] key-rebuild: probable words placed on the training pages (aj = f); newt = nn found by reading; K-C02 (sig = m, A = [fait]) on 13 Nov, validated on p. 517.
- [x] retry: every unresolved word retried with the reading key after the shape sheet.
- [ ] clear-pages (again, 14 Nov 2026): p. 515 (view 271, right page) is a contemporary clear copy of the letter pp. 517-518, found at the integration check of PR #557; the word-by-word comparison with the readings of pp. 517 and 518 is the next step. A clear copy of p. 523 was not searched for.

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

**Reading** (`reading-p517.md`, `translation-p517.md`). 231 words: 201 certain, 22 probable, 3 restored, 5 unresolved = **96.5%: read** by the contributor's count (certain + probable)
(`reading_review` grade A). Strict share (README read bar): **201/231 = 87.0%, read in part**; see the integration check below. Each probable word is justified in the reading file. The writer heard that the pope was told, from the court of
‹T…›, that "this duke" had letters from the King of [Spain] urging him to make war on Henri III and protect Marshal de Montmorency
(Damville); he doubts it, explains Montmorency's fears of Joyeuse around Clermont-de-Lodève and his letters to [Spain], and hopes that
Poigny's mission has calmed him, as the levy of 4,000 foot in the State of Milan has melted away. "Spain" is the code word `y`
(also on p. 523, unread there), restored by sense only and not counted at that check (since attested by pp. 513 and 515 and counted as sure: see the integration check of PR #557 below).

**Prior work for p. 517.** No edition of Colbert 338 found (see above); one web search on Poigny, Montmorency, Joyeuse and
Clermont-de-Lodève in 1584 found nothing printing this advice. Tomokiyo's table is again the key; we claim only the transcription, the
added values and the reading.

## Integration check (13 Nov 2026, PR #546)

Done on the files as submitted.

- **Own decoder** (written from `key-p517.tsv`, not the contributor's code): `transcription-p517.txt` decoded line by line equals the letter lines of `decryption-p517.txt` on all 29 lines. 1,092 signs in the file (the profile says 1,094), 979 in lines 4-29 as stated.
- **M5, own implementation.** No measuring script is in the PR. Re-implemented from the description in `validation.txt` (French lexicon of the repository, frequency >= 5, words of 5+ letters, accents removed, j->i, v->u, y->i; dynamic programming over lines 4-29; code words spelled out as letters; 200 shuffles of the letter values, seed 517): **M5 0.509**, best control 0.068, median 0.025 (contributor: 0.509, 0.067, 0.025). With the code words dropped instead: 0.525 against 0.054. The test reproduces.
- **Hashes and order of events.** By the contributor's record only: the pre-registration, the frozen key file and the frozen block are not in the PR, so their hashes cannot be recomputed, and no external timestamp exists. The committed `key-p517.tsv` hashes to 98ef85f6...; it carries the frozen value aa7d73db in its own header, so it is a later copy of the key. The M5 bar of 0.45 (0.60 for p. 523) was set before the test by the contributor's record; under 0.60 the p. 517 result would also be partial.
- **Images.** Gallica IIIF through `openapi.bnf.fr` (btv1b10033937d, f272, no bot check): lines 1, 2 and 20 at full resolution, about 110 signs, all agree with the transcription (the code word y stands in L20 as transcribed, "escript en y"; L5's y was not looked at).
- **Strict share.** p. 517: 201 certain of 231 words = **87.0%**; holes: 22 probable, 3 restored (Espagne twice from the code word y by sense, que), 5 unresolved. p. 523: 146/200 = **73.0%** (31 probable, 1 restored, 22 unresolved). The contributor's figures, 96.5% and 88.5%, count probable words as read; they are theirs. Both pages are read in part. "Spain" for y is a sense-only value and stays a hole.
- **Reading.** The p. 517 decryption reads as French in its certain words (que le pape a esté advisé de la court de ... que ce duc auoict eu letres du Roy d'[y] de vouloir resolument mouvoir guerre au Roy; la levée des quatre mil hommes de pied qui se faisoict sur l'estat de Milan); the translation follows it.
- **Prior art and duplicates.** Colbert 338 p. 517 is in no other target, lead or catalogue entry than 1572 (grep of the shelfmark and view). Key credit stays with Tomokiyo.

## pp. 518 and 513 (added 13 Nov 2026, after PR #546)

**Documents.** p. 518 (view 273, left page): lines 1-16 in cipher, the end of the p. 517 letter (490 signs), then two nulls and a
postscript in clear Italian. p. 513 (view 270, right page): a letter of 2 January 1585 signed by Luigi d'Este, in clear French
except a cipher block from the end of line 7 to line 13 (208 signs); the left margin carries a contemporary decipherment of that block,
partly lost in the binding.

**Transcription.** Two passes for each page: pass A by one AI agent, pass B by a second AI agent working blind (own crops, no key,
no access to pass A); 17 differences on p. 518 and 11 on p. 513, settled on zoomed crops (sense used only as a tie-break, declared).
The margin of p. 513 was not looked at until the transcription was frozen and the no-test decision recorded.

**Key.** The pages were decrypted with K-C02 **unchanged** (`decryption-p518.txt`, `decryption-p513.txt`). Values for the shapes K-C02
leaves open or contradicts were gathered from p. 517 (after its test) and p. 518 and listed in `key-p518-513.tsv`: Venus sign = o,
barred dumbbell = null, y = [Espagne], and five new shapes of p. 518 (X with a curved stroke = o, f crossed by a double = = f, plain long s
= u, three tight loops = p, cross with a looped head = a) each from one place. They were frozen as key K-C03 with a pre-registration naming p. 513 as held-out block, but
that block has 208 signs, under the 300 the pre-registration required, so **no test was run** and these values are **probable only**
(validation.txt, section 4).

**Reading.** p. 518 (`reading-p518.md`, `translation-p518.md`): 108 words, 87 certain, 16 probable, 1 restored, 4 unresolved = 95.4%
(grade B as a page); with p. 517 the letter is 326/339 = 96.2%. These are the contributor's figures (certain + probable); by the strict
README count of the integration check above, **p. 518 is 87/108 = 80.6%**, read in part. **Shape sheet (14 Nov 2026)**: three doubtful signs (p. 518 L1 "6",
p. 513 L8 "r2" and its first sign) were shown blind to Brice Dudout as shape thumbnails (no values, two controls, both right): "6" = plain o
(d), giving "[pour] estre de la nature" (was 101/107 = 94.4%, letter 95.9%); p. 513: N and the section sign, no change in the count. The writer asks that the news be referred to His Majesty, doubts the
pacification with Montmorency will succeed, then reports his audience: discussing Languedoc with the Pope, who ordered him to do all he
can so that the King comes to terms with Marshal de Montmorency to calm the troubles. p. 513 (`reading-p513.md`, `translation-p513.md`):
47 words, 38 certain, 5 probable, 4 unresolved = 91.5% (contributor's count; strict **38/47 = 80.9%**, read in part): according to the sieur de Longlée, in [Spain] they are scheming in case the Church
changes its shepherd, strengthening their designs and weakening the others', and express orders have been sent to Rome. The margin
decipherment reads "…oy qu'en Espaigne [le sieur] de Longlée [m'a]dvise qu'ilz font [pra]tiques si l'eglise [chan]geoit de pasteur …
ordre exprès … pour le service du Roy", which also gives **Spain for the code word y** (restored by sense only on p. 517).

**Prior work.** p. 513 was deciphered at the time (margin), so its text is not new; we add the transcription and the check of the key.
p. 518: no gloss, no edition found (three web searches on Luigi d'Este's letters to Henri III / Villeroy, Longlée in 1585, and Desjardins'
*Négociations diplomatiques de la France avec la Toscane*, whose tome IV prints the Florentine envoys' dispatches, not d'Este's French
letters; not checked page by page). Tomokiyo's table is again the key.

## BnF fr. 16041 f. 271: a new letter in the same cipher, and a held-out test of K-C03.1 (14 Nov 2026, after PR #546)

- Source: BnF fr. 16041 (Gallica btv1b9060909s; images: source gallica.bnf.fr / BnF, not reproduced), Luigi d'Este's letters to Villeroy.
  Tomokiyo built his table on this volume but cites only ff. 259 and 264 and prints no decipherment; views 524-537 were excluded.
- f. 271 (view 551) is a whole page in cipher (23 lines, 677 signs) of a letter signed by the cardinal on f. 273 r (April 1584). Unlike Colbert 338,
  the groups are separated by vertical strokes (word separators, no value).
- K-C03.1 (the probable values of pp. 517-518 frozen as K-C03, plus a clerical fix) was pre-registered against this page and measured once:
  M5 0.451 vs 0.077 (gap 0.374), thresholds 0.45 / +0.30: validated at the bar, by a margin of 0.001 only (validation.txt section 5).
- Read (`reading-f16041-271.md`, `translation-f16041-271.md`): 160 words, 135 certain, 17 probable, 3 restored, 5 unresolved. Contributor's
  count (certain + probable) 152/160 = 95.0%; strict README count, as in the integration check above, **135/160 = 84.4%, read in part**.
  Content: the Pope's failing health, his stay in the country, and d'Este's plan to plead the King's case against
  Montmorency "as of himself", Montmorency being backed by "someone greater" (Spain). New on this page: g8 = m, X with doubled arms = u.
- Open: ff. 271 r and 272-273 of the same letter (cipher, partly glossed between the lines) not transcribed; many more cipher letters in
  fr. 16041 ff. 269-280 and fr. 16042 (1585-86).

## Integration check (14 Nov 2026, PR #557)

Done on the files as submitted (three commits rebased on our integration of PR #546).

- **Own decoders.** Written from `key-p517.tsv` (K-C02) and `key-f16041-271.tsv` (K-C03.1), not the contributor's code: `transcription-p518.txt` (490 signs), `transcription-p513.txt` (208) and `transcription-f16041-271.txt` (677, separators removed) decode to exactly the letter lines of `decryption-p518.txt`, `decryption-p513.txt` and `decryption-f16041-271.txt`.
- **M5 on f. 271, own implementation** (as at the p. 517 check, with the Italian lexicon added and the higher of the two taken, separators removed, code words spelled out): **0.451 (fr), 0.374 (it)**, as stated; 660 of 677 signs with a value or a null, as stated. The best of 200 shuffled keys is 0.110 with seed 271 in our shuffling and 0.080-0.106 with three other seeds (contributor: 0.077), so the gap stays above 0.30 whatever the shuffle. The pass is at the bar, 0.451 against 0.45, by the contributor's pre-registration; the score itself reproduces to the third decimal.
- **Frozen files.** Not supplied by this PR either, for any of the three tests (p. 517's PREREG-KC02, key and block; PREREG-KC03 and K-C03; PREREG-KC03b, AVENANT-1, K-C03.1, the f. 271 block and mlex2.py). The committed key and transcription of f. 271 carry headers and do not hash to the values stated (0a8af863 and bd37a157 for the files; the stated values are eddc33b7 and 805a826f / 1bd8bb77). The order of events, the 300-sign rule for p. 513 and the thresholds are by the contributor's record.
- **Images** (Gallica IIIF through `openapi.bnf.fr`, full resolution, no bot check): p. 518 (btv1b10033937d f273, left page) lines 1, 2, 8 and 9, about 125 signs, agree (the "6" of L1 is an o with a tick, as the shape sheet found); p. 513 (f270, right page, numbered 513 in the series 511 / 513 / 515 / 517) lines 8 and 9, about 60 signs, agree, with the code word y the ninth sign of L8; f. 271 (btv1b9060909s f551) lines 1, 2 and 10, about 80 signs, agree, with the three interlinear glosses where stated.
- **The margin of p. 513**, read on the image: "…oy qu'en Espaig[ne] / …de Longlée / …dvise qu'ilz font / …tiques si l'eglise / …geoit de pasteur / …tiffiant leurs / …saings et / …oiblissant ceulx / …aultres, et / …a esté envoy[é] / ordre exprès / …pour ce que / …chose tant / …portant pour / …ruice du Roy". It agrees with the reading where both are legible, and "qu'en Espaig[ne]" stands where the cipher has `x f oo N y`.
- **p. 515: a contemporary clear copy of the letter pp. 517-518.** The right page of view 271, numbered 515, is in clear French, headed "Ce memoire doit suivre apres la letre de Cardinal de Pellevé qui est cy dessus pag. 425", and begins "Depuis vous avoir escript presentement je viens d'estre adverty d'une personne qui aultrefois m'a dict des choses qui sont reussies veritables, que le pape a esté advisé de la court de Savoye, que ce duc avoit eu letres du Roy d'Espaigne de vouloir resolument mouvoir guerre au Roy…"; it runs through "…et appaiser les troubles qui sont en tel pays" (the end of p. 518's cipher) and then gives the postscript, in French, that p. 518 has in clear Italian. Looked at on the image at integration line by line, but not transcribed in full; not used by the contributor (nothing in the PR mentions it) and not used for any count except to attest y. Consequences: (1) the text of pp. 517-518 was known at the time, as that of p. 513 was; (2) "court de ‹t…›" is the court of Savoy, and since the copy begins "Depuis vous avoir escript" like p. 517, p. 517 is the start of the memoir (not the continuation of a lost page, as `reading-p517.md` supposed); (3) the filing note ties the memoir to Cardinal de Pellevé's letter at p. 425: whether Pellevé or d'Este wrote it is not settled here; (4) every probable and unresolved word of pp. 517-518 can now be checked against it (a gap, not done).
- **y = Espagne is attested.** Two contemporary witnesses of this cipher give the value at the places where y stands: the margin decipherment of p. 513 ("qu'en Espaig[ne]") and the clear copy p. 515 ("du Roy d'Espaigne", p. 517 L5; "escript en Espaigne", p. 517 L20). A value given by a contemporary decipherment of the same cipher is not a sense-only value, so the y words count as sure: **p. 517 203/231 = 87.9%** (was 201/231), **p. 513 39/47 = 83.0%** (the contributor had 38/47 with Espagne probable), **f. 271 136/160 = 85.0%** (contributor 135/160 with "d'Espagne" probable); p. 518 has no y (87/108 = 80.6%, recounted, unchanged). p. 523's two y words are a reading question, not a recount (the word list has no "Espagne"): left as a gap. The contributor's own figures stay as he gave them.
- **Strict counts recomputed by script** from the word lists of `reading-p518.md`, `reading-p513.md` and `reading-f16041-271.md` (bare word certain, `{}` probable, `[]` restored except code words, `‹›` unresolved): 87/16/1/4, 38/5/0/4, 135/17/3/5 before the y change, as the contributor stated.
- **Second reader.** The blind shape sheet of 14 Nov 2026 was answered by Brice Dudout, the contributor himself, a person, from shape thumbnails with no values and two controls; it is a second human look at three signs, not an independent palaeographer.
- **Prior art and duplicates.** fr. 16041 is not in `catalogue.json` or `research/leads.json` except as the source of Tomokiyo's table in the vetting of entry 1572; f. 271 is in no other target. It shares the key, so it stays in this target (one key, one entry). Colbert 338 pp. 513 and 518 belong to entry 1572.

## Credits

- `tomokiyo`: key or decipherment used (the table; we do not claim the key).
- `dudout`: transcription, shape names, the added values, the test and the reading.
- `bourdeau`: pointer (catalogue entry 1572).

## Files

`transcription.txt`, `decryption.txt`, `key.tsv`, `validation.txt`, `reading.md`, `translation.md`, `profile.json`; for p. 517: `transcription-p517.txt`, `decryption-p517.txt`, `key-p517.tsv`, `reading-p517.md`, `translation-p517.md`; for pp. 518 and 513: `transcription-p518.txt`, `decryption-p518.txt`, `reading-p518.md`, `translation-p518.md`, `transcription-p513.txt`, `decryption-p513.txt`, `reading-p513.md`, `translation-p513.md`, `key-p518-513.tsv` (probable values); for fr. 16041 f. 271: `transcription-f16041-271.txt`, `decryption-f16041-271.txt`, `key-f16041-271.tsv` (K-C03.1), `reading-f16041-271.md`, `translation-f16041-271.md`.
