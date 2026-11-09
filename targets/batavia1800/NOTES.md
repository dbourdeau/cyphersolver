# batavia1800: J. C. Smissaert (Raad der Aziatische Bezittingen) to C. J. Prediger, 20 Nov 1800 (Nationaal Archief 2.01.27.02 inv. 209): key of the letter cipher rebuilt from the clear minute and validated

Status: solved at the time (the clear minute of the same letter is filed with it, so the content is existing); key rebuilt from the minute and validated on a held-out passage (Brice Dudout, 9 Nov 2026; 0.933 of characters vs 0.433 for the best of 200 shuffled keys, margin 0.500). 60 cipher words: 54 certain, 3 probable, 3 restored, 0 unresolved (0.95 read, restorations excluded).

Contributed by Brice Dudout (L'Europe chiffrée), with Claude Opus 5.5 agents. Source: **Nationaal Archief, The Hague,
2.01.27.02** (Inventaris van de archieven van de Raad der Aziatische Bezittingen en Etablissementen, 1800-1806),
**inv. 209**, 5 scans (https://www.nationaalarchief.nl/onderzoeken/archief/2.01.27.02/invnr/209). The archive's
description already names the encipherment ("overbrenging in cijfer") with the minute. Found in our own sweep of the
Nationaal Archief (2 Nov 2026), harvested 9 Nov 2026. Not in the catalogue or the leads. No images are included: the
inventory record shows them as downloadable but states no licence.

## Documents

| scan | content | role here |
|---|---|---|
| 0001, 0002 (left), 0004 | clear minute of the letter, the passages to encipher underlined, with small strokes under them counting the letters; postscript | the plaintext of the pair |
| 0002 (right) | the letter as sent, in partial cipher, "Geacht vriend", 20 Nov 1800 (14 lines with cipher, 60 cipher words) | the ciphertext |
| 0003 | blank verso (show-through of 0002) | none |
| 0005 | end of the postscript, "Amst. 20 april 1801", signed Smissaert (seen as a thumbnail only) | clear |

There is no cipher in the file without its clear: what is new is the key and the identification of the pair, not the text.

## The key (`key.tsv`)

Simple substitution of letters. Each letter is written as a column of two digits, a top digit 1-7 over a bottom digit
1-4, so the alphabet fits a 7 x 4 grid (code = top then bottom):

| | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| 1 | h | r | - | l |
| 2 | v | m | i/j | u |
| 3 | y | z | c | p |
| 4 | t | k | s | a |
| 5 | b | g | o | f |
| 6 | e | d | w | x |
| 7 | n | - | - | - |

54 = f is seen only in the held-out word "gelieft" (probable). Not seen: q; cells 13 and 72-74 empty. Encipherer's slips:
"verking" for "versterking"; 42 (k) for s in "secretesse" (three times); a stray 44 (a) after "andere".

## Validation (`validation.txt`)

Protocol `frozen/PREREG.md` hashed after the cipher was transcribed and before the clear minute was read. Learning part
A = lines L01-L12 aligned with the minute; key built by script (majority letter per code, 23 codes, no conflict) and
frozen. Held-out part H = lines L13-L14 (60 letters, "Heer Gouverneur Generaal zulks in secretesse gelieft te
communiceren"), hashed before learning. One measurement: **0.933** of characters against at best 0.433 for 200 shuffled
keys (margin 0.500), coverage 0.983: **validated** (thresholds 0.85 and 0.30 fixed in advance).

Declared reservations (`frozen/AMENDEMENT-01.md`, written before the freeze): two copying slips in A corrected from the
raw notes taken before the clear (H unchanged); and the beginning of the clear of H was glimpsed on the learning crop of
scan 0001, so the test is not blind on those words. It stays mechanical: the key comes by script from the A alignments
only, with nothing added by hand, and H was not changed.

## Reading (`reading.md`)

Smissaert tells Prediger, then at Batavia, that besides the long-delayed shipment of a corps of troops to the Indies,
the Asiatic Council has been authorised to prepare a second, similar expedition to Batavia from another port of Europe,
which would considerably reinforce the military on Java; Prediger is to pass this on to the Governor-General in secrecy.
Only the sensitive words are in cipher. 60 cipher words: 54 certain, 3 probable, 3 restored (letters checked against the
minute), 0 unresolved; read share 0.95 with restorations excluded, 1.0 with them.

## Prior work (re-checked 9 Nov 2026, GitHub API)

Nothing in this repository: `catalogue.json` and `research/leads.json` on main 1e974a24 have no Smissaert, Prediger,
"2.01.27", Aziatische or Batavia 1800-1801 entry (the Batavia hits are other items); no target (only `lejava1921`, not
related); issue and PR search for Batavia, Smissaert, Prediger, 2.01.27.02, Aziatische: 0. No printed edition of the
letter or study of the cipher found (two web searches). The clear minute in the same file is the prior solution: the
content has always been readable there.

## Remaining gaps

- The clear of the minute is transcribed here only where it pairs with the cipher and for the letter's opening; the
  rest of the minute and the postscript (scans 0004-0005) are not transcribed. Blocker: not-attempted.
- One reader (an agent); no human palaeographic check of the digit columns. Blocker: not-attempted.
- q unseen; f from one word only. Blocker: too-short.

## Escalation

- [x] clear-pages: the clear minute in the same file used for learning and as the held-out reference
- [x] siblings: no other cipher in inv. 209; the 1811 Janssens despatches (NA 2.01.27.05 inv. 12) use another system (numeric code, French)
- [x] print: two web searches, no edition found
- [n/a] key-rebuild: the key is validated
- [n/a] retry: nothing unread
