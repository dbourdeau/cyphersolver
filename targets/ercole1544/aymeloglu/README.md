Status: fuller reading of catalogue 1556 (Andrew Aymeloglu, 25 Nov 2026). cc. 174r-175v, now dated Mantua, 9 January 1544: 1,277 of 1,340 word units read with nothing supplied or doubtful (95.3%). cc. 78r-79r, 4 May 1544: 731 of 779 (93.8%), read in part.

# ercole1544 / aymeloglu: second transcription, register copy and fuller reading of cc. 78r-79r and 174r-175v

Andrew Aymeloglu, with Claude (Anthropic) and OpenAI Codex, 24-25 Nov 2026. Nothing in WAINUT's or Brice Dudout's files is changed.

## How this relates to WAINUT's work

WAINUT (LcCompany, PR #221, 3 Nov 2026) recovered the table from the July 1544 pairs and read both letters in part. We did not know of that work. We started from the catalogue entry, which lists 1556 as open, and did not search `targets/` for the shelfmark. So this is a second, independent recovery of the same table and a second transcription, and it should be read as a fuller reading of WAINUT's partial one, not as a first solution. The credit for the key and the first reading is WAINUT's.

Two things follow from the independence:

- **The transcriptions agree on 94.4% of signs** (7,471 of 7,913 aligned positions over the seven pages; per page 92.1% to 96.0%), with our edited text against WAINUT's third state. Both sides knew the table when settling.
- **The letter table is the same.** Ours came from cc. 96, 102-105 and 106-110 with their decipherments; WAINUT's from cc. 103r/104r, tested on cc. 109/107.

Brice Dudout's blind shape plate (PR #975) settles signs at places we also read: his *intertener* at E21 is our reading, and his z at G06, which gives *masca* and not *tasca*, agrees with ours, *si cauara la mascara*. The register has the Pope ready to throw off the mask at that place.

## What is new

1. **The register copy.** Ercole's confidential letter-book, Biblioteca Apostolica Vaticana, Barb. lat. 5792, has the letter of cc. 174-175 in clear on ff. 5v-8v, headed *Al ditto S.or in zifra, & fuvi la minuta di man propria*, closing at Mantua on 9 January 1544, and going on past the point where the Modena leaf breaks off. It often words things differently, so it settles persons and subjects more often than letters. For 4 May 1544 it has related letters, not the cipher's text; the dispatch of 5 May recalls what Ercole wrote in cipher the day before. Folio by folio: [`vatican-register.md`](vatican-register.md). This answers WAINUT's open items "Date of cc. 174-175" and "Mantua copialettere not opened" (the confidential registers for 1537-46 are at the Vatican, not Mantua).
2. **Codes.** From the register and the text: L^6 Re d'Inghilterra, L^22 Stato di Milano, L^54 Granvela, 95 pace, 96 guerra (WAINUT's open codes), 15 mm, 21 uu, 43 S. S.ta (probable). L^30 is very probably the marchese del Vasto; that is inferred from other letters and its four uses are counted as doubtful. 44 S. M.ta and L^9 Imperatore are in the July pairs. 63 stays open (*però* fits both uses). [`key.tsv`](key.tsv) gives the source and confidence of each value.
3. **c. 175r and G02-G07 read.** WAINUT has these as decoded, not read.
4. **A reading of both letters as sentences**, with a translation.

## Files

| File | What |
|---|---|
| `transcription_0078_0079.txt`, `transcription_0174_0175.txt` | the edited transcription, WAINUT's line labels |
| `frozen/` | the shape transcription each page was frozen at before any decoding (third reader, with the first two readers' alternatives) |
| `departures.tsv` | every supplied sign (`x!`), doubtful sign (`{a/b}`) and unread sign, with the frozen reading at that place |
| `key.tsv` | the key, one value a line, with source and confidence |
| `decryption_*.txt` | the key applied to the transcription, line by line, unedited |
| `reading_*.md`, `translation_*.md` | Italian sentences and English, same blocks and holes |
| `vatican-register.md` | the register copy, the parallels and the printed sources checked |
| `blind/` | the blind readers' rows and the keys to the crops (no images) |

The scripts, the first two readers' transcriptions, the page notes and the checks are in [aaymeloglu/unsolved-ciphers, gonzaga-1545](https://github.com/aaymeloglu/unsolved-ciphers/tree/main/gonzaga-1545). `decode.py` there reproduces the decryptions from the transcriptions and the key, and `check_edition.py` and `check_readme.py` reproduce the counts.

## Method

1. Three readers transcribed each page by shape from line strips, without decoding. The third reading was frozen by SHA-256 before the key was applied.
2. An editor settled each page against the image. A sign may be changed to a listed look-alike (c/e, d/y, a/n, g/z, h for a long s joined to the next letter, and so on) when the word needs it and the shape allows it. A change the shape does not allow is marked `x!` and shows as a bracketed letter. Every departure from the frozen reading is counted: 558 of 7,892 signs (7.1%), 69 of them supplied.
3. The register copy was then collated and both letters reread (Codex).
4. Blind checks, below. Readings that failed them were moved to supplied or doubtful.

## Counts

A word unit is a word of the decryption; a code counts once even when it stands for a title of several words.

| | Read as written | With a supplied letter | Doubtful sign or inferred code | Unread | Total |
|---|---:|---:|---:|---:|---:|
| cc. 78r-79r, 4 May | 731 (93.84%) | 29 | 11 | 8 | 779 |
| cc. 174r-175v, 9 January | 1,277 (95.30%) | 42 | 11 | 10 | 1,340 |

Only the first column counts as read. The January letter is over the 95% bar on this count by four words (it needs 1,273); the May letter is not. Words that survive only in the register add nothing to either count.

What the register does add to the January count: seven word units are codes whose value comes from it (95, 96 three times, L^6, L^22, L^54). Without them the letter stands at 1,270, under the 1,273 it needs. So the January letter is over the bar only with code values taken from the register, and the reviewer should weigh that.

## Blind checks

Readers had unlabelled crops and a description of the sign shapes, and no text. Rows and crop keys are in `blind/`.

- **Names and numbers** (31 crops): both readers gave the edition's signs for 23, one of the two for 6, neither for 2.
- **The *ge* group** (*genti*, *diligentia*): both readers read a single h in six of six places. These are supplied, *[g]enti*.
- **Sixteen places in the May letter reread after the register was found**, with seven controls; key and scoring rule committed before the readers reported. Both readers gave the new signs in two places and the old signs in three; they split on the rest. Ten words were moved to supplied or doubtful: *co[n]*, *i[l]*, *[s]i*, *[s]emo*, *obgli[g]ati*, *co[s]e*, *Pi[s]a*, *[L]iuorno*, *[s]a*, and the name code at B08. That took the May letter from 741 to 731, under the bar. The readers were not consistent on the controls either (two of seven matched sign for sign), so a split is weak evidence both ways.
- **Thirty-eight places in the January letter reread after the register was found**, with nine controls, key committed first; single swaps inside one look-alike pair were left out. Six of nine controls matched sign for sign. Both readers gave the new signs in six places and the old signs in four. Eleven readings were not confirmed on the changed signs and ten words were moved to supplied or doubtful: *[?non]* (D07), *[?Fernese]*, *ne [s]e*, *s[i]a*, *a[cc]enna*, *p[er]*, *ue[n]uta*, *pre[g]aua*, *s[a]ppeuo*, *[la]*, *ta[n]to*. That took the January letter from 1,287 to 1,277.
- **D07, *non* or *ben*.** Both blind readers saw 55 (*ben*) and not 53 (*non*) in *[?non] m'ho sapputo imaginar la ragion*. The register has the negative (*né io mai ho saputo imaginarmi la ragion*), and the sentence needs it; WAINUT's transcription can be compared at this place.
- **Figure groups or letters.** The pairs read as 95, 96, 61 and 64 were given by one reader as digits and by the other as letters (z s, z b, b i, b q). The shape allows both; the choice rests on the sense and, for 95 and 96, on the register.
- **A second edit of c. 174r** from a checkout with no edition in it agreed on 321 of 328 words.

## Open

- Eighteen word units unread, among them A27 and G06-G07.
- The name code at F07 and F24, where the register names the Emperor: the raised figures are not those of L^10 (Papa) and were read L^11, L^10 or L^19 on crops. The same doubt at B08.
- L^30 inferred, 63 open, 28 perhaps a null.
- The informant in Rome is not named.
- No palaeographer and no person without AI has checked the transcription. Every reading here was made by AI agents.

## Images

Biblioteca Estense, Lodovico Media Library IIIF, licence stated CC BY-NC-SA: used privately, none committed. Biblioteca Apostolica Vaticana, DigiVatLib: viewed online and linked, none committed. The conditions of neither library were checked for analysis with an AI assistant, and neither library was asked.
