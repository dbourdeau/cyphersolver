# duben1764, system A (catalogue 1616): the letter on images 90R-93L, read in part with key_c01; 87-89 is not system A

Work of 17 Nov 2026 on Chiffer n:o 1 (Riksarkivet K 259, IIIF A0073297), following `dudout/system_a/INVENTORY_chiffer1.md`.
Text files only; images on the Riksarkivet IIIF server (`https://lbiiif.riksarkivet.se/arkis!A0073297_NNNNN/full/max/0/default.jpg`).

| file | what it is |
|---|---|
| `c90R-93L_pass1.txt`, `c90R-93L_pass2.txt` | two transcriptions of 90R, 91L, 91R, 92L, 92R, 93L (93 number lines, 1,585 groups of 100 or above). Pass 1 from full-width 4-line strips, pass 2 from zoomed half-lines, made without re-reading pass 1 |
| `disagreements.txt` | the 36 groups where the passes differ and the reading kept (settled on the image) |
| `c90R-93L_merged.txt` | the merged transcription (header explains the one normalisation: this scribe writes 3 open, like 0; 370, 420, 580 are 373, 423, 583) |
| `decode_90R-93L_key_c01.txt` | the merged text decoded with `key_c01` unchanged (`<nnn>` = group not in the key) |
| `reading_90R-93L_tagged.txt` | the reading line by line: sure words, {probable} words, ‹n› = an unresolved span of about n words |
| `c87L_first3lines_test.txt`, `decode_87L_first3lines_key_c01.txt` | three lines of 87L and their decode with key_c01 (no French) |
| `decode_plain.py` | the decoder used (groups below 100 dropped, unknown groups shown) |

## Findings

1. **90R-93L is a system A letter with no contemporary decipherment found.** key_c01 (unchanged, SHA 3fcecea8...) decodes
   1,265 of the 1,585 groups of 100 or above (80 %); the decode is French from the first line ("il seroit difficile, mon cher
   Comte, de ..."). Nothing is written above or between the cipher lines on 90R-93L (one inserted cipher group string on 91L.03
   and 91L.13 only). The clear of 30 Jan [1764] on 94-95 is **not** its decipherment: its opening ("La maniere dont on a recu
   ici ...") and its content (Orlov, Poniatowski, Rakief) do not follow the decode, and no line of the decode places in it.
   The letter ends on 93L.02 with the nulls 16.136.96.743, as it began with 96.70.

2. **Reading (Daniel's rule): read in part, about 44 %.** Word count from `reading_90R-93L_tagged.txt`: 349 sure + 32 probable
   out of about 876 words (the unresolved spans are estimated at 495 words from the group count). The unread part is mostly
   where key_c01 has no value (320 groups, 158 distinct values) or a value cut badly by the 27 Oct alignment ("limp", "kie",
   "uran", "sama"). No new key is proposed or frozen here; values suggested by the sense are only marked {probable}.

3. **87L-89R is not system A.** Three lines of 87L decoded with key_c01 give no French ("in sama t t so ac r ...", see the
   two 87L files); its value profile already differed (INVENTORY). It is in another hand. Whether the 30 Jan clear on 94-95
   is its decipherment is open (it would need another key).

4. **Interlinear check, Chiffer n:o 1.** Images 87-93 and 104-107 and 112-115 were looked at for interlinear decipherment
   (full-size images, 17 Nov 2026): there is none; the contemporary decipherments of this file are separate clear pages
   (97R-99L, 102R-103R, 106R-107L, 109R-110L, 116-117), as the INVENTORY lists. Only the 15 Nov 1765 letter (124R-126, outside
   Chiffer n:o 1) carries an interlinear gloss.

## What the letter says (from the readable parts; English)

Düben (the hand and system of the St Petersburg letters to "mon cher Comte", Gyldenstolpe) writes that it would be difficult
to express [his feelings] about what he has just [received]; he has been reproached with little zeal for the service of Her
Majesty at the very time when he did everything in the world to prove his attachment, but his efforts were useless. He gave
the Empress the assurances of the King's friendship and reported her dispositions; he neglected nothing to press her to fulfil
them, did all he could, but "the unhappy turn of affairs" prevented success: "it is assuredly not my fault"; the promises the
Empress had made to take an interest [in the King's affairs] ... on condition of a perfect reciprocity, on which he had given
strong assurances. Count Panin disapproved of measures taken; he began to show doubts about [the] sincerity [of the Swedish
court], about the little confidence shown to its old servants and its visible predilection for [one] party, and then the
election of the Marshal of the Diet made the same ideas ... useless; [the Empress acts] in concert with the King of
[Prussia]. Later passages speak of what he has always done for the Empress, of "persecution", of an invariable [attachment],
of his very unhappy position, of justice, asks [the Count] above all to help his cause, mentions what comes "from the
Empress's side", and closes with the measures taken by Her Majesty and "the bottom of my heart".

The date is not in the cipher read so far. The content (Diet marshal election, Panin's doubts, promises of the Empress)
fits the late summer or autumn of 1765 (Diet opened in Feb 1765) better than early 1764; to be checked.

## Limits

Transcription by one reader (an AI agent), two passes, not checked by a palaeographer. The second pass was made by the same
reader, so it is not fully independent. No measure was run (the letter has no clear); nothing here is a new key.

## Re-run (from `targets/duben1764/`)
```
python3 -I sysA_1616/letter90/decode_plain.py dudout/system_a/key_c01.json sysA_1616/letter90/c90R-93L_merged.txt
```
