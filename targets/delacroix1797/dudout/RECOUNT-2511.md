# Recount after sign plate 2511 (25 Nov 2026)

Tool: `python strict_share.py` (the folder's own script: word division and marking rule of
`beling2026/scripts/make_reading.py`), run on `beling2026/` as it is and on a copy with
`delacroix1797-planche-2511.patch` applied. Table (`code_table_F_partial.tsv`) not rebuilt.

| | cipher words | sure (class A only) | probable (a single-use value) | holes | read share (sure + probable) | strict share |
|---|---|---|---|---|---|---|
| before | 444 | 296 | 121 | 27 | 0.939 | 0.667 |
| after the 4 changes | 444 | 298 | 123 | 23 | **0.948** | 0.671 |

Words that leave the holes: [sur] (détaillés sur tout), le[çon], [d]'envoyer, sans [dél]ai.
On the reviewer's count of 442 words: 419 of 442 = 0.948. Still read in part: 95 % needs 422 of 444 (one word more).

Not counted here, for the maintainers to weigh:
- The three 257 places (tokens 139, 213, 438) are read 257 by the person, as Brackx wrote them. The proposals to 251
  are not supported. The table already records 257 = "ai x3" in `all_values`; if these three places stop being
  proposal places, `strict_share.py` stops marking two of them (tokens 139 and 438; token 213 carries "ay"), but only
  one word leaves the holes (n'ai; consul-ai-re-s keeps the class C group 526): 22 holes, 422 of 444 = 0.950. That value rests only on these three places, so
  our rule keeps all three as holes; whether "ai" is a true second value of 257 is the maintainers' call.
- Token 413 reads 1084 to the person (third digit an 8, as the third blind AI reader had it), neither Brackx's 1024 nor
  the proposed 1034. 1084 is not in the table; the hole stays.
- A rebuilt table would give 361 a second agreeing use (class A), which moves "de l'impatience" and "délai" from
  probable to sure; not done here.
