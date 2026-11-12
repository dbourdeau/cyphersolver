# Timestamps

Three evidence folders stamped on 11 Nov 2026 (UTC), before the issue and its comment were posted. Each subfolder holds the
manifest, the RFC 3161 request and reply (Sectigo public time-stamping service), the OpenTimestamps proof as submitted
(not upgraded) and `STAMP.txt`. `stamped/` holds the stamped text files whose SHA-256 still equals the manifest line
(checked 12 Nov 2026); images are not copied. In a file name `/` is written `__`.

| subfolder | TSA time (GMT, 11 Nov 2026) | manifest SHA-256 | lines | match | copied | images not copied |
|---|---|---|---|---|---|---|
| starhemberg_1721-05-31 | 22:07:00 | 3d82d7b9c71d99f97caf103b34251fc504344df870c017e309249a23e67980a8 | 10 | 10 | 10 | 0 |
| riva_starhemberg_1720-12-21 | 23:09:47 | c464fe85d9a7d60dc93e0cdd675265e04a35fbbf2592c5344ae1a65b8da71d79 | 11 | 11 | 7 | 4 |
| riva_starhemberg_1721-06-14 | 23:29:11 | 623c4151d43443427284c72c3968396d13ff15a3b4f08a8294866076768ec030 | 26 | 26 | 11 | 15 |

- The 14 Jun 1721 folder was stamped twice (first at 23:08:15, manifest dbb4b6ad...; a mislabelled figure in its reading
  file was then corrected and the folder stamped again). The second stamp is the one here.
- Not stamped: the files written on 12 Nov 2026 for this folder (one more downgrade in the 1720 letter, the note on the
  order of the table, readings, translations, holes.md, counts.txt, NOTES.md, profile.json).
- Not verified by us: the certificate chain of the RFC 3161 replies and the OpenTimestamps proofs.
- The stamps show that these files existed at those times. They say nothing about priority over work not yet published.
