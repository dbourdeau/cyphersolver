# Third vetting pass, 6 Nov 2026 (batches in_tNN.json, 8 leads each)

Read `research/vetting_2026-11/BRIEF.md` first: its rules, block format, `check_out.py` and the "never pad a field" rule apply unchanged,
with these changes.

- **Worktree**: work in `C:\Users\dbour\cypher-promote` (a fresh checkout of main), not `cypher-review`. Input
  `research/vetting_2026-11/in_tNN.json`, output `research/vetting_2026-11/out_tNN.json` (rewrite after each lead). Do not edit
  `leads.json` or `catalogue.json`, do not commit or stage, do not touch any other file.
- **Each lead carries `prior_unvetted`**: why the earlier passes (3 Nov and 6 Nov) left it unvetted. Your job is to remove that
  specific blocker: open the named edition or calendar (archive.org full text, Google Books, HathiTrust full view, a library PDF),
  find another route to the leaf, or settle the question the note leaves open. If the blocker still stands after a real attempt,
  keep `{"unvetted": "..."}` and say what you tried this time and what would unblock it. Do not repeat the old note.
- **Aggregates**: a series- or cluster-level record that names no single document stays `unvetted`; do not invent a document.
- **Promotable means** the checker's `open` bar: ciphertext seen (or an archive description that itself shows ciphertext survives,
  `seen.kind` "not online" with lead `access` "archive"), at least three searches made for that lead, no decipherment on record
  (printed, interlinear, in the leaf, or in an edition). A printed or interlinear decipherment makes it `read`/`partly_read`.
- **No browser** in this pass, except where noted for a single lead; if a lead needs Chrome, a login or a CAPTCHA, leave it
  `unvetted: needs Chrome: <url>`. Never create accounts. Never solve CAPTCHAs.
- Finish with `python research/vetting_2026-11/check_out.py nNN` and fix until `result: pass`.
- Final reply: one line per id (verdict + six words) and counts by verdict.
