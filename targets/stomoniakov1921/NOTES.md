# Letter traffic to Stomoniakov, 1921: shared solver and unbroken messages

Status: in progress

Each message has its own key, so each deciphered one has its own folder: `lejava1921`, `voikov1921`; `voikov1921b` is decoded, not read. The figure traffic in the same file is `kopp1921`.

## Letter traffic: a transposition

`letters.py` finds runs of 5-letter groups, mostly to Stomoniakov under Kopp's or Lutovinov's address: 041-0787 (Lejava,
5 Apr), 042-0250 (Lejava to Kopp, 26 Apr), 042-0614 (Voikov, 5 May), 042-0627 (Krasin, 16 May), 042-1272 and 1273
(Voikov, 1 June), 043-0436 (Voikov, 16 June), 043-0577 (Lejava). Also 042-0258 (Bronsky, Vienna), which has W and X
and may be in another language.

Measured on the Stomoniakov set (2,310 letters, OCR): O 11.3, I 10.0, E 8.8, A 7.4, T 6.3, N 6.1, R 5.1, S 4.9, D 4.4,
V 4.1. Russian letter frequencies with no substitution, so a transposition of transliterated Russian is the working
hypothesis. Tiltman describes that system on the London link before Nov 1920.

Each carries a number pair in clear, repeated at the end: 01135-26205, 01135-35283, 00908/24898, 01009/32084,
00602/21574, 01115/24763. Reading the first number as a page and line is a guess. The two 01135 messages share a date.

`voikov1883.txt` (Nr 1883/1188/S, 042-1273) is read from the image: 615 letters, about 4 lost.

- `synth.py`: on synthetic Russian the solver gets -3.0 to -3.4 at widths 12 and 24 in 30,000 steps, and fails at 35.
  Real text scores -2.13.
- `run1883.py`: columnar, widths 5-36, both read directions, 120,000 steps, 2 restarts: best -4.825 at 36, rising with
  width, no words. `focus.py`: widths 22 and 23 match shuffled controls (-5.3 against -5.3; -5.26 against -5.23).
- `dbl.py`: double columnar, all permutations up to width 5 x 5: best -5.06, no text.
- Width 24 broke Nr 1883 (`w24.py`, `polish3.py`, key in `keyA3.json`), with `Q` for the soft or hard sign, `zpt` for comma, ending `prodslid`. Earlier runs above were under-searched: the same width had looked like noise at 120,000 steps with a poorer model.
- The two 01135 messages do not share a key (`testB.py`). The second number differs, so the pair may name the key instead; untested.
- `B20*.py`: the other 01135 message breaks on its own key at 20 columns, gap about 42. It opens `prod`, as Nr 1883 predicts.
- `runF.py`: Lejava Nr 1196, read from the image, breaks at 11 columns (-3.47, control -4.47; polished -2.74). Ranking widths by raw score had hidden it: wide widths overfit short messages, so compare with a control at each width and read the text.
- Lejava 26 April (`m0426.txt`, start lost): width 22 gave -3.95 against -4.25, but `pre.py` found nothing across lost-prefix lengths: not broken. It has many Z and T.
- Voikov 16 June (`m0616.txt`): 450,000 steps, 3 restarts, widths 19-36: best -4.03, level with control; not broken, and widths above 36 are untested. Voikov 5 May (`m0505.txt`) and Krasin 16 May (`m0516.txt`): scanned at low widths, no break. 043-0577 has gaps from static and is not attempted. 042-0258 (Bronsky) and 045-0248 (Nikolaev to Prague) not attempted from images.

