# Worklog, figueroa1534 (catalogue 744)

- 2026-11-11 access: PARES `catalogo/description/3548085` and `catalogo/show/3548085`: connection reset (3 tries, minutes apart); `inicio.html`: HTTP 429. Stopped. No image fetched.
- 2026-11-11 literature search: web search on Figueroa, Genoa, cifra, Simancas: no printed text of the 20 letters; Documenti ispano-genovesi (1868) and Levin found, as in the vetting.
- 2026-11-11 literature search: Tomokiyo's blog (2 Oct 2020) leads to `spanish2A.htm` (Figueroa-Charles V cipher 1529) and `spanish2.htm`; the latter lists 18 of the 20 PARES records under four ciphers with reconstructed keys. Table in `prior_art.tsv`. The vetting of 2 Nov 2026 had missed this.
- 2026-11-11 access: direct download of `spanish2.htm` and the key images: 302 redirect; page read through WebFetch only. Key images not read.
- 2026-11-11 stopped: no ciphertext and no key table in hand; entry corrected in `catalogue.json` (status, vetting.prior_art.tomokiyo, vetting.key_held).
- 2026-11-14 key from source: Tomokiyo/Masiá key completed for study by AGS MPD D/00203 no. 243 (1545); frozen by SHA-256.
- 2026-11-14 transcription: shape atlas from Estense c. 60r/60v (gonzaga1549 sign names), 76 families; 1379,14-18 image 06 transcribed blind (A, B, arbitration by three sub-agents), 492 tokens.
- 2026-11-14 control: one pre-registered measurement against the clear copy of the time: 0.873; within-class shuffles max 0.477; whole-key max 0.449; 4.1 % outside the key. Passed.
- 2026-11-14 reading: 1383,312 and 1383,242 decoded from two blind passes: phrases, about a third of the words; not read.
- 2026-11-14 transcription: 1383,242, 296, 312, 351-353, 364 (20 pages, 12,741 signs): two blind shape passes per page, arbitrated on the image by a third sub-agent; frozen by SHA-256 before decoding.
- 2026-11-14 reading: decode with the frozen key, read by sense with a strict count: 60-75 % of words read per letter (38-54 % sure only); _check_reading.py clean share 0.14-0.38: decoded, not read.
- 2026-11-15 review of PR #621: frozen files of the 0.873 measurement added (validation/, rerun.sh regenerates the recorded output byte for byte); unread passages of the five 1553 readings sized by words (1,419 unread words in 4,821; sure only 37-54 %); content summaries cut back to what is read.
- 2026-11-15 reading: shape sheet 312e answered by Brice Dudout (controls 3/3 shapes, 3/3 dots; PREREG frozen before); blind re-labels of the ɏ and dotted-n classes by seven sub-agents (378 signs, shape only); ARB8e frozen before decoding, K4 unchanged, no measurement; readings redone and recounted: sure only 42-58 % per letter, unread words 1,156 of 4,954; states unchanged (decoded, not read).
