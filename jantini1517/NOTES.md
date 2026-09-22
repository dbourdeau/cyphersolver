# Benedetto Fantini (DECODE "Jantini"), Buda/Eger 1517–1518 — catalogue 156 — NOTES

Status: in progress (attempted 21 Sept 2026, parked: not read; cipher unit unresolved, p. 2 untranscribed)

**Sender.** DECODE's "Benedetto Jantini" is a misreading of **Benedetto Fantini**, Ferrarese agent in Hungary in the
household of Cardinal Ippolito d'Este (bishop of Eger). Vestigia holds his whole file, ASMo Ambasciatori, Ungheria
b. 4, "Benedetto Fantini" nos. 1–7 (V1846–V1852, 1515–1518); only nos. 5 and 6 contain cipher.

| DECODE | ASMo no. | Vestigia | date, place | recipient (Vestigia) | cipher |
|---|---|---|---|---|---|
| R1126 | no. 5 | 1849 | [1517], Buda | unidentified ("V. S. Ill.ma", "V. Ex.") | pp. 1–2 almost all cipher, pp. 3–6 clear |
| R1127 | no. 6 | 1851 | 6 Mar 1518, Eger ("Agria") | unidentified | a few cipher lines in a damaged leaf |

The other Fantini letters (nos. 1, 2, 3, 4, 7) are in clear and carry no glosses. No clear copy or decipherment of
nos. 5–6 on Vestigia (V1849 has 12 images = the 6 pages twice). DECODE "Partially decrypted" reflects the clear
passages, not a decipherment.

## System

Same "two-tier" sign cipher as Giuliano Caprile's 1519 letters (catalogue 157, `caprile1519/`): a base glyph
(7, m, n, a, t …) with a small sign written above, one column per plaintext letter (homophonic), and bracket-L signs
as nomenclator words. Caprile's letters of 1519 have 1882 decipherments (Vestigia "b/c" items), which give the key.

## Clear context of R1126 p. 1

"Da Buda quando retornò il compatre … scripsi a V. S. Ill.ma … da poi non ho hauto lettere da V. Ex. … il negotio de
la restitution de Modena et Reggio per l'andata del duca Lorenzo in Franza" — then cipher.

## Log

- 2026-09-21: DECODE R1126/R1127 metadata and images; Vestigia search "Benedetto" finds the Fantini file
  (V1846–V1852), all images fetched (`img/v/`, git-ignored). System identified as Caprile's 1519 cipher.
- 2026-09-21 (second session): attempt, parked.
  - P. 1 transcription (`t1126.txt`, clean columns in `c1126_p1.txt`): 581 columns, 137 distinct labels. That is too many
    types for ~580 tokens, so the labels are not yet consistent.
  - Bracket-L signs make up ~28 % of the columns, which is too common for nomenclator words. They are probably letter signs here,
    not codes as in Caprile.
  - The run `-/7 -/g b/m` recurs 14 times, and `7g`/`7y` together 45 times in 581 columns. That is too frequent for one
    letter per column. `7g` and `7y` follow any sign, like word signs or nulls.
  - Each upper sign keeps to one base (2, zf → 7; &, b, x → m). So a column is one sign, not a consonant × vowel grid.
  - Anneals with it-cinquecento 4-grams (6 × 60k moves each), with 7g/7y as-is, merged into one sign, or dropped as
    nulls: no Italian comes out in any variant.
  - Literature: nothing in print (web search). Bonzagni 1512 (another Este–Hungary cipher) uses a different alphabet.
    Caprile's 1519 key is not built.

## Remaining gaps

- The whole cipher of R1126 pp. 1–2 (~45 lines, ~1,800 columns) and the few cipher lines of R1127: not read.

## Escalation

- Siblings: Fantini nos. 1–7 were checked; no clear copies or glosses. Caprile's 1519 letters use a related system, and
  their 1882 decipherments (R1133/7c) are the only crib-bearing material. Build that key first (see caprile1519
  NOTES "Next step"), then test it here.
- Next: a second, careful transcription of R1126 p. 1 and all of p. 2 with a fixed sign inventory (at most two image agents at a time),
  then decide the unit (whether 7g/7y are word signs or nulls) and re-run the anneal.
