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


## Second attempt, 22 Sept 2026

- Transcriptions: p. 1 read twice (t1126.txt, t1126_p1b.txt), agreement 90 %, adjudicated to `t1126_p1c.txt` (561 units).
  P. 2 read twice (t1126_p2.txt, t1126_p2b.txt), agreement 76 %, adjudicated to `t1126_p2c.txt` (~790 units; about 20
  decisions in L13-L17 unchecked). Combined solver input `c_v5.txt`: 1,258 units, 144 labels, 88 seen 3+ times.
- Conventions settled: a raised y belongs to the base before it (y/7); "r" is a 7 with an entry stroke; "7 9" (bare 7, then
  a 9 on the line) behaves as one sign, and "7 9 m^b" occurs 30 times.
- Controls (synthetic Italian, the same solver): at 1,190 tokens and 90 symbols it recovers 98.7 % of letters with no noise,
  92 % at 5 % label noise and 27-28 % at 10-15 %. So the method works at this length only if the transcription is 95 % right.
- Solver runs on the adjudicated text (it-cinquecento 4-grams, 10 restarts x 300k moves, 4 seeds): the seeds disagree and
  produce no Italian. The same happens with these unit models: one letter per unit; "7 9" merged; bare 7 as a null; upper
  sign only; brackets as word codes (runs split at brackets); a consonant+vowel syllabary (upper = consonant, base =
  vowel); and pins from Caprile's 1519 values and from "che".
- What blocks it: the transcription error is still about 5-8 % (the adjudicators' own estimate), which is just past the
  solver's limit, and the cipher's structure (codes, nulls) is unconfirmed. Moving it on needs one of three things: a key
  or crib (the Caprile 1519 key rebuilt from R1133/7c, if it is the same cipher); a better physical image (ASMo) for
  the faint small upper signs; or a third, careful reading of p. 2 L13-L25.
- Third reading of p. 2 L13-L25 (`t1126_p2d.txt`, changes in `p2_third.md`): 11 units changed, every unit checked on the
  image, estimated error 2-3 %. Final text `t1126_p1c.txt` + `t1126_p2final.txt`, solver input `c_v6.txt` (1,257 units, 143
  labels) and `c_v6f.txt` (labels seen 3+ times: 1,184 units, 87 labels). Anneal 3 seeds x 12 x 400k: no convergence.
- Controls matched to this size: with 144 true signs, even a perfect transcription gives only 42 %, and 3 % noise gives
  29 %. With 90-100 signs and 3-5 % noise, 92-95 %. The filtered real text (87 labels, about 3 % noise) should therefore
  solve if it were a simple one-letter-per-sign homophonic cipher. It does not, so the cipher is not that: word
  signs, nulls or syllable signs are likely. Without a crib this is where a ciphertext-only attack stops.
- Structural check against Caprile R1133 and its 1882 decipherment (7c): there, 1,327 columns carry 2,177 letters, and 245
  bracket signs are whole words. Read the same way, Fantini's ~290 brackets are word codes, and they cut the letter signs
  into 189 runs averaging 4.8 signs (903 letter tokens, 121 labels; `c_v5nb.txt`). A control of that shape (runs of 5
  broken by code gaps, 121 symbols, 3 % noise) recovers **7 %**. So ciphertext-only cannot read this letter at any
  transcription quality. Only a key or crib can: the Caprile 1519 key, where it shares labels (82 shared label types
  covering 76 % of Fantini's tokens, but the commonest signs differ: Fantini 2/7, &/m, zf/7 against Caprile 9/7, m/7,
  L/7), or an ASMo decipherment not on Vestigia. This is an outside blocker (no key material).

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
