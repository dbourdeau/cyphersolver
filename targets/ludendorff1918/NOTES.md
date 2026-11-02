# Ludendorff → German military attaché Stockholm, and Berlin → Legation and Consulate-General Stockholm, July 1918 (catalogue 656)

Status: attempted, open. Not deciphered. Six telegrams of five-figure groups whose figures are flat in every column, with
no key anywhere we could reach. The sibling numeric-code telegrams (catalogue 654) have their own folder:
`targets/stockholm1918/`, which also holds the shared test scripts in `work/`.

## The documents

NARA RG 59, M367, enclosures of Stockholm despatches 1426 and 1475. The US Legation obtained the copies and re-cabled most
from Christiania as telegrams 1233–1236 (763.72/11668). Stockholm 2952 reports "number nine to German Military Attaché ...
signed Ludendorff". `transcription.txt` has every group.

| Telegram | Header | Groups | Frame | Cable copy |
|---|---|---|---|---|
| w791 | SSD GRHQU S M POL ABT BEFSTOHL 26/7, "Sehr dringend", to DEUTSCHER MIL ATT STOCKHOLM, 5 Teile | 170 | roll 141 f. 1264 | roll 108 ff. 0705–09 |
| w769 | berlin 217 50, 26th 11:40, legation allemande sthlm | 45 | roll 141 f. 1257 | roll 108 ff. 0698–99 |
| w716 | berlin 215 28w, 26th 7:10, legation allemande sthlm | 23 | roll 141 f. 1258 | roll 108 ff. 0699–0700 |
| w592 | Berlin 73350 31, 26th 10:30, Deutsches Generalkonsulat Stockholm | 23 | roll 141 f. 1260 | roll 108 ff. 0722–23 |
| w628 | Berlin 178 52, 22nd 8:25, Legation Allmande Stockholm | 47 | roll 122 f. 0156 | none found |
| w611 | berlin 67352 33, 22nd 5:55, Kaiserl deutsche gesandtscha stockholm | 20 | roll 122 f. 0157 | none found |

w791 is headed "5 Teile" and each part carries "teil / urachi / n gruppen / 26 7". The declared counts are 39, 30, 38, 31,
33 (the catalogue read the first as 29). Our count is 39, 30, 37, 31, 33: part 3 has four struck groups on the frame, one of
which must be real. It ends "nr 34298 p roem 4 Ludendorff". It is the Ludendorff telegram: GRHQU is Grosses Hauptquartier.

## The clear words

These are facts on the frames. What they stand for is open.

- "urachi" stands in each part of w791 where a key word or indicator would stand [?].
- w628, w769, w716 open with a spelled number and a ten-letter pronounceable word: "Fuefsecho Ifesuijuni" (22nd), "funfacht
  vanadopote" (26th), "funfneun cavesaltri" (26th). Read as German numerals these are fünf-sechs, fünf-acht, fünf-neun: 56,
  58, 59, which climb with the date, so probably a running number of this channel [?].
- w611 opens "hansa 22 juli" and has clear names between its groups: vera, lilly, vera, vera hanna, LOLO. They are possibly
  cover names or a telegraphic disguise [?].
- w592 opens "2507 18" and ends "bidenus 177/2", and one group is garbled to letters (5710v oh110).

## What was measured

`../stockholm1918/work/kappa.py`, `addsearch.py`, `slider.py`, `family.py`.

- **Flat figures.** Index of coincidence per column of the five-figure groups: 1.01, 1.04, 1.02, 1.06, 1.01 for w791 and 1.04,
  1.03, 0.99, 0.97, 1.04 for the others (1.00 = uniform). The catalogue's sibling systems are not flat: their first column
  reaches 2.5 to 9.8. There is no sign of an ordinary code with a limited page range here.
- **Almost no repeats.** Of 328 groups, 71903 occurs twice in w791 (7 apart) and 03515 twice in w628 (28 apart). Chance predicts 0.5
  pairs. If the text were an additive over a code, a repeat means the same word under the same additive, so these two are the
  only foothold, and it is thin.
- **No reused additive.** Digit kappa at every offset, within and across all six telegrams: 1,575 tests, one at |z| ≥ 3.5
  (w791 with w769 at −142, z = 3.7, on 120 digits) against 0.7 expected by chance. No depth.
- **A figure bias in w791 only.** Digit counts 93, 79, 98, 86, 65, 67, 95, 68, 112, 67 (chi-squared 28.9 on 9 degrees, even digits
  ahead). The other telegrams are too short to say. It may be partly the typeface, where 3 and 8 are easily confused. Open.
- **Known keys.** The groups against everything Mendelsohn 1937 prints (13040, 5950, 26040, 18470, 12444, 1777, 2310, the Verkehrsbuch):
  plain, additive −999 to +999, slider no. 1 at all 1,000 settings. No setting beats chance or yields sense.

The system stays undetermined. The measured evidence allows a superenciphered code or a purely numeric cipher; it does not
separate them. Whether the Army's own attaché cipher and the Foreign Office's are one system is also open, and "one key, one
entry" may yet split this folder: w791 is kept with the legation telegrams only because nothing distinguishes them statistically.

## Remaining gaps

- All six telegrams, 328 groups - blocker: no-key-material; no key for this traffic in print or online, and no depth to attack
- Any MI-8 or Room 40 decode - blocker: needs-physical-access; RG 165 MID files and RG 457 at NARA, TNA HW 7 for 1918 are not online

## Escalation

- [x] siblings: catalogue 654 and 655 from the same batches checked; no shared groups
- [x] clear-pages: despatches 1426 and 1475 and the Christiania cables viewed; no decode or paraphrase; the cables were routed "To MID"
- [x] known-keys: everything in Mendelsohn 1937 tested; none fits
- [x] print: Mendelsohn 1937, Friedman's field-code studies, Zeman 1958, web searches; no text of the telegram found
- [n/a] key-rebuild: nothing reads and no depth exists to start from
- [n/a] retry: no key to retry with

## What would finish it

The attaché cipher's key, or the clear text of Ludendorff's telegram: "nr 34298 p IV" looks like a registry reference [?],
which would be the way into the OHL or Political Section files in Bundesarchiv-Militärarchiv, Freiburg, though much of the
Prussian army archive burned in 1945. The Politisches Archiv of the Foreign Office may hold a copy, since the military
attaché's traffic passed through the Legation.

## Sources

- NARA RG 59, M367: [roll 141](https://catalog.archives.gov/id/27158076) ff. 1257–1264, [roll 122](https://catalog.archives.gov/id/27140577)
  ff. 0156–0157, [roll 108](https://catalog.archives.gov/id/27128808) (cable copies).
- C. J. Mendelsohn, *Studies in German Diplomatic Codes Employed during the World War* (War Department, 1937),
  [Internet Archive](https://archive.org/details/41784749082377).
