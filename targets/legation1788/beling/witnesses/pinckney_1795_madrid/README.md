# Pinckney 1795, "Cypher 2d" passages with Taylor's interlinear: transcription

10 November 2026. Source: NARA RG 59, M31 roll 7, frames 0017-0021, local copies in
`sources/raw/pinckney_madrid_1795_2026-11-10/` (`M31-007-NNNN.jpg`). Local image work only
(`sips` crops, read by eye). No web, nothing posted.

Independence: read from the images alone. No key or earlier reading was opened (nothing
under `output/` other than this folder, nothing under `sources/raw/reconstruction_2026-11-06`,
no file with "key" in its name). The only project file read was the lead note
`research/pinckney1795_xyz_leads_2026-11-10.md`, as instructed; it quotes a handful of
candidate values, and where a reading here leans on anything other than the ink, the note
column says so. Cross-references in the notes ("663 has 'the' at ...") are to other lines of
these same frames, never to a key.

Files:

- `lines.txt`: one line per manuscript line, 34 lines.
- `spans.tsv`: 206 rows; every group is in exactly one row, in order.
- `README.md`: this file.

## What the frames are

| Frame | Side | Content |
|---|---|---|
| 0017 | left | Last page of Pinckney's letter of 11 Aug 1795 (code passages in his own cipher, no interlinear), signed "Thomas Pinckney". Not transcribed here. |
| 0017 | right | Pinckney to the Secretary of State, "San Ildefonso 27 August 1795", one page, signed. The covering letter; text at the end of this file. |
| 0018 | left | Blank verso of the 27 Aug letter, with the docket "Pinckney Thos. / recd 25. Nov. 1795". |
| 0018 | right | Enclosure, leaf A, second side. Four passages (lines L01-L08), then Pinckney's heading at the foot: "The cyphered part of my letter of the 20th. July 1795", an "x" over the 20; under it in the clerk's hand "This is probably a mistake - the letter recd. is dated July 21. G. T. Jr"; at the lower left "Cypher 2d". Sideways at the upper right: "inclosed in a letter from Mr. Pinckney of 27. Aug. 1795". |
| 0019 | left | Enclosure, leaf A, first side. Seven passages (L01-L14), beginning "That they are still anxious". No heading on this side. |
| 0019 | right | Enclosure, leaf B. Five passages (L01-L08), then the heading "[T]he cyphered parts of my letter of the 17th. August 1795", an "x" over the 17; "Cypher 2d." at the lower left; clerk's note "+ this is probably a mistake - the letter to which it appears to belong is dated the 11. Augt. G. T. Jr". |
| 0020 | left | Blank verso of leaf B, with the docket "inclosed in a letter from Mr. Pinckney of 27. Aug: 1795". |
| 0020 | right | **A different letter**: Pinckney to the Secretary of State, "San Ildefonso 1 October 1795", "Dear Sir", page 1. All in clear except the last line, where "for where [m]easures are" is followed by ten code groups with interlinear words. That line is transcribed here as 0020-L01 because the passage runs on to frame 0021. |
| 0021 | left | Page 2 of the 1 Oct letter: two more lines of the same passage, clear text, then a second short passage ("to induce a" + nine groups + "and I con[clude]"). Both with interlinear words. |
| 0021 | right | Page 3 of the 1 Oct letter, all clear, signed "Thomas Pinckney", addressed at the foot "The Secretary of State". |

So the July passages are **0019 left, then 0018 right**: leaf A was bound with its second side
first. The whole of 0019 right belongs to the August letter, not the July one. Frames 0020-0021
are not part of the enclosure; the 1 Oct letter was written in the Department's cipher from the
start, and Taylor deciphered it the same way.

A narrow strip of leaf A's first side shows beside the gutter at the top of frame 0020. It
carries the right-hand ends of 0019L lines L01-L05 (6, 2., 3., a cut digit, 8) and settles the
last digit of 1226 and 1258.

## Conventions

Line ids: `0018-Lnn`, `0019L-Lnn` (left page), `0019R-Lnn` (right page), `0020-L01`, `0021-Lnn`.
In `spans.tsv` the frame column carries `0019L` / `0019R`.

| Token | Meaning |
|---|---|
| `+` | a single cross written after the group (once, at 0019L-L03, beneath it) |
| `++` | a double cross after the group: two uprights with one or two bars, like `#`; at 0018-L05 one upright with two bars |
| `^` | a small 3- or z-shaped squiggle written under the last digit |
| `?` at the end | doubtful reading; digit and alternative are in the note and in the list below |
| `_` | digit(s) hidden in the gutter or cut by the page edge; the number hidden is not known |
| `*` | a digit that is there but under a blot |
| `{...}` | words in clear on the line |
| `<...>` | group struck out by the writer |
| `[...]` | groups written by the writer above the line as a replacement (0021-L02 only) |

In `spans.tsv`, `kind` is `interlinear`, `clear-on-line` or `none`. A dash in the interlinear
column is Taylor's stroke (`—` short, `——`/`———` long). `placement` is `clear` when the ink of
the word or dash stands over the listed group or groups and no neighbour competes;
`ambiguous` otherwise, with the literal position described in the note. Square brackets inside
an interlinear word mark letters lost at an edge.

## How Taylor's words sit over the groups (read before using the rows)

- Taylor did not centre each word on its groups. In many phrases he wrote the words compactly
  from the left and filled what remained with a dash. A dash row therefore belongs with the
  word row or rows before it (also across a line break: 0019L-L02/L03, 0019R-L07/L08,
  0021-L01/L02). The safe unit is word(s) plus dash over the union of their groups.
- Because of that packing, a `clear` placement is a statement about the ink, not a guarantee
  of the value. Three places where the ink and the rest of these frames disagree:
  `by` stands over 1527 at 0018-L05 but over 1515 (dash over 1527) at 0019R-L03;
  `of` stands over 1162 at 0020-L01 and over 935 at 0021-L03, with the dash covering 1518,
  which has `of` cleanly above it in eight other places; `system` stands over 200 with a dash over
  1578 1018 at 0018-L06, but over 200-1578 with `conjectures` starting over 1018 at 0021-L01.
- Where several words drift together over the same number of groups (for example
  `in their system`, `between france Spain, &`, `circumstances my present Opinion is`) they are
  kept as one row marked `ambiguous` rather than split by guess.
- Taylor crosses his t with a long stroke that runs through the whole of `the`, `they`,
  `their`, `them`, `therein`, `those`, `to`. These words look struck out but are not. The
  only real cancellations in his hand are a word under `rejected` (0019R-L03) and a blotted
  letter after `possession` (0019L-L05).
- 22++ carries the double cross that elsewhere sits under words in -ed (complied, offered,
  acknowledged, observed, considered), while Taylor wrote `circumstances` over it.

## Marks, as they occur

- `+`: 997+ (possessions, [instruct]ions), 589+ (rights, three times), 1197+ (Stipulations),
  1008+ (ourselves), 47+ (Intentions), 20+ (means), 574+ (occurrences), 964+ (written `object`).
- `++`: 411++ complied, 182++ offered, 892++ [ac]knowledged, 638++ observed, 371++ considered,
  22++ (see above), and a hidden group at 0019R-L02 under `[..]ed`.
- `^`: 940^ in all four occurrences of `guarantee`, 986^ under `shall`, 728^ after `still`.

## Counts

| Frame / page | Lines | Groups | Struck | Interlined words | Dash-only rows | One word over one group (clear) | Ambiguous rows | Doubtful groups |
|---|---|---|---|---|---|---|---|---|
| 0018 right | 8 | 67 | 0 | 50 | 4 | 37 (36) | 5 | 5 |
| 0019 left | 14 | 115 | 0 | 81 | 13 | 60 (59) | 6 | 11 |
| 0019 right | 8 | 69 | 0 | 49 | 4 | 29 (22) | 14 | 7 |
| 0021 left | 3 | 32 | 2 | 16 | 3 | 6 (5) | 6 | 3 |
| **Targets** | **33** | **283** | **2** | **196** | **24** | **132 (122)** | **31** | **26** |
| 0020 right | 1 | 10 | 0 | 5 | 0 | 0 | 1 | 0 |
| All | 34 | 293 | 2 | 201 | 24 | 132 (122) | 32 | 26 |

"Interlined words" counts every word Taylor wrote, including the cut ones at the edges
(`fo[r]`, `[..]ed`, `ac`). The 21 July set (0019 left + 0018 right) is 182 groups; the
11 August set (0019 right) is 69, not counting what the gutter hides; the 1 October passages
are 42 (33 + 9).

## Passages and matching to the 21 July letter

The passages are **not numbered or lettered**. Pinckney set them off with a short horizontal
rule under each one and often a closing dash on the line. One boundary (0019L L12/L13) has no
rule and is taken from the short line and the stop. The July set has eleven passages, the same
number as the coded passages of the letter of 21 July (frames 0008-0013), so they can be
matched by order only.

| No. | Lines | Groups | Taylor's words |
|---|---|---|---|
| J1 | 0019L L01-L05 | 54 | That they are still anxious for further delay which is to them equivalent to a cession of our rights so long as we shall acquiesce therein they being in possession of the object of controversy |
| J2 | 0019L L06-L07 | 12 | not guarantee the possessions of Spain in America. |
| J3 | 0019L L08-L09 | 16 | Stipulations on this subject in our treaty with france should be observed. |
| J4 | 0019L L10 | 7 | Their accomodation with france |
| J5 | 0019L L11 | 11 | Establish a triple alliance between france Spain, & ourselves. |
| J6 | 0019L L12 | 2 | an alliance. |
| J7 | 0019L L13-L14 | 13 | Intentions of the french government with respect to our negotiat[ion] here. |
| J8 | 0018 L01-L02 | 11 | French commissioners have complied with their instructions. |
| J9 | 0018 L03-L05 | 28 | minister at paris offered an accommodation between Spain and france unless our rights were previously acknowledged by the former. |
| J10 | 0018 L06-L07 | 22 | This court means to proceed in their system of delay or whether they will yield to us our rights |
| J11 | 0018 L08 | 6 | alliance and guarantee |

The lead note places the eleven coded passages of the 21 July letter on ms pp. 1-2, 4, 6,
7 (three), 8 (three) and 10 (two). By order that would give J1 = pp. 1-2, J2 = p. 4, J3 = p. 6,
J4-J6 = p. 7, J7-J9 = p. 8, J10-J11 = p. 10. This is an inference from the order; frames
0008-0013 were not opened for this job. J1 and the opening of J2 agree with what the lead note
reports for the first two passages.

The August set (0019 right) has five passages: L01, L02, L03, L04, and L05-L08 (36 groups).
The October letter has two: 0020-L01 + 0021-L01-L02, and 0021-L03.

## What the gutter and edges hide

- 0018 right: the left edge of L02-L05 is in the gutter (one digit lost on each, perhaps more on
  L03). L01, L06 and L08 start clear of it; L07 starts right at it with 1069 complete.
- 0019 left: the right edge is under the gutter shadow. L01, L05, L08 and L13 run into it. L01
  and L05 are recovered from the frame 0020 strip; L08 and L13 are not.
- 0019 right: every line starts in the gutter. Lost, as far as can be judged: one digit on L01,
  L05 and L08; two on L06;
  all but the last stroke of a group on L07; most of a group on L03; a whole group on L02; and
  on L04 the start of the word (`[wit]hout`) and perhaps a group before 37.

## Doubtful digits

Doubtful readings of visible digits (12, plus two inside struck groups):

| Line | Written here | Note |
|---|---|---|
| 0019L-L01 | 1058? | second digit faint and open: 0, alt 3 |
| 0019L-L01 | 1569? | first digit lost in a smear that may be a cancelled start; 5, 6, 9 legible |
| 0019L-L01 | 728^? | last digit rounded: 8, alt 3 or 9. 723 at 0018-L07 (yield) has a plain flat-topped 3 |
| 0019L-L02 | 885? | first digit a solid blot |
| 0019L-L02 | 265? | middle digit small: 6, alt 5 or 8 |
| 0019L-L04 | 1097? | first two digits overwritten: 10, alt 11 |
| 0019L-L04 | 134? | last digit ink-filled: 4, alt 1 or 7 |
| 0019L-L08 | 1580? | third digit blotted: 8, alt 6 or 0 |
| 0019L-L14 | 1421? | on the bottom edge under `here.`: last digit 1, alt 4 or 7 |
| 0021-L01 | 1488? | 88 smudged, alt 08 (1408 has `will` elsewhere; Taylor wrote `must`) |
| 0021-L01 | 1497? | second digit smudged: 4, alt 0 or 1 |
| 0021-L02 | 728? | interlined group, last digit a small raised loop: 8, alt 0 |
| 0021-L02 | <1469?> <1288?> | struck groups: alt 1169; alt 1280 |

Hidden, cut or blotted digits (14):

| Line | Written here | What can be said |
|---|---|---|
| 0018-L02 | _97+ | a lower curve before 97; 997+ fits |
| 0018-L03 | _78 | nothing visible before 78 (478 stands at L01) |
| 0018-L03 | 11*1 | third digit under a blot; 1181 at 0019L-L10 in the same run of groups |
| 0018-L04 | _56 | a curve before 56; 856 fits |
| 0018-L05 | _12 | top of a stroke before 12: 4 or 1 |
| 0019L-L08 | 125_ | last digit cut: 0, 6 or 8 |
| 0019L-L13 | 54_ | cut after "54"; could also be a single 5 with a + |
| 0019R-L01 | _513 | a slanting stroke before 513; 1513 fits |
| 0019R-L02 | _++ | whole group hidden, only its double cross visible |
| 0019R-L03 | _71? | a cut stroke (7?) and 1 |
| 0019R-L05 | _490 | 1490 fits |
| 0019R-L06 | _58 | 1058 fits (`[th]at`) |
| 0019R-L07 | _1? | last stroke and stop only |
| 0019R-L08 | _97 | 997 fits |

Heavily inked but not in doubt: the 9 of 59 (both times), the first 8 of 885 at 0019R-L05 and
L07, the 6 of 698 at 0019L-L01.

## Method and re-read

Pixel sizes from `sips -g`; 1500 px overviews; then full-resolution strips of one to three
lines with the interlinear, three overlapping segments per line at 2x. Doubtful groups were
enlarged 3x-7x. After the first pass every line was re-cut differently (two overlapping halves
at 1.5x) and re-read against the rows. No digit reading changed on the re-read; several
placements were revised, and drifting word runs were merged into single ambiguous rows.
Working crops are in the session scratchpad and are not kept.

## Frame 0017: Pinckney on the two ciphers (transcribed last, in clear)

Right-hand page, whole letter:

> San Ildefonso 27 August 1795
>
> Dear Sir
>
> An opportunity offering for America, I avail myself of it to rectify a mistake I have made
> in the letters I have written to you since my arrival in Spain, having made use of a Cypher
> which I had made for the purpose of corresponding with our Ministers in Europe, and with a
> copy of which you are not furnished – I now enclose the cyphered parts of the two letters
> I have written –
>
> I am My Dear Sir
> Your faithful & obedt. Servt.
> Thomas Pinckney

That is all he says. The letter does not name or describe the second cipher; the label
"Cypher 2d" appears only on the two enclosure leaves (0018 right and 0019 right, lower left),
in what looks like Pinckney's hand.
