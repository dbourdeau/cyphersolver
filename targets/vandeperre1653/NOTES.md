# Paulus van de Perre (London) to Johan de Bruyne, Aug-Nov 1653: the cipher runs in Thurloe I (Birch 1742): NOTES

Status: in progress. Key rebuilt by a contributor (GitHub issue #556, aaymeloglu): a 22-letter alphabetical substitution
with *ee* signs and word codes, read over 20 printed runs (322 groups). Strict 44/61 words = 72 %, read in part. The passages were
read at the time: Thurloe's translators glossed them in English and Birch prints the glosses. The gaps look outside-blocked (printer's
errors that only the manuscripts can settle). The folder was committed without a page for lack of time; a page can follow.

## The documents

Thomas Birch, *A Collection of the State Papers of John Thurloe*, vol. 1 (1742), pp. 431, 500, 522-523, 576, 582. These are Thurloe's
office's English translations of intercepted letters of Paulus van de Perre, Dutch ambassador in London, to Johan de Bruyne
(de Brune), pensionary of Zeeland, of 29 Aug, 3 Oct, 10 Oct, 4/14 Nov and 11/21 Nov 1653 (NS). The ciphered phrases are left as
figures, some with short English glosses printed over them. The originals are in the Bodleian, Rawlinson A (Thurloe papers). British
History Online drops the number runs; the Internet Archive scan `collectionofstat01thur` (leaf = printed page + 29) has them.

Not the same correspondence or system as targets/thurloe (Beverning and Vande Perre to Boreel, Thurloe i. 435, unread). Applied
here on 14 Nov 2026, this key gives gibberish on that ciphertext. Not in catalogue.json or research/leads.json (catalogue mentions
"targets/thurloe and colbert hold 1653 Dutch ciphers (Beverning/Vande Perre) of a different correspondence"). One key, one entry: a
new folder.

A further, unseen item (contributor): **Bodleian MS. Rawl. A.7, old p. 47**, Van de Perre to de Bruyne, 17 Oct 1653. The Bodleian
catalogue and Macray (col. 12, item 4) describe it as partly Dutch, partly cipher; Birch does not print it. Whether it uses this key is
not known.

## 14 Nov 2026: issue #556 (aaymeloglu), integration check

Claim (issue #556; the contributor's public repository aaymeloglu/unsolved-ciphers, folder vande-perre-1653, CC0). Copied into
`aaymeloglu/`: `transcription.txt` (every run as printed), `key.json`, `reading.txt` (mechanical and edited output), `repairs.json`,
their notes as `NOTES_aaymeloglu.md`, and the source audit as `evidence-audit.md`.
- Key: a 22-letter alphabetical substitution, letters in order with gaps from about a = 3 to w = 29. The fraction sign and 57/77 stand for *ij* and *ee*. There are word
  codes: 109 Major-General Harrison, 76 Denmark, 52 queen of Sweden (from the glosses), 115 Jarmuyen (Yarmouth), 617 de.
- How: bijective simulated annealing over a 4-gram model of Hooft's *Nederlandsche Historien* on the digits alone, on 14 Sept 2026.
  Four of eight restarts converged. The English glosses were checked afterwards and supplied the five C values. That order is by the contributor's
  record. Key-shuffle z = 18.0 (1,000 shuffles).
- Grades after the explicit repairs: 304 S, 5 C, 13 I of 322. Two short fragments are unresolved (P522.2 *diemnicvndament*, P582.4 *ote*).
- The contributor's words: "these passages were read at the time ... file it as 'read at the time, key rebuilt', not a new break."

Checked here:
- Own decoder (`own_decode.py`, from key.json; not their verify.py, which needs their cipherkit package): all 20 runs give
  their "printed" output letter for letter. 322 groups, 32 distinct (`_check_profile.py --measure`).
- Print: IA leaf n529 (p. 500) fetched (archive.org, plain curl). P500.2 (70 groups), the first 21 groups of P500.3 and the last 7 of
  P500.1 agree with the transcription: 98 groups, no difference.
- Strict count over the reading table in `NOTES_aaymeloglu.md`: about 61 words, 17 holes = 72 %, read in part. Holes: every word that
  carries a repair (cijffer, een, dispositie twice, gespeurt, ons, verwac[hten], gequalificeert, propositie, principal[e]n, [14],
  ana[ba]ptisten, [Jarmuyen]), plus the unresolved *diemnicvndament* (3 words) and *ote*. The contributor's grades give 304/322 =
  94.4 % of groups S.
- z = 18.0 not reproduced (needs their Dutch corpus). With 322 groups of continuous Dutch on a plain alphabetical key, chance is not
  a serious alternative. The glosses agree with the readings (I want a cipher / in a hostile country / the good disposition ...).
- Prior art: the English glosses of 1653 are a contemporary reading, in print since 1742. The Dutch cipher text and the key are new as far
  as known (contributor; one web check here found nothing).
- Outcome: key recovered from ciphertext-only, by the contributor's record (provenance contributed). Prior solution: in print (the glosses).

## Remaining gaps
- The 13 repaired groups (printer's or writer's slips such as 14 for t in *dispositie*, 17 for u): - blocker: needs-physical-access; only
  the manuscripts (Bodleian Rawlinson A, the Thurloe papers) can show the digits as written.
- P522.2 *diemnicvndament* and P582.4 *ote*: - blocker: needs-physical-access; three substitutions or a missing prefix, same manuscripts.
- Bodleian MS. Rawl. A.7 old p. 47 (17 Oct 1653, partly cipher, not in Birch): - blocker: needs-physical-access; not digitised as far as known.

## Escalation
- [x] siblings: Rawl. A.7 p. 47 located (contributor); De Bruyne's reply of 31 Oct 1653 (Birch p. 552, group 118) noted, not read.
- [x] clear-pages: Birch's English context and glosses used (contributor).
- [x] known-keys: targets/thurloe piece (a) tested with this key: gibberish (14 Nov 2026).
- [x] print: Birch vol. 1 OCR screen, Colenbrander, *First Dutch War* (contributor's evidence-audit.md).
- [x] key-rebuild: by the contributor (annealing, then by hand).
- [ ] retry: the repaired and unresolved groups need the manuscripts.
