# ercole1547 solve log (24 Nov 2026, Brisbane; times in FREEZE files are UTC)

Note made before solving: 276 signs (449 tokens with raised marks and dots) on one page is short. Brice Dudout's
annealing on the same letter did not converge (targets/ariosto1559/NOTES.md). The shuffle control might fail on length.

Split fixed in FREEZE_TX.txt: BUILD = lines 1-6 (216 signs), HELD-OUT = lines 7-8 (60 signs). Everything below used
lines 1-6 only. Language model: local 5-gram, no spaces, early spelling (work/build_lm.py: lang source it-gutenberg
+ Serristori legations x3, 10.2 M letters). The registry model it-cinquecento could not be built: gutenberg.org
answered 503.

| # | attempt | settings | result |
|---|---|---|---|
| 1 | Count of signs and marks by sign (structure, no values) | lines 1-8 for the inventory in SIGNS.md; lines 1-6 for the pairs | Two classes: S01 S02 S11 S12 S13 S17 S03 carry raised figures; S14 S10 S04 S19 carry strokes. S01^s is always followed by S02; S05^X always follows S03. Bars come with a dot |
| 2 | Annealing, marks ignored (model A: 25 signs -> letters, many-to-one) | work/solver.py A, seeds 1-3, 120k steps, no frequency term | FAILED: collapsed to "iiii..." (roman numerals in the corpus). Frequency term added (weight 4, L1 distance to Serristori letter frequencies) |
| 3 | Model A again | seeds 1-4, 150k steps | FAILED: raw -3.10 to -3.38 per letter, four different keys, no words. Not a simple substitution on the bases |
| 4 | Model B (bare sign = letter; raised figure = vowel, free; sign+stroke/bar = own letter) | solver.py B, seeds 1-4, 250k | NOT CONVERGED: raw -2.61 to -2.76, four different keys. But ^s = e in 4 of 4, ^6 = i in 4 of 4, ^7 = o in 4 of 4, ^4 = a in 3 of 4 |
| 5 | Model B2 (strokes and bars ignored) | seeds 1-4, 250k | FAILED: raw -2.95 to -3.17 |
| 6 | Model B3 (every mark is a following letter, any letter) | seeds 1-4, 250k | FAILED: raw -2.58 to -2.78, no agreement |
| 7 | Model C (every sign+mark its own letter, 75 symbols) | seeds 1-4, 250k | FAILED: raw -2.42 to -2.54, overfit, no agreement |
| 8 | Hypothesis from 4: raised figures 4 5 6 7 8 = a e i o u in order (the S-shaped mark is a 5) | by hand | kept as hypothesis H5 |
| 9 | Hypothesis: barred signs with dots are name codes | by hand | WRONG (see 11): they are doubled consonants |
| 10 | Model B5 (as B, vowels fixed by H5, barred signs break the chain) | work/solver2.py, seeds 1-6 planned, 200k; stopped after 5 | PARTIAL: seed 2 raw -2.19 reads "intenderete", "della grande impertan", "opera per intendere", "potrete", "e da credere", "sia per". Other seeds -2.46 to -2.80, no sense |
| 10b | B5 with S04 merged into S03 | seeds 1-5 | FAILED: -2.42 to -2.75 |
| 10c | B5 with vowels free | seeds 1-5 | PARTIAL: seed 1 raw -2.31 reads "intenderete", "potrete", "credere"; others fail |
| 11 | Pattern word, by hand, in parallel with 10: S09 S10 S11^5 S10 S12^5 S02^5 (twice, lines 1 and 3; once followed by S11^5) = "intendere", "intenderete". The word also stands in the clear lines of the letter ("vederete intendere") | lines 1 and 3 | HELD: gives S01^5 S02 = "per" (10 times), "opera per intendere", "piu che potrete", then the rest by sense |
| 12 | Values fixed one by one from lines 1-6 (basis for each in KEY.tsv) | | first idea S13^5 S14^- = "meglio" was WRONG; "quello / quella / quale / questo" fits all 5 uses (S13 = qu, bar = doubled l). Strokes on the second class are vowels: / a, \ e, I o. Bars double: ll, cc, ss |
| 13 | Key frozen (FREEZE_KEY.txt), then decode_once.py run once on all 8 lines | | DECODE.txt. Lines 7-8 read as Italian on the first pass |
| 14 | shuffle.py | 5,000 shuffles at seeds 20261112 and 7, values permuted within consonant bases, vowel bases and vowel marks | 0 of 5,000 shuffles reach the real key at either seed, on the held-out lines, the build lines and the whole page (shuffle_out.txt) |

Raw annealing outputs: log/anneal_*.txt. A process slip to record: `pkill -f "solver.py"` was used once to stop my own
first runs; it would also have stopped any other session's process with that file name. I cannot tell whether one was running at that moment; a check straight after showed other sessions' Python jobs alive.

## Weak or open key values (frozen as they are)

- ^9 = o: "cosa" wants o, "circa" wants a. One each in lines 1-6. The two marks may differ.
- ^2 = o: one use (como).
- S10 under a bar = "ni" (ogni, twice), although a bar doubles elsewhere.
- S12 with a cross-stroke (line 5): no value.
- S01^4s: a code for a person (twice). No value.
- S02^^ = "ri": one use, set by sense.
- S09 holds two signs that the transcription did not separate: the figure 6 (i) and a taller b/f-like sign.

## Emendations suggested by the decode (NOT applied; the first pass is the figure of record; none re-checked on the image after the decode)

| line | as transcribed -> decode | proposed | would give |
|---|---|---|---|
| 2 | S22^- -> "ss" in "e ss re" | value "sse", or a lost S21 | essere |
| 2 | S01^s S02 -> "per" in "impertanza" | S01^7 | importanza |
| 2 | S09 after S05^X -> "i" (the cross-arm runs into the sign; noted at transcription) | S09 with cross-stroke = fa | che facciate |
| 3 | S03^9 -> "co" | ^9 as a | circa |
| 4, 5 | S17^7 S11 -> "so t" (the 7 stands over the S11; noted at transcription) | S17 S11^7 | questo; "s to" |
| 5 | S02^^ S11 -> "ri t" (the S11 "looks y/g small"; noted at transcription) | S02 S04^\ | r[i]mediare |
| 5 | S12^s -> "de" in "essende" | S12^7 | essendo |
| 7 | S09 -> "i" in "de i rancesi" | the b/f-like sign = f | de Francesi |
| 7 | S18? -> "o" (flagged at transcription as possibly S02) | S02 | estraordinaria |
| 7 | S14^- -> "ll" in "dillgentia" | none; a missing i | dilligentia |
| 8 | S05^X -> "he" (drawn as an upright cross here; noted at transcription) | a second mark = hi | per chiarirvi |
