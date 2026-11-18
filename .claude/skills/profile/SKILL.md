---
name: profile
description: Create or update a target's profile.json, the fixed-field record of the cipher system, the ciphertexts, what the model was given, the solution steps and the outcome, used for the LLM-performance paper with George Lasry. Use when starting a new target, after each solution step, when a target is finished (the writeup skill calls it), when `docs/_check_profile.py --audit` lists a target as missing, or when the user says "profile it". Argument is the target's folder name, e.g. /profile toledo1565.
argument-hint: <folder>
---

# Profile a target

Target: `$ARGUMENTS`. The file is `targets/<folder>/profile.json`, shaped by `profile.schema.json` at the repository
root. Read the schema's descriptions before filling a field you have not filled before. Worked examples:
`targets/toledo1565/profile.json` (read, crib attack), `targets/bordeaux/profile.json` (read with an archive key after a failed
solver), `targets/orpo1942/profile.json` (not read, two documents).

The profile is data for a paper on how well LLMs attack historical ciphers. Every field must be something a
reader could check against the folder. Rules:

1. **Source every value from the folder.** Read `NOTES.md`, the key files, the ciphertext and transcription files,
   and `git log --format='%ad %s %(trailers:key=Co-Authored-By,valueonly)' --date=short -- targets/<folder>/ targets/<folder>/` for dates (the second path covers history from before the targets/ move),
   sessions and model ids. Do not fill a field from general knowledge of the cipher.
2. **Measure counts, do not copy them.** Run
   `python docs/_check_profile.py --measure targets/<folder>/<file>` with `--digits`, `--width N`, `--letters` or
   `--drop-first` as the file needs, and put the result in `documents[].length` with `"measured": true` and
   `"file"`. If the measured count differs from the NOTES, keep the measured one and say why in
   `transcription.notes`. A count taken from NOTES or a source gets `"measured": false`.
3. **Write "unknown" rather than guess.** Any field may be `"unknown"`. A guessed value is worse than a gap,
   because the analysis cannot tell them apart. Required fields are never omitted.
4. **One document entry per ciphertext unit** (a letter, a message, or a set under one key that was attacked as
   one). Documents that the project never had in hand do not get an entry.
5. **Prior solution is the contamination field.** Record whether a reading existed anywhere before this project
   read it (archive decipherment, print, online), when it was found relative to the attempt, and whether the
   reading used it. Check NOTES' prior-work section and the README row.
6. **Solution steps in order, failures included.** One step per distinct move: access, transcription,
   statistics, hypothesis, crib, solver, control, sibling key, key from source, prediction, reading,
   verification, literature search. Dates where the notes or git give them. Steps of kind solver, hypothesis
   and crib carry `technique`, a list from the schema (simulated annealing, hill climbing, EM alignment,
   beam/DP decoding, SAT/constraint solving, exhaustive search, crib testing, key-structure hypothesis, frequency
   analysis, repeat/pattern analysis, language-model scoring, key matching, plaintext matching, contextual
   inference, statistical test, manual reconstruction, automated search (unspecified)): name what the step actually
   ran, so the paper can say which techniques the model used (Lasry, Oct 2026).
7. **Outcome** uses one fixed class. `fraction_read` is the share of enciphered tokens given a value; count it
   from the reading file when there is one, otherwise "unknown". `grades` counts H/C/M/I readings only when the
   reading marks them. Set `fraction_read_method` ("measured" or "estimated") and `fraction_read_source` (file and
   unit: cipher tokens, with unread marks such as [..] or ? counted as unread). Set `outcome.key` (recovered / partial
   / none), the state of the key apart from the text; `outcome.codes_open` ({open, total, tokens_open}) for code
   groups without a value; and `documents[].read` for each document. The class follows the read bar in README
   Conventions. A text entry's `read_share` counts holes by words: `[...]` is one unread word, `[... n]` is n (the least number the decode shows where it is an estimate)
   (README Conventions, "Holes are counted by words", 14 Nov 2026). When a complete key over a noisy transcription gives values that do not read as sense, add
   `fraction_coherent` (share of text that reads) so `fraction_read` does not overstate the result. For `read in part`, `fraction_read` is required and `gaps` lists every unread piece with
   its blocker (`no-key-material`, `too-short`, `illegible`, `needs-physical-access`, `open-codes`), copied from
   the `## Remaining gaps` section of NOTES.md (writeup skill, section 0a). The write-up checker rejects a partial
   outcome without them.

7a. **Full texts.** For "read" and "read in part", fill `outcome.texts` (per document: transcription file,
   decryption file, optional translation, a short `summary` of contents and context) and `outcome.key_file` when the
   key was recovered, extended or corrected (`docs/_texts.py`; the writeup skill, section 0). Paths are relative to
   the target folder.
8. **Statistical validation.** A reading whose key the project recovered (`outcome.method` "key recovered ...")
   is checked against chance and overfitting: write `validation.tsv` (cipher token TAB reading, one per line;
   format in `docs/_validate.py`), then `python docs/_validate.py <folder> --write`. It records
   `outcome.validation`, a verification step, and "statistical test" in `outcome.verification` on a pass. Where the
   test cannot run (transposition, no token alignment, non-alphabetic plaintext) record why with
   `--na "reason"`. Never edit the reading to make it pass; a weak or fail verdict is a finding.

9. **Credits and provenance.** `outcome.credits` names everyone outside the project who contributed, one item per
   person and role: `{"who": <contributors.json id>, "role": ..., "note", "date", "source", "published"}`. Roles:
   solution, new cipher, new cipher with solution, verification (George Lasry's four kinds of contribution), key or
   decipherment used (whose key, table, decipherment or edition was applied; `contemporary` for one made at the time,
   `decode` for an unattributed DECODE key), prior solution (`published: false` when unpublished), key corrected,
   transcription, identification, pointer (pointed to a key, source, crib or error the work used). Add a new person
   to `contributors.json` first; the checker rejects an unknown id. Do not credit the project, a catalogue that only
   listed the target, or an archive that only holds the images. `outcome.provenance`: `contributed` when an outside
   contributor produced the result and the project only checked it, `mixed` when one extended the other, omitted for
   the project's own work. `contributed` results are left out of the paper data. From 13 Oct 2026 a target whose
   method applied an existing key or decipherment must credit its owner (`_check_profile.py`). An outside check of
   the reading adds a `verification` credit and "independent verification" to `outcome.verification`. Never credit
   the withheld fr. 3029 / fr. 3092 targets.

Keep `system.summary` to one sentence. Put prose in the `notes` fields, and keep those short: NOTES.md stays
the narrative.

## While a target is in progress

Create the profile on the first session with what is known (documents, system as far as established,
conditions). Append a solution step when each move ends, whether it worked or not. That record is the one the
paper needs, and it cannot be rebuilt accurately afterwards.

## Check

```
python docs/_check_profile.py <folder>
```

It must print `result: valid`. Unknown fields are listed as gaps and are allowed. Then
`python docs/_export_profiles.py` should include the target without a skip line. Stage `targets/<folder>/profile.json`
by explicit path.
