# goslinga1730: Sicco van Goslinga to Reinhard van Reede-Ginkel, 1730 (catalogue 2534)

Gelders Archief (Arnhem), 0613 Familie Bentinck / Aldenburg Bentinck, inv. nr. 3889, 79 scans.
Permalink: https://proxy.archieven.nl/0/9F5C2770E8A342E0A4384AC604A46608 (viewer on www.archieven.nl).
Scans are not in this folder (screenshots kept locally only). Writer and addressee as given by the inventory and the
catalogue entry; the letter is addressed "A Monsieur de Ginkel".

## Documents

| doc | scans | state proposed | words |
|---|---|---|---|
| Compiègne, 23 July 1730, to "Monsieur de Ginkel" | 23, 24, 27 (slip on 25) | **read** | 78 cipher words: 29 spelled from letter groups verbatim, 46 word/name groups (values from the slip), 1 marked repair, 2 holes |
| Fontainebleau, May 1730 (scan 8) | 8 | **not read** | held-out test only (130 groups transcribed, first 16 lines) |

The July letter is written in French; its Dutch passages carry the code, with clear Dutch words between the code
groups. A loose slip in a second hand lies on the third page (scan 25; the same page without the slip is scan 27).
It gives all the coded Dutch passages in plain text, so it is a contemporary decipherment of this letter only.

## System

Numbers with a point after every group, set into clear Dutch.

- Groups up to about 160: single letters, several homophones per letter, no word division inside a coded stretch
  (e 19, 42, 56, 85, 92, 112, 139; o 37, 38, 49, 68, 76, 88, 98, 115; n 10, 58, 79, 105, 153; 91 = ij).
- Groups from about 200 to 970: words, in roughly alphabetical order (207 aen, 418 dat, 421 de, 433 dese, 457 dit,
  479 een, 491 en, 582 het, 623 ick, 639 in, 669 konnen, 697 maar, 729 met, 806 onse, 809 op, 814 over, 856 saken,
  866 seer, 881 sijnde, 888 soo, 937 tusschen, 947 van de, 958 veel). Common words have two groups (en 491/492, het
  582/585, dese 433/453).
- Groups with a caret over the last digit: names and titles (103^ and 109^ the Emperor, 253^ the King of Prussia,
  286^ the British minister, 292^ Seckendorff, 342^ the King of Great Britain, 697^ the King of France, 704^ the
  Keeper of the Seals, 744^ Spain, 914^ Sicily; also 12^ "werdt"). 697 without the caret is "maar", so the caret makes
  a separate group.

## Key source and key

`pairs.tsv` pairs every one of the 253 code groups of the letter, in order, with the slip (`gloss_slip_scan25.txt`);
`scripts/build_key.py` checks that the pairs cover the transcription group for group and builds `key.tsv` /
`key_frozen.tsv`: 107 entries, one per group (66 letter groups, 41 word/name groups), no conflicts. The letter has
253 code-group occurrences of 109 distinct groups: the 107 of the key and the two holes 158 and 478. Where the slip
and the groups spell a word differently the pair notes it (volkomen / volkomene, onderrigten / onderighten); the
slip spells group 253^ "de Coning van Pruyssen" once and "de Coning van Pruysse" once, and the key keeps the first
spelling.

## Held-out tests

1. **Split test inside the letter** (`scripts/build_key.py`): key built from the pairs up to "verdwinen" (part A)
   and applied to the last paragraph (part B, from "De 704^ verhaalde", 63 groups, 23 words). Of the 38 part-B
   groups that the part-A key knows, 38 agree with the slip, 0 wrong; 25 part-B groups are not in the part-A key;
   4 of 23 words are fully given by it. (Before the 253^ correction below these figures were 37, 26 and 3.) This confirms the letter groups; the word groups of part B are mostly
   new and rest on the slip.
2. **Cross-letter test on the May 1730 page** (scan 8, no slip; `heldout_fontainebleau1730_*`): the frozen key gives
   no Dutch from the letter groups ("hswlls", "gtsmb", "ixe?f?ij"). The 130 code-group occurrences are 96 distinct
   groups. 46 of the 82 low-group occurrences (23 of 50 distinct low groups) are in the key but give nonsense, so
   the May letters use another letter table, or their low groups mean something else. Of the 48 high or caret-group
   occurrences (46 distinct) 8 are in the key and a few fit the context (958 veel after "geoordeelt 418 [dat]", 744^ after
   "van", 201 and 203 for aen/aan in "yders 201 deel" and "morgen 203"), which suggests the word list may be shared.
   Not tested further. Result: the key does not read the May letter.

## Transcription

`SIGN_CONVENTIONS.md` was written before the key. Pass 1 from 1x crops, pass 2 from 2x half-line crops
(`scripts/stack.py`) plus a 4x look at two groups. 17 lines differed; each was settled on the image: 292 vs 292^
(caret seen), 91 vs 41 (the 4 of this hand), 5 vs 7, 34 vs 37, 21 vs 41 and ?6 vs 76 in "oorlog" (the second group
there is written over an erasure with 49 above it), 68 vs 66, 103 vs 105, 32 vs 34 (Engelandt), 805 vs 806. A first
set of screenshots had blurred tiles over part of each page and was not used.

Blind review (13 Nov 2026, an independent AI reader working from the images before opening the transcription):
60 code groups of six lines (23.1, 23.2, 23.3, 27.6, 27.9, 27.10/27.11) compared, 59 agree. The one difference is a
caret over 253 in 23.1 ("aan 253^ heeft"), which both passes had missed; it is corrected in
`transcription_goslinga1730.txt` (the pass files are left as they were). The key therefore no longer holds 253 and
253^ as two groups for the King of Prussia.

## Reading

`scripts/check_marks.py` rebuilds `decryption_goslinga1730.txt` from the transcription and the frozen key, runs
`scripts/reading.py check` on `reading_goslinga1730_marked.md` (every departure marked) and re-runs the key build. It
passes. Counts: 78 cipher words; 29 spelled verbatim from letter groups; 46 word or name groups (value from the slip
only); 1 marked repair (`{e/w}aer`: the first group of "waer" is 92, which is e in six other places); 2 holes (158,
in the left margin before "waer", and 478, before "volkomene"; the slip renders neither). 75 of 78 = 96.2% read from
the signs without repair.

Content: Seckendorff's information to the King of Prussia proved true; the Emperor's answer agrees with it and its
points follow in French; a plan of war and operations has been drawn up; if things are settled and carried out in
full harmony, the Emperor will in all likelihood listen to reason; but the jealousy between the Kings of France and
Great Britain, a British letter to Spain and another from "this court" (probably the French court, where the writer
is) about the expedition to Sicily may make all these measures go up in smoke; the Keeper of the Seals told of an
incident between the British minister and the King of Prussia; the writer asks the addressee to tell him whether it
is true.

Reading checker (`docs/_check_reading.py --file`, origin/main 65cdcd9d5, re-run 13 Nov 2026 after the corrections of
the blind review):

| file | clean share |
|---|---|
| reading_goslinga1730.md (whole file: English header, original spelling, modern spelling, notes) | 14/47 = 0.298 |
| original-spelling section alone | 0/11 = 0.0 |
| modern-spelling section alone | 5/11 = 0.455 |
| translation_goslinga1730.md | 22/23 = 0.957 |
| decryption_goslinga1730.txt (unspaced letter runs) | 1/18 = 0.056 |

The low Dutch scores come from the checker's Dutch word list (6,771 words), not from holes in the text. In the
modern-spelling section the only real holes are [#158] and [#478]; the other misses are ordinary Dutch words the
list does not hold (tussen, zo, informatie, conform, behelst, substantie, operatie, harmonie, gearresteerd,
waarschijnlijkheid, jaloezie, expeditie, heilzame, conferentie, voorval, belemmering, onderrichten). In the
original spelling it also misses the period forms (ick, seer, soo, dese, saken, konnen, sullen, waer, aen).

## Correction from the blind review

Group 12^ was first given as "nie werdt", which made the sentence on the Emperor negative ("if it is not settled").
On the slip, line 7 ends "volkomen eharmoo" and line 8 begins "nie werdt": "nie" is the end of "harmonie", split
over the line, and the letter groups before 12^ already spell "harmonie" in full (8 7 41 20 98 79 9 85). So 12^ =
"werdt", and the sentence is positive: "if it is [#478] settled and carried out in full harmony, the Emperor will
in all likelihood listen to reason". Corrected in `pairs.tsv`, the key, the decryption, both readings and the
translation; the word counts do not change.

## Prior art (checked 12 Nov 2026)

Two web searches (Goslinga, Compiègne 1730, Ginkel, Seckendorff, gecijferd, Middachten; Goslinga, Van Reede, 1730,
Soissons, edition, cipher). Found only the edition of the Slingelandt-Goslinga correspondence (W.A. van Rappard,
1978; another series) and general work on the Congress of Soissons (F. Dhondt). No edition or modern decipherment of
these letters. The vetting of 11 Nov 2026 found nothing in DECODE, Tomokiyo or Lasry. The slip in the folder is a
contemporary decipherment and was used as the crib; say so in any write-up. In this repository "Goslinga" also
occurs in `targets/geertruidenberg/decode/api_2796.json`, a DECODE record of a 1713 document addressed to Buys and
Goslinga: another document, not this folder.

## Remaining gaps

- Groups 158 and 478 of the July letter - blocker: open-codes; each occurs once and the slip renders neither.
- The word and name groups of the July letter - blocker: too-short; their values rest on the slip only, and none is
  confirmed by a second occurrence outside this letter.
- The May 1730 letters from Fontainebleau (scans 5/7, 8, 9, 11-13) - blocker: no-key-material; another letter
  table, not solved. A ciphertext-only attack on the low groups, helped by the shared word list, might work; not
  tried.
- Scans 30 and 40 - blocker: not-attempted; a number code in French in another style, not examined.
- The second decipherment slip on scan 69 (dateline read as 1 June 1733, uncertain) - blocker: not-attempted; its
  cipher letter was not found among the scans fetched, and it was not paired.
- The key Gelders Archief 0613 inv. 3973 ("Sleutel voor geheimschrift") - blocker: needs-physical-access; not
  scanned, not compared.
- A human check of the transcription - blocker: not-attempted; one blind review only (an AI reader, 60 code groups
  of six lines and the 8 sentences), no human palaeographer. The split test checks the letter table only, since
  part B is also on the slip.

## Escalation

- [x] siblings: the May 1730 page from Fontainebleau (scan 8) tested with the July key; its letter groups give no
  Dutch
- [x] clear-pages: the contemporary slip on scan 25 used as the crib for the July letter; the slip on scan 69 not
  paired
- [ ] known-keys: Gelders Archief 0613 inv. 3973 ("Sleutel voor geheimschrift") is not scanned; not seen
- [x] print: web searches (12 Nov 2026) and the catalogue vetting (DECODE, Tomokiyo, Lasry; 11 Nov 2026) found no
  edition or decipherment; the printed Slingelandt-Goslinga correspondence (Van Rappard 1978) is another series and
  was not seen
- [ ] key-rebuild: the May 1730 letter table not rebuilt (no ciphertext-only attack tried)
- [ ] retry: groups 158 and 478 not retried beyond the slip

## Image route

www.archieven.nl search (`miadt=37`, `micode=0613`, term `Goslinga`), open item 3889, click the first thumbnail, type
the scan number in the viewer frame, screenshot (`scripts/anl_view.py`, after Dan Bourdeau's
`research/sweep_2026-11-11_dutch_2/anl_view2.js`). Device scale 2 and a wait of 14-15 s per page are needed to get
sharp tiles. User-Agent WAINUT-research, one page at a time. No block met.

## Files

`SIGN_CONVENTIONS.md`, `transcription_goslinga1730_pass1.txt`, `..._pass2.txt`, `transcription_goslinga1730.txt`,
`gloss_slip_scan25.txt`, `pairs.tsv`, `key.tsv`, `key_frozen.tsv`, `decryption_goslinga1730.txt`,
`reading_goslinga1730.md`, `reading_goslinga1730_marked.md`, `translation_goslinga1730.md`,
`heldout_fontainebleau1730_transcription.txt`, `heldout_fontainebleau1730_decryption.txt`, `profile.json`,
`scripts/` (anl_view.py, crop.py, stack.py,
build_key.py, decrypt.py, reading.py, check_marks.py).
