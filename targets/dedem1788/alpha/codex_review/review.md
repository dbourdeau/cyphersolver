**Structure: OVERSTATED; alphabetical ordering is strongly supported.** Independently reconstructed local crib fragments give 95 ordinary group/reading pairs: within-sheet Spearman **.799**, versus numeric **.351**, four-column **.567**, six-column **.645**. Ten columns also gives **.799**, necessarily: within each 500-block both layouts induce identical ranks. Five columns wins globally (.874 versus ten-column .828), but physical sheets, one complete bilingual list, and the 3150 boundary remain hypotheses. This manually selected sample is not a blinded gold alignment.

The early, unfiltered 95-pair list still scores **.602** within-sheet (10,000 permutations, maximum over seven layouts: p99.9=.368). Thus the signal survives exclusions. However, later CORE selection explicitly uses slot fit, and bootstrapping enforces monotonicity. **The 94% validation leaks:** rebuilding restores full CORE, including 74 distinct held keys in the first fold; reference alignments also use full-data anchors. “Exact” scoring accepts prefixes. The 74%-versus-2% comparison is therefore not independent validation.

**Word verdicts:** S=SOLID; P=PLAUSIBLE; X=SPECULATIVE. Ellipses remain unresolved.

R2131: PORTA[S] … aan[S] [den][X] ENVOYE[P] verklaard[X] … heeft[P] om[S] gedurende[P] deze[P] Oorlog[S] met[S] de[S] Franschen[X] en[S] sig[P] in[P] … neutraliteit[X] te[S] houden[P].

R2122: ENVOYE[P] het[S] verlangen[X] en[S] van[S] PORTA[S] ontrent[P] het[S] doen[P] een[S] -er[X] negociatie[X] in[P] [de][X] Republicq[P] niet[S] geheel[S] te[S] moeten[P] en[S] laaten[P] ignoreren[S, plaintext]. Possible suffix joining needs explicit justification.

Independent witnesses, using zero-based cipher positions: **1764/Oorlog**, R2121 #486, clear line 57; **1518/met**, #10, clear line 6; **86/de**, R2053 #5, clear line 1 (R2121 #11 instead corresponds to *den*). **3373/Porta**: R2121 #180, clear line 23. **3273/Porte Ottomanne**: R1947 #42, clear line 10. **3610/envoy title**: R1947 #407, clear lines 36–37; R2053 #9, clear line 1—possibly including “de Prusse”.

The supplied mixed lexicon admits 9/19/5/18 forms for verklaard/Franschen/neutraliteit/verlangen; these are corpus-limited counts, not all Dutch possibilities. **Negociatie violates its own lower bound, negociations**; negotiatie would fit. Only 8/20 and 11/20 key-passage groups have A/B labels. Full width-matched sentence-template nulls produced 0/200,000 completions each; short-clause searches nevertheless found 3/512 and 4/512 fitting alternatives. Neither experiment estimates unrestricted analyst false-reading rates.

Historical sanity: R2121's loan discussion supports a financing theme; these files do not independently establish the French-war/neutrality message.

Before publication: adjudicate crib alignment, repair tokenization, freeze spellings/segmentation, remove fold leakage, test unseen documents, and separate attestation from contextual coverage. Scripts, slot alternatives and simulation limitations are documented in [evidence.md](evidence.md).
