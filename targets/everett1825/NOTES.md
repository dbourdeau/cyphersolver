# Alexander H. Everett to Henry Clay, Madrid, 25 Sep 1825: six coded passages in the State Department code

Status: written up 24 Nov 2026 (`docs/everett1825.html`).

State on 24 Nov 2026 (the section "24 Nov 2026: the claims review applied" at the end is the latest word where it
differs from the older sections). The State Department's clerk deciphered all six coded parts at the time (frames
0110-0111, found by Andrew Beling on 22 Nov 2026); that is the first decipherment. All six parts, 1,201 groups, are
read here with the State Department code sheet (NARA M97 roll 13 frames 1056-1057, Weber's WE028;
`key_we028_everett1825.tsv`): 844 cipher words, 26 holes, 818 read, 0.969. Class: read. Method: "read with known
key", for the whole (the part split of 23 Nov 2026 was withdrawn on 24 Nov: see the last section). MS pp. 14-18
248 of 257 words (0.965), MS pp. 1-6 570 of 587 (0.971). The reading of record is
`everett1825_collated_reading.md`. No person has checked a reading against the film.

The first contribution (27 Oct 2026), by WAINUT: read in part with the JQA code table (`../jqa/code_table.tsv`,
applied unchanged): 347 of 355 groups have a table value; 8 groups are open and some words rest on context only.
Sections 1 to 6 below are its record; its title was "three coded passages in the JQA code".

Catalogue 638. Contributed by WAINUT (https://github.com/WAINUTAI), a Dutch AI company; the work was done with AI
language-model agents, and every group was checked against the NARA frames twice, the second time independently.

## 1. The document

- **Source.** NARA RG 59, Despatches from US Ministers to Spain vol. 25, microfilm M31 reel 27
  ([naId 188610348](https://catalog.archives.gov/id/188610348)), enclosure "Notes of a Conversation of Mr. Everett
  with Mr. Zea" (Francisco Zea Bermúdez, the foreign minister). The cipher is on frames 0119 (MS pp. 14-15,
  [frame](https://catalog.archives.gov/medialz/dc-metro/rg-059/603720/M31/M31-027/M31-027-0119.jpg)), 0120 (right
  page, MS p. 17, after "End",
  [frame](https://catalog.archives.gov/medialz/dc-metro/rg-059/603720/M31/M31-027/M31-027-0120.jpg)) and 0121 (left
  page, MS p. 18, [frame](https://catalog.archives.gov/medialz/dc-metro/rg-059/603720/M31/M31-027/M31-027-0121.jpg)).
- **What Manning has.** Manning III doc. 1134, p. 2062 (the OCR of the page header reads "2002"), is headed
  "[extract]" and prints only passage A, as "[Here follow six lines in cipher, without decodification.]", after
  "...an interference of Providence." His extract ends at "in reply to his remarks."; passages B and C, after "End",
  are neither printed nor mentioned.

## 2. The code and the key

The passages are in John Quincy Adams's St Petersburg code of 1811-1812 (the = 1385, of = 1576, that = 1384,
and = 668, I = 1401), whose table was rebuilt in [`../jqa`](../jqa/NOTES.md). This folder has no key of its own:
`profile.json` names `../jqa/code_table.tsv` as its key file, as other entries use a sibling folder's key
(`../feuquieres/grand_chiffre_1691.tsv`, `../balbases1677/key.json`). Nothing in `../jqa` is changed. Three more
letters in the same code have their own folders: [`../crawford1813`](../crawford1813/NOTES.md) (Paris 1813,
catalogue 652), [`../appleton1823`](../appleton1823/NOTES.md) (Cadiz 1823, catalogue 637) and
[`../ellis1839`](../ellis1839/NOTES.md) (Mexico 1839, catalogue 653). The code was evidently still in use at the
Madrid legation in 1823-1825.

`decode.py` here calls the shared script `../appleton1823/decode.py` with this folder's files.

## 3. Transcription and decryption

- **Transcription** (`everett1825_transcription.txt`): **355 groups** in three passages (A 8 lines, B 14,
  C 12). These are the coded passages of MS pp. 14-18 only. The catalogue counts "about 445 groups" from frame 0114;
  a check of frames 0112-0118 made after the review shows why: the same Notes (endorsed as the duplicate sent with
  despatch No. 7 of 25 Sept 1825) carry further coded passages on MS pp. 1-6 (frames 0112-0115): short runs on
  pp. 1-3, pp. 4-5 wholly in code, and nine coded lines opening p. 6; about 80 lines, very roughly 900 groups.
  Pp. 7-13 (frames 0115-0118) are clear. Those passages are not in this file: they are transcribed in `dudout/texts`
  and in `beling/transcription_six_sections.txt`. A pencil "Decyphered" at the foot of p. 4 suggests the Department
  deciphered them; the decipherment was found on 22 Nov 2026 on frames 0110-0111 (section of 22 Nov below). There is
  no interlinear decipherment on pp. 14-18. Marks: a lozenge after a group = -s (plural or possessive), like the superscript o in `../jqa`; a caret
  after it = -ed; a cross under 1535 = all (al, all, als by the next letter, as in `../jqa`) and under 1167 = well; a
  tick under a group truncates it (108 comply -> compl in ac-compl-ish; 563 time -> tim in le-gi-tim-).
- **Decryption** (`everett1825_decryption.txt`, `python decode.py everett1825_transcription.txt`): 347 of 355 groups
  have a value in `../jqa/code_table.tsv`, applied without any change. The raw output already reads as English with
  syllables to join.

## 4. The reading

`everett1825_reading.md`. Everett did not argue at length with Zea, being satisfied that his remarks did not express
his real sentiments but were "merely a language imposed upon him at present by particular circumstances" (A). The
foreign ministers at Madrid agree: they think Zea privately well disposed to recognition of the new American states,
so "there is a strong power somewhere acting in a [125] direction". Zea dare not risk his place, since a declaration
for recognition would give his rivals the means to overthrow him, and he may think it good policy to dissemble
(B-C). The influence of the Emperor Alexander is said to be directed against recognition. Everett has not yet spoken
with the Russian minister, d'Oubril. Some ministers ascribe Russia's policy to a [258] of opposition to England
rather than to the regard for legitimacy that the Emperor gives as his ostensible motive (C). The rivals are not
named in the cipher. Pierre d'Oubril was the Russian minister at Madrid in 1825.

**Values read against the table or from context** (marked [?] in the reading unless said otherwise):

- 666 = Zea [?] (twice, "Mr. Z[ea]" and "Mr. Z[ea]'s"). The table has March (M, 1x). With the tick, March cannot
  give Zea, so either the table value or the reading is wrong.
- 601 = Mr. (three times, each before a name). The table has (sympt)oms (M, 1x). Not marked, since it holds at
  every occurrence.
- 70: necessary in A (the table's second value). In B, "well [850^] to the [70] of recognition" fits neither
  commerce nor necessary: read [?cause].
- 1072 = satis- (twice: "well satisfied", "if he is satisfied") against the table's see (M, 1x). Not marked.
- Context words: [?enter] (1293 tent), [?pretty] (211, no value, + 776 ty), [?tenor] (only 908 or is written),
  [?language] (1501 a 1454 ri 1238 gu 1524 age), [?imposed] (1424 im 1155^ port), [?expressed] (297 ex 520 ed,
  followed by 1504 observed), [?disposed] (850^, no value), [?shewing] (1094 she 1184 wi 483 new),
  [?liberality] (880 li 1325 bers 1543 against), [?head] (171 hea), [?enable] (only 545 en before "them"),
  [?overthrow] (929 over 557 those/ough), [?dissemble] (845 dis 541 insure), [?sacred] (1068 sa 1055 policy),
  [?d'Oubril] (809 de 926 ou 1354 1421 ill), [?legitimacy] (1512, no value), [?ostensible] (917, no value).
- Second values of the table confirmed here: 257 = speci (more e-speci-ally), 1525 = al (person-al), 1599 = ood
  (under-st-ood), 727 = rather (rather than), 1201 = g (re-co-g-ni-tion); 1479 riv (grade I) fits riv-al-s.
- 450 (ink, M) follows "think" both times and is left out of the reading as redundant.
- Line C10 "1290 727 1383" is written over; legible as read, but heavier.

**Open groups:** 125, 126, 211, 258, 850, 917, 1354, 1512 (no value in the table). The reading suggests contrary,
express, pret-, spirit, dispos-, os-, br, acy, all from context only.

## 5. Controls (`python decode.py everett1825_transcription.txt --controls`)

The true decode has a function-word rate of 0.37; every group shifted by 1, 2, 3, 7, 50 or 100 either way gives
0.02-0.12, three random table permutations 0.03-0.05. Shuffling the order keeps the same words, so it needs a
word-order model: an independent check with a character-trigram model trained on the English of Manning vol. III
(doc. 1134 left out) scored the true decode -2.129, wrong keys -2.50 to -2.70, and 200 shuffled orders mean -2.399,
best -2.351. That check needs Manning's text from archive.org and is not included.

## 6. Prior work

Manning prints passage A undecoded and omits B and C. The plaintext phrases do not occur in Manning vol. III. One
web search found no decipherment. Not checked: a decipherment on another copy, in a separate State Department file,
or in the Clay Papers.

## Proposed table changes (for `../jqa/code_table.tsv`, not applied)

`../jqa/code_table.tsv` was used as it is. Proposals, with the evidence above: 601 Mr. (3x) instead of (sympt)oms;
666 Zea [?] instead of March; 1072 satis (2x) instead of see. Second values confirmed in 1825: 70 necessary,
257 speci, 1525 al, 1599 ood, 727 rather.

Queued as a `jqa` follow-up for the maintainer (not applied here). The most important is 1264 = full stop, attested
41 times (Crawford 1813 30x, Ellis 1839 11x, fixed by Ellis's clear copy), which conflicts with the table's grade-H
"gar".

## Brice Dudout's parallel reading (27 Oct 2026)

Brice Dudout (Europe chiffrée, `https://bdudout.github.io/europe-chiffree/en/documents.html#everett-1825`) read the
same Notes on the same day, independently, with the same table frozen before use. Before reading he checked the table
on Everett's despatch of 8 Sept 1825 (frames 0061-0064) against the Department's decoding printed by Manning
(doc. 1133): 288 of 304 groups agree (0.947; permuted-value control p99 0.023). His reading covers all the cipher:

- the six lines on p. 15: 74 groups, 72 read; 126 read {convey} from its place in the block;
- pp. 1-6 and 17-18: 1,127 groups, 1,111 read (0.986; 0.929 without his readings from sense), 16 open. Pp. 1-6 hold
  how Zea entered the government and removed Ugarte ("a creature of Russia", sent on a mission to {Tur}in, a probable reading), and a
  portrait of the minister; pp. 17-18 the reasons for his refusal.

He applies an overlay of Everett's own values, each recurring in independent contexts: 727 rather (x3), 1201 g (x5),
557 thro (x2), 948 Russia (x4). They are listed in `../jqa/overlay_dudout.tsv`; 126 convey is added to the table as
grade I. He notes the pencil glosses: "Decyphered" at the foot of p. 4, and five words in another hand on p. 5.
Spot check of passage A: where the reading here marks "[?language] [?imposed]" as context words, his gives the same
sentence, "a language imposed upon him at present by particular circumstances". The two readings have not been
compared group by group. Catalogue 638 was removed on 27 Oct 2026 as read.

## Remaining gaps

Rewritten 24 Nov 2026 after the code sheet was applied, and again after the claims review the same day. The eight
groups without a value (125, 126, 211, 258, 850, 917, 1354, 1512) and the context-only words of the first reading are
no longer gaps: the sheet gives all of them. What is left is 26 words of 844, each listed with its groups in
`everett1825_collated_holes.md`.

- 20 words where the cipher as written does not give the word: a wrong group ([many], [of], [great], [are], th[at], [seems], ver[s]ed, leve[l], liber[al]ism, shewi[ng], refine[d]), a figure left out (ey[es], tal[ents]) or a syllable or ending with no group ([ten]or, necess[ity], act[ing], en[able], Russia[n], spi[rit], Minister[s]) - blocker: no-key-material; the key has a value for every one of these groups and the value is not the word, so no key can supply them. The frames show the groups as transcribed. The copy on the reel is endorsed as the duplicate; another copy of the Notes, which might have the groups right, was not looked for on the reel or elsewhere. The State Department clerk has the word, or a correction to it, at 21 of the 26 holes.
- two words with no group at all, [under] (MS p. 5) and [is] (MS p. 18) - blocker: no-key-material; supplied from the sense, nothing is written for them
- [than], MS p. 18, 121L.10 fourth group, 1383 or 1388 - blocker: illegible; the last digit is written over and heavily inked on the film, two blind AI readers read 8, two of three transcribers and the clerk read 3 (than)
- [the], MS p. 5, 114R.03 sixth group, 1385 or 1345 - blocker: illegible; the third digit is blotted on the film, the blind film check was split, 1345 is boa; Dudout and the clerk have 1385 "the"; a whole-word group, so it is a hole like [than] (claims review, 24 Nov 2026)
- ind[u]strious (MS p. 5, 114R.14, 800 dous) and des{+cri}b[i]ng (MS p. 5, 114R.17, 1359 bring) - blocker: no-key-material; the tick stands under the first 0 of 800 and under the 3 of 1359, which by the printed rule withdraw u and i (dos, brng), where the words want o and r withdrawn; the key gives the letters for the marks as they stand, and no key can supply the other letter (claims review, 24 Nov 2026; an AI model's look at frame 0114, not blind)

## Transcription doubts

Checked 24 Nov 2026 on the NARA catalog JPEGs of frames 0112-0115 and 0119-0121, each place enlarged with no
overlay, by an AI agent that knew the candidates (not blind; no person has looked). "Film check" is Andrew
Beling's blind check of 22 Nov 2026 (`beling/film_check/`, two AI readers); "sheet" is the code sheet; "clerk" the
State Department's decipherment. Loci are those of `everett1825_collated_transcription.txt`.

- 628 (112R.04, sixth group; Dudout 623) - read: 628; checked: image, decode, transcription; the last digit has two closed lobes like the 8 of 182, the 3s of 233 are open; film check 628; sheet 628 me, 623 mat; clerk "to me"
- 458 (112R.05, tenth group; Dudout 433) - read: 458; checked: image, decode, transcription; middle digit a small 5 without its flag, last digit an 8 as in 182 beside it; film check 458; sheet 458 ve; clerk "believe"
- 845 (112R.06, eighth group; Dudout 843) - read: 845; checked: image, decode, transcription; first digit with a closed upper loop (3 or 8 on the film), last digit a 5 with its flag; sheet 845 dis, 345 first; clerk "dissimulation"
- 1081 (113L.03, ninth group; Dudout 1031) - read: 1081; checked: image, decode, transcription; third digit closed above and below; film check 1081 by both readers; sheet 1081 self, 1031 city; clerk "himself"
- 1564 (113R.05, sixth group; Dudout 1364) - read: 1564; checked: image, decode, transcription; second digit with a flat top and a faint flag; film check 1564 (one reader); sheet 1564 observe, 1364 tain; clerk "as I observe"
- 880 (115L.07, seventh group; Dudout 330) - read: 880; checked: image, decode, transcription; second digit an 8, first digit 3 or 8 on the film and the same shape as the first digit of the 880 of li-ber-alty on 120R.11; sheet 880 li, 380 sti, 330 fi; clerk "inclined"
- 1057? (114R.17, first group; Dudout 1057, Beling 1257) - read: 1057 or 1257, not settled; checked: image, decode, transcription; second digit a closed oval with an exit stroke; film check 1257 by both readers with that digit unsure; three ticks under the group; sheet 1057 crisis less three letters gives cri (des-cri-bing), 1257 hath does not; clerk "describing". The word is read either way under the one-digit rule; the group keeps its mark
- 1383? (121L.10, fourth group; WAINUT 1383?, Dudout 1383, Beling 1388) - read: 1383 or 1388, not settled; checked: image, decode, transcription; written over and heavily inked, as are 1290 and 727 before it; film check 1388 by both readers; sheet 1383 than, 1388 then; clerk "than". Kept with its mark and counted as a hole
- 1385 (114R.03, sixth group; Dudout 1385, Beling 1345) - read: 1385 or 1345, not settled; checked: image, decode, transcription; third digit blotted on a dotted line, film check split (1385, 1345); sheet 1385 the, 1345 boa; clerk "the correct"; the claims reviewer's look (24 Nov 2026, AI, not blind) finds the digit like the A-shaped 4 of 1046 beside it and leans 1345. The collated transcription keeps 1385; since the claims review the word is counted as a hole, [the], like [than]
- 1203 (113R.03, ninth group; Beling 1205) - read: 1203; checked: image, decode, transcription; clear on the frame; sheet gal, where the sense wants 1233 great: a slip of the writer, counted as a hole
- 634 and 27 (114L.01, seventh and eighth groups; Beling 684) - read: 27 and 634; checked: image, decode, transcription; both clear; sheet love and mem where the sense wants 271 es and 684 are: slips of the writer, holes
- 1593 (113L.01, fifth group) - read: 1593; checked: image, decode, transcription; clear; the clerk decoded it "once"; one digit from 1573 od: read under the one-digit rule
- 1601 (114R.15, third group) - read: 1601; checked: image, decode, transcription; a tall 6, in all three transcriptions; the sheet ends at 1600; one digit from 1001 C (publi-c): read under the one-digit rule
- 1525 (120R.04, fifth group) - read: 1525; checked: image, decode, transcription; clear; the clerk decoded it "agent"; one digit from 1535 al (person-al): read under the one-digit rule
- 797 (115L.07, second group) - read: 797; checked: image, decode, transcription; clear; the clerk decoded it "done"; one digit from 767 tune (for-tune): read under the one-digit rule
- 1083 with its mark (114R.01, fourth group) - read: 1083, a short upright stroke under it and a lozenge after it; checked: image, decode, transcription; the last digit is not a 2; sheet sen, where "seems" wants 1082 sem with the cross: a hole. The collated transcription writes the group 1083+<>, its notation having no sign for a bare stroke (MARKS in `we028.py`: a cross whose cross-bar is not visible); Beling has a stroke, Dudout a cross. A hole either way
- the tick under 1359 (114R.17, second group) and under 800 (114R.14, second group) - read: under the 3 of 1359 and under the first 0 of 800; checked: image, decode; looked at in the claims review of 24 Nov 2026 by an AI model that knew the candidates (crops of frame 0114), and the crops seen again when the fixes were applied; by the printed rule they withdraw i (brng) and u (dos), where describing and industrious want r and o: both words are holes. The marks under 769, 256, 457, 982 and 1086 stand where the rule needs them; the other marks were not measured
- 1228 (121L.02, third group) - read: 1228; checked: image, decode, transcription; the same shape as the 1228 of "teeth are good" (113R.11) and "good fortune" (115L.06), unlike the 3 of 1327 and 1392; the clerk has "best" (1328), which is his misreading; all three transcriptions have 1228
- the mark under 108 (121L.01), under 850 (120R.06) and beside 569 (115L.04) - read: a tick; a long stroke under the last figure with a caret after the group; no mark under the group; checked: image, decode, transcription; see MARKS in `we028.py`
- the other 18 groups where Beling's transcription differs from Dudout's, and the three runs - read: Dudout's digits; checked: image, decode, transcription; film check of 22 Nov (16 of the 27 by one blind reader); the lines 113L.04, 113R.01, 114L.01, 114L.20, 114R.03, 114R.15, 114R.20, 115L.01, 115L.02 and 121L.07 were also looked at here on 24 Nov as whole lines at reduced scale, and nothing on them goes against Dudout's digits

## Escalation

- [x] siblings: read with the JQA table (`../jqa`); the same code as `../morris1813` (reversed blocks), `../crawford1813`, `../appleton1823`, `../ellis1839`
- [x] clear-pages: the clear text around each passage used for the sense; Manning's extract checked; the State Department's decipherment of all six parts found on frames 0110-0111 (Andrew Beling, 22 Nov 2026)
- [x] known-keys: the JQA table applies directly (the = 1385, of = 1576); the State Department code sheet (M97 roll 13) applied to every group on 24 Nov 2026: it has a value for all eight groups the table lacked
- [x] print: Manning III doc. 1134 prints passage A undecoded
- [x] key-rebuild: context values checked at their occurrences; second table values confirmed; superseded on 24 Nov 2026 by the code sheet, which needs no rebuilt value
- [x] retry (24 Nov 2026): every open group and every word given from sense or from the alphabetical slot in the earlier readings decoded again with the code sheet and its printed rules for the marks, and regraded: 821 of 844 words read, 23 holes; after the claims review the same day 818 of 844, 26 holes (last section). The other Everett despatches on the reel were not needed for values and were not searched

## Files

- `everett1825_transcription.txt`, `everett1825_decryption.txt`, `everett1825_reading.md`
- `decode.py`: runs `../appleton1823/decode.py` (which applies `../jqa/code_table.tsv`) on this folder's files;
  `--controls` runs the wrong-key controls (standard library)

## The eight enciphered pages read by Brice Dudout (27-28 Oct 2026)

Frames 0112-0115 (pp. 1-6) and pp. 17-18: 1111 of 1127 groups read with the jqa table and a graded overlay. See `dudout/README.md`. This answers the "next step" above.

## 14 Nov 2026: reading review recorded

All nine `outcome.texts` entries were read as sentences against their decryptions (Claude, session of 14 Nov 2026) and a
`reading_review` grade A recorded on each in `profile.json`:

- `everett1825_reading.md` (passages A, B, C): coherent, holes marked; read in part, read_share 0.904, unchanged.
- `dudout/texts/p01`-`p06`, `p17`, `p18` `_reading.md`: the deciphered passages run on from the clear text as coherent
  sentences. Word-level `read_share` measured on the passages in «guillemets», a word with an unresolved group ‹n› being
  a hole: p. 1 1.0 (59 words), p. 2 1.0 (36), p. 3 0.969 (96), p. 4 0.969 (162), p. 5 0.988 (173), p. 6 0.958 (72),
  p. 17 0.991 (113), p. 18 1.0 (92). If the words given whole from sense ([x], overlay grade S: many, me, I, of, Russia,
  soon, above, enable, is, Russian) are counted as holes too, pp. 1, 2, 3 and 6 come to 0.949, 0.917, 0.948 and 0.944,
  just under the 95% bar; the state was left `read` because those values rest on a group, most with a slot or a repeat
  (overlay.tsv). Both figures are in each entry's `note`.

Not done: the two readings of pp. 17-18 still differ in two places (WAINUT `[?cause]` and `[125]`, Dudout `{measure}`
and `{contrary}`); the comparison in Remaining gaps stays open. No reading file was changed; frames not re-opened.

## 14 Nov 2026: pp. 1, 2, 3 and 6 of Brice Dudout's reading set to read in part

The reading review of today recorded two word counts for his eight pages: one counting only words with an unresolved
group as holes, one counting also the words given whole from sense. The second is the one the read bar means (a value
proposed from context alone is not a word read, REREAD_BRIEF "The iterative loop"). By it pp. 1, 2, 3 and 6 are under
95% (0.949, 0.917, 0.948, 0.944) and are now `read in part` in `outcome.texts`; pp. 4, 5, 17 and 18 stay `read`
(0.969, 0.988, 0.973, 0.967). The sense-only words were not checked group by group on the film here, apart from the
overlay rows for "me", "soon" and "of". The target's class was and stays read in part.

## 22 Nov 2026: the period decipherment, and the group-by-group comparison (Andrew Beling, `beling/`)

A verification and a source find, not a new reading; details and files in `beling/README.md`.

- The State Department's decipherment of all six coded parts is on the same reel: M31 roll 27 frame 0110 (right page,
  parts 1-4) and 0111 (both pages, parts 4-6; parts 5 and 6 marked "14 & 15" and "17 & 18"). Writer and date unknown.
  Transcription: `beling/period_decipherment.txt`. It reads as both readings here do, and settles the two places
  where they differ: 70 = necessary with "ity" written above ("the necessity of recognition"), 125 = contrary.
- All eight open groups have values on the State Department code sheet already in the repository
  (`../morris1813/beling/key/codebook_M97_13_transcription.csv`): 125 contrary, 126 convey, 211 pret, 258 spi,
  850 dispose, 917 os, 1354 br, 1512 acy (the values Dudout proposed).
- Three transcriptions compared (`beling/scripts/compare.py`): with Dudout's files 1,113 groups in both, 1,086 agree,
  27 differ; with WAINUT's passage A 74 of 74, B and C 278 of 281. Dudout's p. 18 files leave out one code line
  (`1440 1082+D 569 1310 1541 480 262 1599 1384 1385`, "it seems to be also understood that the"), which his
  reading has.
- The 27 differing groups were read blind on the film by an AI model reader with no candidates given; the 11 it was
  unsure of went to a second blind reader that saw the whole line (model readings, not a person's). Dudout's digit
  at 18, Beling's at 8, 1 undecided (p. 5 line 3, 1385 or 1345). Of the 8: at 628, 458, 845, 1081, 1564 and 880
  Dudout has the word from sense or open and the group gives it from the key; at 1257 ("hath"; "describing" wants
  cri, which 1057 does not give either) and 1388 ("then" for 1383 "than", a whole-word group, outside the one-digit
  rule) the group on the film does not give the word. No word of either reading changes; the transcription files
  were not edited.
- Of the 8, 628 and 1564 rest on one model reader; at 845 and 880 the first digit is ambiguous (reader 1 gave 345
  and 380, reader 2 845 and 880, each with the other as alternative), though Dudout's 843 and 330 are excluded
  either way. 16 of the 27 groups rest on one reader.
- The transcription of the period decipherment (`beling/period_decipherment.txt`) has one reader; no second
  reader has checked it.
- Conditions of the images: the frames are NARA microfilm (RG 59, M31 roll 27) served by the National Archives
  Catalog. The Catalog record (naId 188610348) gives access and use as "Unrestricted", and NARA's notice says that
  materials produced by Federal agencies are generally in the public domain and may be reproduced without
  permission. No conditions came with the images and nothing was signed. Nobody at NARA was asked about AI
  readers; Andrew Beling decided to use the frames with them on this basis.

## 24 Nov 2026: integration of PR #900 (maintainers; owner's decision of 23 Nov 2026)

- **Two parts** (`outcome.parts` in `profile.json`). MS pp. 14-18 (passages A, B, C, catalogue 638) stay "read with
  known key": the JQA table applied unchanged. MS pp. 1-6 become their own part, "read from existing decipherment":
  the State Department's decipherment of those passages is on frames 0110-0111, parts 1-4. `outcome.method` stays
  "read with known key" as the primary part. The reading files of pp. 1-6 are Brice Dudout's, made with the table
  before the decipherment was found; none was changed.
- **The clerk's errors, noted.** The period decipherer worked from the key and corrected himself: 625 mation to
  many, 1593 once to understood, 1596 ongue to of, 1525 agent to personal, 483 until to -ing, 797 done to "Tune"
  (faint), 908 or with "Ton" above (`beling/README.md`). At these places he and Dudout agree against the key.
- **Readers.** The transcription of the period decipherment has one AI reader and no second reader; a few words are
  uncertain and some line ends of frame 0111 are lost at the binding. Our review opened frame 0111 and saw the
  decipherment there ("5 part", "6 part", "(ity)" over "necessary"); frame 0110, which carries parts 1-4, was not
  opened by us.
- **The gap `not-attempted` for pp. 1-6 is removed** from Remaining gaps and from `outcome.gaps`.
- **Crops removed.** The 39 crops of `beling/film_check/crops/` were taken out of the repository (Andrew Beling
  agreed). `beling/film_check/positions.tsv` and `readings.tsv` keep the pixel box of every place and the frame
  links, so each crop can be cut again from the NARA frame.
- **Eight value edits proposed, not applied.** The film check supports another digit than `dudout/texts` at eight
  places. No file under `dudout/texts` was edited, and `everett1825_transcription.txt` was not edited either.

  | Place (Dudout's file) | His group and value | Group the film check supports | Its value on the code sheet | Word | Support |
  |---|---|---|---|---|---|
  | p. 1 line 4, 7th | 623 `[me]` | 628 | me | to me | one model reader, sure |
  | p. 1 line 5, 10th | 433 `[ve]` | 458 | ve | believe | reader 1 unsure of the middle digit, reader 2 fairly sure |
  | p. 1 line 6, 8th | 843 `{di}` | 845 | dis | dissimulation | first digit ambiguous (345 or 845); 843 excluded either way |
  | p. 2 line 3, 9th | 1031 `[self]` | 1081 | self | himself | both readers 1081 |
  | p. 3 line 5, 6th | 1364, open | 1564 | observe | as I observe | one model reader, sure |
  | p. 5 line 17, 1st | 1057 `[cri]` | 1257 | hath | describing | both readers 1257, second digit not sure; neither group gives cri, so the word stays from sense |
  | p. 6 line 7, 7th | 330 `[li]` | 880 | li | inclined | first digit ambiguous (380 or 880); 330 excluded either way |
  | p. 18 line 9, 4th | 1383 than | 1388 | then | than | both readers 1388; a whole-word group, so the one-digit rule does not make it read |

  One more place is undecided (p. 5 line 3: 1385 or 1345; the sense and the period decipherment want 1385). The code
  line `1440 1082+D 569 1310 1541 480 262 1599 1384 1385` ("it seems to be also understood that the") is missing from
  his p. 18 transcription and decryption files, though his reading has the words; it is not restored here. If the
  edits are accepted after a person has looked at the film, six words move from "from sense" or open to "read from
  the key" (me, ve, dis, self, li, observe), pp. 1, 2, 3 and 6 are measured again and those pages are reviewed again.
- **Not done here:** no frame opened in this pass, no page re-measured, no reading_review added. There is no site
  page and no README results row for this target yet; both wait for the write-up.

## 24 Nov 2026: the code sheet applied, the readings compared, the recount (maintainers, later the same day)

The status line named three next steps. All three could be done from files in the repository and from the NARA
frames online, so they were done before any write-up. An AI agent did the work for the maintainers; no person has
looked at the film.

**The key is the State Department code sheet.** `../jqa` showed on 14 Nov 2026 that the table rebuilt there is the
code of the sheet at NARA M97 roll 13 frames 1056 (alphabetical) and 1057 (numerical), Weber's WE028, transcribed by
Andrew Beling in `../morris1813/beling/key/codebook_M97_13_transcription.csv`. The sheet had not been applied to
this target. `we028.py key` copies its value for each of the 444 different groups of the six parts into
`key_we028_everett1825.tsv`. Every group has a value except 1601, which is not a number of the sheet. Four rows
differ from the CSV and say so: 233 sim, 234 sin and 1093 shal, which the alphabetical sheet prints so (frame 1056
looked at: "sight 1100, sim 233, sin 234, since 235"; "shal 1093"; the CSV has sem, sen, shall), and 681 are, left
blank in the CSV because its two halves differ (numerical "are", alphabetical "arc"; too faint on frame 1056 to
settle here; `../jqa/code_table.tsv` has are, H). The eight groups the JQA table lacked are on the sheet:
125 contrary, 126 convey, 211 pret, 258 spi, 850 dispose, 917 os, 1354 br, 1512 acy.

**The sheet prints its rules for the marks.** Last column of the alphabetical sheet (frame 1056), below the
figures and the punctuation, read here on the frame:

> [lozenge] to a noun makes its gen. or plur. to a verb makes its 3. p. s. i. act. [caret] to a verb makes its
> part. pas. or imperf. indic. [cross] under the last figure doubles the last letter of those represented by that
> no. under the penult figure it doubles the penult letter: under the antepenult figure doubles the antepenult
> letter &c. [tick] under a figure withdraws the letter corresponding as in the last article. u. & v. are
> convertible always so are i. & j.

So the marks are part of the key, not an inference from use: 666 with a tick is zeal less a letter, Zea; 1178 with
two ticks whither less two, white; 1034 with two ticks claim less two, cli (dis-in-cli-nation); 1441 with two
ticks Italy less two, ity (ob-sc-ur-ity); 769 with two ticks Turkey less two, ture (ven-ture); 117 with three ticks
connexion less three, connex (connex-ed); 231 with a tick put less one, pt (ke-pt); 251 with a cross son, soon; 466
with a cross and a tick uge, ugg (str-ugg-ling); 850 with a stroke under its last figure and a caret, dispos-ed.
Every marked group of the six parts gives its word by these rules when the letter is taken from the word. The rule
ties the letter to the figure the mark stands under; the letter was taken here from the word, and the place of each
mark under its group was not measured. (Corrected by the claims review of the same day, last section: at 1359 and
800 the tick stands under another figure than the word needs, so all but those two marked groups come out by the
printed rules, and describing and industrious are holes.)
`../morris1813` and `../jqa` inferred the same rules from use and may cite the printed text; nothing in those
folders was changed.

**The three transcriptions collated.** `we028.py collate` writes `everett1825_collated_transcription.txt`, all six
parts, 1,201 groups, from Beling's, Dudout's and WAINUT's files; where they differ the group taken and the reason
are in the script (DECISIONS, RUNS, MARKS) and in "Transcription doubts" above. For the eight value edits proposed
on PR #900:

| Place | Proposed | Decision | Why |
|---|---|---|---|
| p. 1, 623 | 628 | applied | film check, sheet (628 me), clerk "to me", frame seen |
| p. 1, 433 | 458 | applied | film check, sheet (458 ve), clerk "believe", frame seen |
| p. 1, 843 | 845 | applied | last digit 5 on the film, sheet (845 dis), clerk "dissimulation", frame seen |
| p. 2, 1031 | 1081 | applied | both blind readers, sheet (1081 self), clerk "himself", frame seen |
| p. 3, 1364 | 1564 | applied | film check, sheet (1564 observe), clerk "as I observe", frame seen |
| p. 6, 330 | 880 | applied | second digit 8, sheet (880 li), clerk "inclined", frame seen |
| p. 5, 1057 | 1257 | not applied | the three ticks and the sheet want 1057 (crisis less three letters, cri); the digit is not settled on the frame; the group is written 1057? and the word is read either way under the one-digit rule |
| p. 18, 1383 | 1388 | not applied | written over; 1383? kept with its mark; the word is counted as a hole |

"Applied" means in the collated transcription. No file under `dudout/texts` was edited, nor
`everett1825_transcription.txt`, nor Beling's files: they stay as contributed. The place left undecided on PR #900
(p. 5 line 3) is 1385. The code line missing from Dudout's p. 18 files (121L.03) is in the collated file, from the
other two transcriptions; the frame has it.

**Frames looked at.** M31 roll 27 frames 0110-0115 and 0119-0121 and M97 roll 13 frame 1056 were fetched from the
National Archives Catalog (plain HTTPS, no bot check) and the places listed under "Transcription doubts" enlarged.
The frames are not committed. The look was not blind.

**The two readings compared, place by place.** Passage A is the same 74 groups in WAINUT's and Beling's files.
For pp. 17-18 WAINUT's passages B and C and Dudout's two pages have the same groups except the line Dudout's files
lack and the mark on 1383. The words differ in two places, and the sheet and the clerk settle both: 70 is
*necessary* (WAINUT [?cause], Dudout {measure}; the clerk wrote "ity" above it), 125 is *contrary* (WAINUT open,
Dudout {contrary}). WAINUT's context words against the sheet: 666 zeal with a tick, Zea (the JQA table's March was
wrong); 601 M; 1072 satis; 1293 ent (ent-er); 211 pret; 1454 lan; 1155 pose with the caret, imposed; 297 express;
850 dispose; 1543 alty; 171 head; 557 thro; 541 emble; 1055 cred; 1354 br (de-ou-br-il); 1512 acy; 917 os: all read
from the key. Three stay holes: [ten]or (only 908 or is written), shewi[ng] (483 until) and en[able] (only 545 en).
450 is nk on the sheet (thi-nk), not a redundant "ink". Most of Dudout's values from the alphabetical slot ({x})
are on the sheet as he gave them, or as a longer word that a tick shortens (850 dispose, 541 emble, 722 rare,
645 middle, 666 zeal, 285 evil, 481 United); at 70 the sheet has necessary, not measure, and at 1178 whither,
117 connexion, 1441 Italy, 769 Turkey, 519 ection, 705 que, 732 rea and 450 nk, where the word comes out the same by
the mark rules or with the next group. Of his values from sense ([x]) the sheet has most as he gave them or within
a letter: 1504 above, 297 express, 1201 G, 843 din, 251 son with the cross, 1419 ight, 246 sm, 993 frank, 1325 ber,
1423 ility, 244 sk, 1599 ood, 948 Russia, 257 speci, 709 qui, 401 N, 653 Y; 1552 oa, 882 like, 1346 bor, 170 hea,
1452 L, 1402 ia, 1001 C; 800 dous and 1359 bring with a tick. It does not give 625 many, 1596 of, 1407 s, 1401 l,
1355 al, 797 tune, 483 ng, 1525 al, 1593 ood or 545 enable, which are slips or omissions of the writer (holes, or
read under the one-digit rule). Of his 16 open groups the sheet reads 12: 79 nevertheless; 1564 (his 1364)
observe; 1343 501 blu-e; 520 457 864 ed-uc-ation; 1112 404 pass, name; 67 monarch; 1543 alty; 1366 tal. Four are
slips and stay holes: 1203, 27, 634, 129.

**One-digit rule (README Conventions, 14 Nov 2026).** The sheet is the surviving key of the period. Five words have
a group one digit from the one wanted, inside a word whose other groups are read from the key, with the group seen
on the frame: understo{+od} (1593 for 1573), publi{+c} (1601 for 1001), des{+cri}bing (1057 or 1257), for{+tune}
(797 for 767), person{+al} (1525 for 1535). They count as read. The rule does not cover the whole-word groups
(625 for 615 many, 1596 for 1576 of, 1203 for 1233 great, 634 for 684 are, 1385 for 1384 that, 1083 for 1082
seems), the transposed figures (1355 for 1535, 483 for 438) or a figure left out (27 for 271, 129 for 1293).

**Count** (`python we028.py count`; words of `everett1825_collated_reading.md`, a word with a square bracket in it
is a hole):

| | Words | Holes | Share |
|---|---:|---:|---:|
| MS p. 1 (parts 1 and 2) | 57 | 1 | 0.982 |
| MS p. 2 | 35 | 1 | 0.971 |
| MS p. 3 | 94 | 1 | 0.989 |
| MS p. 4 | 158 | 5 | 0.968 |
| MS p. 5 | 173 | 5 | 0.971 |
| MS p. 6 | 70 | 1 | 0.986 |
| MS pp. 14-15 (part 5, passage A) | 54 | 1 | 0.981 |
| MS p. 17 | 112 | 4 | 0.964 |
| MS p. 18 | 91 | 4 | 0.956 |
| MS pp. 1-6 (parts 1-4) | 587 | 14 | 0.976 |
| MS pp. 14-18 (parts 5 and 6) | 257 | 9 | 0.965 |
| All six parts | 844 | 23 | 0.973 |

Every page and every part is at 95% or more, no gap is untried and every part is covered: by the read bar the class
is **read**, for both parts. Two choices carry the figure and are stated in `everett1825_collated_holes.md` with what they change:
13 words whose code spelling differs from the ordinary spelling by a letter are counted as read, as in `../jqa`
(if all were holes: 808 of 844, 0.957, with part 6 at 0.946 and MS p. 18 at 0.934); the five one-digit slips are
counted as read (if all were holes: 816 of 844, 0.967, with MS p. 2 at 33 of 35). The earlier figures (0.904 for
passages A to C; 0.917 to 0.949 for pp. 1, 2, 3 and 6 on the strict count) were measured against the rebuilt table
and its overlay, where a value from the alphabetical slot or from sense is a hole; against the sheet most of those
values are the key's own.

**The clerk's decipherment against the frame.** For parts 5 and 6 frame 0111 was read here beside
`beling/period_decipherment.txt`. Three places differ from that transcription: the clerk wrote "as would en / them"
(the transcription has "enable"), "his over thro" (it has "overthrow"), and at 1228 he wrote "best" (as the
transcription has), where the group is 1228 good on the frame and in all three transcriptions (best is 1328): his
misreading. Beling's file was not edited. The clerk gives the word, or a correction to it, at 18 of the 23 holes.

**Reading review.** A second AI agent, which had not made the reading, read `everett1825_collated_reading.md` as
sentences and checked every line of the six parts against the decryption, by eye and by a letter comparison: grade
A, no group left out. It found two unmarked changes, where the reading departed from the key without a mark (the
groups give "refinement education" and "prime Minister of Spain and Europe"), and two unequal standards, and the
file was changed for all four: refine[d] and Minister[s] are now holes;
des{+cri}bing carries the doubt on its group; for{+tune} is read under the one-digit rule like the other slips.
"as I observe" is kept as written (no caret; the clerk has the same).

**One key, one entry.** All six parts are in the one code. The other State Department code targets keep their own
folders, one per legation and correspondent, each with this sheet or the table rebuilt from it as its key:
`../jqa` (St Petersburg 1811-12), `../morris1813` (Cadiz and Madrid 1814-15, a copy with the blocks reversed, with
Claiborne's letters), `../crawford1813` (Paris 1813, in progress), `../appleton1823` (Cadiz 1823, in progress),
`../ellis1839` (Mexico 1836-39).

**Files of this pass.** `we028.py` (collate, key, decode, count); `everett1825_collated_transcription.txt`;
`key_we028_everett1825.tsv`; `everett1825_collated_decryption.txt` (the key output, unedited);
`everett1825_collated_reading.md` (the reading of record); `everett1825_collated_holes.md` (the 23 holes and the
five slips, one by one, and the notes on the count). The earlier
files stay as they were: `everett1825_*.txt/.md` (WAINUT), `dudout/`, `beling/`.

**Not done.** No person has looked at the film or read the text against it. Frame 0110 (the clerk's parts 1 to 4)
was not read here; for those parts the clerk's words are taken from Beling's transcription. The place of each mark
under its group was not measured against the printed rule. The reel was not searched for another copy of the Notes
or for Everett's other coded despatches. No key replay (`replay.py`) was written.

## 24 Nov 2026: the claims review applied (maintainers, later the same day)

A second AI agent, read-only, checked the page against these notes, the profile and the files, recounted the words
with its own scripts, and looked at the NARA frames (catalog JPEGs enlarged; an AI model that knew the candidates,
not blind). Its verdict: the class holds. Its findings and the maintainers' decisions, applied here, in the page and
in the ledgers:

- 24 Nov 2026: the part split of 23 Nov (pp. 1-6 read from existing decipherment) was decided before the code sheet
  was applied; with the sheet both parts are read with the known key, and the clerk's decipherment of the time stays
  the first decipherment. `outcome.parts` is removed from the profile: one method, "read with known key", for all six
  parts; `prior_solution` and `first_break` keep the clerk's decipherment as the first.
- **Credit.** The State Department's clerk deciphered all six passages at the time (frames 0110-0111). Where Everett
  slipped he wrote what the key gave and corrected it from the sense; at a few places he left the key's value (en,
  Minister, the for that), and some of his line ends are lost in the binding. WAINUT (pp. 14-18) and Brice Dudout
  (all six) deciphered them again on 27 Oct 2026, independently of each other and before the clerk's text was found,
  with the table rebuilt in `../jqa`. Andrew Beling found the clerk's decipherment, transcribed the code sheet and
  compared the three transcriptions. The maintainers read all six parts with the sheet on 24 Nov 2026. "First
  deciphered on 27 Oct 2026" is withdrawn wherever it stood.
- **[the].** "the correct principles" (114R.03.6, 1385 or 1345, the film check split) is now a hole, as [than]
  (121L.10.4, 1383 or 1388) already was: both are whole-word groups whose digits are not settled.
- **Two ticks.** At 1359 (des-cri-bing) the tick stands under the 3, and at 800 (ind-us-trious) under the first 0. By
  the printed rule they withdraw i and u, where the words want r and o withdrawn. Both words are holes:
  des{+cri}b[i]ng and ind[u]strious. The other five marks looked at (769, 256, 457, 982, 1086) stand where the rule
  needs them; the rest were not measured.
- **The clerk at nine places.** His word was one of the grounds for the choice of a group at nine places, where the
  film check went against Dudout's files or was split: 628, 458, 845, 1081, 1564, 880, 1057?/1257, 1383?/1388 and
  1385/1345 (114R.03.6). The profile said eight. No word counted as read rests on him alone.
- **The reading review** of 24 Nov found two unmarked changes (refine[d], Minister[s]), not none; both were marked as
  holes before it was recorded.
- **Smaller fixes on the page.** "best policy" is in the second line of MS p. 18 (1228 is the third group of that
  line); every number but 1601 has a key value; at [ten]or the clerk wrote "Ton" (reading tone), so the bracketed
  letters there are not his; Everett says Zea is "well versed in English and speaks it at times"; at 845 and 880 the
  two blind film readers split on the first digit, at 458 one was unsure of the middle digit, and 628 and 1564 rest
  on one reader.
- **Not changed.** The collated transcription and decryption were not regenerated: the group at 114R.03.6 stays 1385
  in the transcription and the doubt is carried by the bracket in the reading.

**Recount** (`python we028.py count`; the reviewer's own counter gives the same):

| | Words | Holes | Share |
|---|---:|---:|---:|
| MS p. 1 (parts 1 and 2) | 57 | 1 | 0.982 |
| MS p. 2 | 35 | 1 | 0.971 |
| MS p. 3 | 94 | 1 | 0.989 |
| MS p. 4 | 158 | 5 | 0.968 |
| MS p. 5 | 173 | 8 | 0.954 |
| MS p. 6 | 70 | 1 | 0.986 |
| MS pp. 14-15 (part 5, passage A) | 54 | 1 | 0.981 |
| MS p. 17 | 112 | 4 | 0.964 |
| MS p. 18 | 91 | 4 | 0.956 |
| MS pp. 1-6 (parts 1-4) | 587 | 17 | 0.971 |
| MS pp. 14-18 (parts 5 and 6) | 257 | 9 | 0.965 |
| All six parts | 844 | 26 | 0.969 |

The class stays read. It depends on counting 17 words as read under the README rules for spellings and for
one-digit slips: the 13 code spellings one letter from the ordinary spelling and the four slips still counted as
read (des{+cri}b[i]ng is now a hole for its tick). As holes, the 13 spellings give 805 of 844 (0.954; MS p. 5 0.936,
MS p. 18 0.934), the four slips 814 of 844 (0.964), and both together 801 of 844 (0.949), with MS pp. 14-18 at 244 of
257 (0.949), under the bar.
