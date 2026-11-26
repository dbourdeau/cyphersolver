# NOTE · catalogue 698 · stage A and stage B, scored against the key strip · v1-M · 17 Nov 2026

*Provenance:*
- *The model's words throughout (M). J.'s verbatim words: none; this note quotes him nowhere. His rulings are named by the plan that holds them.*
- *Model on record: `claude-opus-5-5` (the third cipher chat, session `eea13873`), read from the log. It ran stage A, read the strip's letters, made the strip file, ran the checks and wrote this note.*
- *Not seen by the desk.*
- *J.'s acts: the rulings of the sealed plan v7-M (SHA-256 `fc31c799…1d73a`), and bringing the desk's order file and tile script.*

## Result
**Stage A missed.**
- The Spanish key passed its bar: its score beat every one of 1,000 null copies, p = 0.0010. The strip refused it.
- German (p = 0.0460) and English (p = 0.0030) did not pass their bars.
- **The strip gives two classes with a sure match and a sure letter:** class 4 is u and class X is x. The Spanish key has 4 = n and X = m, so k = 0 of 2.
- With n = 2, below the plan's floor of 5, no language could hit whatever its score (§8 step 8). That was fixed in the chain (entry 277) before any results file was opened.

**Stage B cannot pass with two strip signs, and did not:** p = 0.5, the smallest possible. It needs seven signs or more (§10).

## Weaknesses first
1. **The strip check rests on two pairs.** At n = 2 the strip could not confirm a key; it could only refuse one. The Spanish key fails on both pairs, but two pairs are a thin refusal: a key could be wrong on these two and right elsewhere.

   With the doubtful pairs added (reported only; decides nothing), Spanish agrees on 2 of 8, on classes 2 (i) and Z (y). Of the 1,000 Spanish null keys, 104 agree on 1 of the 2 sure pairs. With the doubtful pairs, the most any null key reaches, in any language, is 4 of 8. German and English agree on 0 of 8.
2. **The strip went thin at the match, not at the letters.**
   - Six tiles were matched sure.
   - Three of them fell out, because a doubtful match put the same class on a tile with a different letter: classes Q, R and T. The sealed rule drops a class whole on any such conflict.
   - A fourth, class E, has a doubtful letter at its place: j, read partly from the alphabet's order.
   - Only classes 4 and X survive.
3. **The letters** (note of 20:56Z, chain entry 276):
   - 9 sure, 14 doubtful and 4 not read;
   - one reader, at the frame's poor resolution;
   - the doubtful letters rest partly on the order of the alphabet along the strip.
4. **A pass on the bar shows that the message scores better than shuffled copies of itself under this model. It does not show that the key is right.** The Spanish decode is strings with a Spanish look and no sentence, such as "estodoq ueser" and "ondeasillo" (M; not evidence).
5. **The results files' names carry `_v1`,** as §15 item 1 wrote them. §15 item 4 names them without it. The checks were run on the files item 1 made, each checked against its SHA-256 in the chain. Printed; no effect.
6. **Stage B could not pass with this strip, and the plan said so beforehand** (§10, "7 signs or more"). It ran because §15 item 5 says it runs if stage A misses. It is read here as missed by having no hit; "missed" is read as "no hit".

## Results

| Language | Score (message) | Null scores, min / median / max | Copies at or above | p | Bar | n | k | Null k, max | Strip | Hit |
|---|---|---|---|---|---|---|---|---|---|---|
| Spanish | −278,934 | −341,213 / −313,683 / −285,547 | 0 | 0.0010 | pass | 2 | 0 | 1 | no | no |
| German | −300,894 | −334,780 / −313,581 / −288,806 | 45 | 0.0460 | no | 2 | 0 | 1 | no | no |
| English | −284,205 | −322,264 / −302,753 / −283,636 | 2 | 0.0030 | no | 2 | 0 | 1 | no | no |

| Class | The strip (sure) | Spanish key | German key | English key |
|---|---|---|---|---|
| 4 | u | n | b | c |
| X | x | m | f | l |

**Stage B** (letter table, decode first):
- 2 signs on the strip and 8 letters decoded.
- 2 re-pairings, all listed; p = 0.5; it cannot pass.
- Reported only: word coverage p = 1.0, and the German and English tables p = 0.5 each.

## Forecasts (§11; a calibration record, not evidence)

| Forecast | P | Came | Brier |
|---|---|---|---|
| Stage A hits (bar and strip) | 0.05 | no | 0.0025 |
| Stage A passes its bar but fails the strip | 0.30 | yes | 0.4900 |
| The strip gives five or more legible pairs | 0.75 | **no: missed** | 0.5625 |
| The strip gives seven or more classes of reading v3, surely matched | 0.50 | **no: missed** | 0.2500 |
| Stage B passes its bar, given that stage A missed | 0.25 | no | 0.0625 |

- **Five scored; mean Brier 0.2735.** Two misses at 0.50 or more print at full weight.
- **"Legible pairs" is scored as the pairs of the strip file.** That reading was set down in the reading note of 20:56Z, before the strip file was made, and it agrees with draft v2, where "five legible pairs" meant n ≥ 5. Read instead as places whose letter is sure, 9, it would have come.
- **The class forecast is a miss on any count:** 6 classes were matched sure, 2 survive.
- **Four are still open:**
  - the plaintext's language;
  - the Bureau's text on the roll;
  - a long word in the words file;
  - the word rule.

## What the plan opens next, in order
1. **After the bar** (§10), two things may follow. Both are stamped before the words file opens:
   - a re-reading of both frames against the strip's shapes, marked "not blind", deciding nothing;
   - graded fills.
2. **The desk's file of the Bureau's words** (SHA-256 `60d507b9…a1ee879`). Then `bureau_check_v2.py` for stage A in three languages and for stage B (§15 item 6).
3. **Once the word rule's output is stamped,** the other quarantined sources (§5).

## Model hypotheses, tagged M
- **M1.** The strip is the message's key, and the tile match is where it failed. The doubtful pairs disagree with the Spanish key on 6 of 8 classes. That does not say which of the two is wrong.
- **M2.** A re-reading of the message against the strip's shapes, with the letters in view, is the likeliest route to a reading. Under §10 it is not blind and cannot be evidence; only the word rule can then be.
