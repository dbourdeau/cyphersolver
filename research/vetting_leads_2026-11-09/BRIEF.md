# Leads still unvetted, pass of 9 Nov 2026 (applies to every batch)

`research/leads.json` holds 287 leads with no verdict. This pass takes the ones whose earlier note records a partial check
that never reached a verdict, and the few never vetted. Your job is the evidence; the session applies your output.

The method, verdicts, block format, "Per-lead work, enforced" and access rules are those of
`research/vetting_2026-11/BRIEF.md`; read it and the docstring of `docs/_check_catalogue.py` first. What differs here:

- Work in `C:\Users\dbour\cypher` (the DECODE dump and the target folders `known.py` searches are only there). Write
  **only** your output file `research/vetting_leads_2026-11-09/out_NN.json` and scratch files in the scratch directory you
  are given. Do not edit `leads.json` or `catalogue.json`, do not run the site build, do not commit or run any git command
  that changes the tree. `by` is "claude leads vetting 9 Nov NN", `date` "2026-11-09".
- Input `in_NN.json` (up to 10 leads). Output `out_NN.json`: `{"<id>": block}`, rewritten after each lead.
- The lead's `vetting_note` says what earlier passes saw and where they stopped. It is evidence to re-check, and it often
  names the missing step (an edition not opened, a volume to read, a key to compare). Do that step.
- **The unvetted rule stands.** A cluster or series-level record with no identifiable cipher document, a title that only
  mentions a cipher, an edition or a parallel decipherment series that would cover the item and could not be opened:
  `{"unvetted": "what is missing and where to look"}`. Prefer a true `unvetted` to a weak `open`; do not pad. If this pass
  finds the blocker is only Chrome, a login or a CAPTCHA, write `{"unvetted": "needs Chrome: <url>"}`; no browser tools here.
- A verdict `read` or `partly_read` needs the decipherment *seen* (on the leaf, in a printed edition you opened, in a
  target folder's NOTES) and `closed` saying exactly where. An editor's summary or a citation is not a decipherment.
- A lead may reach `open` only with the cipher seen on a scan, facsimile or printed transcription, or, for an archive-only
  lead (`access: archive`), the archive's own description quoted and an edition/calendar that would cover it opened.
- DECODE images are copyright: scratch space only, never in the repo.

Before finishing, run `PYTHONUTF8=1 python research/vetting_leads_2026-11-09/check_out.py NN` until it prints
`result: pass`. Reply with one line per id (verdict + six words), the count by verdict, the last line of check_out's
output, and any caveat to know before applying an `open` (not seen, edition unopened).
