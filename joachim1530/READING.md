# The surviving ciphered account: edited reading

BnF Clairambault 331, letter beginning f. 156r; cipher on f. 157r–v, Gallica canvases f149–f150. Read on 23 September 2026. The heading dates the copy 15 March 1530; the sender is attributed to Giovan Gioacchino da Passano. The body addresses Francis I. The page also contains a subsequent letter for the Grand Master.

**This is a reconstructed reading, with explicit gaps and emendations, not a contemporary decipherment.** The account is substantially read; it is not a claim to have recovered the omitted continuation or every word. Run `python joachim1530/decode.py` to regenerate the literal reading, the edited unspaced reading, the 402-row audit, and the coverage figures.

## Conventions and coverage

- `[S2]`, `[D]`, `[Q]` preserve three rare signs whose expansions are not established. `[D]` probably refers to Wolsey; `[S2]` may be a royal title. These contextual identifications are **not** entered as solved key values.
- Italicized editorial comments and punctuation are not encrypted words. Spacing below is editorial. u/v is displayed as v where appropriate; the decoder retains u.
- All established values are **I**, inferred from the ciphertext; none is H (historical key) or C (independent known plaintext). **M** marks residual uncertainty. Thirteen local substitutions are listed by exact line and position in `key.json` and `reading_tokens.tsv`; most concern displaced or missing dots.
- 402 observed tokens, 28 aliases; **395/402 assigned (98.26%)**, **386/402 coherent on the conservative audit (96.02%)**. The 16 excluded tokens comprise seven rare-sign occurrences, four letters in the two `so [D]` expressions, the four-letter `dese` financial junction, and one apparent extra stroke in `parutite`. This is an editorial measure, not an independently measured cryptanalytic accuracy. The 13 emendations are included in coherent coverage and exposed individually.
- The final 402 count is coincidentally the same as the old transcription's count. It is a different segmentation and inventory. The first fresh dotted transcription had 397 tokens; recognizing `1 m S m m` as encrypted `un ann` added five. The old file had wrongly called it clear “in summa.”

## Italian reading, in manuscript order

**Introduction, f. 157r, lines 1–3**

> Sapera vostra magesta che questo [S2] de gli beni del
> [D], per quanto si dice, son pervenuti circa **[clear amount: m over DCCC, scuti]**,
> in l'infrascrite par[u?]tite, cioe:

The literal third line has `parutite`; *partite* is the likely intended word, but the extra stroke is kept outside the coherent count. The opening's syntax and royal-title expansion are not silently repaired by supplying an “a” or a verb. The gist is a report, expressly qualified by “per quanto si dice,” about goods associated with the person `[D]`.

| Entry | Edited Italian | Clear numeral component |
|---|---|---|
| 1 | In denari contanti | CL, followed by a raised abbreviation, scuti |
| 2 | In crediti de so [D] per [Q] interditi et poi levati | L, raised abbreviation, scuti |
| 3 | Per gli fruti de un anno de lo intrate de so [D] | LX, raised abbreviation, scuti |
| 4 | In baghe circa | XX, raised abbreviation, scuti |
| 5 | In vasele d'oro et d'argento | CCL, raised abbreviation, scuti |
| 6 | In supelectili de casa per el meno | CC, raised abbreviation, scuti |

`so [D]` is literal; an abbreviated reference to the person is plausible but not expanded. `baghe` is kept as written, tentatively jewels/rings in this asset list. `vasele` means vessels and `supelectili` household furnishings. `per el meno` is “at least.” `interditi` is the recovered word; the precise legal meaning and agency of `[Q]` remain unsettled.

**Final passage, f. 157v, lines 2–6**

> Per l'intrate del vescoato de Vinchiestri et abadia de sancto Albano, rebatuti
> **[clear stacked m/m-like notation, scuti]** dese intrato al deto [D] insieme
> con lo arcivescoato de Diorch, asignati et ordinati, havera [Q] per ano circa
> **[XX + raised abbreviation, scuti].**

The toponyms identify Winchester, St Albans and York. *Rebatuti* (“deducted”) is supported; the earlier tempting *restituti* (“restored”) is **not** the recovered word. `de Diorch` is retained, not silently changed to `de Iorch`. `asignati` is the spelling with one s. The first four letters on the middle line decode literally `dese`; this is an attested regional word for “ten,” but its attachment to the stacked notation and following `intrato` is not settled here. No precise deduction or allocation is asserted in translation.

**Bottom total:** a large M above `DCCL . Scuti`, introduced by a separate sum mark. The seven right-margin numeral components add correctly: CL + L + LX + XX + CCL + CC + XX = DCCL, or 150 + 50 + 60 + 20 + 250 + 200 + 20 = 750. Their apparent thousand multipliers suggest 750,000 scudi, versus the introduction's approximate 800,000; that scale remains an editorial interpretation of the financial notation. The inline stacked notation is not an eighth right-margin item. The list mixes property and revenue descriptions, so it must not be represented as a modern audited balance sheet.

## English rendering of the established sense

Your Majesty will learn that, according to what people say, goods of `[D, probably the Cardinal]` have come to the amount written, in the following items: ready cash; credits, with an unresolved reference to their restriction and subsequent recovery; one year's income; jewels or rings; gold and silver vessels; and household furnishings, “at least” the amount stated.

The final passage concerns the revenues of Winchester and the abbey of St Albans, a deduction whose numerical wording remains uncertain, and income assigned or ordered together with the archbishopric of York. It ends with what `[Q]` will have annually. The rare signs are left visible because substituting “king,” “cardinal,” or “he” at every occurrence would give an unwarrantedly definite account of the transfers.

## The continuation that is not present

Immediately afterwards the copyist says: “En apres suivent une page 3 lignes en chiffre. Et puis est escript ce qui suit.” A page and three lines of the original cipher have been omitted, not photographed elsewhere in this copy. The next text is the clear valediction, beginning “Sire, doppo l'haver…”, followed by the accompanying letter. The missing original passage has no available token count, is outside the 402-token denominator, and is **unread**. Recovering it requires the original or an independent complete copy.

## Source and novelty limits

The plaintext above was obtained from the manuscript signs, after the 22 September attempt had failed. No published parallel plaintext was used. *Letters and Papers* IV no. 6307 is dated **4 April 1530**, not this March letter, and cannot validate the account. Subsequent dictionary checking confirms that `dese` can mean “ten”; it supplies no parallel text for this document. The absence of a prior reading is the result of the searches recorded in NOTES, not proof that none exists.

- [Gallica, f149 (f. 157r)](https://gallica.bnf.fr/ark:/12148/btv1b9000761d/f149.item)
- [Gallica, f150 (f. 157v)](https://gallica.bnf.fr/ark:/12148/btv1b9000761d/f150.item)
- [OVI/CNR AGLIO: dese under dieci](https://aglio.ovi.cnr.it/results_f.php?ag=30&x=4)
- [Letters and Papers no. 6307, 4 April 1530](https://www.thomasmorestudies.org/wp-content/uploads/2021/01/1530_LP_4.6307.pdf)
