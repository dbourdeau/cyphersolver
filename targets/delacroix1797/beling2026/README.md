# delacroix1797: the clear draft of despatch No. 5 found, matched to the 653 groups, and a partial table of the code

Contributed by Andrew Beling, with AI agents (Claude Opus), 21-22 Nov 2026. This folder adds to Daniel Bourdeau's
target `targets/delacroix1797` (catalogue 649) and changes nothing outside it: the target's `NOTES.md`,
`profile.json`, `ciphertext.txt` (Michael Brackx's transcription) and `solver/` are untouched. Whether and how the
target's status changes is the maintainers' call.

## What was found

1. **The plaintext survives.** The French foreign ministry's own clear draft of the despatch is in the Archives
   diplomatiques, Correspondance politique, États-Unis, vol. 48 (39CP/48), ff. 41r-42r, images 81-83 in the archive's
   viewer: [f. 41r](https://archivesdiplomatiques.diplomatie.gouv.fr/ark:/14366/bg45qmrw70n9/2b676193-3faa-4124-8969-36508dbd0385),
   [f. 41v](https://archivesdiplomatiques.diplomatie.gouv.fr/ark:/14366/bg45qmrw70n9/b9c3c223-5dcd-4f49-9812-0a19cafc5310),
   [f. 42r](https://archivesdiplomatiques.diplomatie.gouv.fr/ark:/14366/bg45qmrw70n9/20350b61-e4d4-4561-ae72-5403928abb96).
   It is dated Paris, 25 messidor an V, addressed to Létombe, and marked in the margin "à chiffrer. F." and
   "Politique N° 5". Found on 21 Nov 2026 in the archive's online viewer. This is the "minute" the target's NOTES name
   as what would move it.
2. **A test fixed beforehand shows the draft is the text behind Brackx's 653 groups** (table below).
3. **A partial table of the code ("cipher F")** follows from the pair. On Brackx's digits as transcribed
   (`key/code_table_F_partial.tsv`): 297 numbers with a value, 136 confirmed by two or more uses that agree, 148 on a
   single use, 13 unsure. The table of 21 Nov applied all eight proposed digit changes, which the earlier notes did not
   say; it is kept as `key/code_table_F_with_proposals.tsv` (296 numbers, 136 confirmed, 149 single use, 11 unsure;
   251 and 1034 occur only under the proposed changes). What each change does to the table, with the blind readers'
   support, is in `key/proposal_dependent_entries.tsv`.
4. **The American copy lacks one clause of the draft**: "Le Citoyen Ade[t] *est arrivé à Paris, il y a quinze jours:
   Il* a eu son audience" has no groups for the words in italics (the groups run `81 973 | 82 727 969`, a-de | a eu
   son). Probably a copyist's skip; where it happened cannot be told from the film.

This is a reading from the period's clear text, not a solution of the code from the numbers. Read share of the
reading, measured on Brackx's digits as transcribed: 0.939 (27 of 444 cipher words marked), so **read in part** by
the 95% bar. The holes are the eight places where a digit change is proposed (marked whatever is decided), the unsure
values, and a few groups that stand for something other than their value elsewhere. Caution: 148 values rest on one use in this letter, so the share measures
how consistently the table gives the draft; the evidence that the draft is the text is the test.

## The test (plan written and hashed before the draft's wording was opened)

Plan: `plan/TEST_PLAN.md`; hashes of the plan, the scripts, the ciphertext and the test text: `plan/FREEZE_before_reading_draft.txt`
(plan 01:31 EST, test text 01:32 EST, results 01:43 EST on 21 Nov 2026). These are local file times and SHA-256 sums only;
there is no outside timestamp (no RFC 3161 stamp), so the order of events rests on our record. The freeze file uses the
first session's local names: `work/ciphertext_brackx_upstream.txt` is `../ciphertext.txt` and `test_text_merged.txt` is
`transcriptions/clear_draft_test_text.txt` (same sha256); the scripts keep their names. The plan's writer had
seen the two draft readers' short reports (their line counts and hard spots such as "[facilité?]", "Boston"), not the draft's wording.

**Which digits each step used.** Tests 1, 2a, 2b and 3 (the full alignment, the frozen training table and its 36 of 43)
ran on Brackx's digits exactly as upstream (`../ciphertext.txt`, sha256 663e0a42..., recorded in the freeze file), as
the plan required. The hand alignment `key/alignment_by_group.txt`, the decryption and the reading are on Brackx's
digits too. Only the table of 21 Nov (`key/code_table_F_with_proposals.tsv`) applied the eight proposed changes; the
frozen test files are left as they were.

| Test | Pass mark set beforehand | Result | Controls | Verdict |
|---|---|---|---|---|
| 1. Letters of the draft per group | 2.0 to 6.0 | 3.42 (2,234 letters, 653 groups) | none | pass |
| 2a. Repeated runs of 3+ groups fall where the draft repeats a string | at least 0.60 and above all 200 controls | 0.83 (15 of 18) | up to 1.00, mean 0.70 | **miss** |
| 2b. Full alignment: share of repeated groups that take the same letters each time (best of 8 starts) | at least 0.50 and above all 80 controls | 0.77 | 40 shuffled drafts up to 0.16, 40 passages of Turner 1904 up to 0.17 | pass |
| 3. Table fitted on the first 568 groups, frozen (sha256 8854344a...), scored on the last 85 | at least 40 predictions, 70% fit, above the 99th percentile of 200 shuffled keys | 43 predictions, 36 fit (84%); 34% of letters covered | shuffled keys: 99th percentile 13%, max 14% | pass |

Test 2a is reported as a miss: its controls score almost as high, because 11 of its 18 pairs are repeats of one run
(`705 806 711|400 405`, "citoyen"), so it could not separate anything. The verdict rule (tests 1 and 2b) was fixed in the plan.

**Independent re-check, 22 Nov 2026** (a second AI agent, which did not write the first session's code):
- the frozen hashes match the files; the first session's scripts were re-run from the frozen inputs:
  tests 1 and 2a, all eight alignment starts of test 2b (0.77 best) and all 80 controls (at most 0.17) came out
  identical, the full alignment byte for byte; re-fitting test 3 gave the same frozen table (sha256 8854344a...) and
  the same score, 36 of 43. The scripts are deterministic, so this shows the files give the numbers, not when they
  were made.
- a separate scorer for test 3, written from scratch (`scripts/reviewer_heldout.py`, its plan in
  `review/REVIEW_PLAN_heldout.md`, output `review/heldout_mine.json`): **36 of 43 predictions fit**; 1,000 shuffled
  keys fit 12.3 on average, 17 at the 99th percentile, 18 at most. Compared with the hand alignment group by group,
  34 of the 43 predictions give exactly the draft's letters there; the other 9 differ by an ending (`re`/`rez`,
  `au`/`aux`, `consuls`/`consul`, `les`/`le`) or are a fitting error (413 given as "j"; it is a full stop).
- 28 lines of the draft (13 on f. 41r, 8 on f. 41v, 7 on f. 42r) read again on the images against
  `transcriptions/clear_draft_ff41r-42r.md`: no difference of wording.

## Files

| Path | What |
|---|---|
| `transcriptions/clear_draft_ff41r-42r.md` | the draft, line by line, merged from two blind AI readings (`clear_draft_reader_A.txt`, `clear_draft_reader_B.txt`); one wording dispute ("aurez"/"avez"), settled |
| `transcriptions/clear_draft_test_text.txt` | the letter body used in the tests (frozen) |
| `key/alignment_by_group.txt` | each of the 653 groups with the draft letters it stands for (made by hand after the tests) |
| `key/code_table_F_partial.tsv` | the partial table on Brackx's digits: class A confirmed by 2+ agreeing uses (136), B one use (103), B2 one use, only the joint value of a pair or triple sure (45), C unsure (13). Column `at_proposal_places` counts uses at the eight places where a change is proposed; the class is judged on the other uses, and every value a number takes is in `all_values` |
| `key/code_table_F_with_proposals.tsv` | the table of 21 Nov, built with all eight proposed changes applied (A 136, B 104, B2 45, C 11) |
| `key/proposal_dependent_entries.tsv` | for each of the eight places: the entry on Brackx's digits, the entry under the proposal, and the blind readers' support |
| `decryptions/decryption_1797-07-13.txt` | `key/code_table_F_partial.tsv` applied to Brackx's digits, unedited (`scripts/decode.py`) |
| `readings/reading_1797-07-13.md`, `translations/translation_1797-07-13.md` | the French text by sentences with holes marked (`scripts/make_reading.py`), and an English translation |
| `proposals/transcription_corrections.tsv` | eight digit changes offered to Brackx's transcription, with three blind readings of the film |
| `plan/`, `tests/` | the plan, its hashes, the run log and the results of tests 1-3, the frozen training table |
| `scripts/` | `align_em.py`, `run_tests.py`, `heldout.py` (tests), `check_manual.py`, `build_table.py` (table), `decode.py`, `make_reading.py`, `reviewer_heldout.py`, `code_structure.py` |
| `review/` | the independent re-check of 22 Nov |

To reproduce (Python 3 with numpy): `python scripts/run_tests.py ../ciphertext.txt transcriptions/clear_draft_test_text.txt <turner> out`
then `python scripts/heldout.py score ../ciphertext.txt out/alignment_full.json 568 tests` (scores the frozen table in `tests/`),
and `python scripts/reviewer_heldout.py ../ciphertext.txt transcriptions/clear_draft_test_text.txt tests/table_train_frozen.json key/alignment_by_group.txt`.
The tables: `python scripts/check_manual.py ../ciphertext.txt transcriptions/clear_draft_test_text.txt key/alignment_by_group.txt tokens.json`,
then `python scripts/build_table.py tokens.json proposals/transcription_corrections.tsv key/code_table_F_partial.tsv --brackx`
and, without `--brackx`, `key/code_table_F_with_proposals.tsv` (both rebuild byte for byte). Then
`python scripts/decode.py ../ciphertext.txt key/code_table_F_partial.tsv` and
`python scripts/make_reading.py transcriptions/clear_draft_test_text.txt key/alignment_by_group.txt key/code_table_F_partial.tsv proposals/transcription_corrections.tsv`.
`<turner>` is the plain text of Turner, *Correspondence of the French Ministers to the United States, 1791-1797* (1904),
archive.org item `correspondenceof00turnrich`, file `correspondenceof00turnrich_djvu.txt` (sha256 42cdda7c...), used
only for control passages; not committed. Test 2b takes about ten minutes on 14 cores.

## Transcription doubts

The digits are Brackx's; we change none. Proposals, each read blind on the film (NARA M30 roll 4, frames 0244-0245)
by three AI readers given shuffled line crops and nothing else (two on 21 Nov, one on 22 Nov):
- 808 (245 left, line 12, 8th group) - read: 898 with "80" written above (3 of 3); checked: image, decode (898 = con four times; le-con)
- 1024 (245 left, line 13, 1st) - read: 1034 (2 of 3; the third 1084, second choice 1034); third digit blotted; checked: image, decode (1033, 1035 = e; pri-e)
- 327 (245 left, line 25, 8th) - read: 527 (2 of 3; the third 327); checked: image, decode (527 = d three times; d'envoyer)
- 257 at three places where the text has "ai" (244 right line 11, 9th; 244 right line 17, 6th; 245 left line 15, 4th) - read: 257 by most readers (251 first choice for the third reader at two of the three places); checked: image, decode; unresolved: either the clerk wrote 257 (= al) for 251, or the code has something we do not understand; 251 = ai is a conjecture from the text and the run 253 ainsi, 254 ajouter, 257 al
- 108 (244 right, line 19, 1st) - read: 108 or 128 (no reader 100); unresolved; the text wants "sur" (100 = sur twice)
- 381 (245 left, line 25, 11th) - read: 381 (3 of 3, blotted); unresolved; the text wants "del" (361 = de l')
- 383 (244 right, line 7, 3rd), where the text wants "de la" - read: 383 (third reader's second choice 363; 363 = de la elsewhere); unresolved
- seen in passing on 21 Nov: 300 read 308 by two readers (244 right line 5), 1105 read 1185 or 1195 (245 left line 20); both single-use values, numbers in doubt
The eleven unsure values of the 21 Nov table were read on the film by the third reader at all 21 of their places: every
first reading agrees with Brackx, so their doubt is in the value, not the digits.

## What the code looks like (observations from the table)

- Whole words, syllables, single letters and names: 887 gouvernement, 368 dépêche(s), 705 ci, 806 to, 150 m, 921 Boston,
  767 Adams; Adet, Rozier and Mozard are spelled out; full stops have numbers (412, 413, 416, 417).
- **Neither one-part nor plain two-part.** Over the whole table, number order and alphabetical order of the values do not
  agree (Spearman 0.08; shuffled 99.5th percentile 0.16), as the target's NOTES found. But neighbouring numbers are in
  alphabetical order far more often than chance: 76% of adjacent pairs ascend against 50% for shuffled values (99.5th
  percentile 55%), e.g. 2-10 ce, celui, cer, ces; 253-257 ainsi, ajouter, al; 493-500 point, politique, port,
  possible (figures from the table on Brackx's digits). So the table is made of short alphabetical runs placed in an order that is not alphabetical
  (`scripts/code_structure.py`). Common syllables and letters recur in several runs (e, s, se, d, m, i, et), which is
  where most far-apart homophones sit; 16 of 30 values with two or more numbers keep them within a small block, as the
  target's NOTES inferred (81-83 a, 972-973 de, 265-269 le/les, 799-800 vous).
- `705 806 711|400 405` (seven times) is ci-to-y-en, Citoyen.

## Weaknesses a reviewer should weigh

- **Draft against sent text.** The draft is the ministry's minute, not the copy that was enciphered. Where the
  alignment breaks: the missing clause above; "par M. Adams" has no group for "M." the first time; on f. 41v line 11 the
  word written over another reads "facilité" but the groups carry "utilité" (1126, which also gives "utiles" four words on),
  so the enciphered text had "utilité" or the overwriting came later; 571 stands where the draft has both "(se)rait" and
  "général"; 496 stands for "port" three times and once where the draft has "pui(ssent)"; 268/269 give "les" where the
  draft has "le". These are listed as holes in the reading.
- **One letter only.** No second text in this code has been found (39CP/48 paged in full, 39CP/47 spot checked: they
  hold the ministry's decipherments of Létombe's despatches, not the numbers), so the 148 single-use values are
  untested outside this letter.
- **Test 2a missed**; it is reported, not counted.
- **Readers.** All transcription readers and both checking sessions are AI agents (Claude Opus). No person has read the
  film or the draft for this contribution.

## Sources and credits

- Michael Brackx: transcription of the 653 groups (issue #122, 27 Oct 2026), and the pointer to Létombe's reply.
- Daniel Bourdeau: the target, its structural findings (neighbouring-number homophones; strict one-part order ruled out).
- Archives du ministère des Affaires étrangères, France, Correspondance politique, États-Unis, vol. 48, ff. 41r-42r
  (the draft; images linked above, not committed). The archive states that reuse of its public information is free
  provided its provenance is cited; the images are linked here to keep the repository small.
- US National Archives, RG 59, M30 roll 4, frames 0244-0245 (the copy in code; catalog naId 188512917); not committed.
- Andrew Beling, with AI agents: finding the draft, the test, the table, the review.
