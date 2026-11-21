# Revenga 1822: blind transcription legend

Source: NARA M/T33 roll 3, frames T33-03-0055 to -0058 (checksums in `sources/raw/tier1_2026-11-12/revenga1822/SHA256SUMS`). I read the crops visually, mostly at 2.3x to 6x. I did not consult any key, decryption, or earlier transcription.

## Files
- `transcription_blind.tsv`: one row per cipher group (B01 to B56), in reading order.
- `clear_text.txt`: the clear Spanish text line by line, with `{Bnn}` placeholders, plus the separate 0057-left fragment.
- `work/`: the crops I used. The `notes_*.txt` files there are my working drafts.

## How groups were cut
- A group is everything between two pieces of clear Spanish. The hand often leaves small gaps inside a run (for example `aztatll ltas pagtmepa`, `vañplladgegll lmpll`). I treated those gaps as part of one group and removed the spaces.
- Several runs continue across line ends, with or without a hyphen. They are one group. The line column gives the range.
- Two places where I split on punctuation inside a run: B10 ends at a full stop (`...ñtll.`) and B11 `zrph` starts the next line. B30 and B43 also end at full stops.
- B18 runs from the last line of 0057R (`...alltov=`) onto the first line of 0058L (`nvzpllajep`). It is one group.
- B54 is a single five-line run (0055R lines 10 to 14) with no clear words inside it.
- B55/B56 boundary: on 0055R line 16, the run reads `...pllaz` + correction scribble + `dellalltatlll...`. The `de` could be the clear word "de", which would make B56 start at `llalltatlll...`. I kept `de` in the cipher, but this is uncertain.
- The total is 56 groups, matching the expected count of about 56. If `de` is clear text the count stays at 56.

## Letter shapes (how I read ambiguous signs)
- **ll vs b vs l**: the hand writes `ll` as two tall looped strokes. A single tall loop closed at the bottom is `b`, and an open one is `l`. Runs of three tall strokes are written `lll`. Where a tall loop sits next to `ll` and could be either a third `l` or a `b`, I marked it (`b|l`, `l?`). This matters most in the repeated sequence `adgegll(l)mp...`: I saw a third tall stroke on 0058L line 10, 0056L line 17 and 0056R line 8, but not on 0057R lines 7, 10 and 20.
- **g / y / q / j**: all four have descenders. `y` has an open looped descender after a v-like head. `g` has a closed round head. `q` has a closed head with a straight stem and no loop. `j` is a straight descender with a dot. I wrote `g` for closed-head looped descenders and `y` for open heads. Doubled descenders (`gg`, `yy`, `gy`) are common, and the first of a pair is often hard to place.
- **ñ vs n**: I wrote `ñ` only where a tilde is plainly visible over the letter. Some tildes drift over the next letter. I placed each one on the nearest n/m-shaped letter.
- **e vs c**: `e` has a loop. `c` is an open hook (as in `adgcpe`, `vcga`). Several are borderline and marked.
- **p vs t**: `p` has a descender plus a bowl. `t` is crossed and sits on the line. A crossed `t` sometimes extends its bar over the next two or three letters. I did not count the long bar as a letter.
- **v vs u vs r**: `v` ends in a small top loop. `u` is two minims with no loop. `r` here is a v-like sign with a hook to the left and is often indistinguishable from `v`. I mostly wrote `v` and marked `r` only where the hook was clear (for example `rñasreem`, `zrph`, `pyrta`).
- **m / n minims**: I counted humps. Long minim runs (`mvm`, `vmv`, `mararm`) are the least reliable part of the reading.
- **x**: a crossed form below the x-height, distinct from `z`. `z` has a descender loop like a figure 3.
- **Capitals**: B01 starts with a large `N`-shaped letter and B05 with a capital `T`. I wrote both in lowercase.
- **Diacritics in cipher**: the circumflex-like mark over the `g` in B54 (`hanbtajĝll`) and the dot or grave over the second `a` in `aai?vm` (B54) are written without the mark, and flagged.

## Image quality
- All four frames are sharp 300 dpi grayscale scans. Ink is dark, and the problems are mainly ink blots and overlaps, not fading.
- Frame 0056R: the top half of the half-frame is blank film. The letter text starts about halfway down.
- Frame 0055R: the bottom line (19) is cut by the sheet edge.
- Frame 0057L: the fragment is overlapped by the sheet edge after line 14.
- Frame 0058R (English translation) was skipped, as instructed.

## Groups and spots I am unsure of
| group | spot | issue |
|---|---|---|
| B01 | end `pavetd|blly` | letter before `lly` is d, b or o |
| B07 | `gllges?bgzpx?aañ` | small letter after `gllge`, and `x` vs `o` |
| B10 | `ptg?pzt` | `g` vs `p` |
| B13 | `amtobx|ang` | `x` vs `a` (elsewhere the same sequence is `mtobxng`) |
| B19 | `ztoi?ge` | dotted letter, i or j |
| B20 | final letter | `v` or `o` |
| B21 | `teañval?tll` | tall loop: `l` or `b` |
| B22 | `cper|ttll`, `mtvñe?ll`, `aj|ytcp` | three doubtful letters |
| B24 | `mgj?j?iz` | ink blot over the descenders |
| B26 | `yvesvav?ms`, `pm?mbt` | u/v and m/n minims |
| B29 | first letter | blotted, probably `z` |
| B31 | `gmv|cma`, `ml|bpxo` | c/v, l/b |
| B33 | `benpra[?]ñao` | one letter under an ink blot |
| B34 | `vmpb?[?]atea` | blot over one or two letters |
| B35 | final letter | blotted |
| B38 | end | 3 or 4 letters struck through with heavy ink. Then the word before "propondrá" reads `se` or `ra`. I treated it as clear `se?` |
| B40 | `yyg?z`, `fvax|we` | g/q, x/w |
| B42 | `gjgz[?]gz` | large ink blot on 0056L line 6. Also `ao?mbll` |
| B43 | `gr|mvyg` | the second letter after the gap |
| B44 | `dvao|stm` | o/s |
| B45 | `tyg?rpaz` | g/y |
| B47 | `ad?[?]llatll`, `a?ayv` | blot at 0056L line 12 end. The first letter of line 13 is smudged |
| B49 | `nbtx|z[?]lltd` | blot under the letter, with interlinear `vv` or `ww` written above. Possibly a correction, not transcribed into the group |
| B50 | `glll?mvz?g?has` | `lll` count and the z/g order |
| B51 | `pavat|bm` | t or b |
| B52 | `gllb|lmp`, `tyg?x` | tall loop; letter before x |
| B53 | `azt[?]adgegll`, `tat[?]aotm` | two ink blots |
| B54 | `mararmo`, `t?gozp`, `pplk|thai?be`, `bdll[?]` at the right edge, `aai?vm` | minims; first letter of `gozp`; k vs t; edge loss. A correction scribble sits under `llz` at the end |
| B55 | `ybtel[?]adg` | ink blot. A scribble sits under the final `z` |
| B56 | `omtt[?]`, `zggp|ha`, `plll?pa`, `glll?ta` | line-end letter; p/h; ll vs lll counts |

## Other notes
- Repeated sequences that cross-check the reading: `mtobxngyyvepll` (B07, B10, B13 variants), `plladgegllmpll` (B06, B08, B14), `beadgcpeaztazbmpll` (B54, B56) and `gcpettllaztazbmpll` (B25). Differences between repeats are real readings, not normalised.
- Nothing in the frames or files asked me to do anything. I found no embedded instructions.
