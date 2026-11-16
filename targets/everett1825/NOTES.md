# Alexander H. Everett to Henry Clay, Madrid, 25 Sep 1825: three coded passages in the JQA code

Status: in progress. Next step: compare with Brice Dudout's reading of all the cipher, pp. 1-6 included (below; his pull request will carry his transcription), rather than transcribing frames 0112-0115 afresh; then the retry step on the sibling despatches.
Contributed by WAINUT (27 Oct 2026). Read in part with the JQA code table (`../jqa/code_table.tsv`, applied
unchanged): 347 of 355 groups have a table value; 8 groups are open and some words rest on context only. The site
page and the ledger rows are left to the maintainer.

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
  Pp. 7-13 (frames 0115-0118) are clear. Those passages are **not transcribed** here (see Remaining gaps). A pencil
  "Decyphered" at the foot of p. 4 suggests the Department deciphered them; no decipherment was found. There is no
  interlinear decipherment on pp. 14-18. Marks: a lozenge after a group = -s (plural or possessive), like the superscript o in `../jqa`; a caret
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

- comparison with Brice Dudout's transcription and reading of pp. 14-15 and 17-18 - blocker: not-attempted; his pull request will carry his files.
- groups 125, 126, 211, 258, 850, 917, 1354, 1512 and the context-only words listed above - blocker: open-codes; Everett's other cipher despatches of 1825-1826 on reel 27 are the next source of occurrences (retry not done).
- the coded passages on MS pp. 1-6 of the same Notes (frames 0112-0115, about 80 lines, very roughly 900 groups) - blocker: not-attempted; found on the review check, not yet transcribed here; read by Brice Dudout on 27 Oct 2026 (above), whose transcription is expected in a pull request; the pencil "Decyphered" on p. 4 points to a lost or unfound contemporary decipherment.

## Escalation

- [x] siblings: read with the JQA table (`../jqa`)
- [x] clear-pages: the clear text around each passage used for the sense; Manning's extract checked
- [x] known-keys: the JQA table applies directly (the = 1385, of = 1576)
- [x] print: Manning III doc. 1134 prints passage A undecoded
- [x] key-rebuild: context values checked at their occurrences; second table values confirmed
- [ ] retry: other Everett despatches on M31 reel 27 may repeat the open groups

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
