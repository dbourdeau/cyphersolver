# Timestamps

Seven evidence folders were stamped on 11 Nov 2026 (UTC), before the issues were filed. Each subfolder holds the manifest
(`MANIFEST.sha256`), the RFC 3161 request and reply (`.tsq`, `.tsr`, Sectigo public time-stamping service), the
OpenTimestamps proof as submitted (`.ots`, not upgraded) and `STAMP.txt`. `stamped/` holds the stamped text files, copied
only where their SHA-256 still equals the manifest line (checked on 12 Nov 2026). In a file name `/` is written `__` and the leading work-folder name is dropped.

| subfolder | TSA time (GMT, 11 Nov 2026) | manifest SHA-256 | lines | match | copied | not copied |
|---|---|---|---|---|---|---|
| riva1722_1726 | 21:08:17 | 3ceef5f0b362b5c50c0f59a5b6bbfbbdd3d3e65a8a6618847805753d94e5d2c7 | 16 | 16 | 13 | 3 third-party files (see below) |
| selvatico1722_4letters_partial | 21:30:31 | 990f5d145f66ad6059a66c33160005339be08accb1d07557882bcc8b701fe150 | 28 | 27 | 26 | 1 large file; 1 file changed since (the log, which had its stamp line added) |
| selvatico1722_blind2 | 21:43:56 | 16b23329b5ad9d591f7205a9ac5511bb30d90340c919987ef3c2d79baf99e986 | 127 | 127 | 28 | 99 images |
| selvatico_undated_cc2_14 | 21:55:54 | 0a958e110b8fac4c512f1e7db08cb4d76fd8304a19ec832dd424fb06974e4c7a | 73 | 72 | 27 | 45 images; 1 file changed since (the log) |
| starhemberg_1727-02-19 | 22:04:28 | 77cc6460343dee145ad83c72534ed6bc1d1c5961ada8ea052918ab7d07763b60 | 10 | 10 | 10 | 0 |
| olivazzi_1725-04-17 | 22:13:06 | 6fc391b6323d8478ce11ed893ab8e099ff61f39e38b66e326bdc30a59c30fb84 | 12 | 12 | 12 | 0 |
| olivazzi1725_pass2 | 22:25:51 | d76bbcfcce9cd3f8f1d5ac9d63416df2793422199420cecd21670778bd8ea57d | 105 | 105 | 27 | 78 images |

- Three stamped files of `riva1722_1726` are copies of another contributor's transcriptions of the 1722 letters (the two
  passes in `targets/selvatico1719/work/` and a decode of one). They are in the manifest but are not copied here.
- The frozen transcriptions are in `stamped/`: the 20 Mar 1726 pass A (before any key), the 1722 passes C and C2, the blind
  second transcription of the 1722 letters (`tx__blind_*.txt`), pass D of the undated letters, the 1727 pass A, the two
  Olivazzi passes and their consensus.
- Not stamped: everything written on 12 Nov 2026 for this folder (the 1726 notation change and its K3 decode, overrides
  for 1726, readings, translations, holes.md, counts.txt, NOTES.md, profile.json).
- Not verified by us: the certificate chain of the RFC 3161 replies and the OpenTimestamps proofs. What was checked: the
  SHA-256 of each manifest equals the hash printed in the issues, and the stamped files above equal their manifest lines.
- The stamps show that these files existed at those times. They say nothing about priority over work not yet published.
