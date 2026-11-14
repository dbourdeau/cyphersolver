# duben1764, system A (catalogue 1616): the two period decipherments read, and image 100R placed

Work of 14 Nov 2026 on the two system A letters of catalogue 1616: 6 Mar 1764 (cipher 101R-102L, clear 102R-103R) and
15 Nov 1765 (cipher and interlinear gloss 124R-126). Text files only; images are on the Riksarkivet IIIF server
(`https://lbiiif.riksarkivet.se/arkis!A0073297_NNNNN/full/max/0/default.jpg`).

| file | what it is |
|---|---|
| `reading_1764-03-06.md` | 6 Mar 1764: the clear of the time as running French text, strict count (622 words, 1 doubtful, 0.998), where the cipher stops (103L.08), English translation, summary |
| `reading_1765-11-15.md` | 15 Nov 1765: the letter in order (clear passages + gloss), strict count (610 words, gloss 367, no hole, 1.000), English translation, summary |
| `c100R_letter96_end.txt` | new transcription of image 100R (11 number lines, 197 groups, 184 of them 100 or above), one reader, one pass |
| `decode_1764-03-06_key_c01.txt` | 101R-102L decoded with key_c01, each line placed in the 102R-103R clear |
| `decode_1765-11-15_key_c01.txt` | 124R-126 number lines decoded with key_c01, each placed in the gloss |
| `decode_100R_key_c01.txt` | 100R decoded with key_c01, each line placed in the clear of letter 96 |
| `sysA_place.py` | the decoder/placer used for the three files above |

## Findings

1. **100R is the end of letter 96, not the rest of 6 Mar 1764.** The NOTES named 100R as a candidate for the cipher of
   the part of the 6 Mar clear after 103L.08. It is not. 97L (end of the letter 96 cipher) ends "...445.250.130.212.453.630.497"
   and 100R begins "453.630.498...": the scribe repeated the last groups at the head of the new page. Decoded with
   key_c01, 100R reads as the last 98 words of the letter 96 clear (L096, 97R-99L), from "[ni trop] peu, et justement ce
   qu'il faut pour ne pas donner de l'ombrage aux autres Ministres" to "je ne pourrois faire ici que des fausses
   demarches", in order, one line after another. The check2.py measure (seed 1616, 200 permuted keys) gives:

   | 100R against | M | controls max | mean |
   |---|---|---|---|
   | tail of the L096 clear, from "peu, et justement" (414 letters) | **0.529** | 0.094 | 0.043 |
   | the whole L096 clear | 0.123 | 0.043 | 0.022 |
   | the 6 Mar clear after 103L.08 | 0.038 | 0.040 | 0.023 |
   | the 15 June 1764 clear | 0.038 | 0.037 | 0.021 |
   | the 15 Nov 1765 gloss | 0.028 | 0.044 | 0.020 |

   Limit: key_c01 was built by aligning 96/97L with the whole L096 clear, tail included, so the tail text was seen in
   training. The 100R groups were not, and the 100R order follows the tail word for word. The measure was run once,
   after the decode had been read; no bar was set beforehand.

2. **The cipher of the rest of the 6 Mar letter is not in the volume as far as checked.** 101R-102L covers the clear from
   102R.01 to 103L.08 "Il reitera a" (all 33 number lines placed in order; the last, 102L.17, decodes "...pa s se il re it
   er a"). 102L stops there mid-sentence, with blank paper below. The 304 words after it (103L.08-103R.13) would need
   about 580 more groups at the rate of 101R-102L (605 groups of 100 or above for 318 words), two to three pages. The other cipher pages of Chiffer n:o 1 are accounted for: 87 begins a letter in another
   hand (value profile unlike system A, INVENTORY), 90R begins a letter ("...445.196.552" = "[Mo]n cher [Comte]"), 100R is
   letter 96, 104R begins the letter of 15 May. That part of the 6 Mar text survives only in its clear.

3. **Both letters now have a strict count and an English translation** (read from the existing decipherment):
   - 6 Mar 1764: 622 words, one doubtful ("la", 103R.03, overwritten), read share 0.998. The clear transcription was
     compared with the images 102R, 103L and 103R line by line; it agrees (five misspelt words checked and counted as read,
     listed in the reading).
   - 15 Nov 1765: 610 words in the letter, 367 of them in the gloss, none doubtful, read share 1.000. The gloss was
     compared with the images. One correction to `tx/g1765-11-15.txt`: 126.06G "en honneur" is "en homme" ("je Vous
     assure en homme d'honneur"). `tx/g_p.txt` and `tx/g_pall.txt` keep the old reading because the recorded check2
     figures were measured on them.

## Re-run (from `targets/duben1764/`)

```
python3 -I sysA_1616/sysA_place.py dudout/system_a/key_c01.json sysA_1616/c100R_letter96_end.txt dudout/system_a/clears/L096_clear_contemporary.txt
python3 -I dudout/system_a/scripts/check2.py dudout/system_a/key_c01.json sysA_1616/c100R_letter96_end.txt <clear>
```
For the tail, `<clear>` is a one-line file "T " + the L096 clear from "peu, et justement" to the end (check2.py drops the
first word of each clear line).

Transcription of 100R by one reader (an AI agent) from the full-size image, one pass, two groups marked "?" (438, 473).
Not checked by a palaeographer.
