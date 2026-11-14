# anover1610: Philip III to the Count of Añover, Lerma, 20 May 1610 (Madrid, Biblioteca Histórica Municipal, I 242,29), a partial key rebuilt from sibling letters

Status: read in part, codes open (Alberto Garvía García, issue #499, 12 Nov 2026; checked here 13 and 14 Nov 2026; written up 14 Nov 2026 by the owner's decision). The ten ciphered lines of f. 53r are read from a key rebuilt from the sibling letters: by the README word rule 77 of 89 words are sure (86.5%), under the 95% bar; key partial. The reading reproduces from the contributor's transcription and key table; the project has not compared it with the manuscript (Memoria de Madrid refuses scripted requests; page 2 was seen once in a browser at the catalogue sweep of 2 Nov 2026, no copy kept), and the open codes are still workable from letters of the series of which no transcription has reached the project (see Remaining gaps).

Catalogue 1988 (Philip III's real cédulas in cipher to Rodrigo Niño Laso, conde de Añover, Consejo de Guerra; four leaves of the series have no decipherment bound in, and I 242,29 is one). Language Spanish. The catalogue's own route was: read the glossed siblings for a key, then apply it to I 242,29 (Hispana idBib 58678726, Memoria de Madrid 424541).

## What was submitted

Issue #499 (alberto-garvia, 12 Nov 2026) carries a summary and figures; the transcription, key and reading are in a Zenodo report, doi 10.5281/zenodo.24174363 (CC BY 4.0, 11 pages, fetched here), and in six zip attachments on the issue that the project could not download (403). The report, prepared with ChatGPT/Codex and without independent palaeographic review, as the contributor states:

- Documents: I 242,29 (the target; 5 pages, cipher on p. 2, f. 53r, "Lerma, 20-V-1610", the reverse carries an archival note on Angola) and, as parallels with the cipher and its contemporary clear text, I 242,33 (Lerma, 19 Jun 1610), I 242,42 (San Lorenzo, 21 Feb 1610), I 242,47 and I 242,48 (both Lerma, 20 May 1610; 47 is Madrid in the catalogue), and I 242,71 (Madrid, 20 Feb 1611) as a separate negative control.
- Method: a mixed nomenclator (homophones for letters, syllables and whole words; groups of unequal length) rebuilt from the sibling decipherments by matching cipher sequences; the siblings' clear texts are existing decipherments, not claimed as a discovery.
- Result: ten ciphered lines of f. 53r, read in part (see `reading.md`): Dutchmen gone to set up a factory at Pinda on the Angolan coast, against the truce; the king charges the count to see it remedied, without sending a person to "the Islands", and to report.

## What was checked here

- The key table of the report (74 values; 66 graded C = matched with a clear text, 3 M, 5 I = contextual only) is in `key.tsv`; the ten transcribed lines in `transcription.txt`.
- An own parser (all segmentations of the digit runs, `decryption.txt`) applied to the table reproduces the contributor's line-by-line reading: 213 tokens, two not in the table as written (the group read gelb = mando, bum = pues). Apart from those two signs the result is ten lines of connected Spanish; a wrong key could not do that, so the values taken from the siblings do carry over.
- A language-model control of my own (Spanish 1490-1650 quadgrams, permuting the digit values) was inconclusive (the real decode -4.39 per letter, the best of 200 permutations -4.20); it is not relied on. The contributor's own control (316 contiguous quadgrams from graded-C fragments at -1.95 against -3.17 for the best of 200 permuted keys) was not re-run.
- Not checked: the transcription against the manuscript (Memoria de Madrid answers curl with an Akamai "Access Denied"; Hispana 429; no browser tool in this session); the sibling plaintexts behind the key values; the zip dossier.
- English translation (PR #547, alberto-garvia, 13 Nov 2026): `translation.md`, line by line on `reading.md`; checked here by script that the 12 bracketed holes stand in the same lines and order, and read line by line against the Spanish. Two small fixes: line 1 no longer translates code 101 twice ('word [101: report?] has been had'), and line 5 keeps the null 58~ in place with its gloss. It claims no complete decipherment. (As of 13 Nov the target was still in progress; it was written up as read in part on 14 Nov, see Write-up.)
- Prior art: the contributor searched Tomokiyo, DECODE, Retortillo Atienza 2019 and the Correia thesis and found no earlier reading; a web search here found none either. Devos 1950 (Les chiffres de Philippe II) was not consulted by anyone. DECODE: not a DECODE record that this project knows of.

## Strict count

Recounted here on 14 Nov 2026 from `reading.md`, word by word, by the README rule (sure words only). The ten lines hold 89 words. Holes, 12:

- 10 that the reading itself brackets: *buena* (U01), *aviso* (101), *trato* (241), *bien* (114), four codes with a value from the context only; *disimulación* (e = mu, from the context); *persona* (fo = so, a revisable transfer: grade M in `key.tsv`, which gives no direct parallel); *puerto*, *entablando*, *capitulado* (a doubtful null 28~ or 58~ inside the word; in *capitulado* also the clu/du question below); *otras* (the sign m = as gives "otraas").
- 2 on a sign the transcriptions do not settle: *mando* (line 6, the sign printed `gel{b?}`, value from control A09) and *porque* (line 5, `bo` in the contributor's transcription and `60` in Brice Dudout's; the contributor confirms `bo` on the images, Dudout marks his own reading doubtful).

77 of 89 words sure = **86.5%**, under the 95% bar: read in part. The contributor's own figures (his, once): 78 of 88 words firm (88.6%), 173 of 211 cipher-group occurrences in firmly readable words (81.99%), 202 of 211 with an equivalence in the table (95.73%). Key: partial (8 of the 74 groups of the table have no sure value: U01, 101, 114, 241, e, fo, 28~, 58~; 9 occurrences).

Statistical check (`python docs/_validate.py anover1610`, `validation.tsv`, 14 Nov 2026): the reading scores -1.948 per letter in the Spanish 4-gram model against -3.627 on average for 200 random keys of the same structure (best -3.001, z 7.7), and -2.176 at best for a key annealed onto the shuffled ciphertext (z 10.4); verdict pass, on 205 tokens and 68 types. The key came from the sibling clear texts, not from this text. The control of 13 Nov (digit values permuted, inconclusive) is superseded by it.

## Remaining gaps

- The transcription of f. 53r against the manuscript (Memoria de Madrid 424541), and of the sibling parallels A01-A14 etc. - blocker: needs-physical-access; the viewer answers scripted requests with an Access Denied page (a bot check, recorded on 13 and 14 Nov 2026, not got round), so it needs a person at a browser or the contributor's images as files. Two independent AI transcriptions of f. 53r agree on every digit string (the contributor's and Brice Dudout's, frozen 3 Nov 2026 by his record); one doubt stands: L05 `bo 32` or `60 32` (por fits the sense only)
- The last sign of line 4, `clu` = tu in the contributor's reading (capi-tu-lado, control B02), written `du` by Brice Dudout, whose `du` is glossed *conde* twice in I 243,18 - blocker: needs-physical-access; one sign or two can only be settled on the images of both letters; asked of both in issue #499, no answer yet
- U01 (buena), 101, 114 and 241 (context-only codes), e = mu, fo = so (persona), the nulls 28~/58~ and the otraas anomaly - blocker: open-codes; tried on 14 Nov 2026 against the glossed letter I 243,18 (MdM 425791, Lerma 30 Apr 1610; section at the end): none of them occurs in it. This gap is workable, not blocked from outside: the further letters of the series (below) may carry these codes with a gloss
- Devos 1950 and any complete nomenclator sheet of the series: not seen by anyone - blocker: no-key-material

## Other leaves of catalogue 1988 (not part of this target)

This folder and its page cover one letter, I 242,29. The catalogue entry 1988 stays open, narrowed, for the three other cipher-only leaves (Hispana idBib 58438217, 58438218, 58678720), of which no transcription has reached the project. Named by Dudout (issue #499, 13 Nov 2026) in the same table family: unglossed I 242,35 (MdM 424529, cipher copy of the King's letter to the Archduke of 19 Jun 1610), I 242,59 (425639) and I 242,60 (425637), both Lerma 10 May 1610; the contributor reports work on 35/59/60 in his dossier that settles no value of I 242,29; which of these are the catalogue's unglossed identifiers is not mapped. I 242,66 is a further glossed parallel, not used (no transcription of it has reached the project). If they are read with this table they join this target (one key, one entry).

## Escalation

- [x] siblings: I 242,33, 42, 47, 48 (and 71 as a control) matched by the contributor; I 243,18 aligned by Brice Dudout; their decipherments were not seen here
- [x] clear-pages: the letter has no decipherment bound in; its reverse carries an archival note about Angola
- [x] known-keys: Tomokiyo's page on Spanish seventeenth-century ciphers and DECODE searched by the contributor: no key for this series
- [x] print: Retortillo Atienza 2019 and the Correia thesis searched by the contributor; Brásio, Monumenta Missionária Africana V p. 587 opened by him (a different letter of 31 May 1610 on Pinda); a web search here found no printed reading. Devos 1950 is identified but no copy was seen by anyone (it treats Philip II's ciphers)
- [x] key-rebuild: the contributor's table (the material of this folder)
- [x] retry: the open codes run against Brice Dudout's alignment of the glossed I 243,18 on 14 Nov 2026: none occurs, no value changed; the unglossed I 242,35, 59 and 60 were not used: no transcription of them has reached the project (the contributor reports work on them in his dossier, not seen here, which settles no value of I 242,29); whether they are the three leaves left in catalogue 1988 is not mapped

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
   progress with no page. (That was the position of 13 Nov; I 243,18 was tried on 14 Nov without result and the
   target was written up as read in part that day, see Write-up.)
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
| `validation.tsv` | the 211 tokens with their values, input of `docs/_validate.py` (14 Nov 2026) |
| `contributor/tokenization_211.txt` | the contributor's 211-token analytical layer (issue #499, 13 Nov 2026) |
| `contributor/controls.tsv` | his sibling control windows A01-D06 and E01-E04 (issue #499, 13 Nov 2026) |
| `contributor/i243_18_dudout_alignment.txt` | Brice Dudout's token-by-gloss alignment of I 243,18 (issue #499, 14 Nov 2026) |


## Documentary and transcription update (13 November 2026)

A subsequent AI-assisted review by Alberto Garvía García is available in the updated Zenodo deposit (version 2, 13 November 2026), including `INFORME_REVISION_20261113.md` and `Cyphersolver_1988_Incidencia_499.md`.

- **Manuscript recheck:** All 211 analytical cipher occurrences in I 242,29 were re-examined against the available manuscript images. No additional secure code values or corrections were established. This review was AI-assisted and does not constitute independent human palaeographic verification.
- **Tokenization:** The difference between the contributor's 211 analytical occurrences and the parser's 213 tokens has been documented. The counts use different segmentation conventions; neither should be treated as an independently verified correction to the other.
- **Historical corroboration:** *Monumenta Missionária Africana*, first series, volume V, p. 587, was inspected directly. It contains a related dispatch dated 31 May 1610 concerning Pinda, rather than a transcription of the ciphered letter dated 20 May 1610. The general historical episode was already documented; the potential contribution of this project lies in recovering the specific instructions and the cipher key.
- **Remaining work:** Devos (1950) has been identified bibliographically but not consulted in full. Independent palaeographic verification, unresolved code groups and the remaining cipher-only letters are still outstanding.

The decipherment remains **read in part / key partial**. The contributor's strict figures are unchanged: 173/211 cipher occurrences in firmly read words (81.99%) and 78/88 editorial words firm (88.64%).

## Issue #499 comments of 14 Nov 2026 (checked 14 Nov 2026, afternoon)

Two new comments after the project's reply of 14 Nov, 01:53 UTC:

1. **Brice Dudout, 09:25 UTC: his alignment of the glossed letter I 243,18** (Memoria de Madrid 425791, Lerma, 30 Apr 1610), 114 token = value pairs on six manuscript lines, made on 3 Nov 2026 by his record, offered for the open codes; saved as `contributor/i243_18_dudout_alignment.txt`. Checked here against `key.tsv`: of the pairs whose token is in the table and whose gloss he read, 71 agree and 1 does not (`mel` glossed once *or* beside *er* in the same line, which looks like a slip of the alignment). 24 tokens of the letter are not in the table for I 242,29 (among them `du` = conde, `gul` = muy, `ja` = sa, `ju` = su, `cli` = ti, `yal` = ga, 99 = assi, 255 = vra). None of the open codes of I 242,29 (U01, 101, 114, 241, e, fo) occurs in it. So the letter supports the table and closes no open code. The alignment was not compared with the image.
   One point to settle: in his own notation the last sign of line 4 of I 242,29 is `du`, the ligature the contributor writes `clu` (= tu, from control B02, giving capi-tu-lado), and in I 243,18 his `du` is glossed *conde* twice. Either the two are different signs in different hands, or the value of the sign in I 242,29 needs a second look. Asked of both in the draft reply.
2. **Alberto Garvía García, 10:58 UTC:** he has checked line 5 again on the manuscript images himself and confirms `fal 242 37 bo 32` (*por*), with Brice Dudout's `60` noted as the alternative; he has reviewed I 243,18 and finds, as above, that it confirms correspondences and resolves none of the open codes; he attaches a publication package and a complement of controls (two zip files: both return 403 to this session, so they were not seen) and asks again for publication as read in part.

Where this leaves the target: the transcription is supported by two independent AI transcriptions that agree on every digit string and by the contributor's own second look at line 5; the open codes have now been tried against the one further glossed letter of the family that was named, without result. What is left is outside the project's reach from here (the images behind the bot check; Devos 1950) or belongs to other leaves of catalogue 1988. The page as read in part is the owner's decision: the reply of 14 Nov said it could be written once I 243,18 gave nothing. The two zip files should come as a pull request or as text, since attachments cannot be fetched here.

## Write-up (14 Nov 2026)

Written up as read in part by the owner's decision, after the reply of 14 Nov that the page could follow once I 243,18 had been tried. What the page has to say plainly, and does:

- No image of the manuscript is shown: Memoria de Madrid refuses scripted requests (a bot check, not got round), and the reuse terms of the images were not checked. The project's only sight of the leaf is page 2 in a browser at the catalogue sweep of 2 Nov 2026 (catalogue 1988, vetting block): no copy was kept, and the opening groups noted then (`5411 5 ba 32 de je 2110 cle 6857101 s 55 fal 2854 je 332110283757`) agree with line 1 of the contributor's transcription, digit for digit, the letter signs written differently. The transcription is the contributor's, supported by Brice Dudout's independent one; the project has not compared it with the image.
- The contributor's zip attachments returned 403 and were not seen: the six of 12 Nov (his dossier, with the full five-page transcription and the 133-entry table) and the two of 14 Nov (publication package, complement of controls). The page rests on his Zenodo report and his issue comments only.
- Open question, put to both: whether Dudout's sign `du` (glossed *conde* in I 243,18) is the sign the contributor reads `clu` = tu at the end of line 4 of I 242,29.
- The checker's test for "read in part" asks that every gap be blocked from outside. Here one gap (the open codes) is workable from letters of the series of which the project has no transcription; the page says so under "What remains uncertain".

