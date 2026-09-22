# Benedetto Fantini (DECODE "Jantini"), Buda/Eger 1517–1518 — catalogue 156 — NOTES

Status: attempted, open (closed 22 Sept 2026: not read; no key material for this cipher exists anywhere found)

**Sender.** DECODE's "Benedetto Jantini" is a misreading of **Benedetto Fantini**, Ferrarese agent in Hungary in the
household of Cardinal Ippolito d'Este (bishop of Eger). Vestigia holds his whole file, ASMo Ambasciatori, Ungheria
b. 4, "Benedetto Fantini" nos. 1–7 (V1846–V1852, 1515–1518); only nos. 5 and 6 contain cipher.

| DECODE | ASMo no. | Vestigia | date, place | recipient (Vestigia) | cipher |
|---|---|---|---|---|---|
| R1126 | no. 5 | 1849 | [1517], Buda | unidentified ("V. S. Ill.ma", "V. Ex.") | p. 1 (18 lines after 6 clear lines) and p. 2 (25 lines) cipher; pp. 3–6 clear |
| R1127 | no. 6 | 1851 | 6 Mar 1518, Eger ("Agria") | unidentified | 5 short cipher lines in a damaged leaf |

DECODE errors: author "Jantini" → Fantini; R1126 date given as 1 Jan–31 Dec 1517 (Vestigia's placeholder), origin
Ferrara → Buda (the letter is written from Hungary; Ferrara is the archive's series). The other Fantini letters (nos. 1, 2, 3, 4,
7) are clear with no glosses. No clear copy or decipherment of nos. 5–6 on Vestigia (V1849's 12 images = the 6 pages
twice). DECODE "Partially decrypted" reflects the clear passages, not a decipherment. Pp. 3–6 of R1126 were checked:
they continue the letter in clear (the Hungarian diet, the governors of the young King Louis II), they are not a decipherment.

## Clear context of R1126 p. 1 (`t1126.txt` C01–C06)

"Ill.mo sig.r mio obser.mo Da Buda … scripsi a V. S. Ill.ma … da poi non ho hauuto lettere da V. Ex.tia … per intender
dil ben stare suo et de tutta la casa … che exito hara hauuto il negotio dla restitution de Modena et Regio per la
mandata dil duca Lorenzo [in Franza?] instanza" — then cipher to the end of p. 2. (Modena/Reggio restitution and
Lorenzo de' Medici's journey to France date it to spring 1518 at the latest; Vestigia's "1517" is the file year.)

## System

A two-tier sign cipher of the same family as Giuliano Caprile's 1519 letters (catalogue 157, `caprile1519/`): a base
glyph (7, m, n, g, y, 4, t, a) with a small sign written above it, and bracket-L signs.
Transcription `t1126.txt` (one reader, second pass on 3 lines only): 43 lines, 1,374 columns, 1,061 letter columns of
143 upper/base types, 299 bracket-L signs (22 %) with 22 inner signs; `t1127.txt` 5 lines, ~40 columns, faint.

## What was tried (21–22 Sept 2026)

1. **Siblings / clear pages / print.** Fantini nos. 1–7 on Vestigia; Bonzagni 1512–14 (other Este–Hungary cipher: a
   different simple substitution); web search: nothing printed. DECODE holds no Modena key record 1490–1540.
2. **Caprile 1519 key.** Only crib-bearing material in the family. Three pairings tried (agents, files in
   `caprile1519/pair5`, `pair8`, `pairX`): R1131/5b (water-stained, alignment no better than shuffled controls);
   R1134 (NOTES' "interlinear on pp. 4–5" is wrong: those pages are a second letter in clear with cipher insertions,
   no decipherment); R1130/4c, short clear-bounded segments: the cipher is **syllabic**, upper sign ≈ consonant, base ≈
   vowel (7 = none, m = e, n = o), bracket-L = CV syllables (te, re, to, si, ra). ~20 values, held-out 16/18 vs
   shuffled mean 8.1.
3. **Ciphertext-only syllabary anneal** (`syl_anneal.py`, it-cinquecento 5-grams, letter-distribution penalty).
   Control (`control.txt`: 2,200 letters of 16th-c. Italian enciphered in the same structure, 2 homophones per
   consonant, 22 syllable signs): with bases 7/m/n seeded, recovered nearly verbatim; still recovered with 10 % of
   signs corrupted (`control_noise.txt`, 3 of 4 restarts). On R1126 (8 restarts, raw and with -/7 -/g, -/7 -/y
   merged as ligatures, `t1126_lig.txt`): no Italian, restarts disagree, score/char −2.37 against −1.77 for the
   control's true key (`runs/`).
4. **Caprile values as seed** (`seedC.json`): score falls from about −140 to −1,250. Fantini's key is not Caprile's.

Conclusion: the annealer works at this length and noise, so the failure is the model or the key family, not search.
Without a crib (no decipherment, no clear copy, no printed text) and with a key different from the only paired
sibling, the cipher is not readable from the material available.

## Remaining gaps

- R1126 cipher pp. 1–2 (43 lines, ~1,370 columns) - blocker: no-key-material; no decipherment, clear copy or key anywhere; Caprile's key does not fit; ciphertext-only syllabary anneal fails where controls succeed
- R1127 cipher (5 lines, ~40 columns) - blocker: too-short; plus faded and torn, same unknown key

## Escalation

- [x] siblings: Fantini nos. 1–7 (V1846–V1852) all opened; clear, no glosses; V1849 images duplicate the 6 pages
- [x] clear-pages: R1126 pp. 3–6 are the letter's clear continuation, not a decipherment
- [x] known-keys: Caprile 1519 values (R1130/4c) seeded: score collapses; Bonzagni 1512 alphabet is a different system; no Modena key on DECODE
- [x] print: web search, Vestigia bibliography fields empty; nothing printed
- [x] key-rebuild: ciphertext-only syllabary anneal, control-validated (clean and 10 % noise), fails on R1126
- [n/a] retry: nothing read, so nothing to regrade

## Log

- 2026-09-21: DECODE R1126/R1127 metadata and images; Vestigia "Benedetto" → Fantini file; images in `img/` (git-ignored).
  A second session's first attempt on p. 1 (`c1126_p1.txt`, 581 columns; letter-per-column anneals: nothing).
- 2026-09-21/22: full transcription `t1126.txt`, `t1127.txt` (agent; `seg/signs.md`); Caprile pairings; syllabary
  model; control-validated anneals; closed attempted, open.
