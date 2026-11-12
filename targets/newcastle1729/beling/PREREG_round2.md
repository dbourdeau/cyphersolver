# Pre-registration, round 2: newcastle1729 (11 Nov 2026, evening)

Written by Andrew Beling (with AI agents) before `scripts/full_table.py` and `scripts/check_194.py` exist and before
any score in this round. [V] = seen on the image, in a catalogue or in output; [I] = inference.

## What was done before writing this
- Print search for a clear text of the report or of any coded passage (details in `README.md` section 7). **No clear
  text was found.** HMC *Polwarth* vols I-IV (archive.org full text) end in 1725 [V]. Vol. V (1725-80, 1961) is
  search-only on HathiTrust; searched inside, it has 0 hits for "Port St. Mary", "Port Saint Mary", "Marys",
  "Sainte", "cipher", "decipher", "Cadiz", "galleons", and 3 for "Pareti" [V hit counts, pages not shown]. Coxe,
  *Memoirs of the Kings of Spain* (1813) and *Memoirs of Walpole* (1798-1800) have nothing on the Port St Mary
  correspondent [V grep]. So the round-2 test of the open-group proposals against a clear text **cannot be run**.
- The Huntington page lists for mssBLA 170-195 were read [V], and the deciphered items in the same code that the
  repo has only in part were looked at. mssBLA 194 (60893-60894) is a whole code letter with an interlinear
  decipherment; Brackx (#189) listed 19 of its pairs. It was transcribed in full
  (`transcription/sib194_60893.txt`, `sib194_60894.txt`) **and in doing so its gloss for 1118 was seen**: "tain"
  (under "163 1118", "cer-tain"). This is the only glossed occurrence of any of the 15 open groups found. Because it
  was seen before this file was written, it is reported as an observation, not as a test result.
- 60917 L02, L17 (869 or 369) and L16 (880 or 830) were looked at on full-resolution crops; 60909 was placed (see
  README). None of this is scored.

## Frozen inputs (hashes in `results/frozen_inputs_round2.sha256`, taken before either script exists)
- the repo files at origin/main 4337f026 as in round 1 (`codetable.tsv`, `transcription/sib*.txt`)
- `transcription/clear_4aug_brackets.tsv`, `transcription/sib194_60893.txt`, `transcription/sib194_60894.txt`
- `results/open_group_values.md` (the round-1 proposals, unchanged; the 1118 entry there reads "toujours / très?
  weak")

## 1. One check with a shuffled control: the table against mssBLA 194 (consistency, not the open groups)
- Table: rebuilt with the repo rule (as `check_4aug.py`) from every repo `sib*.txt`, with Brackx's line
  `L194h60893` removed from `sibbrackx189.txt` (so no 194 gloss is in it).
- Material: every token of `sib194_60893.txt` and `sib194_60894.txt` with a firm gloss (no `?` on group or gloss,
  not struck, gloss not `_`) whose group has a value in that table.
- Score: share of those tokens whose gloss equals the table value after the round-1 normalisation (lower case,
  accents dropped, j=i, v=u, y=i, z=s, letters only); a gloss that begins with the table value, or a table value
  that begins with the gloss, counts as a match when the shorter has at least 3 letters (perfection/perfectionn).
- Null: 200 tables made by permuting the table's non-null values over its groups, seed 1729.
- Pass: score >= 0.80 and score minus best shuffled >= 0.30; "too small" if fewer than 30 tokens qualify.
- What it can show: that 194 is in the same code and that this transcription agrees with the table. It says nothing
  about the report's open groups.

## 2. Full construction (descriptive, no score)
`scripts/full_table.py` writes `results/full_table.tsv`: one row per group seen in any source, with
- the value (the repo rule over all glosses, the 194 transcription included),
- every gloss attestation (file:line=gloss), marked doubtful where the source marks it,
- every clear-copy attestation: the 4 Aug code lines aligned to the clear copy 60903-60904 with the full table
  (round-1 alignment); a token that covers exactly its value is "clear agrees", one that does not is "clear differs"
  with the letters the alignment gave it (approximate),
- the round-1 context proposal for the 15 open groups,
- a basis column: gloss / gloss+clear / clear only / context only, and a conflict flag where glosses disagree or the
  clear copy differs.
No value in the repo's `codetable.tsv` is changed by this; changes are proposed in `table_notes.md` only.
