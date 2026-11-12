# Timestamps

One evidence folder was stamped on 12 Nov 2026 (UTC) before issue #476 was posted. The subfolder holds the manifest
(`MANIFEST.sha256`), the RFC 3161 request and reply (`.tsq`, `.tsr`, Sectigo public time-stamping service), the
OpenTimestamps proof as submitted (`.ots`, not upgraded) and `STAMP.txt`. `stamped/` holds a selection of the stamped
text files, copied only where their SHA-256 still equals the manifest line (checked when this folder was built). In a file
name `/` is written `__` and the leading work-folder name is dropped.

| subfolder | TSA time (GMT, 12 Nov 2026) | manifest SHA-256 | lines | match now | copied |
|---|---|---|---|---|---|
| 20261112T062527Z_bonde_despatch_1677-11-24 | 06:25:27 | 2826a3385f5c7b06bb7a7f9b95f1d8590715fcac6fd97b068366e42722f6cd5a | 138 | 137 | 10 |

- The line that no longer matches is the session log (`work/LOG.md`), which had its stamp line appended. Not copied.
- 93 manifest lines are images and crops (the archive's images cut up): not copied. The other stamped files are the session scripts and the files of the
  despatch of 17/27 Nov 1677 (479R-481R), decoded in the same session below our threshold and not filed: not copied.
- Checked by SHA-256 against the manifest: `key.tsv`, the transcription, its doubts file and the segmentation in this folder
  are byte-identical to stamped files. The blind second transcription (b127) is in no stamp; its freeze record is
  `second_transcription/BLIND_FREEZE.txt`.
- The RFC 3161 reply was read with `openssl ts -reply -text`: time 06:25:27 GMT; its message imprint equals the SHA-256 of
  `MANIFEST.sha256`. Not verified by us: the certificate chain and the OpenTimestamps proof.
- What the stamp shows: these files existed at 06:25:27. It came after the decode (06:24:26). The freeze of key v9
  (06:08:58) and of the transcription (06:24:26) before the decode rests on the session logs and `tx/FREEZE.txt`, which the
  stamp covers but does not prove. Key v9 itself was not stamped before this page was transcribed.
