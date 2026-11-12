# Timestamps

Three evidence folders were stamped on 12 Nov 2026 (UTC) before issue #453 and its second comment were posted. Each subfolder
holds the manifest (`MANIFEST.sha256`: SHA-256 and path of every file in the work folder at that moment), the RFC 3161
request and reply (`.tsq`, `.tsr`, Sectigo public time-stamping service), the OpenTimestamps proof as submitted (`.ots`, not
upgraded) and `STAMP.txt`. `stamped/` holds a selection of the stamped text files, copied only where their SHA-256 still
equals the manifest line (checked on 12 Nov 2026 when this folder was built). In a file name `/` is written `__` and the
leading work-folder name is dropped.

| subfolder | TSA time (GMT, 12 Nov 2026) | manifest SHA-256 | lines | match now | copied | what it fixes |
|---|---|---|---|---|---|---|
| 20261112T025406Z_bonde_2317 | 02:54:07 | bac9c4c652d1d1f0758d0795ab23071640d73498fbd1ab98de799550cf066949 | 67 | 65 | 12 | keys v1, v2, v3 (as `KEY_v3_posthoc.tsv`), the 102R gloss lines, the 107L control, the image-324 training and test lines and their first decode |
| 20261112T031020Z_bonde_memorial_1676 | 03:10:20 | 8bdcf24e95c565f49bb562a6facdeed08fa68caae02f33e4af0bd8344fcc53a5 | 90 | 88 | 17 | key v3, the six pages of f.307v-311r, their segmentations, tally and shuffle output |
| 20261112T035321Z_bonde_memorial_opening | 03:53:21 | dacc238e0ff924bf71428319aa49520353675d6ebaab9d6577974446952b8921 | 109 | 108 | 10 | f.306r-307r transcriptions, segmentations, freeze record, tally and shuffle output, the reading |

- Lines that no longer match: `LOG.md` and `REPORT.md` of the first two folders and `LOG.md` of the third. Each had lines
  appended after its stamp (the stamp line itself, as each log declares). They are not copied.
- Images (40, 43 and 45 crops and strips in the three manifests) are not copied: they are the archive's images cut up.
- Checked by SHA-256 against the manifests: `key.tsv`, all eleven files in `transcriptions/`, all files in `segmentation/`
  and the b101 second transcription of image 324 are byte-identical to stamped files. The b103 blind files in
  `second_transcription/` are not in any stamp.
- The RFC 3161 replies were read with `openssl ts -reply -text`: the times above, and each message imprint equals the
  SHA-256 of its `MANIFEST.sha256`. Not verified by us: the certificate chain of the replies and the OpenTimestamps proofs.
- What the stamps show: these files existed at those times. The freeze-before-decode order inside each session rests on the
  session logs (`FREEZE.txt`, `LOG.md`), which the stamps cover but do not prove; the stamps came minutes after each decode.
- Not stamped: everything written for this folder on 12 Nov 2026 (overrides.tsv, the readings in this form, holes.md,
  counts.txt, NOTES.md, profile.json), and the blind second transcription of b103 (its freeze is in
  `second_transcription/BLIND_FREEZE.txt` only).
