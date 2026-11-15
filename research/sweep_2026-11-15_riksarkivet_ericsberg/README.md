# Riksarkivet, Ericsberg volumes, Stedingk E 6706 and E 6618-6621 (15 Nov 2026)

Source key `riksarkivet_ericsberg`. Continuation of `sweep_2026-11-14_riksarkivet_more` (routes, detector limits there).
**Result: 0 rows** in `candidates.json` (empty list). Nothing padded.

## Method

Same route as the 14 Nov sweep: image-series id from the APE EAD (`dao()`), `lbiiif.riksarkivet.se` with
`Referer: https://sok.riksarkivet.se/`, three streams, about 1.5 s per image per stream, no bot check, no Chrome.
Every 3rd image of 31 Ericsberg volumes and of Stedingk E 6618-6621, every 2nd of E 6706. Fetched at 1200 px (the digit-run
detector `digitscan.py` is tuned to that glyph size; 800 px would shrink the glyphs below its range), 420-px thumbnails kept,
flagged pages re-opened at 800 px. Detector hits ranked per volume (`rank.py`, `top.json`) and the top 4 to 6 pages of
16 volumes viewed by eye in 2 x 2 sheets at 800 px. Nothing was transcribed.

Volumes (refs and image counts in `units.json`): Ericsberg B 1/13 (547 images), B 1/14 (582), B 1/15 (819), B 2/26 (626),
02/05/B/16, C. G. Tessin papers 02/07/04/1-4, 7-12, 03/01/~/1, 2, 4, and Vol. 303-306, 308-311, 313. Vol. 306 and 311
now resolve (A0040387, 282 images; A0040392, 257 images): the earlier connection resets did not recur. Stedingk
E 6706 (466), E 6618 (416), 6619 (393), 6620 (492), 6621 (336).

Images paged: **4,290 requested, 4,257 fetched** (33 failed fetches, 24 of them in E 6706) of 12,611 in the 32 volumes (34%).
(The 14 Nov README counts 27 Ericsberg volumes, 9,969 images; this run took 27 Ericsberg + 5 Stedingk.)

## What the pages show

- **B 1/13-15 (Hedvig Elisabeth Charlotta to Sophia Albertina, 1793-1807):** dense French letters in clear, with fold
  stubs, decorative paper borders and enclosures. No page of the 600 sampled shows digit groups; top detector scores
  (9-25) are paper borders and a seal. B 1/14, catalogued "Med chiffernycklar" (already a scandinavia lead), is sampled
  (193 pages) and shows no key sheet, so the keys are not in the sampled pages.
- **B 2/26 (1788-1827):** French letters with border patterns (image 85) and printed court notices. Clear.
- **C. G. Tessin papers 02/07/04:** Tessin's accounts, Cronstrom's Paris art accounts 1693, an extract of the Swedish-French
  convention 1738, poems and tales, printed festivities. Vol. 11 image 133 (score 206/215) is a page of tally strokes
  (accounts), not number groups; 349 is a clear "copie" of a 1750 subsidy declaration. Clear.
- **Vol. 303-314:** French letters 1790 (Stedingk-period), Swedish orders, German and Swedish printed matter (the Hannover
  patent 1866, price tables). Print and table pages produce the high detector scores. Clear.
- **Stedingk E 6706:** Russian coronation programme of 1826 (French and Russian printed notices). E 6618-6621: French
  and Swedish letters 1759-90, printed Swedish regulations. No digit groups seen.

## What it does not show

A 1-in-3 sample of letter volumes finds a cipher-bearing volume often, not a single ciphered postscript; short code groups
inside clear sentences show only at 800 px or more and were not looked for on the unflagged pages. The detector fires on
print, tally strokes, borders and tables and is not a measure of absence. The next step for B 1/14 would be a page-by-page
pass of images 1-30 and 540-582 for the key sheets, not a sample.

## Blocks

- **De la Gardie E 1649 (`R7000021`, 543 images): closed by a login wall, not a route problem.** Image requests answer
  401 "Du maste vara inloggad" for every header combination (Referer, Origin, the viewer URL as Referer, the `/v2/` path);
  the viewer `sok.riksarkivet.se/bildvisning/R7000021_00001` redirects to a login page: "on account of GDPR you must log in to
  read digitised material younger than 110 years". Not clicked through; needs the user's Riksarkivet account or a request.
  The manifest itself opens (canvases 3135 x 2213) but carries no image access.
- No other block. Vol. 306 and 311 opened on retry.

## Files

`units.json` (32 volumes, strides), `process_vol.py`, `digitscan.py`, `rik_common.py`, `tools.py`, `rank.py`, `top.json`,
`run0-2.log`, `candidates.json` (empty). Scan tables, thumbnails and sheets stayed in the session scratchpad.
