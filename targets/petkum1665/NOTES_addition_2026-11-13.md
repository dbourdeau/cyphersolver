# Addition to NOTES.md, 13 Nov 2026 (b186): the three remaining steps

Contributed by Malcolm McBratney (Brisbane), working with Claude (Anthropic). Answer to the maintainer's comment on #444 (12 Nov 17:02 UTC): "three doable steps remain: (1) Sehested's glossed Paris relations (unit 261294, images 5-141) for the other 29 codes, (2) filing the twelve letters per letter, and (3) the blind second readings." All readers here are AI readers. Every file in this addition is new; no existing file of the folder is changed.

## Bottom line

1. Key v5 (`key_v5.tsv`) = `key_v4.tsv` + 8 rows read under the chancery's glosses on Sehested's relations. 8 of the 29 open codes are now valued: 82, 163, 281, 307, 309, 310, 338, 369. 21 stay open. Step 1 is done in part only: 23 of the 137 images were read (list in `gloss/KEY_v5_coverage_261294.tsv`); the other 114 were opened at contact-sheet size or not at all.
2. The twelve bare letters (13 pages) are filed per letter: frozen transcription, decryption, word division, ledger, strict figure with its arithmetic, shuffle controls. The first-reader figures under KEY_v3 are the ones in our log of 12 Nov (pool 121/190), reproduced unit for unit.
3. All twelve have a blind second reading, made from the images before the first reader's files were opened. Token agreement 393/403 = 97.52%. Pooled strict share is the same for both readers under KEY_v3: 121/190 = 63.68%.
4. Under v5 no letter reaches 95%. The best is 16 Mar 1666 at 16/17 = 94.12% (unchanged by v5). Shuffled-key control per letter (first reader, KEY_v3): 0 of 5,000 at both seeds for three letters, 1 to 6 of 5,000 for two, 136 to 1,871 of 5,000 for five, and two are too short to test. The pool of twelve is 0 of 5,000 at both seeds for both readers. Details below.

## Step 1: key v5 from Sehested's glossed relations

Source: Rigsarkivet, TKUA, Speciel del, Frankrig, Gesandtskabsrelationer: Hannibal Sehested og Jean de Paulmyer 1662-65 (epid 19852643, unit 261294). Image ids from the API image list (`billed-reference-lister?bsid=261294`), fetched once each by plain curl, read from 2400 px copies.

Rule (as for v4): a value is taken only where the gloss word sits over the cipher number and the neighbouring tokens have key values that read as the gloss. No value from context. The 29 codes were those listed in `profile.json` (`outcome.gaps[0]`): 40, 82, 108, 134, 135, 151, 163, 181, 197, 198, 235, 248, 281, 307, 309, 310, 330, 338, 344, 346, 351, 369, 370, 374, 376, 388, 390, 394, 399 (10 + 10 + 9 = 29).

| code | value | tier | attestations (image, page) |
|---|---|---|---|
| 310 | nous | G | 5L "prendre avec nous elle", 6L "nous y verront", 17R "elle nous proposoit", 21R "que nous sommes" (4) |
| 369 | tant | G | 5L "pas tant considere", 8L "estre tant mieux", 18L "a tant de Princes" (3) |
| 309 | nostre | G | 6L "faire en nostre faveur", 25L "pour nostre deffence" (2) |
| 307 | negociation | G | 6L "cette negociation", 18R "ma negociation en cette Cour" (2) |
| 163 | alliance | G | 7L "bonne alliance avec", 17R "son alliance", 17L "de l'alliance", 24R "alliances et amities" (4) |
| 82 | l'Electeur de Brandebourg | G | 17R "pour gagner l'Electeur de Brandebourg" (1) |
| 281 | maistre | G | 21L "au Roy son Maistre de ne" (1) |
| 338 | quu (qu'u) | A4 | 5R "qu'un traitte" (338.26.373) (1) |

Full quotations with cipher context: `gloss/KEY_v5_attestations_261294.tsv`. Frozen: md5 4a57336cc67cae9fc649a83b4bfcbf3e at 2026-11-12T21:25:25Z (same command), after the attestations and before any decode of the twelve with v5.

Conflict (not resolved, nothing changed): key v2 row 164 = alliance (from 574R). Sehested's glosses give 164 = amitie five times (7R, 17R, 21R, 24R twice), and 163 = alliance beside it on 24R ("alliances et amities" over 163.31.38.164.31). Row 164 is left as v2 has it; both values are code words, so no count changes. `gloss/KEY_v5_conflicts.tsv`.

Effect on the counts: the 8 new rows are code words (E) except 338. They turn N into E, never into S. Every S gained under v5 in the twelve comes from the v4 rows PF, Q and 242 (tier A3), as `counts_twelve.txt` shows by giving v4 beside v5: per letter, v4 and v5 strict figures are identical.

## Step 2: the twelve letters per letter

Rigsarkivet TKUA England A III 52 (epid 19852633, unit 261267). Ids from the API image list (`bsid=261267`).

| id | letter | image (api id) |
|---|---|---|
| petkum_1665-01-06 | Petkum, 6 Jan 1665 (page 2) | 367 left (48872914) |
| petkum_1665-01-13 | to Biermann, London 13 Jan 1665 | 368 right (48872915) |
| petkum_1665-01-27 | to Biermann, London 27 Jan 1665 | 381 right (48872928) |
| petkum_1665-03-03 | Petkum, 3 Mar 1665 (last page) | 403 left (48872950) |
| petkum_1665-05-12 | to Biermann, London 12 May 1665 | 445 right, 446 left (48872992-93) |
| petkum_1666-03-02 | to Biermann, London 2 Mar 1666 | 618 right (48873165) |
| petkum_1666-03-16 | Petkum, 16 Mar 1666 (last page) | 625 left (48873172) |
| petkum_1666-03-23 | to Biermann, London 23 Mar 1666 | 629 right (48873176) |
| petkum_1666-03-30 | Petkum, 30 Mar 1666 (last page) | 633 left (48873180) |
| petkum_1666-04-06_king_p2 | to Frederik III, 6 Apr 1666, page 2 (page 1 = 634R, filed as petkum_1666-04-06) | 635 left (48873182) |
| petkum_1666-04-06_biermann | to Biermann, London 6 Apr 1666 | 636 right (48873183) |
| petkum_1666-04-27 | to Biermann, London 27 Apr 1666 | 648 right (48873195) |

Dates for the four end-pages are those of the first reader's file names (12 Nov); the heading is on a page not transcribed. Two further bare pages (337L, 376L) belong to letters glossed by the chancery on their first page and are not part of the twelve.

Files per letter: `transcriptions/<id>.txt` (first reader, frozen 12 Nov 11:20:14 UTC, copied byte for byte), `decryptions/<id>.txt` (KEY_v3, byte-identical to the decode of record), `decryptions/<id>_v5.txt` (KEY_v5), `units/<id>.seg` (first reader's word division, written after the decode and before the tally, as in our log), `units/<id>.ledger.tsv` (label of every unit under v3, v4, v5). The figures are in `counts_twelve.txt` with S, E, N and the division written out; `controls_twelve.txt` has the shuffles.

The filed figures (KEY_v3, first reader) are unchanged and come first. The v5 figures are a new decode: "v5, decoded after the key update; not held-out for leaves used to build v5". The leaves that built v5 (unit 261294) are not among the twelve. Order in this session: v5 frozen 21:25:25 UTC; blind transcriptions frozen 21:31:08 UTC; first reader's files opened after that; decodes and shuffles 21:32 to 21:37 UTC. The first reader's transcriptions and KEY_v3 decodes date from 12 Nov 11:20 UTC.

## Step 3: blind second readings

Made by a fresh AI reader from the images, before the first reader's transcriptions, word division, decodes or crops were opened; frozen (md5 and UTC time in one command) at 2026-11-12T21:31:08Z. The sign classes were fixed before the first page was read, from the labels of `key.tsv` with reference crops from the glossed Sehested leaves (`gloss/sign_convention_b186_blind.md`). Four corrections of sign class were made on close crops before the freeze and are logged: G to Q three times (381R once, 403L twice) and G to QX once (446L). Then: agreement with the first reader (`agreement_twelve.txt`), one decode with v3 and one with v5, one strict count, shuffles at seeds 20261112 and 7.

Exposure, disclosed: before transcribing, the blind reader had read the first reader's log, which names the files, their md5s, the 14-page list, the pooled tally (121/190) and one token string ("218.26.385" on 635L). The blind reading of that group is 218.26.365~ and agrees with the first reader's file. The blind reader also saw, in a sister folder, one token string of the 28 Apr 1665 letter (185.277.ct.368.MT, "comeatus"); the 12 May letter has a similar group, read blind as 185.277.ct.369~, and the first reader has the same. No decode of the twelve was seen.

Blind units are the first reader's word units mapped onto the blind tokens (as for the five letters of the comment on #444); the first reader's notes (`!N`) are kept.

## Per-letter table

Strict = S/(S+E+N). F = first reader (b138, 12 Nov), B = blind reader (b186). Shuffles: shuffles at or above the true score, of 5,000, seed 20261112 / seed 7, KEY_v3 (v5 gives the same numbers for every letter, because v5 adds no row the control scores).

| letter | F v3 (filed) | F v5 | B v3 | B v5 | agreement | shuffle F | shuffle B |
|---|---|---|---|---|---|---|---|
| 1665-01-06 | 16/25 = 64.00% | 16/25 = 64.00% | 17/25 = 68.00% | 17/25 = 68.00% | 53/53 | 0 / 0 | 0 / 0 |
| 1665-01-13 | 7/20 = 35.00% | 7/20 = 35.00% | 7/20 = 35.00% | 7/20 = 35.00% | 22/24 | 158 / 136 | 156 / 155 |
| 1665-01-27 | 6/13 = 46.15% | 7/13 = 53.85% | 5/13 = 38.46% | 6/13 = 46.15% | 24/24 | 470 / 513 | 1289 / 1289 |
| 1665-03-03 | 15/27 = 55.56% | 16/27 = 59.26% | 14/27 = 51.85% | 17/27 = 62.96% | 52/55 | 6 / 6 | 286 / 280 |
| 1665-05-12 | 13/19 = 68.42% | 14/19 = 73.68% | 13/19 = 68.42% | 14/19 = 73.68% | 52/52 | 3 / 1 | 3 / 1 |
| 1666-03-02 | 14/20 = 70.00% | 14/20 = 70.00% | 14/20 = 70.00% | 14/20 = 70.00% | 45/46 | 0 / 0 | 0 / 0 |
| 1666-03-16 | 16/17 = 94.12% | 16/17 = 94.12% | 16/17 = 94.12% | 16/17 = 94.12% | 41/42 | 197 / 197 | 197 / 197 |
| 1666-03-23 | 5/7 = 71.43% | 5/7 = 71.43% | 5/7 = 71.43% | 5/7 = 71.43% | 16/17 | 262 / 260 | 245 / 227 |
| 1666-03-30 | 7/14 = 50.00% | 7/14 = 50.00% | 7/14 = 50.00% | 7/14 = 50.00% | 18/18 | 1871 / 1850 | 1871 / 1850 |
| 1666-04-06 king p2 | 22/25 = 88.00% | 22/25 = 88.00% | 23/25 = 92.00% | 23/25 = 92.00% | 65/66 | 0 / 0 | 0 / 0 |
| 1666-04-06 Biermann | 0/1 = 0.00% | 0/1 = 0.00% | 0/1 = 0.00% | 0/1 = 0.00% | 2/3 | not testable (2 spelled tokens) | not testable (1) |
| 1666-04-27 | 0/2 = 0.00% | 0/2 = 0.00% | 0/2 = 0.00% | 0/2 = 0.00% | 3/3 | not testable (0) | not testable (0) |
| pool of twelve (information only) | 121/190 = 63.68% | 124/190 = 65.26% | 121/190 = 63.68% | 126/190 = 66.32% | 393/403 = 97.52% | 0 / 0 | 0 / 0 |

Pool arithmetic. F v3: 16 + 7 + 6 + 15 + 13 + 14 + 16 + 5 + 7 + 22 + 0 + 0 = 121; units 25 + 20 + 13 + 27 + 19 + 20 + 17 + 7 + 14 + 25 + 1 + 2 = 190. F v5: 16 + 7 + 7 + 16 + 14 + 14 + 16 + 5 + 7 + 22 + 0 + 0 = 124. B v3: 17 + 7 + 5 + 14 + 13 + 14 + 16 + 5 + 7 + 23 + 0 + 0 = 121. B v5: 17 + 7 + 6 + 17 + 14 + 14 + 16 + 5 + 7 + 23 + 0 + 0 = 126. Pool shuffles: F v3 true -3.5810, best -4.1456 (seed 20261112, as in our log) and -4.1285 (seed 7); B v3 true -3.6298, best -4.1522 and -4.0820.

Disagreements between the readers (9 substitutions, 1 omission, `agreement_twelve.txt`): 13 Jan 204/201 and 54~/51; 3 Mar QX/Q, G/Q, 6~/B; 2 Mar Q/G~; 16 Mar 243~/343~; 23 Mar PSI/U4; 6 Apr (king) X~ omitted by B; 6 Apr (Biermann) 14/U4. Five of the ten are sign-class choices among G, Q and QX or PSI and U4: the forms are close, and 403L has an x-like interline mark under a sign that one reader took as the cross of QX and the other as a separate mark. Not adjudicated here.

## Caveats

- No letter is read in the README's sense (95%). 16 Mar 1666 is at 94.12% on 17 units with 0 code words, but its shuffle control fails (197 of 5,000 at both seeds): too few spelled tokens to tell the key from chance on its own.
- Per-letter shuffle controls: 0 of 5,000 at both seeds for 6 Jan 1665, 2 Mar 1666 and 6 Apr 1666 (king, p.2), both readers; 3 and 1 of 5,000 for 12 May 1665; 6 of 5,000 for 3 Mar 1665 (first reader) but 286 and 280 (blind); 136 to 1,871 of 5,000 for 13 Jan, 27 Jan 1665, 16 Mar, 23 Mar, 30 Mar 1666; not testable for the two one-group letters. The pool of twelve is 0 of 5,000 at both seeds for both readers. Our log of 12 Nov reported only the pool; the per-letter results at seed 20261112 were in our working files and are the same as here.
- v5 is not held out. It was built after every count of record and after the first reader's decodes of the twelve (12 Nov); its effect here is on code words only (N to E).
- Step 1 covers 23 of 137 images. The 21 open codes (40, 108, 134, 135, 151, 181, 197, 198, 235, 248, 330, 344, 346, 351, 370, 374, 376, 388, 390, 394, 399) were looked for only there. Sehested writes to the king about Paris; Petkum's open codes are mostly London names and titles, so some may not occur in unit 261294 at all.
- Blind reader exposure as disclosed above. Units of the blind reading are the first reader's; a reading that changes a word is judged with the first reader's word and note.
- Shuffles were run with the contributor's `decode_v2.py` (b94, md5 873d99230b08bc7b4aa8fdc0f986cb27), the decoder of record for these letters, whose logic `scripts/shuffle_control.py` reproduces; `shuffle_control.py` itself was not changed or run by us. The French corpus header guard is that of b138.
- The repository's checkers were not run by us.

## Reproduce

From the folder: `python3 -I scripts/count_twelve.py` (writes `counts_twelve.txt` and `units/*.ledger.tsv`; asserts every .seg against its frozen transcription; needs `key.tsv`, `key_v4.tsv`, `key_v5.tsv`); `python3 -I scripts/agreement_twelve.py` (writes `agreement_twelve.txt`). Decryptions were written by `decode_v2.py` in decode mode (b94), of which `scripts/decode.py` is the decode mode unchanged in logic (NOTES.md); we did not run `scripts/decode.py`. The twelve KEY_v3 decryptions are byte-identical to the first reader's decodes of 12 Nov (checked by `cmp`).

## What remains

- Step 1: images of unit 261294 not read in full (`gloss/KEY_v5_coverage_261294.tsv`), and the 21 codes still open.
- Readings (French with holes and English) for the twelve: not written.
- Blind second readings of the four letters of #444 and the four Paulmyer letters: not made in this session (not among the three steps named).
- The 164 conflict (amitie in Sehested's glosses; alliance in v2 from 574R).
