# PREREG — petkum1665, held-out test of key v7 (PR #699, Malcolm McBratney) — 17 Nov 2026

Written and frozen by SHA-256 (PREREG.sha256) BEFORE any of the leaves below was cropped, looked at or transcribed for this test.

## Key (frozen, unchanged)
- `key/key_v7.tsv` = `targets/petkum1665/key_v7.tsv` of PR #699 at commit e8f0f7e5002a11b65b3666d31f4f642651c40d78
  (md5 d1ee7e3094e1643bfb0f58b39e9d0052, sha256 c44f5b560898538d299c4afe6e74c57f72b9c64a6a269a502ca6b0b79033fdea).
- No row added, removed or changed. Our own T2 values that v7 lacks (207, 225, 376, 395; rank values 197, 344, 351) are NOT added.
- Every row is used for the character score, whatever its tier (doubtful rows 181, 248 included, as written).

## Portion (fresh: never used for a key, a check or a measure by us, McBratney or Daniel Bourdeau)
Rigsarkivet TKUA England A III 52, unit 261267, glossed relations to the king (list `deciphered_leaves` of
research/sweep_2026-11-11_tkua_paging_3/petkum_leaves.json). Pages, in this order:
  1. image 505 left, 2. image 505 right, 3. image 501 right, 4. image 437 right, 5. image 481 left.
(505 and 501 were named as reserves in our PROTOCOL.md of 11 Nov 2026 and never transcribed; 437 R and 481 L appear in no
file of ours, of PR #622, #646, #689, #699 or of origin/main targets/petkum1665.)
The portion H7 = the glossed cipher runs of whole pages taken in this order until the adjudicated count of glossed cipher
tokens reaches at least 300 (the page that crosses 300 is taken whole, then stop). If the five pages give fewer than 300:
no measure, CAPPED; no other page is added without a new hashed addendum written before it is looked at.
Pages transcribed but not reached by the rule stay unmeasured (they are not burned by this test, but they have been seen).

## Transcription (two blind passes, then adjudication, then freeze)
- Crops of the five pages at full resolution (images on SPOF_2, never published).
- Pass A and pass B: two separate AI sub-agents, each given only the page crops and the label sheet (`SHEET.md`, sign names,
  no values) — no key, no earlier transcription, no repository, no web. Neither sees the other's output.
  Each writes one row per cipher run: image, line, tokens (sheet labels), gloss (the chancery's interlinear decipherment
  written over that run, copied letter for letter as seen, abbreviations as written; '-' if none). A run is split where the
  gloss starts or stops.
- Adjudication: every token or gloss letter where A and B differ is settled on the image by the coordinating agent
  (who knows key v7: disclosed), before any decode of the portion; listed in ADJUDICATION.tsv. FINAL.tsv frozen by
  SHA-256 before the single measure.

## Measure (one only)
`measure_v7.py` (frozen with this file): decode each glossed run with key v7, compare with the gloss.
Normalisation (values and glosses alike): abbreviations expanded (`expand()`), lower case, accents dropped, a-z only.
Score = 1 - Levenshtein(P, R) / max(|P|, |R|) over the concatenation of glossed runs; for a value written
"A (B)" the nearer of A and B is used per run. Controls: 200 permutations of the key's value bundles among its tokens
(seeds 1..200), same procedure. **Bar (fixed here): score >= 0.85 AND score >= best control + 0.30.**
Reported, not decisive: the same score on pass A alone and pass B alone; token agreement A/B; strict count of SURE runs
(every token valued, no tier C or '?', decode = gloss).

## Afterwards
If the bar is passed: key v7 is validated on a held-out portion of unit 261267 (credit: key v7 = Malcolm McBratney;
measure = Brice Dudout's side). Then the strict recount of our reading of image 573 with v7 (Daniel's 95 % rule, SURE words
only). If it fails: recorded as failed, no re-test on these pages.
Frozen transcriptions of the first reader (e.g. the "15" of 528R.18) are not touched.
