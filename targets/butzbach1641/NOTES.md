# butzbach1641: numeric cipher sheet in HStAD D 4 Nr. 76/6 (Landgraf Philipp of Hesse-Butzbach, "Varia")

Status: read in part, with the key found in the same file (read with known key). 95 of 124 words sure = 76.6 %.

## Source

Hessisches Staatsarchiv Darmstadt (HStAD), D 4 Nr. 76/6 (Arcinsys he:v5549727, "Varia", 1641; record in
`research/sweep_2026-11_german_portals_2/arcinsys_detail.json`). Digitised microfilm via Deutsche Digitale Bibliothek /
Archivportal-D (IIIF):
- cipher sheet: view 13 (film frame 0416), IIIF image `c7eca322-4298-457d-a7d9-dc7b23f8283c`; the sheet is written
  sideways (turn 90 degrees clockwise);
- key strip: view 11 (film frame 0414), IIIF image `c4df6eac-a485-4535-abb1-e323b26fbc60`, small strip lower left.

No image is included here. The IIIF `full/max` is capped at 2500 px; region requests at full resolution (3500 x 2544)
work and were used for the crops.

Date: 1641 (file), 1633/34 suggested by Brice Dudout, not checked. The file is dated by a 1641 almanac it contains, but
it is a collection of ciphers (it also holds a "Union" alphabet of 1618-1620 and items of Ludwig V, d. 1626). The content
(Philippsburg blockaded, Imperial and Spanish troops at Saverne, relief promised before New Year) would fit winter
1633/34; the military events have not been checked.

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
| `reading.md` | reading (sure / {probable} / [restored] / ‹unresolved›), count, the 11 unresolved places, translation |

## Transcription

Two passes by the same reader (Claude, for Brice Dudout), 17 Nov 2026: the second on different crops without
reopening the first file, so blind only in the sense of the file. Pass 2 re-lists 15 lines in full and 5 in part;
the others it read as pass 1. Arbitration on the image. Details in `transcription/pass_differences.md`.

Open point: in "entsetzung" (line 1) the arbitrated digits are 15 23 28 29 28 15 29 34 39 23 17 ("enstsetzung"). At high
zoom the word seems to be 15 23 29 28 15 29 34 39 23 17, without the third number (pass 1 read it 32, pass 2 [3]2?).
A blind check of this and 18 other numbers has been prepared for Brice Dudout and not yet answered. The word is counted
probable either way.

## Reading and count

See `reading.md`. 124 words: 95 sure, 18 probable or restored, 11 unresolved. By the repository rule (sure words only)
95 / 124 = 76.6 %, read in part. Our count with probable words was 113 / 124 = 91 % (letter body, lines 1-25: 96 %);
it is that, a count with probable words. In the letter body the writer has been at Zabern pressing the Imperial and
Spanish commanders for the relief of Philippsburg; regiments are on the march; the addressee is to encourage the
officers and soldiers to hold until New Year; the money for them is ready. Sender and addressee are not named.

## Prior work

The repository had the Arcinsys record only (no lead, no reading). No edition found in a quick web search; nothing in
our own folders on D 4 Nr. 76/6.

## Credits

Images: Hessisches Staatsarchiv Darmstadt, D 4 Nr. 76/6, via Deutsche Digitale Bibliothek / Archivportal-D.
Transcription, decoding and reading: Claude (Anthropic) for Brice Dudout (L'Europe chiffrée), 17 Nov 2026.
