# William H. Crawford to James Monroe, Paris, 15 Aug 1813 (Despatch No. 3, item 1): a coded letter in the JQA code

Status: in progress. Next step: compare with Brice Dudout's parallel reading (below; his pull request will carry his transcription), then a second reading of the groups read once and the retry step on Crawford's other coded runs.

**Date corrected 27 Oct 2026: 15 Aug 1813, not 3 Sept** (see "Date and Brice Dudout's parallel reading" below).
Contributed by WAINUT (27 Oct 2026). Read in part with the JQA code table (`../jqa/code_table.tsv`, applied
unchanged): 1,313 of 1,368 groups have a table value; about 40 context words are marked [?] and about 30 groups are
open (read_share 0.915). The site page and the ledger rows are left to the maintainer.

Catalogue 652. Contributed by WAINUT (https://github.com/WAINUTAI), a Dutch AI company; the work was done with AI
language-model agents.

## 1. The document

- **Source.** NARA RG 59, Despatches from US Ministers to France vol. 17, microfilm M34 roll 17
  ([naId 188672892](https://catalog.archives.gov/id/188672892)), frames 0027 (right leaf), 0028 and 0029 (both
  leaves), e.g. [frame 0028](https://catalog.archives.gov/medialz/dc-metro/rg-059/603720/M34/M34-017/M34-017-0028.jpg).
  The letter opens in code on 0027R. Words in clear are written in among the groups. A clear paragraph and the
  closing are on 0029L-R. The film shows no interlinear decipherment.
- **Same code, and Crawford says why.** The clear paragraph on 0029L-R: "Among the Papers of the Legation delivered me
  by Mr Thomas Barlow is a copy of a letter in Cypher from John Q. Adams esquire." The Duke of Bassano is spelt
  1278 1448 1576 1308 1068 352 (du-ke of bass-sa-no), five times.

## 2. The code and the key

The letter is in John Quincy Adams's St Petersburg code of 1811-1812 (the = 1385, of = 1576, that = 1384,
and = 668, I = 1401), whose table was rebuilt in [`../jqa`](../jqa/NOTES.md). This folder has no key of its own:
`profile.json` names `../jqa/code_table.tsv` as its key file, as other entries use a sibling folder's key
(`../feuquieres/grand_chiffre_1691.tsv`, `../balbases1677/key.json`). Nothing in `../jqa` is changed. Three more
letters in the same code have their own folders: [`../appleton1823`](../appleton1823/NOTES.md) (Cadiz 1823,
catalogue 637), [`../everett1825`](../everett1825/NOTES.md) (Madrid 1825, catalogue 638) and
[`../ellis1839`](../ellis1839/NOTES.md) (Mexico 1839, catalogue 653). With them, the code is seen in State
Department use from 1811 to 1839, at St Petersburg, Paris, Madrid and Mexico.

`decode.py` here calls the shared script `../appleton1823/decode.py` with this folder's files.

## 3. Transcription and decryption

- **Transcription** (`crawford1813_transcription.txt`): **1,368 groups** in 102 lines, read by eye from the
  full-resolution frames. About 150 groups (lines 27R01-04, 27R17-20, 28R06-09, 29R01-02, about 11%) were re-read
  independently on fresh crops. That check found one slip, now corrected: 29R01, ninth group, is 1383 (than), not
  1303. In this hand 8 is an o with a small top tick, so 0 and 8 have to be told apart by sense. About 89% of the
  groups were read once only. A review pass re-read the clear word in 28R02 on the full-resolution frame: it is "silly"
  (no f descender), not "folly", so the phrase is "the silly pub[li]cations of our sapient Editors".
- **Decryption** (`crawford1813_decryption.txt`, `python decode.py crawford1813_transcription.txt`):
  1,313 of 1,368 groups have a value in `../jqa/code_table.tsv`, applied without any change; 55 groups (38 numbers)
  have none. The raw output reads as English on every page, e.g. 27R12 "between the amer sian and the french govern
  ment at Paris", 28L24 "that i have been REPRESENTED as an im pe u ous and un ac", 29R01 "no more is commu ted in
  this country than what com port with the views of the emperor".

## 4. The reading

`crawford1813_reading.md`, read in part. Crawford explains why he has not opened the official correspondence. After
Bassano's letter from Dresden, Mr. Warden acts as the organ of communication at Paris. Crawford will not follow the
court to Dresden: a minister must follow a court only within its own dominions, and outside France he would lose his
immunities. He doubts Bassano's sincerity and points to the slow answer to his letter. He has been represented as
"an impetuous and unaccommodating man", he thinks through the American papers. The Russian mediation is unwelcome to
Napoleon, who will not let the French negotiation advance before the result at St Petersburg is known. The second
half deals with the "plan of indemnity" of the late minister Joel Barlow: a rumoured arrangement by which Paris
capitalists were to take the trade licences and pay 25 per cent in advance into the indemnity fund. Crawford calls
the contract useless now, because licensed imports have glutted the US market, and will use it only as evidence that
France admitted the principle of indemnity. The opening line (27R01) is a heading and is only partly read ("Paris,
... 3rd ... the Secretary of State. Sir, ...").

**Values read here against the table or without one** ([?] in the reading unless said otherwise):

- 1264 = **full stop** (table: gar, H, 1x). It stands 30 times, always at the end of a clause, while Crawford
  writes "and" as 668 throughout. In Ellis's despatch of 1839 ([`../ellis1839`](../ellis1839/NOTES.md)) the clear
  copy fixes 1264 as the full stop. A first reading of this letter had taken 1264 as "and"; the full stop fits every
  place. Not marked.
- 713 = **r** (table: port, M, 1x), as in the 1839 alignment: 1098 713 = "Sir" (27R02, after "the Secretary of
  State"); 601 713 499 545 = "Mr. Warden" (27R11; 499 ward and 545 en are table values). Warden matches the Madison
  editors' summary below. Not marked.
- 1009 1401 1366 = cap-i-tal, as in 1839 (1366 = tal there; table: take, M). Not marked.
- 449 = -nity/-nities (no value): im-mu-449 = immunities, in-dem-449 = indemnity (five times). Not marked.
- 1106 = will (table: pa, M, 1x): "these immunities will cease", "it will be proper". Not marked.
- 462 = -tract (con-462 = contract, 3x) and 1323_ = been (3x), not marked; 770 = -turn (re-770, 2x),
  400 = under (before the clear "stood"), 1450_ 1379 = latter, 130 = mine (de-ter-130^ = determined; "as fast as
  mine"), all marked [?].
- 1105 = accept (un-1105-able, [?]); 1105 700 occurs twice and gives no word that fits both places, so 700 stays
  open.
- Context words, each [?] in the reading: dated, Dresden, subjects, During, affect, sent, brought, return, former,
  who, independent, especially, allies, not, till, fast, has, disposed, whence, originated, here, charged, postpo-,
  no, claim, houses, and, constitu-, reconcile, correspondingly, date, tool, exchequer, it, whom I have, colonial,
  the plan, however, under, thousand, ret-, keep.

## 5. Controls (`python decode.py crawford1813_transcription.txt --controls`)

Function-word rate 0.36 for the true table; every group shifted by 1, 2, 3, 7, 50 or 100 either way gives 0.02-0.14;
three random permutations of the table give 0.03-0.05. An independent bigram check (share of adjacent word pairs in a
fixed list of common English bigrams; script not included) gave 0.117 for the true decode, 0.015-0.019 for three
shuffled group orders and 0.000-0.001 for shifted or permuted keys.

## 6. Prior work

Monroe to Madison, [ca. 1 Nov 1813] (*Papers of James Madison, Presidential Series* 7, pp. 11-12;
[Founders Madison/03-07-02-0011](https://founders.archives.gov/documents/Madison/03-07-02-0011)): a Crawford letter
"of the 4th of Sepr. in cypher", to be "decypherd as soon as possible"; the editors' note 1 identifies it as the
letter of 3 Sept, which is Despatch No. 4 (frame 0031), not this one (27 Oct 2026, below). Monroe to Madison, 12 Oct 1813 (PJM Pres. Ser. 6, pp. 691-692;
[Madison/03-06-02-0671](https://founders.archives.gov/documents/Madison/03-06-02-0671)), note 1: the coded letters
of 15 Aug and 3 Sept discussed the correspondence with Bassano, the proposed commercial treaty, the European war and
D. B. Warden's conduct. So a decipherment was ordered in 1813 and the editors summarise the content, but neither
page prints a deciphered text or names a decoded copy. Not checked: ASP Foreign Relations 3 (a search summary says
Monroe's report of 18 Jan 1814 printed the 15 Aug letter and an extract of 8 Sept, not this one), the Crawford
Papers, a decoded copy elsewhere in RG 59. As far as we checked, no full text of the coded letter has been printed.
In `profile.json` the prior solution is therefore "unpublished" (made in 1813, not found), not "no"; ASP FR 3 and the
Crawford Papers stay on the print list (escalation `print` open).

## Proposed table changes (for `../jqa/code_table.tsv`, not applied)

`../jqa/code_table.tsv` was used as it is. Proposals, with the evidence above: 1264 full stop instead of gar (1839
clear copy, 11x; this letter, 30x); 713 r (1839, and Sir / Mr. here) instead of port; 449 -nity (5x); 462 -tract
(3x); 1106 will instead of pa.

Queued as a `jqa` follow-up for the maintainer (not applied here). The most important is 1264 = full stop, attested
41 times (Crawford 1813 30x, Ellis 1839 11x, fixed by Ellis's clear copy), which conflicts with the table's grade-H
"gar".

## Date and Brice Dudout's parallel reading (27 Oct 2026)

**The letter is of 15 Aug 1813.** Checked on the frames in review:

- Frame 0005, "Extract from the Despatch Book of the American Legation at Paris": "Despatch No 3 - Sent to Mr
  Sherburne at Nantz Thursday 19th August - consisting of No 1 Letter from Minister to Secret.y of State Aug. 15th
  1813 in cypher - 2 Note of ditto to ditto same date - 3 Letter of ditto to ditto same date - Secret convention with
  the French Government in cypher - File of Moniteurs to the 19 August inclusive". The "No. 1" of the old title is
  the item number in this despatch.
- Frame 0027, right leaf: headed "No (3)" in clear above the first line of groups.
- Frame 0031: "Despatch No (4) Private, Paris 3d September 1813", with the decipherment written over the groups. That
  is the letter Monroe calls "of the 4th of Sepr. in cypher" (section 6), so the decipherment made in 1813 that the
  PJM note points to is No. 4's, not this letter's. The PJM note on the coded letters of 15 Aug and 3 Sept does
  cover this one.
- The heading groups are 1109 336 868 952 959 952 954 = Paris [15] Au[gust] 1813. Both transcriptions here read the
  second group of digits as 932 939 932 (the pattern of 1813 was Brice Dudout's reading); on frame 0027 they are 952 959
  952 954, and the key sheet M97 frame 1057 prints 951-960 = 0-9 (A. Beling, issue #203, checked 5 Nov 2026).
  `crawford1813_transcription.txt` (WAINUT's) was not changed: it still has 932 939 932, and 402 in 27R19 (482 on the
  frame) and 1106 in eight lines (28L04, 28L05, 28L17, 28L25, 28R04, 28R06, 28R09, 28R19; 1186 = will in the table, probably
  the same 8/0 slip) were not re-read there. Dudout's corrected
  transcription is `dudout/transcription.txt`. Section 4's "Paris, ... 3rd ..." took 954 at its table value "3rd (23rd)" (grade M).
  The ninth group is transcribed 1303 (back) here and 1503 (able, giving Hon-orable) by Dudout; not settled on the
  frame at the size viewed.

**Parallel reading.** Brice Dudout (Europe chiffrée,
`https://bdudout.github.io/europe-chiffree/en/documents.html#crawford-1813`) read the same letter on the same day,
independently, with the same table frozen before use: 1,371 groups, 1,330 read (97.0%; 87.9% without his readings
from sense), 41 marked unread. He validated the table first on No. 4's interlinear decipherment (194/226 and 224/246
values agree; shuffled-value controls at most 0.027/0.020). He also reads 1264 as a full stop and 1323 as been, and
says American State Papers, Foreign Relations III prints another letter of the same day, in clear (register item 3).
Spot checks: both readings have Crawford refusing to follow the court to Dresden, the "plan of indemnity" obtained
from the foreign ministry, Barlow's arrangement with capitalists and "the silly publications of our sapient Editors".
The two transcriptions differ in length by three groups; they have not been compared group by group. His values that
differ from the table are listed in `../jqa/overlay_dudout.tsv`. Catalogue 652 was removed on 27 Oct 2026 as read.

## Remaining gaps

- comparison with Brice Dudout's transcription and reading (1,371 groups against 1,368 here; group 9 of the heading) - blocker: not-attempted; his pull request will carry his files.
- about 40 context words marked [?] and the open groups ([102], [267], [343], [366], [529], [58], [104], [531], [665], [700], [909], [1204], [1313], [1444] and others) - blocker: open-codes; most occur once here. Crawford's other coded despatches in the same volume (frames 0031-0033, 0047-0049, 0065-0067, 0072, 0086-0090, 0199-0201, 0213-0214) are workable siblings, not yet transcribed, and the next source of occurrences.
- about 89% of the groups were read once only - blocker: not-attempted; a second full reading against the frames is workable and still to do.

## Escalation

- [x] siblings: read with the JQA table (`../jqa`); Ellis's 1839 values (1264, 713, 1366) used
- [x] clear-pages: the clear words and paragraphs of the letter used for the sense
- [x] known-keys: the JQA table applies directly (the = 1385, of = 1576)
- [ ] print: the Founders/PJM notes checked (summary only); ASP FR 3 not checked
- [x] key-rebuild: context values for 449, 462, 770, 1106, 1323, 130 checked at their occurrences
- [ ] retry: Crawford's other coded runs on M34 roll 17 not tried

## Files

- `crawford1813_transcription.txt`, `crawford1813_decryption.txt`, `crawford1813_reading.md`
- `decode.py`: runs `../appleton1823/decode.py` (which applies `../jqa/code_table.tsv`) on this folder's files;
  `--controls` runs the wrong-key controls (standard library)

## Independent reading by Brice Dudout (27 Oct 2026)

1,330 of 1,371 groups read with the jqa table and a graded overlay; the legation register dates this letter 15 August 1813 (despatch no. 3, sent 19 August), not 3 September. See `dudout/README.md`.
