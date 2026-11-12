# Timestamps

Six evidence folders of ours were stamped on 12 Nov 2026 (UTC) before the matching issue or comment was filed. Each subfolder holds the manifest (`MANIFEST.sha256`, one SHA-256 per file with the path on our machine), the RFC 3161 request and reply (`.tsq`, `.tsr`, Sectigo public time-stamping service), the OpenTimestamps proof as submitted (`.ots`, not upgraded) and `STAMP.txt`. Layout as in `targets/riva1722/timestamps/`, except that no `stamped/` copies are made: the files of this folder that were stamped are listed below with the manifest that holds them (same SHA-256), so the folder itself is the stamped copy.

| subfolder | TSA time (GMT, 12 Nov 2026) | manifest SHA-256 | files | what it holds |
|---|---|---|---|---|
| 20261112T013639Z_petkum_30nov1665_read_in_part | 01:36:39 | 6ef31bf2bfe4cde7dea39a7b4acddf3cbbf07076ca143884e88b55f86321f83d | 22 | #443 first: R1 transcription of p2-3 and of the held-out pp.1, 4; keys v1 and v2; first decodes and unit labels |
| 20261112T014326Z_petkum_30nov1665_b94_folder | 01:43:29 | 921615ef73a70d0192d7f4ab21c6de6bc7653aeb56e3f1b8ce77a83fed86131e | 215 | #443 whole working folder incl. KEY_v3 (code 51 corrected) and images |
| 20261112T015101Z_petkum_blind_more | 01:51:01 | 2be2f96d8d05c3a4245718c62be0a2b95e56285f4e5021af865854e5b0e99c04 | 41 | blind R2 of 30 Nov and its decode |
| 20261112T020323Z_petkum_blind_more | 02:03:23 | 2127280ea4411b8afc4274111bc4ed38560ae96d42e9af88925e328609fcaac7 | 111 | #444: four letters (transcriptions, segmentations, decodes) |
| 20261112T052641Z_petkum_more2 | 05:26:41 | 22b81a5dbd162686246b9700dc30d341740418e185d7e06e985280b9ef579206 | 81 | five more letters, first reader |
| 20261112T122423Z_PAULMYER_1664 | 12:24:24 | 80f1d48d16b47f92afae16d0ab59024ab16b6c7d89f4b42f4a72864a1b0c37af | 62 | Paulmyer passage of 25 Apr 1664 (filed as 2 May) |

Checked on 12 Nov 2026 for this folder: the SHA-256 of each `MANIFEST.sha256` equals the hash given in our issues and comments, and the message imprint inside each `.tsr` reply equals that SHA-256 (`openssl ts -reply -text`). Not checked: the certificate chain of the replies and the OpenTimestamps proofs. The stamps show that these files existed at those times; they say nothing about priority over unpublished work.

## Files of this folder found in a manifest (first manifest that holds the same SHA-256)

| file in this folder | stamp | path in the manifest |
|---|---|---|
| `decryptions/paulmyer_1664-04-25.txt` | 20261112T122423Z | trackB/b146_tkua_gloss/work/decode_147L_once.txt |
| `decryptions/petkum_1665-03-24.txt` | 20261112T020323Z | trackB/b96_petkum/work/decode_24mar1665_416R.txt |
| `decryptions/petkum_1665-04-28.txt` | 20261112T052641Z | trackB/b114_petkum3/work/decode_28apr1665.txt |
| `decryptions/petkum_1665-06-23.txt` | 20261112T052641Z | trackB/b114_petkum3/work/decode_23jun1665.txt |
| `decryptions/petkum_1665-09-17.txt` | 20261112T052641Z | trackB/b114_petkum3/work/decode_17sep1665.txt |
| `decryptions/petkum_1665-11-23.txt` | 20261112T020323Z | trackB/b96_petkum/work/decode_23nov1665_568R_569R.txt |
| `decryptions/petkum_1665-11-30_R2_blind.txt` | 20261112T015101Z | trackB/b96_petkum/work/decode_R2_v3.txt |
| `decryptions/petkum_1665-11-30_p1-p4_R1_heldout.txt` | 20261112T013639Z | work/decode_heldout.txt |
| `decryptions/petkum_1665-11-30_p2-3_R1.txt` | 20261112T013639Z | work/decode_573.txt |
| `decryptions/petkum_1665-12-10.txt` | 20261112T020323Z | trackB/b96_petkum/work/decode_10dec1665_576R_577R.txt |
| `decryptions/petkum_1666-01-18.txt` | 20261112T052641Z | trackB/b114_petkum3/work/decode_18jan1666.txt |
| `decryptions/petkum_1666-04-06.txt` | 20261112T052641Z | trackB/b114_petkum3/work/decode_6apr1666.txt |
| `decryptions/petkum_1666-04-13.txt` | 20261112T020323Z | trackB/b96_petkum/work/decode_13apr1666.txt |
| `gloss/KEY_v1_gloss_377_401.tsv` | 20261112T013639Z | tx/KEY_gloss_377_401.tsv |
| `gloss/KEY_v2.tsv` | 20261112T013639Z | tx/KEY_v2.tsv |
| `gloss/KEY_v2_additions_574R.tsv` | 20261112T013639Z | tx/KEY_v2_additions_574R.tsv |
| `gloss/rowrule_check_574R.tsv` | 20261112T014326Z | trackB/b94_scan/work/tierB_check_574R.tsv |
| `key.tsv` | 20261112T014326Z | trackB/b94_scan/tx/KEY_v3.tsv |
| `transcriptions/paulmyer_1664-04-25.txt` | 20261112T122423Z | trackB/b146_tkua_gloss/tx/paulmyer_147L_R1.txt |
| `transcriptions/petkum_1665-03-24.txt` | 20261112T020323Z | trackB/b96_petkum/tx/petkum_24mar1665_416R.txt |
| `transcriptions/petkum_1665-04-28.txt` | 20261112T052641Z | trackB/b114_petkum3/tx/petkum_28apr1665_435R.txt |
| `transcriptions/petkum_1665-06-23.txt` | 20261112T052641Z | trackB/b114_petkum3/tx/petkum_23jun1665_473R.txt |
| `transcriptions/petkum_1665-09-17.txt` | 20261112T052641Z | trackB/b114_petkum3/tx/petkum_17sep1665_528R.txt |
| `transcriptions/petkum_1665-11-23.txt` | 20261112T020323Z | trackB/b96_petkum/tx/petkum_23nov1665_568R_569R.txt |
| `transcriptions/petkum_1665-11-30_R2_blind.txt` | 20261112T015101Z | trackB/b96_petkum/tx/petkum_30nov1665_R2_blind.txt |
| `transcriptions/petkum_1665-11-30_R2_blind_keynames.txt` | 20261112T015101Z | trackB/b96_petkum/work/R2_b94names.txt |
| `transcriptions/petkum_1665-11-30_p1-p4_R1_heldout.txt` | 20261112T013639Z | tx/petkum_572R_574L_heldout.txt |
| `transcriptions/petkum_1665-11-30_p2-3_R1.txt` | 20261112T013639Z | tx/petkum_573_R1.txt |
| `transcriptions/petkum_1665-12-10.txt` | 20261112T020323Z | trackB/b96_petkum/tx/petkum_10dec1665_576R_577R.txt |
| `transcriptions/petkum_1666-01-18.txt` | 20261112T052641Z | trackB/b114_petkum3/tx/petkum_18jan1666_597R.txt |
| `transcriptions/petkum_1666-04-06.txt` | 20261112T052641Z | trackB/b114_petkum3/tx/petkum_6apr1666_634R.txt |
| `transcriptions/petkum_1666-04-13.txt` | 20261112T020323Z | trackB/b96_petkum/tx/petkum_13apr1666_641L_642L.txt |
| `units/paulmyer_1664-04-25.units.tsv` | 20261112T122423Z | trackB/b146_tkua_gloss/work/units_147L.tsv |
| `units/petkum_1665-03-24.seg` | 20261112T020323Z | trackB/b96_petkum/seg/24mar1665.seg |
| `units/petkum_1665-04-28.seg` | 20261112T052641Z | trackB/b114_petkum3/seg/28apr1665.seg |
| `units/petkum_1665-06-23.seg` | 20261112T052641Z | trackB/b114_petkum3/seg/23jun1665.seg |
| `units/petkum_1665-06-23_blind.seg` | 20261112T052641Z | trackB/b114_petkum3/seg/23jun1665.seg |
| `units/petkum_1665-09-17.seg` | 20261112T052641Z | trackB/b114_petkum3/seg/17sep1665.seg |
| `units/petkum_1665-11-23.seg` | 20261112T020323Z | trackB/b96_petkum/seg/23nov1665.seg |
| `units/petkum_1665-11-30_p1-p4_R1_heldout.units.tsv` | 20261112T013639Z | work/units_heldout.tsv |
| `units/petkum_1665-11-30_p2-3_R1.units.tsv` | 20261112T013639Z | work/units_573.tsv |
| `units/petkum_1665-12-10.seg` | 20261112T020323Z | trackB/b96_petkum/seg/10dec1665.seg |
| `units/petkum_1666-01-18.seg` | 20261112T052641Z | trackB/b114_petkum3/seg/18jan1666.seg |
| `units/petkum_1666-04-06.seg` | 20261112T052641Z | trackB/b114_petkum3/seg/6apr1666.seg |
| `units/petkum_1666-04-13.seg` | 20261112T020323Z | trackB/b96_petkum/seg/13apr1666.seg |

## Not stamped

- The blind second transcription of the five letters (b115) and its segmentations (four of five; `petkum_1665-06-23_blind.seg` is byte-identical to the first reader's, which is stamped) and decodes; the three Paulmyer sister letters of 2 May, 16 May and 19 Jun 1664 (b147: transcriptions, unit files, decodes). They were made after the last stamp above. Their freeze times rest on our logs only (2 May 12:31:02, 16 May 12:33:07, 19 Jun 12:36:00 UTC; blind five frozen before 05:35 UTC).
- Everything written for this folder on 12 Nov 2026: readings/ (copied from our working files, header lines added), counts.txt, controls.txt, agreement.txt, units/units_from_seg.tsv, units/petkum_1665-11-30_R2.units.tsv, scripts/, NOTES.md, holes.md, profile.json, gloss/README.md.
- In full: `decryptions/paulmyer_1664-05-02.txt`, `decryptions/paulmyer_1664-05-16.txt`, `decryptions/paulmyer_1664-06-19.txt`, `decryptions/petkum_1665-04-28_blind.txt`, `decryptions/petkum_1665-06-23_blind.txt`, `decryptions/petkum_1665-09-17_blind.txt`, `decryptions/petkum_1666-01-18_blind.txt`, `decryptions/petkum_1666-04-06_blind.txt`, `transcriptions/paulmyer_1664-05-02.txt`, `transcriptions/paulmyer_1664-05-16.txt`, `transcriptions/paulmyer_1664-06-19.txt`, `transcriptions/petkum_1665-04-28_blind.txt`, `transcriptions/petkum_1665-06-23_blind.txt`, `transcriptions/petkum_1665-09-17_blind.txt`, `transcriptions/petkum_1666-01-18_blind.txt`, `transcriptions/petkum_1666-04-06_blind.txt`, `units/paulmyer_1664-05-02.units.tsv`, `units/paulmyer_1664-05-16.units.tsv`, `units/paulmyer_1664-06-19.units.tsv`, `units/petkum_1665-04-28_blind.seg`, `units/petkum_1665-09-17_blind.seg`, `units/petkum_1665-11-30_R2.units.tsv`, `units/petkum_1666-01-18_blind.seg`, `units/petkum_1666-04-06_blind.seg`, `units/units_from_seg.tsv`.
