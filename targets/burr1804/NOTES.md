# Aaron Burr to Joseph Alston, New York, [c. 20 July] 1804: the stroke-and-figure cipher on the clear page (catalogue 2049)

Status: read. Key recovered from the ciphertext alone (simple substitution, 132 signs, every one read), 5 Nov 2026.

## The document

- Gilder Lehrman Collection, **GLC01523**: Aaron Burr to Joseph Alston, unsigned, addressed at the foot "J. Alston
  Esqr", with the direction "Enclose to Chs. Biddle, Phila". Gilder Lehrman dates it c. 13-21 July 1804; the Hamilton
  Education Program transcript heads it 20 July 1804. Burr's 18 July letter (Davis, *Memoirs*, vol. 2) says "Write under
  cover to Charles Biddle, Philadelphia", and this letter says the jury "have adjourned over to Monday Eveg (23d.)",
  so it was written between 18 and 21 July 1804, before Burr left New York on the 21st.
- Images: Hamilton Education Program, https://hamilton.gilderlehrman.org/supporting-document/burrs-coded-letter-about-duel-1804
  (`GLC01523_Page_3.png` is this page, 1200x1400); Google Arts & Culture asset `_AHwqSQ7laubpw`. Images not committed.
- The page is in clear except ten lines (lines 15-21 here) in a cipher of figures and hatched stroke signs, with
  clear words between ("made of more", "The advice comes with double force", "being about 20,000", "To").
- Gilder Lehrman's catalogue says "The second and third pages are in cypher" and the Hamilton page says "The cyphered
  part of the letter has not yet been decoded". The "second and third pages" are two sheets of number cipher filed
  with the letter. **They are a different letter and a different cipher**: Burr at Baltimore, 31 Jan, 10 Feb and
  18 Feb [1808], in a period-6 Vigenère (docket "Balt. ... 1808" on one sheet, pencil "1523A" on the other). They have
  their own folder and page: `../burr1808/` (one key, one entry).

## The cipher

Simple substitution, one sign per letter, words kept apart, clear words mixed in. The signs are figures for a-l and
hatched stroke groups (written by Gilder Lehrman's transcriber as Roman numerals) for m-u, with three odd signs:

| a | b | d | e | f | g | h | i | l | m | n | o | p | q | r | s | t | u | v | w | y |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 5 | 4 | 2 | 1 | 0 | 6 | 7 | 8 | 10 | II | III | IV | V | VI | VII | VIII | IX | X | Y | λ | (-) |

The key is built in runs: a-f count down 5 to 0 (c = 3 would be the unused value), g-i count up 6 to 8, and m-u are
Roman numerals II to X in order (l = "10", written like "lo", sits where I would be). c, j, k, x, z do not occur.

## The reading

Transcription: `transcription.txt`, decryption: `decryption.txt`, reading: `reading.md`, key: `key.tsv` (sign labels checked against the image; Gilder Lehrman's transcript drops two
groups in line 19, "II X VII 2 1 VII | 4 1" = "murder be", which the image has).

> - as you are not made of more pl[e]ant [pliant?] materials than myself. The advice comes with double force -
> The little band - being about 20,000 in this state [struck word] stand firm -
> If the inquest of murder be found, what would you advise - To stand - to go to Europe or what? -

Context: the coroner's jury on Hamilton's death had sat four times by 18 July; Burr wrote that day that its object
was "to obtain an inquest of murder" (Davis, *Memoirs*, vol. 2). It returned "wilful murder" on 2 August. Here Burr asks his
son-in-law, in cipher, whether to stand trial or go to Europe if the inquest finds murder, and counts "the little
band" of his supporters in New York at about 20,000. He left New York on 21 July, for Perth Amboy and Philadelphia, and then went south.

Measured: 132 cipher signs, 132 read (100%). One word is uncertain: "pleant" (V 10 1 5 III IX), one sign off
"pliant"; the third sign is clearly the e-sign (1). Grade C (read in context; the spelling may be Burr's).

## Prior work

- Not deciphered before, as far as found: Gilder Lehrman (catalogue, AMDigital record, Hamilton Education Program)
  says undecoded; Davis, *Memoirs of Aaron Burr* (1837) prints Burr to Alston 13, 18 and 29 July 1804 but not this
  letter (Gutenberg #7851 grepped for "pliant", "little band", "inquest", "double force"); Kline and Ryan, *Political
  Correspondence and Public Papers of Aaron Burr* (1983): the table of contents (archive.org search-inside, pp. 25-27)
  lists for July 1804 only letters to Van Ness and Charles Biddle, no letter to Alston; the volume 2 text is not
  indexed. Tomokiyo's cryptiana has Burr only for the 1806 Entick code. Not on DECODE.
- So the reading is new unless Kline's volume 2 annotation quotes it; the July 1804 section of vol. 2 (pp. 876-889)
  was not read.

## Remaining gaps

None. Every sign reads; "pleant" is flagged.

## Escalation

- [n/a] siblings: no other Burr letter in this stroke cipher found (Davis's July-August 1804 letters are in clear)
- [x] clear-pages: the letter's clear lines and Davis's 18 July letter give the context ("inquest of murder")
- [n/a] known-keys: no key needed; recovered from the text
- [x] print: Davis 1837 grepped; Kline 1983 table of contents read; cryptiana; DECODE harvest
- [n/a] key-rebuild: key complete for every letter that occurs
- [n/a] retry: nothing unread
