# keyedit: budgeted key editing (prototype)

After Weight-Space Programming (Takehi et al., 2026): the key is the "weights", an editor reads and edits it for free,
and every language-model score costs one unit of a fixed budget. `keyedit.py` is the harness (CLI in its docstring),
`baseline.py` the greedy single-token editor, `make_pelissier_task.py` builds `pelissier_task.json`.

## Test 1 (2 Nov 2026): Pelissier 1592, pass-2 key repaired toward the pass-3 key

93 tokens, 401 cipher lines, 27 tokens wrong at the start (token-weighted accuracy 0.880). Model `fr-1600-letters`.

| editor | scores spent | accuracy |
|---|---|---|
| none (start key) | 0 | 0.880 |
| greedy swaps, most frequent token first | 25 / 100 | 0.880 / 0.880 |
| greedy swaps | 600 | 0.910 |
| LLM (Sonnet, fresh subagent, no glyph shapes, truth hidden) | 9 | 0.931 |

The LLM filled blank tokens from context ("satis?action" -> f, "?icardie" -> p) and used scores to confirm batches.
It left the big merged families untouched (X a/u, I p/l, w et, J ss), which the language model cannot separate.

Caveats: one run, one target, start errors mostly blank tokens; the truth is the project's own pass-3 key; the first
view of the start key's error list was seen by the experimenter, not by the editor. Next: repeat with 3 seeds, a
corrupted (not blank) start, and with the glyph shapes from GLYPHS.md given to the editor.

## Test 2 (2 Nov 2026): corrupted start, 3 seeds, with and without glyph shapes

Start = the test-1 start key plus 12 correct tokens (>= 15 occurrences) set to a wrong letter, seeds 1-3 (39 wrong
tokens, accuracy 0.679 / 0.684 / 0.680). Budget 25 scores. Editors are fresh Sonnet subagents, truth hidden.
A = French text and counts only. B = also `glyph_shapes.md` (GLYPHS.md shapes and families, letters removed).

| seed | start | greedy 25 | greedy 600 | LLM A | LLM B |
|---|---|---|---|---|---|
| 1 | 0.679 | 0.679 | 0.519 | 0.938 (23 scores) | 0.706 (25) |
| 2 | 0.684 | 0.684 | 0.606 | 0.913 (23) | 0.853 (24) |
| 3 | 0.680 | 0.719 | 0.825 | 0.954 (18) | 0.841 (23) |
| mean | 0.681 | 0.694 | 0.650 | 0.935 | 0.800 |

- Greedy score-chasing can lower accuracy (seed 1: 0.679 -> 0.519 at 600 scores): the LM score rewards wrong letters
  that make plausible n-grams.
- Shapes made the editor worse, not better. B editors extrapolated within look-alike families (I=l -> E=l, z as a
  "lead-in stroke" set to null) where the truth splits the family. Every A and B run left z (480 tokens, truth c)
  wrong; A runs also kept scoring z=blank best. Shape notes need to say which family members differ, not just lump.
- Remaining errors in A runs: z, m (ll vs l), Z, o., Tr, q9: polyphonic or context-conditioned tokens, which a
  one-token-one-letter key cannot represent.
- Caveats: n=3 per arm, one target, one model, truth is our own key, B/A differ in prompt length too.

## Test 3 (2 Nov 2026): second target (Soglia 1848, Italian) and Haiku vs Sonnet

Soglia 1848: Italian, 92 tokens, 396 occurrences, 2-digit table of letters and syllables; 8xxx code words fixed. Truth =
`targets/soglia1848/key.json`. Start = truth with 12 of the 28 eligible groups set to another value from the table
(seeds 1-3). Model `it-modern`. No glyph shapes (tokens are digits). Budget 25. `make_soglia_task.py` builds it.

| seed | start | greedy 25 | greedy 600 | Sonnet | Haiku |
|---|---|---|---|---|---|
| 1 | 0.480 | 0.480 | 0.399 | 0.823 (23 scores) | 0.631 (5) |
| 2 | 0.662 | 0.662 | 0.402 | 0.937 (11) | 0.871 (14) |
| 3 | 0.593 | 0.593 | 0.394 | 0.907 (15) | 0.831 (9) |
| mean | 0.578 | 0.578 | 0.398 | 0.889 | 0.778 |

- Same pattern as Pelissier: greedy never improves and loses accuracy at 600 scores; the LLM gains 0.2-0.3.
- Haiku is behind Sonnet on every seed (mean -0.11) but still far above greedy. It stopped early (5, 14, 9 scores):
  it did not spend its budget, which is part of the gap (seed 1: 4 of ~12 repairs).
- Haiku seed 3 broke the protocol: it scored candidate text offline with the `lang/` model through a helper, so its
  9 scores understate its model use. Treat that run as contaminated.
- Haiku was not run on Pelissier; Sonnet-vs-Haiku is one target, n=3.

## Test 4 (2 Nov 2026): Martinique 1778-79 (French, numeric code groups)

`make_martinique_task.py`, `sense.py` (the strict sense proxy of `targets/martinique1778/measure_sense.py`, applied to a
session key). Model `fr-modern`. Sonnet editors, budget 25, no shapes.

**Calibration** on f.123 (1779, interlinear decipherment = known key; 77 groups, 104 tokens). Start = truth with 12 groups
given another group's value.

| seed | start | greedy 25 | greedy 600 | Sonnet |
|---|---|---|---|---|
| 1 | 0.856 | 0.827 | 0.779 | 0.962 (7 scores) |
| 2 | 0.865 | 0.865 | 0.788 | 0.952 (5) |
| 3 | 0.856 | 0.856 | 0.817 | 0.904 (4) |

**Open run** on f.88 (1778, unread; 181 tokens, 109 groups; start = key_bouille + tentative, 128 tokens valued, sense proxy
62.4%). Two independent Sonnet editors (21 scores each):

| | valued tokens | sense proxy | LM score/char |
|---|---|---|---|
| start | 128 (70.7%) | 62.4% | -1.99 (editor 2's first score) |
| editor 1 | 147 (81.2%) | 75.7% | -1.74 |
| editor 2 | 160 (88.4%) | 85.6% | -1.66 |

- Independent agreement is the better evidence than the proxy, which rewards any filled group that sits inside a
  dictionary word. Editors filled 16 and 27 blanks; 10 were filled by both, 6 identically: 103=u, 619=va ("pouvant",
  "hopitaux"), 667=im, 665=pa ("d'impatience"), 531=autant, 495=minist ("ministre"). Both also changed 46 aux -> avec
  ("avec d'autant plus d'impatience"). They disagreed on 26 (cu vs gle), 260, 509, 545.
- Not verified: no outside reading exists, so these are proposed values (high confidence only for the six agreed ones).
  The number groups (568, 479, 402, 454 ...) stay unread; one editor guessed 138 = la Dominique from the date.
- Not written into targets/martinique1778 or any profile.json.

## Test 5 (3 Nov 2026): held-out check, Haiku then Sonnet, and the f.88 values re-checked

**Held-out check** (`make_martinique_heldout.py`, `heldout.py`). On the f.88 task, 15 groups with an interlinear value
(`key_bouille.tsv`) are blanked in the start key, so the editor cannot tell them from the genuinely unknown ones (23-32
tokens per seed, seeds 1-3). The grader counts exact recovery of the blanked groups, wrong fills, damage to the kept
known groups and fills of the genuinely unknown groups. `keyedit.py init` now writes `heldout.json` next to `truth.json`;
`chain.py SRC DST` starts a new session from another session's final key (fresh budget).

| editor | held-out recovered (of 45) | fills on held-out groups | wrong fills | kept groups damaged |
|---|---|---|---|---|
| Haiku, 25 scores (spent 3 / 3 / 2) | 3 | 3 | 0 | 0 |
| Haiku, then Sonnet over its key (8 / 6 / 8) | 4 | 10 | 6 | 4 (seed 1: 91, 1, 719, 819) |
| Sonnet alone (9 / 7 / 6) | 2 | 5 | 3 | 1 |

- Recovery is 2-4 of 45 blanked groups (4-9%). Fills on held-out groups are right 40% (chain) and 40% (Sonnet alone) of the
  time; the wrong ones are plausible French the LM score prefers (268 force for garnison, 636 le for au, 705 nombre/de for
  re, 815 quatre/deux for is). So a filled group with no second source is closer to a coin flip than to a reading.
- The groups held out are drawn uniformly, so they include syllables and function words with little context. The check
  measures the hard end; it does not say how good the editors are on the easy blanks of the open run.
- Sonnet over Haiku cleared a documented value (91 = x, interlinear) and changed three others: an editor told "do not
  assume earlier edits are right" also damages known groups.
- Open f.88, Haiku alone: 134 valued tokens, sense proxy 65.2% (start 62.4%). Fills 103=i, 509=re, 260=z, 412=l. A Sonnet
  pass over it changed nothing (3 scores; two guesses reverted). The two earlier Sonnet editors (75.7% and 85.6%) used a
  prompt without that warning; the difference is partly prompt, so these runs are not a clean model comparison.
- Haiku stops early (2-3 of 25 scores), confirming Test 3: cheap and safe, but it fills little.

**Re-check of the agreed f.88 values.** 46 = avec contradicts the f.31 interlinear (`pairs1779_f3_f31.txt`: 46 = aux, in
"arrivés aux [vaisseaux]"); keep aux. 103 got five different values from five editors (u, i, l, ur, y), so it is not
agreed; "hôpitaux" needs u. 619, 667, 665, 531 and 495 occur in no paired letter, so no interlinear can test them yet;
checking them needs pairing C8 A 78 f.3 (rest), f.5, f.31 (rest) and f.144 from the ANOM images (manifests load in the
browser pane: recherche-anom.culture.gouv.fr/ark:/61561/<ark>/manifest). Not done.

Caveats: 3 seeds, one letter, one language model; the truth is the project's own interlinear key.

**Update (3 Nov 2026): fills tested against new pairs.** Pairing C8 A 78 f.31 (rest), f.3, f.5 and f.144 from the images
(targets/martinique1778, `pairs1779_f3_f31_more.txt`, `pairs1779_f5_f144.txt`) gives an outside test of the f.88 fills.
Fills on groups that occur in the pairs: the two first Sonnet runs (Test 4) were right on 12 and wrong on 17; the Test 5
runs right on 1 of 20 (approximate count, `top pair value` as truth). Confirmed: 103 = u, 665 = pa, 531 = autant,
491 = an, 321 = pas, 402 = di. Refuted: 545 (it; editors gave trois/men), 195 (ni), 272 (i), 320 (mi), 412 (du), 443 (y),
454 (mille), 516 (tro), 622 (ces), 845 (ga). Of the six "agreed" values, three are confirmed (103, 665, 531); 619, 667
and 495 occur in no paired letter. 46 stays open (aux x2, avec? x2). So agreement between two Sonnet editors was a
fair, not a strong, signal: about 40% of their individual fills held, and the held-out rate (about 40%) predicted it.
