# Protocol records (freeze order)

Copied unchanged from the contributor's working folder (16 Nov 2026), so that the order of events can be checked by hash.
The order itself (which file was written before which) rests on file times in that folder: **by the contributor's record**.
The crops sent to Claude Fable 5.2 (lot 15) and the arbitration crops are not committed (Gallica images, Source gallica.bnf.fr / BnF);
their SHA-256 are in `lot15-sent-files.sha256` (paths shortened to the folder; no crop of f. 207v, view 216 cut at x >= 0.445).

| Record | Working name | File in this target |
|---|---|---|
| choice of the blind portions | CHOIX-PORTION*.md (+ .sha256) | protocol/ |
| key v1 / v3 / hand 2 | key_main1_v1.json, key_main1_v3.json, key_main2_fable.json (= Fable's KEY-PROPOSAL-MAIN2.json as returned, same hash) | key_hand1.json, key_hand1_v3.json, key_hand2.json |
| scripts | tools/measure.py, measure_v3.py, measure_main2.py | measure.py, measure_v3.py, measure_main2.py |
| transcriptions B / C / H | B_f161r_*, C_f160v_*, fable2/H/H_f207v_* | f161/, f160/, f207v/ (read1, read2, read_final) |
| sign codes hand 2 | GLYPHS-MAIN2.md | f207-209/GLYPHS-hand2.md |

All hashes listed in PREREG*.sha256, B_/C_/H_*.sha256 match the committed files (checked 17 Nov 2026).
PREREG-v4 (key_main1_v4.json, measure_v4.py) was never run; those two files are not committed.

Timeline (file modification times, 16 Nov 2026, CET; by the contributor's record):

| Step | B (f. 161r) | C (f. 160v) | D (f. 161v) | H (f. 207v) |
|---|---|---|---|---|
| portion chosen | 11:31:40 | 12:32:59 | 12:48:24 | 11:15:19 (addendum later the same day) |
| key frozen | 11:34:29 | 12:36:36 | — | 18:18:36 |
| PREREG frozen | 11:35:35 | 12:36:45 | 12:50:41 | 18:19:34 (sha file 18:19:40) |
| first crop / pass 1 | 11:40:02 | 12:39:03 | 12:54:12 (287 signs: stopped) | first crop 18:19:52; pass 1 18:22:31 |
| pass 2 / final | 11:41:40 | 12:46:03 | — | 18:25:04 / 18:25:06 |
| measurement | 11:41:51 | 12:46:17 | not run | 18:25:21 |

Both transcription passes of each portion were made by the same agent (Claude Opus 5.5) in the same session, the second
on different crops without reopening the first file; they are not independent readers.
