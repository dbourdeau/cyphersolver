# Châtillon → Servien, 3 août 1635, BnF Français 3758 — Châtillon, 3 August 1635

Status: no write-up of our own (result by George Lasry, presented on docs/chatillon1635.html)

**24 Oct 2026, DECODE check** (Claude Opus 5.5): George Lasry's permission of 24 Oct 2026 covers his decryptions on DECODE. Searched the full DECODE record list (10,606 records, fetched 24 Oct 2026 with the project cookie) for this shelfmark (Français 3758 — Châtillon, 3 August 1635): no record, so DECODE holds no decryption of it; his full text exists only in his BnF cipher research report files. The excerpt state is kept.

## Source

This result is George Lasry's, obtained with ChatGPT Astra 6 and Anthropic Opus 5.5 and reported in "BnF cipher research" (10 October 2026), which he sent to Daniel Bourdeau on 13 October 2026 for publication here. The transcription, the key and the reading are his. This repository only spot-checked one sample against the Gallica image (below); it did not re-solve the cipher.

## His metadata

- Report status: 10/10 pages transcribed; 4/4 cipher pages deciphered
- Ciphertext-only: No
- Sender: Châtillon
- Recipient: Servien
- Date: 3 août 1635
- Key: 78 signs: 56 letter signs, 20 in nomenclature, 2 repeat controls.
- Ciphertext: 666 written positions, 624 identified (93.7%); one group boundary uncertain.
- Contents: Châtillon criticizes the army’s condition and discusses withdrawal across the Rhine for greater safety.
- Method category (our classification): key recovered based on adjacent plaintext; extent: partial

## His entry, as sent (excerpts and translations)

Quoted from the report; line breaks as extracted from the PDF.

```text
Français 3758 — Châtillon, 3 August 1635
Contents: Châtillon criticizes the army’s condition and discusses withdrawal across the Rhine for greater
safety.
10/10 pages transcribed; 4/4 cipher pages deciphered
Ciphertext-only: No
Sender: Châtillon
Recipient: Servien
Year: 3 août 1635
Key: 78 signs: 56 letter signs, 20 in nomenclature, 2 repeat controls.
Ciphertext: 666 written positions, 624 identified (93.7%); one group boundary uncertain.
Plaintext in another folio of the same volume: Plaintext in the same volume: f123v for f124r; f126r
for f126v–127r; f127r for f127v.

Excerpt and Translation
Excerpt
f127v, cipher continuation
Cette consideration les pourra empescher de s’engager si avant, mais Je Vous respon que nous
ne jouons point de ruse cete fois, mais nous passons le Rhin pour nostre plus grande seurete
afin d’avoir se grand fleuve entre les ennemis et nous.
Translation
This consideration may prevent them from advancing so far; but I assure you that we are playing no trick this
time. We cross the Rhine for our greater safety, in order to have this great river between the enemy and
ourselves.
```

## Links

- No link in the report.

## Images

- `lasry_p087_2.png`: George Lasry's image from the report (credit: George Lasry, BnF cipher research; manuscript © BnF via Gallica).
- Further images in the report, not copied here: p086_1.png.

## Spot-check (13 Oct 2026)

- Batch B. Image checked: none (no Gallica link in dossier; fr. 3758 ark not found offline, gallica.bnf.fr behind Cloudflare)
- Folio matches the report: unclear; cipher present: yes
- What we checked: his f127v crop: clear "mais Je Vous respon que" then 95(nous)...46(ennemi)...33(de)... codes consistent with his table, but sign-level read of 8+ symbols from the small crop was not reliable
- Verdict: **partly confirmed** (method key recovered based on adjacent plaintext, extent partial). The check is a sample, not a re-solution.
- Notes: Plaintext of the same letters elsewhere in the volume (f123v, f126r, f127r). 93.7% identified. Repo CATALOGUE lists Chatillon-Servien fr. 3758 nos.100,104 (ark btv1b9059471x?).

## Notes and corrections

Fr. 3758 is also part of [targets/rohan1636](../rohan1636/NOTES.md).

## Verification 4, 23 Oct 2026

The profile marks this document read, but its texts entry names no file. The reading is George Lasry's ("BnF cipher
research", 10 Oct 2026); the repository holds only his entry with one excerpt and its translation (`lasry_entry.md`), and
NOTES, README and the folder give no fuller text. His decryption is his to publish, so the entry stays an **external
pointer** to his decipherment, with a note saying so; it is not scored or reviewed here.

## George Lasry's report PDF (24 Oct 2026)

Lasry sent his report on this item as a PDF (`lasry/report/34_francais-3758-chatillon-3-august-1635.pdf`), extracted with
`research/reading_audit/lasry_pdf_extract.py` into `lasry/report/` (summary, key image, excerpt and translation, the
full Readable text by folio). The page now shows it at the top. Measured: whole text 0.998 (v10_relabel.measure),
deciphered passages 1.0. His status: 10/10 pages transcribed; 4/4 cipher pages deciphered. Outcome: read. He translates the excerpt only
(`lasry/report/translation_excerpt.md`).

## 14 Nov 2026: decryption listed in outcome.texts

The full-texts check (`docs/_texts.py`) reported "no decryption file" for George Lasry's entry: his Readable text by folio
(`lasry/report/readable.md`, extracted unedited from his report PDF of 24 Oct 2026; see `lasry/report/ATTRIBUTION.md`) was listed
only as the reading. It is now also listed as the entry's decryption. No text was changed and nothing was re-deciphered here.
His report status: 10/10 pages transcribed; 4/4 cipher pages deciphered. Still open: the transcription of the cipher itself, which is not in the
PDF or in this folder; it has been requested from George Lasry (`research/reading_audit/TRANSCRIPTIONS_WANTED.md`).
