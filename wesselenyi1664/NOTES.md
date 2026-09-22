# R674 — Ferenc Wesselényi to Leopold I(?): cipher passages in a Latin draft (c. 1663–64)

Status: read (22 Sept 2026). Key: recovered for letters (reversed alphabet, the alphabet of DECODE key R672); two
code numbers open. Written up: docs/wesselenyi1664.html.

MNL OL E 199 (Wesselényi family archive), 8. pallium 1. 01, old number "E 199 IV/3.t.-1" on the leaf (DECODE R674,
1 p., Latin, "Non-decrypted", simple substitution, numerical). Catalogue #45 "Ferenc Wesselényi to unknown recipient",
dated there 1 Jan 1664: that is only the start of DECODE's span 1664-01-01 – 1670-12-31.

## What it is

- One page in Wesselényi's papers: Latin clear text with sixteen runs of dotted numbers 3–29 and two codes (60, 64).
  Corrections in the hand (a duplicated 14 struck in "millia", "tandem aliquando necessario" struck and rewritten
  one line down, a struck word after "accommodari") mark it as a draft or the sender's file copy, which is why it
  is in the sender's family archive.
- Addressee: "praesidium Maiestatis Vestrae" — the King, Leopold I (inferred; no address on the page).
- Heading at top centre, "S…zzi(?)" — not read.
- Content: military proposal in the Turkish war. If the Lord General [60] joins the regiments of Heister, Schneidau
  and Sporck (≈3,000 men) and 2,000 foot are added, "we" can camp at [64]; seeing that, [64] would more readily
  accept an imperial garrison; if not, action must follow, "ista nux durissima … frangi debet". Date by content:
  the war of 1663–64 (Heister's, Schneidau's and Sporck's regiments all served in Hungary then; peace of Vasvár
  Aug 1664). The DECODE span to 1670 is the folder's.

## Key

Reversed alphabet of 24 letters: 24=a 23=b 22=c 21=d 20=e 19=f 18=g 17=h 16=i 15=k 14=l 13=m 12=n 11=o 10=p (9=q)
8=r 7=s 6=t 5=u (4=w) 3=x (2=y 1=z); vowel homophones 25=a, 26=e, 28=o, 29=u (27=i not seen). Codes 60, 64 unread.

Found ciphertext-only first: a one-to-one anneal (hu-modern) failed; a Latin anneal allowing two numbers per letter
(`solve2.py la 8 4 2`) gave the whole text in all 8 seeds with slips (teneralis, castorsnaidae); fixed by hand from
"generalis", "tria millia hominum", "si adiungerentur", "duo millia peditum".
Then, among the neighbouring DECODE records, **R672** (MNL OL P 1238 Teleki Mihály collection, cipher keys no. 12,
1660–90) has exactly this reversed alphabet (24=a … 1=z) and puts syllables Ba Be Bi Bo Bu at 25–29 and Ka…Ku at
60–64. This letter uses 25–29 as the bare vowels a e (i) o u instead, and its 60/64 are names/places, not Ka/Ku
("Generalis Ka", "ad Ku in castris" make no sense). So R672 is a relative of the key (same alphabet), not the key.

Writer's slip: "Spork" is 7 9 11 8 15 — 9 is q; p is 10 everywhere else.

## Reading and measurement

`reading.md` (text, translation, notes); `transcription.txt` (the runs); `decode.py` + `key.py` reproduce it.
Transcription: DECODE DOC_R674_D1892 (EK, 2020), checked against the image; one correction (after "prius": 10, not 20).
244 cipher tokens (measured, `_check_profile.py --measure`): 241 letters read as sense, 3 code tokens unread
(60 ×1, 64 ×2). 241/244 = 0.988. Grades H 239, M 2 (26=e once in "Haster"; the slip 9 in "Spork").

## Remaining gaps
- code 60 ("Dominus Generalis [60]", once) - blocker: no-key-material; not in R672 (60 = Ka there) or in any of the Fasc. 327 Konv. D keys (R676–R690) or Teleki keys R665–R673; a person, probably the imperial commander in the sector (de Souches? not provable)
- code 64 (twice: "nos ad [64] in castris", "videns [64]") - blocker: no-key-material; a place or its townsmen that might take an imperial garrison; no key with these numbers found

## Escalation
- [x] siblings: R675 (E 199 8.1.02, "NB Rottal", Hungarian, other numeric system, marked Decrypted) opened; Teleki keys R665–R673 and Fasc. 327 Konv. D keys R676–R690 fetched and scored against the recovered alphabet: only R672 agrees (19 of the letter values), its codes do not fit
- [x] clear-pages: the page has no decipherment or gloss; R675 is a different letter
- [x] known-keys: R672 (alphabet matches), R676, R677, R680, R682, R683, R685, R687, R689, R666–R673 tried for 60/64: none gives a sense
- [x] print: web search (Wesselényi 1664 cipher, "nux durissima", Heister/Schneidau/Sporck): no edition of this draft found; Jankovics's work on Wesselényi's E 199 drafts cites a 1664 draft urging de Souches's army (context only)
- [x] key-rebuild: all 27 distinct numbers except 60 and 64 have values; the two codes occur 1 and 2 times with no alphabetical frame
- [x] retry: every run re-decoded with the final key (`decode_out.txt`); all read as Latin in context
