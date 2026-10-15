# Van Reede (Berlin) to the Secret Committee of the States General, 24 March 1793 (DECODE R1893)

Attempted, not solved: closed unread on 21 Sept 2026 (a marked three-digit code with no key and no crib).
Write-up docs/vanreede1793.html.

Split on 14 Oct 2026 from `vanreede1787` under the one-key rule (George Lasry, 14 Oct 2026): one entry per key. The old
entry (catalogue 231) joined Arend Willem van Reede's despatches of 1787–88, which are in William V's 1782 Grand
Chiffre (DECODE key R1024), with this despatch of 1793, which is not. The Grand Chiffre letters are a different cipher,
with their own page ([`targets/vanreede1787/`](../vanreede1787/), docs/vanreede1787.html). Catalogue entry 231 was
restored on 14 Oct 2026, narrowed to R1893, as "attempted, open". The DECODE downloads (`decode/`, git-ignored, main
checkout `targets/vanreede1787/decode/`) and `fetch_decode.py` stay in `../vanreede1787/`; the scripts here read
the scans from there.

## The document

DECODE R1893 = Nationaal Archief, Staten-Generaal 1.01.02, inv. 6695: van Reede to the Secret Committee, Berlin,
24 March 1793, in Dutch (DECODE tags the language as HU, wrongly). Four pages; DECODE transcription D3608
(`ciphertext_R1893.txt`).

## The code

Three-digit groups with per-digit overmarks (~ v = ¨ +): 696 tokens, 513 distinct marked forms (`analyze_1893.py`),
so several thousand possible values. The marks are absent from the 1787–88 despatches, which is why the system was
separated from the Grand Chiffre on the first day.

## What was tried

- Keys: the 1793 Fagel key bundle on DECODE (R2842–R2852; thumbnails `fetch_key_thumbnails.py`,
  `make_thumb_montages.py`; selected pages `fetch_selected_key_pages.py`); R2846, R2848, R2850 and R2851 examined
  (numeric cells indexed with `index_key_digits.py`, `index_key_digits_generic.py`, `index_r2851_digits.py`,
  `crop_key_matches.py`, `crop_index_matches.py`; the R2851 cells addressed by R1893's groups extracted with
  `extract_r2851_cells.py`), and the interlinearly decrypted control R2243. None reads R1893.
- Ciphertext-only: with 513 distinct forms in 696 tokens, most forms occur once or twice; a code of this size cannot
  be rebuilt from this much text without a crib.

Closed until a key or a deciphered copy turns up (Staten-Generaal secret files, NA 1.01.02).

## Log

- 2026-09-20: records and transcription fetched; R1893 separated as a different system (per-digit marks).
- 2026-09-21: the Fagel key bundle and R2243 tried; ciphertext-only attack judged not feasible; closed unread.
- 2026-10-14: split from `vanreede1787`; the R1893 files moved here.

## Remaining gaps

- R1893 (24 Mar 1793, 696 tokens) - blocker: no-key-material; different three-digit overmarked code, 513 distinct forms; keys R2846, R2848, R2850, R2851, R2243 tried; no crib

## Escalation

- [x] siblings: van Reede's other DECODE records (R1026-R1029, R1057) are Grand Chiffre; the 1793 Fagel key bundle R2842-R2852 opened
- [n/a] clear-pages: no clear copy or gloss on the R1893 images in DECODE's transcription; not re-checked against the images after the split
- [x] known-keys: R1024 (Grand Chiffre), R2846, R2848, R2850, R2851, R2243 tried; no fit
- [n/a] print: no printed edition of the Secret Committee's 1793 despatches was searched; recorded as not done in the old notes
- [n/a] key-rebuild: 513 distinct forms in 696 tokens leave nothing to rebuild from without a crib
- [n/a] retry: nothing reads, so there is no extended key to retry with
