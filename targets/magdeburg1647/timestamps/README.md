# Timestamps

One evidence stamp covers this target: `20261113T090853Z_fable_reply_ourkeys/`, made on 13 Nov 2026 before our keys were sent
to a second (AI) reader. It holds the manifest (`MANIFEST.sha256`, 11 lines: SHA-256 and path of each file sent), the RFC 3161
request and reply (`.tsq`, `.tsr`, Sectigo public time-stamping service), the OpenTimestamps proof as submitted (`.ots`, not
upgraded) and `STAMP.txt`.

| subfolder | TSA time (GMT) | manifest SHA-256 | lines | lines for this target | copied to `stamped/` |
|---|---|---|---|---|---|
| 20261113T090853Z_fable_reply_ourkeys | 13 Nov 2026 09:08:54 | 650a82c9ed32e84d9021fafd95b5637b62343799e5b6e19fb2ed0ac8762fee9f | 11 | 3 | 2 |

- `stamped/LASA530_KEY_v2.txt` (SHA-256 f1378d6b...) is byte-identical to `gloss/KEY_lasa_v2.txt` (md5 c8fade56), the frozen key used for
  every decode in this folder.
- `stamped/REF_GLYPHS.txt` (SHA-256 b0dfe96c...) is byte-identical to `gloss/REF_GLYPHS_b162.txt`, reader 2's glyph sheet.
- The third line for this target, `reference/REF_SHEET_f51_f3.jpg` (SHA-256 3ea4fac2...), is not copied: it is a sheet of crops
  of the archive's images of frames 3 and 51.
- The other eight lines are files of other targets (hashes only; their files are not part of this pull request).
- The RFC 3161 reply was read with `openssl ts -reply -text`: status Granted, time 13 Nov 2026 09:08:54 GMT, TSA Sectigo Public
  Time Stamping Signer R37, message imprint = the SHA-256 of `MANIFEST.sha256`. Not verified by us: the certificate chain and the
  OpenTimestamps proof.

What the stamp shows: the frozen key existed, unchanged, by 13 Nov 2026 09:08:54 GMT. It is about 19 h 21 min after the key's
freeze recorded in the b160 session log (12 Nov 2026 13:47:27 UTC). The transcriptions, decodes, ledgers and shuffle outputs are
not in any stamp; their order (freeze, then one decode) rests on the session logs, copied in `transcriptions/FREEZE_LOG.txt`, and
on the md5 of each frozen file, which every decryption header repeats. Not stamped: everything written for this folder on
13 Nov 2026 (key.tsv, units/*.tsv, readings, translations, counts.txt, NOTES.md, profile.json).
