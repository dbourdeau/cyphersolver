# Pre-registration: newcastle1729, the unread sibling clear pages and the 15 open code groups

Written 11 Nov 2026 by Andrew Beling (with AI agents), before any script, score or value proposal file exists.
What had been done before writing this: the page lists of HDL objects 60924 (mssBLA 188), 60914 (4 Aug 1729) and
60966 (mssBLA 187) were fetched, and the unread pages were looked at as whole-page images (60915, 60916, 60921,
60922; 60903-60906, 60910-60912; 60961, 60962, 60964). The bracketed passages of the 4 Aug clear text (60903-60904)
were read at full resolution. No scoring had been done.

## What the page survey found (stated before any test)
- No unread page carries new code groups with glosses. 60916 is the clear covering letter of 29 June 1729 (to
  Townshend); the code strip at its right edge is the left edge of the next leaf, 60917, already transcribed.
  60910 is show-through of 60909; 60911, 60912, 60922, 60964 are blank or backs; 60905 and 60921 are an endorsement
  and a covering note; 60961-60962 are the clear 23 June letter, with no brackets and no code groups.
- **60903-60904 is the clear text of the coded 4 Aug letter**: the passages that are in code on 60907-60908 are
  written out in clear and set in square brackets. This plaintext is not used anywhere in the repo.
- None of the report's 15 open groups (805, 6, 1210, 689, 460, 285, 214, 711, 1118, 1052, 726, 836, 585, 1152, 222)
  occurs in any sibling transcription, glossed or not.

So **there are no held-out glossed occurrences of the open groups**. Their values cannot be tested; the work on them
is a value-finding exercise, and every value proposed is marked [I] with its evidence. No threshold applies to them.

## Frozen inputs
- `codetable.tsv` at origin/main 4337f026, sha256 bbca1e3eef4978f5444bb7c32ca46bd2ae088fcab8c0a772ced46452ebb75525.
- `transcription/sib*.txt` and `report_61005*.txt` at the same commit (hashes in `results/frozen_inputs.sha256`).
- This folder's `transcription/clear_4aug_brackets.tsv` (the bracketed clear passages, paired with the code lines),
  hashed before `scripts/check_4aug.py` exists.

## The one test: the code table against the 4 Aug clear text (a held-out check of the key, not of the open groups)
- Table: rebuilt by `scripts/check_4aug.py` from every `sib*.txt` **except the three `sib4aug_*` files**, with the
  repo's rule (most common firm gloss per group; `_` = null). The 4 Aug glosses are not read; only the 4 Aug group
  numbers are.
- Material: every code line of 60907-60908 paired with a bracketed clear passage of 60903-60904 (15 brackets, 14
  units after joining the two brackets that share line 60907 L18). 60909 has no clear parallel and is not used.
- Normalisation of both sides: lower case, accents dropped, ç = c, j = i, v = u, y = i, z = s, only letters kept.
- Score: for each unit, a dynamic-programming alignment of the decoded token stream to the clear letters. A token
  with a table value scores 1 when it covers exactly that value; any token may instead cover 0 to 14 letters for 0
  (an unknown group or a struck group always does); nulls cover nothing. Score = matched tokens / tokens with a
  table value, over all units.
- Null: 200 tables made by permuting the reduced table's non-null values over its groups, seed 1729.
- Pass: score >= 0.85 and score minus the best shuffled score >= 0.30. One run. If fewer than 30 tokens have a value
  in the reduced table, the result is reported as "too small" whatever it scores.
- Reported alongside, not tested: the same alignment with the full frozen table (which includes the 4 Aug glosses),
  as a check of the 4 Aug gloss transcription against the clear copy.

## Value-finding on the 15 open groups (no test)
Evidence allowed, each marked: the table's alphabetical and numerical order (neighbours in `codetable.tsv`); the
report's own context; the sibling clear pages; homophone patterns in the table. Nothing is promoted to a firm value
on this evidence alone; proposals go to `results/open_group_values.md` as [I].
