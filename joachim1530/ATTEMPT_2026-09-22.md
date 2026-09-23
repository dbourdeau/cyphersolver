# Passano's ciphered account, London, 15 March 1530

Status: attempted and closed from the present evidence — no verified reading of the cipher.

## Source and identification

BnF, Collection Clairambault 331, f. 156r–157v, [Gallica btv1b9000761d](https://gallica.bnf.fr/ark:/12148/btv1b9000761d). Digital canvases `f148`–`f150` correspond to the three sides. The heading identifies a copy of a letter to the king and one enclosed for the Grand Master, dated 15 March. The Italian letter is by Giovan Gioacchino da Passano (Jean Joachim, sieur de Vaux), writing from London to Francis I. The account attached to it occupies f. 157r–v. Its nine lines of cipher are followed by separate, clear scudi amounts. The French copyist notes: “En apres suivent une page 3 lignes en chiffre. Et puis est escript ce qui suit.”

The immediately preceding clear text says Passano is trying to recover payments from Cardinal Wolsey: “8 termini et pagamenti per 4 anni.” It mentions outstanding quittances for May and November 1528 and May 1529, and a payment of 12,500 scudi. The clear passage after the cipher resumes “Sire, dopp[o] l'haver con ogni reverentia et humilita basciati le mani de V. Mta ...”. These are context, **not decrypted text**.

Tomokiyo lists f. 156 among the undeciphered Italian letters in this volume, describing the cipher as apparently a list of sums. No DECODE record or published decipherment was found in the searches of 22 September 2026. Le Grand's *Histoire du divorce de Henry VIII*, vol. 3, and *Letters and Papers Henry VIII* no. 6307 contain a **related but differently dated** Passano report; they do not supply a reading of this account. They must not be treated as a parallel plaintext.

## Cipher transcription and structure

`ciphertext.txt` records 402 proposed signs in nine account entries, omitting the plain “in summa” and Roman-numeral amounts. It is a provisional, sign-level transcription from full-resolution Gallica IIIF images (`f149`–`f150`), with 20 aliased signs. The sheet has no secure word divisions. Letter-like and numeral-like forms recur; dots above some forms may be meaningful and are not resolved. This is a research transcription, not a diplomatic one, and any further attack should recheck it against the manuscript.

Index of coincidence: 0.0819. The most common aliases are `4` (58), `3` (51), `9` (39), `i` (39), `S` (35), `7` (33), and `m` (29). Item lengths and repeated runs were preserved. The different cipher at f. 149 in the same volume and the Passano/Sormano cipher in BnF fr. 3096 have visibly different sign inventories; neither gives an established key here.

## Attempts and controls

- Italian one-to-one substitution search, including 40 × 80,000-step incremental annealing, did not yield connected language. Period Italian, modern Italian, French, Spanish, Latin, and English models were tried; reversal and adjacent-pair swapping were also tried. The initial Italian solver erroneously omitted `v`; that defect was corrected and the results rerun.
- Treating frequent signs as spaces or nulls, many-to-one mappings, and Italian dictionary word segmentation also failed to yield a defensible reading.
- A positive control of matching length and item structure recovered all 20 of 20 assignments for an artificial Italian monoalphabetic cryptogram. With 10% and 20% random sign corruption it still recovered 18/20 and 17/20, respectively, with recognizable Italian. This supports rejecting **simple one-sign/one-letter substitution on the current transcription**, not all possible cipher systems. Systematic glyph conflation or a more complex cipher could still account for the failure.

No plaintext value, keyword, cipher key, or connected passage is verified. The clear letter identifies the business of the account but does not disclose the text of its entries.

## Remaining gaps

The 402 cipher signs remain unread. A full diplomatic transcription should distinguish dotted and lookalike signs and include the clear amounts in alignment with the nine entries. The original outgoing letter, its enclosure, or a matching cipher key, if extant, would be decisive. The heading's reference to “Vol. 70 fol. 78” has not been identified securely with a surviving manuscript, and no parallel plaintext has been verified.

## Escalation

Compare the Clairambault copy with any original of the 15 March 1530 letter or attached account; search the diplomatic registers and key books for Passano's London correspondence. If an independent copy or key is found, redo the sign inventory before attempting a solution. Until then, classify this as attempted and closed from the present evidence, not solved.
