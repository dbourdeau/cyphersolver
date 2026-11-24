# Brief 2: mark the unmarked words and correct the page, for the targets you examined

You examined these targets under `TARGET_BRIEF.md` and reported. This is the repair that was held back. Do it
only for YOUR targets, and only where your report found (a) words that depart from the key with no mark, or
(b) a statement on the write-up page that is false. If neither applies to a target, do nothing for it and say so.

## A. Mark, do not rewrite

1. In the published reading file(s), mark every place you reported as an unmarked departure, in **that file's own
   convention** as its header states it (for most: `[ ]` round the letters, or the whole word, that the key does
   not give; some files use `{x/y}`, `°`, `‹ ›` or italics: follow the file). If the file has no convention, use
   `[ ]` and add one line to its header saying so.
   - **Do not change, add or remove a single letter of the text.** Only marks. If you believe the reading is wrong
     and the key's word is right, still only mark it, and say so in NOTES.
   - Mark only what you verified yourself against the key output. Where your count was an estimate by alignment
     (you reported "about N"), either verify each place now, or mark the ones you verify and state exactly how
     many remain unverified and unmarked. Do not mark by guess and do not claim completeness you do not have.
   - If a companion file already holds the marks (a `*_marked.*` file), do not duplicate them by hand: point
     `outcome.texts[].reading` at the marked file if it is the same text, and say so.
2. Where the published text is **another person's or another source's text** (a contemporary gloss or clear copy,
   an edition, a contributor's reading kept as theirs), do not mark inside it. Make sure its header says in one
   line what it is and that it is not the output of the key, and name the file that is (the mechanical decrypt),
   if the folder has one.
3. Correct any header line in a reading or decryption file that your findings make false (for example "letters as
   the key gives them"), in the plainest wording that is true.
4. Unstated spelling conventions (modernised spelling, added diacritics, expanded titles): state them in one
   header line. Do not mark each word.

## B. The page

5. In `docs/<slug>.html`, correct each false statement you quoted in your report, with the smallest change that
   makes it true, taken from NOTES and the files. Change nothing else. Do not touch anything between a
   `<!-- name:start -->` and `<!-- name:end -->` comment pair (generated blocks), the `<head>`, navigation or
   scripts. Keep entities and markup valid. If a statement cannot be made true in a sentence, cut it.
   If a count on the page changes because of your marks (words read, percentage), do not recompute it yourself:
   list it under `page_counts_now_stale` in your report.

## C. Record and measure

6. Extend your `## Decrypt audit, 16 Nov 2026` section in `NOTES.md` with a paragraph "Marked on 16 Nov 2026":
   how many places were marked in which file, what was left unmarked and why, which header lines changed.
7. For each reading file you marked, run
   `python3 research/reading_audit/v2_score.py <path to the reading file> <language code>` before (use
   `git show HEAD:<path>` into a scratch file) and after, and note the hole rate. Do **not** change `read_share`,
   `state` or `class` in `profile.json`; report the figures.
8. Append one step to `profile.json` `solution` as before (`kind`: "verification"), keeping the file's existing
   formatting as far as you can (if a full re-dump would reformat the file, insert the step textually instead).
   `python3 docs/_check_profile.py <folder>` must print `result: valid`.
9. Same limits as before: only your own target folders and their own `docs/<slug>.html`; no commits, no network,
   no existing target scripts, no other files under `docs/`.

## Report

Write `/tmp/claude-0/-home-user-cyphersolver/76f0b7a4-c1c5-55a3-8d79-a23ef7d005dc/scratchpad/targets_out2/<folder>.json`:

```json
{"folder": "...", "marked": [{"file": "...", "places": 0}], "left_unmarked": {"count": 0, "why": "..."},
 "headers_changed": ["file: old -> new"], "page_changes": ["old -> new"], "page_counts_now_stale": ["quote"],
 "hole_rate": [{"file": "...", "before": 0.0, "after": 0.0, "state_in_profile": "read | read in part | ..."}],
 "falls_below_read_bar": false, "wording_changed": false, "notes": "anything that needs a decision"}
```

`wording_changed` must be false. Then answer in at most 80 words per target.
