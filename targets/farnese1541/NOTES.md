# Farnese to Poggio, December 1541: Spain IA-1 (DECODE R91, catalogue 262)

Status: in progress (read in part, 67.8% of tokens certain, 75.3% with uncertain words; clear stretches still
unread, see Remaining gaps)

Catalogue 262. AAV Segr. Stato, Spagna 1A (IA-1), ff. 64r-66r: Cardinal Alessandro Farnese (Rome) to Giovanni Poggio,
bishop of Tropea, nuncio in Spain; clear passages on the deputation of legates, the war, the Nuremberg diet and Buda,
cipher ff. 64r l.16 - 65r (2,963 digits after the image re-read), closing on f. 66r "a qui 1[.] di Xbre ... Come
fratello Il Car. Farnese". DECODE R91 (five page images, transcription by MEG 2020, four cleartext Farnese letters of
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
  24 = ci is confirmed by *cioe* (24 9 5), *medicina*, *iudicio*. 23 is undetermined (19 occurrences, every value
  within 4 nats) and kept at Meister's ci.
* **1 = s, z or et** (Meister prints "et 1"): +113 nats; *il grado et honor suo*, *lo imperator et il re*.
* Every other syllable family (d, l, m, n, r, s) keeps Meister's order: each of the 24 orders was scored, and the
  printed one wins by 18-112 nats. A scan of all unassigned pairs seen 15+ times found no further missing code
  (best +42, the che/per padding level).

Final key for R91: a3 e5 i7 o9 u/v0, c8, b/c/bb 02, d/f/g 01, l/p 2, n/m 4, r/t 6, s/z/et 1, null 11; ca 21 ce 22
(ci 23?) ci 24 co 26; da-do 12 14 16 18; la-lo 62 64 61 66; ma-mo 04 06 03 05; na-no 80-83; ra-ro 88 89 08 00;
sa-so 84-87; dot over the preceding digit (sometimes over the code's own first digit): ta-to 80-83, qua-qui 84-86,
che/chi/non 87-89, N.S. 08, S.M.ta 00. Open code: 4 0 where *S.M.* is wanted (once with a dot before it; IA-2's key
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
`reading_65r_en.md`:

| part | tokens | certain words + nulls | with uncertain words and emendations |
|---|---|---|---|
| 64r l.16 - 64v | 1,612 | 1,127 (0.699) | 1,222 (0.758) |
| 65r | 1,351 | 881 (0.652) | 1,008 (0.746) |
| **letter** | **2,963** | **2,008 (0.678)** | **2,230 (0.753)** |

15 emendations, each one digit (the aligner prints a two-digit emendation once per digit, 31 entries); 12 sit on
digits the re-read doubts, 3 on sense alone (*resultarebbe*, *levarsi*, *cristiano*). 739 tokens unread. **Read in part,
below the 95% bar.**

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

## Remaining gaps

Unread pieces of R91 (739 tokens), by blocker:

* **illegible**: corrosion holes at the right edge of 64r l.16-20 and the line ends of 65r (~45 positions); 64v.12
  pos 1-15 ink-burnt and holed; 64v.13 pos 1-4 faint cluster; 65r.15-18 (15.19-42, 16.5-42, 17.1-34, 18.1-45),
  where corrosion runs through almost every sign and no digit could be read better than the re-read (~140 tokens);
  the struck passages (dropped from the stream).
* **open-codes**: {4 0} (*S.M.*?, 64v.2), 2 6 where *di* is wanted (64v.2, 64v.22), 23 undetermined.
* **not yet worked out (no outside blocker)**: clear digits with no reading found: 64r.16 start and after "il",
  64r.17 before "laltro", 64v.10 after "iudica", 64v.11 the noun after "preceda", 64v.12 "non si 2 9 0 8 4 8 1",
  64v.13 "facen ... rebbe" and "al c-u-scir", 64v.14 after "sente", 64v.15 before "efeto", 64v.21, 65r.1-3 starts,
  65r.4 "manco 7 1 8 3", 65r.10 start, 65r.21 the word before "sorte", 65r.23 end.

## Escalation

What was tried on R91 (writeup skill section 0a), 2026-11-05:

1. Siblings: IA-2 (R92) is another key (Klee); DECODE has no other Farnese item of 1538-48 (18 Sept search).
2. Known keys: Meister key 1 (fails), key 2 (fits, corrected as above).
3. Print / clear copy: no edition of Farnese's December 1541 letters to Poggio found; Simonetta's article on Farnese
   nuncios' letters in the Likhachev collection (St Petersburg) not seen. The decifrato, if one survives, would be in the
   Nunziatura di Spagna registers or the Carte Farnesiane (Naples); not online.
4. Key rebuild: done (k2b -> k2d), every syllable family tested, missing-code scan.
5. Retry: image re-read of every line, two reading passes per page, a key-guided image check of every unread stretch.

Next: a third reading pass on the "not yet worked out" list with fresh eyes (word lists of Farnese's 1541-42
letters; the clear passages of the same letter as a vocabulary); better images of 65r.15-18 and 64v.12 (AAV
photography, UV) for the illegible pieces.
