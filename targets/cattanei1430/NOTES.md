# Francesco de' Cattanei (Rome) to Gianfrancesco Gonzaga, 13 and 21 February 1430 (DECODE R1854 images 4-5)

Read 22 Sept 2026 (key recovered from the ciphertext alone). Split on 14 Oct 2026 from `targets/r1854/` under the
one-key rule (George Lasry, 14 Oct 2026): DECODE R1854 holds four letters to Gianfrancesco Gonzaga in four ciphers.
This entry is Cattanei's two letters, one key (image 5 is the verso of the 21 Feb letter, photographed upside down).
The other letters of the record, each a different cipher with its own page: image 2 (`targets/r1854/`, Rome 9 Aug
1428), image 3 (`targets/mutiliana1428/`, Forlì 6 Nov 1428), image 1 (`targets/malatesta1428/`, Pandolfo Malatesta,
not solved). The solver and helper scripts are in `targets/r1854/`; images are git-ignored there (`decode/`, `img/`
in the main checkout) and not reproduced (Archivio di Stato di Mantova).

| image | date | language | signs | read |
|---|---|---|---|---|
| P4 (I8414) | Rome, 13 Feb 1430 | Latin | 1,537 (`p4v2.txt`, `ct_p4.txt`) | 1,505 |
| P5 (I8415) | Rome, 21 Feb 1430 (verso) | Latin | 199 (`p5v2.txt`, `ct_p5.txt`) | 199 |

Together 1,704 of 1,736 signs (0.982), re-counted 5 Oct 2026. Reading: `reading_p4.md` (P4 + P5); notes on the
second pass `p4v2_notes.md`.

## Method

Ciphertext-only anneal (`../r1854/solve.py`, Latin model) gave Latin at once ("sollicitabo bullam", "galeotam"); a
subagent second pass then checked every sign against the image: 209 edits, look-alikes split (slanted b = i vs
rounded = o; η vs 9; ⊢-o = q; o†o = x; Λ-type d), `key4_v2.txt` (earlier stages key4_1-key4_4). Signs for et, con,
-rum; x written cx (dicxit, reducxit). Rescoring outputs `occ_9.txt`, `occ_b.txt`; anneal logs `run_p4*.txt`.

## Content in brief

- P4 (Rome, 13 Feb 1430): Cattanei's news: Carlo (Malatesta?) on a marriage alliance with King Louis (of Anjou); a
  galley of Giovanni de Orlandis took a Catalan ship, lost at Gaeta (5,000 ducats); Castile presses Aragon; an envoy
  of the lords of Rimini left empty-handed; the archbishop of Patras offered the temporal lordship (of Patras) to the
  Venetians with the pope's licence, and the cardinals answered it was better lost than given to Venice; Niccolò da
  Tolentino's chancellor; the abbot's excommunication lifted; six Bolognese citizens expected.
- P5 (Rome, 21 Feb 1430): the Rimini envoys Astorgio and Bartolomeo appeared before the commissaries with a mandate
  and authenticated copies of bulls; "credo parum iuvabit"; in clear "denarios non habeo pro expensis".

## 30 Sept 2026: "Patras io(?)" is "Patrasio"

For the quotation list (George Lasry), the "[…]" after "Patras" in P4 L14 was re-examined. The two signs are `I bo`
(slanted b = i, rounded b = o; each attested dozens of times in P4 with those values), so the key gives
"...depatrasiocumlicencia". Read as one word: "archiepiscopus de Patrasio", a Latin form of the Italian name
Patrasso (grade: letters H from the rebuilt key, word division I). The phrase now reads without a gap: "dominus
a[rchi]episcopus de Patrasio cum licencia domini nostri dare volebat temporale dominium dominio Venetorum".
Corrected in `reading_p4.md`, `p4v2_notes.md` and the page. No count changes.

## 5 Oct 2026

- P4 L20 "debert onorio" re-divided with every letter as keyed: "creditur Nicolaus cito de Bertonorio debeat
  recedere" (Bertinoro; 12 signs). P4 L22 "domicus noster" = dominus noster (c for n, 7 signs).
- P4 L04 "leonebi": the image shows `t +` (e b) clearly, so "Leonelli" (Leonello d'Este) is not forced; left open.

## Remaining gaps
- P4 L04 "leonebi … re[∂]bs", L05 "aisignata pure st", L11 "uniei … cille", L14 "a-mhi" (~32 signs) - blocker: illegible; signs re-read at 10-13x, 786-px scan, values not fixable from single occurrences

## Escalation
- [x] siblings: R1853 register and the Mantova key records on DECODE opened (see `targets/r1854/NOTES.md`); no 1430 key; the other R1854 letters are other ciphers
- [x] clear-pages: P5 is the verso of the second letter, not a clear copy; only "denarios non habeo pro expensis" and the date are clear
- [x] known-keys: the register keys tried; none fits
- [x] print: web search; nothing printed for these letters
- [x] key-rebuild: key rebuilt ciphertext-only, then every sign checked against the image (209 edits)
- [x] retry: open spots re-read at 10-13x (22 Sept) and from the re-fetched images (5 Oct 2026): L14, L20, L22 read
