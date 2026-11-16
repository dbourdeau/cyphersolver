# Morier 1808: Harford Jones's letter to Lord Minto in figure cipher (IOR/L/PS/9/67/18-21)

Status: read (catalogue 2649). Lead from Daniel Bourdeau's Koç/Ottoman deep sweep (14 Nov 2026).

British Library, India Office Records, Political and Secret, IOR/L/PS/9/67. Free images on the Qatar Digital
Library (links only; the images are not in this repository):

| item | QDL record | what |
|---|---|---|
| /18 | https://www.qdl.qa/en/archive/81055/vdc_100038378586.0x000016 | Sir Harford Jones to the Governor General (Minto), Bombay 28 Apr 1808, "True Copy" in figures signed Jas. Morier, Priv. Sec.; enclosed in Jones's letter to the Secret Committee of 30 Apr 1808 (20 images) |
| /19 | https://www.qdl.qa/en/archive/81055/vdc_100038378586.0x000017 | the ninth paragraph of Minto's instructions to Malcolm, in figures, with the clear text written in the margin (4 images) |
| /20 | https://www.qdl.qa/en/archive/81055/vdc_100038378586.0x000018 | a second figure copy of /18, ending "I have the honor to be &c" in clear and a figure signature; docket "Recd 6 June 09" (12 images) |
| /21 | https://www.qdl.qa/en/archive/81055/vdc_100038378586.0x000019 | a second figure copy of /19, without the clear text (4 images) |

## The system

- Homophonic substitution of letters by figures 2-99. A letter has two to five figures, e.g. e = 2 6 8 40 74 (94),
  t = 7 44 50 77, h = 5 60. The cipher uses one letter for u/v and one for i/j.
- A stop ends a word and a comma joins figures within a word. The copyists cut and join words freely.
- A few 3- and 4-figure groups stand for words: 8674 = Persia, which takes suffixes ("8674,90,66" = Persians);
  4040 = French (probable); 630 = Bombay (probable).
- The heading is "630. 9,63,79,98,68. 128. 218081." = Bombay April 28 1808. The figures of the date carry the nulls
  1 and 2. The signature on /20 is "2,5,9,43,1,36,2,43,1,30. 98,2,90,8,66,1.", read as Har(f)ord J(o)nes with the
  nulls 1 and 2 (probable).
- The key is `key.json` (62 figures). Two figures were found after the measure: 88 = z (authori[z]ed) and 94 = e
  (therefor[e]). They are added in `decode.py`, not in the frozen key.
- This is not the code of targets/jones1802. That one is a page,word code book used by Jones at Baghdad in
  1798-1802. Here each figure group stands for one letter, and no jones1802 value applies.

## How it was read

1. Transcription by Claude (Opus 5.5) from the QDL images, made in Chrome by Brice Dudout on 16 Nov 2026, of all
   four items. /18 and /20 are two copies of the same text, so each served to collate the other.
   - `transcription_18_part1.txt`: /18 images 0002-0004, 0006, 0010, 0011, 0015, 0017, 0020.
   - `transcription_18_f6v-f7v.txt`: /18 images 0012-0014.
   - `transcription_20.txt`: /20 images 0001, 0003, 0004, 0005, 0008, 0009, and the passage written in the margin
     of 0007.
   - `transcription_21.txt`: /21 image 0001.
2. The key was solved by simulated annealing over figure-to-letter maps, scored by an English 4-gram model, with
   the stops kept as word boundaries. It was solved on /18 + /20 only. The 4-gram model came from a 19th-century
   English diplomatic corpus (Project Gutenberg, Lord Lyons vol. 1).
   - Every restart converged on the same readable English: "the inclosed copy of a letter No. 2 addressed by me
     on the following day to the Hon. the Gov. here…".
   - Four values were then fixed by hand: 34 = k, 2 = e, 6 = e, and 24 is the numeral 24 ("the 24 inst").
3. Held-out measures (`verification/`):
   - **First test, failed.** PREREG v1 (`PREREG.md`, frozen before the key search) held out /21 image 0001
     (316 figures, 72 words).
     - The measure was the share of decoded words found in the corpus vocabulary.
     - The result was 0.729, against a best control of 0.157 over 200 within-class key shuffles. That fails the
       0.85 bar.
     - No word was misread. The misses were copyists' cuts (g en, instructi ons), names (Malcolms, Bagdad,
       Pashaw, Harford, Jones), u/v spellings (enuoy, euent), and the copy errors cort and accreditted.
     - That portion is burned.
   - **Second test, passed.** PREREG v2 (`PREREG_v2.md`) was frozen before the new portion was transcribed. It
     held out /18 images 0012-0014 (444 figures, 94 words), new text not used for the key.
     - The metric allows u/v and i/j and a fixed list of names, and it counts copyists' cuts and joins
       separately.
     - The score was S2 = 0.968 (word 86, name 2, split 2, join 1, fail 3), against a best control of 0.340. The
       bar was max(0.85, 0.640), so it passed.
     - The strict share of plain dictionary words alone was 0.915.
     - The key was not changed between the two tests. /19 was dropped from H2 before transcription, because it
       is a copy of the burned /21 text with its clear text in the margin.
4. The reading as sentences is in `reading_18.md` and `reading_21.md`.
   - In the 94 words of H2: 90 sure, 1 probable (88 = z), 3 restored ([mor]e, relin[q]uish, thin[k]), 0 open.
   - In the whole letter (676 words): 1 word unread, the place in "from ‹to› Roads".

## Prior art

- Catalogue 2649 (14 Nov 2026) listed no decipherment, and none was found in the BL or QDL records.
- **Contemporary decipherment of the enclosure.** /19 carries in its margin the clear text of the ninth
  paragraph, written at the time. Our reading of /21 was made from the key alone, before /19 was seen, and agrees
  with it word for word.
- **Pencil notes.** A later reader pencilled a few letters between the lines of /18 ff. 7-8 (images 0013-0015,
  e.g. "receiving"). This is a partial key-free decipherment of a few words. It was not used.
- No clear copy of the /18 letter was found in these four items. The original, or a clear copy, may be among
  Minto's papers or the Bengal Secret enclosures; that was not checked.

## Gaps

- "from ‹to› Roads" in the opening: written "44,36" in both copies, which reads "to". A copying slip for a place
  name.
- 4040 = French and 630 = Bombay are probable, read from context and the heading.
- The figure signature is probable.

The scripts in `verification/` are kept as run (paths point to the contributor's local copies of the transcriptions and of the Lord Lyons corpus); `measure.py` is the v1 measure, `v2.py` + `measure_v2.py` the v2 measure.
