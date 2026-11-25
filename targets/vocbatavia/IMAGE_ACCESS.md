# IMAGE_ACCESS (NA 1.04.02 images via the GLOBALISE IIIF manifests; plain GET, no login; 25 Nov 2026 UTC)

Viewer for the login test (Malcolm, private window): https://www.nationaalarchief.nl/onderzoeken/archief/1.04.02/invnr/1141/file/NL-HaNA_1.04.02_1141_0901 (NOT yet tested by a person). The NA site gave HTTP 503 (maintenance) on 25 Nov during the 1640 test.
Licence: NA scans of 1.04.02 are offered as public domain / CC0 by the NA (INCOMPLETE: terms page not re-checked today).

image | IIIF URL | local file md5 | pixels
1141_0901 | https://service.archief.nl/iipsrv?IIIF=/c7/6b/5f/3a/c0/9f/43/5a/93/d0/6b/72/38/d4/41/3b/92de9aff-4333-48df-8716-4a68c3cd0caa.jp2/full/max/0/default.jpg | 99eab80f15baaa4b7a102515bb8e08c8 | 3053x4138
1141_0902 | https://service.archief.nl/iipsrv?IIIF=/c7/6b/5f/3a/c0/9f/43/5a/93/d0/6b/72/38/d4/41/3b/bedaac06-b7f3-4096-a616-cdff91ecd0d9.jp2/full/max/0/default.jpg | b57f39c50d1840f071c9bff7f8d13c77 | 3042x4132
1141_0905 | https://service.archief.nl/iipsrv?IIIF=/c7/6b/5f/3a/c0/9f/43/5a/93/d0/6b/72/38/d4/41/3b/4bf28291-5f5f-4053-aee4-b9f705c69a69.jp2/full/max/0/default.jpg | 29576573811f9d1c90bfd1ff6738c3ed | 3053x4138
1141_0906 | https://service.archief.nl/iipsrv?IIIF=/c7/6b/5f/3a/c0/9f/43/5a/93/d0/6b/72/38/d4/41/3b/f5015245-9d3a-4770-8597-5d505635040f.jp2/full/max/0/default.jpg | 53842c495e88c5346c43c9d517c2f27d | 3042x4132
1141_0886 | https://service.archief.nl/iipsrv?IIIF=/c7/6b/5f/3a/c0/9f/43/5a/93/d0/6b/72/38/d4/41/3b/b4142f1b-868a-4270-a7eb-621310ca22db.jp2/full/max/0/default.jpg | b5c46b79fb59aa3ed19193711a308ef0 | 3042x4132
1141_0890 | https://service.archief.nl/iipsrv?IIIF=/c7/6b/5f/3a/c0/9f/43/5a/93/d0/6b/72/38/d4/41/3b/2a2cc57b-aa1e-4238-86c3-0de00f619c8f.jp2/full/max/0/default.jpg | 2bb878e97d61cd3a02408a671578c8c9 | 3042x4132
1134_0570 | https://service.archief.nl/iipsrv?IIIF=/be/ea/2c/5d/25/a4/44/cc/ab/03/0a/c6/c7/50/48/83/aaf5c5bd-4d7d-48fd-928c-e5b438209c90.jp2/full/max/0/default.jpg | 1479f15e898ee76f438d3e69ce48fa1f | 2930x4118
1134_0605 | https://service.archief.nl/iipsrv?IIIF=/be/ea/2c/5d/25/a4/44/cc/ab/03/0a/c6/c7/50/48/83/ad9bc69b-39d5-4d99-8ec0-5f49cbfdb876.jp2/full/max/0/default.jpg | 349546195c0e485d28374dd4f7873fe7 | 2940x4103
1134_0617 | https://service.archief.nl/iipsrv?IIIF=/be/ea/2c/5d/25/a4/44/cc/ab/03/0a/c6/c7/50/48/83/86b3d92f-261d-4a87-8d89-287f9f39e065.jp2/full/max/0/default.jpg | 8cba1b50ffe9d1bbd74ce7134e6c6b00 | 2940x4103

Fetch times: 1141 pages 21:07-21:14 UTC (0886/0890 at 21:14:20, after the first-pass stamp); 1134_0570/0605/0617 21:17-21:19 UTC. Earlier images: see letters/1640 and the trackB record.

## Crops and filing (26 Nov 2026 AEST, before the PR)
- The crop JPEGs in images/ are archive images and are NOT filed in the pull request. Their boxes are in images/crops.tsv
  (x, y, w, h in pixels of the NA IIIF full image, with a IIIF region URL that rebuilds each crop). Boxes were recovered by
  multi-scale template matching against the full images (scripts/find_crop_boxes.py; match scores 0.986-0.997).
  Test: the 1134_0583 region URL returned HTTP 200 and a 2650x1150 image at 2026-11-25T23:10:11Z.
- 1134_0583 IIIF base: https://service.archief.nl/iipsrv?IIIF=/be/ea/2c/5d/25/a4/44/cc/ab/03/0a/c6/c7/50/48/83/04c112a0-1dcb-4a3e-acb3-f20467571b0b.jp2 (full image 2940x4073, md5 9d31783b0d04c58cc7d9e3a8d5a919a6).
- The blind second readers' working crops (reader 2: 17 crops of 1134_0583; reader 3: page images and enlargements of 1141_0901/0902/0905/0906)
  are kept locally and not filed.
