# Siena, Concistoro 2308 fasc. 2 no. 25 (DECODE R4813): a lord's route by Lajatico, Radicondoli and Casole

Status: read — key recovered from the ciphertext alone; 477 of 496 cipher signs (96.2%) in words read as Italian.

Split on 14 Oct 2026 from `siena1421` under the one-key rule (George Lasry, 14 Oct 2026). The old entry grouped the
whole bundle of Sienese cipher letters (Concistoro 2308 fasc. 2), each in its own key. This slip has a key of its own;
the other letters with recovered keys are their own entries, each a different cipher with its own page: no. 14
([`targets/siena14/`](../siena14/NOTES.md)), no. 18 ([`targets/siena18/`](../siena18/NOTES.md)), no. 4
([`targets/borghesi1456/`](../borghesi1456/NOTES.md)), nos. 6 and 24 (George Lasry's
[`targets/siena1431/`](../siena1431/NOTES.md)). The unread pieces, the key index of fasc. 1 and the access notes stay in
[`targets/siena1421/`](../siena1421/NOTES.md), with the shared solvers (`homsolve2.py` etc.). The work below was done
on 24 and 30 Sept 2026 in the siena1421 sessions and is carried over from its NOTES.

Work date: 2026-09-24. From catalogue 336 (now narrowed to the unread pieces).

## The document

ASSi Concistoro 2308, fasc. 2 "Lettere in cifra", no. 25 (pencil number = Meister's numbering), DECODE R4813
(`Concistoro_2308_67`, dated "1500-1599", a placeholder; status N/A). Image `IMG_R4813_*` (ASSi, not public domain,
git-ignored in the main checkout's siena1421 working folder). Slip, 11 lines, all cipher, undated, unsigned.

## Transcription and key

- `transcripts/no25.txt`, `no25.tok`, `no25_signs.tok`: 496 tokens in 65 point-divided words, 22 signs built on a
  running horizontal stroke (agent E). Measured 14 Oct 2026: 496 tokens, 22 distinct.
- Italian, simple substitution (Sienese 'ch' spelling). `homsolve2.py` (words=1, it-cinquecento) gave the key
  unaided; hand fixes H = h, Y = m (`keys/no25_key.txt`). None of the 43 filed keys of fasc. 1 fits.
- Verification pass (agent E, `transcripts/no25_reading.txt`, transcription rev. 2): Y and X are two glyphs
  (Y = m, X = r), XB = z, G was S.

## Reading

"Noi aviamo chompreso che questo signiore no chavalcharà per lo modo che chostoro di qui voreveno, e dilivera senza
altra presa fare di qui partirsi e d'esare chostà, e crediamo sarà sabato prossimo, e farano la via di Laiaticho, e poi
di là si partirano e l'altro dì sarano a Radichondoli e per quello paese e ancho a Chasole ... e però richordiamo a la
signoria vostra che ne' detti luoghi faciate provedere di pane, vino, biada ... per fante propio significharemo a la
magnificientia vostra." An armed lord's route from the Volterra side (Lajatico) through Radicondoli and Casole into
Sienese territory; Siena asked to provision it. Undated.

**477 of 496 cipher signs (96.2%) in words read as Italian**, 18 signs in two unclear words ('s'hadra', 'o chon
grediamo'), 1 code sign TH unread. Meets the read bar.

30 Sept 2026 (quotation list for George Lasry): L03 w1 'presa' re-checked on the DECODE image (4000 px). The second
sign is the hooked X (r), which rules out 'spesa'; the blotted first sign has the loop-crossing-a-stem shape of Q (p),
not PHI. So 'senza altra presa fare' stands ('without making any further halt').

## Validation

`mk_validation.py` (split from siena1421's combined script on 14 Oct 2026) writes `validation.tsv` for no. 25 alone;
`docs/_validate.py siena25 --write`: pass (see profile.json outcome.validation).

## Remaining gaps
- two unclear words ('s'hadra', 'o chon grediamo', 18 signs) and the code sign TH - blocker: too-short; each occurs once, no context or sibling fixes them

## Escalation
- [x] siblings: the whole busta opened (keys R4746-R4789, letters R4790-R4814, R1858); no other letter in this key
- [x] clear-pages: none for this slip; the bundle's decipherments (nos. 8, 10, 13/16, 22) belong to other keys
- [x] known-keys: all 43 key sheets of fasc. 1 compared by eye; none fits
- [x] print: Meister 1902, Cecchini 1952, Senatore 2009: no printed decipherment of this slip
- [x] key-rebuild: key recovered by homsolve2 from the ciphertext alone, then fixed on the image
- [x] retry: every word re-checked on the image (transcription rev. 2, 30 Sept check of 'presa')
