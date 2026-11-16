# Trinity College Cambridge O.4.22, f. 248v: not a cipher, a Paschal full-moon table

Catalogue entry 2902. Cambridge, Trinity College, MS O.4.22 (James 1253; Gregory-Aland l 186), f. 248v,
a Greek Gospel lectionary of the 11th-12th century. Images: [CUDL page image 503](https://cudl.lib.cam.ac.uk/view/MS-TRINITY-O-00004-00022/503)
(downloads CC BY-NC 4.0, © The Master and Fellows of Trinity College, Cambridge; not committed here).

## What is on the page

At the foot of column 2, the reader Ioannes greets "my teacher, arch-priest and cousin"
(Ἐγὼ Ἰωάννης ἀναγνώστης χαιρετίζω τὸν διδάσκαλόν μου, ἀρχιερέα καὶ ἐξάδελ-). Below, across both
columns, three faint lines of 38 Greek letter-numerals. The last words of the note, "φον" and "μου",
are written in minuscule at the right ends of numeral lines 1 and 2 (CUDL leaves them out).

The CUDL description (C. Wright) calls the numerals a cryptogram not decipherable by the common Greek
systems, perhaps hiding the dedicatee's name.

## Reading

The numerals are 19 pairs: a running count Α, Β, Γ ... ΙΘ (1-19), each followed by a value
(Daniel's suggestion in the catalogue). The values are the Paschal full moons ("legal Passover")
of the 19-year cycle, day of the month only, March for 21-30 and April for 1-18:

| year | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ms | Β | ΚΒ | Ι | Λ | ΙΗ | Ζ | ΚΖ | ΙΕ | Δ | ΚΔ | ΙΒ | Α | ΚΑ | Θ | ΚΘ | ΙΖ | Ε | ΚΕ | ΙΓ |
| date | 2 Apr | 22 Mar | 10 Apr | 30 Mar | 18 Apr | 7 Apr | 27 Mar | 15 Apr | 4 Apr | 24 Mar | 12 Apr | 1 Apr | 21 Mar | 9 Apr | 29 Mar | 17 Apr | 5 Apr | 25 Mar | 13 Apr |

The years are those of the Byzantine lunar cycle (κύκλος σελήνης), which runs three behind the
Alexandrian golden number (year 1 = golden number 4), as follows from the world era AM = AD + 5508.
The dates are the standard Julian computus: 21 March + (19(GN-1) + 15) mod 30.

So no name or message is hidden: the reader wrote a computus aid below his note. Pairs and doubts:
`pairs.tsv`.

## Check

`results/measure.py` (sha256 01a463dd5ba3a1b50afc370abc20e8e17da0c044c2893db8e4cfdd3d558a6a94, frozen
before it was run): 19 of 19 values equal the computus date with offset 3; 200 shuffles of the values
over the counts give at most 4 of 19 (mean 1.0); every other offset 0-18 gives 0 of 19
(`results/measure_output.txt`). The hypothesis came from looking at the values (value + count repeats
13, 34, 23 for counts 3-14), so this is a confirmation on the same 38 numerals, not a held-out test;
there is no further text. A chance match of 19 values from 30 possible days each is about 30^-19.

## Transcription

Read on contrast-enhanced full-resolution crops (16 Nov 2026) and collated with CUDL. The reading of
the CUDL string was known beforehand. Differences and doubts:

- "φον" (end of line 1) and "μου:" (end of line 2): minuscule, end of the clear note; not in CUDL.
- Count 5 value ΙΗ: the ink shows Ι and two Η-shaped signs (this hand writes Η like Π); dittography?
- Count 14: CUDL ΙΑ; Δ and Α look alike in this hand; the computus needs ΙΔ.
- Count 18 value ΚΕ: after Η a small group with a tilde, then a point, then Κ Ε; the Ι of the count
  ΙΗ is uncertain.
- CUDL's grouping "Δ ΛΕ", "ΙΚ Δ", "Κ· Β" is Δ | Λ, Ε | ..., Ι | ΚΔ, and ΚΒ (one value with a point).

## Prior art

CUDL record: "remains to be resolved". Web searches on 15 and 16 Nov 2026 found no published solution.
Not searched: the Pinakes bibliography, Gardthausen and Mioni on Byzantine scribal cryptography.
