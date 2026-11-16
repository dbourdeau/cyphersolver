# John J. Appleton to John Quincy Adams, Cadiz, 6 Aug 1823: 18 code groups in the JQA code

Status: in progress. Next step: look for more coded despatches on M31 reels 24-27 and read them with the same table (the retry step).
Contributed by WAINUT (27 Oct 2026). Read in part with the JQA code table (`../jqa/code_table.tsv`, applied
unchanged): 15 of the 18 groups read, two more (1088, 794) from the alphabetical slot only, one group (192) open. The
site page and the ledger rows are left to the maintainer.

Catalogue 637. Contributed by WAINUT (https://github.com/WAINUTAI), a Dutch AI company; the work was done with AI
language-model agents, and every group was checked against the NARA frame twice, the second time independently.

## 1. The document

- **Source.** NARA RG 59, Despatches from US Ministers to Spain vol. 22, microfilm M31 reel 24
  ([naId 188609418](https://catalog.archives.gov/id/188609418)), frame 0134, foot of the left page
  ([frame](https://catalog.archives.gov/medialz/dc-metro/rg-059/603720/M31/M31-024/M31-024-0134.jpg)).
  Manning, *Diplomatic Correspondence of the United States concerning the Independence of the Latin-American Nations*
  III (1925), doc. 1124, p. 2041, prints the 18 groups (with OCR noise) and "[no decodification]".
- **Context.** The finance minister Yandiola tells Appleton that the constitutional government has sent two
  commissioners to England to liquidate an account; "the success of their mission depended upon its remaining
  secret -- that if this liquidation was effected it would produce" [code]. The two blanks in the clear sentence
  before ("an account which they had with ---- amounting to ----") are plain dashes in the MS, not code.
- **Second coded leaf, not transcribed.** Frame 0150 of the same reel is a separate leaf headed "with Mr Appleton's
  Despatch of 6 & 8th Aug. 1823": about 10 lines of numbers in the same code (1385, 1576 and 1290 occur), then plain
  text signed by Appleton; frames 0140 and 0143 are its dockets. Manning does not print it. The film is badly
  degraded by bleed-through.

## 2. The code and the key

The 18 groups are in John Quincy Adams's St Petersburg code of 1811-1812 (the = 1385, of = 1576, that = 1384,
and = 668, I = 1401), whose table was rebuilt in [`../jqa`](../jqa/NOTES.md). This folder has no key of its own:
`profile.json` names `../jqa/code_table.tsv` as its key file, as other entries use a sibling folder's key
(`../feuquieres/grand_chiffre_1691.tsv`, `../balbases1677/key.json`). Nothing in `../jqa` is changed. Three more
letters in the same code have their own folders: [`../crawford1813`](../crawford1813/NOTES.md) (Paris 1813,
catalogue 652), [`../everett1825`](../everett1825/NOTES.md) (Madrid 1825, catalogue 638) and
[`../ellis1839`](../ellis1839/NOTES.md) (Mexico 1839, catalogue 653). The code was evidently still in use at the
Madrid legation in 1823-1825.

The shared decoding script for the four letters is `decode.py` in this folder; the other three folders call it
through a small `decode.py` of their own.

## 3. Transcription and decryption

- **Transcription** (`appleton1823_transcription.txt`): `1088 648<> 1576 794<> 1384 1453 347 1372 500 /
  192: 668 1384 169 1244 1501 1110 1426 1290`. All 18 numbers agree with Manning. Diamonds after 648 and 794
  (plural); a small raised double dot after 192, meaning unclear.
- **Decryption** (`appleton1823_decryption.txt`, `python decode.py appleton1823_transcription.txt`):
  16 of 18 groups have a table value; 14 of them give the English directly: "... of [794] that La-fit-te was [192]
  and that he had a part in England".
- **Groups read from the slot.** The table's numbers run alphabetically in short stretches: among H-graded entries
  3 or fewer apart, 226 of 261 neighbouring pairs are in order. So a slot is evidence, not proof.
  - 648 = **millions**. The table has April (M, 1x), but `../jqa/code_conflicts.txt` (line 177) records a clerk
    decode of 648 as "millions"/"million" on 0210R3, and the slot is 646 might < 648 < 649 min. April fits neither
    slot nor sense.
  - 1088 = **seven [?]**. The table has sa (H, but a single clerk reading, in con-ver-sa-tions), which does not fit
    the slot 1087 set < 1088 < 1091 sever. Seven fits; so do settle, seventh and seventy.
  - 794 = **dollars [?]**. No value in the table; the slot 792 by < 794 < 796 don and the sense fit.
  - 192: **open**. Slot 191 hon < 192 < 193 hon/honor, 194 hood: a hon- word (honest, honour, honourable ...).

## 4. The reading

`appleton1823_reading.md`: "(... it would produce) [?seven] millions of [?dollars]; that Lafitte was [192], and that
he had a part in England." Lafitte is probably the Paris banker Jacques Laffitte; that identification is an
interpretation and was not checked.

## 5. Controls (`python decode.py appleton1823_transcription.txt --controls`)

The true decode has a function-word rate of 0.50; every group shifted by 1, 2, 3, 7, 50 or 100 either way gives
0.00-0.17 and syllable salad ("9th min offer ? the ri ? ted e hon to the"); three random permutations of the table
give 0.00-0.06. Hits alone prove little: 18 random numbers in 1-1600 hit a table value 9.2 times on average, because
the table is dense. What separates the true reading is the grammar and the syllable chain la-fit-te.

## 6. Prior work

Manning prints the passage undecoded. One web search found no decipherment.

## Proposed table changes (for `../jqa/code_table.tsv`, not applied)

`../jqa/code_table.tsv` was used as it is. Proposals, with the evidence above: 648 millions (clerk 0210R3, slot)
instead of April; 1088 seven [?] (slot) instead of sa; 794 dollar(s) [?] (slot; no value now).

Queued as a `jqa` follow-up for the maintainer (not applied here). The most important is 1264 = full stop, attested
41 times (Crawford 1813 30x, Ellis 1839 11x, fixed by Ellis's clear copy), which conflicts with the table's grade-H
"gar".

## Remaining gaps

- group 192 (hon-) and the slot-only values of 1088 and 794 - blocker: open-codes; each occurs once in this text and has no clerk decode; Appleton's other despatches on M31 reels 24-27 may repeat them (retry not done).
- the second coded leaf on frame 0150 - blocker: illegible; bleed-through on the microfilm, the original volume would
  allow a transcription.

## Escalation

- [x] siblings: read with the JQA table (`../jqa`); Appleton's second leaf (frame 0150) found
- [x] clear-pages: the clear text around the passage used for the sense; Manning's extract checked
- [x] known-keys: the JQA table applies directly (the = 1385, of = 1576)
- [x] print: Manning III doc. 1124 prints the code undecoded
- [x] key-rebuild: slot inferences for 648, 1088, 794, 192 with the alphabetical-run check
- [ ] retry: other Appleton despatches on M31 reels 24-27 may repeat the open groups

## Files

- `appleton1823_transcription.txt`, `appleton1823_decryption.txt`, `appleton1823_reading.md`
- `decode.py`: applies `../jqa/code_table.tsv` to any of the four letters in this code; `--controls` runs the
  wrong-key controls (standard library)

## 14 Nov 2026: reading review recorded

The reading was read as a sentence against `appleton1823_decryption.txt`, group by group (Claude, session of 14 Nov 2026).
It is one coherent clause continuing the clear text; the three holes (seven?, dollars?, 192) are marked. `reading_review` grade A
recorded in `profile.json`; the state stays read in part (read_share 0.8). No file of the reading was changed and the
frame was not re-opened.
