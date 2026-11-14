---
name: writeup
description: Write up a finished cipher target on the site and in every ledger, in this repository's convention. Use when a target is read, solved, explained or closed, when the Stop hook or `docs/_check_writeup.py` reports a finished target with no write-up, or when the user says "write it up". Argument is the target's folder name, e.g. /writeup gramont1529.
argument-hint: <folder or slug>
---

# Write up a finished target

A result is not finished until it is on every one of these surfaces. Concurrent sessions in this repo commit each
other's folders with `git add -A`, so the commit log never announces a solve; the only reliable signal is the
checker. Work through the list, then run `python docs/_check_writeup.py <slug>` until it prints `complete`.

Target: `$ARGUMENTS`. Read `targets/<folder>/NOTES.md` and the reading files first; the write-up is written from the notes,
not from memory. The slug is the folder name unless a page already exists under another name (check
`python docs/_check_writeup.py --audit` and the README row's link). Never invent a second page for the same target.

## 0. Before writing

- `git status -sb`: know which branch the shared checkout is on. Other sessions switch it. If it is not `main`,
  work in your own worktree: `git worktree add <scratchpad>/wt-main -b writeup-<slug> origin/main`, do everything
  there, push `HEAD:main`, then `git worktree remove`. Never `git commit --amend` during a rebase.
- `git fetch origin` and read `origin/main:docs/_manifest.py`, not the branch copy, if they differ: main's is newer.
- Read one recent page for tone and structure: `docs/gramont1529.html` (solved), `docs/lorraine1592.html`
  (partly read), `docs/orpo1942.html` (attempted, not solved).
- **One key, one entry.** Solutions are presented by key or cipher system (George Lasry, 14 Oct 2026). Never
  combine in one target, page or ledger row documents that use different ciphers just because they share
  something else: the same collection or volume, sender, recipient, embassy, date, or a feature such as
  superscript digits. That is confusing and error-prone (`superscript` mixed Ghinucci's Worcester syllabary with
  Gilino's Sforza key; `vasto1527` mixed del Vasto's letter cipher with Ranzo's initial-letter code; both were
  split on 14 Oct 2026 into ghinucci1527/gilino1527 and vasto1527/ranzo1528). Several letters in the same key
  belong together; a letter in another key gets its own folder and page, and the pages link each other in one
  sentence ("a different cipher, with its own page"). A sibling key that was tried and ruled out, or another
  cipher mentioned as context, is fine. Before writing, check that every document in the profile shares the key;
  if `outcome.parts` would carry two different keys or systems, split the target instead.
- Decide the outcome method (George Lasry's categories, `docs/_methods.py`, `docs/glossary.html`) and write it
  into the profile: `outcome.method`, `outcome.method_basis` (one sentence of evidence), `outcome.contribution`.
  `python docs/_classify_outcomes.py` proposes one from the profile's fields; decide from NOTES. The extent
  (complete / partial) comes from `outcome.class` and the read bar. The build derives the badge, colour, seal and the
  hero outcome line from the method, so the `st`/`stt` typed in PAGES only matter for pages without a profile.
  The README row goes in the section of its method (`M.SECTION`); `--audit` section G checks it.
- Credit everyone outside the project in `outcome.credits` (profile skill, step 9): whose key or decipherment was
  used, who pointed to a source, who solved it before, who sent a solution, correction or check. The build prints
  them on the page as the hero's credits line and adds them up on `contributors.html` and the front page's top
  contributors; nothing on the page is typed by hand. A result sent in by someone else gets `outcome.provenance`
  `contributed` (or `mixed`) and a `solution` credit with the PR, issue or email as `source`.
- **Full texts (George Lasry, 22 Oct 2026).** A reading (classed "read" or "read in part", or "already solved" with a
  reading method such as read from existing decipherment or read with known key) shows the complete
  transcription and the complete decryption of every document it covers, and the key when the project or a
  contributor recovered, extended or corrected it: historians can use the text, and earlier contributors can judge
  the reading. List them in the profile's `outcome.texts` (one entry per document or letter: `doc`, optional
  `label`, `transcription`, `decryption`, optional `translation`, and a one-to-three-sentence `summary` of what it
  says with its historical context) and `outcome.key_file` (`docs/_texts.py`). The builder renders a "Full texts"
  section before the sources, short files inline; `_check_writeup.py` refuses a reading without it. A decryption is
  the deciphered text, with unread groups marked, not only a score or a sample. If a contributor's texts are
  missing, ask for them and keep the result as a pointer until they arrive.
- **A reading must read, and be translated (George Lasry, 22 Oct 2026, on matignon1586).** A mechanical decryption
  is not a reading. Before anything is called read or read in part, build the decode into coherent sentences in its
  own language and translate them into English; where a sentence will not form, go back to the image and the key
  (a figure misread, a homophone mislabelled, a code group), fix, re-decode, and repeat until the sentences hold.
  A few holes are fine; holes in almost every sentence are not. Per `outcome.texts` entry: the `decryption`, a
  `reading` file when the decryption is raw (unspaced, capitals, decoder lines), a `translation` into English (not
  needed when `language` is `en`), and `state`: `read`, or `decoded, not read` for a leaf that does not yet build
  sentences (shown for checking, not counted, and never inside a target classed "read"), or `not prose` for key
  sheets, code lists and worksheets. Each `read` entry carries `reading_review` {grade A|B, by, date, note}: someone read
  the decryption as sentences (A coherent with scattered holes, B coherent but raw) — `_check_writeup.py` refuses an
  entry without it. `python docs/_check_reading.py <folder>` scores the sentences (language-neutral: a sentence is
  clean with at most one hole in ten words) and points the reader at the weak ones; it is not the verdict. The headline percentage on the page is never a token-run
  figure for a text that does not read.
- **No cipher type without evidence.** Until part of the text is read, name the system only as far as measured
  evidence goes ("a transposition: letter frequencies match Spanish"). Do not name a specific system, or say what
  its users were taught or would have been given, unless a source is cited; families not yet excluded are
  "open", not "likely" or "where practice puts the answer" (Richard Bean, issue #37, on an unsourced
  *Doppelwürfel* claim in `blume`). This applies to NOTES, the profile's `system` fields and the page.
- Words (README Conventions, `python docs/_check_terms.py <slug>`): say what happened ("deciphered with Lasry's
  key", "key recovered from the clear passages", "transcribed the contemporary decipherment"); do not use "read" or
  "solved" alone as an outcome word, and do not call an item unsolved because a catalogue says "undeciphered".
- Dates: "Date" is the document's date. The work date is the day the finding first landed in the repository
  (`git log --diff-filter=A --format=%ad --date=short -- targets/<folder>/ targets/<folder>/ | tail -1` if it was not today).

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
`read` state. `_check_writeup.py` checks the bar both ways (audit section F). The read share counts holes by words
(14 Nov 2026): a bare `[...]` is one unread word, a longer hole is written `[... n]` with n counted from the decode or
transcription (where groups do not map to words, the least number of words the decode shows; an estimate is said to be
one in the reading's notes, and on the page wherever a sized mark changes a stated figure); a mark whose extent the
files do not show stays bare, counts as one word, and is listed as "extent unknown" in the reading's notes (and on the
page where it could change the class). On a target read with its surviving period key, a group one digit off inside a
word counts as read only under the one-digit rule of README Conventions (slip seen on the image, whole word spelled).

Blockers: `no-key-material`, `too-short`, `illegible`, `needs-physical-access` count as outside the session.
`open-codes` is allowed but keeps the target on the audit's list of workable partials (section E), and
`not-attempted` is refused. Mirror the list into `profile.json` `outcome.gaps` and set `outcome.fraction_read`.
`python docs/_check_writeup.py <slug>` fails a partial write-up until all of this is present. The Stop hook
blocks once on any partial target the session worked on that is still unjustified or has open-codes gaps.

## 1. The page: `docs/<slug>.html`

Copy the skeleton of a recent page. The builder regenerates nav, footer, contents strip, lead figure, byline date
and version stamps; you write everything else. **Copying a page copies its words too**: replace the `<title>`, the
meta description, the kicker, the `<h1>`, the subtitle, the hero cipher strip, the glance box and the Sources
section (gonzaga1542 and branicki1757 once shipped with the limantour1909 head). `_check_writeup.py` fails a page
whose title or h1 shares no name or year with its manifest title, or whose title another page already uses.

**Say each fact once, from the source.** A count, a percentage or a date typed into the head, the glance box and the
body drifts apart when one of them is edited. Take every figure from `profile.json` or `NOTES.md` (recompute it
from the file when you can) and, before you finish, grep the page for each number you used and make sure every
place agrees. A claim about people or history that the target's sources do not carry ends with "(This background is
not from the sources and was not checked here.)" or is cut. Credits follow `profile.json` and the contributor's own
notes, never a guess from git authorship. Required parts, in order:

1. `<head>`: `<title>Short name (dates) — Read / Read in part / Not a cipher / Attempted</title>`, a one-paragraph
   `<meta name="description">`, `<link rel="stylesheet" href="style.css">`.
2. `<!-- site:nav -->` on its own line right after `<body>`.
3. `<section class="hero">`: optional `<div class="cipherstrip">` (a line of the cipher, a line of its reading,
   a few key equivalences); `<p class="kicker">place → recipient · cipher type · dates · outcome</p>`; `<h1>`;
   one `<p class="sub">`: a single plain sentence (about 30 words, no shelfmark) saying what it is and what came
   of it; `<p class="meta">Daniel Bourdeau</p>` (the builder adds the dates; a contributor's credit goes in the
   summary box, not the byline).
4. `<main>` directly after the hero's `</section>`, opening with the "At a glance" box. `<main>` is what gives the
   body its text column and margins, and the builder hangs the contents strip on it: leave it out and the page runs
   edge to edge with no contents strip (siena2023, 17 Oct 2026). Never close `</section>` and go straight into a
   callout or `<h2>`. The shelfmark goes in its Where row. Each row is one or two short, plain sentences for a
   reader who has never seen the page; facts only from the page, measured numbers exactly as in the body:
   ```html
   <div class="callout glance">
   <p class="gl-top"><strong>At a glance</strong><span class="gl-res">Read &middot; 241 of 244 cipher numbers</span></p>
   <dl>
     <dt>The letter</dt><dd>Sender to recipient, place, date; what the document is.</dd>
     <dt>Where</dt><dd>Holder and shelfmark; DECODE record and how it was catalogued.</dd>
     <dt>The cipher</dt><dd>The system in a sentence or two.</dd>
     <dt>How it was read</dt><dd>Where the key came from and how it was checked.</dd>
     <dt>What it says</dt><dd>The content, at most one short quotation.</dd>
     <dt>Still open</dt><dd>The concrete gaps.</dd>
   </dl>
   </div>
   ```
   The badge carries the method and extent in the glossary's words (known key applied, partial; key recovered from
   the ciphertext alone; not solved; not a cipher…) and the measure. Relabel rows that do not fit ("The document", "How it was tried", "Why it resists"), drop an empty
   one, and add a "Credit" row for prior work or a contributor. Examples: `docs/toledo1565.html`,
   `docs/wesselenyi1664.html`.
5. Numbered `<h2><span class="num">01</span> …</h2>` sections: the documents and keys; the reading (one section
   per letter, with the text in the original language and, where useful, a translation); method; what remains
   uncertain (list every unread group and the grade of every doubtful reading, H/C/M/I as in README Conventions);
   Sources (archive links with view numbers, editions, prior keys with their authors).
6. Figures: `<figure><img src="<slug>_<what>.jpg" alt="…" loading="lazy"><figcaption>…</figcaption></figure>`, cut
   from the scans at the width of the text column (about 1100 px), JPEG, under 400 KB each, named `<slug>_…`.
   Page images themselves are never committed; crops for the site are.
   **Every image names its own source, and every page shows the cipher.**
   - A snip of the cipher is required on every page (`_check_writeup.py` fails without one). Crop it from the
     scans the work used: a clear stretch of cipher, ideally with its gloss or decipherment. Look for the scans
     in the target folder, here and in the main checkout (`C:\Users\dbour\cypher\<folder>`). If they are not
     there, fetch them (Gallica IIIF, DECODE with the cookie, BL IIIF, PARES, archive.org for printed texts). Only
     when no image can be had (none exists, or only a paid or physical copy) record why in
     `docs/_explore_skip.json` under `"snip"`.
   - Every image figure carries `data-credit` naming **its specific source**: holder, shelfmark and folio or
     page, and the route. For example: `<figure data-credit="Biblioth&egrave;que nationale de France, fr. 3976
     f. 133v, via Gallica">`, `"British Library, Harley MS 260 f. 419r, via DECODE R8364"`, `"Meister, Die
     Geheimschrift (1906), p. 176, via the Internet Archive"`, `"S. Tomokiyo, Cryptiana"`. A diagram made here
     from a scan says so: `"Drawn here from BnF fr. 2984 p. 30 (Gallica)"`. The build prints the credit as
     `Image: …` at the end of the caption, so do not also write it into the caption text. The checker fails a
     figure without one.
   - The third field of an `IMAGES` lead crop is its credit, in the same specific form.
   - BnF cipher photographs (Gallica, or BnF photographs on DECODE): George Lasry passed on (22 Sept 2026) that
     crops may be used with proper attribution, so use them. Exception: fr. 3029 and fr. 3092 (his own
     forthcoming work) stay withheld.
7. Close with `<p class="muted">` pointing to the repository folder, then `<!-- site:footer -->`.

**Contributed pages (pull requests, emailed write-ups, a contributor's own `build.py`) go through the same
skeleton.** They arrive hand-made and pass most checks while missing parts of it. Before merging or integrating one,
bring it to this format: `<main>` after the hero, a "Credit" row in an "At a glance" box (not a one-line
"Current result" callout), a crop of the manuscript itself in the first section (a visual key made from glyph
samples is not a substitute; the `IMAGES` lead crop is shown on the page only when the page has no figure of its
own), the optional `cipherstrip` when the cipher has printable tokens, short `<h2>` titles (the contents strip shows
them as chips on a phone; keep them under about 30 characters), and the closing `<p class="muted">`. Compare it side
by side with `docs/sweden4306.html` or `docs/toledo1565.html`.

Write the HTML with the Write tool, not a Bash heredoc (long payloads fail to parse). HTML entities for accents
in attribute and manifest strings (`&eacute;`, `&rsquo;`, `&mdash;`), plain UTF-8 in the body is fine.

## 2. The manifest: `docs/_manifest.py`

`PAGES` and `IMAGES` are data in `docs/_manifest.py` (they were in `_build_site.py` until 10 Nov 2026); the builder
imports them and the checkers read the file as text, so keep one `dict(slug=...` per entry.

- Add a `dict(slug=…, label=…, year=…, y=…, place=…, st=…, stt=…, title=…, blurb=…, quote=…, rights=…)` to
  `PAGES`, in chronological position. `y` is the sort year (float for a range), `stt` the badge text
  (`read`, `read in part`, `not a cipher`, `already in print`, `double pass not broken`…), `blurb` three or four
  sentences, `quote` one line from the reading, `rights` the archive's credit line.
- Add the slug to `IMAGES`: `('<slug>_lead.jpg', 'caption', 'credit')`, or `None`. Every page needs the key.
- Portraits of the correspondents (required; `_check_writeup.py` fails without one): for the principal sender and the principal recipient (named
  people only), research a public-domain portrait on Wikimedia Commons for each side separately; reusing one side
  is not a reason to skip the other. Search in this order, and try each before giving up: the person's image
  already in `docs/_portraits.json` (reuse it with the same `File:`); Wikidata P18; the lead image of their
  Wikipedia article in every language that has one (en, fr, it, es, de, pt, nl: the API
  `action=query&prop=pageimages&piprop=name&titles=<title>` returns it; pause a few seconds between calls, Wikimedia
  answers HTTP 429 to bursts); their Commons category. Identify the person first: a title ("the Constable",
  "the Grand Master", "the Duke of Nevers", "the King of Portugal") names a definite person at the letter's date,
  so resolve it and look them up. Accept a painting, drawing, engraving, medal or miniature; no photos of busts or
  tombs, no CC-BY or CC-BY-SA files, no coats of arms, signatures or street signs (a lead image is not always a
  portrait). Check the file's description and dates match the person, not a namesake or relative. Then
  `python docs/_add_portrait.py <slug> sender|recipient "<name>" "File:<Commons file>" "<Portrait by X, 1590>"`,
  which checks the licence, crops the face and updates the manifest; the build puts the from/to strip under the
  title. Look at the crop (profiles are often missed). A figure cropped from a public-domain group scene is acceptable
  when the source identifies which figure is the person (the Commons/Wikidata description, a key or legend, a label
  in the image, or a reliable source naming the position): add `--box x0,y0,x1,y1` (fractions of the image; it
  crops that region from a 2000-px copy) and make the caption say it is a detail, e.g. "Detail of <scene>, <artist,
  date>". If the figure cannot be identified with confidence, do not crop. Leave a side out when the person is anonymous, an office,
  or has no trustworthy portrait. Skipping is allowed only when it is impossible: both sides anonymous or offices, not a letter
  between people, or nothing trustworthy on Commons after a real search. Then record why in `docs/_explore_skip.json` under `"portrait"`; the checker accepts that instead.
  The same pass applies to pages that do not go through this skill: contributed results, batch imports and pages
  built by a generator (e.g. `tools/lasry_bnf_pages.py` for George Lasry's BnF items). A generator writes the page,
  not the portraits; run `_add_portrait.py` for every named correspondent afterwards. When adding several, make a
  contact sheet of the new `docs/portrait_*.jpg` and look at every crop; recrop a missed face with `--box` (it saves
  `portrait_<name>-2.jpg`; move it over the bad file and fix the name in `docs/_portraits.json`).
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
- **Atlas** (generated; `tools/atlas_places.py`, run by the build): every profile document whose two places are known
  becomes an atlas letter. The build reads `"places": {"from": "<place>", "to": "<place>"}` on the document, or else
  matches both ends of its free-text `route` against the gazetteer (`docs/atlas.json` `places` plus `NEW_PLACES` and
  `ALIASES` in the tool). So: write `route` as "Paris -> London" where you can, and when it names people ("Henri III ->
  Matignon"), add `places` with the cities they were in at that date (insert the one line; do not reformat the file).
  A new city goes into `NEW_PLACES` as `[lat, lon]`. Leave a letter without `places` rather than guess. Hand-drawn
  entries in `docs/atlas.json` (no `"src"`) are kept and take precedence for their target.
  `python tools/atlas_places.py --gaps` lists write-ups with no atlas letter and the route ends that matched no place.
- **Key web** (`docs/keys.json`): when a named key read this target (a sibling's key, a DECODE key record, Lasry's or
  Tomokiyo's table, a key rebuilt here), add a `links` entry `{"key", "target": "<slug>", "how": "read unchanged" |
  "adapted" | "rebuilt from" | "partial", "note"}`, and a `keys` entry `{"id": "k-…", "label", "kind", "by", "year",
  "note"}` if the key is new. Only edges the NOTES state explicitly. A key rebuilt here, even from the target's own
  text only, or recovered by an outside solver, is a key: give it a node (`"kind": "rebuilt here"` or `"scholar's key"`)
  and a `"rebuilt from"` edge, so a later letter read with it can link to it. Only when there is no key at all (read
  from a contemporary decipherment with no values rebuilt, key not identified, not a cipher) record it as
  `"unlinked": {"<slug>": "<reason>"}`. `_check_writeup.py` fails (MISS) until one or the other is there whenever the
  profile's `outcome.method` involves a key (known key, external key, or key recovered from adjacent plaintext, outside
  plaintext or ciphertext only) or its steps used a sibling or source key.
  `kind` is one of `contemporary key`, `archive key`, `DECODE key record`, `scholar's key`, `rebuilt here`; labels are
  plain text (no HTML entities); `year` is the year the key was in use (an integer, or null if unknown), and a scholar's publication year goes in
  `found`. Optional `"image": {"src", "credit", "caption", "page"}` puts a picture of the key on its card (credit
  required). A `rebuilt here` key also gets `{"source": "s-cyphersolver", "key": "k-…"}` in `source_links`, the
  project's hub node. Every named key the NOTES say was tested and did not fit goes in `"tried": [{"key", "target", "note"}]`
  (add the key node if it is new). `_build_site.py` fails the build on an unknown kind or edge type, a missing key or
  page, an uncredited image, or a target both linked and unlinked.
- **Zoom overlay** (`docs/zoom/<image name>.json`, optional): every figure image already opens in the deep-zoom viewer
  (`zoom.js`). To lay the transcription over a line crop, give `{"image", "source", "lines": [{"x", "y", "w", "h",
  "text", "gloss"}]}` with the box in fractions of the image, placed by looking at the image; `text` from the repo's
  transcription, `gloss` its reading. Only when the transcription matches the visible lines one for one. `"iiif"`
  (an info.json URL) swaps in the archive's full-resolution image.

## 3. The ledgers in the repository root

- `README.md`: one row in the `## Results` table of the target's outcome method (`docs/_methods.py` SECTION: Key
  recovered from ciphertext-only / ... based on plaintext from external sources / ... based on adjacent plaintext /
  Read after matching with key from external sources / Read with known key / Read from existing decipherment / Not
  solved / Not applicable). Six columns: Target (name, place, dates, shelfmark, catalogue item and class), Date (of
  the document), Landed (work date), Extent (complete / partial / &mdash;), Result (what was deciphered and what is
  open), Where: `` [`targets/<folder>/`](targets/<folder>/) · [write-up](https://dbourdeau.github.io/cyphersolver/<slug>.html) ``.
  The Where link is what marks the row as written up; without it the row lists as "notes only".
- `SOLVED_CATALOGUE.md` (solved and partly read only): next number, same columns as the rows above it.
- `SOLVED_RANKING.md` (solved and partly read only): one row in the single `## Composite ranking` table, inserted
  at its score position and marked `†` (provisional) after the rank: the six axis scores, the score computed with the
  stated formula (0.25 D + 0.25 H + 0.20 N + 0.10 R + 0.10 F + 0.10 V, two decimals), and the reasons in the last cell.
  Renumber the ranks below it (equal scores share a rank). No separate provisional table, preamble sentence or
  arithmetic line.
- `catalogue.json` (catalogue items only): the catalogue holds open targets only, so **take the entry out**.
  If the target was read, partly read, resolved or found already in print, delete its entry (ids are never
  reused) and add its id to the list in `CATALOGUE.md` under "Read or resolved here, and removed". If the entry
  covers several items and only some were read, narrow it to the unread ones (title, date, shelfmark, status)
  and set `"outcome": "attempted, open"`; a target attempted and closed unread keeps its entry with the same
  outcome. Before deleting, make sure the README row or `SOLVED_CATALOGUE.md` carries everything the entry's
  status said. Also look for the target under another name: DECODE entries carry `decode_ids`, so match the
  record numbers (`R1234`) in the folder's NOTES against them. Dump with `indent=1, ensure_ascii=False` and a
  trailing newline.
- `docs/findings.html`: a new `<li>` at the top of its `<ul class="findings">`:
  `<li><b>Who to whom, date</b> &mdash; <span class="fnd">outcome in one line</span> … <a href="<slug>.html">write-up</a></li>`.
  The builder dates it and mirrors the newest five onto the home page. Do not edit that mirror on `index.html`: a plain
  `<li>` added there is moved to `findings.html` by the next build.
- `targets/<folder>/profile.json`: run the `/profile <folder>` skill. It records the cipher parameters, the challenge
  conditions, the solution steps and the outcome in fixed fields for the LLM-performance paper.
  `python docs/_check_profile.py <folder>` must print `result: valid`.
  If the project recovered the key, run `python docs/_validate.py <folder> --write` (or `--na "reason"`); the checker
  requires a validation verdict on every recovered key.
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

**Claims review (required for a new page).** The checker cannot tell whether a sentence is true, so before the page
is recorded a separate reviewer checks it against its sources: follow `.claude/skills/writeup/claims-review.md`
(launch a read-only agent with that brief on the page, then fix every error and likely finding, choosing the
wording the sources support). Then record it:

```
python docs/_check_writeup.py --reviewed <slug> --claims-reviewed
```

`--reviewed` records a fingerprint of the target's `NOTES.md` and `profile.json` (docs/_page_sources.json) and
refuses a page that fails the head, link or markup checks; without `--claims-reviewed` it refuses a page that has
no record yet (a page recorded earlier without one shows a warning on the per-page check). The checker fails a page with no record, and the audit
(section Q) and the Stop hook flag any page whose sources changed after its record, so a stale page cannot sit
unnoticed. CI runs `python docs/_check_writeup.py --gate` on every push and pull request: it fails on a head, link
or markup violation that is not in `docs/_audit_baseline.json`.

The builder prints `note: <slug>.html has no README row`, `note: README links <slug>.html, which is not in the
manifest` and `note: <slug>.html has no hero section` when the surfaces drift; fix and rebuild. The checker must
end with `result: complete` (warn lines are allowed, MISS lines are not). Then check `git diff HEAD -- CATALOGUE.md`
shows only the intended rows.

**Look at the page before committing.** The checker reads markup, not layout. Serve `docs/` locally (in the
built-in browser) and open the page at desktop width and at phone width (375 px): the body sits in the
centred text column with margins like any other write-up, the contents strip and the At a glance box show, the
cipher crop is there, and nothing scrolls sideways (`document.documentElement.scrollWidth` no wider than the window).
Compare it with a recent page. This applies to every page you publish or merge, contributed ones included.

Stage by explicit path: the new page and its images, `_manifest.py`, `_dates.json`, every regenerated
`docs/*.html`, the ledgers touched, `decode_updates/queue.json`. Never `git add -A`: the shared tree carries other sessions' work. Commit subject
`Site: write-up for <who to whom>, <dates> (<shelfmark>)`, body listing what each surface got, as in `git log
--grep='^Site:'`. Push to `main` (`git push origin HEAD:main` from a worktree) and confirm
`https://dbourdeau.github.io/cyphersolver/<slug>.html` after the Pages build.

## 4a. Keeping a finished page true

A page is written from `NOTES.md` and `profile.json`; when either changes, the page may now say something the
sources no longer support. That is the commonest error found in the 7 Nov 2026 review of all 559 pages (counts,
"Still open" lines, glance boxes and credits left behind by a later update).

- Whenever you change `NOTES.md` or `profile.json` of a finished target, re-read its page against them: the head and
  meta description, the glance box, "Still open", every count and percentage, credits, and the Full-texts
  summary. Fix what changed, run `python docs/_check_writeup.py <slug>`, then `--reviewed <slug>` (a small change needs a
  careful re-read; after a large rewrite of the body, run the claims review again with `--claims-reviewed`). The audit lists
  the pages you still owe (section Q); the Stop hook asks once if you changed sources and left their page unreviewed.
- When a target is split or merged, do this for **every** page involved, and remove the record's rows from the
  glance box and hero of the page that lost them (bergamo1585, windischgraetz1720, beatrice1482 and others kept
  the old record's rows).
- Generated parts are rebuilt from their source, so an edit in the page is undone by the next build: fix badges,
  titles and cite lines in `docs/_manifest.py`, Full-texts summaries in `profile.json` (`outcome.texts[].summary`),
  portrait cards in `docs/_portraits.json`, and the texts themselves in the target's `reading*`/`translation*` files.
- Do not run scripts from a `targets/` folder to check a number on a page: several rewrite tracked files. Recount
  with `python docs/_check_profile.py --measure <file>` or by hand.

## 5. If the target is not actually finished

Put `Status: in progress` (or `Status: no write-up`, with the reason) in the first forty lines of the folder's
`NOTES.md`. The audit and the Stop hook read that line and stop asking.
