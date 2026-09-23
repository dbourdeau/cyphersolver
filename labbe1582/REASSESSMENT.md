# Renewed attempt, 23 September 2026

**Cipher not read; no validated key. Move on from this attempt, keeping the research target open.** The clear prose is not a partial cryptographic solution. The earlier local notes stopped before transcribing Prague’s insertions and overstated the completeness of the clear reading. The work below does not establish that the cipher is intrinsically impossible.

## What was added

- Reinspected the cached target scans and both May witnesses at native scale.
- Created `cipher_inventory.md` and `runs_draft.json`: **29 Prague insertions**, plus the May passage divided at clear *plusieurs*. The inventory includes all cipher stretches identified on the target scans; the repeated lower portion of f64 on f65 left is not counted twice.
- Measured **834 Prague draft digits and 77 May draft digits** with `_check_profile.py --measure ... --digits --width 1`. These are counts of draft written figures, not established cipher-token counts. One obscured locus is `[?]`; other glyph/joining uncertainties remain at run level.
- Tested 1,566 retained forward/backward prefix configurations, six fixed-pair variants, further null treatments and a May crib. No output gave continuous defensible French in context.
- Recovered **538/538 letters** in a synthetic substitution control. This validates that restricted solver implementation, not its applicability to this manuscript.
- Found an explicit cipher-dispatch reference in the March letter and a specific earlier-letter lead in **BnF fr. 4695 no. 51**.
- Created `profile.json`, outcome **not read**, key **none**.

## Best archival lead: a cipher reportedly sent in February

On [f63](https://gallica.bnf.fr/ark:/12148/btv1b9060073v/f63), L’Abbé says that on the 24th of the previous month he wrote by two routes to a correspondent whose name appears to be **Barquin**, sending a copy of the cipher previously sent with his letters to Nevers:

> Le 24e dudict passé j’escrivay au Sr Barquin [name provisional] par deux voies diverses […] et luy ay envoyé par l’une, copie de la chiffre que je vous envoyay avec mesdictes dernieres, affin que nous nous pouvions escrire librement.

Checked against `images/key_reference.png`, cropped from native f63. **“Par l’une” means by one of the two routes**, not a place-name “Linc.” The date is 24 February 1577. This establishes a reported cipher dispatch, not the survival of its enclosure or the identity of the March and May keys.

A [catalogue mirror](https://biblioteca.phorteeducacional.com.br/items/5616940) identifies **BnF français 4695 no. 51**, L’Abbé to Nevers, Prague, **5 February 1577**. Its original is [Gallica btv1b90582923](https://gallica.bnf.fr/ark:/12148/btv1b90582923). The volume also includes his letter of 20 April as no. 55 and a letter from **Gaspar Barchino** as no. 25. Barchino is a possible lead for Barquin, not a proved identification.

The 5 February letter could belong to the preceding correspondence mentioned in March. **Its text, enclosures, folio and canvas have not been inspected.** Gallica image/manifest requests failed with connection resets or timeout through Python, curl and the in-app browser. The BnF catalogue endpoint also failed. Searches found no accessible contemporary key or decipherment. The mirror is a catalogue lead, not a substitute for viewing the source.

## Clear prose and corrections

`prague_reading.md` is a content outline; `breslau_reading.md` is a provisional transcription of clear prose. Neither is a complete diplomatic edition or recovered cipher plaintext. Their historical account concerns Nevers’s financial/legal business and imperial-court intelligence; sensitive assertions remain encrypted.

Two corrections to the earlier Prague outline are directly visible: the opening describes **L’Abbé’s own fever and nineteen days confined to his room**; f66 requests **200,000 talers each year for the stated years** for the Hungarian frontier, not 100,000 from each estate. Other names, amounts and legal expressions in the older readings still require an editorial pass before quotation.

The folder name `labbe1582` is inherited; the target letters date from **1577**.

## What the cryptanalysis does and does not show

The numerical system and token boundaries remain undetermined. French is the expected plaintext language from the surrounding prose, not a result established by decoding. Both May witnesses substantially repeat the cipher; the apparent `53/35` and `13/14` differences remain unresolved.

The previous session’s June 1580 “Chifre avec Madame” comparison is retained as prior work, not a comprehensive exclusion of Nevers’s keys. A cached 1584 Nevers symbolic alphabet was inspected in this attempt; it does not supply this numerical table.

Unrestricted homophonic scoring initially collapsed to repeated letters; those outputs were discarded. Later probes used constrained substitutions. The C# sweep also penalizes repeated triples. French-looking fragments in optimized outputs are not evidence by themselves.

The possible *mais … jamais* pattern in May was an **imposed crib**. Neither it nor the additional *ne/ni* hypothesis produced a coherent extension. **Do not treat `33=m`, `02=a`, `13=i`, `45=s`, `04=a`, `43=n` or `16=e` as recovered key values.** None is validated.

The successful synthetic test establishes only that clean substitution text of that form can be recovered. It does not resolve glyph errors, null conventions, syllabic or word values, or changes of key in the real letters. Negative searches are bounded attempts, not proofs of impossibility.

## Remaining gaps

- All Prague cipher insertions — blocker: no-key-material; no validated plaintext or segmentation. The expanded inventory is a draft, not a verified character edition.
- May cipher in nos. 37 and 38 — blocker: no-key-material; 77 draft digits and a substantially duplicate witness, with no clear counterpart.
- Cramped/overwritten Prague figures, especially f64r08 — blocker: illegible; an obscured locus is `[?]`, and other ambiguous figures remain flagged at run level.
- Earlier letters and enclosures, especially fr. 4695 no. 51 — blocker: needs-physical-access; here this means restored access to the digital images or another supplied copy, not necessarily an in-person visit.
- A continuous edition of all clear prose remains unfinished and is not counted as a partial cryptographic solve.

## Escalation

- [x] siblings: compared the May duplicate; identified fr. 4695 nos. 51 and 55 in the catalogue mirror. Their images remain inaccessible and unchecked.
- [x] clear-pages: inspected cached target continuations and duplicated views. No clear equivalent of an encrypted insertion was identified.
- [x] known-keys: retained the prior 1580 mismatch and inspected the cached 1584 symbolic alphabet; archive access prevented broader uncached comparisons.
- [x] print: renewed searches for L’Abbé, Nevers, Prague/Breslau 1577, the correspondent and shelfmarks found catalogue leads, not a key or reading. This is not a claim to have searched every printed edition.
- [x] key-rebuild: tested prefix/suffix groupings, fixed pairs and null treatments with French n-gram scoring; no coherent key resulted.
- [x] retry: expanded to all identified Prague stretches, compared f64 with its repeated view on f65, and retried pair/null and crib hypotheses. Rejected the crib after its extension failed.

## Disposition

Move on pending better evidence, especially the cipher-dispatch trail. Preserve the target as **attempted, open**, not solved or partially deciphered. No solved-ledger entry is warranted. No DECODE ID has been verified. This attempt is documented on the project site; no DECODE edit or external message was sent.

The attempted/unread write-up was prepared at the user’s request with `.claude/skills/writeup/SKILL.md`. No solved-ledger entry is warranted.
