# R4936 g/q shape check, 23-24 Nov 2026: the evidence, as text

No DECODE image and nothing derived from one (no crop, thumbnail or sheet page) is in this folder. The images are
DECODE R4936 (IMG_R4936_I28640_P1/P2, access level 2) and stay private. Box coordinates below are pixels of the native
image, so a reader who has the image can find each place.

The rule, the key and the protocol are committed byte for byte as they were hashed, in French; this file gives the
English. `SHA256SUMS.txt` lists the hashes: `shasum -a 256 -c SHA256SUMS.txt` from this folder. The hashes were
written locally when each file was frozen and first quoted publicly in PR #917 (commit c752a72); there is no
outside timestamp, so the order "frozen before looked at" rests on our log.

## Part 1. Blind sheet T, answered by a human (Brice Dudout)

- `sheet-T-rule.md` (SHA-256 7f08d4fd...): the selection rule, written before any thumbnail was cut. It fixes the
  targets, the controls, the alphabet examples and what each answer does (integration clause, section "Intégration").
  Criterion: the hand's g-shaped figure has two forms, a **long loop** (the tail goes well down, turns left and comes
  back up: value u) and a **short hook** (short tail ending in a hook, like the q read t in fegyvert, eytenek).
  Targets, all on p. 1 l. 1-13 (clean letters): 8 g read t (T1-T8), 1 q read u (T9), options loop / hook; 2 c read y
  (C1, C2), options c / e. Controls: 3 clear signs (x / z). Alphabet examples are never targets or controls.
  Clause: a hook at a g read t supports t there (relabel g->q); 6 or more hooks of 8 allow proposing the form rule
  for the other g=t places, to be checked place by place before any recount.
- `sheet-T-key.json` (284ea28e...): question order (seeds 20261124 / 4936), which option ("forme 1" / "forme 2") is
  which form for each question, the boxes. It was not loaded in the sheet and was opened only after the answers.
- `sheet-T-answers.json` (62a7d87b...): the exported answers, 14 questions, no remarks.
- `sheet-T-results.tsv`: answers decoded with the key. Controls 3/3. T1-T8: 8/8 hook -> g->q at the 8 places.
  T9: loop -> q->g (u supported). C1 fegyvert: e -> c->e (y supported). C2 kyralyoknak: c -> y not supported, unchanged.
- The sheet was built and scored by AI agents (Claude); the answers are the human's. Not a human_check in the
  schema's sense; the entry is `outcome.sign_check` in `../profile.json` (moved there unchanged from
  `sign_check_pending.json` at the integration of 24 Nov 2026, the field being in the schema).

## Part 2. Place-by-place pass by an AI agent (Claude), calibrated on part 1

- `ai-protocol-partA.md` (927b4cbb...): part A, frozen before any unseen place was looked at (only the four
  alphabet examples seen). Places: the 106 g read t not on the sheet + the 36 g read u = 142. Criterion (hook /
  loop / doubtful, confidence 1-3; confidence 1 counts as doubtful). Blind calibration on 21 mixed anonymous crops
  (the 9 human places, the 3 controls, 9 unseen places drawn with seed 4936) with a stop rule: more than one
  disagreement with the human answers, or one control wrong, stops the pass. What each verdict does: g read t + hook
  -> g->q; g read t + loop -> t not supported, flagged; g read u + hook -> conflict, flagged; doubtful -> nothing.
- `ai-protocol-partAB.md` (bc670d63...): parts A + B. Part B was frozen after the calibration and before the
  133 remaining places: the calibration result and the criterion made precise on the human prototypes at 400%
  (hook: tail 1-1.4 bowl heights below the line, open hook to the left, nothing goes back up; loop: about 2 bowl
  heights or more, turns left and climbs back into a closed or nearly closed lower loop).
- `ai-calibration-classification.tsv` (d1889951...): the 21 verdicts, written and hashed before the table was read.
  `ai-calibration-table.json`: which crop was which. Agreement with the human 9/9, controls 3/3.
- Limit: the agent had read the human answers before the calibration, so the blinding covered which crop was
  which, not the expected proportion (8 hooks, 1 loop). Page 2 crops can be told by the paper colour.

## The table of places

`R4936-places.tsv`: 153 rows, one per place: the 142 AI places, the 9 human g/q places (T1-T9) and the 2 c/e
places. Columns: line, s (rank of the figure in its line among the figures of R4936_align.tsv on main, from 0,
"-" skipped), word, pos_in_word, figures_before, label_before, label_after, reading (the letter of the reading),
verdict (hook / loop / doubtful; c / e), confidence, by (human / AI), stage, effect, note_fr (the AI's note).

| | hook | loop | doubtful |
|---|---|---|---|
| g read t, human (8) | 8 | 0 | 0 |
| g read t, AI (106) | 94 | 0 | 12 |
| q read u, human (1) | 0 | 1 | 0 |
| g read u, AI (36) | 4 | 27 | 5 |

No t is written with the loop; four u are written with the hook (mutatnanak twice, instructioban, tule; tag
`g=u:hook` in `../R4936_align.tsv`): the hook supports t, it does not prove it.

## Counts (`python3 tools/R4936_count728.py` from the target folder)

341 cipher words = 338 rows of R4936_align.tsv + 3 `[...]` runs of R4936_reading.md (reading lines 9, 16 and 22; one word each).
Decision of 24 Nov 2026 (Daniel Bourdeau): the 94 AI relabels count as probable until a reader who has not seen the
answers checks them; the 8 human places stand.

| | sure | {probable} | [restored] | <unresolved> | sure share |
|---|---|---|---|---|---|
| main before the check (`--align` on main's file) | 232 | 105 | 1 | 3 | 0.680 |
| human places only (AI = probable) | **234** | 103 | 1 | 3 | **0.686** |
| AI places counted as sure | 302 | 35 | 1 | 3 | 0.886 |

The 94 AI relabels fall in 78 words; 68 of them would become sure if a blind reader confirms the AI verdicts.

## Part 3. Blind sheet C, answered by a human (Brice Dudout), 24 Nov 2026

- `sheet-C-rule.md` (SHA-256 bb67d671...): the selection rule, in French, written before any thumbnail was cut. Targets:
  the 19 places the AI pass left open: the 4 conflicts (g read u that the AI called a hook: L04 s18, L09 s27, L10 s20,
  L41 s30), 10 doubtful g read t and 5 doubtful g read u (R4936-places.tsv, verdict doubtful). Options: short hook /
  long loop, prototypes taken from places Brice settled on sheet T. 3 controls. Excluded as illegible: L31 s11-s12.
- `sheet-C-key.json` (b1acc226...): question order (seeds 20261126 / 4937), which option is which form, the boxes.
  Not loaded in the sheet; opened only after the answers were exported.
- `sheet-C-answers.json` (0df053b9...): the exported answers, 22 questions, one remark ("Q" at q04).
- `sheet-C-results.tsv`: answers decoded with the key, with the effect of each.

| | hook | loop | other form |
|---|---|---|---|
| conflicts, g read u, AI hook (4) | 0 | 4 | 0 |
| doubtful g read t (10) | 8 | 1 | 1 |
| doubtful g read u (5) | 0 | 5 | 0 |

- The 4 conflicts are loops: u confirmed, tags `g=u:hook` removed. The AI's hook label was wrong at all four places it
  had flagged, so the 94 AI relabels of part 2 stay probable.
- 8 hooks on g read t: relabelled g->q (t supported). 1 loop on a g read t (alt-, L25 s35): t not supported, tag kept.
- 1 other form (tartani, L24 s6): a long straight tail with neither loop nor hook (the stroke at its foot may be the
  flag of the 7 on the next line). Labelled `Q` in the transcription and the alignment: a figure with no value in the
  key; t by sense only, tag `g=t` kept ({probable}). A possible second Q at L24 s9 is not checked.

Counts after sheet C (`python3 tools/R4936_count728.py`):

| | sure | {probable} | [restored] | <unresolved> | sure share |
|---|---|---|---|---|---|
| human places only (AI = probable) | **239** | 98 | 1 | 3 | **0.701** |
| AI places counted as sure | 312 | 25 | 1 | 3 | 0.915 |
