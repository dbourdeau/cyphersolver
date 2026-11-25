# Vetting, Geniza B 5652 verso and T-S K5.7 (2026-11-26)

Run by a Claude Code session (Claude Sonnet 5.5) on the two rows of `research/sweep_2026-11-26_geniza_followup/candidates.json`,
after merging `origin/worktree-agent-a23532850f6961897` (no conflicts). Nothing promoted; `catalogue.json` untouched.
The evidence is in the `vetting` blocks of leads 3860 and 3861 in `research/leads.json`; this file says how each decision was reached.

## Merge

`merge.py` did not know the new sweep folder: `sweep_2026-11-26_geniza_followup` was added to its `SWEEPS` list. Both rows already
had valid `region`, `seen`, `score_note` and `period` ("unknown"), so no schema fault needed fixing; the rows merged as **3860**
(JRL B 5652 verso) and **3861** (T-S K5.7). `leads.json` kept its serialisation (indent 1, ensure_ascii False, CRLF, trailing CRLF;
checked by byte count). The rows' vetting blocks were rebuilt to the gate's keys (`prior_art` with decode, tomokiyo, lasry,
edition, literature; `key_check`, `duplicates`); the sweep's `candidates.json` was left as the sweep wrote it.
(The `PROBLEM pares_ags[50-54]` lines `merge.py` prints are old period faults in another sweep, not touched.)

## Results

| Lead | Leaf | Verdict | Gate |
|---|---|---|---|
| 3860 | JRL B 5652 verso (and a foot line on the recto) | **open** | passes (`--lead 3860`: ready to promote) |
| 3861 | T-S K5.7 | **duplicate** of catalogue 3757 | closed by verdict; not promotable |

### 3860 JRL B 5652 (open)

- **Ciphertext seen.** Manchester's Luna IIIF images answer plain curl (only the Luna search pages have the reCAPTCHA): verso
  `luna.manchester.ac.uk/luna/servlet/iiif/ManchesterDev~95~2~57820~106599` and recto `...57816~106598`, native 5350 x 4017 px, viewed at
  1600 px, plus a 1800-px crop of the recto foot. One leaf, 79 x 166 mm. **Verso: 6 lines of ring-ended signs, the first three
  upside down**, by my rough count 100 to 130 signs (the sweep's "about 90" is low). **Recto: a 5-line plain Judaeo-Arabic letter and, new here, a
  sixth line at the foot of about 14 ring-ended signs** beside a plain Hebrew-script word. No key, gloss or transcription on the leaf.
- **Who knew it.** The Manchester catalogue (Luna manifest metadata, images shot 2007) reads: "Possibly from same manuscript: ... T-S
  K5.7, K24.19, K24.23, Misc.10.60, Misc.11.91, Misc.22.218; JTS ENA 3211.1-2", "Includes the same cipher as known from eight other
  Genizah fragments (see the article above)", reference Bohak, "Cracking the code and finding the gold" (forthcoming). So the cipher
  was identified on it by 2007. This is the "Manchester note" of the literature survey, now read in full rather than as a snippet.
- **Bohak 2010 read in full.** The CSIC volume PDF (albert.ias.edu bitstream; curl and WebFetch get 403, so it was opened in one Chrome tab
  and its text extracted there, no CAPTCHA involved) contains Bohak's pp. 9-23. A search of the whole article for "5652", "Rylands",
  "Manchester" finds nothing; his list "currently known to me" has Misc.10.60, Misc.11.91, Misc.22.218, K24.23 and ENA 3211.1-2 (plus the
  K24.19 and K5.7 of the main text). **B 5652 is not published or read there.** PGP's list on the K24.19 page matches Bohak's and omits it too.
  PGP 32630 has no bibliography, no cipher tag. No Fragment-of-the-Month post, paper or web page that reads it was found. Not checked:
  FGP (registration), Schaefer-Shaked, Friedberg.
- **DECODE, Tomokiyo, Lasry.** `decode_search.py` for Genizah, Geniza, Judaeo-Arabic, Rylands, Taylor-Schechter, Bohak: 0 rows; grep of the
  eight DECODE harvest batches: nothing relevant. Tomokiyo `unsolved.htm` and `GL.htm` fetched live and grepped for the same terms plus
  K5.7, K24, 5652, Cairo, Hebrew, Fustat: 0 hits.
- **Key.** Published: Bohak's fig. 3 (p. 21) is a table of the 22 K24.19 signs for aleph to taw, and the whole K24.19 text is
  printed with its decoding. Comparing the K24.19 image (CUDL, 1918 px) with the verso by eye: the same classes of sign occur (circle with
  a dot, 6/9-shaped ring ends, X, H, U forms), so it is the same cipher in kind. **No sign-by-sign table and no decipherment was
  made**, so "the key covers these signs" is likely but not shown. Recorded in `key_in_volume` and `key_held`; it does not block an open lead.
- **Duplicates.** `leads.json`, `catalogue.json`, `targets/`, sweep READMEs by "B 5652", "5652", "32630": only this lead and the 24-26 Nov
  sweeps. K24.19 and K24.23 are in no ledger (read and published; do not add them). K5.7 is a different leaf (3757, below).

### 3861 T-S K5.7 (duplicate of catalogue 3757)

- **Ciphertext seen.** CUDL IIIF by curl, 995 x 2000 px served (native 2480 px wide). Recto: four long lines, colon-divided ring-ended
  signs of the K24.19 set, a few small extra marks; verso blank (viewed). The sweep's "about 150 signs" is consistent with its own
  count of colons and marks; Bohak counts 26 letter positions per line (about 104 letters).
- **Already published.** Bohak 2010 pp. 13-15 and fig. 2 is about exactly this leaf: it was the fragment that started his interest
  (Wasserstrom: "written in some as yet indecipherable code"). He applied the K24.19 table, printed the four decoded lines, and found
  "meaningless gibberish": 26 letters per line, lines 2 and 4 beginning identically with aleph to yod, 22 interior letters once the first
  two and last two (read vertically) are removed, so a permutation is suspected; "its exact nature still awaits further elucidation".
  **Catalogue 3757** ("T-S K5.7, inner 22 positions in each row", vetted open by Codex on 23 Nov 2026) already records this leaf and this
  problem. The mechanical collision check misses it because the shelfmark text differs ("..., inner 22 positions in each row").
- **Therefore** 3861 is closed `duplicate` (via the gate's own `closed` field). The 15 Nov sweep's "charakteres, not a text cipher" and the
  26 Nov sweep's "text cipher" are both superseded: it is the K24.19 cipher, whose plaintext is not a plain message.
- DECODE, Tomokiyo, Lasry: as for 3860, nothing. PGP 42030: "indecipherable cipher" (from CUDL), bibliography 0, scholarship 404.

## Recommendation

**3860 B 5652: promote.** It passes the gate, is not in any ledger, and no reading is known; Bohak's 2010 article does not carry it
even though Manchester cited that article for it. A reading attempt needs (1) a sign transcription of the verso and the recto foot
line from the Luna IIIF images (full size is open by curl, so no new image is needed), (2) the Bohak fig. 3 table, which is only a
printed image and has to be re-keyed from the volume PDF or K24.19 itself (K24.19's decoded text is printed, so the sign values
can be read off the image against it), and (3) a test of the decoded letters for Judaeo-Arabic recipe formulae (the sibling strips
give titles such as "for the sea", "for a menstruant woman"). It is the cheapest reading in the Geniza set: short, one hand, key in print.
Courtesy: write to the Rylands Genizah curators and to Bohak before publishing a reading. **3861 T-S K5.7: close as a duplicate
of 3757** (done in `leads.json`); the open problem, the arrangement of the interior 22 positions, belongs to 3757 and is a harder
target (difficulty 4 there), not a transcription job. Hold nothing else; the sweep's next-step list for K5.7 is now 3757's.

## Routes and tools

| Host | Result |
|---|---|
| luna.manchester.ac.uk IIIF image and manifest URLs | plain curl; the manifest's metadata carries the catalogue note |
| lunatest.* detail pages | load but the catalogue data is JavaScript; use the manifest |
| princetongenizalab.github.io/iiif/jrl | plain curl |
| images.lib.cam.ac.uk IIIF | plain curl (995 x 2000 served for "full") |
| albert.ias.edu Bohak 2010 PDF | 403 to curl and WebFetch; opened in Chrome (one tab), fetched same-origin and text extracted with pdf.js from cdnjs: all 178 pages, article on pp. 9-23 of the volume |
| decode_search.py, cryptiana unsolved.htm / GL.htm | work |
