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
- **R7476** (nr 13 pp. 31-34), not printed: probably Stanisław Chomentowski at the Porte, c. 1712-13; 3-digit
  syllabary; 99.6% of 1622 numbers glossed, 91.2% of the glosses read here; 98.9% decodable with `sien/syllabary.tsv`
  plus values from this letter.
- **R7481, R7482** (nr 5 pp. 1-3, 5-6), not printed: Turculeț(?) 1709, Polish news from Bender (700 Swedes with
  Colonel Gyllenkrook to Suceava, the King and Mazepa to go to Rákóczi) and a Latin letter; key B; 99.4% glossed; p. 3
  is a fair copy of the decipherment of pp. 1-2.
- **R7484, R7485** = Zbiór Dzieduszyckich **24/11 no. 116** (not 26/32; DECODE "Krakow_UNK_3/4"): Chomentowski to
  Sieniawski, Adrianople 9 May 1713, and an undated second letter; same syllabary; ~99% glossed; R7485's cipher
  passage also written out in clear at the head of the page.

## Remaining gaps
- Schenck letters: 72 of 77 code numbers (373 tokens: 187, 181, 166, 186, 254, 132, 193, 258, 349, 513, 526 ...) - blocker: open-codes; context gives roles, not names; no key on DECODE, the neighbours or in print
- Schenck letters: 9 runs, 48 numbers, without sense (lceth, ditlan, gutswor ...) - blocker: open-codes; digits confirmed twice on the images, probably names or slips
- Schenck letters: dotted letter signs and small codes 83, 3., 2. - blocker: open-codes; before codes and runs, nulls or particles not settled
- R7476: 136 glosses (8.8%) unread - blocker: illegible; faint brown interlinear hand, values mostly given by syllabary.tsv

## Escalation
- [x] siblings: R7460-R7467 and R7501-R7507 opened (other collections, keys for other correspondents); DECODE has only AKM 21 plik 30/1 of the Schenck file
- [x] clear-pages: address leaves and dockets read (Baron de Schenck at Cracow, "Seligman", receipt dates); no decipherment sheet; the recipient's superscripts used as a check
- [x] known-keys: keys A and B and the R7475 table and Chomentowski syllabary tried on the Schenck letters: none fits (different number ranges)
- [x] print: Kaczka 2012, Mareș 1987 (cited), web search for Schenck and a Saxon Vienna agent 1706: no edition or key
- [x] key-rebuild: letter table rebuilt complete; codes assigned by context where a role is unambiguous (5); an alphabetical nomenclator (189 Schenck, 190 Schweden) was considered but 150/208 do not fit one series, so no values were inferred from position
- [x] retry: every run re-read at full resolution against the key (24 corrections); unread runs re-imaged twice
