# Passano's account of Wolsey's assets, London, March 1530

Status: read — surviving account substantially deciphered, 386/402 tokens coherent (96.02%) with 13 explicit emendations; key partial. The copyist's omitted page and three lines remain unavailable and unread.

## Result, 23 September 2026

The 22 September negative was overturned by re-transcription. Dots distinguish plaintext letters: `3=i / 3d=d`, `7=o / 7d=p`, `8=i / 8d=q`, `9=o / 9d=t`, and `S=a / Sd=g`. Straight strokes (`1`, `1d`) were separated from curved `2`, `2d`. A many-to-one substitution search on this inventory immediately gave connected Italian. The account lists ready cash, credits, one year's revenues, baghe (probably jewels/rings), gold and silver vessels, and household furnishings; its last passage names Winchester, St Albans and York.

The formerly “clear in summa” is actually cipher `1 m S m m`, followed by `7`: **un anno**. It belongs in the ciphertext. The old 402-token transcription and the final 402-token transcription are not the same sign inventory; the fresh dotted transcription initially had 397 tokens, to which these five were added. There are sixteen physical cipher lines, grouped into nine provisional transcription blocks, **not nine cipher lines or nine independent accounts**. The actual structure is an introduction, six short listed items and a longer final passage, with seven right-margin entries.

`READING.md` gives every surviving line in Italian, cautious English sense, the clear sums, all residual problems, and the unavailable continuation. `key.json` supplies the inferred alphabet and each local emendation. `decode.py` creates literal and edited readings plus a 402-row token audit. No historical key or parallel decipherment has been found.

## Source and identification

BnF Clairambault 331, f. 156r–157v, [Gallica btv1b9000761d](https://gallica.bnf.fr/ark:/12148/btv1b9000761d), digital canvases f148–f150 (two facing pages per canvas). The surviving cipher is f. 157r–v, f149 right and f150 left. The copy's heading dates the royal letter and accompanying Grand Master's letter 15 March 1530. Attribution to Giovan Gioacchino da Passano (Jean Joachim, sieur de Vaux) follows the existing identification and London diplomatic context; it is not a newly decrypted signature. The royal letter addresses Francis I. The cipher account occurs before the valediction and the second letter.

The preceding clear text discusses recovering payments and quittances from Cardinal Wolsey, including May and November 1528 and May 1529 and 12,500 scudi. This context was known before the attack, but is not a parallel plaintext. The new account reading identifies a different subject: the disposition of goods and revenues, not merely the French instalment schedule.

The marginal source reference appears **Vol. 79, fol. 78**, correcting the earlier notes' “70”; its present shelfmark is unverified. After the account the copyist explicitly says a page and three lines in cipher follow, then resumes clear Italian. This is an omission in the historical copy, not a technical image-access problem.

## Prior work and contamination

The user's candidate and the 22 September research identified Tomokiyo's Francis I page as listing this passage undeciphered. There is no identified DECODE record and no matching key or published decipherment in the local material. On 23 September Cryptiana returned HTTP 503 and the Gallica viewer failed in the web text tool; the previously downloaded Gallica images were inspected directly. Searches for the shelfmark, Passano, Wolsey and recovered wording did not locate a parallel text. This supports “no prior reading found,” not a categorical novelty claim.

The related Passano dispatch in Le Grand III p. 412 and *Letters and Papers Henry VIII* IV no. 6307 is dated **4 April 1530**. It is not the plaintext of this March account. A post-solution lexical check in OVI/CNR's AGLIO confirms regional `dese` = ten, but the financial sentence remains uncertain. No target plaintext was imported from that source.

## Attack history and verification

1. The previous session transcribed 402 proposed signs as 20 classes; substitution, language variants, null/space hypotheses and many-to-one searches failed. Its positive and noisy controls worked, but random corruption could not exclude systematic merging of dotted signs. The old transcription and scripts remain as evidence of this failed route.
2. Fresh inspection produced `ciphertext_dotted.txt`, 397 tokens, 28 types. `recheck/search.cjs` uses a seeded incremental four-gram annealer, the shared `it-cinquecento` model and a frequency-divergence penalty. 100 restarts × 100,000 iterations gave connected text from random keys. Without the penalty the model preferred repeated `i`, a failed preliminary trial. The merged-sign trial still yielded distorted text. Saved result files retain both principal outputs.
3. Manual extension supplied `1d=b`, `n=m`, `T=s`, and identified three unsolved rare signs. Image checking led to 13 local contextual emendations, mostly missing/displaced dots. These are exposed rather than silently baked into the alphabet. `Rebatuti`, not `restituti`, is the supported reading. The cipher phrase `un anno` was recovered from the passage previously called clear.
4. The final inventory has 402 tokens, 28 aliases, IC 0.0602 (measured by `_check_profile.py --measure`). 395 tokens have inferred letter values; 386 read coherently under the conservative editorial audit. Internal checks are repeated words, connected Italian on both sides, three place names, accounting vocabulary, and the sum of the right-margin numeral components: 150+50+60+20+250+200+20=750. Numerical multipliers and the inline stacked notation remain qualified. No independent contemporary key is claimed.

## Reproduction

From the repository root:

```
python joachim1530/decode.py
python docs/_check_profile.py --measure joachim1530/ciphertext_rechecked.txt
python docs/_check_profile.py joachim1530
```

For the breakthrough run:

```
python joachim1530/recheck/prepare.py
node joachim1530/recheck/search.cjs dotted 100 100000 2351
```

The search deliberately uses the pre-breakthrough 397-token transcription without manual corrections. The final decoder uses the 402-token inventory. The model binary is regenerated, not committed. Full images are in the shared `gallica_331/` cache; the site includes credited crops of both cipher pages.

## Remaining gaps

- `[D]` (four occurrences), `[Q]` (two), `[S2]` (one): blocker: no-key-material. Wolsey and a royal title are plausible for D and S2; Q may be a pronoun or title. None has a verified expansion. Do not substitute whole words as if recovered from a key.
- `so [D]` twice, the extra stroke in `parutite`, and the `dese`/stacked-sum junction: blocker: no-key-material. All occurrences were inspected and decoded; an independent copy or original is needed to settle abbreviation, copy errors, segmentation and numerical phrasing. Nine additional tokens are excluded from coherent coverage despite assigned letter values. The 13 emendations elsewhere are separately audited.
- A page and three lines explicitly omitted by the copyist: blocker: needs-physical-access (or an independent complete digital copy). These are not present in the supplied manuscript. No token denominator or plaintext can be manufactured for them.

## Escalation

- [x] siblings: reopened manuscript f. 149, Gallica f141; its Greek/geometric inventory is different. Its heading/body dating is inconsistent. It does not supply this account's key. Neighbouring clear material is not a decipherment.
- [x] clear-pages: the full f148–f150 opening was inspected. After the account are a declared omission, valediction and accompanying clear letter, not a plaintext of the account.
- [x] known-keys: the existing comparison with Ferrara Passano/Sormano material, fr. 3096, yielded no matching inventory. No historical key for this London account was located. The account alphabet is now reconstructed explicitly.
- [x] print: checked local Le Grand/Letters and Papers research and verified no. 6307's April date. Shelfmark, correspondent and wording searches yielded no parallel. Cryptiana was unavailable on recheck; no fresh full-site search is claimed.
- [x] key-rebuild: dotted transcription, seeded many-to-one annealing, repeated-context key extension, complete image checking, all 16 lines decoded, un anno restored.
- [x] retry: all rare signs and awkward transitions reread. D, Q, S2, so and dese remain explicit and uncounted; further expansion requires outside evidence. The omitted continuation cannot be attacked from this copy.

## Writeup outcome

The **surviving account** meets the repository's >=95% read bar with a partial key. This is not “whole original letter decrypted”; the absent continuation is prominently excluded from the percentage. No DECODE correction is sent because no record has been identified. Catalogue item 281 is removed from the open list and the old negative superseded; the failed evidence is preserved.
