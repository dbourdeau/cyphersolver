# T-S K24.24: Geniza leaf in an unidentified cursive script (Cambridge University Library)

Status: in progress

Cambridge University Library, Taylor-Schechter K24.24 (Princeton Geniza Project id 33913). Undated paper leaf, one side
(recto here, CUDL image 1) carrying ten lines in an unidentified cursive script, the other side plain Arabic. PGP: "Magical
fragment, perhaps. Unidentified alphabet or cipher", tags `cipher`, `magic`, no transcription, no bibliography, one related
document (not opened: the static page does not list it). Entered by Alan Elbaum in 2021. Lead from the 15 Nov 2026 Arabic sweep and the
25 Nov 2026 Geniza sweeps (`research/sweep_2026-11-25_geniza_thorough/`, `research/sweep_2026-11-25_geniza_literature/`).
Partner target: `targets/tsk2437/` (T-S K24.37). Session of 24 Nov 2026 (claude-sonnet-5-5), ciphertext-only.

## Access

CUDL IIIF by plain curl (no bot check): `https://images.lib.cam.ac.uk/iiif/MS-TS-K-00024-00024-000-0000N.jp2/<region>/full/0/default.jpg`,
N = 1 (the cipher side, 3806 x 3664 px) and N = 2 (the Arabic side, 3865 x 3597 px). `full` is capped at 2000 px, so
`fetch_images.py <id> <out.jpg>` takes 1800-px region tiles and stitches the native image. Images stay in the git-ignored
`img/`. CUDL's image permissions statement (on the PGP page): reproduction on the public web needs permission from
genizah@lib.cam.ac.uk, so no image is committed here.

## What the leaf shows

- **Cipher side (image 1):** ten lines, each of 25-33 pen-lift groups (about 290 stroke components in all, matching the
  28-35 signs per line the sweep counted), thick brush ink, one hand, slanting cursive. Dots (single, paired or in threes) stand between groups. Long
  diagonal strokes (ascender-like) cross into the line above; the lines are not ruled and rise slightly to the left. The left ends of the lines
  are aligned and open with a hooked sign; the right ends run into marginal marks (about seven short marginal items on the
  right edge, partly on a torn border) and, at the top right, a separate short line of marks. Direction of writing is NOT established.
- Sign forms seen: bar with a downward stem at one end; Z or three-stroke zigzag, sometimes with dots; ring with a cross (theta-like); long slash,
  sometimes with a hooked head; V or W shapes; S curls; stem with a loop (5, 6 and 8 shapes). Lines 6-9 end in runs of digit-like signs.
  No letter-shape identification was made. It is not a ring-letter script like Bohak's K24.19 family (see comparison).
- **Arabic side (image 2):** about nine lines of plain Arabic in a bold cursive with marginal notes; legible words include al-hamd li-llah, Muhammad,
  kitab, `ala`, Allah; the last line has three vertical strokes. Not transcribed, not a decipherment of the other side, no obvious link in content.

## Moves (all recorded in `profile.json`)

1. Prior art: PGP record, both Geniza sweeps, web search, DECODE harvest grep: nothing. Not in Bohak 2010's list.
2. Native images; looked at bands and line strips of the recto.
3. A hand transcription at sign level was not completed: the cursive is connected and the slashes cross lines, so a by-eye split into signs was not
   reliable. Instead `glyphs.py` produced an objective **stroke-level** stream (`transcription_auto.txt`, `cipher_tokens.txt`):
   ink components, 10 lines by slope-corrected y-clustering, 30 shape clusters by k-means. A token is one connected ink component, not a sign.
   289 tokens; line counts 32, 27, 24, 26, 33, 28, 31, 33, 27, 28 (clusters are size-driven and noisy; the exemplar sheets are in `img/auto/`).
4. Statistics (`analysis.py transcription_auto.txt --drop .`): IC 0.041 (uniform 0.033), entropy 4.67 of 4.91 bits; repeated 2/3/4-grams
   39/4/0 against shuffle means 44.3/2.3/0.1; H(next|prev) z -0.4. Nothing beyond chance, but this is a test of noisy strokes, not of the text.
5. Comparison with the Bohak family (K24.19 image viewed), T-S NS J479 (viewed), `tsas187240` glyph catalogue: no shape match by eye (table below).
6. Attacks (`attack.py`): many-to-one monoalphabetic annealing with the new `lang/` models `he-tanakh` and `ja-from-arabic`, no word breaks, both directions:

   | model | real forward | real reversed | shuffled nulls (10) | z fwd / rev | control (10) | control vs nulls |
   |---|---|---|---|---|---|---|
   | he-tanakh | -2.836 | -2.717 | -2.801 (sd 0.064) | -0.5 / +1.3 | -2.593 | z 3.3 |
   | ja-from-arabic | -2.660 | -2.700 | -2.610 (sd 0.051) | -1.0 / -1.8 | -2.374 | z 4.6 |

   Real text scores no better than shuffles. The control (model-language text, same length, random many-to-one map to 30 classes)
   separates only at z 3-5, and its text overlaps the model corpus, so the attack is weak at 30 noisy classes: this is a null result about the
   method on this transcription, not evidence about the leaf.

## Do the two K24 leaves share a system?

Best judgement: **no, two separate texts** (kept in two folders). Different hand and ink (slanted brush cursive vs upright pen angles), different
sign shapes (rings, zigzags, long slashes vs stems with feet, boxes, arches), different layout (10 dense lines vs 8 sparse lines with dashes and a
ruled frame), different size (K24.24 about 290 strokes, K24.37 about 150 signs). Shared: dot dividers, and a zigzag shape in both. Only a sign-level
transcription of both could prove it.

## Sign comparison with published and neighbouring systems

| system | source | look | K24.24 |
|---|---|---|---|
| Bohak ring-letter cipher (K24.19, K24.23, Misc.10.60 ...) | K24.19 image viewed 24 Nov | upright, medium signs with rings, x, 9, H; plain Hebrew words interspersed | no ring-letter set; slanted brush cursive; no x, 9, H forms |
| T-S NS J479 (Elbaum, ~22 signs) | image viewed; Elbaum's table not seen | upright, rings with a dot, P- and D-like shapes | no shape match; the ring-with-cross is the nearest and differs |
| T-S AS 187.240 glyphs | `targets/tsas187240/glyphs.txt` | goblet, 8, C, L, n, 3, U shapes | no match by eye |
| ENA 4100.7b | `targets/ena4100/NOTES.md` | Judaeo-Arabic with alef-initial words | not compared by shape |
| zimam (Greek/Coptic) numerals | not obtained | curvilinear numeral signs for 1-9, 10-90, 100-900 | hypothesis only (see below) |

## Hypotheses not yet tested

- **Zimam numerals as letters.** The digit-like runs at the line ends, the theta-like ring and the dot-separated groups fit numeral signs
  (Coptic or zimam forms) used as an alphabet: the keys on CUL Or.1080 J277 and Bodl. MS heb. f 102/28 give Hebrew letters by Greek/Coptic numeral
  value, and PGP's tag on Bodl. f 102/28 is `cipher`. With 27 signs (units, tens, hundreds) the inventory would be about 27; the stroke clusters
  here cannot show that. Needs the chart (Chrisomalis 2010, pp. 149-150, or Thomann, SCIAMVS 19, 2018) and a sign-level transcription.
- Arabic-language plaintext in Hebrew or invented letters (the verso is Arabic): tested only by the annealing above.

## Remaining gaps

- the whole recto: no sign-level transcription - blocker: illegible; connected cursive that a by-eye split could not do reliably, needs a human reader of Geniza cursive or a per-sign segmentation at native size
- the marginal marks at the right edge and the line above line 1: not transcribed - blocker: illegible; overlapped by the torn border and lines
- any key: none known - blocker: no-key-material; no zimam chart or Elbaum mapping obtained

## Escalation

- [ ] siblings: K24.19 viewed; K24.23 and the PGP "related document" not opened; ENA 3211.1-2, Misc.10.60/11.91/22.218 not viewed
- [n/a] clear-pages: the Arabic verso is plain text with no decipherment on it
- [ ] known-keys: J277 and Bodl. f 102/28 keys are Hebrew-letter value lists, not applied (no sign-level text to apply them to); zimam chart not obtained
- [x] print: PGP, both sweeps, web search, DECODE grep: no reading; Bohak 2010 PDF (academia.edu) not opened (403 to fetch)
- [x] key-rebuild: monoalphabetic annealing on the noisy stroke stream with Hebrew and Arabic models: null result (controls above)
- [n/a] retry: nothing read, nothing to retry

## Next steps

1. Sign-level transcription of the recto from native crops, line by line, by a reader of Geniza cursive (or by a per-sign contact sheet), with the
   forms of the zimam chart beside it.
2. Test the zimam-numeral-as-letter hypothesis (sign-for-sign table, then the J277 value key).
3. Ask the Cambridge Genizah Research Unit / Princeton Geniza Project (Elbaum, Bohak, Zinger) whether either leaf is known; nothing here has been sent.
