# NLI Geniza sweep, signed-in Chrome (26 Nov 2026)

Run by a Claude Code session (claude-sonnet-5-5) to image the Geniza leaves that NLI blocked in `sweep_2026-11-26_geniza_followup`.
Claude in Chrome, one tab of mine, the user's signed-in NLI session. No credentials typed, nothing downloaded, nothing
registered. Screenshots stayed in the session scratch folder; no image is in the repository. Nothing promoted;
`catalogue.json`, `leads.json`, `targets/`, `docs/` untouched. `candidates.json` is empty: no new ciphertext was seen.

**The sweep stopped early.** After NLI 577.1/63 was imaged, the next navigation on www.nli.org.il (the Ktiv landing page
`https://www.nli.org.il/en/discover/manuscripts/hebrew-manuscripts`) returned a Cloudflare "Just a moment" page that
turned into a **Turnstile "Verify you are human" checkbox**. Per the brief I did not click it and did no further work on
the host. The tab (title "Just a moment...", URL above) is left open for the user. AIU XII.41, XII.68, VI.B.174, VI.B.157
and the Ktiv term searches (cipher, code, cryptic, symbols, unidentified script, magic, Hebrew and Arabic) were therefore
**not done**: I had no NLI record ids for the AIU leaves (PGP carries no NLI URL for them) and finding them needs the Ktiv search.

## Records (PGP dump, `pgp-metadata` of 25 Nov)

| Shelfmark | PGP id | PGP description (short) | NLI route |
|---|---|---|---|
| NLI 577.1/63 | 33652 | prayer or magical fragment in Arabic script; Muhammad invoked, "string of magical characters"; lower fragment "literary" | docId `PNX_MANUSCRIPTS990038689760205171` (in PGP fragment_urls); manifest `PNX_MANUSCRIPTS990038689760205171-1`; **imaged** |
| AIU XII.41 | 30954 | recto last page of Eutychius' Annals; verso a cross, "cryptic symbols", Arabic alphabet partly mirrored | not located (web search finds no Ktiv record) |
| AIU XII.68 | 30980 | Arabic magic, text in several directions, red grids of numbers/symbols/words | not located |
| AIU VI.B.157 | 31197 | many magic squares in Arabic and Hebrew letters | not located |
| AIU VI.B.174 | 31203 | Ladino accounts; facing page "mysterious symbols, triangles, circles, lines, dots" | not located |
| BL OR 10656.25 | 32265 | Arabic document, four columns of symbols "(astronomical? not Coptic numerals)"; verso calendar text | not online as far as found (BL archive record `Or 10656`, 26 folios; neighbouring BL Genizah records say "digital images currently unavailable", consult in London; Friedberg and NLI catalogues are named as other descriptions) |

## Table of every leaf with its image verdict

| Leaf | Images | Verdict | Extent | Notes |
|---|---|---|---|---|
| NLI 577.1/63 recto (two fragments, photo A. Bar Hama) | 4985 x 3256 px | **plain Arabic prayer text**, naskh-type hand: 7 lines left fragment, 6 lines right fragment. Right fragment last two lines read as a formula (salawat "ala sayyidina Muhammad wa-alihi ajma'in", then a line of repeated "Allah" / "la ilaha illa Allah" in running script). Class: **magic/devotional, plain**, not a cipher | about 13 lines | the PGP "string of magical characters" is the repeated divine name, in Arabic letters |
| NLI 577.1/63 verso | same | left fragment 7 lines of plain literary Arabic; right fragment **blank** | 7 lines | nothing to classify |
| AIU XII.41 verso, XII.68, VI.B.157, VI.B.174, BL Or 10656.25 | not seen | **unclassified**; PGP descriptions only (magic, accounts, symbols); none described as text with letters | n/a | see Routes and What remains |

No ciphertext, no sign system, no key or gloss, so no per-leaf prior-art table is owed. Prior art for 577.1/63: none
beyond the PGP record (no mention in Tomokiyo, DECODE or the Bohak family list).

## NLI routes: what worked signed in

- `https://www.nli.org.il/en/discover/manuscripts/hebrew-manuscripts/itempage?vid=KTIV&scope=KTIV&docId=<PNX id>` loads
  signed in (it was a hard block signed out, curl and Chrome). The record's "View Manuscript" link opens the viewer in a new tab.
- The manifest `https://iiif.nli.org.il/IIIFv21/DOCID/<PNX id>-1/manifest` returns 200 (IIIF v2.1) to a `fetch()` run from
  a www.nli.org.il page; image ids are `FL<digits>`, canvas sizes 4985 x 3256.
- **Images load only as `<img>` elements inside a www.nli.org.il page** (Referer/fetch-metadata dependent): navigating the
  tab directly to `https://iiif.nli.org.il/IIIFv21/FL31383534/full/max/0/default.jpg` (or `/1000,/`) returns a Spring
  "Whitelabel Error Page, Bad Request 400". From a page on www.nli.org.il, `new Image().src = <iiif url>` works for
  `full/1600,/0/default.jpg`, `full/max/...` and region crops `x,y,w,h/1600,/0/default.jpg`. Recipe: open the viewer page,
  run JS that clears `document.body` and appends a full-window `<img>` with that URL, then screenshot (a 1600-px width gives
  readable lines; use region crops for detail).
- The in-page viewer itself showed blank pages (tile requests with status 0 and a `NotifyError` call), so use the img overlay.
- The browser tool's JavaScript output filter blocks any result containing URLs with query strings or cookies; return
  counts and path pieces only.
- **What still triggers Cloudflare Turnstile even signed in:** the Ktiv landing/search page
  (`.../hebrew-manuscripts`) after a few item loads. Not clicked. Item pages and the viewer did not trigger it.
- Tab quirk: a tab opened in the claude-in-chrome group may vanish from the tab list while a cross-domain page loads
  (another session shares the group); re-run `tabs_context_mcp` and wait for a screenshot.

## What remains

1. A person (or this route with a user-cleared Turnstile) to open the Ktiv search for the AIU Genizah leaves
   (shelfmarks "AIU XII 41", "XII 68", "VI B 157", "VI B 174"; the NLI sys numbers or docIds are not in PGP), then apply the
   img-overlay recipe. VI.B.174 and XII.41 verso first (PGP: symbols; XII.41 verso looks like an alphabet practice with a
   cross, so most probably not a cipher).
2. Ktiv term searches (cipher, code, cryptic, secret writing, symbols, unidentified script, magic; Hebrew and Arabic
   equivalents) were not run.
3. BL Or 10656.25: check Friedberg (registration) or a BL reading-room request; not online by any route found.
