# Diego de Ibarra, Paris, 10 July 1593, in the Feria-Mansfeld cipher (BnF fr. 3984 no. 68, f. 145)

Status: read in part — 224 of 598 groups read as sense (37.5%) with Tomokiyo's Feria-Mansfeld table (keyM.tsv) and one
value added (57 = li); the three-letter word codes, which carry much of the sense, have no published table.

Split on 14 Oct 2026 from `sessa1593` under the one-key rule (George Lasry, 14 Oct 2026). Until then this letter was
filed with three Spanish despatches of 1593 in the Spanish office cipher of 1592-93 (Miranda to Feria, Sessa to
Ibarra, Sessa to Philip II; catalogue item 19): [`targets/sessa1593/`](../sessa1593/NOTES.md) (a different cipher,
with its own page). The work below was done in the sessa1593 sessions of 19 Sept and 5 Oct 2026 (the 19 Sept pass
with Arya Sanketbhai Patel's PR #8) and is carried over from its NOTES; the no. 68 files moved here on 14 Oct 2026.
Shared material stays in `../sessa1593/`: the Gallica fetchers (`fetch.py`, `fetchr.py`), `deskew.py`, `lines.py`,
Tomokiyo's pages and key images (`src/spanish3.htm`, `src/spanish3mansfeld.png`), and the git-ignored images
(`img3984/r0268_*`, in the main checkout's `targets/sessa1593/`).

Work date: 2026-09-19. Catalogue item 19 (removed from the catalogue on 20 Sept 2026 when the four were read in part).

## The letter

BnF fr. 3984 no. 68, f. 145 (ark `btv1b9060633d`, canvas 268): *"Lettre, avec chiffre, de «D. DIEGO DE IBARRA,... De
Paris, a 10 de julio 1593». En espagnol."* A clear Spanish opening (*"...V.S.a de 4 y 5 deste, y de buena gana
aguardara... espero que me dara V.S.a mas claridad"*) running into cipher. Tomokiyo's caption for the key,
*Syllabic cipher for Duke of Feria and Count of Mansfeld (1593)*, cites this folio: July 1593, Mansfeld / Feria /
Ibarra in Paris, fr. 3984 ff. 130, 145.

## The cipher (19 Sept 2026)

**no. 68 is in the other cipher**, as Tomokiyo's citation of fr. 3984 f. 145 says: the values run far higher
(97, 98, 800, 200, 7243, 9482) and the leaf carries **three-letter word codes** — *pra, rom, mon, xen, vul,
cil, denp, hes, dur* — which is exactly what he describes for the *Syllabic Numerical Cipher for Duke of Feria
and Count of Mansfeld (1593)* (`src/spanish3mansfeld.png`, "three-letter symbols representing words, *vas*
for *segnor*"). That key is downloaded but not yet transcribed into a key file.

**no. 68, f. 145** (Ibarra, Paris): a **different cipher** — the Feria-Mansfeld key, transcribed to
  `keyM.tsv`. Clear opening running into cipher: *aguarda cavalleria ... que aya recivido su ...*

Still open: a scatter of groups in every letter, the later lines, and **the nomenclature of the
Feria-Mansfeld cipher**, which is the one real gap left. Its three-letter groups (*pra, dur, hes, gar, pun,
rom, mon, xen, vul, cil*) carry much of no. 68's sense, Tomokiyo tabulates none of them, and the obvious
candidate was checked and excluded: **fr. 3995 f. 101 (canvas 194) is an Italian nomenclature**, not a
Spanish one (*Austria, Ambasciatore, Assemblea, Battaglia, Bisogno, Borbone, Cardinale di, Castello,
Cattolici, Concilio generale, Corte di*). It belongs to another correspondence.

## A test on one line (5 Oct 2026, superseded the same day)

**no. 68 tested again:** line 11 transcribed and decoded with `keyM.tsv`: *va le ri a no la vi o xur que le de di as
se ri as ...* - syllables, no Spanish, as on ll. 7-10. Tomokiyo's table does not give continuous text on the body;
ll. 12-31 not transcribed. Token count estimated (28 lines x ~22).

## 10. no. 68 transcribed in full and the Feria-Mansfeld key tested ciphertext-only (5 Oct 2026)

All cipher lines of f. 145 transcribed from the 3600-px crop to `ct68.txt`: **20 cipher lines (ll. 4-23; ll. 1-3 are
clear), 598 groups**, counted (the 620 of section 9 was an estimate from a wrong line count). Diacritics dropped.
`dec68.py` decodes with `keyM.tsv`.

**The earlier verdict was wrong.** On a full transcription Tomokiyo's table *does* give Spanish: *a mi no me parece que
puede*, *se [ha] de poner todo lo que se puede*, *lo que podemos*, *aliento, y si ella apareciera, y palabra*, *no
estamos desesperados*, *peligro*, *espero*, *de acudir a lo que esta*, *supuesto e numero*, *pareceria que venia a
ayudar ... y la cavalleria*, *no seria fuera de*, *a lo menos no parece sino*. Lines 7-10 had read badly in the
19 Sept pass because their transcription was truncated.

**Control** (`anneal68.py`, es-golden-age 5-gram, no spaces): keyM scores **-2.500** per character; 200 keys with
keyM's values shuffled among the numbers score at most **-3.378** (mean -3.805). The key is real.

**Rebuild:** an unconstrained hill-climb over all numbers collapses onto *que* (homophone collapse, score -1.59 but
nonsense) and was rejected. Constrained fill of the numbers missing from keyM (`fill68.py`): **57 = li** is top of
all candidates with a gain far above the median (3 occurrences: *peligro*, *aliento*) and is accepted (`fill68.json`).
64 (9 occurrences; *ha* by context: *se ha de poner*, *ha de acudir*) is not separated by the LM (na -2.549, ha
-2.569) and stays unread. 31, 77, 81, 95, 200T, 800T: no candidate stands out. Cribs: *Paris* and *Su Magestad* are
in clear on the leaf; *Feria*, *Mansfeld*, *Liga* fit no syllable run, so they would sit in the open three-letter
codes (pra, dur, hes, gar, pun, rom, mon, xen, vul, cil, var, vis, tor ...), which no crib fixes.

**Retry of nos. 45/79/47:** 57 = li belongs to the Mansfeld cipher, not to the 1592-93 office key, so it gives nothing
there; no new office-key value came out, and the ~75 doubtful groups stand.

| | before | after |
|---|---|---|
| no. 68 | ~12/620 = 0.02 (estimate) | **224/598 = 0.375** (measured) |
| all four | 1224/1930 = 0.634 | **1436/1908 = 0.753** |

Key files here: `keyM.tsv` (Tomokiyo's Feria-Mansfeld table), `fill68.json` (57 = li); decoders `dec68.py`,
`decodeM.py`; `anneal68.py` (shuffled-key control and the rejected free hill-climb), `fill68.py` (constrained fill);
transcription `ct68.txt`; sense count `sense68.tsv` (the no. 68 rows of sessa1593's `sense.tsv`); reading `reading68.md`.

## Remaining gaps
- no. 68, f. 145: 374 of 598 groups unread - blocker: no-key-material; the three-letter nomenclature (pra, dur, hes, gar, pun, rom, mon, xen, vul, cil, var, vis, tor ...) is published nowhere, fr. 3995 f. 101 is Italian and no crib fixes it; the numbers 64, 31, 77, 81, 95 are not separated by the LM control; the diacritic finals dropped in ct68.txt are still to be added from the image

## Escalation
- [x] siblings: the three office-cipher letters of sessa1593 are another key; fr. 3995 ff. 94-101 opened next to the office key (f. 101 another correspondence); fr. 3984 f. 130, the other letter Tomokiyo cites for this key, attempted 14 Oct 2026 but Gallica answered with a Cloudflare challenge (HTTP 403), so not yet opened (Next)
- [x] clear-pages: no. 68's clear opening read; no decipherment on the leaf
- [x] known-keys: Tomokiyo's Feria-Mansfeld table (keyM.tsv) applied; the 1592-93 office key (key92.tsv, fr. 3995 f. 97) does not fit (higher figures, three-letter word codes; 19 Sept 2026); Tomokiyo's Ibarra-Doria (1592) and Ibarra-Zúñiga (1593) key images listed with it are for other correspondences and were not applied; fr. 3995 f. 101 is an Italian nomenclature of another correspondence
- [x] print: Tomokiyo spanish3.htm (the key, no reading); BnF notice for fr. 3984
- [x] key-rebuild: keyM tested against 200 value-shuffled keys (-2.500 vs at most -3.378); unconstrained hill-climb rejected (collapses onto que); constrained fill accepts 57 = li, 64 (ha by context) not separated (5 Oct 2026)
- [x] retry: all 20 cipher lines transcribed (ct68.txt) and decoded with keyM + 57 = li; each line scored for sense (sense68.tsv)

## Next

Open fr. 3984 f. 130 (the other letter Tomokiyo cites for the Feria-Mansfeld key, about canvas 240 of
`btv1b9060633d`) when Gallica serves images again: a second letter in this cipher could fix some of the three-letter
word codes by repetition. Add the diacritic finals to `ct68.txt` from the image.
