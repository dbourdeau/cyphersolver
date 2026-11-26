# NOTE · catalogue 698 · the match of the strip's tiles to the reading's classes, from shapes alone · v1

*Model-written (M), `claude-opus-5-5`, session `eea13873`. Plan v7-M, §8 step 3. Not seen by the desk.*

**Seen when this was made:** the desk's 27 tiles (zip SHA-256 `0db938ad0b012b134c2a75f5a6a57fbbd520344e07e7382844276af6144fd484`, each tile checked against the stamped list); blind reading v3; frames 39 and 58.

**Not seen:** the order file; the tile script; frame 42; any letter of the strip; any stage A result. The cover file's rectangles have been in this chat's context since 05:33Z on 17 Nov; they were not used, and no height was measured.

## How it was made
- **The views.** `visser698/match_v1/view_tiles_and_classes_v1.py` (SHA-256 `6bf81cf2ad2d6eea2c606b793dcba8db7f7e0a228dc415e88b29b01ef341fb81`) redraws to the pixel the seven views that were looked at:
  - the 27 tiles at three times, as they are;
  - the tiles at five times, each stretched between its own 1st and 99.5th percentile;
  - up to six signs of each of the reading's 17 classes, sure ones first, from frame 39 and from frame 58 redrawn in frame 39's pixels.
  It cuts and draws, and reads nothing.
- **The match.** Each tile was set against the class sheets and against the reading's own words for each class, and called by eye.
  - **Sure** means the shape has every feature the class is defined by and nothing that another class has.
  - **Not sure** means it fits one class best but lacks a feature or has an extra one; the note names which.
  - **No class** means no class fits as well as a miss would.

## Weaknesses first
1. **One reader, by eye.** The tiles are 68 pixels square, rendered by the desk as darkness against the paper's own level. The message's signs are about 25 pixels wide on raw photostats. Scale, slant and stroke weight differ between the two.
2. **The reading's classes are themselves doubtful in places** (41 of its 120 signs).
   - Some classes may hide more than one sign of the strip. `Q` takes round, three-cornered and filled rings; three tiles go to `Q` and three to `P`, and two each to `T` and `R`.
   - That is not settled here: §8 step 5 leaves out a class that two strip signs give with different letters.
3. **This chat knows that a pass needs at least five classes the strip gives with a sure match and a sure letter.**
   - Six tiles are marked sure. Each was marked for its shape alone, but the knowledge could have leaned on the line between sure and not sure.
   - The second count of §8 step 9, with the doubtful matches, decides nothing.
4. **Seven tiles match no class, and three classes (`A`, `9`, `Y`) have no tile.** A key strip may hold signs the message does not use. A tile marked no class may also be a class sign too damaged or too unlike its class to call.
5. **The desk's cut.** Each tile holds what the desk's box holds. Two tiles (2 and 9) carry strokes at their edges that may be a neighbour's, and one (21) is mostly blot.

## The match
| Tile | Class | Sure | Shape |
|---|---|---|---|
| 1 | none | no | a short upright stroke with a speck at its right and a low dash; smaller than any sign of the message; a stray mark, or what is left of one |
| 2 | none | no | a long upright stroke on the right with a foot at its lower right, joined at the top by a bar to a knotted loop at the upper left, and two blots joined by a stroke low on the left; like no class as a whole; perhaps a sign with a neighbour's trace |
| 3 | none | no | a dense knot at the top left and a stroke down to the right that ends in a short fork; like 9 turned over, whose tail runs down to the left; no class |
| 4 | `4` | yes | a bar with two short strokes up at its left and a long slash down from its right end to the lower left |
| 5 | `T` | no | a thin stem under a slanted bar, not joined to it, with a dot at the bar's right end; T, but the bar slants and the dot stands to the right |
| 6 | `R` | yes | a stem, an arm up to the right from its top, and a dot in the angle |
| 7 | none | no | faint and broken: an arc along the top with a knot at its right end, a dot in the middle, a slash low at the left; like S or 9 in parts; no class |
| 8 | `Q` | yes | a round ring at the left of a slash, joined to its top |
| 9 | `K` | no | a crossing at the top, a round bowl below curling back to the left, and strokes at the lower right that may be a neighbour's; K most like, 3 next |
| 10 | `P` | no | a closed loop at the top right of a stem, a short dash at the upper left, and a second stroke from the stem's foot up to the right; P in its loop and dot, with a stroke P lacks |
| 11 | `T` | yes | a stem with a heavy bar across its top and a tick above the bar |
| 12 | `3` | no | a zigzag at the upper left and two parallel strokes down to the left through a bar: 3, turned |
| 13 | `S` | no | a bar along the top with a short stroke down at its left end, and a long slash from its right end down to the left; S without its foot, or 4 with its ticks turned down |
| 14 | `P` | no | a slash up from the lower left to a peaked loop at its upper right, with a dot at the upper left, and loose marks; P, or A if the loop is open |
| 15 | `H` | no | an upright stem, a roof from its top to the right that comes down in a second stem, and a dot between them; H in its roof, with a dot H has not shown |
| 16 | `Q` | no | a three-cornered ring at the left joined to a stroke up to the right, and a long stroke down to the lower right; the ring is that of the doubtful Q (2:653, 2:717, 6:616, 5:285), but the long stroke runs down to the right, where Q's slash runs down to the left |
| 17 | `E` | yes | a large open C with a stroke through its middle up to the right, blotted at the top |
| 18 | none | no | two strokes crossing at the top over a closed triangle with a leg down to the right; X above and Z's triangle below; no class |
| 19 | `2` | no | a spiral ring at the upper left, a stroke down at the right, and a base stroke from the lower left up to the right through it; 2 in its base, 9 or Q in its ring |
| 20 | `X` | yes | two crossing strokes, the long one ending in a hook at the lower left, with a dot; as the X at 2:368 |
| 21 | `V` | no | a heavy blotted slash with an angle opening to the lower right at its upper left; V if the angle is its wedge; the blot hides most of it |
| 22 | `R` | no | a tall stem with a foot, a bar to the right from its top, a dot under the bar; R, its arm flatter than R's |
| 23 | `P` | no | a short slash with a closed box on its right near the top; P, small and blotted |
| 24 | none | no | a ring lying on its side with a short stroke at its left and a dot below; like no class |
| 25 | none | no | a small blot with a short tail down to the right; too little to class |
| 26 | `Q` | no | a slash with a filled ring at its left, joined near its top; Q with a filled ring, as at 1:545 |
| 27 | `Z` | no | a flat bar on top from a corner at its left, a stroke down from its right end that closes the top, a tail down to the lower left, and a dash to the right at the waist; Z, with 3's bar |

## Counts (by script, from `STRIPMATCH_v1.json`)
- **Matched sure, 6:** `4`, `E`, `Q`, `R`, `T`, `X`, one tile each.
- **Matched not sure, 14:**
  - `P` three times;
  - `Q` twice;
  - `2`, `3`, `H`, `K`, `R`, `S`, `T`, `V` and `Z` once each.
- **No class, 7:** tiles 1, 2, 3, 7, 18, 24 and 25.
- **Classes of the reading with no tile:** `A`, `9`, `Y`.

## Next, by the plan
1. This file and `STRIPMATCH_v1.json` are hashed and stamped.
2. Then J. brings the desk's order file and tile script, each checked against its hash in the chain.
3. This chat fetches frame 42 and checks it against the cover file's hash.
4. It runs the tile script on the frame, and checks every tile at the place the order file gives it.
5. Only then are the strip's letters read.
