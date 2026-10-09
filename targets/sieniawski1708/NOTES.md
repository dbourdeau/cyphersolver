# Letters to Hetman Sieniawski (1709-1714) and Vienna to Schenck (1706) — DECODE R7468-R7500

Status: read in part (written up 9 Oct 2026)

Catalogue entry 333 ("Letters to Hetman Sieniawski and Dresden to Schenck", 1708). Work started 9 Oct 2026.

## Records (DECODE metadata pulled 9 Oct 2026, `decode/views.jsonl`)

All held by the Archiwum Narodowe w Krakowie, owner 32 (uploaded 29 Sept 2023), private ciphertext, status 4 (N/A),
cipher type 6 (unknown), symbol set numerical, no decryption or key file attached on any record.

| Records | DECODE name | DECODE description | pages |
|---|---|---|---|
| R7468-R7480 | ADzied 26/32 nr 13, items 1-13 | "Listy multańskie i inne do Adama Mikołaja Sieniawskiego pisane szyfrem z różnymi wiadomościami", 1709-1714 | 2-8 each |
| R7481-R7483 | ADzied 26/32 nr 5, items 1-3 | "Listy z Wołoszczyzny do A. M. Sieniawskiego, pisane szyfrem z wiadomościami z Benderu o Szwedach, Czerkiesach i Turkach", 1709 | 3 each |
| R7484, R7485 | Krakow_UNK_3, _4 | none (1713; 1600-1799) | 5, 1 |
| R7486-R7500 | AKM 21 plik 30/1, items 1-15 | sender "NN z Drezna (jezuita?)", receiver "Schenck (Szench) szambelan Augusta II", 1706 | 3-8 each |

Neighbours checked: R7460-R7461 (ASang 85/3, keys, 1600-1799, other collection), R7462-R7467 (ASang 85/3 and
Krakow_UNK_1/2, unknown cipher, French), R7501-R7507 (AKPot 3227, Wąsowicz to Aleksander Lubomirski 1662-69, R7501 a
key). None of them is a key for these groups.

## First look (9 Oct 2026)

- **R7486-R7500 are not from Dresden.** The first letter is headed (later hand) "Wien 7 marty 1706", docketed
  "Rec. 12 aprilis 1706", numbered "N. 18", in German, signed "Votre tres humble et tres obeiss[ant]". Letter of
  29 May 1706 is "N. 32". A Vienna correspondent writing to Schenck. Clear German with (a) 3-digit code numbers for
  persons and words (150, 181, 187, 189, 190, 208, 258, 413, 452 ...) and (b) runs of 2-digit numbers spelling words.
  A few code numbers carry an interlinear clear word in another hand (above 208: "der", below: "der Kayser"?), and
  some 2-digit runs carry small superscript letters.
- **Sieniawski group, several systems, most deciphered at the time between the lines:**
  - R7473 (nr 13 item 6): dot-separated 2-digit monoalphabetic substitution, Polish, full interlinear decipherment
    ("Jaśnie wielmożny M. P. Kasztelanie krakowski hetmanie w. k. ..."): J/i=29 a=19 s=73 n=72 e=9 w=65 l=74 m=76
    o=39 z=69 y=59 P=62 k=67 t=77. The same numbers, unseparated, fill R7468-R7472 (digit strings with clear "WM Pana").
  - R7481-R7483 (nr 5): comma-separated numbers, interlinear decipherment in Polish (R7481) and Latin (R7482:
    "Hinc tantum haec occurrunt novalia ...").
  - R7484, R7485, R7476: 3-digit syllabic code (≈1-350) with interlinear Polish; R7485 also has the decipherment
    written out in clear at the head of the page.

## Prior work and contamination (searched 9 Oct 2026)

- M. W. Kaczka, "Unpublished Letters of Constantin Brâncoveanu and Constantin Stolnicul Cantacuzino, from the
  Polish Archives", *Danubius* XXX (Galați 2012), pp. 101-140 (`print/kaczka2012.pdf`): prints, from these
  originals, the Brâncoveanu and Cantacuzino letters of ADzied 26/32 nr 13 (pp. 1-5, 11-14, 15-16, 17-24, 25-28,
  35-38, 39-41, 43-46, 47-49) and the postscript nr 5 pp. 3-4, with the chancellery key in fn. 21 (key A, after
  A. Mareș 1987) and the Turculeț key in fn. 22 (key B). Kaczka names the collection Zbiór Dzieduszyckich (not
  "Dzików"). Not printed: nr 13 pp. 29-34, nr 5 pp. 1-3 and 5-6 (the Turculeț letters, announced for a separate
  edition, not found), Krakow_UNK_3/4.
- The Vienna-Schenck letters (R7486-R7500): no edition, no key, no DECODE or literature reading found. Found
  before the attempt; the Kaczka material concerns only the Sieniawski group.

## The Vienna -> Schenck letters (R7486-R7500)

**Documents.** Fifteen letters of 7 March - 14 July 1706, numbered by the writer (N. 15, 18, 27, 28, 31, 32, 35, 38,
39, 40, 41, 44, 47 ...), German with French and Latin, signed "Votre tres humble et tres obeiss. Serviteur" with a
cover name read "Sidon"/"Sadon". Address (R7488): "A Monsieur / Mons.r Le Baron de Schenck / Chambell. de Sa
Majesté / Le Roy de Pologne / à Cracovie". Receipt dockets "Recept. ... in Cracau", "in Lublin". A later archive hand
wrote "Seligman"/"Lehman" on two address leaves. DECODE's "NN z Drezna (jezuita?)" is wrong: every letter is dated
Vienna. Transcriptions: `transcr/R74xx.txt` (two agents from the full-resolution DECODE images, 9 Oct 2026).

**System.** Clear German with (1) a 2-digit letter cipher for single words or phrases, (2) 3-digit code numbers
(100-599) for persons, courts and things, (3) a few 1-2 digit codes outside the letter range (83, "3.", "2.") and
(4) letter signs with a dot ("o.", "b.", "L.", "d.", "e.", "f.", "g.", "c.", "m.", "p.", "oo", "ooo") standing before
codes and runs, apparently nulls or particles.

**Key of the letter cipher, recovered ciphertext-only (9 Oct 2026).**
1. Free homophonic annealing (`solve.py`, de-1740s order 5, many-to-one, unigram prior) on 642 tokens: no sense.
2. Run statistics: runs end in 19 43, 21 45, 20 44, 19 55; 16 starts runs; the frequent numbers cluster
   (19-21, 43-45). Hypothesis: homophones are consecutive numbers in alphabetical order.
3. `monotone.py`: annealing only the 23 block boundaries over 1-84 with the de-1740s model. Best restart
   (-913 against -1212 to -1496 for the others): b from 10, c 13, d 16, e 19, f 22, g 25, h 28, i 31, k 34, l 37,
   m 40, n 43, o 46, p 49, q 52, r 54/55, s 58, t 61, u 63/64 ... i.e. **three numbers per letter, a = 7 8 9 up to
   z, alphabet without j and v** (`key.py`). Decodings: "der Baron Kleinburg alhier", "correspondenz", "seiner
   proposition", "ein rescript so ... zugleich unterschrieben", "combination", "religionis", "confidence",
   "secretarz", "introduction", "accordirten puncten", "diffidence". 79 = z (zugleich, correspondenz, abgesetzt);
   70 = w (wieder, wegen), so w and the x/y/z blocks are not exactly three wide.
4. Second pass over every run against the key (subagent, full-resolution crops, `transcr/RUNS_FINAL.txt`): 24 lines
   corrected. Traps: the scribe's 31 looks like 21 ("ʒi"), his 6 is a delta and was read as 0 or 8. 67-69 serve for
   v and w (von, Vanitäten, Avisen), 76-78 = y (Ogilvy, Convoy, Secretarÿ), 79 = z (Reichsvicecantzler). The
   recipient's superscripts over R7486 runs (s a k l a over "geschlagen", p r e t over "dessipiret", a u f) agree with
   the key: he deciphered these runs himself.
5. Readings in context include "dieser glaubet sey kein guttes omen", "Herr Senfft hat gar 181 abgesezt", "es soll
   hier viel Cabalen ...", "o. Reichsvicecantzler", "der Baron Kleinburg alhier", "aus Muscau geschrieben", "seiner
   proposition", "ein rescript, so 154 und 166 zugleich unterschrieben", "du cabinet", "Malcontenten auffs neue
   allarmiren", "die schon accordirten puncten wieder resiliren", "diffidence", "dimission", "introduction".

**Measure** (`measure.py`, 9 Oct 2026): 682 letter-cipher numbers, 634 in runs that give sense (93.0%; 9 runs of 48
numbers give none: gutswor, sollwiglaufeenden, is, lceth, be, datmseyihm, iwzo, t, ditlan). 499 code tokens + 37
small codes; 77 distinct codes, 5 with a value (126 tokens). All cipher tokens 1218, read 760 = **62.4%**.
`ciphertext_schenck.txt` (1181 numbers, measured with `_check_profile --measure --drop-first`).

**Codes, by context only (grade I unless said).** 189 = Baron Schenck, the addressee ("Das schreiben des 189 unterm
9. curr.", "des 189 zugestossenen Unpässlichkeit", "189 sich des hungarischen Weines enthalten"); 190 = Charles XII
("dass 190 nec superiorem, nec parem aut inferiorem vertragen können"; "150 kein besondere confidence mehr gegen 190");
150 = King Augustus ("in favorem 150", "150 nichts von Schweden zu erwarten habe"); 100 = the Imperial court
(M: "das interieur von 100", "bei 100 mächtige grosse desordre"); 208 = der Kayser (C: the recipient wrote "der" and
"Kayser" by it in R7493). Open: 187 (104 tokens, the writer's principal in Vienna, "der 187 hat mir gesagt"), 181
(67, a great man in Vienna at odds with 190, "an seinem Arm nicht völlig restituiret"), 166 (ill in May, has a
"Titul"), 186 ("Mons. 186 in Krak. arrivirt"), 132 and 193 (rivals for one post; 132 "ein guter Jurist, guter
publicist, guter Linguist"), 254, 258, 349, 513, 526, 527 and the rest.

## The Sieniawski letters (R7468-R7485)

Page map, systems and transcriptions by a subagent (`sien/map.md`, `sien/R74xx.txt`), 9 Oct 2026.
- **Printed by Kaczka 2012** (key A): R7468-R7469 (no. V, 28 VI 1709 with PS), R7470 (VIII, PS of 30 VIII 1709),
  R7471 (IV, 15 VI 1709), R7472 (XXIII, Cantacuzino 15 VI 1709), R7473 (XIII, 25 VIII 1712), R7474 (XXVI, Cantacuzino
  8 IX 1714), R7477 (XXV, Cantacuzino 7 V 1714), R7478 (XVII, 10 VIII 1713), R7479 (XIX, 24 I 1714), R7480 (XX,
  29 III 1714), R7483 (XXI, postscript <1714>, now numbered pp. 9-10). Check: R7473 p. 17, ten lines, key A = gloss =
  Kaczka (`sien/R7473_check.txt`; two encipherer slips, 69 for 67 in "krakowski", "prszez").
- **R7475** (nr 13 pp. 29-30), not printed: unsigned adviser to Sieniawski, c. 1707, against the mediation of the
  Bishop of Chełmno (Teodor Potocki) and Stanisław's treaty offers; full interlinear decipherment; letter table rebuilt
  from the gloss (`sien/R7475_key.tsv`): alphabetical homophonic blocks a=17-18, b=20-21, c=22-23 ... z=56-57, e=11-14,
  y=3-4, o=7-8, u=5-6, code 600 = król szwedzki.
- **R7476** (nr 13 pp. 31-34), not printed: probably Stanisław Chomentowski at the Porte, c. 1712-13 (re-dated May-Aug 1714 in pass 2, below); 3-digit
  syllabary; 99.6% of 1622 numbers glossed, 91.2% of the glosses read here; 98.9% decodable with `sien/syllabary.tsv`
  plus values from this letter.
- **R7481, R7482** (nr 5 pp. 1-3, 5-6), not printed: Turculeț(?) 1709, Polish news from Bender (700 Swedes with
  Colonel Gyllenkrook to Suceava, the King and Mazepa to go to Rákóczi) and a Latin letter; key B; 99.4% glossed; p. 3
  is a fair copy of the decipherment of pp. 1-2.
- **R7484, R7485** = Zbiór Dzieduszyckich **24/11 no. 116** (not 26/32; DECODE "Krakow_UNK_3/4"): Chomentowski to
  Sieniawski, Adrianople 9 May 1713, and an undated second letter; same syllabary; ~99% glossed; R7485's cipher
  passage also written out in clear at the head of the page.

## Pass 2 on the Schenck codes (9 Oct 2026, after the coordinator asked for a full reading)

- **Context pass.** Two subagents re-read at full resolution every sentence holding a code or a dotted sign
  (`transcr/CTX_R74xx.txt`, about 90 crops; corrections written back into `transcr/R74xx.txt` as "(ctx: was ...)").
  Index of every code with its sentences: `code_ctx2.txt`.
- **The recipient's gloss in R7493 P1:4-5, re-read:** "der" stands over the dotted sign "o." and "von Kayser" over
  "5 83". So **o. = der, 5 = von, 83 = der Kayser** (grade C). The first pass had put "der Kayser" on 208: wrong,
  208 is the subject of that sentence and stays open.
- **The dotted signs and small numbers are a word code, not nulls**: o. = der (C), L. = und (M: "b. 154 L. 166
  zugleich unterschrieben"), f. = bey (M: "f. 83 gar sehr wohl angesehen", "ob 189 f. 254 reussire"), b. = von dem
  (I: "b. 187 bin ersuchet worden"). d., e., g., c., m., p., oo, ooo, oj, "3." and "2." stay open: their contexts
  give articles or pronouns but no single value fits all occurrences.
- **The 500s are an alphabetical word list.** 509 = Friede ("seine Gedancken in pto des 509, worauf nunmehro
  gedacht werden will", the peace advice of R7495), 513 = Ordre ("die 513 du cabinet", "vor der 513 ausgebung"),
  515 = Progressen ("weiter glückliche 515", news of Ramillies), 519 = Reise ("seine 519 auf morgen oder
  übermorgen festgestellet"), 524 = Urlaub ("beÿ 100 524 nehmen"): F < O < P < R < U rises with the number. Inside
  those bounds 502 = Abreise ("181 502 zu differiren"), 518 = Recommendation, 521 = Resolution ("eine 521 woraus
  ... von 150 Ihm eine convoy") fit the sentences (grade I). The other 500s (504, 508, 510, 516, 517, 520, 525-530)
  occur once or twice in sentences too damaged or too general to choose a word.
- **The 100s-200s are persons, courts and states, not in one alphabetical run.** Anchors: 100 = the imperial court
  (M), 150 = King Augustus (M), 189 = Baron Schenck (M: "einem diplomate vor 189", "das diploma des 189", "der
  Schenckisch-Nideggischen familie" in R7495), 204 = Schweden (M: "83 ist wegen 204 also zu timide ... dessen
  erschöpften Kräfften", "Resolutionen, so etwann 204 eine jalousie verursachen könnten"). 83 Kayser < 100 Hof <
  150 König < 189 Schenck is alphabetical, but 204 Schweden is not (an alphabetical 200s would want France there;
  France does not fit "jalousie"), so no person was valued from position.
- **190 is not Charles XII.** "König von Schweden" is in clear in the same letter; 190 delays a report to the
  Emperor, wants "ein monopolium der affairen", has cabals made against 181 in Vienna: an imperial minister. Value
  withdrawn; open.
- **Persons with roles but no name:** 187 (the writer's principal in Vienna, in the King's service, paid by bill of
  exchange, R7500), 181 (the King's man at the imperial court: sends couriers to 150, has a secretary, rheumatism
  in the arm, "affairs, insonderheit wegen Nellenburg"), 166 (a minister at the King's side, recovered in May, new
  title), 154 (co-signs a royal rescript with 166), 186 ("Mons. 186" arrived in Cracow about 20 May with a new
  function), 132 and 193 (rivals for one post; 132 "ein guter Jurist, guter publicist, guter Linguist"), 131 (sends
  Schenck a genealogy for his diploma), 254, 258, 529, 157, 101, 103, 183, 134, 158 (the King's banker who refuses
  187's bill). The Saxon envoy at Vienna until 1706 was Wackerbarth and from 1706 Vesnich (Wikipedia list of Saxon
  envoys), but Wackerbarth is named in clear in two letters, and no source ties either to a code.
- **Outside material tried:** the Wiener Diarium 1706 on ANNO (dated cribs for the news) is behind a Cloudflare
  Turnstile check and cannot be fetched by the session; searches for a Schenck chamberlain, a "Sidon" or
  "Seligman" agent and a printed 1706 Saxon-Vienna correspondence found nothing; the Hausmann *Repertorium der
  diplomatischen Vertreter* is not online.
- **Measure after pass 2** (`measure.py`, now counting the dotted signs and the small word codes as cipher tokens):
  letter cipher 638 of 682 (93.5%; "iwzo" is "ijzo" = itzo); code tokens 545, 151 with a value; dotted signs 134, 76
  with a value; **all cipher tokens 1,361, read 865 = 63.6%**.

## Pass 2 on the Sieniawski pieces (9 Oct 2026)

- R7481, R7482, R7484, R7485 checked token by token against gloss and key (`sien/R74xx_pass2.txt`, readings
  `sien/R74xx_reading.txt`): R7481 520/522 (99.6%; 407 and 700 unglossed nulls), R7482 355/355, R7484 492/513
  (95.9%; three clear date figures taken out of the count), R7485 96/96. Encipherment slips settled (62 for 65 in
  "ivit", 191 for 181 in "Hanowi", 160 = Moskwa not 169).
- R7476: faint glosses re-read at high contrast (34 crops, `sien/R7476_pass2.txt`), then a language pass with the
  syllabary's alphabetical bands (a 6-8, b 14-21 ... z 320-333; names such as Cesarz 42, Moskwa 160, Turcy 271 head
  their band): 84.8% then **1,435 of 1,622 = 88.5%** (p. 31 92.7%, p. 32 80.1%, p. 33 90.6%, p. 34 97.5%). Code
  XVIII is glossed "Hospodar Multański": Brâncoveanu, in Yedikule from April 1714, so the letter is **May-August 1714,
  Constantinople**, not 1712-13.
- Part measures: printed letters complete (Kaczka); unprinted pieces R7475 ~99.6% (glossed), R7481 99.6%, R7482
  100%, R7484 95.9%, R7485 100%, R7476 88.5%.

## Pass 3 on R7476 and R7484 (9 Oct 2026, the user approved finishing them)

- R7484: code 76 = ferman (glosses "F[e]rmana", "farman"; f band 70-78; R7476 "dano ferman"), "co im ferman i
  wbijają", "stambulscy" (37 = cy): **495 of 513 = 96.5%**. Open, 18 tokens: "umowi-ia t-r-ze-y s-za psuje" (7)
  and "ta ... s-fi-d-no" (5) whose syllables are certain but form no word found; code 112 (gloss a flourish,
  illegible at 3.5x; k band, "kajmakam" unproven); "c-wo-ko-wa-ni" (5).
- R7476, passes 4-6 (sien/R7476_pass5.txt, sien/R7476_unresolved.txt): the bad stretches re-transcribed at
  2.5-3x digit by digit (the closed 7 read as 4 six times, 51/61, 107/47, 245/243, 249/240, 163/168, 236 = 280), the
  glosses re-read, Polish words scored with lang/ pl-modern, names checked against Perłakowski 2020 on the embassy
  (Jan Spiegel = "Pan Szpigieł", Franciszek Goltz). New: "on z tąd nie ruszy, póki mu Porta nie da takiego konwoju",
  "trzysta lwowych na drogę", "z listu przejętego", "sołtan gałga uciekł do Czerkies", "a wekslowe kupcy nie chcą
  płacić", "donieść Jmci Panu Kanclerzowi Koronnemu"; codes 135 = Kanclerz, 215 = Porta (beside 213), 280 = u,
  310 = x added to syllabary.tsv. **1,531 of 1,621 = 94.4%** (p. 31 97.2%, p. 32 89.7%, p. 33 96.1%, p. 34 97.5%).
  Residue 90 tokens: 74 whose letters are known (gloss or key) but form no word after band alternatives, digit
  look-alikes and re-division; 8 in names not identifiable (a seven-sign name on p. 32 L9-10, code 216 glossed
  "Pułta"); 5 one-off codes with no gloss (2, 224, 266, 299 x2); 3 illegible after zoom.

## Remaining gaps
- Schenck letters: 65 of 77 three-digit codes (394 tokens), mostly persons (187, 181, 166, 190, 254, 258, 132, 193, 186 ...) - blocker: no-key-material; roles fixed from context, names not; no key with the letters, on DECODE or in print; the 100s-200s are not alphabetical, so position gives no bound; the Saxon keys would be in the Hauptstaatsarchiv Dresden and the Wiener Diarium 1706 (dated cribs) is behind a bot check the session may not pass
- Schenck letters: dotted signs d., e., g., c., m., p., oo, ooo, oj and small codes 3., 2. (about 90 tokens) - blocker: no-key-material; articles or pronouns, no value fits every occurrence and none is glossed
- Schenck letters: 8 letter-cipher runs, 44 numbers, without sense (lceth, ditlan, gutswor ...) - blocker: too-short; digits confirmed twice on the images, single short runs with no second occurrence
- R7476: 74 of 1,621 tokens - blocker: open-codes; letters known from gloss or key but no word, after six passes (digit re-transcription at 3x, band alternatives, LM scoring)
- R7476: 8 tokens in names (p. 32 L9-10, code 216) - blocker: no-key-material; glossed syllables, no matching name in the embassy literature
- R7476: 5 one-off codes 2, 224, 266, 299 x2 - blocker: no-key-material; no gloss, no band value
- R7476: 3 tokens - blocker: illegible; margin number p. 31 L32, stroke p. 32 L13, gloss over code 112 at 3x
- R7484: 17 of 513 tokens - blocker: open-codes; three short passages whose syllables are certain but whose words are not recovered
- R7484: code 112 (1 token) - blocker: illegible; its gloss is a flourish unreadable at 3.5x, and its only other occurrence (R7476) is also illegibly glossed

## Escalation
- [x] siblings: R7460-R7467 and R7501-R7507 opened (other collections and correspondents); DECODE holds only AKM 21 plik 30/1 of the Schenck file; R7484/R7485 used for R7476's vocabulary
- [x] clear-pages: address leaves and dockets read (Baron de Schenck at Cracow, "Seligman", receipt dates); the recipient's own glosses used: o. = der, 5 = von, 83 = der Kayser
- [x] known-keys: Kaczka's keys A and B, the R7475 table and the Chomentowski syllabary scored on the Schenck runs: none fits
- [x] print: Kaczka 2012, Mareș 1987 (cited), web searches for Schenck, "Sidon", "Seligman", Saxon envoys at Vienna 1706 (Wackerbarth, Vesnich) and printed Saxon-Vienna correspondence: no key, no edition; the Wiener Diarium on ANNO is behind a Cloudflare Turnstile check
- [x] key-rebuild: letter table complete; second context pass over every code (transcr/CTX_*); alphabetical order tested: holds in the 500s (509 Friede, 513 Ordre, 515 Progressen, 519 Reise, 524 Urlaub, bounding 502, 518, 521), fails for the persons; R7476 syllabary bands used to bound values
- [x] retry: every run and every code sentence re-read at full resolution; R7476 glosses re-read at high contrast and its unread stretches re-transcribed digit by digit at 3x (passes 4-6), R7481-R7485 token by token, R7484 pass 3 at 3.5x; Polish candidates scored with lang/ pl-modern; Perłakowski 2020 on the Chomentowski embassy used for names
