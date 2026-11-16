# Brief: explain and repair one flagged target of the decrypt audit

Repository: `/home/user/cyphersolver` (historical cipher targets, one folder per target under `targets/`).
Read `research/decrypt_audit/README.md` first (two minutes): the audit re-applies each recovered key to its
transcription and compares the result, letter by letter, with the published reading. Your targets were flagged:
the published text is not what the key file gives. On the one target examined in depth (`memoire1560`) the cause
was serious: letters changed without a mark, on top of a transcription that merged signs. Your job is to find
the cause for each of YOUR targets and to repair what is a defect of the records.

## For each of your targets

1. Run `python3 research/decrypt_audit/detail.py <folder> 30` (read-only). It prints, per text, the key file and
   tokenisation the audit used, the departures by kind, the commonest replacements, and samples
   `decrypt[gap]context | reading[gap]context` (letters folded: lower case, no accents, v=u, j=i=y).
2. Read the target's `NOTES.md`, `profile.json` (`outcome.key_file`, `outcome.texts`, `outcome.method_basis`, the
   solution steps), the key file(s), and the transcription and reading files of the flagged texts. Look for other
   key material in the folder (a working key, a script with a hard-coded table, an overrides file, a codebook).
3. Classify every kind of departure you see. The causes met so far:
   - **A. key file incomplete or stale**: the reading uses a sign value or a code value that the target's own
     work established but that the key file named in the profile does not hold (a missing homophone, a sign with
     the wrong letter, code groups resolved in a script or in NOTES but never written to the key file).
   - **B. unmarked emendation**: the key gives one letter or word, the reading prints another, and nothing in the
     reading marks it (no brackets). Includes words supplied from context and passed off as read.
   - **C. normalisation**: the reading expands abbreviations, modernises spelling or resolves a title
     ("V. M." to "vuestra magestad") by a stated or unstated convention.
   - **D. clear text or other material**: the published file interleaves passages that are in clear in the
     manuscript, or notes, headers, markers for unread groups; nothing wrong, the audit cannot tell.
   - **E. transcription and reading out of step**: the transcription file is an older or newer state than the one
     the reading was made from, or covers a different extent.
   - **F. audit artefact**: the script chose the wrong column, tokenised wrongly, or took an annotation in the key
     file ("punctuation comma", "letter") for a value.
4. Repair, within these limits:
   - **You may** complete or correct a key file, or add a second key file and list it in `profile.json`
     `outcome.key_file`, **only** with values that the target's own files establish (NOTES, a script, an alignment
     table, a cipher/clear pair in the transcription). Record where each added value comes from (a comment line or
     a source column). Never guess a value from what the reading "needs".
   - **You may** point `outcome.texts[].transcription` or `.decryption` at the right existing file when the
     profile lists the wrong one.
   - **Do not change the wording of any reading, decryption or translation file.** If you find cause B, do not
     bracket anything yourself: count the cases, list them, and report. That repair is decided centrally.
   - Do not touch anything outside `targets/<your folders>/`. Not `docs/`, not `README.md`, not `research/`, not
     another target. Do not commit, do not push, do not use the network.
   - Do not run existing scripts of the target folder (several rewrite tracked files). You may write and run your
     own read-only snippets, and `python3 docs/_check_profile.py <folder>`.
5. Run `detail.py` again and note the figures before and after ("N of M words depart").
6. Record the work in the target:
   - append to `NOTES.md` a section `## Decrypt audit, 16 Nov 2026` placed just before `## Remaining gaps` if that
     heading exists, else at the end: what the audit showed (figures), the causes with one example each, what you
     changed and from which source, the figures after, and what remains unexplained. Plain sentences, no praise,
     no speculation presented as fact. Do not change the `Status:` line.
   - append one step to `profile.json` `solution` (load with `json`, dump with `indent=1, ensure_ascii=False`, and a
     final newline): `{"date": "2026-11-16", "kind": "verification", "what": "...", "result": "worked" | "partial" | "failed"}`.
     Then `python3 docs/_check_profile.py <folder>` must print `result: valid`. If it does not, undo your profile
     change and say so.
7. Look at the write-up page `docs/<slug>.html` if it exists (slug = folder name unless NOTES says otherwise),
   read-only: does it state anything about the key or the reading that your findings make false or that was
   already false (a count of key entries, "every word read with the key", a percentage)? Quote it.

## Report

Write `/tmp/claude-0/-home-user-cyphersolver/76f0b7a4-c1c5-55a3-8d79-a23ef7d005dc/scratchpad/targets_out/<folder>.json`:

```json
{"folder": "...", "causes": {"A": "…one line with counts…", "B": "…", "C": "…", "D": "…", "E": "…", "F": "…"},
 "before": "N of M words depart (texts compared: k)", "after": "…",
 "files_changed": ["targets/<folder>/…"],
 "key_values_added": [{"sign": "…", "value": "…", "source": "file:line or NOTES section"}],
 "unmarked_emendations": {"count": 0, "examples": [{"text": "…", "decrypt": "…", "reading": "…", "where": "file:line"}]},
 "page_statements_false": ["exact quote from docs/<slug>.html — why"],
 "remaining": "what you could not explain or fix",
 "confidence": "high | medium | low"}
```

Omit a cause that does not occur. Then answer with at most 120 words per target: the main cause, what you changed,
before and after, and anything that needs a decision. Be exact about what you did not check.
