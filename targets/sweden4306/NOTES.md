# Sweden DECODE R4306

Status: read in part — contributed solution, 17 October 2026.

**Belongs to: Riksarkivet key-box and Oxenstierna ciphers.** See the [earlier group survey](../riksarkivet1628/NOTES.md) and its [public page](https://dbourdeau.github.io/cyphersolver/riksarkivet1628.html). R4306 has its own entry because it uses a different key from the other systems in that group.

**Transcribed with CTTS, then solved with Opus 5.5**, as expressly confirmed by George Lasry. Lasry directed the work and supplied the Dutch reading, English translation, contextual notes and working material. Codex prepared this contribution and independently checked the transcription counts, source glyphs and five mechanical lines. The original local research files were not changed.

## Document and scope

Riksarkivet, Stockholm, **Chifferklaver låda II:133**, [DECODE R4306](https://de-crypt.org/decrypt-web/RecordsView/4306). The public metadata checked on 17 October 2026 lists a numerical cipher, status Non-decrypted, three pages and a broad date range 1600–1699; the sender, recipient and languages are blank. Its general collection note lists Oxenstierna correspondence, but does not attribute this particular letter.

This contribution covers **one cipher page**, supplied as `1.png` (the earlier survey labels this view IMG_R4306_I25832_P_hi.jpeg). The earlier survey reports a wrapper numbered II:104 and an Amsterdam address; those other views have not been independently inspected for this submission. The live image manager requires login. Do not treat three record pages as three newly deciphered ciphertext pages.

The cipher page has a pencilled **1632?** at upper left. This annotation is visible but is not an established date of composition. The letter mentions earlier letters of 23 February and 13 March, without a year in the deciphered body. The contributor’s suggested late-March/April setting, diplomatic congress and recipient in Swedish service remain hypotheses. Custody in a Swedish archive alone does not identify the recipient, and the February/March references do not prove composition in those months of the same year.

## Cryptanalysis

No interlinear, marginal, top- or bottom-of-page decipherment appears on the supplied cipher page. The contributed key was recovered from ciphertext, using CTTS transcription and Opus 5.5 analysis, not a historical decipherment or a matched archive key; this is a **ciphertext-only recovery**. The supplied readable text is the result, not an external plaintext source used to obtain the key.

The system is **monoalphabetic substitution with nulls and a small unresolved nomenclator**. There are **461 cipher elements in one document**, 40 distinct cipher types, across 35 CTTS rows. The 463 selections include two date-numeral units (`285`, `d13`) excluded from the cipher count. The 461 comprise **422 alphabetic occurrences, 34 nulls, and five occurrences of four unidentified codes**: 105 once, 106 once, 113 once and 114 twice.

The working alphabet assigns consecutive values **30–52 to 23 letters**, with no letter homophones (one number per vowel/consonant). Only 21 alphabet values occur: 45=q and 51=x are predictions from the ordered sequence, not observed recoveries. The preserved source key’s “24-letter alphabet” header is a counting error; there is no listed j, v or z value. Fifteen null classes occur; the key additionally lists 13 as a null, but it is absent from the current transcription. The four nomenclator values remain unidentified, with personal names, powers or courts suggested by their syntax; no complete nomenclator inventory is claimed.

The labels `285` and `d13` are CTTS identifiers for the date numerals interpreted as 23 (written 2o3) and 13 with a superscript mark. These two are not additional deciphered name codes. Assigned-letter coverage is 422/427 non-null cipher occurrences (98.83%); this is not a measurement of semantic accuracy. Edited words, transcription uncertainty and open codes keep the contribution partial.

## Readings and five-line mechanical check

- [reading.txt](reading.txt): the contributor’s **edited, normalized Dutch** text, preserved verbatim.
- [translation.txt](translation.txt): the contributor’s English translation, preserved verbatim.
- [contributor_context.txt](contributor_context.txt): the supplied translation notes and interpretation; formatting only has been simplified.
- [key.txt](key.txt), [transcription.txt](transcription.txt): current CTTS inputs copied byte for byte, with checksums in `input_checksums.json`.
- [visual_key.png](visual_key.png), [visual_key.html](visual_key.html): current numerical alphabet, actual manuscript glyph samples, nulls, open codes and separate date numerals.
- [mechanical_excerpt.txt](mechanical_excerpt.txt), [mechanical_excerpt.json](mechanical_excerpt.json): **exactly the first five manuscript/CTTS lines**, 73 selections yielding 62 letters. Nulls are omitted; no word division, u/v normalization, spelling correction or gap filling is performed.

The literal excerpt reads:

```text
alleswtdenuw
enuerstaenicsal
mondelingekll
menantwoorden
alsodesaecken
```

The uncertain `ekll` / `men` crossing lines 3–4 is retained literally; the supplied edition has `[gekl…men?]`. Likewise line 5 is `alsodesaecken`, not a mechanical confirmation of every restored letter in “Als o[o]c des saecken”. Elsewhere the source key explicitly notes unresolved written readings such as 39 in line 10 and 38 in line 32. The full edition must not be mistaken for exact key output.

`build.py` reproduces the inventory, chart and those five lines only. `validation.tsv` contains only that excerpt. At 62 letters it is below the repository validator’s 80-letter threshold; no full-text statistical validation or accuracy claim is substituted for this limitation.

## Historical research and prior work

The earlier 21 September `riksarkivet1628` survey records unsuccessful attacks on R4306 in several languages and unsuccessful tests of R4296/R4310. Its 1632/Amsterdam description is cited as earlier research, not silently promoted to a proven attribution. The old survey and profile remain as dated project history; the public page receives a dated link to this contribution.

The current key is a new contributed solution by Opus 5.5, as confirmed by Lasry. An earlier local backup is labelled CTTS cryptanalysis and contains incompatible preliminary letter assignments; it is not the successful key or a historical plaintext source. No exact prompt history, solver settings or chronology beyond the supplied records is claimed.

A limited exact-phrase web search for the opening did not locate a complete earlier edition. This is not an exhaustive prior-publication search. The identities of codes 105/106/113/114, writer, recipient and location remain open. The supplied “U.L.”, “gade gegeven” and diplomatic-setting notes are preserved as contributor commentary, rather than independently verified identifications.

## Remaining gaps
- Codes 105, 106, 113 and 114 — blocker: open-codes; four identities in five occurrences remain unresolved.
- Doubtful words and literal-versus-edited discrepancies — blocker: open-codes; the supplied editorial restorations and least-certain final sentence remain explicitly qualified.
- Year, sender, recipient and place — blocker: open-codes; pencilled 1632? is not a confirmed composition date; Amsterdam is reported by the earlier survey, not independently verified here.

## Escalation
This is publication of the supplied solution at the contributor’s request, not a claim that historical identification or further cryptanalysis is exhausted.
- [x] siblings: the earlier group survey and its separation of unrelated key-box/Bremen/Oxenstierna systems were reviewed; no sibling key supplies this solution.
- [x] clear-pages: the supplied cipher page was inspected; no historical decipherment is visible. Other record images were not available through the public image manager in this check.
- [n/a] known-keys: no new exhaustive key campaign requested for submission; prior R4296/R4310 failures are credited to the earlier survey.
- [x] print: limited exact-opening and record searches found no complete printed plaintext; no priority claim.
- [x] key-rebuild: the supplied Opus 5.5 key was counted and its ordered alphabet verified; no new values are invented for the unresolved codes.
- [x] retry: five complete manuscript lines reapplied literally and compared to the supplied edition; editorial differences retained.

## Sources and credit
- George Lasry, supplied CTTS material, edited Dutch reading, English translation and contextual notes, 17 October 2026. **Transcribed with CTTS, then solved with Opus 5.5.**
- [DECODE R4306](https://de-crypt.org/decrypt-web/RecordsView/4306), Riksarkivet, Chifferklaver låda II:133; public metadata checked 17 October 2026.
- [Earlier group survey](../riksarkivet1628/NOTES.md), 21 September 2026, retained as dated prior work.

DECODE changes are queued locally as **Partially**, with Dutch plaintext and the recovered system described, but are not sent by this PR. No exact date or correspondent correction is proposed.
