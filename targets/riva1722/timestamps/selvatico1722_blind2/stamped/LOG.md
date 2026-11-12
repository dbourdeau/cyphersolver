# b74 Selvatico blind second transcription. Exposure log (times UTC, date -u)

| time (UTC) | file opened | purpose |
|---|---|---|
| 2026-11-11 21:33:42 | ls of b70_selvatico_read/, b70/img, b57_estense_hunt/, b57/dl (names only, no contents) | orientation |
| 2026-11-11 21:33:42 | b70_selvatico_read/PARSER.md | notation spec (allowed) |
| 2026-11-11 21:33:52 | b70/img/*.jpg (10 images; images only) | source images |
| 2026-11-11 21:40:46 | (own work) work/ov_*, work/s_*, work/z*.jpg crops made from b70/img only | reading |

## FREEZE of blind transcription at 2026-11-11 21:40:46 UTC (before any b70 tx/key/ledger/dec.py, b57 tx/work, WAINUT, READING or decode was opened)
```
a2c413b7cad3573ae4848fe1ab587981  tx/blind_ALL.txt
0273b00f47d57bbb2347c62207c9984c  tx/blind_L1_10jun.txt
bea5a53ec3392fdbb61ac132db403d41  tx/blind_L2_29jul.txt
7a34fe5594d85b207e06662dd02c7d9d  tx/blind_L3_08aug.txt
eaada83d62d7e37232322ea905880127  tx/blind_L4_12aug.txt
```
Reading notes written before unblinding: digit shapes 1=stroke, 2=r-like, 3=B-like, 5=s, 7=>, 8=curl+s (also a theta-like o-with-bar form, read as 8: 25r.L7, 36r.L9, 36r.L11, 36v.L8, 36v.L15), 9=g. Lone underlined 'o' read 0_ (36v.L1, 23v.L14) or 3_? (36r.L17). Group counts and underlines taken from 0.5-0.6 scale strips; only a minority of groups were checked at full resolution. Clear text is approximate (not the object of the test).
| 2026-11-11 21:40:55 | AFTER FREEZE: b70 KEY_K3.tsv (md5 65b083be69e3a4c6219c65566aee20fc), scripts/dec.py, tx/FROZEN.md5, LEDGER_K3.tsv (head), ls of b70 scripts/tx | unblinding for decode and scoring |
| 2026-11-11 21:41:02 | b70 tx/selv1722_passC_claude.txt, tx/selv1722_passC2_8aug_claude.txt | scoring |
| 2026-11-11 21:41:15 | b70 scripts/ledger.py, scripts/agree.py, LEDGER_K3.tsv (full) | scoring |

| 2026-11-11 21:43:56 | b70/img (10 images) again for adjudication crops crops/adj_*.jpg, crops/adjsheet_1-6.jpg | adjudication of 33 disagreements |

## Results (2026-11-11 21:43:56 UTC)
```
10Jun: my units 150, b70 units 150; alignment columns = paired 150 + mine-only 0 + b70-only 0 = 150
   lookup-token agreement (digits+underline) = 146/150 = 97.33%   [of paired: 146/150 = 97.33%]
   full-token agreement (also ' and ^n; ? ignored) = 146/150 = 97.33%
   b70 S units 128 = paired 128 + unpaired 0; same lookup token 126/128 = 98.44%; lookup disagreements with a b70 S unit = 2
29Jul: my units 308, b70 units 308; alignment columns = paired 308 + mine-only 0 + b70-only 0 = 308
   lookup-token agreement (digits+underline) = 302/308 = 98.05%   [of paired: 302/308 = 98.05%]
   full-token agreement (also ' and ^n; ? ignored) = 298/308 = 96.75%
   b70 S units 279 = paired 279 + unpaired 0; same lookup token 277/279 = 99.28%; lookup disagreements with a b70 S unit = 2
08Aug: my units 761, b70 units 759; alignment columns = paired 759 + mine-only 2 + b70-only 0 = 761
   lookup-token agreement (digits+underline) = 725/761 = 95.27%   [of paired: 725/759 = 95.52%]
   full-token agreement (also ' and ^n; ? ignored) = 721/761 = 94.74%
   b70 S units 675 = paired 675 + unpaired 0; same lookup token 656/675 = 97.19%; lookup disagreements with a b70 S unit = 19
12Aug: my units 221, b70 units 222; alignment columns = paired 221 + mine-only 0 + b70-only 1 = 222
   lookup-token agreement (digits+underline) = 217/222 = 97.75%   [of paired: 217/221 = 98.19%]
   full-token agreement (also ' and ^n; ? ignored) = 216/222 = 97.30%
   b70 S units 191 = paired 191 + unpaired 0; same lookup token 188/191 = 98.43%; lookup disagreements with a b70 S unit = 3
POOLED: my units 1440, b70 units 1439; alignment columns = paired 1438 + mine-only 2 + b70-only 1 = 1441
   lookup-token agreement (digits+underline) = 1390/1441 = 96.46%   [of paired: 1390/1438 = 96.66%]
   full-token agreement (also ' and ^n; ? ignored) = 1381/1441 = 95.84%
   b70 S units 1273 = paired 1273 + unpaired 0; same lookup token 1247/1273 = 97.96%; lookup disagreements with a b70 S unit = 26
pooled check: canon_same 146 + 302 + 725 + 217 = 1390 ; cols 150 + 308 + 761 + 222 = 1441
disagreements with a b70 S unit: 33 {'LOOKUP': 26, 'MARK_ONLY': 7}

10Jun: S 124 + E 26 + N 0 = 150; STRICT 124/150 = 82.67% | outside: struck 0, catchword 0 | labelled 2nd figure, codes with a K3 value counted S: 129/150 = 86.00%
29Jul: S 278 + E 29 + N 0 = 307; STRICT 278/307 = 90.55% | outside: struck 1, catchword 0 | labelled 2nd figure, codes with a K3 value counted S: 285/307 = 92.83%
08Aug: S 649 + E 106 + N 0 = 755; STRICT 649/755 = 85.96% | outside: struck 4, catchword 2 | labelled 2nd figure, codes with a K3 value counted S: 670/755 = 88.74%
12Aug: S 186 + E 33 + N 1 = 220; STRICT 186/220 = 84.55% | outside: struck 1, catchword 0 | labelled 2nd figure, codes with a K3 value counted S: 192/220 = 87.27%
POOLED: S 1237 + E 194 + N 1 = 1432; STRICT 1237/1432 = 86.38% | outside: struck 6, catchword 2 | labelled 2nd figure, codes with a K3 value counted S: 1276/1432 = 89.11%
pooled S check: 124 + 278 + 649 + 186 = 1237
reasons: {'': 1237, 'parser': 132, 'D1 lookup differs from b70': 31, 'D2 b70 reading downgrade': 31, 'struck': 6, 'catchword, repeated at 35v.L1': 2, 'illegible': 1}
```
Adjudication (dec/ADJUDICATION.tsv): b70 right 24, b70 probably right 5, unclear 1, b74 right 3 (all three are tick marks that do not change the key lookup). Total 33.
Not opened at any time: b70 READING.md, K3_LOG.md, LOG.md, work/, crops/; b57 tx/, work/, KEY_K2; any WAINUT pass. b57 dl/ manifests not needed (b70/img used).
dec.py copy md5 6e87ffdcb1670fe00090c0bde86c8a99 (identical to b70), KEY_K3 md5 65b083be69e3a4c6219c65566aee20fc, unchanged.
