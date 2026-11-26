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

## Integration check of pp.124-137 and pp.138-150 (16 Nov 2026, PR #686)

Checked by a model session for the project; no person has checked the transcriptions, the decodes or the English.

- Decode: a decoder written here from `key.tsv` and from `key_v2.tsv` gives the contributor's letters on every line (306 of 306, pp.124-137; 90 of 90, pp.138-150): 6,072 and 1,650 signs in the key, 143 and 32 doubt-marked, 7 and 0 `#`, 1 and 0 labels not in the key. `transcription_p*.tsv` and `decryption_p*.txt` are byte for byte the blind files and `decode_once.txt`.
- Hashes: `key.tsv` on main = `blind/p124-137/key_frozen.tsv` = sha256 7e6f0b8a...a9b3; `BLIND_a.tsv`, `BLIND_b.tsv`, `BLIND_all.tsv`, `key_v2.tsv`, `SHEET_v2.md` and `blind/p138-150/BLIND.tsv` match their FREEZE files. The times in the FREEZE files are the contributor's record; the pp.124-137 result was committed (02:11 UTC) before key_v2 and the pp.138-150 pass (04:04 UTC).
- Judge counts re-added from `judge.tsv`: S 5,667, E 398, N 32 of 6,097 letters (92.9%), no line differs from its marks; S 1,573, E 68, N 11 of 1,652 (95.2%). These are shares of letters, the contributor's measure. By the README rule (words), 1,094 of the 1,485 words of the pp.124-137 judge text carry no mark = 73.7%; the pp.138-150 judge text marks no words, so no word share can be counted there. Both entries stay "decoded, not read".
- Shuffle controls re-run with the scripts as sent (5,000 shuffles, seeds 20261112 and 7, `lang` de-1500s): the same figures, real -3.0196 and -2.4593, 0 of 5,000 at or above the real decode at both seeds on both sets.
- Images (Wellcome IIIF, plain curl; scan 0117 has the sha256 of `PACKET_INDEX.txt`): p.124 lines 1-4 (79 signs) and p.138 lines 1-2 (40 signs) compared with the blind labels. Signs, word dividers and order agree; the differences seen on p.124 are of the kinds the contributor's diagnosis names (a closed figure 4 labelled 4L in L01 "drlcket" and L02 "clrium", and the two signs o-with-tail + 7 labelled as one ARW in L01), which supports "naming, not a wrong key value" on those lines. The other pages were not compared.
- What "blind" covers: the readers had the label sheet and no letter values, by the prompts and sheets in `blind/`; that they saw nothing else is the contributor's record. The label names 4L, 4R and 4U are the names of `key.tsv` and end in the letter each sign stands for, so the sheet is not wholly free of values.
- Kept apart: `key.tsv`, `transcription.txt`, `decryption.txt`, `reading.md`, `translation.md` and the earlier credits are unchanged by PR #686. `key_v2.tsv` is a second table beside `key.tsv` (two signs of Kohn's sheet added, no value changed), not a second key.

## pp.141-160: three blind batches with key_v2 (24 Nov 2026), decoded, not read

Malcolm McBratney (Brisbane), working with Claude (Anthropic). Read with an existing key: the key is Julius Kohn's of 1889 (key_v2 = `key.tsv` with the two of his signs added on 16 Nov); the work here is the blind transcription and its check. Files: `transcription_p141-160.tsv`, `decryption_p141-160.txt`, `reading_p141-160.md`, `translation_p141-160.md`, and `blind/p141-160/` (`README.txt`, `MAPPING.tsv`, `FETCH_LOG.txt`, `tools/`, and per batch `A/`, `B/`, `C/`: prompt, `SHEET_v2.md`, `BLIND.tsv`, FREEZE files, `key_frozen.tsv`, `decode_once.py` and its output, `judge/`, `shuffle.py`, `shuffle_out.txt`, `PACKET_INDEX.txt`). Page images are not committed: `PACKET_INDEX.txt` gives each IIIF URL with its md5 and sha256.

- **Page numbering** (`blind/p141-160/MAPPING.tsv`, recorded from the scans before any transcription and hashed in each FREEZE.txt): scans 0134-0142 = pp.141-149; 0144-0148 = pp.151-155; 0150 = p.157; scans 0151-0160 carry a second sequence 148a-157a (148a on a pasted corner patch); the main sequence resumes at scan 0161 = p.158. So scan = page - 7 holds only to p.157, and pp.161-170 are scans 0164-0173.
- **Batches** (by scan): A = scans 0134-0142 (pp.141-149); B = 0144-0148, 0150-0153 (pp.151-155, 157, 148a, 149a, 150a; 0149 = p.156 left out, its opening being in the 11 Nov reading); C = 0154-0163 (pp.151a-157a, 158, 159, 160). No upstream file or open pull request covered these scans (checked 24 Nov 2026 against main 8b75e65ac and 79 open PRs).
- **Order of events, per batch**: key_frozen.tsv (= `key_v2.tsv` byte for byte, sha256 b47062382f6c...8555), SHEET_v2, decode, shuffle and step scripts, the packet and `MAPPING.tsv` frozen 08:36:39Z (FREEZE.txt); blind transcription by Claude Fable, a separate session given only the prompt, the label sheet (no letter values) and the images, told not to decipher; BLIND.tsv frozen before the decode (A 08:50:36Z md5 aa3a8ac5...; B 08:52:11Z md5 5b467534...; C 08:58:15Z md5 a27d5785...); one mechanical decode, no emendation; one strict judging pass by Claude in a further separate session, given only the decoded letters and a brief (`judge/BRIEF.txt`); the judge's figures re-added by script (`judge/RECOUNT.txt`); the shuffle control after.
- **Transcription**: 621 lines; 12,051 signs in the key (decode_once totals 4,085 + 3,960 + 4,006), 191 doubt-marked (95 + 55 + 41), 7 `#` (batch B), 0 labels not in the key. Not compared with the images after the decode.
- **Judge, strict, by decoded letters** (first pass, figure of record; S = sense, E = one-letter slip, N = no sense):
  - A pp.141-149: S 4,054, E 31, N 0 of 4,085 = **99.2%** (per page 98.1% p.141 to 99.8%).
  - B pp.151-155, 157, 148a-150a: S 3,875, E 83, N 15 of 3,973 = **97.5%** (per page 95.8% p.152 to 98.6%). Of the 83 E, 34 are one sign decoded r where u/v is meant and 12 f for long s.
  - C pp.151a-157a, 158-160: S 3,965, E 41, N 1 of 4,007 = **98.95%**. This judge scored the decode's consistent f for long s (30 letters) as S; scored as E it is 3,935 / 4,007 = **98.20%**. Both stated.
  - The three passes together: S 4,054 + 3,875 + 3,965 = 11,894 of 4,085 + 3,973 + 4,007 = 12,065 letters = 98.58% (judges' rules differ on long s, as above).
- **Shuffle control** (`shuffle.py`, the pp.138-150 script with only the docstring changed): key_v2 letter column permuted among the sign labels, 5,000 shuffles at each of seeds 20261112 and 7, `lang` model de-1500s, order 5, letters only. Real decode A -2.2820 (4,085 letters), B -2.3560 (3,960), C -2.2295 (4,006), each matching `decode_once.txt`; shuffles at or above the real decode: 0 of 5,000 at both seeds in all three (max -5.8216 to -6.1342). Pass (rule: fewer than 5).
- **Reading check**: `docs/_check_reading.py --file reading_p141-160.md` gives a clean share of 0.466 (124 of 266 sentences; hole rate 0.153): 'marginal' (READABLE = 0.70, MARGINAL = 0.45 in the checker), below the 'readable' line, so by the checker's state the entry is **decoded, not read**. The reading file is the judges' line-by-line text with their slip marks and line-end run-ons left as written, which splits words the word list does not know.
- **Page-label correction after the blind pass**: the batch B blind reader wrote scan 0150 as "157a"; `MAPPING.tsv` gives p.157 (main sequence), and "157a" is scan 0160 in batch C. On the image the number of scan 0150 reads "157", with an "a" on a triangular corner piece beside it (patch or fold), not checked by a person against the volume. The label is corrected to p.157 in the four text files above and here; no token, letter or mark changed. The frozen files in `blind/p141-160/B/` keep "157a".
- **Content** (recipe level; English is Claude's summary from the judges' gists, unchecked): dissolving gold in aqua regis, crystallising it and bringing it to an oil with spirit of wine and sal armoniack, digestion in horse dung, sublimation and the precipitation of the mercury of gold (pp.141-149); the fixed red precipitate multiplied with mercurius solis, its use on common quicksilver and projection with borax (pp.151-155); salt of tartar made snow-white, the "arcanum philosophorum" (pp.157, 148a-150a); mercurius solis purified with salt of tartar, sealed in a Venetian glass inside an oak ball and digested in horse dung, then "Ingressus", a gold calx parted with aqua fortis and worked with aqua regis and salt (pp.151a-160). Recipes are given as 16th-century evidence only.
- **Who checked**: readers Claude Fable (blind), judges Claude (separate sessions). No person has checked these transcriptions, decodes, readings or the English.
- Prior art: as for pp.124-137 (repository only; pp.20-178 listed as unread upstream).

## Check by the project (PR #930, 24 Nov 2026)

Checked by a model session for the project (an AI agent, not a person) on the pull request as filed (head c99eb6234). No person has checked the transcriptions, the decodes, the readings or the English. Class, counts and credits are unchanged: pp.141-160 stay "decoded, not read", as filed.

- Decode: a decoder written here from `key_v2.tsv` and the three `BLIND.tsv` gives the filed letters on 621 of 621 lines (212 + 201 + 208) of `decode_once.txt`, `judge/decode.txt` and `decryption_p141-160.txt`: 12,051 signs in the key, 191 doubt-marked, 7 `#`, 0 labels not in the key. `transcription_p141-160.tsv` is the three BLIND files in order; only the page column differs, on 18 rows (157a to 157).
- Hashes (git blobs): `key_v2.tsv` on main = `key_frozen.tsv` of A, B and C (sha256 b47062382f6c...8555); all 9 non-image hashes of each `FREEZE.txt` and the three `FREEZE_blind.txt` match. `decode_once.py` is byte for byte the pp.138-150 script; `shuffle.py` differs from it in line 1 only.
- Judge figures re-added from the marks of `judge.tsv`: A 4,054 S, 31 E, 0 N of 4,085; B 3,875, 83, 15 of 3,973; C 3,965, 41, 1 of 4,007; together 11,894 of 12,065 (98.58%). No row where the marks and the number columns differ, no letter emended. `B/judge/JUDGE_NOTES.txt` says 5 `_` units where the files hold 6; the totals stand.
- Shuffle controls re-run as sent (`python -I`, `lang` de-1500s): real -2.2820, -2.3560, -2.2295; 0 of 5,000 at both seeds in all three, as in the three `shuffle_out.txt`.
- Words (the judges' word breaks, so approximate): about 2,639 words, 187 with a judge mark, 92.9% unmarked (A 96.7%, B 90.0%, C 91.9%); 88.1% if the 127 unmarked words standing on a doubt-marked sign are held as probable. Read as sentences on pp.141, 142, 152, 153, 148a and 158 and sampled elsewhere: continuous Early New High German recipe prose with single-letter slips. What keeps it at "decoded, not read": the reading is the judges' line-by-line text, the English is a page summary, and no doubtful sign was checked on the images. The doubt marks are informative: 42 of the 191 doubt-marked letters were judged E or N (22%), against 129 of the other 11,874 (1.1%).
- Images (Wellcome IIIF, plain curl): scan 0134 re-fetched has the md5 and sha256 of `FETCH_LOG.txt` and `FREEZE.txt`. 348 signs on scans 0134 (p.141 L01-L04), 0150, 0151 and 0161 agree with the BLIND labels in order, dividers and labels; the page numbers of those scans are as `MAPPING.tsv` says.
- Label sheet: 21 of the 54 labels of `SHEET_v2.md` begin or end with the letter they stand for in `key_v2.tsv` (4L, 4R, 4U, G, FL, DQ, S3 ...), 3,235 of the 12,051 signs (26.8%), so the sheet is not wholly free of values.
- Order of events: freeze files, blind files, judge files and results came in one commit, 10 minutes after the last BLIND freeze. The hashes agree with "frozen first" and cannot show it; the order rests on the contributor's record.
- Find passed on to the contributor (a model's reading of the decode and one image, not a reading of record): the "Jupiter-like" sign, a 2-like curve crossed by a stem, is written `#` six times in batch B (p.151 L24; p.152 L01, L02, L09: fi#; p.155 L14: bora#; p.150a L20: bi#e) and `4L` once in batch A (p.141 L03, e[l]empel; seen so on the image). The sense wants x all seven times (fix, borax, bixe, exempel). Kohn's sheet has two x signs (4X, LX) that `key_v2.tsv` marks as not yet seen in the text; not compared with his sheet here. It belongs in a later key table, not in this decode of record.
- Not checked: the other 27 scans, the 191 doubt-marked signs one by one, the slips on the images, the times in the freeze files, Kohn's sheet (scans 0265-0266).

## Remaining gaps
- 96 doubtful signs, mostly the three figure-4 shapes and the s-signs (143 until p.7 was re-read on the image, 14 Nov 2026: 54 there, now 7) - blocker: illegible; assigned partly from context
- p.9 lines 21-25 and two lines of p.10 - blocker: illegible; stained or damaged in the scan
- handwritten pp.11-12 (inserted narrow leaf) - blocker: needs-physical-access; no scan of its own
- p.40 beyond line 9, p.112 beyond line 5, the rest of pp.107, 115, 156, 177 - blocker: needs-physical-access; only opening lines were transcribed, the rest of those pages is a separate piece (see catalogue 1252, narrowed to pp.20-178 and the unread pages)
- pp.124-137: the four systematic slips (l/u, r/u, g/d-k, f/long s; 351 of 398 wrong letters) stay in the decode of record (first pass, 92.9%) - blocker: not-attempted; diagnosed 16 Nov 2026 as blind-reader naming plus two signs missing from key.tsv, no key value wrong (key_v2/EVIDENCE.md); tested on fresh pages pp.138-150 (95.2%), not by re-decoding these pages
- pp.138-150: the remaining slips ('de' for g 15, l/u 16, r for u/v/e 5) and 11 N letters - blocker: not-attempted; first pass of record, a re-read of the signs on the images is the next step; the g/k (ARW/OAR) shape difference rests on 5 crops
- pp.141-160 (24 Nov 2026): the slips of the first pass (A 31 E; B 83 E, 15 N, of them 34 r for u/v and 12 f for long s; C 41 E, 1 N) stay in the decode of record; pp.161-170 (scans 0164-0173) not done - blocker: not-attempted; a re-read of the slipped signs on the images, and a fourth batch for pp.161-170, are the next steps; the page label of scan 0150 (p.157, written 157a by the blind reader) wants a check on the volume
- pp.124-137: the sign-off B A M D (5 times) and 12 other N letters - blocker: too-short; clear initials or isolated signs with no value in the key
- signs of Kohn's sheet not yet seen in the text (e GT, x 4X and LX, y II and UPA, z ZH) - blocker: too-short; they do not occur in the pages read

## Escalation
- [x] siblings: pp.124-137 (the folios the margin of p.19 points to) decoded blind with the frozen key, 16 Nov 2026: 92.9% strict, shuffle 0/5,000 at two seeds; pp.138, 139, 140, 150 decoded blind with key_v2, 16 Nov 2026: 95.2% strict, shuffle 0/5,000 at two seeds; pp.141-149, 151-155, 157, 148a-157a, 158-160 decoded blind with key_v2 in three batches, 24 Nov 2026: 99.2%, 97.5%, 98.95% strict, shuffle 0/5,000 at two seeds each; the rest of MS.309 (pp.20-178, 179-207) is the unread remainder, kept as catalogue 1252 narrowed; no sibling manuscript seen
- [x] clear-pages: Kohn's key sheet (pp.260-261) is the only key or decipherment seen; no clear copy of the recipes was looked for beyond the contributor's searches
- [x] known-keys: Kohn's key (1889) applied; no other key tried
- [x] print: the contributor searched online 10-11 Nov 2026: no published reading found; German specialist literature, Kohn's papers and Wellcome files not checked
- [x] key-rebuild: Kohn's key not rebuilt; its groups were re-aligned (u, t, s) as above; key_v2 (16 Nov 2026) adds the two signs of Kohn's sheet that key.tsv left out (k OAR, l 4C), no value changed
- [n/a] retry: the doubtful signs were decoded in context as marked; no further values are open on the pages read
