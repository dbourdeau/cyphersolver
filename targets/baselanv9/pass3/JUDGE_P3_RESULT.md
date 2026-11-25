# Basel UB AN V 9, pass 3: independent judge result

Judged 25 Nov 2026 (Brisbane). Inputs read: `judge/BRIEF.txt` and `judge/decode.txt` only. RESULT.md, RUN_RECORD.tsv, SCORE_P3.tsv, the key, the rules file and earlier judge output were not opened. Nothing sent or posted.

## Bottom line (letters, S/(S+E+N), no pooled figure)

| section | status | S | E | N | total | central | range on my own calls |
|---|---|---|---|---|---|---|---|
| H1r (f.15r l.1-12) | re-read, not held out | 399 | 6 | 0 | 405 | 399/405 = 98.5% | 394/405 = 97.3% to 400/405 = 98.8% |
| H4 (f.25r l.1-12) | held out | 389 | 9 | 17 | 415 | 389/415 = 93.7% | 386/415 = 93.0% to 398/415 = 95.9% |
| S2 (11 rims) | second series | 486 | 10 | 25 | 521 | 486/521 = 93.3% | 479/521 = 91.9% to 500/521 = 96.0% |

My letter totals equal the decode file's own headers (405, 415, 521).

## H1 without decoder rules C4 and C5: not done

The brief does not mention C4 or C5 and names no rules file, key or alternate decode. A judge limited to the brief and decode.txt cannot tell which letters those rules produced. No figure is given. It needs a second decode run without C4 and C5, judged the same way.

## Method

- Unit: the word. S = all its letters S. E = one letter E, the rest S. N = all letters N. Two swapped letters = N.
- A word broken with "=" is judged as one word; its letters are counted on the line where they stand, and the E letter on the line where the slip stands.
- "~" is not a letter. `ch~ri` = christi, the usual chri-with-bar contraction: S, 4 letters each (7 instances). `dni~` = domini: S, 3 letters. `quae~`, `qui~`, `uirtut~um`: the letters already spell the full word, so S; the bar is redundant and not counted.
- [?] standing alone (H4 L02, H4 L04) holds no letters and is not scored. `ne[?]` = nec: S. `exel[?]us` = excelsus with [?] as s and c missing, one further slip: S under the brief's rule. `t[?]=rar`: not recognisable, N.
- `trans` (H1r L11) and `figurationem` (L12) have no "=" between them; S whether taken as one word or two.
- A real Latin word that is one letter off the form the sentence needs (situs, aere, erus) is called E, not S.
- Low and high are every doubtful call taken against, then for, the decode.
- Arithmetic by script (`python3 -I`), per-line sums shown under each table.

## H1r

| line | S | E | N | total | S/(S+E+N) |
|---|---|---|---|---|---|
| L01 | 43 | 0 | 0 | 43 | 43/43 = 100.0% |
| L02 | 39 | 1 | 0 | 40 | 39/40 = 97.5% |
| L03 | 40 | 0 | 0 | 40 | 40/40 = 100.0% |
| L04 | 38 | 0 | 0 | 38 | 38/38 = 100.0% |
| L05 | 35 | 1 | 0 | 36 | 35/36 = 97.2% |
| L06 | 12 | 0 | 0 | 12 | 12/12 = 100.0% |
| L07 | 14 | 0 | 0 | 14 | 14/14 = 100.0% |
| L08 | 36 | 1 | 0 | 37 | 36/37 = 97.3% |
| L09 | 36 | 1 | 0 | 37 | 36/37 = 97.3% |
| L10 | 33 | 0 | 0 | 33 | 33/33 = 100.0% |
| L11 | 37 | 1 | 0 | 38 | 37/38 = 97.4% |
| L12 | 36 | 1 | 0 | 37 | 36/37 = 97.3% |
central: S 399, E 6, N 0, total 405; S/(S+E+N) = 399/405 = 98.5%; (S+E) = 405/405 = 100.0%
low: S 394, E 5, N 6, total 405; S/(S+E+N) = 394/405 = 97.3%; (S+E) = 399/405 = 98.5%
high: S 400, E 5, N 0, total 405; S/(S+E+N) = 400/405 = 98.8%; (S+E) = 405/405 = 100.0%
sum of S column: 43 + 39 + 40 + 38 + 35 + 12 + 14 + 36 + 36 + 33 + 37 + 36
sum of totals: 43 + 40 + 40 + 38 + 36 + 12 + 14 + 37 + 37 + 33 + 38 + 37

## H4

| line | S | E | N | total | S/(S+E+N) |
|---|---|---|---|---|---|
| L01 | 33 | 1 | 0 | 34 | 33/34 = 97.1% |
| L02 | 25 | 1 | 0 | 26 | 25/26 = 96.2% |
| L03 | 37 | 2 | 0 | 39 | 37/39 = 94.9% |
| L04 | 31 | 1 | 0 | 32 | 31/32 = 96.9% |
| L05 | 37 | 0 | 0 | 37 | 37/37 = 100.0% |
| L06 | 28 | 0 | 5 | 33 | 28/33 = 84.8% |
| L07 | 36 | 1 | 0 | 37 | 36/37 = 97.3% |
| L08 | 35 | 1 | 0 | 36 | 35/36 = 97.2% |
| L09 | 27 | 2 | 4 | 33 | 27/33 = 81.8% |
| L10 | 25 | 0 | 8 | 33 | 25/33 = 75.8% |
| L11 | 38 | 0 | 0 | 38 | 38/38 = 100.0% |
| L12 | 37 | 0 | 0 | 37 | 37/37 = 100.0% |
central: S 389, E 9, N 17, total 415; S/(S+E+N) = 389/415 = 93.7%; (S+E) = 398/415 = 95.9%
low: S 386, E 8, N 21, total 415; S/(S+E+N) = 386/415 = 93.0%; (S+E) = 394/415 = 94.9%
high: S 398, E 8, N 9, total 415; S/(S+E+N) = 398/415 = 95.9%; (S+E) = 406/415 = 97.8%
sum of S column: 33 + 25 + 37 + 31 + 37 + 28 + 36 + 35 + 27 + 25 + 38 + 37
sum of totals: 34 + 26 + 39 + 32 + 37 + 33 + 37 + 36 + 33 + 33 + 38 + 37

## S2

| line | S | E | N | total | S/(S+E+N) |
|---|---|---|---|---|---|
| S2-02 | 49 | 1 | 0 | 50 | 49/50 = 98.0% |
| S2-03 | 39 | 1 | 0 | 40 | 39/40 = 97.5% |
| S2-04 | 38 | 1 | 0 | 39 | 38/39 = 97.4% |
| S2-05 | 4 | 0 | 13 | 17 | 4/17 = 23.5% |
| S2-06 | 40 | 0 | 0 | 40 | 40/40 = 100.0% |
| S2-07 | 50 | 0 | 0 | 50 | 50/50 = 100.0% |
| S2-08 | 47 | 2 | 0 | 49 | 47/49 = 95.9% |
| S2-09 | 54 | 1 | 7 | 62 | 54/62 = 87.1% |
| S2-10 | 59 | 1 | 0 | 60 | 59/60 = 98.3% |
| S2-11 | 51 | 2 | 5 | 58 | 51/58 = 87.9% |
| S2-12 | 55 | 1 | 0 | 56 | 55/56 = 98.2% |
central: S 486, E 10, N 25, total 521; S/(S+E+N) = 486/521 = 93.3%; (S+E) = 496/521 = 95.2%
low: S 479, E 9, N 33, total 521; S/(S+E+N) = 479/521 = 91.9%; (S+E) = 488/521 = 93.7%
high: S 500, E 9, N 12, total 521; S/(S+E+N) = 500/521 = 96.0%; (S+E) = 509/521 = 97.7%
sum of S column: 49 + 39 + 38 + 4 + 40 + 50 + 47 + 54 + 59 + 51 + 55
sum of totals: 50 + 40 + 39 + 17 + 40 + 50 + 49 + 62 + 60 + 58 + 56


## Every word not called S, and every doubtful call

Columns: line, word, letters, central, low, high, reason.

| line | word | letters | central | low | high | reason |
|---|---|---|---|---|---|---|
| H1r L02 | sactorum | 8 | E | E | E | sanctorum, n missing |
| H1r L05 | pmer | 4 | E | E | E | per, m added |
| H1r L08 | dimones | 7 | E | E | E | demones, i for e |
| H1r L09 | situs | 5 | E | E | S | sitis expected (uos ... sitis); situs is a word but does not fit |
| H1r L11 | baptisum | 8 | E | E | E | baptismum, m missing |
| H1r L12 | atundi= | 6 | E | N | E | arundi[nem], t for r; rest of word lies beyond the passage |
| H4 L01 | sugit | 5 | E | E | E | surgit, r missing |
| H4 L02 | aere | 4 | E | E | S | aerem expected after amplexari, m missing |
| H4 L03 | nooen | 5 | E | E | E | nomen, o for m |
| H4 L03 | iestius | 7 | E | E | E | istius, e added |
| H4 L04 | oni | 3 | E | E | E | omni, m missing |
| H4 L06 | emloo | 5 | N | N | N | eloe/eloim? two or more slips |
| H4 L07 | ineffabale | 10 | E | E | E | ineffabile, a for i |
| H4 L08 | uidelichet | 10 | E | E | S | uidelicet, h added (could pass as spelling) |
| H4 L09 | ueus | 4 | E | N | E | deus or uerus, one slip either way |
| H4 L09 | ter | 3 | N | N | S | a Latin word but no sense in "deus ueus ter israel" |
| H4 L09 | imsrael | 7 | E | E | E | israel, m added |
| H4 L09 | t[?]= | 1 | N | N | N | t[?]rar: not recognisable |
| H4 L10 | rar | 3 | N | N | N | tail of t[?]rar |
| H4 L10 | gerum | 5 | N | N | E | regum = swap = N; rerum one slip but no clear fit |
| S2 S2-02 | mesteriosum | 11 | E | E | E | misteriosum, e for i/y |
| S2 S2-03 | erus | 4 | E | E | E | eris, u for i |
| S2 S2-04 | trasiens | 8 | E | E | E | transiens, n missing |
| S2 S2-05 | caraton | 7 | N | N | S | magic name, not verifiable by me |
| S2 S2-05 | mathoi | 6 | N | N | S | magic name, not verifiable by me |
| S2 S2-08 | ineffabale | 10 | E | E | E | ineffabile, a for i |
| S2 S2-08 | periculus | 9 | E | E | E | periculis, u for i |
| S2 S2-09 | ingribe | 7 | N | N | N | inscribe: g for sc, two slips |
| S2 S2-09 | commedendum | 11 | E | E | S | comedendum, m added (attested spelling) |
| S2 S2-10 | mirabala | 8 | E | N | E | one slip from mirabile; mirabili (the form needed) is two |
| S2 S2-11 | gribe | 5 | N | N | N | scribe: g for sc, two slips |
| S2 S2-11 | iouus | 5 | E | E | E | iouis, u for i |
| S2 S2-11 | aurgento | 8 | E | E | E | argento, u added |
| S2 S2-12 | liberabiutur | 12 | E | E | E | liberabitur, u added |

E count check: H1r 6 words = 6 E letters. H4 9 words = 9. S2 10 words = 10.
N check: H4 emloo 5 + ter 3 + t 1 + rar 3 + gerum 5 = 17. S2 caraton 7 + mathoi 6 + ingribe 7 + gribe 5 = 25.

## S2 per rim, range

| rim | central | low | high |
|---|---|---|---|
| S2-02 | 49/50 = 98.0% | 49/50 = 98.0% | 49/50 = 98.0% |
| S2-03 | 39/40 = 97.5% | 39/40 = 97.5% | 39/40 = 97.5% |
| S2-04 | 38/39 = 97.4% | 38/39 = 97.4% | 38/39 = 97.4% |
| S2-05 | 4/17 = 23.5% | 4/17 = 23.5% | 17/17 = 100.0% |
| S2-06 | 40/40 = 100.0% | 40/40 = 100.0% | 40/40 = 100.0% |
| S2-07 | 50/50 = 100.0% | 50/50 = 100.0% | 50/50 = 100.0% |
| S2-08 | 47/49 = 95.9% | 47/49 = 95.9% | 47/49 = 95.9% |
| S2-09 | 54/62 = 87.1% | 54/62 = 87.1% | 55/62 = 88.7% |
| S2-10 | 59/60 = 98.3% | 52/60 = 86.7% | 59/60 = 98.3% |
| S2-11 | 51/58 = 87.9% | 51/58 = 87.9% | 51/58 = 87.9% |
| S2-12 | 55/56 = 98.2% | 55/56 = 98.2% | 55/56 = 98.2% |

## Notes

- S2-05 swings the S2 range: caraton and mathoi are magic names I cannot verify from the brief. Central call N (13 letters); if accepted as names the rim is 17/17.
- "gribe" / "ingribe" (S2-09, S2-11) look like one systematic fault: a sign for sc decoded as g. Scored N both times as two slips.
- Recurrent single-letter faults: a or u where i is wanted (ineffabale twice, periculus, iouus, erus, situs, mirabala), and stray m or missing m (pmer, imsrael, oni, baptisum, nooen).
- H4 L09-L10 ("ueus ter imsrael qui super t[?]rar gerum") is the one stretch that does not read.
