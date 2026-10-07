**CONFIRMED-BUT-OVERSTATED.** The reconstruction is substantially plausible; an independently established ≥95% reading is **not demonstrated**.

`audit.py` reproduces **278 tokens: H164, C53, M40, I20, unread1**. A braced spelling counts once; plaintext and superscript endings add no tokens. Strict H+C+M = **257/278 = 92.45%**; generous assigned-reading coverage = **277/278 = 99.64%**, not measured accuracy. My contextual assessment accepts 17/20 inferences, giving a conditional **274/278 = 98.56%** if the original H+C+M assignments stand. Thus only a generous interpretation passes. Eight upgrades are needed to reach 265/278 (95.32%).

The independent parser reads **981 rows in 12 November page transcriptions** (`tx/*.tsv`). It produces 127 exact token agreements, 18 surface/inflection/abbreviation differences, eight substantive divergences, and 125 unresolved tokens without target-context filling. This conservative procedure is a reproducible evidence floor, not an estimate of decipherability. Every token, source and disagreement appears in `token_comparison.tsv`; `decoded.txt` uses only my rebuilt key.

No H circularity is demonstrated, but **17 H identifiers lack direct evidence in this corpus**; their claimed May witnesses are absent. Additionally, `39:` has “dien,” and `b386` has H-gloss “bylegginge” (`249_p272L.tsv:76`), contradicting the supplied “brengen.” Other substantive divergences: `63:` can/men, `59:` heeft/kan, and `51` k/h. The 54/59 ambiguity affects both letter and colon layers; it needs image verification, not automatic correction.

C operationally means a spelling containing contextual/structural letter assignments. It is neither direct attestation nor calibrated confidence. Several C letters already have H evidence; upgrading them would not change H+C+M. **No current I-code occurs directly in tx/**; `w141` has useful adjacent `W.140=weten` evidence, supporting at most contextual M.

I-item judgments (context and alternatives in `I_assessments.tsv`; SOLID means contextual):

- **SOLID:** n155 nemen/opgenomen; t175 trecken/trekken; t140 toonen; w204 woorden; c324 consteren/consteert; w141 geweten; v274 vernemen; h188 huys/huyse.
- **PLAUSIBLE:** p113 parolen; p122 participant; o177 onder anderen; m131 mannen; e274 engrosseren; g121 gemelde(n); v111 vaertuyg; o211 onderrechten; s254 soecken.
- **SPECULATIVE:** t218 tweehondert; d210 dertigh. Neither amount is uniquely constrained.
- **WRONG in context:** m161 mede; meer/meerder improves syntax but conflicts with the asserted alphabetical slot. Exact replacement remains open.
- **s439:** unread; sweeren speculative.

Controls reproduce **40/43=93.02%**, versus **1.24%** over 1,000 shuffled keys; without added names/words, 32/43 pass. This tests the spelling layer, not inferred codes. `blind_test.tsv` actually yields **M10/10; I3/6 hits, one near, two misses**. Frozen files already cite scan-128 glosses; s250→s258 was revised afterward. Clean blindness is not established.

**Fixes:** supply May transcriptions; repair blind-test accounting/provenance; reconcile conflicts; distinguish coverage from accuracy; bracket uncertain numbers; correct literal “consterent,” “latent,” “welckn,” and review “inen”; label alphabetic slots and morphological expansions as hypotheses.
