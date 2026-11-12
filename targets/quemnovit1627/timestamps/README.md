# Timestamps

One evidence folder was stamped for this letter: the breaker's folder (Track B worker b97), 12 Nov 2026, before issue
#450 was filed. Files here: `MANIFEST.sha256` (21 lines, SHA-256 of each file of that folder), the RFC 3161 request and
reply (`MANIFEST.sha256.tsq`, `.tsr`; Sectigo Public Time Stamping Signer R37), the OpenTimestamps proof as submitted
(`MANIFEST.sha256.ots`, not upgraded) and `STAMP.txt`.

- Manifest SHA-256: fbce8c883a4ea11e7f5dafbaebdf7f47c9e31ac2bc51108fad5f20235b7e1353
- RFC 3161 reply: status Granted; time 12 Nov 2026 02:25:10 GMT; message imprint equals the manifest SHA-256
  (read with `openssl ts -reply -in MANIFEST.sha256.tsr -text`). Certificate chain not verified by us.
- What it shows: the reader-1 transcription, key, unit list, decoder and reading existed in this form at that time.
  It cannot show that nobody looked earlier, and it does not cover the blind readings or the adjudication (made later
  the same day, not stamped).

Files of the manifest and their copies in this folder (SHA-256 compared on 12 Nov 2026):

| Stamped path (b97 folder) | Here | SHA-256 |
|---|---|---|
| `LOG.md` | not here | changed since (a stamp line was appended afterwards) |
| `READING.md` | `readings/reader1_reading_as_filed.md` | equal |
| `REPORT.md` | not here | changed since (a stamp line was appended afterwards) |
| `img/f443.jpg` | not here (image; large images stay out of git) | - |
| `img/f444.jpg` | not here (image; large images stay out of git) | - |
| `img/f447.jpg` | not here (image; large images stay out of git) | - |
| `img/f451.jpg` | not here (image; large images stay out of git) | - |
| `scripts/crop.py` | not in this folder | - |
| `scripts/dec_B.py` | `scripts/dec_B.py` | equal |
| `scripts/heldout_B.py` | `timestamps/stamped/scripts__heldout_B.py` | equal |
| `scripts/sheet.py` | not in this folder | - |
| `tx/quemnovit_443R.txt` | `transcriptions/reader1_frozen.txt` | equal |
| `tx/units_443R.seg` | `transcriptions/reader1_units.seg` | equal |
| `work/CODES_gloss_447.txt` | not in this folder | - |
| `work/KEY_A_v2.txt` | not in this folder | - |
| `work/KEY_B.txt` | `key_B.txt` | equal |
| `work/KEY_v1.txt` | not in this folder | - |
| `work/c443_0.50_0.10.jpg` | not here (image; large images stay out of git) | - |
| `work/decode_B.out` | `timestamps/stamped/work__decode_B.out` (and `checks/dec_B_rerun.out`, byte-identical rerun) | equal |
| `work/heldout_B.out` | `timestamps/stamped/work__heldout_B.out` | equal |
| `work/refs.json` | not in this folder | - |

The images are on the Rigsarkivet viewer: image 443 https://arkivalieronline.rigsarkivet.dk/da/billedviser?epid=19852699#261377,48900927
