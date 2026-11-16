# JACAR retry sweep and NDL check, 15 Nov 2026

Single-threaded (`scan1.py`, 2.5 s sleep plus latency); no 403 or 429 this time (one connection reset, skipped and retried on resume).

## Done
* Pool: JACAR hits in `research/jacar/hits` dated Meiji to Taisho (1920 or earlier) and not in `research/jacar/scan.jsonl`: 2,882 records.
  Prioritised the 759 whose titles mention foreign, unread, intercepted, telegram or cipher-book words (`p1_refs.txt`). All 759 item pages
  fetched (`scan_p1.jsonl`) and searched for digit-group runs and for 'meaning unknown / illegible / intercepted / seized' wording.
* Result: **no ciphertext found**. No record has a run of 4-5 digit groups. The hits are administrative: Army intercept summaries of US wireless traffic at
  Tianjin and Beijing 1920 (C03022517300 ff.), 1908-09 Chinese-student document-theft files (C10071847000 ff.), a 1912 Foreign Ministry telegram that says a
  cipher text was mailed unchanged (C08040666500, no groups quoted), Navy intercept translations 1919 (C10080900300).
* Not scanned: 2,123 records in `rest_refs.txt` (matched on body text only: war diaries, cabinet decisions). Same script will do them.
* NDL Search OpenSearch (`ndl.py`, `ndl_hits.json`, 1,338 records for 暗号電報, 電信暗号, 暗号書, 暗号解読, 密電, 書写資料 暗号): the only pre-1920 manuscript
  material is Waseda's Okuma Papers (大隈文書), 1874 Taiwan-expedition period. `candidates.json` has three entries (Motono cipher telegram, Enomoto cipher
  doubts, Taiwan telegraph cipher tables; one key each). The rest are printed commercial telegraph code books (Maruzen いろは引電信暗号 1888-98 etc.).
* Dedupe: `known.py` has no hit for the Waseda ids, hdl numbers or names; the scanned JACAR refs do not match catalogue 714-716.

## Blocks and open
* Waseda kotenseki pages gave a maintenance notice on 15 Nov 2026: the three candidates are scored from catalogue records only.
* The two '1879' Japanese rows named in the brief were not found in catalogue.json or leads.json by JACAR reference (the 1879 entries there are Chile, India, Chicago); not vetted here.
* MOFA Diplomatic Archive not queried separately (its records appear in JACAR). NDL Digital Collections with a dpid filter returned zero through OpenSearch; images not opened.
* Region is 'Other' (merge.py has no Asia value), period '1801-1900'.
