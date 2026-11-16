# gerlach1252: Johann Gerlach, Occulta scripta chymica, Wellcome Collection MS.309 (catalogue 1252), pp.7-10, 13-19 and parts of six later pages

Status: read in part (Malcolm McBratney with Claude and other model sessions, 10-11 Nov 2026, issue #439; integration check 12 Nov 2026). 1,260 of 1,394 words of the reading carry no doubt mark, bracket or hole = 90.4% by the README read bar (counted from `reading.md`); 17 of about 172 cipher pages. Key: Julius Kohn's of 1889, filed in the volume, applied by the contributor as a table of sign labels with three groups re-aligned. The rest of the cipher (pp.20-178) is not read: catalogue 1252 stays, narrowed.

Contributed by Malcolm McBratney (Brisbane), working with Claude (Anthropic), as GitHub issue #439 (no comments); GPT-6 Astra/Sol and Gemini 4 Argon made the first passes of pp.16-18 and independent passes of pp.8-10 and 13, as he names them. The issue carried the key table, the full sign transcription (Part B), the line-by-line decode (Part A), the reading and translation by page; the files here were laid out from it at integration. Catalogue entry **1252** (Daniel Bourdeau, UK libraries sweep, 28-29 Oct 2026).

## Document

London, Wellcome Collection, MS.309 (b19695561), Johann Gerlach (Girlach), *Occulta scripta chymica* (1572-76), 178 handwritten pages of the "Secreta alchemica" in cipher (pp.7-178; pp.179-207 partly), German alchemy and medicine. Images: Wellcome IIIF, `iiif.wellcomecollection.org/presentation/b19695561` (Public Domain Mark; reachable by plain curl); catalogue https://wellcomecollection.org/works/qb3carav. Read here: handwritten pp.7-10 and 13-19 (scans 0012-0022) and the opening lines of pp.40 (0043, lines 1-9 of 30), 107 (0100), 112 (0105, lines 1-5), 115 (0108), 156 (0149) and 177 (0182). Pp.11-12 are a narrow inserted leaf with no scan of its own.

## Key (`key.tsv`)

Julius Kohn's key of 1889 is written into the volume at pp.260-261 (scans 0265-0266): two leaves of sign groups in rows, dated 1889, with no letters beside them (seen at integration). The contributor read the order of the groups (Z to A) as letters and made a table of 52 sign labels (key_v3): one to three, once four, signs per letter; no nulls, no code groups; comma = word divider; alchemical pictograms (antimony, Mars, Mercury, Sol) as single signs. He says Kohn's u, t and s groups are one step out of line with the text values and moved them, and that three figure-4 shapes (open = l, closed with a point = r, modern closed = u) and the triangle on a stem (q) are assigned partly from context. So the key is not applied unchanged: outcome method "read with known key", with that alignment stated. Signs only on Kohn's sheet seen but not yet in the text: e GT, x 4X and LX, y II and UPA, z ZH.

## Reading (`reading.md`, `translation.md`)

Recipes: flowers of sulphur (p.7), sulphur sublimed three times with colcothar and salt, a medicine for the lungs and chest, with myrrh and asa dulcis against cough and consumption (pp.8-10); red and white flowers of antimony and a fever remedy (pp.13-14); the mercurius solis (p.15); "Was zu der coruption solis gehorig ist": sal armoniack sublimed six times through sal gemme, spiritus vini from burnt wine with calcined tartar, an aqua regis of vitriol, saltpetre and sal armoniack (pp.16-19, margin: 1. sal armoniack fol. 124, 2. spiritus vini fol. 125, 3. aqua regis fol. 137); and the openings of the practica of the philosophers' stone (p.40), the oak chest for putrefaction (p.107, 112), mercurius solis et lunae (p.115), the arcanum tartari (p.156) and oils and herb juices (p.177). The English is the contributor's; the recipes are given as 16th-century evidence only.

## Count

| Rule | Read | Of | Share |
|---|---|---|---|
| README bar, from `reading.md`: words with no '?', bracket or hole, 17 pages | 1,260 | 1,394 | 90.4% |
| Same, per page (read / words): p.8 99/111, p.13 115/125, p.19 99/105, p.7 92/96, p.9 91/118, p.10 91/118 | | | 89.2%, 92.0%, 94.3%, 95.8%, 77.1%, 77.1% |
| Contributor's rule: signs in words giving sense, firm | p.8 489/529, p.9 405/503, p.10 461/535, p.13 515/536, p.19 450/470 | | 92.4%, 80.5%, 86.2%, 96.1%, 95.7% (his figures) |

No page but p.7 reaches the 95% read bar by the README count, and p.7 only on the marks of `reading.md` (see the check of 14 Nov 2026 below); the contributor's p.13 and p.19 "read" rests on his sign-level count. Class: read in part for all.

## Integration check (12 Nov 2026)

- An own decoder written from the key table reproduces all 348 decoded lines of `decryption.txt` from `transcription.txt` (6,479 lettered signs, 143 doubtful; sign counts per page identical, e.g. p.8 529, p.13 536, p.19 470).
- Kohn's two leaves (scans 0265, 0266) and the first six lines of p.8 (130 signs) compared with the Wellcome IIIF images: group structure, word dividers and shapes agree with the labels; "multen" and the following words decode as the reading says. The other pages were not compared with the images.
- The contributor's word-list test (decoded words found in 64,029 spellings of 116 texts of 1500-1599: 77% to 96% per page; 1,000 shuffled keys per page at most 30%), his sign-agreement figures between transcribers (91.6% to 99.6%) and the blind p.8 control (firm 92.4%) were not re-run: lists and scripts were not sent. The p.8 control's order of events is by his record (a SHA-256 manifest of 70 files, RFC 3161 time 11 Nov 2026 22:41:32 UTC, stated in the issue, not recomputed).
- Pp.16-18 rest on single non-Claude readers (p.18 two, adjudicated) and are not rated.
- Prior art: the Wellcome catalogue says Kohn's key is inserted; the contributor found no published reading; German literature, Kohn's papers and the Wellcome files not checked. A reading with an existing key, not a first break.

## Independent verification by Brice Dudout (PR #570, 14 Nov 2026): p.7 re-read on the image

Brice Dudout (`VERIFY_dudout_20261114.md`, `verify_dudout_20261114.py`) reproduced all 348 lines of `decryption.txt`
from `key.tsv` and `transcription.txt` with his own decoder (re-run here: 348 of 348), and re-read p.7 on the full-size
Wellcome image (b19695561_0012). On that page the three figure-4 shapes are distinct: the open form (4L, l), the closed
form with the stem through it (4R, r) and the closed form with a flat foot (4U, u). All 45 figure-4 signs marked
doubtful on p.7 agree with their shape, and three signs change:

| line | was | now | word |
|---|---|---|---|
| L07 | `PI LEO OL? PHI DOT 4R?` | `PI LEO PHI DOT 4L` | souil |
| L07 | `SQ? LEO 4L? ST LAM` | `RH LEO 4L ST LAM` | wolet |
| L13 | `EUR 4U? PLUS? ST TRI` | `EUR 4U 4R? ST TRI` | ruret |

His commit changed `transcription.txt` and `decryption.txt` for p.7 (54 doubtful signs there, now 7) and left
`reading.md` and the count to the maintainer.

Checked here on the same image (full size, lines L07, L08, L12 and L13, about 75 signs): every sign agrees with the
corrected transcription. L07 word 2 has no sign between the delta and the crossed circle, and ends in the open 4; L07
word 4 begins with the rhombus that begins the line; the third sign of L13 is a faded figure 4 with its stem, so `4R?`
with its doubt mark is right.

Applied to `reading.md` p.7: *wolet* without the doubt mark; *ruret?* in place of *ruhet? [ruret?]*. The count becomes
1,260 of 1,394 words (90.4%; was 1,259 of 1,395, 90.3%), and p.7 92 of 96 (95.8%). That p.7 figure rests on the marks
of `reading.md` only: five more words of the page stand on a sign still marked doubtful in the transcription (`X?`
L13 and L18, `CC?` L14, `EUR?` L17, `PST?` L21) and carry no mark in the reading; with them p.7 would be 87 of 96
(90.6%). The single text entry stays read in part. The end of L24, left untranscribed, fits *o[der]* by his reading; it
stays bracketed.

Not re-read: the other pages. Doubtful figure-4 signs remain on pp.8, 9, 10, 13, 16, 107, 112, 115 and 177 (his list),
and the same re-reading could be done there.

## pp.124-137: blind sibling decode (16 Nov 2026), decoded, not read

Malcolm McBratney (Brisbane), working with Claude (Anthropic). The margin of p.19 sends the reader to fol. 124 (sal armoniack), 125 (spiritus vini) and 137 (aqua regis); those 14 pages (scans 0117-0130, all cipher, p.129 three lines) were taken as a sibling test of the key. Files: `transcription_p124-137.tsv`, `decryption_p124-137.txt`, `reading_p124-137.md`, `translation_p124-137.md`, and `blind/p124-137/` (packet prompt and label sheet, both blind halves, FREEZE files, `key_frozen.tsv`, `decode_once.py` and its output, `judge/`, `shuffle.py`, `shuffle_out.txt`).

- Key: `key.tsv` as on upstream main (commit 89e25ef7d), frozen byte for byte before the decode (sha256 7e6f0b8ad16f89e3b2ed29cfd469e143044dabcd19051b08f2801b24be02a9b3, `blind/p124-137/FREEZE.txt`). Unchanged.
- Transcription: blind, by two Claude sessions given only a sheet of sign labels with shapes, no letter values, and told not to decipher (pp.124-130 `BLIND_a.tsv`, pp.131-137 `BLIND_b.tsv`; hashes frozen 01:46-01:49 UTC). 306 lines, 6,072 signs in the key, 143 doubt-marked, 7 `#`. Not compared with the images after the decode.
- Decode: once, mechanically (`decode_once.py`, which refuses a second run). No emendation.
- Judge: one strict pass by letter (`judge/JUDGE_NOTES.txt`): S 5,667, E 398, N 32 of 6,097 = **92.9%** strict; per page 90.8% (p.127) to 94.8% (pp.125, 130). The reading file is the judge's segmented text, unchanged, with its marks: `[x]` a wrong letter, `{x}` a hole.
- Four systematic slips make 351 of the 398 wrong letters: l for u/v (195), r for u (72), g for d or k (57), f for long s (27). Reported as **suspected key-table errors** in `key.tsv` (u/v sharing signs with l and r, d/k with g, s with f) or label confusions in the blind transcription. Not fixed: with them fixed the share would be about 98.7%, which is untested.
- Shuffle control (`blind/p124-137/shuffle.py`): the letter column of the key permuted among the sign labels, 5,000 shuffles at seeds 20261112 and 7, scored with `lang` model de-1500s (order 5, letters only), mean log-prob per letter. Real decode -3.0196; shuffles scoring at or above it: 0 of 5,000 at both seeds (max -6.0697, -5.9688). Pass.
- Reading check: `docs/_check_reading.py` gives `reading_p124-137.md` 0.239 (43 of 180 sentences clean) and the decryption 0.241, "not a reading". The bracket marks split words into fragments and the run-on lines are left as written, so the figure understates the sense; by the checker's state the entry is **decoded, not read**.
- Content (recipe level): the end of a mercury preparation and the sal armoniack (p.124); spirit of wine from strong wine (pp.125-127); the spirit sharpened with tartar and put to putrefaction in a sealed viola in an oak cask over a water kettle, furnace and apparatus described (pp.127-135), the "balneum roris" (p.136); aqua regis against aqua fortis, from saltpetre and Hungarian vitriol (p.137). The English is Claude's recipe-level summary, unchecked. It confirms the margin references of p.19.
- Prior art: searched only in this repository (upstream NOTES list pp.20-178 as unread, catalogue 1252 narrowed); the literature was not searched again for these pages. Collision check 16 Nov 2026: no upstream file and no open pull request covers pp.124-137.
- The figure of record for pp.124-137 stays 92.9%, the first pass. It is not re-decoded with key_v2 (below).

## The four slips of pp.124-137 diagnosed; key_v2; fresh blind pass of pp.138, 139, 140, 150 (16 Nov 2026), decoded, not read

Malcolm McBratney (Brisbane), working with Claude (Anthropic). Files: `key_v2/EVIDENCE.md` (with `crops/`, `work/align.py`, `work/freq.py`, `FETCH_LOG.txt`, `FREEZE_v2.txt`), `key_v2.tsv` and `key_v1_to_v2.diff`; `transcription_p138-150.tsv`, `decryption_p138-150.txt`, `reading_p138-150.md`, `translation_p138-150.md`, and `blind/p138-150/` (prompt, `SHEET_v2.md` with its diff, `BLIND.tsv`, FREEZE files, `key_frozen.tsv`, `decode_once.py` and its output, `judge/`, `shuffle.py`, `shuffle_out.txt`, `PACKET_INDEX.txt`).

- **Diagnosis of the four slips** (`key_v2/EVIDENCE.md`): blind-reader naming, plus two of Kohn's signs left out of `key.tsv`. **No key value is wrong.** l and r for u (258): the scribe's u in the later hand is Kohn's closed printed 4 (4U), labelled 4L or 4R by the readers; the three 4-shapes are distinct on the images and on Kohn's sheet. g for d/k (55): 24 are SIG + SEVEN ("de") read as one ARW; 30 are k, written with Kohn's third k sign (o with an arrow), which `key.tsv` lacks, so the readers had no label for it. f for long s (27): S3 labelled MM by one reader. Per-reader counts from an alignment of the judge with the blind labels (301 of 306 lines); the g/k difference rests on 5 crops.
- **key_v2** (`key_v2.tsv`, sha256 b47062382f6c...8555): adds `k OAR` and `l 4C` (Kohn's sheet p.260; 4C not seen in the text) and sharpens the shape notes; no letter value changed. `key.tsv` itself is left as it is. Label sheet SHEET_v2 (no letter values) adds a look-alike section.
- **Fresh pages**: pp.138, 139, 140, 150 (scans 0131-0133, 0143), not covered by any upstream file or PR. Key_v2 and SHEET_v2 frozen 03:51:31Z; blind transcription by one Claude session from the sheet alone, frozen 03:57:39Z (md5 f9c60f62b69513ad2897705d65f0ca7a): 90 lines, 1,650 signs in the key, 32 doubt-marked, 0 `#`, 0 not in the key (decode_once totals). One decode, no emendation.
- **Judge**, one strict pass by letter, given only the decoded letters (`judge/BRIEF.txt`): S 1,573, E 68, N 11 of 1,652 = **95.2%** strict (p.138 95.3%, p.139 92.5%, p.140 96.4%, p.150 96.5%); (S+E)/all 99.3%. Remaining slips: 'de' where g is meant 15 times (30 letters; now the readers split ARW into SIG + SEVEN: the over-correction of the sheet's warning), l and u swapped 16, r for u/v/e 5, c in 'ck' and 'acch' 5, others 12 (30 + 16 + 5 + 5 + 12 = 68 E letters; judge/JUDGE_NOTES.txt).
- **Shuffle control** (`blind/p138-150/shuffle.py`, the pp.124-137 script with only the input file name changed to `BLIND.tsv`): 5,000 shuffles at seeds 20261112 and 7, `lang` model de-1500s, order 5, letters only. Real decode -2.4593 (1,650 letters; matches `decode_once.txt`); shuffles at or above it: 0 of 5,000 at both seeds (max -6.0198 and -5.8675). Pass.
- **Reading check**: `docs/_check_reading.py` gives `reading_p138-150.md` a clean share of 0.294 (10 of 34 sentences; hole rate 0.208), below 0.60, so by the checker's state the entry is **decoded, not read**. The judge's line-end run-ons are left as written and the slips are not corrected, which splits words the word list does not know.
- **Content** (recipe level; English is Claude's summary, unchecked): the aqua regis recipe continued from p.137, the phlegm drawn off in a water bath and sal armoniack added (pp.138-139); dissolving gold in aqua regis and refining gold with lead on a cupel (pp.139-140); the end of a precipitate made with spirit of wine, and how to multiply it with mercurius solis (p.150).
- Prior art: as for pp.124-137 (repository only; pp.20-178 listed as unread upstream).

## Remaining gaps
- 96 doubtful signs, mostly the three figure-4 shapes and the s-signs (143 until p.7 was re-read on the image, 14 Nov 2026: 54 there, now 7) - blocker: illegible; assigned partly from context
- p.9 lines 21-25 and two lines of p.10 - blocker: illegible; stained or damaged in the scan
- handwritten pp.11-12 (inserted narrow leaf) - blocker: needs-physical-access; no scan of its own
- p.40 beyond line 9, p.112 beyond line 5, the rest of pp.107, 115, 156, 177 - blocker: needs-physical-access; only opening lines were transcribed, the rest of those pages is a separate piece (see catalogue 1252, narrowed to pp.20-178 and the unread pages)
- pp.124-137: the four systematic slips (l/u, r/u, g/d-k, f/long s; 351 of 398 wrong letters) stay in the decode of record (first pass, 92.9%) - blocker: not-attempted; diagnosed 16 Nov 2026 as blind-reader naming plus two signs missing from key.tsv, no key value wrong (key_v2/EVIDENCE.md); tested on fresh pages pp.138-150 (95.2%), not by re-decoding these pages
- pp.138-150: the remaining slips ('de' for g 15, l/u 16, r for u/v/e 5) and 11 N letters - blocker: not-attempted; first pass of record, a re-read of the signs on the images is the next step; the g/k (ARW/OAR) shape difference rests on 5 crops
- pp.124-137: the sign-off B A M D (5 times) and 12 other N letters - blocker: too-short; clear initials or isolated signs with no value in the key
- signs of Kohn's sheet not yet seen in the text (e GT, x 4X and LX, y II and UPA, z ZH) - blocker: too-short; they do not occur in the pages read

## Escalation
- [x] siblings: pp.124-137 (the folios the margin of p.19 points to) decoded blind with the frozen key, 16 Nov 2026: 92.9% strict, shuffle 0/5,000 at two seeds; pp.138, 139, 140, 150 decoded blind with key_v2, 16 Nov 2026: 95.2% strict, shuffle 0/5,000 at two seeds; the rest of MS.309 (pp.20-178, 179-207) is the unread remainder, kept as catalogue 1252 narrowed; no sibling manuscript seen
- [x] clear-pages: Kohn's key sheet (pp.260-261) is the only key or decipherment seen; no clear copy of the recipes was looked for beyond the contributor's searches
- [x] known-keys: Kohn's key (1889) applied; no other key tried
- [x] print: the contributor searched online 10-11 Nov 2026: no published reading found; German specialist literature, Kohn's papers and Wellcome files not checked
- [x] key-rebuild: Kohn's key not rebuilt; its groups were re-aligned (u, t, s) as above; key_v2 (16 Nov 2026) adds the two signs of Kohn's sheet that key.tsv left out (k OAR, l 4C), no value changed
- [n/a] retry: the doubtful signs were decoded in context as marked; no further values are open on the pages read
