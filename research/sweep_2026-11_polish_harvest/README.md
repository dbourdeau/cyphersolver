# szukajwarchiwach 1900-50 and Radom harvest (2 Nov 2026)

The Chrome localStorage key `szh` (1,883 records, 67 terms) was still in the profile. Saving it to disk failed: a POST from
the https origin to a local receiver on 127.0.0.1 never completed (probably Chrome's local-network permission, which only
the user can grant), so `szh.json` is not on disk. The records were triaged inside the page instead.

## Counts
- 1,211 records start in 1900 or later (excluding Radom); 309 have a scan flag; about 400 match a cipher word in title/note.
- Radom, fonds 58/387: 125 records (115 per the earlier note), 9 with scans. All are Holocaust-era person cards where
  "Szyfra" is a Jewish given name. Zero rows.
- The 1900-50 hits are nearly all noise: the first name Szyfra, shop-owner "Szyfra X" court files, police cipher
  instructions (Policja Państwowa 1931-39), Biuro Szyfrów administration, PPR/Communist Party szyfrogramy 1945-48, WWII
  underground dispatches, telegram-cipher care in ministries, thieves' house-marks (NAC 3/1/0/3/110).
- Four items are kept as rows (candidates.json): KNP cipher-section dispatch copies 1919, a Ukrainian cipher telegram 1919,
  Skrzyński-Paderewski cipher dispatches 1919, Lublin passwords and ciphers 1916-18. known.py found none of them.
  Skipped on purpose: Paderewski private telegraph code 1922 (a code book), 2/106/0/1/1.5 (1927-28 embassy telegrams),
  705/2/0/-/30 (1929-33 embassy cipher telegrams, no scan).

## Result
4 rows, not 60. This source has no more real ciphered letters in 1900-50. No row has been viewed; each is scored from its
catalogue description.

## Not reached
The ~400 cipher-word records were read by title only; about 130 pre-1939 non-scanned titles were skimmed in batches of
13-14 and none looked like a cipher letter. The 1939-50 set was dropped as WWII/Communist-era telegram noise.
Nothing blocked; no check appeared. Prior-art search (Tomokiyo, Lasry, editions) not done.
