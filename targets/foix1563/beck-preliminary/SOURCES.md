# Sources, attribution and access limits

## [S1] Manuscript witness
British Library, Additional MS 4136, ff.148v-149; DECODE R9241. The supplied photographs reproduce four numbered cipher extracts copied under a heading identifying the Queen Mother, de Foix in England and 15 January 1563. Scope and attribution follow the heading and Daniel Bourdeau's earlier identification. This report does not silently convert the copied year or establish the identity of speakers within quoted material.

Record: https://de-crypt.org/decrypt-web/RecordsView/9241

Photographs supplied for the research by Daniel Bourdeau: `IMG_R9241_I43237_P1.jpg`, `IMG_R9241_I43237_P2.jpg`, both 3205 x 4149. Their SHA-256 hashes are in `data/provenance.json`. The public files contain no photographs or crops. Rights to redistribute the images have not been established by this project.

## [S2] Bourdeau's prior source work
https://github.com/dbourdeau/cyphersolver/tree/main/targets/foix1563

`NOTES.md` inspected through the connected repository on 3 October 2026, blob `3f4c8db8670fdae7d3d66f022d65922e5782e962`. This catalogue target includes separately solved Coligny material; this contribution concerns only R9241, not R9238 or its decipherment.

Earlier first/second transcriptions: `qm_tokens.txt`, `qm2_f148.txt`, `qm2_f149.txt`. Recorded blob for qm2_f149.txt: `f4d3c19de43db7aecd6c4a7b14b2b2e4e095e3c4`. They supplied independent prior graphical distinctions, not independent confirmation of our plaintext. Photographs decide source disputes; neither transcription is authoritative.

## [S3] Lawrence Beck / ChatGPT research checkpoints
The preparation uses the supplied `Catherine_1563_Research_Update_v09_Evidence.zip` (audit v0.9 / source-key v13). Its original verifier was executed during preparation and returned PASS (32 checks). V0.8 and v0.9 did not add accepted plaintext to the v0.7 reading. The source and key copied into this package are byte-identical to v13. Recorded methodological details are in the v0.6-v0.9 research notes, including source-driven word-code proposals and failed computational rankings.

This review release is a consolidation, not a new cryptanalytic break. The matching-historical-key and exact-counterpart searches have not succeeded. The source audit was informed by emerging French and was not a blind or independent expert review. The new compact decoder is a replay tool, not the original discovery solver.

## [S4] Unresolved documentary leads
Satoshi Tomokiyo, *French ciphers during the Reigns of Charles IX and Henry III*. Text snapshot inspected in the prior research; the 1565 graphical table and underlying leaves were not obtained:
https://github.com/dbourdeau/cyphersolver/blob/main/research/gallica_sweep/src/henryiii.txt
Original: http://cryptiana.web.fc2.com/code/henryiii.htm
Recorded candidate: de Foix's letters of 11 October 1565 to Charles IX and Catherine, BnF Francais 15971, ff.21 and 26. Same correspondence network is not proof of key reuse.

David Potter, *The Correspondence of Paul de Foix, Ambassador in England, 1562-1566*, Camden Fifth Series 58 (2019), DOI 10.1017/S0960116319000289. Notes 204-205 and an author-upload landing page were found, but the associated full letter was not acquired or aligned. The author listing is not an established counterpart or proof of an earlier decipherment.
https://doi.org/10.1017/S0960116319000289
https://www.academia.edu/143900518/Correspondence_of_Paul_de_Foix_French_Ambassador_at_the_Court_of_Elizabeth_I_1562_1565_

Other cipher tables and historical studies were methodological comparisons, not sources of transferred values. The audit record distinguishes descriptions from images actually inspected. No broader comparative claim is required for the findings presented here.

## Credit and integration
Lawrence Beck initiated and directed the project. ChatGPT performed the computational work, source comparison, candidate development, translations and drafting described in the supplied research notes. Daniel Bourdeau supplied the photographs, earlier transcriptions and prior source identification/research. No external reviewer is represented as having approved this Catherine result.

The contribution is additive under `targets/foix1563/beck-preliminary/`. It makes no change to the parent profile, catalogue metrics, solved status, site templates or other contributors' findings. Daniel can decide how a reviewed partial result should be linked from the site. It is not a journal submission or a request to halt further decipherment.
