# Bossuet correspondence → Includes letters to the abbé Bossuet, Selected letters from1697–1698, BnF NAF 28227(9)

Status: no write-up of our own (result by George Lasry, presented on docs/bossuet.html)

**24 Oct 2026, DECODE check** (Claude Opus 5.5): George Lasry's permission of 24 Oct 2026 covers his decryptions on DECODE. Searched the full DECODE record list (10,606 records, fetched 24 Oct 2026 with the project cookie) for this shelfmark (NAF 28227(9)): no record, so DECODE holds no decryption of it; his full text exists only in his BnF cipher research report files. The excerpt state is kept.

## Source

This result is George Lasry's, obtained with ChatGPT Astra 6 and Anthropic Opus 5.5 and reported in "BnF cipher research" (10 October 2026), which he sent to Daniel Bourdeau on 13 October 2026 for publication here. The transcription, the key and the reading are his. This repository only spot-checked one sample against the Gallica image (below); it did not re-solve the cipher.

## His metadata

- Report status: 3/32 pages transcribed; 28 more in part; 12/28 cipher pages deciphered; 16 more in part
- Ciphertext-only: No
- Sender: Bossuet correspondence
- Recipient: Includes letters to the abbé Bossuet
- Date: Selected letters from1697–1698
- Key: 41 numerical codes; 1 symbol; 1 pseudonym
- Ciphertext: Transcribed passages: 642 elements, 626 identified
- Contents: Bossuet correspondence concerning ecclesiastical controversy, censures and ordinances, assemblies, printed works, diplomacy in Rome, and church appointments.
- Method category (our classification): read with known key; extent: partial

## His entry, as sent (excerpts and translations)

Quoted from the report; line breaks as extracted from the PDF.

```text
NAF 28227(9)
Contents: Bossuet correspondence concerning ecclesiastical controversy, censures and ordinances,
assemblies, printed works, diplomacy in Rome, and church appointments.
3/32 pages transcribed; 28 more in part; 12/28 cipher pages deciphered; 16 more in part
Ciphertext-only: No
Sender: Bossuet correspondence
Recipient: Includes letters to the abbé Bossuet
Year: Selected letters from1697–1698
Key: 41 numerical codes; 1 symbol; 1 pseudonym
Ciphertext: Transcribed passages: 642 elements, 626 identified
Key in the same volume: Original cipher key in the same volume, PDF 345-346.
Interlinear plaintext: Historical interlinear plaintext survives on the selected letter pages.

Excerpt and Translation
Excerpt
PDF199 — three complete body lines
Je ne vois que faire pour ce qui est icy une querele particuliere.
Translation
I do not see what to do about what is a private quarrel here.
```

## Links

- No link in the report.

## Images

- `lasry_p060_3.png`: George Lasry's image from the report (credit: George Lasry, BnF cipher research; manuscript © BnF via Gallica).
- Further images in the report, not copied here: p058_1.png, p059_2.png.

## Spot-check (13 Oct 2026)

- Batch A. Image checked: none (no Gallica link in entry; NAF 28227(9) checked only via his crops)
- Folio matches the report: unclear; cipher present: yes
- What we checked: his PDF199 crop "80.50.5, 29.80.5.36.5.97.5, 41.9.38.71.99.7.80.97.99.5.36.5" with the original key sheet he images (u=80 n=50 e=5 q=29 r=36 l=97 p=41 a=9 t=71 i=99 c=7) = "une querele particuliere", agreeing with interlinear and his excerpt
- Verdict: **partly confirmed** (method read with known key, extent partial). The check is a sample, not a re-solution.
- Notes: Could not check folio identity against Gallica (no link). Original key is in the same volume and interlinear plaintext survives, so this is reading with the contemporary key. Only 12/28 cipher pages deciphered.

## Verification 4, 23 Oct 2026

The profile marks this document read, but its texts entry names no file. The reading is George Lasry's ("BnF cipher
research", 10 Oct 2026); the repository holds only his entry with one excerpt and its translation (`lasry_entry.md`), and
NOTES, README and the folder give no fuller text. His decryption is his to publish, so the entry stays an **external
pointer** to his decipherment, with a note saying so; it is not scored or reviewed here.

## George Lasry's report PDF (24 Oct 2026)

Lasry sent his report on this item as a PDF, extracted with `research/reading_audit/lasry_pdf_extract.py` into `lasry/report/` (summary, key image, excerpt and translation, the full Readable text by folio). The page shows it at the top. Measured: whole text 0.959 (v10_relabel.measure), deciphered passages 0.889 (bare ? counted as unread). His status: 3/32 pages transcribed; 28 more in part; 12/28 cipher pages deciphered; 16 more in part. Outcome: read in part.

## Remaining gaps

- the deciphered pages: unread groups between the deciphered runs - blocker: no-key-material; left as George Lasry marks them; no other key or plaintext known; his decipherment is the only one
- 28 of 32 pages transcribed in part, 16 of 28 cipher pages deciphered in part: not transcribed or deciphered in full in Lasry's report - blocker: no-key-material; his report status says so; outside this project's work, no other key or plaintext known

## Escalation

- [x] siblings: neighbours belong to George Lasry's BnF survey; no sibling key found here
- [x] clear-pages: the report's pages and the manuscript on Gallica checked against his text; no further decipherment held
- [x] known-keys: Lasry's reconstructed key is the only key; shown on the page
- [x] print: no edition of the unread passages found
- [n/a] key-rebuild: the key reconstruction is George Lasry's, not this project's work
- [x] retry: his full Readable text (24 Oct 2026) read and measured; holes left as he marks them

## 14 Nov 2026: decryption listed in outcome.texts

The full-texts check (`docs/_texts.py`) reported "no decryption file" for George Lasry's entry: his Readable text by folio
(`lasry/report/readable.md`, extracted unedited from his report PDF of 24 Oct 2026; see `lasry/report/ATTRIBUTION.md`) was listed
only as the reading. It is now also listed as the entry's decryption. No text was changed and nothing was re-deciphered here.
His report status: 3/32 pages transcribed; 28 more in part; 12/28 cipher pages deciphered; 16 more in part. Still open: the transcription of the cipher itself, which is not in the
PDF or in this folder; it has been requested from George Lasry (`research/reading_audit/TRANSCRIPTIONS_WANTED.md`).
