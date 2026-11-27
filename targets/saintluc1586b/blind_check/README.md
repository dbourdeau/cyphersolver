# Blind shape plates of 25 Nov 2026 (f. 260r-v)

Brice Dudout answered two blind plates on the Gallica images of f. 260r (canvas 268) and f. 260v (canvas 269).
Images: Source gallica.bnf.fr / BnF. For each question he saw a strip of the line with one sign boxed in red, the same sign
enlarged, and several "shapes" (forme 1, 2, ...), each shown as one or two crops of another token of the same hand. No
labels, values, words or readings were shown. Text options: "none / other shape", "cannot tell apart", "illegible", "not a
sign", and a remark field. Each plate had 3 hidden controls (signs of known shape in sure words).

The selection rule of each plate was written and hashed before any crop was cut; the amendment (AVENANT-1) was applied
before the plate was sent, at the look-alike check of the example crops. Rules, amendments and remarks are in French.

| file | content |
|---|---|
| `plate_a_2511/REGLE-SELECTION.md` | rule of plate A: 13 questions (10 targets, 3 controls) |
| `plate_a_2511/AVENANT-1.md` | amendment before sending (one option dropped as a look-alike, two example crops replaced, boxes fixed) |
| `plate_a_2511/answer_key.json` | which shape was which label, boxes of the target and example crops, the controls |
| `plate_a_2511/reponses-saintluc1586b-2511.json` | the answers exactly as exported (25 Nov 2026 20:12 UTC) |
| `plate_b_2511b/...` | the same four files for plate B: 8 questions (5 targets, 3 controls), answered 21:49 UTC |
| `SHA256SUMS` | SHA-256 of the eight files |

The HTML plates are not included (they embed the crops). Their SHA-256: plate A
`b7ff59ad71d8fdc0855adeccc4a86fdc14adcbbfaca6cec6ef2f07465a42d45e`, plate B
`656fc8a578a3c6a97b858268d30cc77a4dd6b183f4300a2c1b6635073353d872`. Every box is in the answer keys, in pixels of the
full-size Gallica images.

## The question asked

Brackx already split-tested the multi-valued labels by shape (issues #95, #99). These plates ask another question: where
the reading needs a value that the sign's label does not have (9 read q, 3/z3 read u, z read h, P read ff), is the sign
mislabelled? The options are different signs of the table, each with a single value.

(Note added at the merge of PR #992: not every option has a single value. `z` is u / v / h / m in the key, so at the four
`z` places the plate settles the shape and u is chosen among the four values by sense, as elsewhere in this reading. The
count stands. The plate A rule says the same and is hashed, so it is left as filed. See `label_corrections.md`.)

## Plate A (13 questions)

Controls: 3 of 3 as expected. Results:
- ʒ at v. 20 r42, r46, v. 23 r32, v. 24 r47 (labelled 3/z3) matched `z`, so u: *leuee*, *du*, *guerre*, *uos* read.
- r. 1 r7 matched `zc` (h): *hier* read.
- The three places 9 read q (r. 23 r3, v. 13 r14, v. 26 r18): "none / other shape" each time, remark "a q with 2 bars".
- The two places P read ff (v. 25 r2, v. 27 r2): "none / other shape", remark "a stem with a triangular flag".

Neither described shape is in Brackx's label legend.

## Plate B (8 questions)

Same five targets, the reviewer having seen them on plate A (stated in the rule). Every plausible shape of the table was offered,
plus the two shapes he described, each shown by a token outside the targets found by template matching: the two-barred ϙ at
v. 3 r20 (labelled t2) and the flagged stem at v. 9 r2 and r35 (labelled v).

Controls: 3 of 3 as expected (q04 v, q06 ###, q07 7; remark on q07, "with a dot after it": the control's box held a dot, the
shape chosen has one value, kept). Results:
- r. 23 r3, v. 13 r14, v. 26 r18: the two-barred ϙ, 3 of 3. On q01 the remark says one distractor (forme 1, the `tt` crops) showed
  two different signs; the shape chosen gives a single value, so the answer is kept.
- v. 25 r2, v. 27 r2: the flagged stem, 2 of 2.

So both shapes are stable, distinct signs. Proposed labels: `Q2B` = q (r. 23 r3, v. 13 r14, v. 26 r18, v. 3 r20) and `FF` = ff
(v. 25 r2, v. 27 r2, v. 9 r2, v. 9 r35). The values come from the sense of the words alone (consequence, quand, ce qu'il,
quinse; affaires, affaire, effect, affin): Tomokiyo's table has neither shape and the f. 245 cribs do not use them. These words
therefore stay doubtful (`[?word]`); v. 3 *[?quinse]* and v. 9 *[?effect]* are added as doubtful words. Read shares unchanged:
f. 260r 0.764, f. 260v 0.866 (v10). Both pages stay decoded, not read.

Not on a plate: v. 9 r14 (labelled 9) looks like a ϙ with a bar; with q it would give *reuocque* (v. 9, "ont reuocque tous leurs
passeports"?). Left as it is.
