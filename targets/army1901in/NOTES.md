# Japanese Army serial kana table of 1901: telegrams to the General Staff (JACAR C09122805800 ff.)

Contributed by Harumi-Matsuba (GitHub issue #371, 10 Nov 2026; repository
https://github.com/Harumi-Matsuba/kagigo1901-public, commit 7a627e4, `docs/READING1901.en.md`, `src/table1901.py`; code MIT,
documents and data CC BY 4.0). Integrated and checked here 10 Nov 2026. Not in the catalogue. Page: `docs/army1901in.html`.
Outside the LLM paper's scope (Japanese; contributed). Different tables, each with its own target: `targets/army1901/`
(the General Staff's outgoing drafts of the same months, catalogue 715) and `targets/army1902/` (1902-04).

## The cipher

Telegrams in romanised Japanese (one in katakana) from officers in China and Hiroshima to the General Staff, Feb-Apr 1901:
only the sensitive words are in digits, two per kana, sent in groups of five. The table numbers the syllabary row by
vowel row with voiced kana right after the plain one, 00 (ア) to 67 (ン). `texts/key.md`.

The telegrams were read at the time: each has its contemporary translation in the same file, and in some the recipient
wrote the kana beside the digits. What is new is the reconstruction of the table.

## The telegrams

| JACAR | frame | date, route | role | pairs | agree |
|---|---|---|---|---|---|
| C09122805800 | 0237 | 2 Mar 1901, Taku: Fukushima -> Tamura, No. 93 | build | 23 | 23 |
| C09122805900 | 0241 | 25 Feb 1901, Taku: Fukushima -> Tamura, No. 92 | build | 4 | 4 |
| C09122806000 | 0243 | 22 Feb 1901, Taku: Fukushima -> Tamura, No. 89 | build | 4 | 4 |
| C09122801000 | 0155 | 22 Apr 1901, Taku: Fukushima -> Tamura, No. 9 | build | 11 | 11 |
| C09122724200 | 0325 | 23 Feb 1901, Taku: Lt.-Gen. Yamaguchi -> General Staff | build | 14 | 14 (three digits re-read with the table) |
| C09122796200 | 0071 | 8 Mar 1901, Chungking: Capt. Idogawa -> Fukushima | test | 10 | 10 |
| C09122806100 | 0245-0246 | 18 Feb 1901, Hiroshima: Maj.-Gen. Manabe -> Tamura (kana telegram) | test | 14 | 11 |
| total | | | | 80 | 77 |

C09122806100 was listed as unread in `targets/army1902/` (the 1902-04 table does not read it). With this table:
45 67 18 65 28 = テンシヨク (translation 転任, transfer; the digits say 転職), 67 20 14 = ンチワ (任地ハ), 34 28 37 = フクム (服務).
91 stands twice where the translation has ニ就キ / ニ就テ (Satoshi Tomokiyo's alignment at the group level, meijiarmy2.htm),
69 where 任地 has ニ (the table's ニ is 21). The 〇 at the head and the 一 at the end of the first run are left over when it is
cut into pairs.

## Checks made here (10 Nov 2026)

- `decode.py` written from the stated table (does not import the contributor's code): 77 of 80 pairs give the kana of the
  filed translations; the misses are 91, 91, 69 (`decode_out.txt`). Note: the first version of `targets/army1901/decode.py`
  carried a wrong copy of this table (ヂ, ヅ inserted, 70 values); fixed 10 Nov 2026, its out-of-range count (21 of 148) unchanged.
- Shuffled-table control on the two test telegrams (`python decode.py control`, seed 1901, 1,000 tables): real table 21
  kana agree, shuffled max 5, mean 0.27 (`control_out.txt`). The contributor's figure: 0 of 1,000 random permutations as good.
- The contributor's second transcription (Codex, blind): 123/135 digits, lowest telegram 75.0% (C09122801000).
  JACAR unreachable from this session, so no digit was checked against the images here; no human has checked them.
- The contributor's "16/16" counts the two test telegrams together: the 10 kana of C09122796200 and ンチワ, フクム of
  C09122806100. Counted here per telegram: 10/10 and 11/14 (テンシヨク included, the three off-table pairs as misses).
- Prior work: contributor's search of 10 Nov 2026 (Cryptiana meijiarmy.htm, meijiarmy2.htm, meijijapan2.htm, unsolved.htm;
  this repository; GitHub; web) found no earlier reconstruction. Not checked: the books of Nagata, Sasaki and Ōno; NIDS originals.

## Remaining gaps
- C09122806100 values 91 (twice) and 69 - blocker: no-key-material; outside the table, 91 apparently a code for ニ就キ; no code list found
- C09122724200 three digits re-read with the table in hand (first readings 72542, 45075, 02948) - blocker: illegible; poor image, and JACAR was not reachable from this session to look again

## Escalation
- [x] siblings: the contributor viewed the 1901 telegram files; the outgoing drafts of the same months use another table (army1901)
- [x] clear-pages: the filed translations of all seven telegrams used as cribs or checks
- [x] known-keys: the 1902-04 table (army1902) does not read C09122806100 (army1902 NOTES); the outgoing grid (army1901) is a different arrangement, not tried on these
- [x] print: contributor's prior-work list (PRIOR_CHECK.en.md); Cryptiana pages; nothing found
- [x] key-rebuild: 38 values attested, 30 filled from the arrangement; 68-99 unknown
- [x] retry: every telegram re-decoded here with the completed table; 69 and 91 stay off the table

## Files
- `ct_<JACAR>.txt`: digit runs with the translation's kana (contributor's `data/telegrams1901.tsv`)
- `decode.py`, `decode_out.txt`, `control_out.txt`; `texts/<JACAR>_reading.md`, `_en.md`, `texts/key.md`
