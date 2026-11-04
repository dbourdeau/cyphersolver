# Leads review, 3 Nov 2026 (applies to every batch)

Goal, from Daniel Bourdeau: review every open lead and promote any with **no known prior-art decipherment, regardless of
whether a key is in the collection or has been found**. Your job is the evidence; the session applies your output.

Worktree: `C:\Users\dbour\cypher-review` (do NOT work in `C:\Users\dbour\cypher`). Read first: the docstring of
`docs/_check_catalogue.py` (the vetting block) and README "Catalogue vetting bar".
Input: `research/vetting_2026-11/in_NN.json` (up to 10 leads). Output: `research/vetting_2026-11/out_NN.json`, a JSON object
`{"<id>": block}`, rewritten after each lead so a crash loses nothing. Do NOT edit leads.json or catalogue.json, and do
not commit. Use UTF-8 (`PYTHONUTF8=1`). Do not modify any other file in the repo.

## For each lead

1. **Duplicates**: `python research/archive_sweep_2026-10/known.py "<shelfmark>" "<correspondent>" "R<decode id>" ...`. Ignore
   hits that are only this lead's own row or sweep. A hit on a catalogue entry or a target with the same document is a duplicate.
2. **Prior art**: at least three distinct web searches per lead (series or shelfmark + decipher; correspondents + cipher;
   edition or calendar). Cover the DECODE record, Tomokiyo's cryptiana, Lasry (papers and GL.htm), the printed
   edition or calendar, and the literature (HistoCrypt, Cryptologia). A calendar's "cipher undeciphered" often means the
   editor deciphered it and printed the text: open the volume where you can. "Undeciphered" in Cryptiana means no contemporary
   decipherment, not unsolved. A printed or interlinear decipherment, even a contemporary one, is prior art.
3. **See the cipher**: open the record or scan in `links`. Look at the leaf where a viewer renders it, and say what you saw.
4. **Keys**: record any key in the volume (`key_in_volume`) or held in the repo, on DECODE or in print (`key_held`), and whether it
   was tested. **A key never blocks a lead.** Use `key_lookup` only where a reading with that key is already on record.

Existing `vetting` or `vetting_note` on a lead is evidence to re-check, not a result. Leads closed `key_lookup` are in these batches
because the rule changed: if no decipherment is on record they are now `open` with the key in `key_held`, but re-check and
fill any weak field. A lead with a full block and no verdict was held back for some reason: find it, and settle the verdict.

## Per-lead work, enforced

The first pilot shared eight searches across twenty leads and pasted the same prior-art text on all of them. That proves nothing, and it was thrown away.
Each `open` block must carry `"searches": [{"query": "...", "result": "what came back for this document"}, ...]`, at least three, with queries you
actually ran for that lead, naming its correspondents, date or shelfmark. Each `prior_art` value must say what was searched and found for that document.
For a calendared or edited series (CSP, LP Henry VIII, HMC, Nuntiaturberichte, Thurloe, Ford ...), open the printed volume's text at that item if it is online: this is where
most prior decipherments sit. If an edition or calendar that would cover this item exists and you could not open it, the lead is `unvetted` naming that volume, not `open`: an unopened edition is an unanswered prior-art question. DECODE: `known.py` searches the harvested dump; state that this is what you ran.
A description that only says a letter was sent in cipher or mentions cipher does not show ciphertext survives: that is `unvetted` unless the description shows it.
Before you finish, run `python research/vetting_2026-11/check_out.py <batch>` and fix what it reports until it prints `result: pass`. Never pad a field to pass it: move the
lead to `unvetted` instead.

## Verdict

- `open`: the cipher is real, and three or more searches found no decipherment. Key status is irrelevant.
- `read` / `partly_read`: a decipherment is on the leaf, printed, or otherwise on record. Say exactly where.
- `duplicate`: name the catalogue entry, lead or target. `not_cipher`: evidence it is no cipher (shorthand, a mention of a
  cipher with no ciphertext, a keys-only item with no ciphertext). Add `closed`: reason, on every verdict other than open.
- `{"unvetted": "what is missing"}`: you could not establish a verdict honestly. Name the blocker so it is not retried blindly.

Thin or vague leads are normal. A cluster or series-level record with no identifiable cipher document should stay `unvetted`, not
`open`. A title-only record that only mentions "cipher" or "code" is `unvetted` unless the description or the leaf shows ciphertext.
Prefer a true `unvetted` over a weak `open`: each `open` goes into the catalogue on your word. Never invent findings, and never
give `not_cipher` or `read` from a low-resolution glance.

## Block format

Fields as in the docstring: `date` "2026-11-03", `by` "claude leads review batch NN", `seen` {`kind`, `where`, `extent`,
`cipher`}, `prior_art` {`decode`, `tomokiyo`, `lasry`, `edition`, `literature`}, `key_check`, optional `key_in_volume` and `key_held`,
`duplicates`, `verdict`, and `closed` when not open. Every text field is at least 12 characters and says what was searched and found.
`seen.kind` is scan, facsimile or transcription only if you really looked. Otherwise use "not online", which needs lead `access`
"archive" and a `cipher` field quoting the archive's description. If the lead has no `access` but is archive-only, add
`"lead_updates": {"access": "archive"}` beside the block's fields, and set `seen.kind` "not online" only when the description
itself shows that cipher is in the document.

## Access

Try curl or WebFetch first. Known routes: Gallica via openapi.bnf.fr IIIF; Internet Archive full text at
`archive.org/download/<id>/<id>_djvu.txt`; DECODE helper `python research/frame_check_2026-10/decode_fetch.py <record> <scratch dir>`
(images are copyright: scratch space only, never in the repo). **Do not use the browser in this batch.** If a source needs Chrome, a login or a
CAPTCHA, finish the checks you can and write `{"unvetted": "needs Chrome: <url>"}`; the session runs a Chrome pass afterwards. Known still-blocked:
Abhilekh Patal (login), Academia Sinica images (account), PARES (may give 429; stop at the first), Gale, Besançon. Do not create accounts.

Finish every id in the batch, then reply with one line per id: verdict + six words, plus a final count by verdict.

## Chrome pass (in_cNN.json -> out_cNN.json)

These leads came back `unvetted` because scripts were blocked. Use Claude in Chrome (`mcp__claude-in-chrome__*`, load via ToolSearch in ONE call, and read the `anthropic-skills:chrome-browser` skill first). This replaces the "no browser" rule above for this pass. Work in your own new tab, one tab at a time at a polite pace (a few seconds between pages), never touch a tab you did not open, and close your tab at the end. Never solve or click through a CAPTCHA, never sign in or create an account: name the blocker in `unvetted`. If a challenge page is the only thing showing, stop on that host and go on to the next lead. Read with `get_page_text`; look at the actual leaf where a viewer renders, and zoom on cipher leaves before judging. Gallica: an openapi.bnf.fr IIIF URL opens in a tab. Each row has `earlier_note`: what the first pass found, so don't repeat it, and follow any edition it names through archive.org. All other rules hold: per-lead searches, `check_out.py cNN` must pass, and `unvetted` is correct when the record still does not show ciphertext.
