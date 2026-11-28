# vind1647: reading (Danish, 17th-century spelling)

From `decryption.txt` (key.tsv applied to transcription.txt). One AI reader (Claude Opus 5.5, 26 Nov 2026); no person
has checked it. The decryption column is `decryption.txt` as it stands. In the reading column, punctuation is added,
u/v and o/ø are normalised where the sense is clear (uere = være, forst = først, blod = blød), and square brackets mark
a hole: [wanted / cipher gives], or [word] alone where the cipher gives the word but a sign of it was re-read after the
solve on the sense alone. Word by word with status: `python3 -I targets/vind1647/count_words.py`.

| line | decryption | reading |
|---|---|---|
| 01 | kiere broder ieg fick dit breff | Kiere [broder], ieg fick dit breff |
| 02 | fra min moder udi afften forst och | fra min moder udi afften. Først, och |
| 03 | som det skal uere giort mit ingenium | som det skal være giort, mit ingenium |
| 04 | at exercer quasi saa er dette ald for | at [exercere / exercer]: quasi saa er dette ald for |
| 05 | ringe der til men faar at legge ander= | ringe der til, men faar at legge ander- |
| 06 | ledis dikt hoffued udi blod forend | ledis [dict? / dikt] hoffued udi blød, forend |
| 07 | din uille der udi kand skee ieg for= | din uille der udi kand skee. Ieg for- |
| 08 | undrer mig paa at det icke uar subtiler | undrer mig paa at det icke uar subtiler, |
| 09 | efftersom der haffuer uerit grende cant= | efftersom der haffuer uerit [trende / grende] cant- |
| 10 | zelister der offuer ocd haffer huercken | zelister der offuer, [och / ocd] haffer huercken |
| 11 | staffueh ret icke heller alle bogsta= | [staffued / staffueh] ret, icke heller [alle] [bogsta- |
| 12 | pfuer inford | ffuer / bogstapfuer] [indført? / inford]. |

Notes on the reading:
- "udi afften": this evening. "exercere": the final e is not written (a hole).
- "legge ... hoffued udi blød": the Danish idiom "to put one's head in soak", to think hard.
- "broder" (line 1) and "alle" (line 11): the second sign of each was re-read after the solve on the sense alone (frozen
  reading y and d, blind reading g and h), so both are holes.
- "mig" (line 8): the writer first wrote img (= min) and put n (= g) over the g, making "mig".
- "udi" (line 7): its first sign is t in the first transcription and l in the blind one; with l the word would be "kdi"
  (a hole). Counted read.
- d and h are a pair of the reciprocal key; two holes, "ocd" and "staffueh", are that pair confused. "grende" for
  "trende" has the g sign where t is wanted. "bogstapfuer": both readers saw an e-like sign (cipher e = p) where f is
  wanted.
