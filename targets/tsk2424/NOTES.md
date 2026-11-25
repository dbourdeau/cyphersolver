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
   reliable. Instead `glyphs.py` produced an objective **stroke-level** stream (`transcription_auto.txt`; its `cipher_tokens.txt` was replaced by the second attempt below):
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

## Second attempt: sign-level transcription (24 Nov 2026)

Files: `transcription.txt` (10 lines, page order left to right), `signs.tsv` (line, index, x0, x1, label, grade, native
pixels of the deskewed image), `cipher_tokens.txt`, `segments_a.json` (the ledger), tools `prep.py` `win.py` `seg.py`
`sheet.py` `finalize.py`. The first attempt's stroke stream is kept as `transcription_auto.txt`. Measured with
`python docs/_check_profile.py --measure targets/tsk2424/cipher_tokens.txt`: **228 signs, 42 classes, IC 0.0442**.

**What changed against the first attempt.** The signs are large (100-250 px), so a line holds 18-30 signs (18, 21, 20, 21, 24,
25, 30, 22, 24, 23), not the 24-33 components of the stroke count; the first stream cut single signs into 2-3 strokes and
merged others. Of 289 stroke tokens only the isolated simple signs carry over; the class inventory is new (42 shape classes
against 30 size-driven clusters) and the statistics now differ (below). Images: CUDL has only the two images (recto, verso);
nothing in raking light or multispectral.

**Method.** Deskewed by 1.15 degrees, background flattened, each line viewed at 2x in windows of 5-8 signs with a pixel
ruler, cuts recorded per sign, then class sheets to split and merge. Where a sign ends was decided by pen lifts, a change of
stroke weight and repeated shapes; ligatures are rare, and the long slashes cross into the line above. **Not done: a fully
independent second reading.** The check pass (lines 1 and 7 at 0.9x with cuts drawn, the rest through class sheets) moved no
cut, but it was the same reader, so grades rest on one reader: 15 firm, 178 likely, 35 doubtful.

**Sign legend** (label, count, shape; page order, glyphs as in the image):

| Label | n | Shape |
|---|---|---|
| SB | 25 | stem with a hook at the top and a spur or arm to the left (cross-like) |
| HB | 21 | bar rising to the right, hooked back to the left at the top (open, like a Hebrew bet) |
| HC | 11 | the same with a second bar joined by a right-hand stem (closed) |
| HK | 15 | arc over a curve falling to the lower left, with a dot (below or inside); always dotted |
| Z7 | 14 | bar with a long stem down from its right end (a 7), the foot often blobbed or ragged |
| PI | 13 | arch with two legs (square or rounded, like a het or tav) |
| LS, LT | 9, 9 | long curved ascender with a top hook; long thin straight slash |
| MS | 8 | two or three stacked parallel diagonals joined by a stem |
| WV | 8 | wave: a rising S-curve, usually after SB |
| R8 | 8 | ring with an S-curl or arc over it (an 8) |
| BR, FS, RO, SC | 7 each | bare bar; 5-like stem with a curl bowl; ring or bowl hanging below the line; S over a bar |
| FB, RC | 6 each | stem with a left cross-bar and top hook; C-ring with dots at its open side |
| ST | 5 | plain stem with a flag at the top |
| RS, RX, SX | 4, 4, 3 | long slash with ring(s); ring crossed by a diagonal; slash with a 6-bowl |
| LF | 3 | leaf: arc and thin diagonal enclosing a loop |
| 18 others | 1-2 each | SD LA AR BL SS PS ES CC (2 each); ZL DB SH LV ZG LH WU LC SL BK TR GH (1 each): rare shapes, probably merges or damage forms |
| `.` | 5 | dot cluster standing alone (three in lines 3 and 5 are doubtful) |

**Doubt list** (line.index in `signs.tsv`; page order): 1.4 HK, 1.16 WV, 2.8 HB, 2.18 LS, 3.4 and 3.9 and 5.11 dots, 3.17 Z7,
4.5 RS, 4.11 RX, 4.12 HK, 5.14 BL, 5.23 RO, 6.4 ST, 6.11 RO, 6.25 HK, 7.1 ST, 7.2 BR, 7.3 SD, 7.5 SB, 7.6 BK, 7.10 RO,
7.17 Z7, 7.27 ES, 8.9 RO, 8.10 ES, 8.13 SB, 8.14 HB, 8.15 Z7, 9.7 TR, 9.13 SB, 9.20 PI, 10.2 GH, 10.3 AR, 10.5 SS, 10.12 BR,
10.13 BL, 10.20 Z7. Line 7 begins in a smeared, glare-damaged patch (x 250-575: 7.1-7.6, read in the gray image); the faint
signs 10.2-10.3 are ghosts of ink. Rings (RO) hang below the line above and are assigned to it. The slashes LS/LT that cross
lines are assigned to the line where they start; a slash through a ring may be one sign (RS) or two.

**Direction: right to left, from layout.** After removing the page tilt the line ends at the right align to a straight edge
(x 3140-3265, sd 11 px about a line sloping 12.6 px per line) while the left ends are ragged (x 255-518, sd 75 px): the lines
begin at the right and run out at the left, as in Arabic or Hebrew script. Stroke order does not show it (thick brush). The
transcription is therefore in page order, to be read from the right end of each line.

**Statistics** (`analysis.py transcription.txt --drop .`, 300 shuffles; first attempt in brackets): IC 0.0442 [0.041],
entropy 4.77 bits; repeated 2/3/4-grams 30/3/0 against 28.5/1.8/0.1 [39/4/0 against 44.3/2.3/0.1]; H(next|prev) 2.449 against
2.642 (sd 0.046), **z -4.1** [-0.4]. The bigram structure is real: SB then WV 6 times, SB then HB 6, HB then SB 4, HB then SC 4;
PI HB SB, SB HB SC and HB SB WV twice each (page order). HB and HC together are 14 percent of the signs, SB 11 percent. Words:
only five stand-alone dot clusters, too few to give word lengths. Annealing (`attack.py`, 42 classes, 8 restarts x 5000
steps, 20 controls): he-tanakh forward z 1.0 / reversed -0.6, ja-from-arabic 0.8 / 0.8, ar-mamluk 1.6 / -0.5; the
controls separate from the nulls at z 4-5, so 42 classes on 228 signs is too sparse for the method (a null result about the
method, as before).

**What the plain text on the leaf says.** Nothing plain on the recto: no header, numerals or words; the pencil shelfmark and the
yellow label are the library's. Along the right edge (x 3200-3500) a second, lighter layer in a finer pen: long arcs and ruled
lines (one boxed corner near line 6) and small sign-like marks, not transcribed; they could be a diagram, which would fit PGP's
"magical" tag. The verso is a bold Arabic hand of nine lines with long strokes and a marginal note; at the 0.4x view legible
words are Allah (written out), `ala`, kitab, al-insan (?), al-ala (?), and the last line ends in three upright strokes; no
name, date or subject could be read, and nothing links to the cipher side. Not a decipherment of the other side.

**What now looks like language or numerals.** Numerals: no. The signs do not form a closed set of 27 with a repeated-run
pattern; the first attempt's digit-like line ends were SB/ST/FS stems (lines 8-10 start with stems at the left end: FS ST ST Z7
in line 9), which are ordinary members of the class SB/FS/ST. Language: the bigram structure (z -4.1), the very uneven
frequencies (SB, HB, HK, Z7, PI, HC = 46 percent of the signs with 42 classes) and the aligned right margin are what a
substitution text would show; no word divider system is visible. Several shapes resemble Hebrew semi-cursive letters (HC and HB
bet, HK he, PI het or tav, Z7 dalet or resh, RO samekh, LS/LT lamed): a bet-like sign at 14 percent does not fit plain Hebrew, so
the guess is a substitution over Hebrew-looking shapes, with Judaeo-Arabic the likely plaintext (the verso is Arabic). Untested.

## Remaining gaps

- the marginal marks at the right edge (x 3200-3500, a lighter finer layer of arcs and small signs) and the faint stroke beside line 1: not transcribed - blocker: illegible; overlapped by the torn border and by the lines
- line 7 left end (7.1-7.6) and the doubtful signs in the doubt list: smeared or ghosted ink - blocker: illegible at the available resolution
- an independent second reading of the sign segmentation (one reader so far): no outside blocker, to be done by a second pass or a Geniza-cursive reader
- any key: none known - blocker: no-key-material; no zimam chart or Elbaum mapping obtained

## Escalation

- [ ] siblings: K24.19 viewed; K24.23 and the PGP "related document" not opened; ENA 3211.1-2, Misc.10.60/11.91/22.218 not viewed
- [n/a] clear-pages: the Arabic verso is plain text with no decipherment on it
- [ ] known-keys: J277 and Bodl. f 102/28 keys are Hebrew-letter value lists, not yet applied to the new sign-level text; zimam chart not obtained
- [x] print: PGP, both sweeps, web search, DECODE grep: no reading; Bohak 2010 PDF (academia.edu) not opened (403 to fetch)
- [x] key-rebuild: monoalphabetic annealing on the noisy stroke stream with Hebrew and Arabic models: null result (controls above)
- [n/a] retry: nothing read, nothing to retry

## Next steps

1. A second, independent reading of the sign segmentation (and of the right-margin layer) by a reader of Geniza cursive; sign-level transcription now exists (second attempt above).
2. Test the Hebrew-shape and zimam hypotheses on `transcription.txt` (right to left): sign-for-sign tables, the J277 value key, Judaeo-Arabic models; start from the repeated SB-WV and PI-HB-SB groups.
3. Ask the Cambridge Genizah Research Unit / Princeton Geniza Project (Elbaum, Bohak, Zinger) whether either leaf is known; nothing here has been sent.
