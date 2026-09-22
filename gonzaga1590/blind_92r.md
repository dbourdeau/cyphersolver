# f. 92r blind re-transcription (21 Sept 2026)

Independent transcription from 4x crops (grayscale + autocontrast, ~420 px pieces with overlap,
`%TEMP%\gz_blind92r`), made before opening `ct_92r.txt` / `reading.md`. Line centres measured from the ink
profile: P2 y≈1960 (line 2); P3 y≈142, 324, 500, 671, 844, 1029, 1207. Decoded with `beam.py` / `beam2.py`, then
compared with `ct_92r.txt` and the doubtful places re-cropped (P2 x1500-3150 y1890-2030; P3 x1900-3300 y70-215).
Tokens = figure pairs + signs.

## (a) P2 line 2 (p1l1b + p1l2 + p1l3), "non lo potendo … del quale"

    12 13 31 31 32 40 35 | 80 28 15 13 13 62 21 29 82 83 93 13 02 53 13 53 63 51 62 33 13 93 62 51 23 11 40 23 35 72 84 30 13 36 35 16 40 15 31 24 38 23 32 39 16 15
    (phase as decoded) … 30 25 31 35 | 36 35 16 23 31 39 | 36 25 [1] 23 1?5 40 23 35 | 72 | 84 | 30 13 | 36 35 16 40 15 31 24 38 23 32 39 16 15

- decode: far riso[l]uere a fauor loro **contro cotesto [72 Regno di] [84 Francia]** la conseruatione
- vs ct_92r: ct has `…35 59 36 35 16 23 31 39 93 62 51 23 11 40 23 35 72 04 30…`. The re-crop shows `…35 | 36 35 16 23 31 39 | 36 25 …`
  (no 59, no second 9) and **`72 84`** where ct has `72 04` (it is the looped 8, the same shape as in "84 Francia" at the end of the letter).
- Italian: "non lo potendo far risolvere a favor loro contro cotesto Regno di Francia, la conservatione del quale è
  desiderata…". This fits the context: the Pope would not be turned against France.
- verdict: **read**. One stray digit (the `1` after `co`, or `12`→`2`) is left as the writer's slip or a misread.
- newly read: 15 tokens (contro 6, cotesto 7, 72, 84). Still unread: 1 stray digit.

## (b) P3 l1 (p1l3b), "e desiderata da tutti i buoni" → "conoscendosi"

    15 21 36 40 37 21 15 31 22 | 22 33 21 30 23 27 23 34 37 19 20 39 16 37 | 32 23 22 30 37 38 16 34
    (re-crop of the blot: … 23 34 37 | 19 28 39 16 37 | 32 23 22 30 37 38 16 34)

- decode: e desiderata da tutti i buoni **italiani**
- vs ct_92r: ct `…37 93 73 22 23 22 29 0{blot}37 37 38 16 34` has lost phase. Under the blot the figure is the `0` of `30`.
  The run reads `16 37 | 32 23 22 30 37 38 16 34` = "ni | italiani" (20 digits, even, no fix needed).
- Italian: "…desiderata da tutti i buoni Italiani, conoscendosi…"
- verdict: **read**.
- newly read: 8 tokens (italiani). Still unread: 0.

## (c) P3 l2 (p1l4), after "conoscendosi P.{che}" → "cotesta potenza … Spagnoli"

    {che} 38 16 3 2 2 36 14 37 30 38 23 22 | 36 35 23 15 40 23 38 | 17 35 23 15 16 20 22 {M} 30 37 | 11 15 21 36 40 37 11 34 | 96

- decode: {che} **a n[i?] chilata** cotesta potenza {M} li medesimi [96 Spagnoli]
- vs ct_92r: ct `38 16 33 22 36 14 33 73 03 82 23 22`. I see a single `3` after `16`, not `33`, and `37 30 38` where ct has
  `33 73 03 82`. That gives "a n i c h i l a t a" with one extra `2` (a `3 2 2` group where `32` is expected).
- Italian: "conoscendosi P[apa?] che, annichilata cotesta potenza, li medesimi Spagnoli procureranno…". The sense fits:
  once France is destroyed, the Spaniards will try to subject everyone.
- verdict: **read**. One stray digit remains.
- newly read: 10 tokens (anichilata). Still unread: 1 stray digit; {M} sign value unknown (as before).

## (d) P3 l3 (p1l5), "procureranno … da {che}"

    17 31 25 36 24 31 15 31 13 16 39 21 34 40 25 23 35 17 35 31 40 32 22 25 18 16 28 16 35 30 13 16 2? 21 22 22 2? 33? 8? 22 21 37 {⊡} 22 21 38 {che}

- decode: procureranno di **sottoporsi** a ognuno [la n d a a a (c) a di] {⊡ S. Ecc.za} [a] da {che}
- vs ct_92r: ct has three extra `33`s (`25 33 36`, `23 33 35 17 33 35`). The crops show plain `40 25 23 35 17 35 31 40 32`,
  so "sottoporsi" stands as written with no emendation needed. The ct note wanted 33→34 plus a dropped 33.
  The tail `30 13 16 (16) 21 22 22 (22/38) 21 37` still gives no Italian ("la nda aa di").
- verdict: head **read** (confirmed, no longer doubtful), tail **unread**.
- newly read: 0 (9 tokens of "sottoporsi" confirmed as written). Still unread: about 10 tokens.

## (e) P3 l5 (p1l7), after "il che" → "chiaramente"

    32 30 {che} 40 15 18 28 36 16 21 39 | 40 34 | 24 15 21 15 | 36 14 37 38 31 22 11 15 16 23 15 | 22 17 15 31 23 22 | 22 30 38

- decode: il {che} seguendo **si vede** chiaramente aperta alla
- vs ct_92r: ct `40 11 15 18 … 21 13 39 40 34 34 24 15 21 11 15 36 14 37 37 38`. The crops show no `11` after `40`, no `13`
  before `39`, one `34` and one `37`. That is `40 34 | 24 15 21 15` = "si vede". The extra `15`/`16`/`22` in my raw
  string came from crop overlaps and were removed.
- Italian: "…il che seguendo, si vede chiaramente aperta alla via della grandeza…"
- verdict: **read**.
- newly read: 6 tokens (si vede). Still unread: 0.

## (f) P3 l6 (p1l8), after "grandeza a di {sign}" → "a questo Regno di Francia"

    27 34 22 21 3? 30 38 18 31 38 16 21 15 20 22 22 21 32 {sign} 15 23 1?3 3 0 3 8 3 3 | 33 24 3? 2 21 5 2 3 | 23 3̄6 22 13 22 3 6 | 36 25 23 15 40 2 2 33 39 72 84

- decode: [u]ia d[e]lla grandeza a di {sign} [e t a l a c c u i … e t c e a a … c o t e s] a qu[e]sto [72 Regno di] [84 Francia]
- vs ct_92r: my digits agree with ct on the head ("uia della grandeza a di") and on the end (`39 72 84`). In the middle
  they differ in phase at several places (ct `15 23 31 33 30 38 38 33 33 24 38 32 21 15 22 33 36 22 21 32 22 36 23 26 22`).
  Neither version gives Italian ("e tal acqu…" is tempting, but it does not continue). An overbar-like stroke over
  `3 6` in the middle (P3 x≈2200, y≈1180) could be a doubling bar, but it may also be the 6's ascender. The sign
  before `15 23` is a filled circle with a small cross below: ct reads it as {che}, it could be ⊕.
- verdict: middle **unread**.
- newly read: 0. Still unread: about 27 tokens.

## Totals for these six stretches

- newly read: **39 tokens** (a 15, b 8, c 10, e 6)
- confirmed as written: 9 (d "sottoporsi")
- still unread: **about 37 tokens** (d tail ~10, f middle ~27), plus 2 stray digits in (a) and (c)
