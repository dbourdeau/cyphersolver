# Sweep and vetting brief (13 Nov 2026, cloud session) - applies to every agent of this pass

You work in `/home/user/cyphersolver` (Linux cloud container, a different network from the earlier sweeps, so a host
recorded as blocked may answer here and the reverse). Other agents share this tree: write **only** inside your own folder
`research/sweep_2026-11-13_<name>/` and the scratch directory you are given. Never edit `catalogue.json`,
`research/leads.json`, `research/archive_sweep_2026-10/merge.py`, `docs/` or any other folder; never run a git command that
changes the tree; never run the site build. Images and downloads go to scratch only (copyright), never the repo.

Read first: `research/archive_sweep_2026-10/BRIEF.md` (what counts, the row schema), `research/vetting_2026-11/BRIEF.md`
(the vetting method and block format, "Per-lead work, enforced"), the docstring of `docs/_check_catalogue.py`, and the
rows of `research/COVERAGE.md` and the sweep READMEs for your area so you do not repeat them.

## Goal

Find enciphered letters and documents (ideally before 1800, up to 1950 accepted) that are not read and not in the project,
in the part of the coverage list you were given, **and vet each good find in the same pass** so it can be promoted.

## Output, in your folder

- `candidates.json`: a JSON list (`[]` is a valid result), rewritten after every find. Row schema and vocabularies as in
  `research/archive_sweep_2026-10/BRIEF.md` (required keys: year (int), date, title, correspondents, place, language,
  region, period, shelfmark, folio_note, cls A/B/C, status, why, importance/solvability/difficulty 1-5 ints, score_note,
  verify, links [{label, href}], seen, source, prior_art, needs_archive_scan yes/no/partly/unknown, access_note).
  The shelfmark must be real and citable, with a record link.
- A row you could vet carries a `vetting` block (fields in the `_check_catalogue.py` docstring; `date` "2026-11-13", `by`
  "claude cloud sweep 13 Nov <name>") with verdict `open`, plus `"searches": [{"query", "result"}, ...]` inside the block:
  at least three searches actually run for that document. `seen.kind` is scan / facsimile / transcription only if you
  looked at the ciphertext yourself (download the page image to scratch and Read it; say what you saw: symbols, digits,
  how many lines, no interlinear decipherment). For an item with no images online use `seen.kind` "not online" with
  `needs_archive_scan` "yes", and `seen.cipher` must quote the archive's own description showing that ciphertext is in
  the document (not just that a letter "mentions" or "was sent in" cipher).
- Each `prior_art` value (decode, tomokiyo, lasry, edition, literature) says what was searched and found for that
  document; never paste the same text on several rows. If a printed edition or calendar would cover the item, open it
  (archive.org full text: `archive.org/download/<id>/<id>_djvu.txt`); an edition you could not open means no vetting
  block (leave the row as a lead and say so in `verify`). Prefer no block to a weak `open`; never invent a finding.
- Key-only items go in `key_leads.json`, not candidates.
- `README.md`: routes that worked or were blocked from this network, terms run with hit counts, what was excluded and why,
  what remains. Keep your scripts in the folder.

## Tools and routes here

- Dedup: `python3 research/archive_sweep_2026-10/known.py "<shelfmark>" "<correspondent>" ...` on every candidate.
  **The DECODE dump is not in this checkout** (git-ignored), so known.py does not cover DECODE here: search DECODE yourself
  at `https://de-crypt.org/decrypt-web/RecordsList` (answers curl) or by web search, and say in `prior_art.decode` what you ran.
- WebSearch and WebFetch are available (load with ToolSearch `select:WebSearch,WebFetch`). curl works through the
  container proxy; use a browser User-Agent. Tomokiyo: `cryptiana.web.fc2.com` answers curl. The repo copy `unsolved.htm`
  is Tomokiyo's list.
- A headless Chromium with Playwright is installed (`require('playwright')` in node, `chromium.launch()` with no options)
  for JavaScript-only pages. It is not the user's Chrome: never use it to get round a CAPTCHA, Cloudflare/Anubis
  challenge or login; if one shows, note the host as blocked and move on.
- Gallica: `gallica.bnf.fr` is 403 here; use `https://openapi.bnf.fr/iiif/image/v3/ark:/12148/<ark>/f<N>/full/800,/0/default.jpg`
  and the IIIF presentation manifest on openapi.bnf.fr.
- Reachable at the start of this session (11 Nov): archive.org, digitarq, sok.riksarkivet.se, nationaalarchief.nl,
  catalog.archives.gov, discovery.nationalarchives.gov.uk, digi.vatlib.it, alvin-portal.org, finna.fi, abhilekh-patal.in,
  jacar, archieven.nl, DDB, archivportal-d, rigsarkivet.dk, francearchives, adatbazisokonline.mnl.gov.hu, kalliope,
  digital.onb.ac.at, de-crypt.org. Blocked here: gallica.bnf.fr (403), PARES, Hispana, BVPB (429), hungaricana (403),
  NLS, NLW, manuscripta.at, Lambeth, LAC, HathiTrust, archivesportaleurope, europeana, qdl (403), calames (reset).
- Polite rate: one request per 2-3 s per host; stop on a host at its first 429/403 and note it.
- To judge page images cheaply, build contact sheets (PIL is available, or `pip install pillow`) and Read the sheet;
  open single leaves at 800-1200 px before saying cipher is there.

## Final reply (under 250 words)

Rows written (count, how many with a complete `open` vetting block, the three best with shelfmarks), routes that worked
or were blocked, what is left. Your reply is read by the coordinating session, not the user.

## Added on 13 Nov 2026

- Stop by **17:30 UTC** (check `date -u`); finish the lead you are on, write your README, and report. Rewrite `candidates.json` after every find.
- Today's date for `vetting.date` and `seen` is 2026-11-13. Do not use vetting `by` strings of earlier passes.
- Already in the catalogue or leads (do not re-find): run `known.py` on every candidate. Medici letters 2554-2563 are held leads; MAP LXXII 190-192 is lead/catalogue 2351; Galt (TKUA B.84, images 549/587/609) is lead 2552.
- A glossed cipher (plaintext between the lines, in the margin, or over the groups) is read: not a lead. Only bare ciphertext with no decipherment is a lead. Open the leaf at native size before saying bare.
- Unopened printed editions mean no vetting block: leave the row a lead and name the volume in `verify`.
- Report format: ids/rows found, with verdict and six words each; what you covered and what remains.
