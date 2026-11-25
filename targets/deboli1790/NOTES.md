# Deboli → Stanisław August, St Petersburg cipher despatches, 1790 (catalogue 419; siblings 417, 418, 420, 421) — NOTES

Status: no write-up

Second session, 27 Oct 2026: one pair from each sibling volume was aligned (see "The sibling volumes" below).
1789 (cat. 418) and 1791 (cat. 420) hold and are closed the same way. 1788 (cat. 417) holds for the despatches in
the Polish code but not yet for the older code it replaced. 1792 (cat. 421) does not align on its opening lines.
Those two stay open.

**Verdict: closed, deciphered at the time.** Sessions 2026-10-26/27. Each of the 109 cipher despatches in
AGAD, Zbiór Popielów 4 has its contemporary decipherment, made in the King's cabinet. They are filed apart from the
ciphers: 2 Jan–2 Feb 1790 at the end of **ZbPop 417** (k. 353–386) and 5 Feb–31 Dec 1790 in **ZbPop 420**. The
catalogue entry took these Polish texts for "the open despatch of the same day". They are the decipherments.
Nothing in the volume is unread.

## The document

- AGAD Warszawa, Zbiór Popielów (zesp. 12), sygn. 4 ("Deboli. 1790 (cyfry)", old sygn. 302), 350 leaves, 109
  despatches dated 2 Jan–31 Dec 1790, all to the King per AGAD's list. Scans: agadd2 album 4 (469 images); letter
  list with image links: https://www.agad.gov.pl/inwentarze/ZbPop4.xml.
- Form: the heading is in clear French ("St Petersbourg ce 2 Janvier 1790 / reçu le 13", "Sire!"). The body is
  a page of numeric code groups, 1 to 4 digits (0 to about 2160), some with a subscript a, b or c, separated by points.
  The text starts low on the first page. The signature flourish is in clear. No interlinear decipherment.
- Plaintext language: **Polish** (the decipherments). The French heading is the house form of these despatches.

## The decipherments

- ZbPop 420 ("Korespondencja ... z Debolim", 1790, paginated) and ZbPop 417 (1787 XII–1790 II, foliated). AGAD
  lists them as "język: pol.". Each copy repeats the cipher's clear heading, the date and the "reçu le" date.
  Most add "rep:".
- `pairs.tsv` pairs all 109 cipher despatches with their copies by date: 99 in ZbPop 420, 10 in ZbPop 417. Image
  counts per despatch correlate (r = 0.69 over the 92 pairs where AGAD names the King on both sides; 409 cipher
  images against 400 clear).
- AGAD's list gives 17 of the matching ZbPop 420 items as Deboli to **Kiciński**. The one checked (16 July 1790,
  ZbPop 420 pp. 377ff.) is headed "Sire!" with the cipher's "reçu le 27", so it is the King's despatch. The
  inventory's addressee is wrong there and probably for the other 16.
- That the cabinet kept decipherments of Deboli's despatches is known for 1780–1783: Zielińska & Danilczyk print
  Deboli 1780–1782 from "deszyfry" in Archiwum Królestwa Polskiego 265 (introduction to the 1782 volume, IH PAN
  2017, RCIN). Rolnik 2025 (*Rocznik Filozoficzny Ignatianum* 31/3) quotes the 1790–92 despatches from ZbPop
  415/420/421 and notes that this correspondence was in cipher. So historians already use the decipherments. Only the
  link between them and the cipher originals in ZbPop 4 was missing from the catalogue.

## Verification (code groups against the decipherment)

Opening lines transcribed in `transcription_sample.md`. Three code equivalences hold at matching word positions in
two independent pairs:

| group | value | 2 Jan (ZbPop 4 k. 2r / 417 k. 353) | 9 Feb (ZbPop 4 k. 34r / 420 p. 13) |
|---|---|---|---|
| 1559 | w | group 1 = "W oświadczoney", group 13 = "w samey" | group 1 = "W poważeniu", group 21 = "w Warszawie" |
| 1092 | po- | opens "pomiędzy" (group 26) | opens "poważeniu" (group 2) |
| 606 | z | — | group 10 = "z okazyi", group 29 = "z strony" |

The code is a Polish syllabic and word code. Ratio is about 1.3 groups per word. That fits the "Cyfra polska
posłana do Petersburga Deboliemu", 8 III 1783 (ZbPop 444), which is not online. The key was not rebuilt. With 109
aligned pairs it could be (key from adjacent plaintext) if the codebook is wanted for other volumes.

## The sibling volumes

| catalogue | cipher volume | year | clear volume | same-date matches | pair aligned | result |
|---|---|---|---|---|---|---|
| 417 | ZbPop 428 | 1788 | ZbPop 417 | 108 of 111 | 20 May (holds); 11 Jan (not shown) | open in part |
| 418 | ZbPop 17 | 1789 | ZbPop 419 (+3 in 417) | 103 of 106 | 6 Jan (holds) | closed |
| 419 | ZbPop 4 | 1790 | ZbPop 420 + 417 | 109 of 109 | 2 Jan, 9 Feb (hold) | closed |
| 420 | ZbPop 5 | 1791 | ZbPop 421 | 98 of 105 | 7 Jan (holds) | closed |
| 421 | ZbPop 416 | 1792 | ZbPop 415 (by despatch No) | no AGAD list for 416 | No 95, 17 Feb (fails on opening lines) | open |

Transcriptions of the tested lines are in `transcription_sample.md`.

- **1789, 6 Jan** (ZbPop 17 k. 2r / ZbPop 419 k. 3). This is the same code as 1790. `1559` = "w" ("w którym", word 5,
  group 7); `951` = "od" ("od Hiszpanij", word 24, group 39), the value it has in 1790/91. `355` begins both
  "Hiszpańskiego" (group 23) and "Hiszpanij" (group 40). `1567` begins both "wyiednała" and "wypuszczenie", three
  groups apart, as the words are.
- **1791, 7 Jan** (ZbPop 5 k. 6r / ZbPop 421 k. 302). "ani od WKMci, ani od Deputacyi" sits on
  `1944 951 1570 1944 951`, the same five groups that carry "ani od WKMci, ani od" in the 9 Feb 1790 despatch.
  `1559` = "w" ("W moim pojęciu").
- **1788** uses two codes. Despatches to the spring are in an older code (groups to about 2450; 992, 893, 787 the
  most frequent). From the spring, despatches are in the 1789–91 code and begin with the group `4000`. The
  September despatch (k. 174) runs in the older code and switches at `4000`, so `4000` marks the change of code.
  - 20 May (k. 81r, opens `4000`, / ZbPop 417 k. 120): the alignment holds. `360` = "o" at all three "o" words
    (groups 16, 26, 50 for words 10, 14, 28). `360 2071 820 1657` = "o umowie z" and `360 1785 1657` = "o tym z", so
    `1657` = "z".
  - 11 Jan (k. 5–6v, older code throughout / ZbPop 417 k. 20–22v): not shown. `1328 1015a` falls where "WKMci"
    stands twice (groups 9 and 24 for words 4 and 21), but not at the third "WKMci" (word 66). The older code may
    have homophones; a longer alignment is needed. The clear copy has the same heading and receipt date as the
    other decipherments, so it is very probably this despatch's decipherment, but that is not yet measured.
- **1792** (cat. 421). ZbPop 416 has no AGAD letter list. Its paper wrapper, now image 0001, is endorsed
  "Dechiffrement des Depeches de Deboli en 1792 jusqu'au Mois d'Aout inclus". The decipherments it once held are
  the numbered Polish despatches in ZbPop 415 (No 82 of 3 Jan 1792 onward). The first cipher despatch in 416 is
  "No 95", which is 17 Feb 1792, ZbPop 415 k. 87–100v. Its opening groups do not fit the 1790 values:
  - it starts with `951` ("od") where the text starts "Z czytania";
  - `1570` ("WKMci") falls at group 6, where there is no WKMci in the clear text.
  `1559` sits at groups 22 and 57, which would fit "w" at words 13 and 36. Either the cipher begins with a passage
  that the Polish copy leaves out or puts elsewhere (the 1782 edition says French and Polish passages were
  deciphered on separate sheets), or the 1792 code differs. Open.

Catalogue 412–416 (1783–1787, ZbPop 9, 10, 11, 2, 3) have no scans online.

## Not reached

ZbPop 444/451/453/454 (keys) and ZbPop 320 (deciphered register 1774–77): no album on agadd2.

## Sources

- AGAD letter lists: ZbPop4.xml, ZbPop420.xml, ZbPop417.xml, ZbPop419.xml, ZbPop421.xml, ZbPop428.xml, ZbPop17.xml,
  ZbPop5.xml (https://www.agad.gov.pl/inwentarze/); fonds inventory ZbPopiel12.xml.
- E. Zielińska, A. Danilczyk (eds.), *Korespondencja polityczna Stanisława Augusta. Augustyn Deboli 1782* (Warszawa:
  IH PAN, 2017), Wstęp pp. 11–17. https://rcin.org.pl/dlibra/publication/275188/edition/238967
- D. Rolnik, "„Przestrogi dla Polski” Augustyna Debolego, posła Rzeczypospolitej w Petersburgu ...", *Rocznik
  Filozoficzny Ignatianum* 31/3 (2025), notes 10–58.

## 14 Nov 2026 full-texts audit

The profile had no `outcome.texts`. The folder holds no full text of any despatch: only the pairing samples of `transcription_sample.md` (opening cipher lines of seven despatches and the opening words of the decipherments of the same dates). That file held cipher and plaintext together, so it is split, with nothing changed in either part: `sample_cipher.txt` (the code groups) and `sample_decipherments.md` (the Polish openings, with an English version of each added). `transcription_sample.md` is kept as it was. They are listed as one entry for the five volumes, state `not prose` (a pairing worksheet).

What this does not give: the texts themselves. The target is closed as deciphered at the time; the decipherments are the cabinet's fair copies on the AGAD scans (ZbPop 417, 419, 420, 421), reachable through `pairs.tsv` for 1790, and none is typed here. Typing them, or the ciphers, was not attempted (109 despatches for 1790 alone).
