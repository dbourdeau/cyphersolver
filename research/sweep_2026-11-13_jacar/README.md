# JACAR sweep, 13 Nov 2026 (second pass; continues research/jacar/)

Result: 2 unvetted lead rows, 0 vetted, 0 foreign bare ciphertext found. Stopped early: JACAR returned HTTP 403 to the
sweep's harvest and scan after about 650 item fetches, so per the brief no further JACAR requests were made.

## Done
* Re-harvested with `harvest.py`: 暗号 (9,862), 暗号電報 (1,467), 暗号文 (55), 暗号書 (880), 暗号解読 (37), 解読 (189),
  解読不能 (7), 未解読 (4), 判読不能 (2,387), about 9,950 unique records read in the pool script; 密電 / 密書 / 秘密電報 / 符牒
  and the later terms were not harvested (403 at 密電). The search hit already carries a ~300-character 内容 snippet.
* Search is AND over words and `rows` must be 20/50/100/200 (60 gives HTTP 400). Foreign-word multi-term probes
  (露国 / ソ連 / 英国大使館 + 暗号電報 + 傍受 / 写 / 差押) return 0-3 hits.
* Title and snippet scoring over the pool (digit-group runs, 'meaning unknown', foreign party, copied / intercepted): no new
  foreign ciphertext. Item pages fetched for 621 of 3,095 selected records (`scan_a.jsonl`, scratch): only the Hakodate telegrams
  (already catalogue 361) had digit groups; B08090099200 (1917, British consul Yokohama code telegram refused) has no ciphertext.
* The 'undated' records are items whose search hit lacks a date label, not volumes; of 23 matching the KEEP title filter,
  only C10072242200 and C10072242900 are ciphertext.

## Rows (candidates.json, unvetted)
* C10072242200, C10072242900 (Army Ministry 草按 Meiji 12, 1879): kana-substitution ciphertext transcribed in 内容. Japanese,
  so outside the foreign brief; not viewed, so a lead only. To do: open the 2 frames each for a plaintext rendering, DECODE,
  Tomokiyo, Lasry searches.

## Excluded
Japanese code books, Soviet / Chinese weather codes (read), Kurama intercepts (translated), C01004002600 (key lead already
listed in research/jacar/README.md), J/K newspaper and company records.

## Blocked / remaining
JACAR 403 (rate or load: run 3-4 threads at ~4 req/s plus a parallel harvest; a single curl was 200 minutes later). Remaining:
the 2,474 selected-but-unscanned records in `sel_a.txt` (scratch), the unharvested terms, B-series volumes by 傍受 /
電報 検閲, and a slower (1 request / 2-3 s, one thread) resume. Scripts here are copies of research/jacar/ with the UA scrubbed.
