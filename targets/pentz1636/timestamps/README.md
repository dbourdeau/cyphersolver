# Timestamps

Two of our evidence stamps cover files in this folder. Each subfolder holds the manifest (`MANIFEST.sha256`), the RFC 3161 request and reply (`.tsq`, `.tsr`, Sectigo public time-stamping service), the OpenTimestamps proof as submitted (`.ots`, not upgraded) and `STAMP.txt`. `stamped/` holds the stamped text files that belong to this target, copied only where their SHA-256 still equals the manifest line (checked when this folder was built, 13 Nov 2026). In a file name `/` is written `__`.

| subfolder | TSA time (GMT) | manifest SHA-256 | lines | copied |
|---|---|---|---|---|
| 20261112T041403Z_b106_zobel1629_pentz1636 | 12 Nov 2026 04:14:03 | 3eec360077380e34b7976920511aadf087f8ae4086f6bc81960457b219427815 | 40 | 4 |
| 20261113T090853Z_fable_reply_ourkeys | 13 Nov 2026 09:08:54 | 650a82c9ed32e84d9021fafd95b5637b62343799e5b6e19fb2ed0ac8762fee9f | 11 | 3 |

What each stamped file is here:

| stamped file | SHA-256 (start) | same bytes as |
|---|---|---|
| b106: `tx/pentz_1636-03-26.txt` | b694bbc3 | `transcriptions/vienna_1636-03-26.txt` |
| b106: `scripts/dec_pentz.py` | a3855b18 | `scripts/original/b106_dec_pentz.py` |
| b106: `work/dec_pentz_run1.txt` | 6ed6e95d | `scripts/original/b106_dec_pentz_run1_output.txt` |
| b106: `work/KEY_pentz.txt` | 386398f8 | `key_history/KEY_pentz_v1_b106.txt` |
| fable: `PENTZ1636_KEY_v1.txt` | 386398f8 | `key_history/KEY_pentz_v1_b106.txt` |
| fable: `PENTZ1636_tables_T1T2.py.txt` | a717fb73 | `key_history/KEY_pentz1636_T1T2.py` |
| fable: `PENTZ1636_KEY_v2.txt` | b13a8ca8 | `key_history/KEY_pentz_v2_b110.txt` |

- The other 36 lines of the b106 manifest are the Zobel and Charisius files of the same session and the page images and crops: not copied (Zobel is `targets/zobel1629`). The other 8 lines of the fable manifest are other targets' keys and a handover note: not copied.
- Both RFC 3161 replies were read with `openssl ts -reply -text`: their message imprints equal the SHA-256 of the manifests. Not verified by us: the certificate chains and the OpenTimestamps proofs.
- What the b106 stamp shows: the Vienna transcription, the decoder with its key tables and the run output existed at 04:14:03 GMT on 12 Nov. It came after the decode (the transcription was frozen at 04:11:09 UTC by the session log). The freeze before the decode rests on that log, not on the stamp.
- **The Glückstadt files are in no stamp.** The transcription (md5 1e70795f, frozen 12 Nov 2026 13:30:55 UTC by the b157 log), the key copy the decode used (md5 8306f733) and the decode output were not stamped before this pull request. The key copy is byte-identical to the stamped `PENTZ1636_tables_T1T2.py.txt` (stamped 13 Nov, after the decode). The only record of the Glückstadt freeze is the session log.
