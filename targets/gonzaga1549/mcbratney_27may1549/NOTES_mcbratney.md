# cv1549: Charles V to Ferrante Gonzaga, Brussels, 27 May 1549 (Estense, Campori, Karl V sfasc. III cc. 31-36; decipherment cc. 12-15)

Status: in progress. Prepared for a PR on Malcolm's say; nothing filed, sent or pushed. Only c.31r (22 cipher lines of 184) is
transcribed and decoded. The key is the existing `targets/gonzaga1549/sign_table.tsv`, unchanged; the contemporary decipherment
is the external reference. One key, one entry: if filed, these files belong in `targets/gonzaga1549/` as the 27 May letter.

Biblioteca Estense Universitaria, Modena, Autografoteca Campori, Lettera K, Karl V, sfasc. III. Cipher letter cc. 31-36, Lodovico
record bbdff1f6-f75f-44e1-b9d0-c66a83a9a7a9 (12 canvases; cipher on 31r, 31v, 32r, 32v, 33r, 33v, 34r, 35v, 36r). Contemporary
decipherment cc. 12-15, record 968f7688-4b71-44f2-9954-737adabf92c3, headed "Su Md. en carta de xxvij de Mayo 1549 en Bruxellas".
Spanish; signed by the Emperor, countersigned Vargas(?). Licence CC BY-NC-SA. Block map of all 16 cipher blocks against the
decipherment: r2_estense2 `BLOCK_MAP.md` (not copied here).

## Prior art (before any decode)
`PRIOR_ART.md`. No published reading found. **RISK open on one item: Bertomeu Masiá 2009 not checked** (book not online; it
reproduces two Gonzaga letters, which ones is unknown). The plaintext has existed since 1549 in the same file (cc. 12-15).

## Order of work, 15 Nov 2026 (UTC)
1. 06:33 key table fetched from dbourdeau and mmcbratney main: identical, md5 dd3266dc1f24a2a71ae1d3aec658da7d. Tomokiyo's image
   of Masiá's key (`ref/CharlesV3.gif`, md5 c96ba33d59a999d3794371d8850f23a2) used to read the table rows' shapes.
2. 06:35-06:36 c.31r fetched as native-resolution IIIF crops from the Mac VM (plain GET, one at a time, >=1.3 s apart; 6 bands then
   12 half-bands; one request answered 400 "upscaling should be prefixed with ^", a format error, not a bot check; re-requested at
   native size). Log: Mac `~/Downloads/codebreaking/localai/bench/cv1549/fetch_log.tsv`.
3. Transcription of c.31r by eye, shape labels (`27may1549_31r.tsv`); key file mapping every label to a table value
   (`key_cv1549.tsv`). Exposure: I had seen the decipherment's incipits in BLOCK_MAP.md (B1-B3) before transcribing; c.12r was not
   read before the freeze.
4. **Freeze 06:44:41Z** (`FREEZE.txt`): transcription md5 087034a3661f7600f63444931fecdd10; key md5 8ed377175565360dadf2a6064c7ede32.
5. c.12r L1-L15 transcribed (`27may1549_decipherment_12r.txt`), block references written (`ref_blocks.json`), decoder and controls
   written; **freeze 06:47:15Z** (decoder 7b7def7a58627ced2629ba97eda42459, controls f82dfb5cbdcd1a527987e8e213617402,
   references 9a06ea7b5cf870dc45000c1b325995e3).
6. One decode (`decode_cv1549.py`): first pass, figure of record. No emendation was made.
7. Controls (`controls_cv1549.py`), then post-hoc analysis (`analysis_after_decode.py`, `ledger_cv1549.py`), labelled as such.

## Figures of record (first pass, frozen key, frozen transcription, frozen references)
Per letter (`27may1549_score.txt`): reference letters matched by an identical decoded letter, Levenshtein alignment.
| Block | 31r lines | Units | Holes | Matched / reference letters | % | 65% line |
|---|---|---|---|---|---|---|
| B1 | 1-4 | 65 | 9 | 72 / 118 | 61.0 | **fails** |
| B2 | 5-14 | 151 | 11 | 193 / 269 | 71.7 | passes |
| B3 (first 9 lines) | 14-22 | 166 | 9 | 144 / 208 | 69.2 | passes |
| All | 1-22 | 382 | 29 | 409 / 595 | **68.7** | passes |
Sums: 65 + 151 + 166 = 382 units; 72 + 193 + 144 = 409; 118 + 269 + 208 = 595; 409 / 595 = 0.687.

Per unit (`27may1549_ledger.tsv`): S = key value identical to the decipherment letters it aligns to; E = value given, not
identical; N = no value. S 245, E 108, N 29 (245 + 108 + 29 = 382). **S 245 / 382 = 64.1%: fails the 65% line.**
B1 47/65 = 72.3%, B2 114/151 = 75.5%, B3 84/166 = 50.6%.

Caveats on these figures:
- **The B3 reference was frozen too short.** It stops at 12r L15 "proueea"; c.31r runs on to about 12r L17 "no seria [tolerable]".
  The per-letter alignment lets the reference end early, so B3's per-letter figure counts only the reference up to there; the units
  past that point have nothing to align to and are E in the ledger, which is why B3's unit figure is 50.6%. A rescoring with the
  reference run on to 12r L17 gives B3 212 / 298 = 71.1% and all 477 / 685 = 69.6% (`27may1549_analysis.txt`). That is a second
  figure after the decode, not the figure of record.
- **The per-letter metric has a high chance floor.** Shuffled keys score a median 29.9% and up to 38.7%; scoring a block's decode
  against the wrong block's reference gives 19.3% to 53.4% (B2's decode against B1's shorter reference: 53.4%). Read the 68.7%
  against those, not against zero.
- Clear-letter words inside the cipher (em, ne, sa, tus, quod, nec, pre: 7 units) are counted as holes.
- 63 of the 382 units are flagged "?" (shape doubtful) in the transcription; their values were still taken from the key as labelled.

## Controls (`27may1549_controls.txt`)
- Shuffled key: the values of the 66 labels that have one, permuted, 5,000 keys per seed. Seed 20261112: 0 of 5,000 reach the real
  409 letters; best 37.8%, median 29.9%, 99th percentile 34.7%. Seed 7: 0 of 5,000; best 38.7%, median 29.9%, 99th percentile 34.7%.
- Wrong reference: each block's decode against the other two references, 19.3% to 53.4% (six pairs, listed in the file).
- Not run: the guarded same-language 4-gram shuffle with corpus md5 (no corpus chosen; the reference here is the decipherment, not a
  language model), and a word-level control for the code words (7 units only).

## Where the key and the decipherment agree and disagree (post-hoc, `27may1549_analysis.txt`)
Agree on every occurrence: theta = s (25), n = a (24), omega = e (16), d = r (11), dash-o = l (7), 8 with o-loop = co (7), theta with
bar = ne (6), 8 with two dots = ci (4), Lambda with dot = pa (4), inverted T with dot = tra (4), angle = ll (3), Lambda-o = po (3),
L-o = mo, L with dot = ma, g with two dots = ri, y-s with dot = va, y-s with two dots = vi. Nearly every time: ap = n (32/34),
crossed c = que (13/15), loop-g = y (10/11), triangle with stroke = te (9/10), y with bar across = se (8/10).
Disagree, consistently:
- **V with a dot**: the table's "pa ... also V base" gives pa; the decipherment has da (5) or ta (2) at all 7. V with two dots: pi in
  the table, di (2) and ti (1) in the decipherment. Tomokiyo's image of the key has a v-like sign in the d column and a dotted one
  under da, so the table's V-base row for pa looks wrong for this hand, or my V is the key's d sign.
- **Bare 6**: the table gives a (row a: "also bare 6"); the decipherment has i at 4 of 10. The key image's i column shows a 6-like sign.
- **"ro"/"no" letters**: the table's r; the decipherment has o at all 5. Either this hand's sign is not the key's "no", or my label is
  wrong (it looks like "ro").
- **x with loop ("fish")**: de agrees 18 times; the decipherment has no 6 times. The key has both x-curl with loop = no and x with
  o-loop = de; I lumped two signs under one label.
- **y with a tail to the right**: se in the table by the bar rule; the decipherment has su (2) and so (1): the key's su is y with p-tail.
- **3 with a dot to the right** (no value in the table): o at all 3.
These are findings for the key, not emendations: nothing above was changed in the decode.

## What the letter says (c.31r; from the decipherment)
French "stirrings and preparations" in Piedmont and their "insolences" against the Emperor's and the Duke of Savoy's vassals;
Gonzaga is right to watch them, but France has little money, few troops and is "entangled with the English", so it is not
expected to move on this side; rather it fears trouble from the Emperor's side. Gonzaga is to keep the Emperor's ambassador in
France informed, and to tell the King's lieutenant in Turin to remedy what has been "innovated" against the treaties.
[derived; historical identifications (the ambassador, the lieutenant, the treaties) not checked]

## Remaining gaps
- c.31v, 32r, 32v, 33r, 33v, 34r, 35v, 36r (162 of 184 cipher lines; blocks B3 rest to B16) not transcribed or decoded - blocker:
  none outside; not attempted this session (budget). Next step: same method, page by page, each frozen before its decode.
- Decipherment c.12r L16 to c.14v not transcribed - blocker: none outside; budget.
- Bertomeu Masiá 2009 - blocker: needs-physical-access (prior-art RISK).
- 4-gram shuffle control and word-level control - blocker: none outside; not run.
- Blind second transcription of c.31r - blocker: needs a second reader.

## Escalation
- [ ] siblings: the other gonzaga1549 letters use the same table; the disagreements above (V-dot, bare 6, ro, fish) should be checked
  against their transcriptions before any key change.
- [ ] clear pages: the clear paragraphs of the letter (34v, 35r, 35v) are not part of the cipher; not needed.
- [x] known keys: sign_table.tsv (Masiá via Tomokiyo) applied unchanged.
- [ ] print: Masiá 2009, Corpus documental III not checked.
- [ ] key rebuild: a new key version from the decipherment would be "key recovered based on adjacent plaintext"; not done (one key,
  frozen, per instruction).
- [ ] retry: none.

## Files
`27may1549_31r.tsv` transcription (frozen); `key_cv1549.tsv` key (frozen); `FREEZE.txt`; `27may1549_decipherment_12r.txt`;
`ref_blocks.json`; `decode_cv1549.py`; `27may1549_decryption.txt` (decode, unit by unit); `27may1549_score.txt` (alignment);
`controls_cv1549.py`, `27may1549_controls.txt`; `ledger_cv1549.py`, `27may1549_ledger.tsv`; `analysis_after_decode.py`,
`27may1549_analysis.txt`; `27may1549_reading.txt`; `27may1549_en.md`; `PRIOR_ART.md`; `profile.json`; `ref/` (key table, key image,
upstream NOTES copies). Crops are on the Mac (`~/Downloads/codebreaking/localai/bench/cv1549/crops/`), not here.
Not done: evidence timestamps (stamps/stamp.sh), evidence email, PR. The project checkers (`_check_profile.py`, `_check_writeup.py`)
were not run: they are repository scripts, and the Track B rule is not to run them from here.
profile.json: validated against upstream profile.schema.json with the jsonschema library, 0 errors (not the project's _check_profile.py).
Mac link dropped at about 06:50Z: one further request for c.12r L1-L6 (crop 12r_b0) may or may not have been sent; its log line could
not be read. c.12r L1-L6 were read from the 1200 px image already held instead. The fetch log and crops stay on the Mac.
