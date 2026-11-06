# Farnese to Poggio, 7 August 1542: Spain IA-1 (DECODE R91, catalogue 262)

Status: in progress (written up as read in part; the open-codes gaps remain workable, see Remaining gaps)

Read in part (67.4% of tokens certain, 79.7% with uncertain words and one-digit emendations, after four reading
passes); written up 2026-11-06 as docs/farnese1541.html. Every unread piece is listed under Remaining gaps with its blocker.

Catalogue 262. AAV Segr. Stato, Spagna 1A (IA-1), ff. 64r-66r: Cardinal Alessandro Farnese (Rome) to Giovanni Poggio,
bishop of Tropea, nuncio in Spain; clear passages on the deputation of legates, the war, the Nuremberg diet and Buda,
cipher ff. 64r l.16 - 65r (2,963 digits after the image re-read), closing on f. 66r "a qui; et bene valete. Da Roma alli . ... Come
fratello Il Car. Farnese" with the day left blank. Dated 7 Aug 1542 (section of 6 Nov 2026 below; catalogued as Dec 1541). DECODE R91 (five page images, transcription by MEG 2020, four cleartext Farnese letters of
summer 1542). The companion IA-2 (R92, 15 Apr 1542) is Vatican Challenge Part 5, solved by Simon Klee in another key:
see [`../vatican5/`](../vatican5/), whose NOTES (sections of 15-18 Sept 2026) hold the earlier measurements of R91.

## 2026-11-05: Spain IA-1 (DECODE R91, catalogue 262) is in Meister's key no. 2, the Poggio cipher

Work files: scripts, decodes and keys in this folder, step log `WORKLOG.md`, image re-read `reread/`, DECODE files in `decode/` (git-ignored). The scripts use `../vatican5/it_words.json` (git-ignored, built by `../vatican5/build_it_lm.py`) for word coverage and `../vatican5/IA-2_reread.txt` for the IA-2 control.

### The key was in print

R91 (ff. 64r l.16 - 65r, 2,956 digits, between clear passages on the Nuremberg diet and Buda; closing on f. 66r
"a qui 1[.] di Xbre ... Come fratello Il Car. Farnese") reads with **Meister 1906 pp. 176-177, key no. 2, "Cifra
ultima con Mons. Poggio mandata per il Montepulciano"** (Chigi M II 49, dated by Meister 1538-42). Nobody had
connected it with this letter: Lasry-Megyesi-Kopal tried "Meister's Poggio key" on IA-1 without success (as cited by
Klee), and vatican5's 18 Sept comparison only measured IA-2 against keys 1 and 2.

Why it was missed and how it was found: key 1 ("Cifra data a Monsig. Montepulciano") has the right profile on paper
(polyphonic digits, 9 as the second digit of syllables, a null), and applied as printed it gives nothing
(-4.12 nats/char, `key1.py`). Key 2, read **polyphonically** (each consonant digit stands for a group: b/c, d/f/g,
l/p, n/m, r/t, s/z), gives Italian at once (`key2.py`): *la qualita de la materia, nondimeno perche...*,
*lo imperatore*, *infideli*, *Ingilterra et luterani*, *a la morte saluo la pace*.

### Key 2 as it fits R91

Meister's line is `a e i o u bc dfg lp nm rt sz et / 3 5 7 9 0 or 01 2 4 6 1`: the numbers do not align with the
groups. The fit to R91 settles it:

| plain | code | evidence |
|---|---|---|
| a e i o u | 3 5 7 9 0 | as printed |
| b/c (bb) | **02** | Meister's "or" is a misprint of 02: *potrebbe* = po tre 02 e, *sarebbe*, *farebbe*, *bisogno* (+246 nats over the printed reading) |
| d/f/g | 01 | as printed |
| l/p, n/m, r/t | 2, 4, 6 | as printed |
| s/z | **1** | +221 nats; et has no code of its own in R91 (et is spelled 5 6) |
| null | **11** | +867 nats; 118 times, at word and clause ends (cf. key 1's rule "pongasi la nulla al fine di ogni parola") |
| syllables | ca-co 21-24, da-do 12-18, la-lo 62/64/61/66, ma-mo 04/06/03/05, na-no 80-83, ra-ro 88/89/08/00, sa-so 84-87 | as printed |
| dotted | ta-to ·80-·83, qua-qui ·84-·86, che/chi/non ·87-·89, N.S. ·08, S.M.ta ·00 | the DECODE transcript has no dots; until the image re-read, each dotted value is offered as an alternative of its undotted code |

Single 8 (39 times in the decode) reads mostly as c (*faculta*, *occhi*, *essercito*, *nascere*) and is kept as c.
The recurring group 2 6 0 6 2 6 (three times: *le forze del ___*, *la parte del ___*, *intelligenza ___*) is
probably a code word for the Turk, not in the printed table.

### Key corrections found while reading (2026-11-05, later the same day)

Two more departures from Meister's print, each tested on the whole letter (`k2c.py`, `k2d.py`):

* **ci = 24, co = 26.** 26 is not in Meister's table. The 64r-64v reader found it from about 15 readings
  (*contrario* twice, *conoscere*, *consideri*, *particolari*, *concorrer*, *comune*, *cosa*, *publico*, *conduca*):
  +262 nats, word coverage 0.549 -> 0.594. It explains the two recurring groups: 2 6 0 6 = co+me *come* (six times)
  and 2 6 0 6 2 6 = l+tur+co *l Turco* (*le forze de l Turco*, *la parte de l Turco*, *inteligenza con el Turco*).
  24 = ci is confirmed by *cioe* (24 9 5), *medicina*, *iudicio*. 23 was undetermined at first (19 occurrences, every value
  within 4 nats) and kept at Meister's ci.
* **1 = s, z or et** (Meister prints "et 1"): +113 nats; *il grado et honor suo*, *lo imperator et il re*.
* Every other syllable family (d, l, m, n, r, s) keeps Meister's order: each of the 24 orders was scored, and the
  printed one wins by 18-112 nats. A scan of all unassigned pairs seen 15+ times found no further missing code
  (best +42, the che/per padding level).

Final key for R91: a3 e5 i7 o9 u/v0, c8, b/c/bb 02, d/f/g 01, l/p 2, n/m 4, r/t 6, s/z/et 1, null 11; ca 21 ce 22
(23 unused, see the fourth pass) ci 24 co 26; da-do 12 14 16 18; la-lo 62 64 61 66; ma-mo 04 06 03 05; na-no 80-83; ra-ro 88 89 08 00;
sa-so 84-87; dot over the preceding digit (sometimes over the code's own first digit): ta-to 80-83, qua-qui 84-86,
che/chi/non 87-89, N.S. 08, S.M.ta 00; Francia 000 (Meister p. 177, found in the third pass). Code 4 0 where *S.M.* is wanted, read in the fourth pass as S.M.ta (a slip for ·00 or a variant; once with a dot before it; IA-2's key
has 40^ = S.M.ta).

### The image re-read

DECODE's transcript (MEG, 2020) has no dots, skips cancelled digits and digits at corrosion holes, and misreads a
few digits. Two agents re-read every cipher line against the 400-dpi images (`reread/64r.txt`, `64v.txt`,
`65r.txt`; one DIFF line per line). 2,963 digit positions; ~15 firm or probable digit corrections and ~25
alternatives; 12 struck passages; 136 certain dots (+~65 doubtful), of which 83 stand before an 8 and 9 before a
0, which is Meister's rule for dotted codes. A key-guided second check (KEYCHECK notes in the DIFF lines) changed 7 more
positions where the image allows the digit the reading needs, and refused every change the glyph does not allow
(e.g. *Quanto* at 64r.16, *facendosi sarebbe* at 64v.13). The wide gaps on the page are ordinary spacing, struck
passages or corrosion holes, never word division.

### The reading, measured

`reading.txt` (clerk's spelling, merged from `reading_64.txt` and `reading_65r.txt`), aligned token by token
with the digit stream by `align91.py`; normalised Italian and English in `reading_64_en.md` and
`reading_65r_en.md`. After the fourth pass (2026-11-06):

| part | tokens | certain words + nulls | with uncertain words and emendations |
|---|---|---|---|
| 64r l.16 - 64v | 1,614 | 1,126 (0.698) | 1,306 (0.809) |
| 65r | 1,351 | 872 (0.645) | 1,056 (0.782) |
| **letter** | **2,965** | **1,998 (0.674)** | **2,362 (0.797)** |

(Before the third pass: 2,008/2,963 = 0.678 and 2,230 = 0.753; after it: 2,025/2,965 = 0.683 and 2,261 = 0.763. The
certain share dips in the fourth pass because words carrying a slip are counted uncertain, and some digits that
stood in certain words or nulls now sit in them.) 35 emendations, each one digit: 15 from the first passes (12 on
digits the re-read doubts, 3 on sense alone) and 20 clerk's slips from the fourth pass. 609 tokens unread. **Read in
part, below the 95% bar.**

### Third reading pass (2026-11-05/06)

Two new tools: `probe.py` (a line's digits with dots; best local LM decodes; where a crib encodes the digits) and
`wordfit.py` (a dictionary word lattice over a stretch, 30,000 sixteenth-century forms plus degeminated spellings).

* **Francia = 000.** Meister p. 177 prints three code words for key 2: N.S. ·08, S.M.ta ·00 and **Francia 000**; the
  first two passes had missed the third. It reads at 64v.8 (*sono a l[?] Francia nome, cioe come persona che abbia
  inteligenza con el turco*: the Emperor wants the Pope to brand the King of France the Turk's ally) and at 65r.8
  (*de Francia*, `1 4^ 0 0 0`, after *come ha fato Ingiltera et luterani*). The other three 000 groups (65r.1,
  65r.23 twice) fall inside words already read (*procurar*, *altro*, *trouara*). `align91.py` carries it as a
  three-digit code (EXTRA).
* **64v.11 *la condenatione*** (`62 26 4 14 80 82 9 81`): "bisogno che a questo preceda la condenatione, il che
  mal si puo". It uses an overwritten pair (pos 32-33) that the re-read had marked struck; DECODE transcribes it
  `2 2`, and at 4x the group ends in a clear z-shaped 2 written over an earlier sign, so it is a correction, not a
  cancellation (`reread/64v.txt` line 11, THIRD PASS note). The stream grows by two digits.
* **65r.9 *grose*[?]** (`01 00 85`, "grose ... di denari") and **65r.6 *se[.]de*** (`85 1 1? 4`, pos 56 extra).
* Refused (sense fits, but a digit the re-read does not doubt would have to change): 64v.10 *iudicato et punito*,
  64v.13 *facendosi sarebbe*, 64v.4 *considerando*, 65r.1 *e trauaglio* (pos 30 1->8; the strongest candidate if a
  better image settles the corroded sign), 65r.1 *incarico*, 65r.1 *questo*, 65r.2 *dano*, 65r.9 *imperator*,
  65r.4 *idonea*. Cribs and lattices on every other unread stretch found nothing that passes the digit, grammar and
  padding tests.

### Fourth pass: clerk's slips and code 23 (2026-11-06)

`wordfit.py --slip` lets one code per word be one digit off (`probe.slip_options`), the way a clerk enciphering by
hand miswrites a code. A slip reading was accepted only if the rest of the word's digits match exactly, the slip is a
substitution between neighbouring codes or look-alike digits (3/7, 2/1, 6/8, 8/9, 0/9), and the whole clause then
reads; every slip word is marked [?] (uncertain) and listed with written and assumed digits in the "Fourth pass
(slips)" sections of `reading_64_en.md` and `reading_65r_en.md`. 20 slips accepted (helpers `slip64_*.py`,
`slip65_*.py`):

* 64r-64v (11 readings): *Quanto a quelo che uoi scriuete* (64 > ·84); *Può ben S.M.tà Cesarea assicurarsi* ({4 0}
  > ·00; IA-2's key writes S.M.ta as ·40, so 40 may be a variant rather than a slip); *l'animo di N.S.* and *qualunque
  dichiaratione di N.S.* (the two "2 6 = di" places, 26 > 16); *considerandosi lo Imperator et il Re*; *aver l'uno per
  amico et l'altro per nimico* (replaces *caualli*); *et facendosi, sarebbe cagione che apresso li populi* (two slips,
  plus a doubtful digit); *per interesse publico*; *esporvi puntamente li facultà*.
* 65r (6 readings): *non è altro che procurar incarico e trauaglio a N.S.*; *et questo non solo [in]utile ma con dano
  evidente*; *contra lo imperator*; *qualonche sorte di dechiaratione* (cf. 64v.19, 64v.22).
* Refused again: *iudicato et punito* and *idonea* (would need an inserted digit), *soma* (a second slip next to
  it), *possa*, *in sustantia*, *marchese*, *quando*.

**Code 23 settled.** Of its 19 occurrences, the 13 in read text all split as a code ending in 2 plus 3 = *a*
(*parte*, *pace*, *la*, *boca*), and on the six unread runs that contain it no value (ci, ca, ce, co, cu, che, ti, ta,
qua, gi) gives a word that is not padding (best gain 1.6 nats). This letter writes ci as 24 and does not use
Meister's ci = 23 at all.

What it says. Farnese answers Poggio's report from the court. The Emperor, through the Cardinal of Burgos and
others, asks the Pope to declare himself in his aid (against France). Farnese could say a great deal in reply, but Poggio
knows the arguments himself and there is no need to repeat them at length. Charles may be sure the Pope is most ready to do
for him all that his rank and honour allow, but not the declaration asked of him now. Christian princes are at
odds; the King would treat the Pope "come persona che abbia inteligenza con el Turco et lo conduca a dani di
cristiani"; people would read such a step as moved "piu tosto per rispeti particolari che per [il] publico".
Against the Turk the Pope is ready "di concorrer con tute le sue forze a la difesa o ofesa, in qualonque loco si
sia", and to stake "la uita quando bisogni". A declaration would bring the Emperor evident harm; any loss of
the Pope's reputation or authority would make him less able to help "cosi ne la pace come ne la guerra", and
would give others occasion to leave "la obedientia de la Sede Apostolica" and "occupar li beni de le chiese, come
ha fato Ingiltera et luterani". The Pope will send what aid he can against "le forze de l Turco, o sole o
accompagnate", not having given up hope "di qualche concordia per l'opera de li doi legati"; the Lucca meeting
"sarebbe stata medicina contraria"; "niuno altro rimedio si trouara che non conduchi finalmente a la morte, saluo
la pace".

## 2026-11-06: the letter is of 7 August 1542, and a readable copy is in Chigi L III 65

Search for Farnese's clear text (the user's option 3). Two results: the date was wrong, and the clear text exists offline.

**The date.** The close on f. 66r reads "a qui; et bene valete. Da Roma alli ." with the day never filled in. DECODE's
"a qui 12bre" is a misreading of *et bene valete*, and the "Dec 1541" of the catalogue and of this folder's name came from
it. The clear lines date the letter:

* 64r l.1-15: "accio che V.S. resti avvisata di tutto quanto prima, et possa far noto a S.M.ta Ces.a questa deputatione de
  legati et la ragione di essa, et molto esortarla ... ad non proceder nelle cose della guerra ad atto alcuno piu avanti ...
  per non difficultar lo accordo", the Most Christian King being asked the same, until "l'arrivo delli sop.ti legati".
  Paul III named Contarini (to Charles V) and Sadoleto (to Francis I) peace legates on 7 Aug 1542, after Francis declared
  war in July (Pastor V 472).
* 65v: the King of the Romans "parti alli 9 del passato di Vienna per venir alla dieta di Norimberga a sollecitar la
  provisione de danari per lo exercito, havendo dui giorni avanti dato principio a farlo marciar verso Buda"; Saxony and
  the Landgrave arming against the Duke of Brunswick. The army left Vienna on 7-8 July 1542 and Ferdinand left for
  Nuremberg right after (Cardauns, NB I/7 p. 219 n. 1, Berbena's report from Vienna).
* Pastor, Geschichte der Paepste V (1909) p. 472 and n. 5: the Pope "hielt es fuer zu gewagt, sich offen gegen Franz I. zu
  erklaeren, weil dieser dann von der Kirche abfallen werde", would seize church goods and become a stronger enemy of Spain,
  citing "Schreiben des Kardinals Farnese an Poggio vom 7. August 1542, Biblioteca Chigi zu Rom L III 65". That is the
  cipher's argument (64v.19-22, 65r.4-8). Pastor's n. 7 cites the same letter for the date of the legates.
* Pastor app. 55 (Farnese to Poggio, 19 Aug 1542, Chigi L III 65 f. 260): Sadoleto left the day before yesterday,
  Montepulciano sent to Contarini; "V. S. tanto piu ha da procurare quanto le scrissi con el corriere", i.e. this letter.

So R91 is Farnese to Poggio, Rome, 7 August 1542. Consistent with it: the four other Farnese letters on R91 are of summer
1542, and Meister's key no. 2, "Cifra ultima con Mons. Poggio", is later than the key of the April 1542 letter (R92). The
folder and page keep the slug farnese1541 so that links hold; every date field now says 7 Aug 1542. Earlier sections of
these NOTES that say "Dec 1541" or "1[.] di Xbre" are superseded on that point. The reading is unchanged; the Lucca
sentence (65r.21) is no longer explained as "the declaration Charles wanted at Lucca", since its clause is broken.

**Where the clear text is (none of it online):**

* BAV, Chigi L III 65: Farnese's letters to Poggio. Pastor read the 7 Aug 1542 letter there and summarised its argument, so
  a readable text of it (a deciphered original or a clear copy) is in that volume, near f. 260 (19 Aug). Cardauns cites a
  19 Sept 1542 letter there as an original in cipher. Not on DigiVatLib (IIIF manifest 404 on 6 Nov 2026, while other Chigi
  manuscripts return 200); Chigi M II 49 (the key) is not online either.
* AAV, Lettere di principi 14A: register copies of Farnese's letters to Poggio (Cardauns: 23 Nov 1541 at ff. 45-48, 29 June
  1542 at ff. 453-456, and the 19 Sept 1542 letter). A register copy gives the cipher passages in clear. Not digitised.
* Naples, Archivio di Stato, Carte Farnesiane: Farnese's minutes (Cardauns: busta 707 for the Nov 1541 letters; busta
  for Aug 1542 not identified). Not digitised.
* Printed: Pastor gives only the paraphrase; Cardauns prints nothing of August 1542 to Poggio (the 1542 correspondence "nur
  fragmentarisch", German matters only); Ehses, Concilium Tridentinum IV (1904) p. 283 discusses the legates' date (search-only
  on HathiTrust; its viewer would not render in Chrome, not read).

Any of the three manuscripts would settle the clear runs listed under Remaining gaps and most of the corroded lines. A
photograph request to the BAV (Chigi L III 65, the leaves before f. 260) is the shortest route.

## Remaining gaps

Unread pieces of R91 (609 tokens) after four reading passes, by blocker:

- corrosion holes at the right edge of 64r l.16-20 and at the line ends of 65r (~45 positions) - blocker: illegible; only hole outlines remain on the only image
- 64v.12 pos 1-15 and 64v.13 pos 1-4 - blocker: illegible; ink-burnt and holed, digit count not fixed on the image
- 65r.15-18 (15.19-42, 16.5-42, 17.1-34, 18.1-45) - blocker: illegible; corrosion through almost every sign, no digit readable better than the re-read (~140 tokens)
- 65r.10 pos 1-16 and 65r.12 pos 44 - 65r.13 pos 9 - blocker: illegible; corroded starts and brown outlines at the line end
- 65r.23 pos 53-55 (end of *finalme[nte]*) - blocker: illegible; at the edge of holes
- clear digit stretches that spell nothing under the key after four passes (the last allowing one miswritten digit per word): 64r.16 after "il" and 64r.17 before "laltro" (26 digits), 64r.18-19 short runs, 64v.6 start and middle, 64v.7 start, 64v.10 after "iudica" and 64v.11 `2 6 0 3`, 64v.12 `2 9 0 8 4 8 1`, 64v.14 after "sente" and "pochi", 64v.17-19 around "di concorrer", 64v.21; 65r.2.56-3.8, 65r.5.51-6.4, 65r.8.28-30 and 8.59-9.14, 65r.10.59-11.1, 65r.13.47-51, 65r.14.37-52, 65r.20.53-21.2, 65r.22.21-23 - blocker: open-codes; digits sharp, no word of key 2 fits even with one slip per word: words not found, insertions or omissions by the clerk, or codes outside the printed table, which only the clear text would settle: it exists in BAV Chigi L III 65 (Pastor read it), AAV Lettere di principi 14A and the Naples Carte Farnesiane, none digitised

## Escalation

What was tried on R91 (writeup skill section 0a), 2026-11-05/06:

- [x] siblings: IA-2 (R92, the companion letter of 15 Apr 1542) is another key, solved by Klee; DECODE has no other Farnese item of 1538-48 (18 Sept search); R91's four document images are cleartext Farnese letters of summer 1542
- [x] clear-pages: the clear lines 64r 1-15 and f. 66r are the letter's own clear frame (legates, Nuremberg diet, Buda, date and signature), not a decipherment; no interlinear decipherment on any page
- [x] known-keys: Meister 1906 keys nos. 1-4 tried; key 1 as printed fails (-4.12 nats/char), key 2 fits read polyphonically; Klee's IA-2 key does not transfer
- [x] print: Cardauns NB I/7 (1912) and Pastor V (1909) read 6 Nov 2026: the letter is Farnese to Poggio of 7 Aug 1542, which Pastor paraphrases from BAV Chigi L III 65 (no text printed); register copies in AAV Lettere di principi 14A, minutes in the Naples Carte Farnesiane; none digitised. Earlier: Simonetta's article on Farnese nuncios' letters in the Likhachev collection concerns Guidiccioni 1537; the decifrato, if one survives, would be in the Nunziatura di Spagna registers or the Carte Farnesiane (Naples), not online
- [x] key-rebuild: k2b -> k2d (b/c 02, s/z/et 1, null 11, ci 24, co 26), every syllable family's order tested (24 permutations each), scan of unassigned pairs for missing codes, Francia 000 added from Meister p. 177, code 23 shown unused, no digit group recurs across the unread runs (only 8048, three times), so no missing code word
- [x] retry: image re-read of every line, key-guided image check of every unread stretch, three reading passes with cribs and a dictionary lattice (`probe.py`, `wordfit.py`), a fourth pass allowing one clerk's slip per word (`wordfit.py --slip`, 20 accepted), code 23 tested on every occurrence (not used)

Next, outside the session: photographs of the 7 Aug 1542 letter in BAV Chigi L III 65 (before f. 260), or of its register copy in
AAV Lettere di principi 14A; better images of 64v.12-13, 65r.1 pos 30 and 65r.15-18 (AAV photography, UV).
