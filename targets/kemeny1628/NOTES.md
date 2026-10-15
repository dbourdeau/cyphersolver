# Kemény collection cipher letters, DECODE R4933-R4935 (Kemény_XIX_1628)

Status: in progress

Split on 14 Oct 2026 from `targets/transylvania1645/` under the one-key rule (George Lasry, 14 Oct 2026). That target
grouped ten DECODE records by their number range (R4933-R4942) across two collections and three decades. These three
are the Kemény_XIX_1628 records, a different collection, writer and decade from the Keresdi Bethlen letters of
1645-48 (`targets/transylvania1645/`, a different cipher as far as is known, with its own entry) and from R4941
(`targets/r4941/`). No key is claimed for them, shared with each other or with the Bethlen family.

## Records

| Record | DECODE name | DECODE year | Images | Symbol sets (DECODE) | State |
|---|---|---|---|---|---|
| R4933 | Kemény_XIX_1628_1 | 1658 (name says 1628) | 2 | alphabet, numerical | two spreads photographed; date conflict to resolve on the leaves; not transcribed |
| R4934 | Kemény_XIX_1628_2 | 1628 | 2 | graphic signs, alphabet, numerical | mostly cipher-looking text; not transcribed |
| R4935 | Kemény_XIX_1628_3 | 1628 | 4 | alphabet | largely clear text with short cipher insertions; not transcribed |

Romanian National Archives, Cluj. Access mode on DECODE: authentication required. The images (downloaded 23 Sept 2026,
hashes and URLs in `targets/transylvania1645/image-manifest.json`) are git-ignored and live in the main checkout under
`C:\Users\dbour\cypher\transylvania1645\` (`IMG_R4933_*`, `IMG_R4934_*`, `IMG_R4935_*`). Metadata: `R4933-metadata.txt`,
`R4934-metadata.txt`, `R4935-metadata.txt`.

## Next work

1. Inspect every image; transcribe the cipher spans of each record separately.
2. Decide per record whether the three share a system; test the Bethlen family mapping only as one hypothesis among
   others, and only after a transcription exists.
3. Resolve R4933's catalogue date (1658 vs 1628) and the writers from the clear text.
4. Record every step in `profile.json` (`python docs/_check_profile.py kemeny1628`).

No write-up while in progress.
