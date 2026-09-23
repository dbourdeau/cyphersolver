# Verification and remaining uncertainty, 23 September 2026

This session continued an existing project attempt, copied from
`.claude/worktrees/memoire-chiffre-1560-76e15d/memoire1560`. It did not independently discover
the initial substitution. Preserve that provenance when discussing novelty or model performance.

## What was checked

All ten page images were inspected alongside the inherited ciphertext and mechanical decrypt.
The first five pages now have a line reading; the inherited final-five-page reading was corrected.
The marginal addition at 153r.14 reads `assemblez en la chambre du conseil`; it was absent from
the inherited transcription. The cipher endorsement on the presumed dorse, 157v, reads
`Advertissemens`. Its adjacent later clear annotation says `henry second`, which conflicts with
the dated heading; it is not evidence for redating the document.

Full-resolution regional crops in `review/` resolve several formerly blank passages:
154v.03 `pour les faire respondre par leur bouche`; 154v.12–14 `Ayants recouvertz ... ou pour
le moins de la trouppe d'iceulx La Caze et Mesme, le roy pourra scavoir`; 155v.01 `Si ainsi estoit`;
155v.16–17 `qu'ils sement ... pour oster`; 156r.10 `ainsi que j'ay peu descouvrir`.
The line filler after `je me` at 155v.03 was incorrectly transcribed as the word code POUR:
the enlarged image shows a horizontal filler, not the Z-like word code.

## What the reading is

`reading_working.tsv` is a **normalized editorial reconstruction**, not output from a complete
machine key. Most lexical readings are inferred from the partial key, repeated symbols and
French syntax (repository grade I). It regularizes u/v, i/j, word boundaries, accents and some
scribal spelling. `decrypt_lines.txt` and `key.txt` retain the inherited state and visibly show
why key coverage must not be substituted for textual accuracy. In particular, that ASCII
transcription conflates b/g/u-like looped signs, a/i crosses, and e/n-like shapes. Some apparent
homophones may merely be inconsistent sign transcription; the precise system classification
remains provisional. The draft automatic alignment is a checking aid, NOT independent evidence.

## Every remaining gap was tried

* 152r.12: `Montseuignac` is a plausible literal name reading; the precise internal spelling and
  historical identification remain uncertain. Enlarged name crop and searches for Montseuignac,
  Montsevignac and Montseignac did not supply corroboration. Do not silently substitute a familiar name.
* 152r.15, 152v.21, 152v.26, 153r.10: short connected sign groups fit a plural pronoun or relative
  expansion (`ils`, `qui`, `qu'ils`). Enlarged comparisons support the sentence meanings, but
  the inherited transcription does not preserve enough distinction to establish an exact
  invariant expansion. Their provisional `ils` is bracketed. These are a small open word-code
  family; no original codebook has been found.
* 153r.17: the negative in `pour n'irriter le roy` is demanded by sense and a compact initial
  sign is present, but its precise distinction from the e-like sign remains uncertain at this
  point. Retain the bracket instead of making a diplomatic claim.
* 153v.08: an apparently canceled word is followed by a circled horizontal mark. It may be
  another canceled remnant or an independent small code. The sense continues `en toutes
  lesquelles`; the mark is explicitly retained as unread rather than silently omitted.

No full clause or paragraph remains without a proposed reading. These limited uncertainties
should not be described as a perfectly recovered alphabet or a 100% diplomatic decipherment.

## Escalation

* Siblings/clear pages: inherited images include adjacent leaves and catalogue notice; the
  inherited notes report clear Villars letters around this item and no decipherment. No clear
  copy was supplied or located in this session. The new marginal reading and dorse were checked.
* Published tables: local `ducroc/GL_CharlesIX.png` (George Lasry, 25 May 2022) inspected. Its
  letter assignments and word codes do not match: the target's circled-bar + zo + x consistently
  gives QUE, its omega-like sign L and x-like sign E, whereas that table assigns a different
  inventory. It is not the target key. The local GL.htm lists the Henri II examples, but both
  HTTP and HTTPS access to henryii.htm, GL.htm and a referenced key image failed with HTTP 503.
  **Henri II tables were not successfully obtained or tested.** `henryii_access.txt` records the failure.
* Print/prior art: exact-title search located the catalogue description via Biblissima, not a
  reading. Limited name searches did not find a matching edition. The user's no-prior-reading
  assertion is not independently established by these negative searches.
* Key rebuild/retry: used inherited partial substitution, compared repeated words and word codes,
  reviewed all pages, enlarged ambiguous regions and corrected the editorial text. Automatic
  per-line alignment checked for omitted source material and highlighted the canceled/filler
  issues above. A fresh stochastic solve over the same conflated transcription would not
  provide an independent verification of the reconstructed prose.

## Attribution cautions

The writer is unnamed; Montmorency is a likely recipient from the collection and `vostre grandeur`,
not an explicit deciphered address. The report names Montluc in the third person and says Fumel
is the writer's near neighbour. It does not identify the unnamed `chief` or the expected `prince`;
do not replace either by a named historical person without another source.
