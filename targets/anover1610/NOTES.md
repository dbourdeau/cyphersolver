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
- English translation (PR #547, alberto-garvia, 13 Nov 2026): `translation.md`, line by line on `reading.md`; checked here by script that the 12 bracketed holes stand in the same lines and order, and read line by line against the Spanish. Two small fixes: line 1 no longer translates code 101 twice ('word [101: report?] has been had'), and line 5 keeps the null 58~ in place with its gloss. It claims no complete decipherment. The target stays in progress (sibling leaves untranscribed).
- Prior art: the contributor searched Tomokiyo, DECODE, Retortillo Atienza 2019 and the Correia thesis and found no earlier reading; a web search here found none either. Devos 1950 (Les chiffres de Philippe II) was not consulted by anyone. DECODE: not a DECODE record that this project knows of.

## Strict count

The contributor's figures (his, not the README bar): 173 of 211 cipher-group occurrences in firmly readable words (81.99%), 202 of 211 with an equivalence in the table (95.73%), 78 of 88 words firm (88.6%). The word share recorded here is 88.6%: below the 95% bar, so read in part. Key: partial (some values rest on context, grade I, or on a single parallel, grade M; the nulls 28~ and 58~ are doubtful).

## Remaining gaps

- The transcription of f. 53r against the manuscript (Memoria de Madrid 424541), and of the sibling parallels A01-A14 etc. - blocker: needs-physical-access (the viewer refuses scripted requests, 403 again on 14 Nov 2026; a Claude in Chrome pass is needed). Two independent AI transcriptions of f. 53r now agree on every digit string (the contributor's and Brice Dudout's, frozen 3 Nov 2026 by his record); one doubt stands: L05 `bo 32` or `60 32` (por fits the sense only)
- U01 (buena), 101, 114 and 241 (context-only codes), e = mu, fo = so (persona), the nulls 28~/58~ and the otraas anomaly - blocker: open-codes
- The three other cipher-only leaves of catalogue 1988 and the rest of the series (Hispana idBib 58438217, 58438218, 58678720; I 242,66 as a further parallel) are not transcribed - blocker: not-attempted. Named by Dudout (issue #499, 13 Nov 2026) in the same table family: unglossed I 242,35 (MdM 424529, cipher copy of the King's letter to the Archduke of 19 Jun 1610), I 242,59 (425639) and I 242,60 (425637), both Lerma 10 May 1610; the contributor reports work on 35/59/60 in his dossier that settles no target value; which of these are the catalogue's unglossed identifiers is not mapped
- I 243,18 (MdM 425791, Lerma 30 Apr 1610), a glossed letter of the same table family named by Dudout, is not among the contributor's controls; it may give 101, 114, 241, e or fo - blocker: not-attempted
- Devos 1950 and any complete nomenclator sheet of the series: not seen by anyone - blocker: no-key-material

## Escalation

- [x] siblings: I 242,33, 42, 47, 48 (and 71 as a control) matched by the contributor; their decipherments were not seen here
- [x] clear-pages: the letter has no decipherment bound in; its reverse carries an archival note about Angola
- [x] known-keys: Tomokiyo's page on Spanish seventeenth-century ciphers and DECODE searched by the contributor: no key for this series
- [ ] print: Devos 1950 not consulted; Retortillo Atienza 2019 consulted by the contributor
- [x] key-rebuild: the contributor's table (the material of this folder)
- [ ] retry: waits for the manuscript images

## Issue #499 comments of 13 Nov 2026 (checked 14 Nov 2026)

Three new comments after the project's reply of 13 Nov:

1. **Alberto Garvía García, 18:32 UTC: transcription, tokenization, full key with evidence, controls.** The ten-line
   diplomatic transcription equals `transcription.txt`. His analytical tokenization (211 occurrences) is now in
   `contributor/tokenization_211.txt` and his control windows A01-D06 and four new ones E01-E04 (I 242,48: G48_trata,
   gul = muy) in `contributor/controls.tsv`. Checked here: every one of the 211 tokens has a value in `key.tsv`, and
   decoding them gives his ten-line reading letter for letter (codes U01, 101, 114, 241, e and the nulls marked as he
   marks them). The 74-entry table with grades and references equals `key.tsv` (66 C, 3 M, 5 I). The controls are his
   consistency checks of a key built from them (27 of 34 earlier windows agree, 4 of 4 new), not blind tests; the
   sibling images were not seen here. His figures are unchanged (78/88 words firm, 88.6%); no open code is closed.
   He identifies Devos 1950 (Commission royale d'histoire, in-4 series no. 52) without a copy, and checks MMA V p. 587
   (Brásio 1955, doc. 222, 31 May 1610, AGS Secretarias Provinciales livro 1503 f. 10v): a different letter on the
   Pinda episode, not this decipherment. Santana Pérez 2015 p. 910 n. 46 cites AGS Estado leg. 436 (20 Apr 1610),
   not checked.
2. **Alberto Garvía García, 22:23 UTC:** asks to publish the result as a partial decipherment now. Answer for the
   owner: the README rule lets "read in part" stand only when every unread piece has an outside blocker; here the open
   codes can still be tried against I 243,18 (glossed, unused) and the unglossed siblings, so the target stays in
   progress with no page.
3. **Brice Dudout, 23:42 UTC: an independent transcription.** His own shape transcription of I 242,29 (3 Nov 2026,
   SHA-256 fda879da..., unpublished; order by his record) agrees with the contributor's on every digit string of
   L01-L10, including the cross on 26 and `72 m` in L03; letter-sign differences are notation (`de`/`du` = `cle`/`clu`,
   `jo` = `fo`, `bup` = `bum`). One real difference: L05 `fal 242 37 bo 32` against his `60 32` (a hooked ascender
   like the 6 of L07); he marks it doubtful, `por` supporting `bo` by sense only. Date clause "de Lerma a 20 de Mayo
   de 1610" confirmed. He names further letters of the family (I 243,18 glossed; I 242,35, 59, 60 unglossed; I 242,39
   another table) and reports that his preregistered test of a family table on held-out I 242,42 failed his bar (0.640
   against 0.252, bar 0.85); I 242,42 is a control here, so it cannot be a blind test any more.

## Credits

Alberto Garvía García (issue #499; report with AI assistance, ChatGPT/Codex as he states) proposed the key and the reading. Brice Dudout (issue #499, 13 Nov 2026; AI agents) sent an independent transcription comparison of f. 53r and pointed to further letters of the family. The Biblioteca Histórica Municipal de Madrid (Ayuntamiento de Madrid) holds the originals; the images are on Memoria de Madrid.

## Files

| File | Content |
|---|---|
| `transcription.txt` | the ten ciphered lines of f. 53r, as printed in the report |
| `key.tsv` | the key table of the report (74 values) |
| `decryption.txt` | mechanical decode with an own parser |
| `reading.md` | the contributor's line-by-line reading, translation and notes |
| `translation.md` | the contributor's line-by-line English translation of `reading.md`, holes kept (PR #547) |
| `profile.json` | the target profile |
| `contributor/tokenization_211.txt` | the contributor's 211-token analytical layer (issue #499, 13 Nov 2026) |
| `contributor/controls.tsv` | his sibling control windows A01-D06 and E01-E04 (issue #499, 13 Nov 2026) |


## Documentary and transcription update (13 November 2026)

A subsequent AI-assisted review by Alberto Garvía García is available in the updated Zenodo deposit (version 2, 13 November 2026), including `INFORME_REVISION_20261113.md` and `Cyphersolver_1988_Incidencia_499.md`.

- **Manuscript recheck:** All 211 analytical cipher occurrences in I 242,29 were re-examined against the available manuscript images. No additional secure code values or corrections were established. This review was AI-assisted and does not constitute independent human palaeographic verification.
- **Tokenization:** The difference between the contributor's 211 analytical occurrences and the parser's 213 tokens has been documented. The counts use different segmentation conventions; neither should be treated as an independently verified correction to the other.
- **Historical corroboration:** *Monumenta Missionária Africana*, first series, volume V, p. 587, was inspected directly. It contains a related dispatch dated 31 May 1610 concerning Pinda, rather than a transcription of the ciphered letter dated 20 May 1610. The general historical episode was already documented; the potential contribution of this project lies in recovering the specific instructions and the cipher key.
- **Remaining work:** Devos (1950) has been identified bibliographically but not consulted in full. Independent palaeographic verification, unresolved code groups and the remaining cipher-only letters are still outstanding.

The decipherment remains **read in part / key partial**. The contributor's strict figures are unchanged: 173/211 cipher occurrences in firmly read words (81.99%) and 78/88 editorial words firm (88.64%).
