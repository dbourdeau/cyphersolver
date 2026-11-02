# Vetting brief (applies to every batch)
Repo worktree: C:\Users\dbour\cypher-leads (do NOT use C:\Users\dbour\cypher). Read first: docs/_check_catalogue.py docstring
(the vetting block), README "Catalogue vetting bar", research/latam_vetting/vet_1500.json (a worked example).
Input: research/vetting_2026-10/in_NN.json (20 leads). Output: research/vetting_2026-10/out_NN.json, a JSON object
{"<id>": {vetting block}} written incrementally (rewrite the file after each lead). Do NOT edit leads.json/catalogue.json.
For each lead: (1) run `python research/archive_sweep_2026-10/known.py "<shelfmark>" "<correspondent>" ...` for duplicates and
ledger hits; (2) WebSearch/WebFetch for prior decipherment: DECODE (decode.cs.uni-...), Tomokiyo cryptiana, Lasry, editions,
literature; (3) open the record/scan link in "links" if reachable and say what you saw; (4) key check: keys held in repo/DECODE
for the same series. Block fields exactly as the docstring: date "2026-10-29", by "claude vetting batch NN", seen{kind,where,extent,cipher},
prior_art{decode,tomokiyo,lasry,edition,literature}, key_check, duplicates, verdict (open|read|partly_read|duplicate|key_lookup|not_cipher),
plus "closed": reason when verdict != open. Every text field >= 12 chars and says what was searched and found. "seen.kind" is
scan/facsimile/transcription only if you really looked; else "not online" (only valid when lead access == "archive"; then "cipher"
quotes the archive's description). If access is not "archive" and you could not see it, set verdict "not_cipher"/"duplicate"/... only
on evidence; otherwise leave the lead out of the output with {"unvetted": "reason"} so it stays a lead. Never invent findings.
Bot checks: don't solve CAPTCHAs; note the blocked source. Finish all 20, then reply with one line per id: verdict + 6 words.

## Quality rule (added after batch 04)
A block is promoted into the catalogue on your word, so do the checks per lead, not per batch: run known.py for every lead, run at
least three distinct searches per lead (series/shelfmark + decipher, correspondents + cipher, edition/calendar), and apply any key you name.
If you could not do a check, write the lead as {"unvetted": "what is missing"} rather than a thin "open". Never give not_cipher/read on a
low-resolution glance. Prefer fewer, solid blocks to twenty weak ones.

## Chrome pass (in_cNN.json -> out_cNN.json)
These leads were left unvetted because scripts were blocked. Use Claude in Chrome (mcp__claude-in-chrome__*, load via ToolSearch in ONE call; read the
chrome-browser skill first). One tab at a time, polite pace, never solve/click through a CAPTCHA (ask the user to clear it), no logins or account
creation. Read pages with get_page_text/read_page; look at the actual leaf where a viewer renders. Same block format and Quality rule; an unvetted
entry must name the blocker so it is not retried blindly.
Chrome notes (from c02): bdh-rd.bne.es redirects to bnedigital.bne.es (get_page_text empty there; use screenshots). RAH Biblioteca Digital: Anubis passes in
Chrome; get_page_text works on records; page images via "Objeto digital" then thumbnail. Gallica: direct openapi.bnf.fr IIIF image URL opens in a tab; use
pct: crops at 1600 px. In ital. 1584 canvas = folio + ~4 at the start but drifts. Do NOT navigate any existing tab you did not open (another session's tabs).
Block output format: {id: block} or {id: {"unvetted": reason}} (apply.py also accepts {"vetting": block}).
CEHM-Carso scans DO open in Chrome with no login (c03): https://www.cehm.org.mx/Buscador/VisorArchivoDigital?jzd=/janium/JZD/<FONDO>/<seg>/<seg>/<item>/<CLASS>.jzd&fn=<record id>
(e.g. /DLI/2/292/1/DLI.2.292.1.jzd&fn=112619); or click "Formato Digital" on a FichaBasica page. Zoom into cipher leaves before judging.

## Round 2 (2 Nov 2026) tools now available
VPN exit in Spain is on (PARES reachable: recipe in frame_check_2026-10/BRIEF.md, 3 s between requests, stop at first 429). DECODE cookie works:
python C:\Users\dbour\cypher-leads\research\frame_check_2026-10\decode_fetch.py <record> <scratch dir>\decode\r<record> (images are copyright: scratchpad only; some records use
.png/.jpeg/.pdf names the helper misses, fetch by hand with the same cookie). CEHM-Carso scans open in Chrome (viewer URL pattern above). Hungaricana renders in Chrome.
Academia Sinica: homepage reachable on the VPN; images need a reader account: do not create one; record the blocker. Output file names: out_<batch>.json for in_<batch>.json (e.g. in_n01 -> out_n01).
Block format: {id: block} or {id: {"unvetted": reason}}. Cover every id. The first-pass lessons apply: do >=3 searches per lead you vet, view the ciphertext yourself for "open", never infer.

## Legacy catalogue entries (in_LNN.json -> out_LNN.json)
These entries (ids < 861) are already in the catalogue but never went through the vetting bar. Vet them the same way (block format as above). The entry's own fields
(status, prior_art, outcome, frame_check) are leads, not proof: re-check. A verdict other than open (read, partly_read, duplicate, key_lookup, not_cipher) is
the useful finding for this group: say exactly what shows it. frame_check.result "confirmed" already gives you a viewed page: reuse it in seen (kind scan) and
check prior art, keys and duplicates. Leave an entry out as {"unvetted": reason} if you cannot establish a verdict honestly.
