# everett1825: the period decipherment, and a group-by-group check of the readings (Andrew Beling)

Contributed 22 Nov 2026 by Andrew Beling (ajbeling), with AI agents. **This is a verification and a source find, not
a new reading.** The reading of the coded passages is WAINUT's (passages A, B, C, `../everett1825_*`) and Brice
Dudout's (pp. 1-6 and 17-18, `../dudout/`). This folder adds the State Department's own decipherment of the same
passages, a comparison of three independent transcriptions of the code groups, and a check of every group where
they disagree on the microfilm.

## The period decipherment (frames 0110-0111)

`../NOTES.md` (section 3 and Remaining gaps) says no period decipherment was found; Dudout's README says "no complete period decoding exists for these pages". There is one on the same reel, just before the Notes:
NARA RG 59, M31 roll 27, [frame 0110](https://catalog.archives.gov/medialz/dc-metro/rg-059/603720/M31/M31-027/M31-027-0110.jpg)
(right page: parts 1-4) and [frame 0111](https://catalog.archives.gov/medialz/dc-metro/rg-059/603720/M31/M31-027/M31-027-0111.jpg)
(left page: part 4 continued; right page: parts 5 and 6). Parts 5 and 6 are headed "5 part" and "6 part" with faint
marginal notes "14 & 15" and "17 & 18", the MS pages of the Notes. Parts 1-4 cover the coded runs of pp. 1-6, part 5
the six lines of pp. 14-15 (passage A), part 6 pp. 17-18 (passages B and C). Who wrote it and when is not known; it
is presumably the decipherment that the pencil "Decyphered" at the foot of p. 4 refers to. Our transcription of it
is `period_decipherment.txt`.

What it settles:

- **70 is "necessary", with "ity" written above it**: "well disposed to the necessity of recognition" (part 6).
  WAINUT has `[?cause]`, Dudout `{measure}`. The insertion was read blind by two model readers (film_check, Q39):
  "(ity)" and "(cty)", the second of these noting it may be "ity" with the i merged.
- **125 is "contrary"** ("acting in a contrary direction"), as Dudout proposed; WAINUT leaves it open.
- The decipherer worked from the key and corrected himself where Dudout gives a value from sense against the jqa
  table: 625 mation, corrected to many; 1593 once, to understood; 1596 ongue, to of; 1525 agent, to personal; 483
  until, to -ing; 797 done, to "Tune" (fortune; the insertion, Tune or Time, is faint); and 908 or, with "Ton" above it (passage A, "the tone of his remarks").
  At these places he and Dudout agree against the key, so the group as sent or the key is off, not the reading.
- All the groups the project's reading leaves open have values on the State Department code sheet already in this
  repository (`../../morris1813/beling/key/codebook_M97_13_transcription.csv`, NARA M97 roll 13 frames 1056-1057):
  125 contrary, 126 convey, 211 pret, 258 spi, 850 dispose, 917 os, 1354 br, 1512 acy. These are the values Dudout
  proposed from the alphabetical slots.
- The sentence "it seems to be also understood that the" (p. 18, between "for the present" and "influence") is in
  the decipherment. Its code line, `1440 1082+D 569 1310 1541 480 262 1599 1384 1385`, is in the project's passage C
  (line 3) and in our transcription, but not in `../dudout/texts/p18_0121_transcription.txt` or its decryption. His
  reading has the words, so it is a slip in the files; it also accounts for 1,117 groups in his files against 1,127
  in his README.

## Three transcriptions of the code groups

`transcription_six_sections.txt` is our transcription of all six coded sections, 1,201 groups (frames 0112-0115,
0119-0121), made in October 2026 from the NARA catalog images. It was not blind: the clear text and the period
decipherment had been seen. `python scripts/compare.py` aligns it with the other two and prints:

| Compared with | Groups in both | Agree | Differ | Only ours | Only theirs |
|---|---:|---:|---:|---:|---:|
| Brice Dudout, pp. 1-6 and 17-18 | 1,113 | 1,086 | 27 | 14 | 4 |
| Project (WAINUT), passage A | 74 | 74 | 0 | 0 | 0 |
| Project (WAINUT), passages B and C | 281 | 278 | 3 | 0 | 0 |

Ten of the 14 "only ours" are the p. 18 line above; the other four, and the four "only theirs", are three short
runs on pp. 4 and 5 where the two transcriptions have different groups.

## The film check (`film_check/`)

Every one of the 27 differing groups and the three runs was cut from the catalog JPEGs (`film_check/crops/`, at
the frame's own resolution; the pixel box of each is in `film_check/readings.tsv`), together with eight groups where
both transcriptions agree, as controls, and the "ity" insertion. The positions were written down before any
reading, without the candidate values (`film_check/positions.tsv`). An AI helper agent that had seen nothing
else was given only the crops (shuffled, under neutral ids) and the question "what number is written": all 39
places. A second helper, which did not see the first one's answers, was given the whole line with the place boxed
in red for 12 places: the 11 of the 27 groups where the first was unsure, not sure, or matched neither candidate,
and the "ity"; plus two controls. So 16 of the 27 groups rest on one reader. **These are model readings, not a person's.**
The ten control readings (eight by the first reader, two by the second) were all correct.

Result for the 27 groups (`comparison_with_dudout.tsv`, with the period decipherment's word for each):

- **Dudout's digit is on the film at 18.** Our transcription was wrong there, and at all three short runs.
- **Our digit is on the film at 8.** 628 and 1564 rest on one reader; at 845 and 880 the first digit could be 3
  (reader 1's first choice was 345 and 380), though Dudout's 843 and 330 are excluded either way. At six of the
  eight Dudout's file has the word from sense or leaves it open, and the group on the film carries it in the key:
  628 me (his 623 `[me]`), 458 ve (433 `[ve]`), 845 dis (843 `{di}`), 1081 self (1031 `[self]`), 1564 observe
  (1364 open), 880 li (330 `[li]`). At two the group on the film does not give the word. 1257 (p. 5) is "hath" on
  the code sheet where "describing" wants cri, which 1057 (crisis on the code sheet, crees in the jqa table) does
  not give either, so his `[cri]` stays from sense. 1388 (p. 18) is "then" for 1383 "than", a one-digit slip; as a
  whole-word group it does not count as read under the one-digit rule (README Conventions, 14 Nov 2026). The
  project's file has 1383? there too.
- **Undecided at 1:** p. 5 line 3, the readers split between 1385 and 1345; "the correct principles" wants 1385.

So no word of either reading changes. What would change, if the maintainers agree, is the group written in eight
places of `../dudout/texts` (and 1388 in `../everett1825_transcription.txt`), six words moving to "read from the
key" (me, ve, dis, self and li from "from sense", observe from open; pp. 1, 2, 3 and 6, the pages now just under the
read bar on the strict count), and the missing p. 18 line. None of this is applied here.

## Files

- `period_decipherment.txt`: our transcription of the period decipherment, parts 1-6.
- `transcription_six_sections.txt`: our transcription of the code groups, unchanged since October.
- `comparison_with_dudout.tsv`: the 27 groups and three runs, with both transcriptions, both values, the period
  decipherment's word, the two blind readings, and which the film supports.
- `film_check/positions.tsv`: the places and pixel boxes, written before the readings, with no candidates.
- `film_check/readings.tsv`, `film_check/crops/Q01.jpg` - `Q39.jpg`: frame links, pixel boxes and the readings
  with their stated confidence.
- `scripts/compare.py`: regenerates the counts above (`--list` prints every difference). Standard library only.

The microfilm is a NARA publication of federal records, in the public domain; the crops total about 400 KB and the
frames are linked, not committed.

## Not done

- No person has looked at the film for these places; the two readings are a model's. A person's look would matter
  most at the eight places where the film supports our digits and at p. 5 line 3.
- Our transcription of the period decipherment has one reader; a few words are uncertain (the Russian minister's
  name, "me be", "best") and some line ends of frame 0111 are lost at the binding.
- Who wrote the decipherment, and when, is not known.
