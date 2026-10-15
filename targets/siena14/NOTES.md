# Siena, Concistoro 2308 fasc. 2 no. 14 (DECODE R4802): Sienese envoys to the Priori, before 1429

Status: read in part — key recovered from the ciphertext alone; 876 of 1,495 cipher tokens (58.6%) in words read as sense, 29.2% more in doubtful words.

Split on 14 Oct 2026 from `siena1421` under the one-key rule (George Lasry, 14 Oct 2026). The old entry grouped the
whole bundle of Sienese cipher letters (Concistoro 2308 fasc. 2), each in its own key. This letter has a key of its
own; the other letters with recovered keys are their own entries, each a different cipher with its own page: no. 25
([`targets/siena25/`](../siena25/NOTES.md)), no. 18 ([`targets/siena18/`](../siena18/NOTES.md)), no. 4
([`targets/borghesi1456/`](../borghesi1456/NOTES.md)), nos. 6 and 24 (George Lasry's
[`targets/siena1431/`](../siena1431/NOTES.md)). The unread pieces, the key index and the shared solvers stay in
[`targets/siena1421/`](../siena1421/NOTES.md). The work below was done on 24 Sept 2026 and is carried over from its NOTES;
the transcriptions, `key14.txt`, `prep14.py` and `apply14.py` moved here on 14 Oct 2026.

Work date: 2026-09-24. From catalogue 336 (now narrowed to the unread pieces).

## The document

ASSi Concistoro 2308, fasc. 2, no. 14, DECODE R4802 (ASSi images, git-ignored). Whole-page letter to the "Magnificis et
potentibus dominis Prioribus [et] Capitaneo Civitatis Senarum", 23 full lines + subscription; dorsal list of names.

## Transcription and key

- ~1,300 cipher tokens in 248 point-divided words (agent B, `transcripts/no14.txt`, then `no14b.txt` after splitting
  the old OBAR into OL / OR / O). `no14_signs.tok` measured 14 Oct 2026: 1,291 tokens, 44 distinct; the second reading
  pass counts 1,495 sign tokens with the classes it settled.
- System: Italian, simple substitution with a few homophones (e = TR, 2; o = 6, P; i = Q4, PD, L; a = EQ, Q, TL;
  à = O+")"; q/g = Z), word points kept, two or three code signs for persons (7H, Z7).
- Attack history: plain homophonic anneal (`targets/siena1421/wordsolve.py`, 10 x 300k) stuck at nonsense; a hand crib
  ('8 6 RR IB VB Q' = nostra/vostra, 'RR IB EQ IB 6' = stato, 'Y 6 RR IB VB' = vostr-) pinned the key and Italian
  appeared; then the staged solver `homsolve2.py` (order 3 -> 4, frequency-seeded restarts, swap moves) reached the
  same key with no crib at all. So: key recovered from ciphertext only (`key14.txt`).

## Reading

- First reading (agent B, `transcripts/no14_reading.txt`): envoys of Siena on a journey write to the Signoria: "per la
  gracia di dio noi arivamo qui hieri da sera salvi e ... la nostra compagnia, e siamo pronti a seguire lo nostro camino
  ... del vostro stato e dela vostra cità e di tuta Toscana: significhiamo a la Signoria vostra come questa matina,
  trovandosi Domenico con uno servidore di <7H> ... a ragionare per spacio d'ore due ... a <7H> è dispiaciuto ... la
  inpresa ... per <Z7> di (420) ... ancora afferma l'amico vostro che Carlo Malatesti e ogni altro sono [in] questa
  medesima gielosia ... Toscana unita con le ... tre potentie ... discopertamente ... guera con <Z7> per conservacione
  da (420) e per conservacione loro ... <7H> è a Napoli ... li servidori vostri ... Marco". Glyph findings: '8' is two
  glyphs (compact 8 = v/u; tall theta = n); D also covers a delta-c; 'o–o' joined = f; PLUS^dot = i; arcs = nasal
  abbreviation; gn written ngn.
- Second pass (`transcripts/no14_reading2.txt`, COUNT): 1,495 tokens; 876 (58.6%) in words read as sense, 436 (29.2%)
  doubtful, 161 (10.8%) unread, 22 (1.5%) code signs and numerals (<7H> x4, <Z7> x2, (420) x2, 10).
- **Date.** Not in the text read. Carlo Malatesta of Rimini (1368-1429) is alive; Siena and "tuta Toscana" are to join
  "tre potentie" in open war with <Z7>. Candidates: the Ladislaus war 1409-14 or the Visconti war 1423-24. Either way
  c. 1409-29, at or before Meister's 1421 for no. 1: a candidate for the project's oldest-cipher record only if the date
  can be fixed.

## Validation

`mk_validation.py` (split from siena1421's combined script on 14 Oct 2026) writes `validation.tsv` for no. 14 alone;
`docs/_validate.py siena14 --write`: pass (see profile.json outcome.validation).

## Remaining gaps
- doubtful and unread words (about 40% of 1,495 tokens) and the codes <7H>, <Z7>, (420) - blocker: illegible; small signs at the DECODE resolution, mostly the first lines, lines 13-15 and the subscription; the key itself is recovered

## Escalation
- [x] siblings: the whole busta opened (keys R4746-R4789, letters R4790-R4814, R1858); no other piece in this key
- [x] clear-pages: none; the dorsal list of names is not a decipherment
- [x] known-keys: all 43 key sheets of fasc. 1 compared by eye; none fits
- [x] print: Meister 1902, Cecchini 1952; no printed decipherment found
- [x] key-rebuild: key recovered by homsolve2 from the ciphertext alone, hand crib confirmed it; glyph classes settled on the images
- [x] retry: re-read sign by sign on the images with the extended key (two passes); doubtful words regraded in the reading files
