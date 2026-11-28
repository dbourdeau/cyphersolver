# Independent check of the Farnese cipher, Catalogue No. 2339

19 November 2026 · Archivio di Stato di Firenze, Mediceo del Principato 384, c. 78r

**The swarm broke the cipher.** Ordinary figures recover connected Italian throughout the page. Several of the final edition’s names, code words and sentences still depend on editorial reconstruction. The evidence supports sending the result for independent review. A publication claim of 100% decipherment or first reading in 479 years exceeds the evidence.

## A reproducible test of the break

I fetched the full-resolution manuscript JPEG directly from Florence. Its SHA-256 matched the supplied archive JPEG byte for byte, `59ae6e24069fc7d7883f467e36bdbad55a88bca65f9b58ae4f9581e6f680909a`. A native DeepZoom tile covering the right end of the opening lines also matched the corresponding pixels of the supplied PNG. The live catalogue page matched the repository copy. The following test uses the swarm’s digit transcription. The visual audit sampled the manuscript, including the disputed passages below. [Florence folio 78r](https://archiviodistatofirenze.cultura.gov.it/archividigitali/riproduzione/?id=513466&ua=969) · [Catalogue entry](https://cyphersolver.com/solve/2339.html)

The independent script `replay.py` starts with Brice Dudout’s earlier partial key for c. 76r, recovered from c. 79r. His group had identified the one-digit vowels 6, 8 and 9 and had explicitly deferred applying this key to c. 78r. On line 2, that earlier key alone gives `ilpro·ono·ariocarlo`. Both gaps are the same figure, 45. The neighbouring c. 77r cipher and cleartext support 45 = t in *costui* and 31 = f in *offerendo*. The c. 147r/148r pair supports 02 = u/v in *fussino*. Applying just these three additions, with no language model, dictionary or c. 78r-specific substitution, produces these literal runs. [Earlier key and protocol](https://github.com/dbourdeau/cyphersolver/tree/8d49b5a6de22aa4f62487984ebeba63d0f669dd1/targets/farnese1547)

| Line | Literal run | Reading with spaces |
|---|---|---|
| 2 | `sintendecheilprotonotariocarlo` | s’intende che il protonotario Carlo |
| 3 | `legadifensiua` | lega difensiva |
| 14 | `delparentado` | del parentado |
| 18 | `delalegaperfareinstantiadela` | de la lega, per fare instantia de la |
| 22 | `delcataro` | del cataro |
| 27 | `epartirafraotodi` | e partirà fra oto dì |

Run `python3 targets/farnese1547/independent_check/replay.py` from the workspace or the extracted review packet. It prints both passes for all 27 lines. It uses the transcription’s preferred digits, omits the clear insertions, treats 6/8/9 as singletons and leaves one dot per unmapped group. This deliberately simple test also exposes misspellings and gaps. For marked figures and names, consult the image and diplomatic transcription.

## Where the proposed wording needs review

| Line | What survives inspection | What remains open |
|---|---|---|
| 1–2 | The cited July date includes a visible barred 22. Line 2 is consistent with `51 6 [barred 16] 51 6 03`, or “de 16 del.” | The opening sender and addressee titles lack confirmed values. At the right edge of line 1 the title looks like dotted 92, while the sibling table gives dotted 93 for ambassador. The last marked group looks like 6 followed by a 7- or 5-shaped figure. Grouping the final two figures can fix the alignment without identifying Venice or Niccolò da Ponte. |
| 3 | *Lega difensiva* reads directly. A contemporary account specifically names Switzerland in the proposed league. | *Svizzeri* is a strong contextual expansion of the marked group. A second keyed occurrence would establish its value independently of the politics. |
| 8–9 | The dotted 19 on line 8 is legible. The line 9 gloss is in the clear. | *Ancora* is an inferred expansion of 19. Even the final edition retains competing readings for the abbreviations in the line 9 gloss. |
| 10 | The image supports a compressed marked 68 before 40. The sibling key assigns that marked group to Ferrara. The independently documented itinerary goes through Ferrara. | This is one of Carbon’s stronger corrections. The saved diplomatic input still lacks the second digit, so an amended transcription should identify the correction. |
| 16–17 | Portions of the discussion and reporting instruction are legible, including the conversation the recipient will have. | The saved figures do not reproduce *dal Dominio … et darmene conto … del ritratto di esso* as printed. Around the proposed *di esso*, the strokes look more like `11 70 6 04 8` than the required start `51 70`. The changes need an alignment showing each original figure, proposed replacement and reason. |
| 19 and 25 | *Riens* and the context of promotion to the cardinalate support identification with Reims. Line 25 has a clear dotted 89. | On line 19 the second digit of the title looks like 7. Carbon’s expansion treats it as the same 89 seen on line 25. Leave the title open even though the person is strongly identifiable. |
| 24 | The closing phrase about public benefit and consolation is written in the clear. | The final abbreviated possessive is compatible with the transcriber’s *n[ost]ra*. Carbon’s *mia*, translated as “my own,” is uncertain. |

## Statistical verification

- Running the supplied validator reproduced the full-page language-model scores of **+6.78** against 200 shuffled keys and **+39.20** against 200 shuffled token streams. The result on lines 12–18 also reproduced at **+6.28** against shuffled keys. The validator drops unmapped groups from its scoring string. These results support the order and Italian character of the recovered text. They cannot certify a disputed place name or assign a percentage of correct words.
- On the supplied transcription, the validator’s sibling-only lookup finds an entry for **1,287/1,338 groups (96.2%)**. The report gives 1,295. The extended lookup reproduces **1,313/1,338 (98.1%)**, counting entries such as “[Roma?]” or “[non/mai?]” as mapped. The catalogue’s completion criterion asks how many groups actually give sense in an annotated reading. A count under that criterion has yet to be established. [Catalogue criteria](https://cyphersolver.com/solve/2339.html)
- Dudout did reserve c. 78r lines 12–18. The earlier **0.695** agreement measured a different test, on c. **76r** lines 14–18 against c. 79r. The swarm subsequently examined the c. 78r lines and revised their wording. Their language score gives no blind test of those later revisions.
- A direct rerun of the annealing solver recovered the opening and *lega difensiva* without the sibling substitution table. It gave **+20.90** for its combined score and **+13.44** for language score per character, compared with the reported +23.59 and +9.30. The solver is supplied the proposed tokenization and vowel class. It gives the actual text three restarts and each shuffled stream one. In a separate reconstruction using three restarts on each side, the real text scored **−2.254** per character, ahead of the best of ten shuffled streams at **−3.186**. The recovered words carry more weight than the precise reported deviations.
- All 22 transcribed commas fall on token boundaries under the proposed split. At least one alternative split (also allowing 3 as a singleton) does that too and matches the 28/29 complete chunks on the unmodified input. The words recovered using the independent key discriminate between these possibilities. The claimed 29/29 depends on an editorial change to line 1. The preserved code and outputs also do not document a reproducible run across all 23 Meister JSON keys.

## Documentary checks and credit

Della Casa’s letter of **9 July 1547** describes reports of the French envoy proposing a defensive league involving Venice and the Swiss. His letter of **16 July** gives the intended route through Ferrara and Piacenza to Rome. A letter of **23 July** from Farnese describes the Pope’s recovery from catarrh. On **30 July** Farnese records the promotion of the Archbishop of Reims and adds that Protonotary Carlo has arrived. Together these independently corroborate separate parts of the decipherment. The cipher’s account of a forthcoming visit and pending promotion favors a late-July original, if the news was current when written. The archival copy could be later. The surviving 22 July letter in this edition runs from Farnese to Della Casa. It does not establish the reverse identification supplied in the swarm’s opening. [Comelli, correspondence, letters 333, 335 and 337–341, printed pp. 475–496](https://bitesonline.it/wp-content/uploads/2022/03/Corrispondenza-DellaCasa-Farnese-1546-47_Tomo-II_web.pdf#page=115)

The archive inventory already gives Alessandro and Pier Luigi in parentheses and lists c. 78 without place or date. The shared system across copies from several correspondents supports a Florentine intelligence context. Naming Cosimo’s particular cipher office or reconstructing how his agents obtained this letter would require documentary evidence. The earlier project records unsuccessful key tests on this very sheet and credits Dudout’s partial sibling key. No exact prior plaintext of c. 78r surfaced in this bounded review. The contribution verified here is extending and applying that key to recover this folio. The separate assertions of complete new decipherments on other leaves would require their own comparisons with the surviving cleartexts. [ASFi inventory III, printed p. 103](https://www.regione.toscana.it/documents/10180/320308/Il%20carteggio%20universale%20di%20Cosimo%20I%20De%20Medici,%203/b3e36dec-865f-4ece-8a91-fcca9488f2d7) · [Earlier project record](https://github.com/dbourdeau/cyphersolver/blob/8d49b5a6de22aa4f62487984ebeba63d0f669dd1/targets/farnese1547/NOTES.md)

## Suggested final check

Start with the c. 78r scan, the earlier c. 76r key and the scans of the bilingual neighbours. Independently transcribe lines 1–3, 8–10, 16–17, 19 and 24–25. Save those readings before seeing the normalized solution. Then compare against the diplomatic transcription, the expanded key and Carbon’s edition. For each contested group, give the visible figures, a parallel occurrence if available, the literal reading and any editorial expansion. For a numerical completeness claim, count the tokens in a page-wide alignment and identify which ones give sense without conjectural fills.
