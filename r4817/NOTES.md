# SCH R 201: the cipher flyleaf (DECODE R4817)

Status: solved; read with one explicitly marked textual emendation.
Work: 22–23 September 2026. Catalogue item 271, formerly class C.

## Result

The five lines are a German alchemical note, not an identifiable letter between correspondents:

> PRIMA MATERIA IST / DIE GALLE UOM WIDDER / DAS GEFAE IST EINE / HALB RUNDE KUGEL DER / OFFEN IST DIE WAGE

U/V share a sign. Modern word forms with the conjectural correction marked: “Prima materia ist die Galle vom Widder. Das Gefä[ß] ist eine halbrunde Kugel. Der Ofen ist die Waage.” English: “The prime matter is the gall of the ram. The vessel [emended] is a half-round sphere. The furnace is the balance [or Libra].” Whether these words designate literal materials or alchemical/zodiacal correspondences is not established.

All 79 graphic signs in 19 classes are assigned. 78/79 (98.73%) read without correcting the underlying text. The last sign of GEFAE is visibly the same E as elsewhere. The intended word is probably GEFAS / Gefäß, but the manuscript does not encode that final S. Do not silently repair it or call this 100% verified plaintext. The key covers all attested signs; no external key or independent plaintext validates it.

## Source and dating

- Zentralbibliothek Zürich, **SCH R 201**, *Speculum sophicum rhodo-stauroticum*, catalogued 1618, attributed to Daniel Mögling (1596–1635), writing as Theophilus Schweighardt. https://doi.org/10.7891/e-manuscripta-23267 .
- Cipher surface: https://www.e-manuscripta.ch/zuzneb/content/pageview/1033442 ; IIIF canvas [2], before the title page, apparently the inside front board/pastedown. Korn calls it the first blank page. The cipher has no signature, addressee, date or salutation. Do not infer that Mögling wrote it, or that it was added in 1618 merely because the volume is dated 1618.
- Manifest: https://www.e-manuscripta.ch/i3f/v20/1033440/manifest . Full-resolution source is 3409 × 4031 pixels: https://www.e-manuscripta.ch/i3f/v20/1033442/full/full/0/default.jpg . Public Domain Mark on the library record. Images were publicly retrievable without a DECODE login.
- DECODE https://de-crypt.org/decrypt-web/RecordsView/4817 was retrieved by requests after the web tool failed. It says Non-decrypted, Unknown cipher type, one cipher page, graphic signs. Its claim that no decipherment is known misses the partial result below. It provides four images and a PDF; this investigation used the library's original.
- All 42 library canvases were inspected in contact sheets for other cipher passages or a key. No second specimen or key table in the same signs was identified. This was a visual survey, not a full transcription of the book's German text.

## Prior art and contamination

**Anne-Simone Rous** identified monoalphabetic substitution and supplied a partial decipherment, published in **Uwe Maximilian Korn**, “‘Bilderfahrzeug’ of the Rosicrucians. Daniel Mögling’s *Speculum Sophicum Rhodostauroticum* (1618) in Print and Manuscript,” *Between Manuscript and Print* (2023), pp. 159–186, **p. 178, note 41 and fig. 11**, https://doi.org/10.1515/9783111242699-007 . Open chapter: https://uplopen.com/chapters/6386/files/74c45564-9e3b-4a01-a052-d2cff864b24d.pdf .

That result was found **before the attack** and used as a crib. It contains the difficult opening FRIDA DATERIA, takes VOM as UND, leaves crosses unassigned, and misreads the final N of OFFEN. Our contribution is a checked transcription, distinctions between lookalike signs, a completed working key, coherent word division, and an explicit account of the GEFAE anomaly. This is not a claim to the first recognition or first partial solution.

Targeted searches of Tomokiyo/cryptiana for Speculum, Rosicrucian, Mögling and Schweighardt found no relevant result. Web access to the unsolved page itself failed. Searches for the title, shelfmark, cipher and Rous led to Korn; exact-phrase searches for “Galle vom Widder,” “halb runde Kugel” and “Ofen ist die Waage” found no independent parallel. Negative searches establish only what was not located, not that no earlier complete solution exists.

## Method and corrections

1. Read Rous's published attempt; retrieve the original image rather than use the chapter's small figure.
2. Anchor recurring IST, DIE, DER and EINE. Keep sign identities independent of letter values in `transcription.txt` and describe all 19 forms in `key.json`.
3. Three nested angles are M (PRIMA, MATERIA, VOM); two are N (EINE, RUNDE, OFFEN). The closed semicircle is D. Rous's opening D cannot be retained when this difference is observed.
4. The first sign has two curls and reads P; B in HALB has only a lower curl. The cross is F, appearing once in GEFAE and twice in OFFEN. This gives PRIMA MATERIA and a furnace rather than forcing the first sign to be F.
5. Above the horizontal line, a solid dot gives I and an open ring gives O. Thus the three signs after GALLE are U/V-O-M, not U-N-D. VOM makes the first statement “the gall of the ram.” The same triangular sign is U in RUNDE and KUGEL.
6. Audit all five lines on the 3409-pixel original. Keep R and L separate despite variable arms; K, H and B are singletons constrained by KUGEL and HALB. The damaged-looking E in the final DIE retains the open-bowl shape; its word is also repeated intact in line 2.
7. Reapply the key mechanically: `python r4817/decode.py` produces `literal.txt`, `token_ledger.json`, `verification.json`. Counts: 15 + 17 + 15 + 17 + 15 = 79 signs; measured with `python docs/_check_profile.py --measure r4817/transcription.txt` (19 distinct, IC 0.0727).

The two crosses in OFFEN are adjacent F signs, not an FF code. Raw output UOM retains the shared U/V value. No nulls, homophones, nomenclator or transposition is required. Alphabet letters outside the 19 attested signs are unknown.

## Remaining gaps

- **GEFAE, line 3 sign 8:** E is the reproducible key output; S/ß is the likely intended character, grade M. This is a textual discrepancy, not an unassigned cipher sign. No second copy or original key was found to prove the intended spelling. A copying/enciphering error remains conjectural.
- Writer, precise date, purpose and hermetic interpretation are unknown. These are not missing ciphertext tokens. Libra is only an alternative translation of Wage, not an identification of a substance or apparatus.

## Escalation

- [x] siblings: surveyed every canvas of the volume; no other cipher in this script identified.
- [x] clear-pages: neighbouring and remaining pages inspected in contact sheets; no parallel decipherment located.
- [n/a] known-keys: no cipher series identified or external key located; occurring values reconstructed internally.
- [x] print: Korn 2023 supplies prior partial work; title, shelfmark and Tomokiyo searches above; no independent complete reading found.
- [x] key-rebuild: separated M/N/D, P/B/F and O/I; obtained VOM and OFFEN; every sign assigned.
- [x] retry: replayed all five lines and rechecked GEFAE on the source; it remains E, so the emendation is marked.

## Files and reproduction

`transcription.txt`: five lines of sign IDs; punctuation excluded.
`key.json`: mappings and shape descriptions; I grades mean context-derived, not archival attestation.
`decode.py`: deterministic decoder and coverage ledger; no correction of GEFAE.
`READING.md`: literal, conservative and normalized readings, translation and qualifications.
`token_ledger.json`, `verification.json`: measured values and anomalous position (3,8), 78 I and 1 M.
`profile.json`: chronology, prior-work contamination and outcome.
`get_pages.py`: manifest-driven image/contact-sheet retrieval; full page scans are not committed.
`source-entry.json`: catalogue metadata preserved before removal of item 271.

Site crop and labelled key samples derive from the library image with attribution. The DECODE package is queued locally, not submitted to the database.
