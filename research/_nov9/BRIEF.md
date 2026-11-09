# Sweep brief (9 Nov 2026) - applies to every sweep agent

Work ONLY in the git worktree `C:\Users\dbour\cypher\.worktrees\sweep-nov9` (never `C:\Users\dbour\cypher`). Windows; use Python
with `PYTHONUTF8=1`, curl, and the Write tool for files. Scratch/raw downloads go to the session scratchpad, not the repo
(image files are git-ignored copyright material anyway).

Goal: find historical enciphered letters/documents (ideally pre-1800, any date up to 1950 accepted) that are NOT yet
read/deciphered and NOT yet in the project, in an archive area no earlier sweep covered. Output = leads, not catalogue entries.

1. Before searching, read `research/COVERAGE.md` and the sweep folder READMEs relevant to your area (`ls research`), so you do
   not repeat them. Run `python research/archive_sweep_2026-10/known.py "<shelfmark>" "<correspondent>" ...` on every candidate
   (duplicates). Never edit `catalogue.json`, `research/leads.json`, or `research/archive_sweep_2026-10/merge.py`; do not git commit.
2. Create `research/sweep_2026-11_<yourname>/` with: `README.md` (routes that worked and were blocked, terms run with hit
   counts, what was excluded and why, what remains), your scripts, and `candidates.json` (a JSON list; `[]` is fine). Write
   candidates.json incrementally as you go. Do NOT pad: 0 good rows is a valid result; 5 solid rows beat 30 weak ones.
3. Row schema = `research/sweep_2026-11_czech_slovak/candidates.json` (look at 2 rows and `make_candidates.py`). Required keys
   (merge.py): year, date, title, correspondents, place, language, region (one of England, France, Italy, Spain, Portugal,
   Low Countries, Central Europe, Germany, Scandinavia, Poland-Lithuania, Papacy, Americas, Other), period (15th century,
   1497-1559, 1560-1589, 1589-1598, 1598-1610, 1611-1650, 1651-1700, 1701-1800, 1801-1900, 1901-1950, unknown), shelfmark,
   folio_note, cls (A = ciphertext seen online and unread, B = archive describes it as cipher with no decipherment, C = other
   lead), status, why, importance/solvability/difficulty (1-5), score_note, verify, links [{href,label}], seen ("scan" if you
   viewed the leaf, else "catalogue"), source, plus prior_art, needs_archive_scan ("yes" if images are not online),
   access_note. The `shelfmark` must be a real, citable one with a record link.
4. A row must be: a real letter/document with cipher (not a key-only item, not a monogram/royal "cipher", not a surname
   Ziffer, not 20th-c. telegram administration); not already decoded in a printed edition you can find (do 2-3 web searches
   per promising item: shelfmark+decipher, correspondents+cipher, the edition/calendar); and not already in the repo
   (known.py). Key-only items go in `key_leads.json` (a separate list), not candidates.json.
5. Polite rate: one request per 2-3 s per host, stop at the first 429/403 on a host and note it. Never solve or click through a
   CAPTCHA/Cloudflare check. Chrome (mcp__claude-in-chrome__*, load via ToolSearch in ONE call) only if scripts are blocked and
   only ONE tab that you create yourself; never navigate other tabs.
6. When viewing page images (to confirm cipher), download to scratchpad and Read the jpg; say in the row what you saw.
7. Final reply (under 250 words): rows written (count + the 3 best with shelfmarks), routes that worked/blocked, what is left.
