# jefferson1787 — Jefferson's Code No. 11 (the Barclay–Lamb code), 1786-1791

Status: read in part (16 Nov 2026, recounted over cipher words: about 0.96 of the words of the readings; 8 of 17 documents with words at or above 95%; 5 moved from read to read in part)

Catalogue no. 483 (Founders Online sweep, `research/founders_emlo/`). Worked 26 Oct 2026 from the solve-page brief.

## What it is

Code No. 11 in the numbering of *The Papers of Thomas Jefferson* (Boyd et al., Princeton 1950–) is the code Jefferson
and John Adams gave Thomas Barclay and John Lamb for the Barbary missions of 1785. Barclay used it from Madrid (1786)
and from France (1787); William Carmichael at Madrid had a faulty copy (left by Barclay via David Franks), then a
checked copy from Jefferson (1 Feb 1788), and used it to 1789; Jefferson used it with Carmichael to 1791 and once, by
mistake, with Adams (28 Sep 1787); William Short used it in despatches to Jay (Oct 1789). No key sheet survives. The
Jefferson Papers editors decoded every passage from a partial reconstruction and printed their guesses in brackets.

The system: a two-part numerical code of about 1,750 groups (numbers 1-1750 not in alphabetical order), each a word,
syllable, single letter or punctuation mark, groups separated by dots. Homophones exist: full stop 1013 and 1235,
"is" 1363 and 1306, "the" 1196 and 1190, "their" 1365 and 1565, "minister" 396 and 896.

## Sources and files

- `founders_passages.md`: the printed text of every coded passage (Founders Online), with the editors' notes on numbers.
- `images_manifest.tsv`: Library of Congress, Thomas Jefferson Papers series 1, master images on tile.loc.gov (images
  are not committed). LoC item pages sit behind a bot check; frames were found by item JSON (early in the session) or
  by probing tile.loc.gov thumbnails.
- `transcription/*.tsv`: every code group, letter by letter, with TJ's interlinear decoding (RCs), the clear-text
  sheet (TJ's letters) or the decoding in the State Department copy (Short), and notes on doubtful digits. 18 letters.
- `attested_key.py` → `key.tsv`: 348 values attested outside the editors' reconstruction (T = TJ's interlinear over
  that group, S = a clear-text sheet where the word sits on one group, P = a pair printed in the notes).
- `make_reading.py` → `reading.tsv` (each group's reading and grade) and `validation.tsv`.
- `make_passages.py`, `segment.py`: a segmentation solver tried and not trusted (see WORKLOG).

| Letter | LoC frames | Groups | Plaintext from |
|---|---|---|---|
| Barclay → Commissioners, Madrid 10 Apr 1786 | 005_0494-0497 | 153 | TJ interlinear |
| Barclay → TJ, undated [ca. 3 Jul 1787], two coded footnotes | 007_0476-0481 (filed under 12 Jun 1787) | 7 | — |
| TJ → Barclay, 4 Jul 1787 (PrC) | 007_0605-0606 | 17 | editors only |
| TJ → Carmichael, 25 Sep 1787 (PrC + clear sheet) | 008_0145-0149 | 219 | TJ clear sheet |
| TJ → Adams, 28 Sep 1787 (PrC) | 008_0161-0163 | ~30 | illegible in PrC |
| TJ → Carmichael, 15 Dec 1787 (test line) | 008_0689; plaintext 007_0489 | 40 | 14 Jun 1787 PrC |
| Carmichael → TJ, 8 May, 29 May, 5 Jun, 24 Jul 1788 | 009_0339-0342, 0469-0472, 0516-0517, 0892-0895 | 509 | TJ interlinear |
| TJ → Carmichael, 3 Jun 1788 (PrC + list) | 009_0503-0511 | 74 | TJ list |
| TJ → Carmichael, 25 Dec 1788 (PrC) | 010_0626-0630 | 32 | editors only |
| Carmichael → TJ, 26 Jan 1789 | 010_0877-0885 | 182 | TJ interlinear |
| TJ → Carmichael, 9 Aug 1789 (PrC) | 011_0780-0783 | 27 | editors only |
| Short → Jay, Paris, 9 Oct, 25 Oct, 28 Oct 1789 (Nos. 2, 5, 6) | NARA M34 roll 2, frames 0010-0012, 0017, 0020 | 120 | decoding in the copy (Nos. 2, 6); editors (No. 5) |
| TJ → Carmichael, 11 Apr 1791 (PrC + "decyphered" sheet) | 014_0279-0285 | 544 | clear sheet |

## Key

Rebuilt from the plaintext next to the ciphertext: Jefferson's interlinear decodings of Barclay's and Carmichael's
letters, the clear-text sheets that go with his own (25 Sep 1787, 3 Jun 1788, 11 Apr 1791) and the decoding written
in the State Department copies of Short's despatches. 348 values attested
(`key.tsv`). The editors' reconstruction was built the same way ("made up from various passages in the
correspondence"), but they printed no table; `key.tsv` is the first published table of Code No. 11 values. It is
partial: a code of ~1,750 groups, of which the 18 letters use about 800 distinct numbers.

## Reading

All coded passages already carry a reading in *The Papers of Thomas Jefferson* (prior solution, used here for
alignment). Measured over the transcribed groups (`make_reading.py`): **1,868 of 1,917 counted groups carry a
reading (97.4%)**; grades H 1,519 (a contemporary decoding or clear sheet), C 153 (value attested in another letter),
M 216 (editors' reading not checked by another occurrence), I 16 (conjecture). 37 groups excluded: TJ quoting Carmichael's
numbers back to him (3 Jun 1788) and groups struck out by the writers.

### The conjectured passages, checked against the key

1. **TJ → Barclay, 4 Jul 1787** (the target of the brief). Groups: `M. 1420. 1336. 459. 1089.` (de Rayneval),
   `M. 1420. 374. 1139. 1128.` (de Montmorin, twice), `of the 495.` (editors: [sea]), `223. him.` ([trouble]),
   `1336. 459. 1089.` ([Rayneval]).
   - 1420 = de: confirmed independently: the 15 Dec 1787 test line opens 1420.1250.1194.1307 = De-ar Si-r.
   - [Rayneval] 1336.459.1089: 1336 and 459 occur nowhere else. 1089 ends Carmichael's "imperi-al" (TJ's decoding,
     29 May 1788) but stands for "la" in "la-t-ter" twice in 1791. A name in three groups ending -al/-la after "M. de",
     in the conference on Barclay's case, fits Rayneval (Montmorin's premier commis); grade I, not verified.
   - [sea] 495: **not supported.** 495 is "larg-" in Barclay's 10 Apr 1786 letter ("a 495.1243 sum", TJ wrote
     "larger" over it; 1243 = -er; digits checked at 4x). "Sea" is 1164 in TJ's decoding of L'Oiseau (Carmichael
     29 May 1788). "Opposition from another quarter of the larg[e]" does not read; the word is open (an encoding slip by
     TJ, or a value the 1786 decoding hides). The opposition, from TJ's letter to Jay of 21 Jun 1787, came from the
     ministry of justice side (Lamoignon, garde des sceaux), not from England.
   - [trouble] 223: occurs nowhere else; grade I.
2. **Barclay's footnotes, ca. 3 Jul 1787** (007_0478 and 0479, at the foot of the pages): `* 1196. 1084?. 758. 861.
   1307. 626` and `† 265`. † 265 = Congress, confirmed (TJ wrote "Congress" over 265 in Carmichael 26 Jan 1789; the
   "?65 = Congress" of Barclay 1786). * has six groups, not the five the editors' "The Pro[cu]re[ur]" implies: 1196 = the,
   861 = e, 1307 = r (TJ's decodings), so "The [1084][758] e r [626]", most likely "The Pro-cur-e-r [General]", the
   Procureur général Dudon. 1084, 758, 626 occur nowhere else.
3. **TJ → Adams, 28 Sep 1787**: the LoC press copy is blotted past reading (about 30 groups). The editors decoded the
   RC at MHi (Adams Papers), not seen here.
4. **TJ → Carmichael, 25 Dec 1788**: "our Kentuck[ians]" = 457.980.913.537.814; 537 = u (TJ's decoding, "U-lloa"),
   so the editors' [ians] on 537.814 is a wrong split: Ke-nt-u-[814], with 814 unattested (ck, cky or ckians).
   "It mer[its] your in[vestig]ation": 904, 1581, 1438 unattested; 254 = -ation/-ed (1791 "demand-ed").
5. **TJ → Carmichael, 9 Aug 1789**: line 2 re-read: `1579. 1017. 1363. 1111. 1497. 1271. 402. 1169. 1107. 1363.
   1128. 1088. 31.` 1107 = t fits both "t-alk" and "Braban-t", so [tal]k is t + alk (9?? hidden by a paper flaw). 1111 =
   this (the first transcription had 1001). "their" is written 1569, which is "you" in Carmichael 8 May 1788 (TJ);
   1565 = their elsewhere: a slip of one digit by TJ or the copy.
6. **TJ → Carmichael, 15 Dec 1787**: the printed 40-group line has two misprints (group 12 is 519, not 515; group 15
   is 1097, not 1057). Its plaintext is the opening of TJ's 14 Jun 1787 letter (PrC 007_0489): groups 14-40 align as
   got back to Paris three days ago, I resume immediately the correspondence with which you have been pleased to;
   groups 1-4 are De-ar Si-r; groups 5-13 stand for the heading and "Having" and are not resolved one by one.

### Other findings

- 1360/1363: TJ told Carmichael that his copy wrote 1360 for 1363 (= is); the interlinears confirm 1363 = is.
- Carmichael's TJ-corrected numbers (1567→1527 sa, 1106→1006 fel, 806→600 sto, 1538→1338 on, 59→89 contrary,
  1552→1052 cap, 1396→1390 ne, 146→140 Sweden) are in the transcription notes.
- Short's copies: the State Department clerk wrote the decoding over the groups in Nos. 2 and 6 (9 and 28 Oct 1789);
  No. 5 (25 Oct) has none, and its reading is the editors'. No. 6 ("for the ransom of our prisoners", 581.623 /
  468.623.1043) is not among the Founders "Code No. 11" hits.
- TJ → Short, 6 Apr 1790, which the "Code No. 11" search also returns, is in Code No. 10 (editors' note), not 11.

## Read share over cipher words only (16 Nov 2026)

README Conventions count the read share over the words written in cipher, holes by words, sure words only. The
`texts/*_reading.txt` files hold the coded words alone (the clear text of each letter is not in them, except in
`tj_17870704`, where the clear sentences sit between the coded words and the coded words are listed in
`tj_17870704_decryption.txt`), so only that letter had to be separated. The old figures were counts of code groups
(`make_texts.py`: groups with a reading over groups counted); the new ones are counts of words, with `?` after a word or
alone (a doubtful or unread group), bracketed conjectural syllables (`[Bru]tes`), `[x?]` and the unread `[1531]`
groups as holes. Counted by hand, word fragments joined; `make_texts.py` was not rerun (it would rewrite the files).

| document | was | now | class |
|---|---|---|---|
| Barclay 10 Apr 1786 | 1.0 | 0.991 | read |
| Barclay's footnotes, ca. 3 Jul 1787 | 0.857 | 0.500 (2 of 4 words) | read in part |
| Jefferson to Barclay 4 Jul 1787 | 0.941 | 0.556 (5 of 9 cipher words: de x3, Montmorin x2 read; Rayneval x2, 495, trouble open) | read in part |
| Jefferson to Carmichael 25 Sep 1787 | 1.0 | 0.993 | read |
| Jefferson to Carmichael 15 Dec 1787, test line | 0.775 | 0.913 (21 of 23; the nine unread groups 5-13 are 2 words, an estimate) | read in part |
| Carmichael 8 May 1788 | 1.0 | 0.971 | read |
| Carmichael 29 May 1788 | 1.0 | 0.957 | read |
| Jefferson 3 Jun 1788 | 1.0 | 1.0 | read |
| Carmichael 5 Jun 1788 | 1.0 | **0.941** (16 of 17) | **read -> read in part** |
| Carmichael 24 Jul 1788 | 1.0 | **0.920** (23 of 25; the doubtful full stop, group 1609, is punctuation, not a word, and is not counted) | **read -> read in part** |
| Jefferson 25 Dec 1788 | 0.875 | 0.706 (12 of 17) | read in part |
| Carmichael 26 Jan 1789 | 1.0 | **0.926** (about 112 of 121) | **read -> read in part** |
| Jefferson 9 Aug 1789 | 1.0 | **0.765** (13 of 17; [beg]in, [Bru]tes, [Braban]t, com[motion] open) | **read -> read in part** |
| Short 9 Oct 1789 | 1.0 | 1.0 | read |
| Short 25 Oct 1789 | 1.0 | **0.943** (33 of 35; group 1612, Marquis twice, has no key value) | **read -> read in part** |
| Short 28 Oct 1789 | 1.0 | 1.0 | read |
| Jefferson 11 Apr 1791 | 1.0 | 1.0 | read |

The 28 Sep 1787 postscript to Adams stays decoded, not read (no transcription). Class of the target unchanged (read in
part). fraction_read 0.974 (groups) -> about 0.96 (words, estimated, the word count being approximate where the files
split words into syllables). Grade M groups (216, the editors' reading with no second occurrence) are not marked in the
files and are counted as read because they rest on the editors' printed decipherment (an external plaintext); the
shares would be lower if that reading were not accepted: a stricter reading of "sure words only" would lower the figures further and is for
the coordinator to decide. No measure declaration can be added: the files have no clear/cipher marks to declare (and
`v10_relabel.py` does not read a bare `?` as a hole), so the hand count above is the figure of record.

## Remaining gaps

- single unread or doubtful groups marked ? in Carmichael 5 Jun 1788, 24 Jul 1788, 26 Jan 1789 and Jefferson 25 Sep 1787, and the conjectural syllables of Jefferson 9 Aug 1789 ([beg], [Bru], [Braban], [motion]) - blocker: no-key-material; Jefferson's interlinear carries a ? for the group, or the group occurs once, and no other letter in this code fixes the value

- TJ to Adams, 28 Sep 1787, coded P.S. (about 30 groups) - blocker: illegible; the LoC press copy is blotted, the RC is at the Massachusetts Historical Society (Adams Papers) and was not seen
- Short to Jay, 25 Oct 1789 (No. 5), group 1612 for the Marquis (Lafayette), used twice - blocker: no-key-material; the State Department copy carries no decoding and no other letter has 1612
- TJ to Barclay 4 Jul 1787, groups 495 ([sea]), 223 ([trouble]), 1336 and 459 ([Rayneval]) - blocker: too-short; each occurs only here, and 495 contradicts the editors' word
- Barclay ca. 3 Jul 1787, groups 1084, 758, 626 (Pro-, -cur-, General?) - blocker: too-short; single occurrences
- TJ to Carmichael 25 Dec 1788, groups 814, 904, 1581, 1438; 9 Aug 1789 group 9?? - blocker: too-short; single occurrences, and 9?? is under a paper flaw (illegible)
- 15 Dec 1787 test line, groups 5-13 (heading and "Having") - blocker: too-short; the plaintext is known, the split among nine groups is not
- 47 groups of the 11 Apr 1791 PrC with blotted digits - blocker: illegible; the plaintext is fixed by the "decyphered" sheet

## Escalation

- [x] siblings: all 18 Founders "Code No. 11" documents and the 14 Jun 1787 letter collected; 15 transcribed from LoC images, Short's despatches from NARA M34 roll 2 (No. 6 of 28 Oct 1789, 'ransom ... prisoners', is a further coded passage the search had not listed); Barclay's undated letter found misfiled under 12 Jun 1787
- [x] clear-pages: TJ's clear-text sheets for 25 Sep 1787, 3 Jun 1788 and 11 Apr 1791 used; the 1791 "decyphered" sheet supplied 544 aligned groups
- [x] known-keys: Code No. 8 (Adams) and Code No. 10 (foreign affairs) are different codes (editors); Carmichael's Franks copy is Code No. 13; none applies
- [x] print: Founders Online (PTJ, Adams Papers), cryptiana and a general web search; no key table published
- [x] key-rebuild: key.tsv rebuilt from interlinears and clear sheets (348 values); segmentation solver tried and set aside (wrong seeds propagate); every conjectured group checked against all occurrences
- [x] retry: every bracketed group re-read on the images at 2x-4x (495, 1084/758/626, 1111, 1107, 537) and regraded

## Outcome

Method: key recovered based on adjacent plaintext (Jefferson's interlinear decodings and clear-text sheets in the same
files). Extent: partial (read in part): 97.4% of groups carry a reading, but the Adams P.S. is not legible here and
single-occurrence groups stay open. Prior solution: the Jefferson Papers editors' printed decodings (vols. 9-20,
1954-1982), found before the work and used for alignment. What this adds: the first value table of Code No. 11; the
transcription of 18 letters; corrections to four editorial readings (Barclay's footnote split; Kentuck[ians]; [tal]k;
the 15 Dec 1787 misprints) and the finding that [sea] (495) is contradicted by the code.
