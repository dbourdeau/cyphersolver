# Reading: HStAD D 4 Nr. 76/6, view 13 (film frame 0416)

Key: the strip on view 11 of the same file (`key.tsv`), plus 38 = o and 39 = u deduced from the sheet. Decoded with
`python3 decode.py transcription/digits_arbitrated.txt` (`decryption.txt`), then read for sense.
Marks: sure (no mark) / {probable} / [restored] / ‹unresolved›. Spelling of the cipher kept; v is written u, j is written i;
an overbar on a number doubles its letter (Vilgeehrter, herr). Line breaks inside a word marked "-".

## Text (German)

```
 1 Vilgeehrter herr, {die} {entsetzung}
 2 Philippsburg zu befurdern bin ich
 3 selbsten {etliche} {tag} zu {Zabern} ge-
 4 wesen und ohn underlas bey den
 5 {keyserischen} und spanischen so-
 6 lang {sollicitirt}, bis endlichen
 7 die Frantzosen etliche pas‹…›
 8 ‹…›rt, und darauf der anstalt gema-
 9 cht, das etliche {keyserische} und
10 spanische regimenter nunmehr
11 {alhero} {im} anzug sein, und {gelieb-
12 ts} gott gegen mittwoch und don-
13 nerstag alhie eygentlich anlan-
14 gen und alsdan diseits uff Phi-
15 lippsburg zu marchiren werden.
16 {Ligt} {also} zum hochsten, den her-
17 rn officiern und soldaten ufs
18 beste zuzusprechen, das sie
19 ihre dapffer- und standhafftigkeit
20 ‹…› noch rhummlich wie bishero
21 fortzusetzen und bis den neu-
22 en Jharstag sich gedulden wol-
23 len; das gelt vor sie ist be-
24 reits gesch‹…›, welches
25 gebracht werden sole,
26 den die gräfliche ‹…› all‹…›      [hole and pasted slip]
27 als an auc[h] ‹…›
28 wer‹…›
S1 (oblique slip) {zwantzigsten} ‹…›
S2 (oblique slip) meines ‹398› ‹sammigerku…›
```

Line 19: the cipher has the seven numbers of "dapffer" and then "und standhafftigkeit"; the ending -keit is shared
("dapffer- und standhafftigkeit"), so the word is written "dapffer-" and counted sure. An earlier version wrote
"dapffer[keit]" with an editorial bracket.

Line 25 reads "gebracht" (17 15 12 27 11 13 18 29); the text posted in issue #745 had "gebraucht", a slip.

## Count (repository rule: only sure words count as read)

| | words |
|---|---|
| total (letter body and fragments, slips included) | 124 |
| sure | 98 |
| probable or restored | 15 |
| unresolved | 11 |

Read share by the repository rule: 98 / 124 = 79.0 % (97 / 124 = 78.2 % after the blind check of 18 Nov 2026 and 95 / 124 = 76.6 % before it; see the two blind checks below), **read in part**, with the key found in the same file (read with known key).
Our own count including probable words was 113 / 124 = 91 % (letter body, lines 1-25: 105 / 109 = 96 %); it is given
here only as that, a count with probable words. "auc[h]" (line 27, one restored letter) is counted with the probable words.

## Blind shape check (18 Nov 2026)

Brice Dudout answered a blind sheet of 15 boxed numbers on view 13 (each option a crop of a sure number of the same hand, no letters or words shown; 3 controls on sure words, all answered as expected). The sheet, the answer key, the answers and their hashes are in `blind_check/` (README there explains why 19 places were first prepared and 15 asked).

- Now sure: "gräfliche" (l. 26, first number 17 confirmed) and "dapffer" (l. 19, 11 and 25 confirmed; the cipher has the seven numbers of "dapffer", written "dapffer-" since the ending -keit is shared with "standhafftigkeit").
- Against the reading: the last number of "entsetzung" (l. 1) was seen as 27 (r), not 17 (g): the word stays probable although its 29 was confirmed. The end of "gesch‹…›" (l. 24) was seen as 27 and 22 ("geschr…" … "m"), which gives no word: it stays unresolved.
- Left open by his remarks: "tag" (11 confirmed, but with a mark or two dots above it), "mittwoch" (31 vs 34 not settled), "also" ("28?" instead of 21). "die" was confirmed as written 14 18 15 (dhe) and stays probable; the 11 written as two strokes in "Zabern" was confirmed (a place name, still probable).

## Blind shape check on the new scan (25 Nov 2026)

HStA Darmstadt sent a new colour scan of the sheet on 25 Nov 2026 (private study, not public, not included). Brice Dudout
answered a second blind sheet on it: 9 boxed numbers, 6 targets and 3 hidden controls. The selection rule, with what each
answer would change, was written and hashed before any crop was made. The files are in `blind_check/` (`*_2026-11-25.json`,
README there).

- Controls: 3 of 3 as expected ("gott" 24, "en" 23, "wie" 31).
- "mittwoch" (l. 12): the 5th number was seen as 31 (w), not 34. This settles the point left open on 18 Nov:
  **mittwoch is now sure** (counted above).
- "gesch…" (l. 24): the 6th number was seen as 24 (o) and the last as 23 (n). On the new scan the word reads
  17 15 28 13 18 24 28̄ 15 23 = **geschossen** ("already advanced", of the money), which the rule makes sure. It is not
  counted here yet, because the middle numbers come from the new-scan transcription, which is not in this folder;
  it will come with it.
- The end of l. 29 and l. 30 of the sheet (here slips S1 and l. 28, read on the new scan as "Hagenaw [den] zwey und
  zwantzigsten decembris"): the last number of "Hagenaw" was seen as 31 (w), so Hagenaw is spelled out (sure on the new
  scan). The middle number of "decembris" was seen as 22, not 12: the cipher has "decemmris"; the month stays probable,
  by sense. The looped sign after "decembris" matched none of the shapes offered (15, 18, 39): it stays unresolved, and
  no year is read from it.
- A remark on the 31 of "Hagenaw" ("with a dot above the 1, like an i") describes the dot this hand puts on every 1; it
  changes nothing.
- On the new-scan reading (124 words as here, new words not added) the check gives 104 / 124 sure = 83.9 %; on the whole
  sheet with the words only the new scan shows, 106 / 139 = 76.3 %. Still read in part.

## The 11 unresolved places

| # | place | digits (arbitrated) | what is there |
|---|---|---|---|
| 1 | l. 7, end: pas‹…› | 25 11 28 ‹…› | word cut by a crossing-out at the line end (pass 1: `?? 20 ??`; pass 2: `28 20` + crossing-out); a verb in -irt with l. 8: passirt? forcirt? |
| 2 | l. 8, start: ‹…›rt | ‹…› 27 29 | end of the same word; the first numbers are blotted (pass 1 read `28 29 19 19 27 27 29`, pass 2 left it doubtful) |
| 3 | l. 20, first word | ‹…› | under a blot |
| 4 | l. 24: gesch‹…› | 17 15 28 13 18 ‹…› | end of the verb lost (geschafft?); pass 1 had `27 18 27 ?? 15 ??` |
| 5 | l. 26, fourth word | ‹…› | hole / pasted slip |
| 6 | l. 26, last word: all‹…› | 11 21 21 ‹…› | cut off by the hole |
| 7 | l. 27, last word | ‹…› | hole |
| 8 | l. 28: wer‹…› | 31 15 27 ‹…› | fragment under a blot (pass 1: `31 15 27 ?? / [..] 16 20 11 ??`) |
| 9 | slip S1, second word | ‹…› | slip cut |
| 10 | slip S2: ‹398› | 398 | number off the key (three digits) |
| 11 | slip S2: ‹sammigerku…› | 28 11 22 22 19 17 15 27 20 30 ‹…› | decodes to "sammigerku…", no sense found |

## Why the probable words are probable

"die" is written 14 18 15 (dhe, h for i); "entsetzung" lies under a blot, and the arbitrated digits give "enstsetzung"
with one number too many (see NOTES.md, open point); "etliche" (l. 3) is underlined or struck; "tag" 29 11 17 (11 read
as two strokes); "Zabern" 34 11 12 15 27 23, a place name (Saverne); "keyserischen" l. 5, first half faded; "keyserische"
l. 9 likewise; "sollicitirt" and "alhero" rest on 38 = o; "im" stands alone after "alhero"; "geliebts" split over a
line break; "Ligt also" at a line start written over; "zwantzigsten" on a slip with a doubtful number.

## Translation (English)

"Much-honoured Sir, to further the relief of Philippsburg I have myself been at Zabern [Saverne] for several days and
pressed the Imperial and Spanish [commanders] without ceasing, until at last the French … several passes …; and
thereupon it has been arranged that several Imperial and Spanish regiments are now on the march hither and, God willing,
will certainly arrive here on Wednesday and Thursday, and will then march on this side [of the Rhine] towards
Philippsburg. It is therefore of the highest importance to encourage the officers and soldiers as best one can to keep
up their bravery and steadfastness … as praiseworthily as hitherto, and to be patient until New Year's Day; the money for
them has already been [provided], which is to be brought … the comital (?) … all … as also … [fragments; slips:
'…twentieth…', 'my … 398 …']."
