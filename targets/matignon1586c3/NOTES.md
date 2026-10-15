# Matignon's Cipher-3, 1586: BnF fr. 15572 f. 276 and fr. 15571 f. 179 — NOTES

Split on 14 Oct 2026 from `matignon1586` under the one-key rule (George Lasry, 14 Oct 2026). That entry (catalogue
item 12) joined these two leaves in **Matignon's Cipher-3** with the Mayenne–Forget despatches in **Cipher-1**, a
different cipher with its own entry: [`targets/matignon1586/`](../matignon1586/NOTES.md) (in progress, no page yet).
`f276/` and `f179/` moved here unchanged except for path references; the scans stay in the main checkout's
`targets/matignon1586/scan15571/` (git-ignored), with Tomokiyo's annotated image `img/BnFfr15571f179.jpg`.

**Outcome: read with known key (f. 276) and read from existing decipherment (f. 179), read in part.** The work is
**alejandrozarco's** (PR #25, 6–7 Oct 2026), reviewed and re-measured here; full accounts in
[`f276/SOLUTION.md`](f276/SOLUTION.md) and [`f179/SOLUTION.md`](f179/SOLUTION.md).

## The two leaves

| leaf | Gallica | lines | signs | read (measured) | method |
|---|---|---|---|---|---|
| fr. 15572 f. 276 | `btv1b9061879d` canvas 285 right | 22 | 734 | 706 (96.2%) | read with known key (Tomokiyo's table, checked and extended) |
| fr. 15571 f. 179 | `btv1b90618802` canvas 187 left, bound upside down | 21 | 509 | 473 (92.9%) | read from Tomokiyo's interlinear decipherment, checked with his key |
| **both** | | 43 | **1,243** | **1,179 (94.85%)** | |

Measured with `f276/scripts/measure.py <read_final.txt> 50` (the `targets/matignon1586/measure.py` rule: a sign counts
read only inside a run of at least three lexicon words totalling at least ten letters; lexicon of the shared `lang`
model `fr-1600-letters`, words ≥ 20 occurrences). Re-run 14 Oct 2026 after the move: 706/734 and 473/509, unchanged.
Shuffled-key controls (50): median 6.9% (max 29.3%) and 3.5% (max 23.8%).

The two leaves name the same people (Iehan Durant, La Rousière) and concern Poitou and Saintonge in 1586:

- **f. 276**: a Poitou intelligence note on the Catholic factions round La Roussière, Henri III's governor of
  Fontenay(-le-Comte): La Guiolle unsure of Le Puy, La Saussaie, the priory promised to Aubois, the sieurs de la
  Fontaine, la Chaie and Mirebeau; "Le Pui est ennuyé de la guerre". Its opening matches Tomokiyo's published line.
- **f. 179**: Frontin to come to terms with La Rousière's children; resolved to attack Pons, "il se poura prendre en
  ung mois"; sickness among the foot; "employer Lansac en … l'armée de mer". The siege and the sickness fit, not
  established, the plague in Mayenne's and Matignon's army round Castillon (Aug–Sept 1586).

Writer and recipient of both are not named on the leaves.

## The key

S. Tomokiyo's partial Cipher-3 table (cryptiana, *Henry III's Cipher with Ambassadors*): homophonic letter
substitution with word signs (60 *faire*, a β-like sign *de*, 20 *la*, 18 *le*, p-with-stroke *pour*, C with n *que*,
∴ *qui*), v a null. Checked by a hard-EM alignment of a value-blind transcription of the deciphered sibling f. 277r
against its contemporary decipherment on ff. 279r–280r (`f276/crib/`, `f276/scripts/align_em.py`): 1,271 signs align to
letters and 55 word signs to their words, the table's value the top emission for every frequent column. Added on the
leaves: `###` = *et* (8 places), split columns (ζ = i, ɤ = o; ꝫ = u, ʒ = t), ∂ = f, hooked ϱ = i, dotted v = u,
two-stroke # = i, the C with ε inside = q.

## Remaining gaps

- f. 276 L18 'K' and L14 'C with o inside', one-sign code words not in Tomokiyo's table - blocker: open-codes; each occurs once and neither recurs on these two leaves; the deciphered Cipher-3 siblings f. 189/190, f. 282 and fr. 15570 ff. 271-273 have not been searched for them
- f. 179 L13, the omega-with-overbar code sign (a person, Navarre?) - blocker: open-codes; one occurrence, Tomokiyo's 680-px magenta does not settle it
- blots: f. 276 L04 after "de lui", f. 179 L18 after "en" - blocker: illegible; ink blots, checked on the Gallica natives
- f. 276 L22 closing and f. 179 L20 "de la D[…]use", a struck sign and a few short spans - blocker: illegible; faint or struck signs at the edge of the slip; the other unread signs are words the period lexicon holds fewer than 20 times (prieure, escriuent)

## Escalation

- [x] siblings: ff. 277r-278r with their decipherment ff. 279-280 used to check and extend the key; f. 189/190, f. 282 and fr. 15570 ff. 271-273 not yet searched for the three code signs (named in the gaps)
- [x] clear-pages: ff. 279-280 are the clear decipherment of ff. 277-278; Tomokiyo's magenta interlinear used for f. 179
- [x] known-keys: Tomokiyo's partial Cipher-3 table applied; the Mayenne-Forget Cipher-1 key is a different cipher
- [x] print: no printed decipherment of either leaf; Tomokiyo's opening of f. 276 matches
- [x] key-rebuild: ### = et, the split columns, the C-family signs and the other additions found on the leaves (f276/SOLUTION.md)
- [x] retry: two independent reads of each leaf, then a second (f. 276) and third (f. 179) image pass on every disagreeing span

## Assumptions for George's review

- The two Cipher-3 leaves are one entry (one key). George Lasry's 2022 solution of fr. 15572 f. 43, which stood as a
  credit on the old matignon1586 entry, is credited on neither entry: f. 43 is not one of their documents and its
  cipher was not identified here.
