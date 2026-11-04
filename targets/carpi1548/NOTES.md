# carpi1548: Cardinal Rodolfo Pio di Carpi (Rome) to Antoine Perrenot de Granvelle, Aug–Dec 1548 (catalogue 1265)

Status: in progress. Data only: no profile.json, no reading, no site page yet, and catalogue row 1265 is not yet updated (read at the time and in print, key published in Bertomeu Masia 2009, p. 162). The transcription was not compared with the BNE scans by the maintainer.

Data for issue #228: the digit transcription of the letter of 6 Aug 1548 and of the last cipher block of the
September letter, the contemporary decipherment of the August letter, a key rebuilt from that letter alone, and the
scripts that align and decode. There is no `profile.json` or reading here; the target page and the catalogue
change are left to the maintainer.

## Source

Madrid, BNE, MSS/20210/15/1-6, "Cartas del Cardenal de Carpi al Cardenal Granvela", 12 leaves, six letters, Rome,
Aug 1548 – Dec 1550. BNE Digital bdh0000172678: https://bnedigital.bne.es/bd/es/card?oid=0000172678 (public domain,
CC BY 4.0, attribution to the BNE). The images are about 1,070 px wide per page; the digits are about 8 px.

| part | date | cipher |
|---|---|---|
| /1 | Rome, 6 Aug 1548 | f. 1r 10 lines, f. 1v 18 lines, f. 2r 16 lines |
| /2 | Rome, .. Sept 1548 | first page and a last block of 15 lines |
| /3 | Rome, 18 Oct 1548 | f. 1v 6 lines, f. 2r about 13 lines |
| /4 | Rome, 4 Nov 1548 | f. 1r about 20 lines, f. 1v about 21 lines |
| /5 | Rome, 27 Dec 1550 | none |
| /6 | Rome, 18 Dec 1548 | f. 1r about 13 lines, f. 1v about 19 lines, f. 2r 1 line |

## Files

- `transcription/d1_digits.txt`: the whole cipher of /1, 44 lines, 3,192 digits.
- `transcription/d2_block_digits.txt`: the last cipher block of /2, 15 lines, 1,089 digits.
- `transcription/samples_d3_d4_d6.txt`: one or two lines each from /3, /4 and /6, for the checks below.
- `decipherment/d1_contemporary.txt`: the decipherment written on /1, transcribed in the decipherer's spelling,
  1,785 letters. It is in four pieces, read in this order:
  - the top of f. 1r and its left margin;
  - the two lines below the f. 1r block;
  - the lines above the f. 1v block;
  - the f. 1v margin.

  The second and third pieces are in a larger hand and look like clear text, but they decipher the middle of the
  cipher.
- `key/key_d1_rebuilt.tsv` and `.json`: the key rebuilt from /1. For each group: its value, and how many of the
  units aligned to that group agree with it.
- `scripts/align.py`: aligns the /1 cipher with its decipherment and rebuilds the key.
- `scripts/decode.py`: decodes any block with that key.
- `decryption/d2_block_decode.txt`: the /2 block decoded with the /1 key.

Reproduce from this folder:

```
python3 scripts/align.py
python3 scripts/decode.py transcription/d2_block_digits.txt w2
```

`align.py` takes about 25 s. The decoder needs no other input.

## Transcription

Each line was read digit by digit from 3.2x crops, in thirds, joined at a one-digit overlap.

- **The `d`-shaped sign is the 8 of this hand.** It is the same glyph as a plain 8 in `3028603` (r1.10). The files
  keep `d` as written, and the scripts read it as 8.
- **Unsure readings.** `?` marks 9 unsure digits or joins in /1 and 3 in /2.
- **Corrections from the image check.** Ten places where the alignment showed a digit too many or too few were
  checked on the image at 3.6x. Four were misreadings and are corrected in the file:
  - r1.05 `501d6d7` → `5016d7`;
  - r1.07: one `15` too many;
  - r1.08 `16035265` → `160355265`;
  - r1.09 `37902d6d7` → `379026d7`.

  The other six match the page: the irregularity is the cipher's own, or the decipherment's wording.

## The cipher and the alignment

The system is two-digit groups with homophones. Doubled letters are written once (*fatto* = 58 52 87 15), u and v
share groups, and common words and titles have code groups (17 *che*, 13 *et*, 23 *per*, 18 *non*, 24 *più*,
29 S.tà, 31 M.tà, 97 V.S.). Single digits are scattered between the groups.

`align.py` runs two passes of Viterbi alignment, each re-estimating the key four times. It starts from 23 values
read by hand from a few stretches of /1 (*in questo modo pare haver… fatto alcun ritratto… speranza*, and
*la negociatione*).

- **Pass 1:** two-digit groups only. Besides group → letter, the moves are:
  - group → whole word;
  - a doubled letter with no group;
  - group → null;
  - a one- or three-digit slip.
- **Pass 2:** a letter may also be a one- or three-digit unit, so units that recur become key entries.

Result on /1 (3,192 digits, 1,785 letters):

| | count |
|---|---|
| letter units | 1,461 |
| — agreeing with the final key | **1,380 (94.5%)** |
| word groups | 95 |
| doubled letters | 42 |
| one-off irregular units | 23 |

The one-off irregular units are the remaining candidate misreadings or places where the decipherment's wording
differs. For example, the cipher has *de quelli* where the gloss writes *di quelli* (v1.05).

**Single digits.** The one-digit and three-digit entries in the key (`5` q, `4` u, `3` a, `087` t, `352` a, …) are
mostly the aligner splitting the stream around a single digit:
- `5 4` is the group 54, *qu*;
- `3 52` is a single digit followed by 52, *a*.

They fit the edition's statement that single digits are nulls (below). They are kept as the script learnt them,
not hand-edited.

## Checks on the other letters

- **/2 (independent of the key's source).** The /1 key decodes the /2 block with no change. The decode
  (`decryption/d2_block_decode.txt`) reads as continuous Italian, e.g. *…parendovi non haver altro mezo per venir
  a negociare li particulari…*. It matches the decipherment written above the block on the same page, which ends
  *per causa del S.r Don Ferrando Gonzaga è incomportabile*. The /2 decode ends *…per causa del… è
  incomportabile*.
- **/3, /4, /6 (sample lines only).**

  | sample | decode | gloss on the page |
  |---|---|---|
  | /3 first line | *[q]ui si sta con molta ancietà di vedere quel che se…* | *Qua si sta con molta anxietà di vedere quel che seguirà* |
  | /3 last two lines | *…satisfare a me stesso di servire anche in questo poco a [S.] M.tà* | the end of the f. 2r margin gloss |
  | /4 last line | *seguire le voglie et inclination[i] nostre* | the end of the f. 1v margin gloss |
  | /6 f. 2r line | *a noi … sono … vera briglia…* | the end of the f. 1v margin gloss |

  So every cipher passage looked at has a contemporary decipherment. Only /1 was checked in full.

## Prior art

Seen in the Google Books preview of M. J. Bertomeu Masiá, *La guerra secreta de Carlos V contra el Papa*
(Valencia, PUV, 2009; 2011 printing), after the key above had been rebuilt:

- **pp. 161–162, "Los cifrados numéricos":** Carpi's cipher is described as two-digit numbers for one letter,
  after Palatino's rules.
- **Note 124:** Carpi's five cipher letters are documents 46, 51, 55, 56 and 62.
- **p. 162:** the key as a table, including the nulls (any single digit, and a few two-digit groups).
- **p. 189:** the heading "[BNM, ms. 20210/15-1] [Cardenal de Carpi a Granvela]" (the letter of 6 Aug 1548).

The printed key is not copied here. Where compared, it agrees with the rebuilt key: 17, 18, 23, 24, 29, 31,
54 *q/qu*, 97, and the single digits as nulls. The edition's text of the letters was not compared with the
decipherments on the page.

## Credit and licence

Michael Brackx (`brackx`), with Claude Code (Claude Opus 5.5) under his direction. The contemporary decipherment and
the cipher are the BNE's public-domain manuscript; the transcriptions, key file and scripts may be used under the
project licence (CC BY 4.0 for text and data, MIT for code).
