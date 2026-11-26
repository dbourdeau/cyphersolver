# Juan Manuel 1496: two blind sign-shape sheets (23 and 24 Nov 2026) and the <W26> = 77 merge (Brice Dudout, with Claude)

This folder holds a reviewer's pass on Andrew Beling's target. None of his files outside `dudout/` are changed:
`words_*.tsv`, the transcriptions and the decodes are his, and the folder's figures (653/933, 253/388) are left
for him and the reviewer to update. George Lasry's no. 95 key is applied unchanged (sha256 5ee40781...), with no
value added. Images: BNE MSS/20212/61/1-2 (CC BY 4.0, BNE). No image or thumbnail is committed here.

## The two sheets

Brice Dudout saw only the boxed sign and example thumbnails of the candidate forms, cut from the same letters.
He saw no values and no readings. The rules were written and hashed before the thumbnails were made. Both are in
French, byte for byte as hashed:
- sheet 2311: `sheet-2311-rule.md`, 1427552d...;
- sheet 2411b: `sheet-2411b-rule.md`, 2aa741e7...

Keys (`sheet-*-key.json`) were opened only after the answers (`sheet-*-answers.json`) were exported. A sign
re-entered after a sheet is marked `!` in `transcription_*_v3.txt`.

### Sheet 2311 (9 targets, 3 controls 3/3)
Five words become read:
- 18 Dec: C07 pero, C17 posible;
- 10 Nov: L09 aqui, L15 remedio, L23 Proencia.

Two <W26> (barred v) were confirmed as transcribed, and one answer was "neither" (J6 ninero). One question (J2) was
not integrated: its example thumbnails showed two different characters, a fault of the sheet.

Results: `sheet-2311-results.tsv` (French columns: reponse = answer, forme = form, verdict).

### Sheet 2411b (8 targets, 3 controls 3/3)
- Three <W26> were seen as the 77 form (o) and re-entered as 77!. Each makes a word read: C10 comendador, C15 con,
  C16 lo.
- Three <W26> were confirmed as transcribed (C05 legad?, C10 p?r, C12 c?n).
- J2 (10 Nov R10 "enbi?"): 77 was chosen, with the remark "or another form?". The word is "enbio" {probable} and is
  not counted.
- J6 "ninero": neither form, left unresolved.

Results: `sheet-2411b-results.tsv`.

## The merge <W26> -> 77 (o), adopted on the reviewer's decision, all {probable}

On the control 77 (q01), Brice remarked that the two forms "must be the same character, written in different
ways". The six <W26> places of sheet 2411b also form a continuum of shapes. So <W26> was merged into 77 with the
frozen key, in `transcription_*_v3_merge_W26_77.txt` and `decode_*_v3_merge_W26_77.txt`:
- **No word that was already read breaks.**
- **42 words become read**: 27 on 18 Dec and 15 on 10 Nov. They are listed word by word in
  `merge_W26_77_*.tsv` (columns: ligne = line, avant = before, fusion = after the merge, lecture = reading).
- The identification was made after the decodes had been seen, as for the target's S. So **the 42 words are
  {probable}** under #728 until a measure confirms <W26> = 77.
- In 7 places the sense does not want o: 18 Dec A23 "firma" and C09 "enbia"; 10 Nov L08 "esto", L09 "esta",
  L12 "dexadas", R04 "haze" and R10 "enbia". Four of the five on 10 Nov may hide a second sign in the <W26> class.
  These places need a look before the merge is taken as sure.

## Counts (the folder's word rule: a cipher word is read when its decode equals the reading)

| | 18 Dec (933) | 10 Nov (388) | both (1,321) |
|---|---|---|---|
| main (as filed) | 653 (70.0%) | 253 (65.2%) | 906 (68.6%) |
| after sheet 2311 | 655 (70.2%) | 256 (66.0%) | 911 (69.0%) |
| after sheet 2411b | 658 (70.5%) | 256 (66.0%) | 914 (69.2%) |
| with the merge (42 {probable}) | **685 (73.4%)** | **271 (69.8%)** | **956 (72.4%)** |

Sure words only (no merge): 914/1,321. `words_*_v3.tsv` is the word table after sheet 2411b, without the merge.

## Credit
- Target, transcriptions and word rule: Andrew Beling.
- Key: George Lasry.
- Blind reader of the sheets: Brice Dudout.
- Sheets built, scored and integrated by Claude (AI agent).
