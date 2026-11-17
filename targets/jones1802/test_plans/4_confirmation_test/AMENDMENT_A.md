# Amendment A (15 Nov 2026, 14:50 EST, AI agent): separators. Written after R1 and R2 saved their readings
# (hashed 14:48, `work/readings.sha256`) and BEFORE any reconciliation, alignment or look-up. TEST_PLAN.md unchanged.

What prompted it: the two readers treat the writer's stops differently. R1 keeps a full stop inside an underlined
unit ("177.12,2", "22,33.37,2"); R2 writes a tight stop as a comma and a spaced stop as a group break ("396 59").
Comparing whole groups would turn every such case into a dispute that is about punctuation, not digits.

Change (mechanical, applies to R1, R2 and R3 alike):
1. Each crop's reading is reduced to its sequence of NUMBER FIELDS: split on comma, full stop and space; a doubtful
   digit keeps its first choice; a trailing comma is dropped. "177.12,2" and "177,14,2" are both three fields.
2. Reconciliation (TEST_PLAN Step 1) is done on fields: R1 and R2 fields of a crop are aligned by edit distance on
   fields; an equal field is accepted; an unequal or unpaired field is disputed; R3 reads every crop holding a
   dispute (whole crops), and its field at that place decides if it equals R1's or R2's; else the field is DOUBTFUL.
3. The reconciled field stream (crops in page order) is aligned to the maintainers' field stream (fields of
   `ct_49.txt` groups in their order) by DP: match 0; substitution = digit edit distance / max length, plus 0.5 if
   the field lengths differ; gap 1.0. Each maintainers' group is rebuilt from the blind fields aligned to its
   fields (so group boundaries are the maintainers'). A group with any doubtful or unaligned field is DOUBTFUL.
4. A merged field such as R1's "1371" against "13,71" is an ordinary field disagreement (sent to R3).
Everything else (test set, look-up, marks, control) is as in TEST_PLAN.md.

Also noted, as seen in the readers' hand-back notes (not used): R2 reads an open "L"-shaped figure as 4, R1 mostly
as 2; this is the 2/4 question itself and is left to R3 by the rule.
