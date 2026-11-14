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

## Remaining gaps
- 96 doubtful signs, mostly the three figure-4 shapes and the s-signs (143 until p.7 was re-read on the image, 14 Nov 2026: 54 there, now 7) - blocker: illegible; assigned partly from context
- p.9 lines 21-25 and two lines of p.10 - blocker: illegible; stained or damaged in the scan
- handwritten pp.11-12 (inserted narrow leaf) - blocker: needs-physical-access; no scan of its own
- p.40 beyond line 9, p.112 beyond line 5, the rest of pp.107, 115, 156, 177 - blocker: needs-physical-access; only opening lines were transcribed, the rest of those pages is a separate piece (see catalogue 1252, narrowed to pp.20-178 and the unread pages)
- signs of Kohn's sheet not yet seen in the text (e GT, x 4X and LX, y II and UPA, z ZH) - blocker: too-short; they do not occur in the pages read

## Escalation
- [x] siblings: the rest of MS.309 (pp.20-178, 179-207) is the unread remainder, kept as catalogue 1252 narrowed; no sibling manuscript seen
- [x] clear-pages: Kohn's key sheet (pp.260-261) is the only key or decipherment seen; no clear copy of the recipes was looked for beyond the contributor's searches
- [x] known-keys: Kohn's key (1889) applied; no other key tried
- [x] print: the contributor searched online 10-11 Nov 2026: no published reading found; German specialist literature, Kohn's papers and Wellcome files not checked
- [n/a] key-rebuild: Kohn's key not rebuilt; its groups were re-aligned (u, t, s) as above
- [n/a] retry: the doubtful signs were decoded in context as marked; no further values are open on the pages read
