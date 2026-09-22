---
name: writeup
description: Write up a finished cipher target on the site and in every ledger, in this repository's convention. Use when a target is read, solved, explained or closed, when the Stop hook or `docs/_check_writeup.py` reports a finished target with no write-up, or when the user says "write it up". Argument is the target's folder name, e.g. /writeup gramont1529.
argument-hint: <folder or slug>
---

# Write up a finished target

A result is not finished until it is on every one of these surfaces. Concurrent sessions in this repo commit each
other's folders with `git add -A`, so the commit log never announces a solve; the only reliable signal is the
checker. Work through the list, then run `python docs/_check_writeup.py <slug>` until it prints `complete`.

Target: `$ARGUMENTS`. Read `<folder>/NOTES.md` and the reading files first; the write-up is written from the notes,
not from memory. The slug is the folder name unless a page already exists under another name (check
`python docs/_check_writeup.py --audit` and the README row's link). Never invent a second page for the same target.

## 0. Before writing

- `git status -sb`: know which branch the shared checkout is on. Other sessions switch it. If it is not `main`,
  work in your own worktree: `git worktree add <scratchpad>/wt-main -b writeup-<slug> origin/main`, do everything
  there, push `HEAD:main`, then `git worktree remove`. Never `git commit --amend` during a rebase.
- `git fetch origin` and read `origin/main:docs/_build_site.py`, not the branch copy, if they differ: main's is newer.
- Read one recent page for tone and structure: `docs/gramont1529.html` (solved), `docs/lorraine1592.html`
  (partly read), `docs/orpo1942.html` (attempted, not solved).
- Decide the outcome class. `st` in the manifest is one of `solved` (read end to end or nearly), `partial`
  (partly read), `found` (explained, or found already solved by others), `stuck` (attempted, not solved). The README
  section, solved.html and SOLVED_* rows follow from it.
- Dates: "Date" is the document's date. The work date is the day the finding first landed in the repository
  (`git log --diff-filter=A --format=%ad --date=short -- <folder>/ | tail -1` if it was not today).

## 0a. Before writing up "read in part": push for the full reading

A partial outcome is a stopping point, not a default. It is allowed only when every unread piece is blocked by
something outside the session. Before choosing `partial`/`read in part`, work through each escalation step, and
go back to the reading whenever a step turns something up:

- `siblings`: open the neighbouring and sibling DECODE records, and the leaves next to the cipher in the volume
  (R1944, Castelcicala, Haga, Wolff and Malvezzi were all finished this way).
- `clear-pages`: check whether pages labelled "clear", "cleartext" or "postscript" are the decipherment (d'Affry,
  Rechteren, Dandini).
- `known-keys`: try every known key of the same series, archive, correspondent or decade (R784, Hernán Núñez, Rupert).
- `print`: search the printed editions and calendars (CSP, Bain, Forbes, Fraknói, Nuntiaturberichte, Politische
  Correspondenz, Parke, Lasry's GL.htm, Tomokiyo).
- `key-rebuild`: extend the key from what already reads, by constrained or swap annealing, seeded EM, alphabetical
  bracketing of the nomenclator, or LM context (Dandini, Balbases, Kauderbach, nunzio1718).
- `retry`: run every unread group and doubtful reading again with the extended key, and regrade them.

Then record the result in the folder's `NOTES.md`, which the checker parses:

```
## Remaining gaps
- code groups 42, 57, 88 - blocker: open-codes; each occurs once, no context narrows them
- letter of 3 May, lower half of f.12 - blocker: illegible; water stain, no other image
- R1041 - blocker: no-key-material; different code, no key on DECODE or in print

## Escalation
- [x] siblings: R1036-R1042 opened; R1039 is the clear copy of the first segment
- [x] clear-pages: none on the records
- [x] known-keys: R1024, R1038 tried; R1038 fits
- [x] print: Colenbrander, CSP grep, GL.htm: nothing
- [x] key-rebuild: seeded anneal filled 11 groups
- [n/a] retry: <reason, at least a few words>
```

**Read or read in part?** Apply the read bar in README Conventions: at least 95% of cipher tokens read as sense
(measured), no gap `not-attempted`, every document read, only scattered codes or externally blocked pieces open.
Record `outcome.key` (recovered / partial / none) apart from the text class, `outcome.codes_open`, and each document's
`read` state. `_check_writeup.py` checks the bar both ways (audit section F).

Blockers: `no-key-material`, `too-short`, `illegible`, `needs-physical-access` count as outside the session.
`open-codes` is allowed but keeps the target on the audit's list of workable partials (section E), and
`not-attempted` is refused. Mirror the list into `profile.json` `outcome.gaps` and set `outcome.fraction_read`.
`python docs/_check_writeup.py <slug>` fails a partial write-up until all of this is present. The Stop hook
blocks once on any partial target the session worked on that is still unjustified or has open-codes gaps.

## 1. The page: `docs/<slug>.html`

Copy the skeleton of a recent page. The builder regenerates nav, footer, contents strip, lead figure, byline date
and version stamps; you write everything else. Required parts, in order:

1. `<head>`: `<title>Short name (dates) — Read / Read in part / Not a cipher / Attempted</title>`, a one-paragraph
   `<meta name="description">`, `<link rel="stylesheet" href="style.css">`.
2. `<!-- site:nav -->` on its own line right after `<body>`.
3. `<section class="hero">`: optional `<div class="cipherstrip">` (a line of the cipher, a line of its reading,
   a few key equivalences); `<p class="kicker">place → recipient · cipher type · dates · outcome</p>`; `<h1>`;
   one or two `<p class="sub">` with shelfmark, what it is, what was done; `<p class="meta">Daniel Bourdeau</p>`
   (the builder adds the dates; a contributor's credit goes in the callout, not the byline).
4. `<main>` opening with `<div class="callout"><strong>Summary.</strong> …</div>`: what was catalogued, what was
   found, how, what stays open. Five to ten sentences.
5. Numbered `<h2><span class="num">01</span> …</h2>` sections: the documents and keys; the reading (one section
   per letter, with the text in the original language and, where useful, a translation); method; what remains
   uncertain (list every unread group and the grade of every doubtful reading, H/C/M/I as in README Conventions);
   Sources (archive links with view numbers, editions, prior keys with their authors).
6. Figures: `<figure><img src="<slug>_<what>.jpg" alt="…" loading="lazy"><figcaption>…</figcaption></figure>`, cut
   from the scans at the width of the text column (about 1100 px), JPEG, under 400 KB each, named `<slug>_…`.
   Page images themselves are never committed; crops for the site are.
7. Close with `<p class="muted">` pointing to the repository folder, then `<!-- site:footer -->`.

Write the HTML with the Write tool, not a Bash heredoc (long payloads fail to parse). HTML entities for accents
in attribute and manifest strings (`&eacute;`, `&rsquo;`, `&mdash;`), plain UTF-8 in the body is fine.

## 2. The manifest: `docs/_build_site.py`

- Add a `dict(slug=…, label=…, year=…, y=…, place=…, st=…, stt=…, title=…, blurb=…, quote=…, rights=…)` to
  `PAGES`, in chronological position. `y` is the sort year (float for a range), `stt` the badge text
  (`read`, `read in part`, `not a cipher`, `already in print`, `double pass not broken`…), `blurb` three or four
  sentences, `quote` one line from the reading, `rights` the archive's credit line.
- Add the slug to `IMAGES`: `('<slug>_lead.jpg', 'caption', 'credit')`, or `None`. Every page needs the key.
- Portraits of the correspondents (required; `_check_writeup.py` fails without one): for the principal sender and the principal recipient (named
  people only), look for a public-domain portrait on Wikimedia Commons (Wikidata P18 is a good start; a painting,
  drawing, engraving, medal or miniature; no photos of busts or tombs, no CC-BY files). Check the file's
  description and dates match the person, not a namesake or relative. Reuse the image of anyone already in
  `docs/_portraits.json`. Then
  `python docs/_add_portrait.py <slug> sender|recipient "<name>" "File:<Commons file>" "<Portrait by X, 1590>"`,
  which checks the licence, crops the face and updates the manifest; the build puts the from/to strip under the
  title. Look at the crop (profiles are often missed). A figure cropped from a public-domain group scene is acceptable
  when the source identifies which figure is the person (the Commons/Wikidata description, a key or legend, a label
  in the image, or a reliable source naming the position): add `--box x0,y0,x1,y1` (fractions of the image; it
  crops that region from a 2000-px copy) and make the caption say it is a detail, e.g. "Detail of <scene>, <artist,
  date>". If the figure cannot be identified with confidence, do not crop. Leave a side out when the person is anonymous, an office,
  or has no trustworthy portrait. Skipping is allowed only when it is impossible: both sides anonymous or offices, not a letter
  between people, or nothing trustworthy on Commons after a real search. Then record why in `docs/_explore_skip.json` under `"portrait"`; the checker accepts that instead.
- If the page is solved or partly read, update the `solved` survey entry's blurb and quote counts.

## 2a. The explore features: reveal, atlas, key web

The "How it was solved" replay needs nothing: the build draws it from `profile.json` (three steps or more). The other
three are data files you edit by hand; each is a few lines, and skipping one leaves the target off that feature.

- **Watch it decipher** (`docs/reveal/<slug>.json`, rendered by `cipher-reveal.js`; required, `_check_writeup.py` fails without it): build it whenever the repository holds a
  sign-level transcription paired with a key or decoder. Run the target's own decoder over one continuous passage of
  40–250 groups, ideally the one the page quotes; never fill values from memory or from the plaintext alone. Format:
  `{"slug", "anchor": "<h2 id the reveal goes under>", "title", "caption", "unit", "key_note",
  "tokens": [{"g": "972", "p": "the", "cls": ""}]}` with `cls` one of `unk` (p `?`), `unc`, `code`, `plain` (clear
  text, `g` empty), `null`. Check the result against the page's reading and mark disagreements `unc`. The build
  places the figure once, after the anchor h2. Copy an existing file (`reveal/armstrong.json`, `reveal/toledo1565.json`).
  Skipping is allowed only when it is impossible: no passage can be decoded sign by sign (unread, clear text,
  no transcription and no image to make one). Then record why in
  `docs/_explore_skip.json` under `"reveal"`.
- **Atlas** (`docs/atlas.json`): for each letter with a known origin and destination, append
  `{"slug", "doc", "year": <decimal>, "date", "from", "to", "st", "label"}` to `letters`, adding any new city to
  `places` as `[lat, lon]`. A court or a person goes where they were at that date; leave a letter out rather than guess.
  `st` is the page's `st`.
- **Key web** (`docs/keys.json`): when a named key read this target (a sibling's key, a DECODE key record, Lasry's or
  Tomokiyo's table, a key rebuilt here), add a `links` entry `{"key", "target": "<slug>", "how": "read unchanged" |
  "adapted" | "rebuilt from" | "partial", "note"}`, and a `keys` entry `{"id": "k-…", "label", "kind", "by", "year",
  "note"}` if the key is new. Only edges the NOTES state explicitly. When no named key read it (read from a
  contemporary decipherment, key rebuilt from its own text only, key not identified), record that instead as
  `"unlinked": {"<slug>": "<reason>"}`; `_check_writeup.py` warns until one or the other is there.
- **Zoom overlay** (`docs/zoom/<image name>.json`, optional): every figure image already opens in the deep-zoom viewer
  (`zoom.js`). To lay the transcription over a line crop, give `{"image", "source", "lines": [{"x", "y", "w", "h",
  "text", "gloss"}]}` with the box in fractions of the image, placed by looking at the image; `text` from the repo's
  transcription, `gloss` its reading. Only when the transcription matches the visible lines one for one. `"iiif"`
  (an info.json URL) swaps in the archive's full-resolution image.

## 3. The ledgers in the repository root

- `README.md`: one row in the matching `## Results` table (Solved / Explained / Partly read or adjudicated /
  Found already solved by others / Attempted and closed). Five columns: Target (name, place, dates, shelfmark,
  catalogue item and class), Date (of the document), work date, Result (bold outcome, then what was read and
  what is open), Where: `` [`<folder>/`](<folder>/) · [write-up](https://dbourdeau.github.io/cyphersolver/<slug>.html) ``.
  The Where link is what marks the row as written up; without it the row lists as "notes only".
- `SOLVED_CATALOGUE.md` (solved and partly read only): next number, same columns as the rows above it.
- `SOLVED_RANKING.md` (solved and partly read only): a `pN` provisional row with the six axis scores and the
  weighted score, and the sentence in the preamble that places it; add the score line at the foot.
- `TARGETS.md`: if the target was in the open list, move it to "Done elsewhere in this repo" with the status text.
- `catalogue.json` (catalogue items only): the catalogue holds open targets only, so **take the entry out**.
  If the target was read, partly read, resolved or found already in print, delete its entry (ids are never
  reused) and add its id to the list in `CATALOGUE.md` under "Read or resolved here, and removed". If the entry
  covers several items and only some were read, narrow it to the unread ones (title, date, shelfmark, status)
  and set `"outcome": "attempted, open"`; a target attempted and closed unread keeps its entry with the same
  outcome. Before deleting, make sure the README row or `SOLVED_CATALOGUE.md` carries everything the entry's
  status said. Also look for the target under another name: DECODE entries carry `decode_ids`, so match the
  record numbers (`R1234`) in the folder's NOTES against them. Dump with `indent=1, ensure_ascii=False` and a
  trailing newline.
- `docs/index.html`: a new `<li>` at the top of the first `<ul class="findings">` under Recent findings:
  `<li><b>Who to whom, date</b> &mdash; <span class="fnd">outcome in one line</span> … <a href="<slug>.html">write-up</a></li>`.
  The builder dates it and folds the list.
- `<folder>/profile.json`: run the `/profile <folder>` skill. It records the cipher parameters, the challenge
  conditions, the solution steps and the outcome in fixed fields for the LLM-performance paper.
  `python docs/_check_profile.py <folder>` must print `result: valid`.
- `decode_updates/queue.json` (targets read from DECODE records): queue the DECODE edits so they can be sent once
  the account has write access. `python decode_updates/queue.py add <folder>` pre-fills the records from the
  profile and their current DECODE status; fill each TODO: `proposed` status (Decrypted only if the whole letter
  reads in sense), a one-line `note`, the `reading` file, and the `key` (`{"decode": "<DECODE id>"}` when the key
  is on DECODE, otherwise `{"file", "lang", "how"}` pointing at the rebuilt key), `cite` for outside sources, and
  `fields` for corrected cipher type or language. Drop records that are only keys or unread siblings. Write each
  record's public reading to `decode_updates/decryptions/R<id>.txt` following `decode_updates/CLEANING_BRIEF.md`
  (the letter text only, gap conventions, no notes or markdown). Then
  `python decode_updates/build.py <folder>` must report 0 gaps. See `decode_updates/PLAN.md`.

  **Whenever DECODE is wrong, queue the correction, even with no new reading.** Compare every record's DECODE
  metadata with what the work found: status, language (cleartext and plaintext), date, place, sender, receiver,
  cipher type. Any mismatch goes in `fields`, and the status goes in `proposed`. A record read from a
  decipherment already imaged on it, or from a key already on DECODE, is still queued: `proposed: "Decrypted"`,
  `reading: null`, `"reading_not_needed": true`, and a `note` naming where the reading is (the `sauli1579` and
  `poupet1522` entries show the pattern). Use `queue.py skip <folder> "<why>"` only when every field and the status
  on DECODE are already right and nothing is added; the reason must say so.

  **This step also runs for targets that are not read.** When a DECODE target is attempted and left open, closed
  unread, or found to duplicate another record, it gets no page, but it still gets a queue entry in the same session.
  Use `proposed` = the current status, `reading: null`, `"reading_not_needed": true`, and `key: {"none": "<why>"}`
  when no key is known. Put what the work found in `note`: the true date or place, sibling and duplicate records,
  prior attempts, and where the material is. Put any ciphertext transcription in `"transcription": [<files>]`,
  which build.py attaches as `transcription.txt`. The `ranzo1528` entry shows the pattern.
- `unpublished/solved.html` (solved and partly read only; optional while the page is unpublished): a `<tr>` in the right table, then recount the sentences in
  "The short version" (items, read in full, in long stretches, to a solver, to a sibling or key).

## 4. Build, check, commit

From `docs/`, with UTF-8 forced (the stats builder crashes on the cp1252 console otherwise):

```
cd docs
PYTHONUTF8=1 python _catalogue_page.py     # only if catalogue.json changed
PYTHONUTF8=1 python _build_stats.py
PYTHONUTF8=1 python _build_site.py
cd ..
python docs/_check_writeup.py <slug>
```

The builder prints `note: <slug>.html has no README row`, `note: README links <slug>.html, which is not in the
manifest` and `note: <slug>.html has no hero section` when the surfaces drift; fix and rebuild. The checker must
end with `result: complete` (warn lines are allowed, MISS lines are not). Then check `git diff HEAD -- CATALOGUE.md`
shows only the intended rows.

Stage by explicit path: the new page and its images, `_build_site.py`, `_dates.json`, every regenerated
`docs/*.html`, the ledgers touched, `decode_updates/queue.json`. Never `git add -A`: the shared tree carries other sessions' work. Commit subject
`Site: write-up for <who to whom>, <dates> (<shelfmark>)`, body listing what each surface got, as in `git log
--grep='^Site:'`. Push to `main` (`git push origin HEAD:main` from a worktree) and confirm
`https://dbourdeau.github.io/cyphersolver/<slug>.html` after the Pages build.

## 5. If the target is not actually finished

Put `Status: in progress` (or `Status: no write-up`, with the reason) in the first forty lines of the folder's
`NOTES.md`. The audit and the Stop hook read that line and stop asking.
