# butzbach1641: numeric cipher sheet in HStAD D 4 Nr. 76/6 (Landgraf Philipp of Hesse-Butzbach, "Varia")

Status: read in part, with the key found in the same file (read with known key). 98 of 124 words sure = 79.0 % (95 on 17 Nov 2026; 97 after the blind shape check of 18 Nov 2026; "mittwoch" made sure by the blind shape check of 25 Nov 2026).

## Source

Hessisches Staatsarchiv Darmstadt (HStAD), D 4 Nr. 76/6 (Arcinsys he:v5549727, "Varia", 1641; record in
`research/sweep_2026-11_german_portals_2/arcinsys_detail.json`). Digitised microfilm via Deutsche Digitale Bibliothek /
Archivportal-D (IIIF):
- cipher sheet: view 13 (film frame 0416), IIIF image `c7eca322-4298-457d-a7d9-dc7b23f8283c`; the sheet is written
  sideways (turn 90 degrees clockwise);
- key strip: view 11 (film frame 0414), IIIF image `c4df6eac-a485-4535-abb1-e323b26fbc60`, small strip lower left.

No image is included here. The IIIF `full/max` is capped at 2500 px; region requests at full resolution (3500 x 2544)
work and were used for the crops.

New scan: on 25 Nov 2026 HStA Darmstadt sent Brice Dudout a new colour scan of view 13 and of its verso (two TIFFs of
about 5700 x 7700 px, received as mirror images), for private study. It is not public, not included and was not seen
here. The reading counted in this folder is still the microfilm reading; the blind check of 25 Nov 2026 was answered on
the new scan, and Brice Dudout's re-reading of it (with the verso, a second letter in the same cipher) is to come in a
separate pull request. What it gives is known here only from his comment on PR #781.

Date: 1641 (file), 1633/34 suggested by Brice Dudout, not checked. The file is dated by a 1641 almanac it contains, but
it is a collection of ciphers (it also holds a "Union" alphabet of 1618-1620 and items of Ludwig V, d. 1626). The content
(Philippsburg blockaded, Imperial and Spanish troops at Saverne, relief promised before New Year) would fit winter
1633/34; the military events have not been checked. On the new scan, as reported by Brice Dudout (PR #781, not seen
here), the end of line 29 and the two "slips" (lines 30-31 of the sheet) give the place and date: Hagenau, 22 December,
with no year written; "decembris" probable (the cipher has "decemmris") and the sign after it unresolved. This is not
in this folder's transcription.

## The piece

A loose sheet, about 28 lines and two small pasted slips: two-digit numbers run together, words separated by dots,
`||` at line breaks inside a word. Not the vowel-sign key (a e i o u h) on the sheet lying above it on the same view.
Microfilm, black and white; a blot and a hole with a pasted slip affect lines 1, 7-8, 20, 24 and 26-28.

## Key (`key.tsv`)

From the strip on view 11: a=11 b=12 c=13 d=14 e=15 f=16 g=17 h=18 i=19 k=20 l=21 m=22 n=23 o=24 p=25 q=26 r=27 s=28
t=29 u=30 w=31 x=32 y=33 z=34 (24 letters; v written u, j written i). No key recovery, so no held-out measure; the key
was checked on the whole sheet: of 682 numbers read, 667 (97.8 %) fall in 11-34 and the result is continuous German.
Off the strip: 39 (10 times) behaves as a second u (und, zu, uff, zum), 38 (4 times) as a second o (sollicitirt, alhero,
noch, bishero); one 398 on a slip is unresolved. An overbar doubles a letter.

## Files

| file | content |
|---|---|
| `transcription/pass1.txt` | pass 1, full, on crops `p1` (French notes, as written) |
| `transcription/pass2.txt` | pass 2 on other crops (bands x3, single lines x4); lists only the lines it read differently or resolved (French notes, as written) |
| `transcription/digits_arbitrated.txt` | arbitrated digits, one manuscript line per line, settled on the image |
| `transcription/pass_differences.md` | the two passes and the arbitration side by side, line by line, with the differences |
| `key.tsv` | key with the view reference |
| `decode.py` | decoder: `python3 decode.py transcription/digits_arbitrated.txt` |
| `decryption.txt` | its output, with the count of numbers in and off the key |
| `blind_check/` | blind shape checks of 17 Nov 2026 (microfilm) and 25 Nov 2026 (new scan): sheets (questions and boxes), answer keys, answers as exported, SHA-256 values; why 19 places were prepared and 15 asked in the first |
| `reading.md` | reading (sure / {probable} / [restored] / ‹unresolved›), count, the 11 unresolved places, translation |

## Transcription

Two passes by the same reader (Claude, for Brice Dudout), 17 Nov 2026: the second on different crops without
reopening the first file, so blind only in the sense of the file. Pass 2 re-lists 15 lines in full and 5 in part;
the others it read as pass 1. Arbitration on the image. Details in `transcription/pass_differences.md`.

Open point: in "entsetzung" (line 1) the arbitrated digits are 15 23 28 29 28 15 29 34 39 23 17 ("enstsetzung"). At high
zoom the word seems to be 15 23 29 28 15 29 34 39 23 17, without the third number (pass 1 read it 32, pass 2 [3]2?).
In the blind check of 18 Nov 2026 (reading.md) Brice Dudout saw the last number as 27, not 17. The word stays probable.

## Transcription doubts

The doubts are those the two passes flagged or disagreed on (`transcription/pass_differences.md`) and those put to the
two blind shape checks (`blind_check/`). "transcription" below means the two passes by the same reader and, where named,
Brice Dudout's blind answer on one boxed number; there is no independent transcriber.

- l. 1 "entsetzung", the number under the blot - read: 28, word {probable} ("enstsetzung", one number too many); checked: image (at high zoom the word seems one number shorter), decode, transcription (pass 1 32, pass 2 [3]2?; blind check 18 Nov confirmed the 29); not settled
- l. 1 "entsetzung", last number - read: 17 (g), word {probable}; checked: image, decode, transcription (blind check 18 Nov: seen as 27, r); the shape answer goes against the reading, so the word stays probable
- l. 1 "die" - read: 14 18 15 (dhe), {probable}; checked: image, decode, transcription (blind check 18 Nov: 18 confirmed as written)
- l. 3 "tag", the 11 - read: 11, {probable}; checked: image, decode, transcription (blind check 18 Nov: 11 confirmed, with a remark on a mark or two dots above it)
- l. 3 "Zabern", the 11 written as two strokes - read: 11, {probable} as a place name; checked: image, decode, transcription (blind check 18 Nov: confirmed)
- l. 5 and l. 9 "keyserischen" / "keyserische", faded first half - read: {probable}; checked: image, decode, transcription (passes differ at 32 21 18 / 33 28); not put to a blind check (faded, not a choice of shapes)
- l. 6, 11, 20 the number 38 (sollicitirt, alhero, noch, bishero) - read: 38 = o, deduced; checked: image (shape clear), decode (14 contexts with 39); the value, not the shape, is the doubt, so sollicitirt and alhero stay {probable}
- l. 7-8 "pas‹…›" / "‹…›rt" - read: ‹unresolved›; checked: image (crossing-out and blot), decode (a verb in -irt), transcription (pass 1 `?? 20 ??`, pass 2 `28 20` + crossing-out; pass 1 `28 29 19 19 27 27 29` for l. 8); not settled
- l. 12 "mittwoch", 5th number - read: 31 (w), sure; checked: image (microfilm cannot tell 31 from 34), decode (34 = z gives "mittzoch"), transcription (pass 1 34, pass 2 31; blind check 18 Nov left it open; blind check 25 Nov on the private colour scan: 31)
- l. 16 "also" - read: 11 21 28 24, {probable}; checked: image, decode, transcription (blind check 18 Nov: "none / other" with the remark "28 ?"); not settled
- l. 19 "dapffer" - read: 14 11 25 16 16 15 27, sure; checked: image, decode, transcription (pass 1 "defension", pass 2 "dapffer (?)"; blind check 18 Nov: 11 and 25 confirmed)
- l. 24 end of "gesch‹…›" - read: ‹unresolved›; checked: image, decode, transcription (pass 1 `27 18 27 ?? 15 ??`; blind check 18 Nov on the microfilm: 27 … 22, no word; blind check 25 Nov on the private scan: 24 and 23, which Brice Dudout reads as "geschossen" there); not counted until the new-scan transcription is in the folder
- l. 26 "gräfliche", first numbers - read: 17 27 11 16 21 19 13 18 15, sure; checked: image, decode, transcription (pass 1 `17 27 ??`; blind check 18 Nov: 17 confirmed)
- slip S2 398 - read: ‹398› unresolved; checked: image (three digits), decode (off the key, no value), transcription (both passes read 398)

## Reading and count

See `reading.md`. 124 words: 98 sure, 15 probable or restored, 11 unresolved (after the blind checks of 18 and 25 Nov 2026). By the repository rule (sure words only)
98 / 124 = 79.0 %, read in part. Our count with probable words was 113 / 124 = 91 % (letter body, lines 1-25: 96 %);
it is that, a count with probable words. In the letter body the writer has been at Zabern pressing the Imperial and
Spanish commanders for the relief of Philippsburg; regiments are on the march; the addressee is to encourage the
officers and soldiers to hold until New Year; the money for them is ready. Sender and addressee are not named.

## Blind shape checks

Two blind shape checks, both answered by Brice Dudout, the contributor of the reading (he knows the text; the sheets
show no letters or words). Each question boxed one number and offered crops of sure numbers of the same hand as
options. Sheets (questions and boxes), answer keys, answers and SHA-256 values: `blind_check/` (README there).

- 18 Nov 2026 (sheet of 17 Nov), on the public microfilm: 15 questions, 12 targets and 3 controls, 3 of 3 controls as
  expected. "gräfliche" (l. 26) and "dapffer" (l. 19) made sure (95 -> 97 sure). The last number of "entsetzung" was
  seen as 27 (r), not 17 (g): the word stays probable. The end of "gesch‹…›" (l. 24) was seen as 27 … 22, no word: it
  stays unresolved. "tag", "mittwoch" and "also" were left open by his remarks; "die" (dhe) and the 11 of "Zabern" were
  confirmed as written and stay probable. A first sheet of 19 places was replaced the same evening, unanswered (README).
  No selection rule was written and hashed before the answers.
- 25 Nov 2026, on the private colour scan: 9 questions, 6 targets and 3 hidden controls, 3 of 3 controls as expected.
  The fifth number of "mittwoch" was seen as 31 (w): mittwoch made sure (97 -> 98 sure). The other answers bear on
  words of the new-scan reading only and are not counted here: the end of "gesch…" seen as 24 and 23, which Brice
  Dudout reads as "geschossen" on the new scan; the last number of "Hagenaw" seen as 31; the middle number of
  "decembris" seen as 22 ("decemmris", stays probable); the sign after it matched none of the shapes offered. A
  selection rule is reported as written and hashed before the crops (`90e1082c…1136c`); its text and the addendum are
  not in the repository, so the hash rests on the author's statement.
- Neither check is `outcome.sign_check`: the first had no rule hashed before the answers, the second has 6 target signs,
  under the minimum of 8. Both are recorded here and as solution steps (18 and 25 Nov 2026).
- Not a second reading: no person other than the contributor has checked the reading against the image.

## Prior work

The repository had the Arcinsys record only (no lead, no reading). No edition found in a quick web search; nothing in
our own folders on D 4 Nr. 76/6.

## Credits

Images: Hessisches Staatsarchiv Darmstadt, D 4 Nr. 76/6, via Deutsche Digitale Bibliothek / Archivportal-D.
Transcription, decoding and reading: Claude (Anthropic) for Brice Dudout (L'Europe chiffrée), 17 Nov 2026; blind
shape checks answered by Brice Dudout, 18 and 25 Nov 2026.
New scan: Hessisches Staatsarchiv Darmstadt, D 4 Nr. 76/6, new colour scan of view 13 and its verso, 25 Nov 2026; the
free new photography was granted by Dr. Rainer Maaß and delivered by K. Weber (Fotowerkstatt), as Brice Dudout reports.
Private study, not shared and not included; AI analysis was not raised with the archive.

Reading review: recorded in the profile as the integration review of PR #781 (an AI agent, for the maintainers; not a
person), 25 Nov 2026. The contributor's own note (Claude for Brice Dudout, 17 Nov 2026, grade B) said: known key; two
passes by the same reader; not a second reader.

## Remaining gaps
- l. 7-8, the word "pas‹…›" / "‹…›rt" (a verb in -irt) - blocker: illegible; crossing-out and blot on the microfilm; a private colour scan exists, re-reading in a follow-up pull request
- l. 20, first word; l. 24 end of "gesch‹…›"; l. 26 fourth word and "all‹…›"; l. 27 last word; l. 28 "wer‹…›"; slip S1 second word - blocker: illegible; blot, hole and cut slip on the microfilm. A private colour scan now exists (25 Nov 2026); the re-reading on it is to come in a follow-up pull request (Brice Dudout reports "geschossen" for l. 24 and the date on the slips)
- slip S2: the number 398 (off the key, three digits, read the same in both passes) - blocker: no-key-material; legible but no value known
- slip S2: "sammigerku…" - blocker: no-key-material; legible, the decode gives no sense

## Escalation
- [x] siblings: the 68 views of the file were fetched; the key strip is on view 11; the sheet lying above the cipher on view 13 is a different, vowel-sign key and does not fit
- [n/a] clear-pages: no decipherment on the sheet (profile: plaintext none); the other leaves of the file were not read for a clear copy, which is not an outside blocker and is left to the contributor to decide (noted 17 Nov 2026 at the claims review of the write-up)
- [x] known-keys: the strip on view 11 of the same file applied to the whole sheet (667 of 682 numbers in 11-34)
- [x] print: no edition or reading found in the repository, own folders and a quick web search
- [n/a] key-rebuild: the key is on the strip; only 38 = o and 39 = u were deduced from 14 contexts
- [x] retry: two passes on different crops, arbitrated on the image; two blind shape checks answered by Brice Dudout (18 Nov 2026, 15 questions on the microfilm; 25 Nov 2026, 9 questions on the new scan; 3 of 3 controls each), which made gräfliche, dapffer and mittwoch sure; nine of the unresolved places stay blotted or cut on the microfilm; 398 and "sammigerku…" are legible and unexplained
