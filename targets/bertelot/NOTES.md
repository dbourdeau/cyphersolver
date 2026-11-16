# Unknown → Bertelot (catalogue item73), undated, BnF Français 3822

Status: no write-up of our own (result by George Lasry, presented on docs/bertelot.html)

**24 Oct 2026, DECODE check** (Claude Opus 5.5): George Lasry's permission of 24 Oct 2026 covers his decryptions on DECODE. Searched the full DECODE record list (10,606 records, fetched 24 Oct 2026 with the project cookie) for this shelfmark (Français 3822): no record, so DECODE holds no decryption of it; his full text exists only in his BnF cipher research report files. The excerpt state is kept.

## Source

This result is George Lasry's, obtained with ChatGPT Astra 6 and Anthropic Opus 5.5 and reported in "BnF cipher research" (10 October 2026), which he sent to Daniel Bourdeau on 13 October 2026 for publication here. The transcription, the key and the reading are his. This repository only spot-checked one sample against the Gallica image (below); it did not re-solve the cipher.

## His metadata

- Report status: 2/5 pages transcribed; 1/5 pages deciphered
- Ciphertext-only: No
- Sender: not given
- Recipient: Bertelot (catalogue item73)
- Date: not given
- Key: 121 mapped forms: 35 letter signs and 86 in nomenclature
- Ciphertext: 1,646 elements, 686 identified; 10 further groups with unresolved boundaries
- Contents: The Nemours–Savoy dispute: a refused levy of two thousand men, reconciliation with Savoy, Piedmont, and crossing the mountains.
- Method category (our classification): key recovered based on adjacent plaintext; extent: partial

## His entry, as sent (excerpts and translations)

Quoted from the report; line breaks as extracted from the PDF.

```text
Français 3822
Contents: The Nemours–Savoy dispute: a refused levy of two thousand men, reconciliation with Savoy,
Piedmont, and crossing the mountains.
2/5 pages transcribed; 1/5 pages deciphered
Ciphertext-only: No
Recipient: Bertelot (catalogue item73)
Key: 121 mapped forms: 35 letter signs and 86 in nomenclature
Ciphertext: 1,646 elements, 686 identified; 10 further groups with unresolved boundaries
Interlinear plaintext: Contemporary interlinear plaintext on the same manuscript pages, ff132r–134v.

Excerpt and Translation
Excerpt
f133r, three complete manuscript lines
Il n’y a point de doubte que S.A. ne ce sente griefvement offensé du refus faict de la levée des
deux mil hommes sans congé ce qui n’est maintenant à propos. Regardez de reparer cela vous
excusant…
Translation
There is no doubt that His Highness feels deeply offended by the refusal concerning the levy of the two
thousand men without leave—something that is not appropriate at present. See that you put this right by
excusing yourself…
```

## Links

- No link in the report.

## Images

- `lasry_p088_1.png`: George Lasry's image from the report (credit: George Lasry, BnF cipher research; manuscript © BnF via Gallica).
- Further images in the report, not copied here: p089_2.png.

## Spot-check (13 Oct 2026)

- Batch B. Image checked: none (no Gallica link in dossier; fr. 3822 ark not available offline)
- Folio matches the report: unclear; cipher present: yes
- What we checked: his f133r crop: interlinear "Il ny a point de doute que S.A. ne se sente griefvement offense du refus faict de la levee des deux mil hommes sans conge ce qui nest maintenant a propos" = his excerpt; mixed code/letter cipher not decoded independently
- Verdict: **partly confirmed** (method key recovered based on adjacent plaintext, extent partial). The check is a sample, not a re-solution.
- Notes: 1/5 pages deciphered, 686/1646 identified. Sender not given; recipient Bertelot. Date not given (Nemours-Savoy dispute, c.1580s?).

## Verification 4, 23 Oct 2026

The profile marks this document read, but its texts entry names no file. The reading is George Lasry's ("BnF cipher
research", 10 Oct 2026); the repository holds only his entry with one excerpt and its translation (`lasry_entry.md`), and
NOTES, README and the folder give no fuller text. His decryption is his to publish, so the entry stays an **external
pointer** to his decipherment, with a note saying so; it is not scored or reviewed here.

## George Lasry's report PDF (24 Oct 2026)

Lasry sent his report on this item as a PDF (`lasry/report/35_francais-3822.pdf`), extracted with
`research/reading_audit/lasry_pdf_extract.py` into `lasry/report/` (summary, key image, excerpt and translation, the
full Readable text by folio). The page now shows it at the top. Measured: whole text 1.0 (v10_relabel.measure),
deciphered passages 0.947. His status: 2/5 pages transcribed; 1/5 pages deciphered. Outcome: read in part. He translates the excerpt only
(`lasry/report/translation_excerpt.md`).

## Remaining gaps

- ff132r-134v: 27 unread groups; 960 of 1,646 elements unidentified, 10 groups with unresolved boundaries - blocker: no-key-material; readable text rests on the contemporary interlinear; his key maps 121 forms; his status: 2/5 pages transcribed, 1/5 deciphered.

## Escalation

- [x] siblings: the volume belongs to Lasry's BnF survey; no sibling key on DECODE known (24 Oct 2026)
- [x] clear-pages: the plaintext beside the cipher is the one he used (see his summary); no further decipherment known
- [x] known-keys: Lasry's reconstructed key is the only key; shown on the page
- [x] print: no edition of the deciphered passages known to this project (24 Oct 2026)
- [n/a] key-rebuild: the key reconstruction is George Lasry's, not this project's work
- [x] retry: his full Readable text (24 Oct 2026) read and measured; holes left as he marks them

## 14 Nov 2026: decryption listed in outcome.texts

The full-texts check (`docs/_texts.py`) reported "no decryption file" for George Lasry's entry: his Readable text by folio
(`lasry/report/readable.md`, extracted unedited from his report PDF of 24 Oct 2026; see `lasry/report/ATTRIBUTION.md`) was listed
only as the reading. It is now also listed as the entry's decryption. No text was changed and nothing was re-deciphered here.
His report status: 2/5 pages transcribed; 1/5 pages deciphered. Still open: the transcription of the cipher itself, which is not in the
PDF or in this folder; it has been requested from George Lasry (`research/reading_audit/TRANSCRIPTIONS_WANTED.md`).
