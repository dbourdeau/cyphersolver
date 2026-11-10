# deboli1786: Deboli to King Stanisław August, St Petersburg, 12 Sep 1786, first page in table 3865 (AGAD Zbiór Popielów 2)

Status: read in part (Brice Dudout, 10 Nov 2026; partial reading explained: 219 groups, 163 certain, 33 probable, 17 restored, 6 unresolved; 196/219 = 89.5% read by sense without the restored groups, under the 95% rule; key K3 partial by our protocol, 0.645 on a held-out page against at most 0.020 for 200 shuffled keys).

Contributed by Brice Dudout (L'Europe chiffrée), with Claude Opus 5.5 agents. Catalogue entry **415** (Deboli 1786, AGAD Zbiór
Popielów sygn. 2). Related: `targets/deboli1787` (our #293, the pieces of 1787 in the older code ZbPop 444), `targets/deboli1788`
(our #169), deboli1789-1791 (Daniel). The Deboli entries, the 1788-91 work and the leads that pointed us to AKP 269 are Daniel's.

## What this folder is, and is not

A **partial reading explained**, at Brice Dudout's request. The key (K3) is **ours**, learnt on pairs of cipher despatches and
the cabinet's clear texts of the time; it is **not validated**: on a held-out page it reads 0.645 of the words, far above chance
(margin 0.625) but under the 0.85 we set. The **content is existing**: the cabinet's clear of this despatch is in AGAD,
Archiwum Królestwa Polskiego 269 (scans 253 right - 254). What is new is the system (table 3865, used by Deboli in 1786-87,
with no key of the time found), the key as a reusable table, and the check of the reading against the clear.

## Document

AGAD Warsaw, Zbiór Popielów (zesp. 12), sygn. 2, "Deboli 1786", scan 146 right: Antoni Augustyn Deboli, Polish envoy at
St Petersburg, to King Stanisław August, 12 Sep 1786, first page (16 lines, 227 groups), a fair copy without corrections,
in table 3865 from end to end (opening "3865 9"). The despatch goes on on scan 147 (not transcribed, not read). Images on
szukajwarchiwach, **not reproduced here** (private research only). Clear of the time: AKP 1/11/0/-/269, scans 253 right - 254
(header "St Petersbourg ce 12. 7bre 1786. reçue le 22."), used for the measurement and the restorations only, not published here.

## System and key (`key/key3865_K3.tsv`)

Table 3865: a one-part code of 1-4 digit groups for letters, syllables, endings, words and names, with nulls (3865 and 9 as
openers, 7, 12 ...) and suffixed variants (a, b, x, z: 1504z differs from 1504). Its alphabet has no j, v or y (i = j = y,
u = v). No key of the time was found (AGAD ZbPop 453/454 checked). K3 (1,287 entries, SHA-256 bcb2bfc2...) was learnt by script
on 16 pieces paired with their clears in AKP 269 (listed in the key's header), with variants "v1|v2" and nulls learnt without
feedback; predicted coverage 0.918 (cross-validation). It was frozen and hashed before the page was transcribed.

## Tests of the key (`validation.txt`)

Four pre-registered rounds, one measurement each: R1 0.591 and R2 0.598 (against 0.60), R3 0.519 (the held-out Z2-023 is a
corrected draft whose cipher follows the struck-out first state), **R4 0.645 on this page**, controls at most 0.020: **partial**.
On clean copies K3 levels off at 0.63-0.65: the misses are truncated values (reso, exe, uau) and variants (auoit/avois), not
wrong values, which is why the reading by sense below is much higher than the measure.

## Reading (`transcription/`, `decryption/`, `reading/`, `translation.md`)

Re-read group by group before publication (10 Nov 2026): **certain** = the K3 value equals the aligned letters of the clear;
anything read only by sense is **probable**; groups without a K3 value, or whose value the clear contradicts, are **restored**
and not counted. 219 groups: 163 certain, 33 probable, 17 restored, 6 unresolved. New values suggested by the clear (not added
to K3): 1647 ViceChancelier, 2255 so, 3551a uniformité, 429 conçue, 631 dimanche, 3778 y (a null in K3).

Content: Deboli has handed Vice-Chancellor Ostermann his written observations on Prince Czartoryski's memorandum (the
Branicki-Czartoryski affair) and sends them to the King, with a passage added for Ambassador Stackelberg, whose agreement is
the condition for success in St Petersburg; Sedler presented the memorandum only on the Sunday.

## Remaining gaps

- 6 unresolved groups (774, 3527, 77x, 1039, 2036a, 279) and 17 restored - blocker: open-codes; values to learn on more pairs
- K3 not validated (0.645 against 0.85) - blocker: open-codes; truncated values cap the measure; a K4 would need new pairs and a new held-out piece
- the rest of the despatch (scan 147) and the other 3865 pieces of ZbPop 2 and 3 - blocker: open-codes; K3 is partial, and unread pieces are kept unopened as held-out material for the next key

## Escalation

- [x] siblings: ZbPop 2 (1786) and ZbPop 3 (1787) sorted piece by piece by opening group; 3865 pieces typed, 9933 headings followed by 3865 found (Z2-023, Z2-119)
- [x] clear-pages: AKP 269 holds the cabinet's clears of 1786-87 (header index made); used as pairs for learning and, after hashing, for the held-out measurements
- [x] known-keys: ZbPop 444 (older code, targets/deboli1787), 451, 445/452, 453/454 (key collections 1765-1792), deboli1788 K4 and deboli1789 keys: none is table 3865
- [x] print: the IH PAN edition of Deboli's reports (Zielińska and Danilczyk) stops at 1782; no edition of 1786-87 found
- [x] key-rebuild: K1, K2, K3 learnt on growing sets of pairs (16 pieces for K3, predicted coverage 0.918)
- [x] retry: four pre-registered rounds (0.591, 0.598, 0.519, 0.645), one measurement each; R4 on a fair copy after R3 failed on a corrected draft
