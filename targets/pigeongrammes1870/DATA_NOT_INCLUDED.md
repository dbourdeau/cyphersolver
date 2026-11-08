# Data included and not included

Alexandre Pillon (collector) agreed on 8 Nov 2026, through the project owner, that his **scans and the transcriptions of them** may be published on the cyphersolver site and in this repository. The permission covers scans and transcripts only.

## Now included (with his permission)

In this folder, next to the scripts that read them:
`inspecteurs_2nov_partial.txt` (his transcription of the 2 Nov 1870 telegram), `inspecteurs_runs.txt`, `chaudordy_nums.json`, `chaudordy_nums_orig.json` and `pool.json` (group lists transcribed from his sheets),
`anchor_chain.json`, `anchors_chaudordy.json`, and the alignment and decode outputs that reproduce those sequences (`align_*_out.json`, `apply_telegram_out.json`, `apply_telegram_log.txt`, `joint_decode_final.txt`, `*_cloze_out.txt`).

On the site, in `docs/data/pigeongrammes1870/`: the AI transcriptions of the twelve page scans of the second round, as a workbook with reliability notes (`pigeongrammes_transcriptions_AI_to_check.xlsx`) and as plain text per page (`pigeongrammes_page_transcriptions_AI_txt.zip`). They are AI readings, about 96% per group, four spots unreliable and one page unreadable. Six cropped snips of the scans are in `docs/pigeongrammes1870_*.jpg`.

## Still not included

- the full-resolution scans (20-35 MB each) and `Pigeongrammes.zip` itself;
- his Excel files (`LIST_Pigeongrammes.xlsx`, `Repertoire1.xlsx`, `Repertoire2_ChiffreNouveau.xlsx`, `Repertoire3_Chiffre Stations.xlsx`, the individual dossiers): the repertoires R1, R2 and R3 remain his unpublished work;
- the derived R2 gap table (only its count is given on the page).

## Which scripts run

Checked on 8 Nov 2026 with the files above: `alpha_test.py`, `spell_solver.py`, `apply_telegram.py` and `joint_loop.py` run and reproduce the committed outputs. All of them (and `bench_loop.py`, `wiki/tools/domain_test.py`, `build_topic.py`) read OCR text of public books from hard-coded `C:\Users\dbour\enquete\` and `pigeon_src\` paths (Favre 1871, Dagron, the 1872 acclimatation article: archive.org and Project Gutenberg; see the page's Sources); fetch those and edit the paths. `bench_loop.py` also reads `Repertoire1.xlsx` (his, not included), so the benchmark cannot be re-run without it; its result is in `bench_loop_log.json`. `pigeon_pool.py` and `pigeon_full.py` read his Excel sheets and cannot be re-run; their output is `pool.json`.

Public-domain material used: Favre, *Le Gouvernement de la Defense nationale* (1871), via archive.org (`chaudordy_18dec_plain.txt` is the printed letter).
