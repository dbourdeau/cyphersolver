# Legacy catalogue vetting, 9 Nov 2026 (applies to every batch)

The 88 catalogue entries below id 861 came in before the vetting gate (README Conventions, "Catalogue vetting bar") and
carry no `vetting` block; `python docs/_check_catalogue.py --audit` lists them. This pass gives each one the block the
gate asks of every newer entry, or finds out that it should not be in the catalogue. Your job is the evidence; the
session applies your output.

The method, the verdicts, the block format and the access routes are those of `research/vetting_2026-11/BRIEF.md`
(sections "For each lead", "Per-lead work, enforced", "Verdict", "Block format", "Access"). Read it first, with the
docstring of `docs/_check_catalogue.py`. What differs here:

- The items are **catalogue entries**, not leads. Read "lead" as "entry". `by` is "claude legacy vetting batch NN",
  `date` "2026-11-09".
- Work in `C:\Users\dbour\cypher` (the DECODE dump and the target folders that `known.py` searches are only there),
  but write **only** your output file `research/vetting_legacy_2026-11/out_NN.json` and scratch files in the scratch
  directory you are given. Do not edit `catalogue.json`, `research/leads.json` or any other file, do not run the site
  build, and do not commit or run any git command that changes the tree.
- Input: `research/vetting_legacy_2026-11/in_NN.json` (up to 10 entries). Output `out_NN.json`, a JSON object
  `{"<id>": block}`, rewritten after each entry so a crash loses nothing.
- **Duplicates**: `known.py` will hit the entry's own catalogue row and often a target folder that has worked on it
  (the entry's `status` and `outcome` say so). That is not a duplicate. Open that folder's `NOTES.md`: if it holds a
  reading of the document, the verdict is `read` or `partly_read` with `closed` naming the folder; if the folder closed
  it unread or blocked, say so in `key_check` or `duplicates` and carry on.
- Most entries were scored from a catalogue description (`seen: "catalogue"`), and 50 are `access: "archive"`. For an
  archive-only entry use `seen.kind` "not online" and quote the archive's description of the cipher in `seen.cipher`;
  if the description only mentions a cipher and does not show that ciphertext survives, write `unvetted`. Where a scan
  is online, look at the leaf and say what you saw.
- The entry's `status` text records earlier checks. It is evidence to re-check, not a result: run your own searches.
- No browser in this pass. If a source needs Chrome, a login or a CAPTCHA, write `{"unvetted": "needs Chrome: <url>"}`.
- DECODE images are copyright: scratch space only, never in the repo.

Before you finish, run `python research/vetting_legacy_2026-11/check_out.py NN` (with `PYTHONUTF8=1`) and fix what it
reports until it prints `result: pass`. Never pad a field to pass it: write `unvetted` instead.

Finish every id in the batch, then reply with one line per id: verdict + six words, plus a final count by verdict.
