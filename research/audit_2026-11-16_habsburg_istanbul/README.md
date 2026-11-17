# Audit: Habsburg Constantinople ciphers with a 'no decipherment' regest (16 Nov 2026)

Claude Code session (Claude Opus 5.5), from the finding in `research/vetting_2026-11-16_w20_b12/` (leads 1221-1225): in HHStA
Türkei I the copy of a despatch that stays in cipher often has its decipherment, a clear copy or an extract filed elsewhere in
the same Konvolut, or a deciphered parallel letter of the same day. Catalogue entries built on a 'feloldás nélkül' regest may
therefore be read already. Proposals only: nothing applied to `catalogue.json` or `research/leads.json`.

Verdicts per entry, with regest numbers, are in `findings.json` (`status`, `evidence`, `leftover`, `recommendation`; the
multi-item entries 1226-1229 also have `items`, one verdict per regest).

## Results

| entry | status | recommendation | deciding fact |
|---|---|---|---|
| 2237 Breuner 12 May 1583 | partly filed | narrow to fol. 137-144 | 49856 (same day) is Breuner's deciphered letter to Archduke Ernst, sharing the enclosures fol. 147-151; the Rudolf despatch itself has no decipherment |
| 343 Sinzendorff 3-7 Sept 1578 | decipherment filed | close | 48372, Sinzendorff to Rudolf 3-7 Sept, 'feloldás külön', fol. 62-75; further cipher copies 48367, 48423, 48424 |
| 342 Ungnad 12 Mar 1576 | open | keep | no other regest of the day anywhere in Türkei I |
| 501 Vrančić/Zay/Busbecq 28 May 1555 | unknown | keep, check 43973-43975 and the printed Verancsics letters | the envoys' clear letter and copy of May 1555 sit next to it; none is called a decipherment |
| 2675 Wyss 11 Feb 1564 | decipherment filed | close | 44942, same day and parties, Latin cipher deciphered between the lines, fol. 73-76; the item looks like its duplicate and triplicate |
| 2676 Rym 5 Sep 1572 | decipherment filed | close | 46733, 4-5 Sep, deciphered between the lines, fol. 79-84; the item is marked 'duplicate' and has the same length |
| 885 Ibrahim pasha letters 1548 | decipherment filed | close as an open cipher | 43245 'sifrírozott orig. és feloldás'; Latin exemplars (AIS); already worked in `targets/ibrahim1548` |
| 1226 Starzer 1611-19 | partly filed | narrow | 73 items: 16 filed or probably filed, 2 parallel/partial, 55 with nothing found |
| 1227 Radibrati, Lustrier 1621-28 | partly filed | narrow | 42 items: 7 filed or probably filed, 2 parallel, 33 with nothing found |
| 1228 Schmid 1632-39 | partly filed | narrow | 28 items: 6 filed or probably filed, 2 parallel, 20 with nothing found |
| 1229 Schmid, Greiffenklau 1642-48 | partly filed | narrow | 30 items: 13 filed or probably filed (Greiffenklau's own regests point to decipherments), 1 parallel, 16 with nothing found |
| 1230, 1231, 1232, 1234, 2455, 2459, 2460 (Ungarische Akten) | open | keep | no same-letter decipherment; 1230 and 1234 have keys in the volume; 2459 has a same-day deciphered spy report (142344), probably the same cipher |
| 2457, 2458 (Ungarische Akten Fasc. 13 Konv. C, 1529) | open | keep | only 142905 (fol. 5), a separate letter, is deciphered: key material |

Catalogue 1226-1229 are the leads 1226-1229 named in the task: they were promoted and are no longer in `research/leads.json`.
Leads 1221-1225 were covered by the w20_b12 batch, not re-run here.

## Method

- `make_items.py` builds `items.json`: the single items by regest id, plus every regest in the w20_b12 'sifrír*' harvest
  (`../vetting_2026-11-16_w20_b12/raw/h_sifrir.jsonl`, 2,633 hits) for Türkei I Kt. 93-120 whose text says feloldás nélkül /
  nincs feloldva / csak sifrír / sifrírban maradt / semmi feloldás (173 regests; the catalogue rows cite 55/31/22/24).
- `audit.py` reads each item's regest in full, lists its whole Konvolut by a quoted shelfmark search (e.g.
  `"Türkei I. Karton 48. Konv. 3."`, `"Türkei I. Kt. 117. Konv.2"`, `"Fasc. 310. Konv. A."`), keeps every Konvolut regest whose
  date string shares a day with the item (range and abbreviated dates such as '1587.06.17., 06.21.' or '1613.05.11. 12.' are
  expanded, which the date search alone misses) or carries no full date, adds every Türkei I hit of a quoted date search for each
  day, and reads all of those in full. 193 items, 1,099 regests read; listings and date searches cached in `raw/konv/`, `raw/dates/`.
- `report.py` and `classify.py` print the result for reading; `verdicts.py` sets a first verdict by rule (the item's own regest
  points to its decipherment; or a same-day regest of the same sender and recipient names a decipherment, clear copy, extract or
  copy = filed; same sender, item names no recipient = probable; same sender, other recipient = parallel); `finalize.py` applies
  ten hand corrections made after reading (listed in the script) and writes `findings.json`. The single-letter verdicts
  (`singles.json`) were written by hand from the regests.
- Hungaricana answered plain urllib requests from this machine with a browser User-Agent, one request per 1.2 s. No Chrome.

## Limits

- Regests only; no leaf was seen. 'Filed' means the archive's regest names a decipherment, clear copy or extract of the same
  letter, or a same-day, same-parties deciphered piece that by length and duplicate marks is the same letter (343, 2675, 2676 rest
  on that inference). 'Probable' items name no recipient.
- The 1226-1229 item list comes from the 'sifrír*' harvest: an item whose regest says 'no decipherment' without the word
  sifrír (e.g. 'titkosírás') is not in it. Of the 'nothing found' items in 1226-1229 a sample was read by hand; the rest rest
  on the rule.
- A decipherment filed in another Konvolut under a different date (e.g. dated by arrival) is found only when a regest points
  to it; several do (57866 → Kt. 103 Konv. 1; 58141 → Kt. 103 Konv. 2), and others may exist.
- Not checked: 503 (AIS only, Ungarische Akten 425-53), 516, 2288, 2299, 2816 (not Hungaricana regest entries), the Thököly
  letter of 1682 in 1230, the printed Verancsics correspondence for 501, and the Potesta translations index (146427) for 2455.
