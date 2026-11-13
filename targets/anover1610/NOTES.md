# anover1610: Philip III to the Count of Añover, Lerma, 20 May 1610 (Madrid, Biblioteca Histórica Municipal, I 242,29), a partial key rebuilt from sibling letters

Status: in progress (Alberto Garvía García, issue #499, 12 Nov 2026; checked and filed 13 Nov 2026). A reading of the ten ciphered lines exists in the contributor's report and reproduces from his transcription and key table; the transcription and the sibling parallels could not be checked against the manuscripts, the images being behind a bot block this session, and the gaps below are workable. No page yet.

Catalogue 1988 (Philip III's real cédulas in cipher to Rodrigo Niño Laso, conde de Añover, Consejo de Guerra; four leaves of the series have no decipherment bound in, and I 242,29 is one). Language Spanish. The catalogue's own route was: read the glossed siblings for a key, then apply it to I 242,29 (Hispana idBib 58678726, Memoria de Madrid 424541).

## What was submitted

Issue #499 (alberto-garvia, 12 Nov 2026) carries a summary and figures; the transcription, key and reading are in a Zenodo report, doi 10.5281/zenodo.24174363 (CC BY 4.0, 11 pages, fetched here), and in six zip attachments on the issue that the project could not download (403). The report, prepared with ChatGPT/Codex and without independent palaeographic review, as the contributor states:

- Documents: I 242,29 (the target; 5 pages, cipher on p. 2, f. 53r, "Lerma, 20-V-1610", the reverse carries an archival note on Angola) and, as parallels with the cipher and its contemporary clear text, I 242,33 (Lerma, 19 Jun 1610), I 242,42 (San Lorenzo, 21 Feb 1610), I 242,47 and I 242,48 (both Lerma, 20 May 1610; 47 is Madrid in the catalogue), and I 242,71 (Madrid, 20 Feb 1611) as a separate negative control.
- Method: a mixed nomenclator (homophones for letters, syllables and whole words; groups of unequal length) rebuilt from the sibling decipherments by matching cipher sequences; the siblings' clear texts are existing decipherments, not claimed as a discovery.
- Result: ten ciphered lines of f. 53r, read in part (see `reading.md`): Dutch factories at Pinda on the Angolan coast, against the truce; the king charges the count to see it remedied, without sending a person to "the Islands", and to report.

## What was checked here

- The key table of the report (74 values; 66 graded C = matched with a clear text, 3 M, 5 I = contextual only) is in `key.tsv`; the ten transcribed lines in `transcription.txt`.
- An own parser (all segmentations of the digit runs, `decryption.txt`) applied to the table reproduces the contributor's line-by-line reading: 213 tokens, two not in the table as written (the group read gelb = mando, bum = pues). The result is ten lines of connected Spanish; a wrong key could not do that, so the values taken from the siblings do carry over.
- A language-model control of my own (Spanish 1490-1650 quadgrams, permuting the digit values) was inconclusive (the real decode -4.39 per letter, the best of 200 permutations -4.20); it is not relied on. The contributor's own control (316 contiguous quadgrams from graded-C fragments at -1.95 against -3.17 for the best of 200 permuted keys) was not re-run.
- Not checked: the transcription against the manuscript (Memoria de Madrid answers curl with an Akamai "Access Denied"; Hispana 429; no browser tool in this session); the sibling plaintexts behind the key values; the zip dossier.
- Prior art: the contributor searched Tomokiyo, DECODE, Retortillo Atienza 2019 and the Correia thesis and found no earlier reading; a web search here found none either. Devos 1950 (Les chiffres de Philippe II) was not consulted by anyone. DECODE: not a DECODE record that this project knows of.

## Strict count

The contributor's figures (his, not the README bar): 173 of 211 cipher-group occurrences in firmly readable words (81.99%), 202 of 211 with an equivalence in the table (95.73%), 78 of 88 words firm (88.6%). The word share recorded here is 88.6%: below the 95% bar, so read in part. Key: partial (some values rest on context, grade I, or on a single parallel, grade M; the nulls 28~ and 58~ are doubtful).

## Remaining gaps

- The transcription of f. 53r against the manuscript (Memoria de Madrid 424541), and of the sibling parallels A01-A14 etc. - blocker: needs-physical-access (the viewer refuses scripted requests; a Claude in Chrome pass is needed)
- U01 (buena), 101, 114 and 241 (context-only codes), e = mu, fo = so (persona), the nulls 28~/58~ and the otraas anomaly - blocker: open-codes
- The three other cipher-only leaves of catalogue 1988 and the rest of the series (Hispana idBib 58438217, 58438218, 58678720; I 242,66 as a further parallel) are not transcribed - blocker: not-attempted
- Devos 1950 and any complete nomenclator sheet of the series: not seen by anyone - blocker: no-key-material

## Escalation

- [x] siblings: I 242,33, 42, 47, 48 (and 71 as a control) matched by the contributor; their decipherments were not seen here
- [x] clear-pages: the letter has no decipherment bound in; its reverse carries an archival note about Angola
- [x] known-keys: Tomokiyo's page on Spanish seventeenth-century ciphers and DECODE searched by the contributor: no key for this series
- [ ] print: Devos 1950 not consulted; Retortillo Atienza 2019 consulted by the contributor
- [x] key-rebuild: the contributor's table (the material of this folder)
- [ ] retry: waits for the manuscript images

## Credits

Alberto Garvía García (issue #499; report with AI assistance, ChatGPT/Codex as he states) proposed the key and the reading. The Biblioteca Histórica Municipal de Madrid (Ayuntamiento de Madrid) holds the originals; the images are on Memoria de Madrid.

## Files

| File | Content |
|---|---|
| `transcription.txt` | the ten ciphered lines of f. 53r, as printed in the report |
| `key.tsv` | the key table of the report (74 values) |
| `decryption.txt` | mechanical decode with an own parser |
| `reading.md` | the contributor's line-by-line reading, translation and notes |
| `profile.json` | the target profile |
