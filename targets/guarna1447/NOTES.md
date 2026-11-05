# guarna1447: Nicolò Guarna to Francesco Sforza, Milan, 21 May 1447 (BnF italien 1584, ff. 153r-154r)

Status: read in part (Brice Dudout, 5 Nov 2026; 616 of about 852 cipher words = 72.3% certain or probable, unresolved stretches estimated; key K3 partial by our protocol: 0.759 on characters against 0.315, and M5 0.441 against 0.118).

Contributed by Brice Dudout (Europe chiffrée), with Claude Opus 5.5 agents. **Not in the catalogue or the leads as such**:
lead 1315 (Guarna's letters, ital. 1584) lists ff. 163-64, 232, 235, 238, 245, 259, 263, 268, 272, 286, 296, and the survey
`research/venice_milan_print/ital1584_copies_A.md` adds ff. 248, 261-62, 288; ff. 153-154 are in neither. We found no late
copy of this letter in the volume (views 140-160 checked).

## Document

Paris, BnF, italien 1584 (Archivio Sforzesco, 1447), ff. 153r, 153v, 154r (Gallica btv1b100373864, views 146-147; folio =
stamped number). Signed "Servitor N. Guarna", dated "Mli dominico 21 Maij 1447". Clear opening, connectives and close; most
of the body in cipher (about 50 lines on 153r, 52 on 153v, 3 on 154r; 3,960 cipher tokens). f. 156 is a 15th-century clear
text of the end of a letter of the same day, which matches the end of this cipher.

**No image, crop or thumbnail is included** (Gallica scans used for research only).

## Key (`key.tsv`)

Rebuilt here: no Guarna key was known (DECODE lists none among the keys Daniel viewed; Daniel reads Guarna's leaves by their
late copies). Training pair: Guarna's letter of 27 May 1447, cipher ff. 163r-163v, aligned with its 18th-century copy
ff. 161r-162v and 165r, the pair recorded in Daniel's survey of the ital. 1584 copies.

System: homophonic substitution with nulls (x, hd, qo...), **clear decoy words written inside the cipher** (quia, adviso,
tanto, tame, mo, cio, oto, si, ot, primum, tua, spes...), and a small code: A = Papa, cer = Signore, mea = non, con = qua,
tus = que, tuy = gente d'arme, ba = per, ra = perche, qt = quantunque, tri = Re de Ragona, SF = Signore de Faenza,
dn = dinari. Several signs carry more than one value in the table (listed by frequency): the key is partly polyphonic as
we have it, which may reflect our own confusions of look-alike signs.

## Validation (`validation.txt`)

| test | held-out block | key | metric | score | best of 200 controls | result |
|---|---|---|---|---|---|---|
| 1 | f. 153r ll. 1-20 (target letter) | K2 | M5 (Italian words of 5+ letters) | 0.441 | 0.118 | partial (gap 0.323) |
| 2 | f. 164r (training letter) vs its copy f. 165r | K3 | characters | 0.759 | 0.315 | partial (gap 0.445) |

Thresholds fixed in advance: >= 0.60 (M5) or >= 0.85 (characters), and >= 0.30 above the best control. **Partial by our
protocol, twice.** The end of the target cipher agrees word for word with the clear text of f. 156 (not a pre-registered test).

## Reading (`reading.md`, `translation.md`)

| words | certain | probable | restored | unresolved (estimated) | certain + probable |
|---|---|---|---|---|---|
| 852 | 583 | 33 | 0 | 236 | 616 = 72.3% |

**Read in part** (`reading_review` grade B). The unresolved stretches are counted as length/5 words; the total is an estimate.
By part: H 71%, rest of 153r 71%, 153v 73%, 154r 91% (from our working count).

**Content.** Guarna reports an audience with Duke Filippo Maria Visconti about Sforza's coming to Lombardy. The state is in
danger: enemies in the field, troops poorly provided, the plague. On money: 9,000 ducats, money expected from the gabelle and
for the troops at Cremona, then "not another florin for a long while". The Duke answered "more openly than the other times"
and shows a "fervent wish" for Sforza's coming; Sforza should come quickly, with all or part of his company.

## Declared deviations

1. **The key is not validated**: both tests are partial (0.441 < 0.60; 0.759 < 0.85). Both held-out blocks are used.
2. **Two slips before freezing.** Line 20 of H (clear only) was seen before H was frozen. The copy f. 165r was seen at low
   resolution while H' was chosen; it was not used for the key or the language model.
3. **The unresolved count is an estimate** (stretch length / 5), and our earlier note said 862 words and 72.6%; the recount
   by script on `reading.md` gives 852 and 72.3%.
4. **Part of the content is not new**: f. 153v from about l. 46 to f. 154r agrees with the 15th-century clear of f. 156.
5. **A blind shape sheet on the near-identical signs is still pending** (h-like 4 / hk, sigma / o with a hook, t / T / z,
   hs / h): not answered, so not applied. The second decode with K3 changed no word.
6. **One reader** (an AI agent) on a microfilm; no palaeographer checked the signs.

## Remaining gaps

- About 236 unresolved words (estimated), mostly on 153r and 153v ll. 4-19 - blocker: illegible; look-alike signs not separated on the microfilm; the pending shape sheet and a fine re-transcription are the next step.
- No fresh held-out block to validate K3 - blocker: no-key-material; H and H' are used; another Guarna leaf with a complete late copy (lead 1315) would serve.

## Escalation

- [x] siblings: views 140-160 of ital. 1584 inventoried; ff. 163-164 (27 May) used as the training pair; f. 156 identified as the clear of the end.
- [x] clear-pages: f. 156 (15th-c. clear) and f. 155 (clear slip) checked; f. 156 matches only the end of the letter.
- [x] known-keys: none of the 208 DECODE keys listed by Daniel is Guarna's; R1857 (Barbavara/Pusterla) and R5323/R5324 (the Duke) belong to other writers and were not applied.
- [x] print: four web searches (the fourth on 5 Nov 2026: Guarna to Francesco Sforza, 1447) found nothing on Guarna or this letter; Cerioni, *La diplomazia sforzesca* (1970), and printed calendars of BnF ital. 1584 not seen, named as the next print sources.
- [x] key-rebuild: K, K2, K3 extended from the training pair (163v to the end).
- [x] retry: the whole letter decoded again with K3; no word changed.

## Prior work

When checked through the GitHub API (origin/main 895f21c4, 5 Nov 2026): no target, PR or issue for ff. 153-154; lead 1315
does not list them; `targets/barbavara1447` and `targets/visconti1447` (same volume) concern other writers. No edition found
(three web searches). Not seen: Cerioni (1970) and printed calendars. Tomokiyo, WAINUT and Brackx have no part in this target.
If an edition prints this letter, we will credit it.

## Credits

- `dudout`: transcription, key K3, the two measurements, the reading.
- `contemporary`: prior solution for the end of the letter (the clear text of f. 156).
- `bourdeau`: pointer (lead 1315 and the survey of ital. 1584 late copies, which gave the training pair ff. 163-164 / 161-162).

## Files

`transcription.txt`, `decryption.txt`, `key.tsv` (CC BY 4.0), `validation.txt`, `reading.md`, `translation.md`, `profile.json`.
