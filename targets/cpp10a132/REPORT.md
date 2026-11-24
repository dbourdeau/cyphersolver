# REPORT: cpp10a132 (Cyphersolver catalogue 2130)

**Result: key recovered from ciphertext only; decoded in one pass. Judge figures pending.** 24 Nov 2026 (Brisbane).

## Target
College of Physicians of Philadelphia, Historical Medical Library, Ms. 10a 132 (medical-pharmaceutical miscellany,
Italy, 1500-1550; Hirsch 646), on OPenn. The book is paginated in ink; OPenn's TEI calls the pages folios.

| page (OPenn image, TEI label) | lines | cipher letters | split |
|---|---|---|---|
| p75 (6207_0112, "75r"): three struck lines, a first start of the same text | 3 | 100 | train |
| p76 (6207_0114, "76r") | 21 | 609 | train |
| verso of 76 (6207_0115, "76v"): 13 lines + 2 lines in large script, then a pen drawing of a winged head | 15 | 428 | held-out |
| **total** | **39** | **1,137** (100 + 609 + 428) | held-out 428 / 1,137 = 37.6% |

Counts are from decode_once.py (decode_counts.txt), not by hand [measured]. The candidate sheet's "about 850 letters"
covered p76 and p75 only: the verso had not been viewed. Also in the text: 2 scribal abbreviation strokes with no key
value, 14 lost or illegible marks (11 of them line ends in the gutter of the verso image), 7 numerals in clear.

## Prior art
None found: no key, decipherment, gloss or printed reading (PRIOR_ART.md). OPenn says only "Fol.76 in cipher".
Hirsch's 1983 catalogue was not opened (print only).

## Method record
- Transcribed in full from the OPenn master TIFFs (sha1 matches OPenn's manifest; FETCH_LOG.txt), then frozen
  (FREEZE_TX.txt) with the split. Limit on blindness, stated in the freeze: the system was recognised by eye while
  transcribing, because the cipher is ordinary letters, word-divided.
- Key recovered from the train split only, two independent ways that agree in all 20 letters (SOLVE_LOG.md):
  a shift test over four alphabets, and a free substitution hill-climb that assumes no shift (27 of 48 restarts
  converge to the same key; the other 21 stall and are logged).
- Key frozen (FREEZE_KEY.txt), then one decode (DECODE.txt). No emendations.

## Key
Each letter is replaced by the next letter of the 23-letter Latin alphabet (a b c d e f g h i k l m n o p q r s t u x y z):
plain a>b, b>c ... h>i, i>k, l>m ... t>u, u>x, x>y. Cipher letters in use: 20 (a, l, z never occur). Numerals are left
in clear. Two ordinary scribal abbreviation strokes (S01, S02) were given no value.

## Figures
- Held-out (verso of 76, 428 letters) and full (1,137 letters) read percentages: **pending the judge**
  (judge/BRIEF.txt, judge/decode.txt). Per page, per letter, first pass, against our 65% line.
- Shuffle control (shuffle_out.txt), 5,000 shuffled keys per seed, la-letters model, mean log-probability per character:

| split | real key | shuffles mean (sd), seed 20261112 | best shuffle | z | shuffles at or above real |
|---|---|---|---|---|---|
| full | -2.299 | -7.650 (0.517) | -5.692 | 10.3 | 0 / 5,000 |
| held-out | -2.062 | -7.625 (0.517) | -5.241 | 10.8 | 0 / 5,000 |
| train | -2.444 | -7.625 (0.538) | -5.725 | 9.6 | 0 / 5,000 |

Seed 7 gives the same picture (z 10.2, 10.8, 9.5; 0 / 5,000 each).

## Gist (UNCHECKED: my own reading of the decode, not judged, not compared with any edition)
Not a recipe: a love charm, a conjuration of the herb rue (ruta), in Latin with north Italian spelling ("paradixi",
"santa misa", "mondi"). "I conjure you, rue, in the name of the Father, Son and Holy Spirit, by holy Mary mother of
our Lord Jesus Christ, by the 12 apostles, the 4 evangelists, the 3 patriarchs, the 24 prophets, the 10 choirs of
angels and archangels, by cherubim and seraphim, sun and moon, stars, all the saints of paradise, the heavens, air
and earth, by the incarnation of the Son of God, his birth, baptism, holy fast, passion, the holy cross on which he
deigned to die, his ascension and resurrection, by all the words said in the holy mass and all the good things of
the world, by which you, rue, have power and strength to do and fulfil all I wish. Amen." A second conjuration
"by the evil spirits" follows: whatever person the speaker touches with the rue, or has touched, is not to be let go,
stand, drink, eat, sleep or take carnal pleasure with anyone but the speaker, and is to love the speaker alone while
the rue is carried. Closing instruction: when the conjuration is made, gather the rue in the name of the person you
want to be loved by; "and let it be said three times".

## Clear text around the cipher (my reading, UNCHECKED)
- No heading on any of the three cipher pages. The cipher pages carry no clear text except numerals.
- p75, below the three struck cipher lines, ordinary Latin ear remedies: "Ad idem accipe amigdolas amaras ut nuchleos
  persicho[rum] ... in folio caulis ... ponatur in aure ..." and "Si granum vel lignum vel lapis vel aliud tale
  corpuschulum in auribus cecidit ...".
- p75 verso: more on removing objects from the ear, then "Ad dolorem aurium Rx medulla vituli recens cum vino ...
  Item sucus rute cum sanguine anguille calidum auribus inmissus quemlibet dolorem auris statim tolit" (rue juice with
  eel's blood for earache).
- p77: "Ad idem. Rx suchus rute cum sanguine anguille ..." (the rue remedy again), then wound cures and scrofula.
  So the charm sits among remedies that use rue, which may be why it was entered here.

## Open problems
1. Line ends on the verso are hidden in the gutter of OPenn's photograph (lines 2 to 12, about one to three letters
   each). Blocker: needs a flatter photograph or the book. Most are recoverable by sense, none was supplied.
2. Verso l.9, a blotted word (decoded "quoqon_e"), and l.7 "_um~": illegible in the image.
3. Doubtful letters kept as transcribed (14 flags): c/e and p/long-s look alike in this hand.
4. p76 l.4: the numeral "xx.iiij" has a blot in the middle (24, or a corrected 29?). p75 l.3 has "xij"(?) choirs of
   angels where p76 has "10".
5. "cunm iuro" at each start is as written (for "coniuro"): scribe's spelling or slip, not emended.
6. S01/S02 are plain scribal abbreviations ("p(ro)fetas", "angelo(rum)") used inside the cipher; left without a value.
7. Hirsch 1983 no. 646 not seen.
8. Not done here by rule of the brief: catalogue edit, profile.json, write-up page, PR. Catalogue 2130 needs its
   extent corrected (verso of 76 is cipher too) and its kind (charm, not recipe).
