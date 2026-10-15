# Alfonso Cistarelli (Eger) to Cardinal Ippolito I d'Este, 25 July 1520 (catalogue 158, DECODE R1137) — NOTES

Attempted, not solved: closed unread on 2 Oct 2026; blocker outside the session (the only image does not settle the
digits; no key exists). Written up in docs/cistarelli1520.html.

Split on 14 Oct 2026 from `caprile1519` under the one-key rule (George Lasry, 14 Oct 2026): one entry per key. The old
entry joined Cistarelli's letter with Giuliano Caprile's letters because they share an ASMo file (Ungheria b. 4) and the
mission. Cistarelli's two-digit figure cipher is its own system. Caprile's 1520–21 sign cipher is a different cipher,
with its own page ([`targets/caprile1520/`](../caprile1520/), docs/caprile1520.html), and so is his 1519 two-tier cipher
([`targets/caprile1519/`](../caprile1519/), docs/caprile1519.html). Shared material stays in `targets/caprile1519/`:
the DECODE record page `decode/rec1137.htm`, the Vestigia record `vestigia/v1904.json` and search
`vestigia/search_Cistarelli.json`, the annealers `anneal.py` and `fastanneal.py` (the scripts here import them from
there), `knownkeys.py r1137`, and the images (`img/IMG_R1137_*.png`, `img/v/v1904_*.jpg`, git-ignored, main checkout).

ASMo, Ambasciatori, Ungheria b. 4, Cistarelli = "b. 4/26", no. 3 (Vestigia 1904). DECODE R1137: "Partially decrypted",
4 images; P1 and P3 clear text, P4 address; the cipher is on P2.

## The cipher

Two-digit groups, mostly ending in 5 or 0 (25 95 70 15 80 55 …), with a few other signs (f, k, u, y), mixed with clear
text. No gloss. 584 numeric groups and 83 other signs in `r1137_transcription.txt` (one reader; group boundaries
inferred, no spaces).

## Prior work

None found: no decipherment, clear copy or gloss in the file, on Vestigia, on DECODE or in print (ASMo inventory;
Somogyi 2025 concerns Caprile's letters).

## What was tried

**Ciphertext-only anneal** (`../caprile1519/fastanneal.py`, `refine37*.py`, outputs `f37_*.txt`, `r37*.txt`) gives a
partly consistent key (e = 0, 25; a = 86, 80; o = 70, 10; i = 45; t = 95; r = 85, 84; s = 90, 15; n = 65, y; l = 55;
p = 75; u = 96; m = 60; d = 20; c = 30) and phrases such as "lettere per", "sempre", "presto", "saria meglio", "non se
poteria", "dua milla", "questi altri", "Antonio" (M). Not a reading. Against the same tokens shuffled: -2.69 vs -3.05 per
token, so there is language signal, but the output gives only fragments ('auan[ti]', 'edirit[o]').

**Known keys** (`../caprile1519/knownkeys.py r1137`): Caprile's 1520–21 key (caprile1520), the 1519 tables
(caprile1519), Bonzagni 1512–14, Sadoleto 1482 and Maffeo 1489 are sign alphabets; the DECODE harvest lists no
Este/ASMo key 1490–1550; no numeric key could be applied.

**Transcription check** (2 Oct 2026): a second reading of P2 L04-L07 against the image (autocontrast bands, native
resolution) disagrees with `r1137_transcription.txt` on 13 of 92 groups (8/9 as in 85/95, 4/9, 0/5/6, 80/86, and where
a group starts); the single "0"/"5" groups may be halves of groups.

**Crib test** (`r1137_crib.py`, `r1137_crib_out.txt`, ORDER 5, 20 restarts base, 4 windows x 3 restarts x 80k per word,
word-level segmentation rerank): cribs custode, agria, alfonso, debito, buda, episcopato give anneal gains -57 to -348
(mean -169), six control words -49 to -363 (mean -172); best word score is a control. No crib lands.

## Log

- 2026-09-21: DECODE and Vestigia records; subagent transcription of P2; ciphertext-only anneal (fragments).
- 2026-10-02: P1, P3, P4 viewed (clear text, address); known keys ruled out; anneal vs shuffled control; transcription
  spot-check (14 % disagreement); crib test negative.
- 2026-10-14: split from `caprile1519`; the R1137 files moved here; scripts import the annealers from `../caprile1519/`.

## Remaining gaps

- R1137 Cistarelli, 584 two-digit groups - blocker: needs-physical-access; the only image (DECODE, whole spread at 3240 px, digits about 25 px, faded) does not settle the digit readings: a second reading of P2 L04-L07 disagrees with `r1137_transcription.txt` on 13 of 92 groups (14 %), and the single "0"/"5" groups may be halves of groups; no key exists anywhere (series, archive, correspondent, decade); ciphertext-only anneal and crib placement do not separate cribs from controls; my judgement, not proven, is that transcription noise is what stops the solve, so a better photograph from ASMo (b. 4/26 no. 3) is the next step

## Escalation

- [x] siblings: Vestigia search "Cistarelli" (20 records) opened; no other Cistarelli letter carries cipher or a decipherment; Caprile's letters in the same box use other ciphers
- [x] clear-pages: R1137 P1/P3 clear text, P4 address; none is a decipherment (2 Oct 2026)
- [x] known-keys: no numeric key of the series, archive (DECODE ASMo/Este 1490-1550: none), correspondent (Bonzagni 1512-14, Ippolito's Eger household) or decade (Sadoleto 1482, Maffeo 1489) exists, so none could be applied
- [x] print: ASMo inventory, Somogyi 2025: nothing on R1137
- [x] key-rebuild: ciphertext-only anneal with consensus fixing (`refine37*.py`): fragments only
- [x] retry: anneal rerun with a shuffled control and crib placement with controls (2 Oct 2026): no reading
