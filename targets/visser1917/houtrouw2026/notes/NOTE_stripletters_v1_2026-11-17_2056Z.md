# READING · catalogue 698 · the letters of the key strip, frame 42 · v1 · 17 Nov 2026

*Provenance. The model's words throughout (M). J.'s verbatim words: none; this note quotes him nowhere. Model on record: `claude-opus-5-5` (the third cipher chat, session `eea13873`), read from the log. Not seen by the desk. J.'s acts: he brought the desk's order file and tile script (his message of 20:44:12Z on 17 Nov), and the sealed plan whose §8 step 4 this follows rests on his rulings.*

## What this is
The letter or letters at each of the 27 places of the strip, read from frame 42 (NARA M1085 roll 302). The places are numbered as the cover file numbers its "signs" (1 = the first). The file is `visser698/STRIPLETTERS_v1.json`.

It was read after two things:
- the match of tiles to classes was stamped (`STRIPMATCH_v1.json`, 20:17:52Z to 20:17:53Z);
- the desk's tile script, run here, gave every tile again (chain entry 274).

`STRIP_v1.json` is not made yet. No stage A results file has been opened.

## Weaknesses first
1. **Poor resolution.** The frame is 1,240 by 600 pixels. The letters stand 10 to 25 pixels tall, and most are faint. Nine places are read sure, fourteen doubtful and four not at all.
2. **The order of the alphabet was used.** The strip lists the letters in order:
   - **Upper row:** a to n, with ll after l.
   - **Lower row:** o to y, with v written last.

   At 14 places, the shape fits the letter the order gives but would not be read as that letter on its own. There the letter is given, marked not sure, with `by_order: true`. Those 14 go only into the count with the doubtful pairs, which decides nothing (plan §8 step 9). None is among the sure pairs.
3. **Four places are not read** (null):

   | Place | Why |
   |---|---|
   | 15 | It is at the torn right end. |
   | 20 | Its mark has no shape. |
   | 25 | Its shape is like a printed A, where the order gives z. |
   | 26 | It is a cursive m or n with a flourish, which could be n with its tilde, rr, w or m. |

   Where the order would give a letter, the glyph field names it; it is not used.
4. **The letter of a place is taken as the mark above its sign.** The upper row stands that way: the printed K, L and LL are over places 11 to 13. So does the lower row: o, u, x and v are over places 16, 22, 23 and 27. A letter written over a neighbour's sign would pair wrongly. Places 14 and 15 stand closest: their rectangles overlap by 14 pixels across.
5. **The reader knew the order, and it may have shaped what was seen.** A reader who expects e after d may see a faint loop as e. The sure field is meant to guard against this, since no letter that rests on the order is sure. But where sure ends and doubtful begins is this reader's judgment.
6. **One reader.** No second reading has been made. The views are kept with their hashes, so that the desk can look at the same pixels.
7. **What the reader knew when reading:**
   - **The match was in context:** tile to class, stamped.
   - **The order file was not:** tile to place. It was read by script for the tile check, and its mapping appears in no tool output in the logs. That was checked by script, without printing the file, against the copy of the log from before the context was compacted and against the live log. So this chat did not know which class stood at which place.
   - **No stage A result was known.**
   - **The desk's file of the Bureau's words stays closed.**
8. **What else was seen on the frame.**
   - The strip lies on a black surround and is creased. Fold lines run through places 2 and 18 and beside places 20 and 25.
   - The right end is torn at place 15. To the left of places 1 and 16 the paper is blank.
   - Above the strip, on the black, lies a thin straight object with a knob, like a pin.
   - No other writing was seen in the window viewed, x 180 to 1,120 and y 130 to 470. Nothing outside that window was viewed. By its brightness it is the black surround: mean 16 above the strip and 12 below, against 168 on the strip.

## How it was read
All views were made from the frame as fetched (SHA-256 `503696999c8c…f90ac2cf1b`; pixel hash in mode L `d84111fd…2294f81d0`, the desk's). They are in `visser698/stripletters_v1/`. The order of viewing was:
1. **Two views of the strip at twice size,** then the same two with the 27 sign rectangles drawn on.
2. **Six sheets at three times size,** each place with the band above it.
3. **The doubtful letters at five times size,** some of them stretched on the paper's levels alone, so that the black surround is not taken for ink.
4. **Four wider views of the letter rows,** at 3.4 to 6 times size.

No view was made of anything outside the strip's window.

| View | SHA-256 |
|---|---|
| `view_left_x180-660_y130-470_2x.png` | `ab887ce471301bf2614c68e4c4dafed79e0b66165f0934d8721d68d726a0f1ba` |
| `view_right_x640-1120_y130-470_2x.png` | `7247d2fa0de6a46977efefa4d7f094cea46a287e7bc901a4586dfe67cb4c903c` |
| `overlay_left_x180-660_y130-470_2x.png` | `e573e2b5c61c3d4fb8dc78c8a3a4ea5250f5ae044cbb1e8fb5ecf85b35dbcf26` |
| `overlay_right_x640-1120_y130-470_2x.png` | `855f8c54061d1c7641eb53bd8f5e3394ec0f799e06e1c02a5169dcf4fecb050c` |
| `sheet_places_01-05_3x.png` | `6f8a8197b141d45f11457036d080ffbd8a1f6dd8b03872824a98ffdb54388a9a` |
| `sheet_places_06-10_3x.png` | `1a207a6b9e000836ff3a11ef3bf5a9e11ed1c0343a9f5b10f4bacd25eba89c78` |
| `sheet_places_11-15_3x.png` | `78b11530bc7d7042c14ff539e092a47f2e1b30758b79d3f9069cafa84afa2fff` |
| `sheet_places_16-19_3x.png` | `a81ce4cc9162a3e0fe0e907d83c6ffd2dbc6e5f33f61bd34a76457dd0d6cdcc3` |
| `sheet_places_20-23_3x.png` | `255ca0557ee763d314a9d36a680d5c9e5346909668a821a3ad54ff30bee92026` |
| `sheet_places_24-27_3x.png` | `f034452a21af73202df89747a9107668e06f827da0ac66c8e7bb8de127a80ca6` |
| `zoom_letters_01-02-05-06_5x.png` | `966c0447a51c35a70ae9d798a3f64c0fc81e5e51968f87883a3a9297b3390652` |
| `zoom_letters_07-08-09-10_5x.png` | `f2612f4e924510e6e1d5044f6a1300c36683c097a1d6811c22da411605f30347` |
| `zoom_letters_14-15-17-18_5x.png` | `80e22187379752628770b427ce8925c783fffdf779c2fe0857adfa714113496b` |
| `zoom_letters_19-20-21-25_5x.png` | `d2763d8e16534ab7d655f0d1b1fd2afbb579b60dd4b55a004cd483110f570ba3` |
| `zoom_letters_26_5x.png` | `6b6eb36994160f458789ba6d761cc96af944cf44a1b725faa6874b0ef8d3a67c` |
| `zoom_letters_13-14-15-20_5x_levels.png` | `82e6e82490981c3b451a0f4ac2ac9c1374d393f51eb02a7882e8caaad337d215` |
| `zoom_letters_03-04-16-22_5x_paper.png` | `0b822a0b83c267242a6375870b0ed91f79a4635bc84747e823149a0e0932b798` |
| `zoom_letters_23-24-27-11_5x_paper.png` | `51c5f69140c0b18a98efeee9902254a38abd915a8d04b191c24843a1da1aeb3c` |
| `wide_letters_row2_x420-640_y290-390_6x.png` | `879aa8a01f41675734206cdea46f84df18d9b4dc234d8e41164e65c62394ff67` |
| `wide_letters_row1_x255-700_y205-300_3.4x.png` | `4379eb835a586327c286b1a30ef1186242f276ad6141f86f91dcec325a858bce` |
| `wide_letters_row2_x290-440_y300-400_5x.png` | `9bcff399cce694407214a6d3ff66299a878adba04c9dc1acd25b25e95067dc53` |
| `wide_letters_row2_x720-900_y250-350_5x.png` | `050b863efd1ba7409a410573b3884d6898990da93112f762c4d6655731b6852d` |

## The letters

| Place | Letter | Sure | By the order | What the shape looks like |
|---|---|---|---|---|
| 1 | a | no | yes | a loop with a tail running to the right, faint: a cursive a, or a Q |
| 2 | b | no | yes | a tall stem with a small bowl at its foot; a fold line runs through it |
| 3 | c | no | yes | one curve with a hook at its upper left, open to the upper right |
| 4 | d | **yes** | no | a loop with an upright stem at its right and a short tail: a cursive d |
| 5 | e | no | yes | a small loop with a tail, faint: e, or a |
| 6 | f | no | yes | a long stroke rising to the right, crossed by a shorter one: f, or x |
| 7 | g | no | yes | a long stroke rising to the right, a faint loop at its upper left |
| 8 | h | no | yes | an upturned V, the left leg the longer: h, or a cursive i |
| 9 | i | no | yes | the shape of place 8, smaller: i, or h |
| 10 | j | no | yes | two dark strokes crossing: j, f or x |
| 11 | k | **yes** | no | a printed K |
| 12 | l | **yes** | no | a printed L |
| 13 | ll | **yes** | no | two printed Ls |
| 14 | m | no | yes | an upright stroke with an upturned V beside it: M with its last leg lost, or N |
| 15 | not read | | | at the torn end; would be n by the order |
| 16 | o | **yes** | no | a closed oval |
| 17 | p | no | yes | a stroke rising to the right, crossed near its top by a curved bar: p, t or x |
| 18 | q | no | yes | a faint loop just right of a fold line: q, or g |
| 19 | r | no | yes | a thick stem with arms like a Y: r, or y |
| 20 | not read | | | a small mark beside a fold line; would be s by the order |
| 21 | t | no | yes | an upright stroke, a bar to the right at its top, a foot: t, or E without its middle bar |
| 22 | u | **yes** | no | two cups with a lead-in stroke |
| 23 | x | **yes** | no | two straight strokes crossing |
| 24 | y | **yes** | no | two arms over a long stroke ending in a loop to the left |
| 25 | not read | | | like a printed A with a bar; the order would give z, which it does not look like |
| 26 | not read | | | a cursive m or n with a flourish: ñ, rr, w or m |
| 27 | v | **yes** | no | a printed V in dark ink, perhaps gone over |

**Counts.**
- **Sure:** 9. That is 8 single letters (d, k, l, o, u, x, y, v) and one pair, ll, which the plan leaves out of n (§8 step 6).
- **Doubtful:** 14.
- **Not read:** 4.

The plan's forecast, "The strip gives five or more legible pairs", at 0.75, is scored only once `STRIP_v1.json` is made: a pair needs the match sure as well.

## Next, in the plan's order
1. `make_strip_v2.py` is run with the order file, and `STRIP_v1.json` is stamped.
2. Only then are the three stage A results files opened, and `strip_check_v1.py` is run.
