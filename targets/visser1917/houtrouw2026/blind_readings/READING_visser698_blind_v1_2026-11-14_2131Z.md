# READING · catalogue 698, the Kolbeck and de Visser symbol message · blind, v1

*Model-drafted (amber), session `78298d5e`, model on record `claude-fable-5-2`. Not seen by the desk. Read from NARA M1085 roll 302, frame 39 (JPEG, 992 by 1328 pixels, SHA-256 `7bfe35da…ed31efcc`), and from nothing else. Frame 42, the key strip, and everything on the quarantine list of 21:23Z were closed while this was made, and are still closed. No solver was run and no letter values were tried.*

## Weaknesses first
1. **This is a poor reading, and I would not seal a run on it alone.** The frame is a photostat at about 20 pixels a sign. Lines 1, 2, 7 and 8 are fairly clear. Lines 3 to 6 are creased and stained, and the right end of lines 5 and 6 is partly lost.
2. **The sign classes are tangled.** Several of my classes may be one sign written twice, or two signs I have merged. The worst cases are listed under "Classes I cannot keep apart".
3. **45 of 121 signs carry a question mark.** A mark means I would not be surprised to be wrong about the class.
4. **I counted 121 signs and 10 dividers.** The ledger's vetting line says about 170 to 200 signs. I cannot account for the difference: either I miss signs in the stained parts, or that count was a guess.
5. **One reader, one pass.** No second reading has been made, and no person has looked.

## How it was made
- An overview, then each line in two halves at six times the frame's size with a ruler in frame pixels (`ruler.py`; the images are `view/r_L<line><a|b>.png`).
- Positions are the sign's centre on the ruler, in frame pixels: `line:x`.
- An attempt to cut the lines into signs by dark columns failed and was not used (`segment.py`, `boxes_v1.json`): the ink is too grey.
- Faint diagonal strokes run down to the left under most signs. I took them for a double image of the photostat and did not read them.

## The classes (named by shape, not by any letter value)
| Label | Shape |
|---|---|
| `E` | a C with a bar through it |
| `T` | a T |
| `I` | an upright bar |
| `A` | two strokes meeting at the top, like a lambda |
| `X` | two crossing strokes |
| `S` | a stem with a bar at the top right and a foot |
| `R` | a stem or an angle with a short arm at the top right and a dot in the angle |
| `G` | a bold stem with a long arm from the top; no dot seen |
| `H` | a stem with a small caret at its upper right |
| `3` | a three, with a flat or hooked top |
| `K` | a three with a stroke crossing its waist |
| `2` | a loop at the top left, a stroke down, a base to the right |
| `9` | a loop on top with a tail down to the left (once) |
| `7` | a slash with a bar or a blob at its top left |
| `Q` | a slash with a ring or a blob at its left middle |
| `P` | a slash with a small loop on its right, near the top |
| `V` | a slash with a small angle and a dot at its top left |
| `Y` | an upright stem with two arms |
| `4` | a hook and a bar with a slash through, like a 4 |
| `t` | a stem with a bar through it |
| `-` | a divider: a dash between groups of signs |

A `"` after a label means two marks above the sign; a `?` means the class is doubtful; `alt=` gives the other classes it could be; `#` is unread.

**Classes I cannot keep apart.**
- `7`, `Q`, `P` and `V` are all a slash with something attached. Where the attachment is a blob I cannot tell a bar from a ring.
- `R`, `G`, `H` and `I` are all a stem with something at the top. The dot of `R` is often missing or doubtful.
- `3` and `K` differ by one stroke that the double image can fake. `S` and `3` are close when the top is flat.
- `E` is the surest class.

## The reading
```
L1  375 E | 405 T | 428 - | 447 S | 472 3 | 497 T | 517 3 | 545 7? alt=Q | 568 E | 597 S | 619 R? alt=G | 637 - | 655 E | 683 T | 708 3? alt=7 | 732 I? alt=T | 747 E | 775 A
L2  303 R? | 335 K | 368 X | 408 2 | 432 K | 450 R | 470 - | 505 E | 527 3 | 554 3"? alt=K | 572 Q? alt=7 | 600 R | 628 - | 653 7 | 672 P | 690 R | 717 7 | 738 R? | 762 3 | 787 2
L3  305 3? alt=K | 332 2 | 356 R? alt=I,7 | 382 H | 410 K? alt=3 | 438 3? alt=S | 460 - | 496 7? alt=3 | 527 4 | 558 Y | 586 t? alt=R,7 | 603 E"? | 628 P | 657 2? alt=9 | 684 H | 705 G | 725 7? alt=3 | 760 -?
L4  298 E | 338 P | 366 E | 390 S? alt=3 | 415 Q | 447 3 | 476 K | 502 E? alt=2 | 533 A? alt=X | 558 E? | 587 G | 617 - | 645 Q | 670 t? alt=T | 703 K | 732 7? alt=V | 760 Q | 787 R? alt=G
L5  285 t? alt=7 | 308 P | 334 R | 357 H | 387 Q | 410 R | 435 - | 461 E | 488 Q? alt=K | 513 E | 545 A? alt=X | 571 4? | 606 K? alt=3 | 640 - | 669 #? | 693 P? | 711 R? | 735 H? alt=T | 763 Q
L6  275 #? | 303 V | 335 2 | 358 V | 400 4? alt=3 | 426 E | 455 V | 478 7? alt=t,K | 503 E | 525 -? | 546 3 | 581 K? alt=3 | 616 7 | 646 Y? alt=T | 670 Q? | 699 K | 724 G? alt=7
L7  358 R | 388 P | 425 S | 456 K" | 485 Y | 512 4 | 549 9? alt=2
L8  440 R | 457 7? alt=I | 474 K | 494 P? alt=Q | 517 R | 539 7 | 561 3 | 588 7? alt=Q | 617 2 | 647 3 | 675 K | 700 V | 721 X | 744 E?
```

**Counts** (by script, from the block above). 121 signs: 76 without a mark, 45 with one, 2 of them unread. Dividers: 10, 2 of them doubtful. Line 7 ends short of the margin. Line 8 stands apart, lower and to the right, where a signature would be.

## Not done
- No second pass. A second reading of every marked sign at a larger size, with all signs of a class side by side, is the next step, and it too can be made with the quarantine closed.
- No counts by class, no index of coincidence, no trial of any letter.
