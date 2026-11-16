# Not established → Duke of Bouillon, 6–8 August 1650, Madrid, BnF Clairambault 460 — graphic cipher, pp53–55

Status: no write-up of our own (result by George Lasry, presented on docs/bouillon1650.html)

**24 Oct 2026, DECODE check** (Claude Opus 5.5): George Lasry's permission of 24 Oct 2026 covers his decryptions on DECODE. Searched the full DECODE record list (10,606 records, fetched 24 Oct 2026 with the project cookie) for this shelfmark (Clairambault 460 — graphic cipher, pp53–55): no record, so DECODE holds no decryption of it; his full text exists only in his BnF cipher research report files. The excerpt state is kept.

## Source

This result is George Lasry's, obtained with ChatGPT Astra 6 and Anthropic Opus 5.5 and reported in "BnF cipher research" (10 October 2026), which he sent to Daniel Bourdeau on 13 October 2026 for publication here. The transcription, the key and the reading are his. This repository only spot-checked one sample against the Gallica image (below); it did not re-solve the cipher.

## His metadata

- Report status: 3/3 pages transcribed; 3/3 pages deciphered
- Ciphertext-only: No
- Sender: Not established
- Recipient: Duke of Bouillon
- Date: 6–8 August 1650, Madrid
- Key: 54 symbols, 50 letter signs, 4 unidentified
- Ciphertext: 949 elements, 941 identified (99.2%)
- Contents: Spanish financial and military support for Bouillon: promised payments, eight armed frigates, and an advance toward Paris.
- Method category (our classification): key recovered based on adjacent plaintext; extent: complete

## His entry, as sent (excerpts and translations)

Quoted from the report; line breaks as extracted from the PDF.

```text
Clairambault 460 — graphic cipher, pp53–55
Contents: Spanish financial and military support for Bouillon: promised payments, eight armed frigates, and
an advance toward Paris.
3/3 pages transcribed; 3/3 pages deciphered
Ciphertext-only: No
Sender: Not established
Recipient: Duke of Bouillon
Year: 6–8 August 1650, Madrid
Key: 54 symbols, 50 letter signs, 4 unidentified
Ciphertext: 949 elements, 941 identified (99.2%)
Interlinear plaintext: Interlinear plaintext on pp53–55. ·
Excerpt and Translation
Excerpt
p55 — postscript
un courrier à Mr de Condé? Don Louis lui escrit et à Fonsaldagne pour les haster d'antr[er] en
France et marcher droit à Paris.
Translation
a courier to Mr de Condé? Don Louis writes to him and to Fonsaldagne to urge them to enter France
and march straight to Paris.
```

## Links

- No link in the report.

## Images

- `lasry_p069_1.png`: George Lasry's image from the report (credit: George Lasry, BnF cipher research; manuscript © BnF via Gallica).
- Further images in the report, not copied here: p069_2.png.

## Spot-check (13 Oct 2026)

- Batch A. Image checked: none (no Gallica link in entry; Clairambault 460 pp53-55 checked only via his p55 crop)
- Folio matches the report: unclear; cipher present: yes
- What we checked: p55 crop last cipher line "x h e [i] 13 | 3 | [box] 3 h m 8" with his system-A table (x=d, h=r, e=o, 13=t, 3=a, box=p, m=i, 8=s) = "droit a paris", matching interlinear "marcher droit a paris" and his excerpt
- Verdict: **partly confirmed** (method key recovered based on adjacent plaintext, extent complete). The check is a sample, not a re-solution.
- Notes: Folio identity not checked on Gallica. Interlinear plaintext throughout pp53-55; reading largely restates it. Same volume as clair460alpha.

## Verification 4, 23 Oct 2026

The profile marks this document read, but its texts entry names no file. The reading is George Lasry's ("BnF cipher
research", 10 Oct 2026); the repository holds only his entry with one excerpt and its translation (`lasry_entry.md`), and
NOTES, README and the folder give no fuller text. His decryption is his to publish, so the entry stays an **external
pointer** to his decipherment, with a note saying so; it is not scored or reviewed here.

## George Lasry's report PDF (24 Oct 2026)

Lasry sent his report on this item as a PDF (`lasry/report/25_clairambault-460-graphic-cipher-pp5355.pdf`), extracted with
`research/reading_audit/lasry_pdf_extract.py` into `lasry/report/` (summary, key image, excerpt and translation, the
full Readable text by folio). The page now shows it at the top. Measured: whole text 0.969 (v10_relabel.measure),
deciphered passages 0.955. His status: 3/3 pages transcribed; 3/3 pages deciphered. Outcome: read. He translates the excerpt only
(`lasry/report/translation_excerpt.md`).

## 14 Nov 2026: decryption listed in outcome.texts

The full-texts check (`docs/_texts.py`) reported "no decryption file" for George Lasry's entry: his Readable text by folio
(`lasry/report/readable.md`, extracted unedited from his report PDF of 24 Oct 2026; see `lasry/report/ATTRIBUTION.md`) was listed
only as the reading. It is now also listed as the entry's decryption. No text was changed and nothing was re-deciphered here.
His report status: 3/3 pages transcribed; 3/3 pages deciphered. Still open: the transcription of the cipher itself, which is not in the
PDF or in this folder; it has been requested from George Lasry (`research/reading_audit/TRANSCRIPTIONS_WANTED.md`).
