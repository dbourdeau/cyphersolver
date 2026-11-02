# Filippo Sega → Cardinal Caetano, 9 January 1591, BnF Français 3613 — Sega, ff148r–v

Status: no write-up of our own (result by George Lasry, presented on docs/sega1591.html)

**24 Oct 2026, DECODE check** (Claude Opus 5.5): George Lasry's permission of 24 Oct 2026 covers his decryptions on DECODE. Searched the full DECODE record list (10,606 records, fetched 24 Oct 2026 with the project cookie) for this shelfmark (Français 3613 — Sega, ff148r–v): no record, so DECODE holds no decryption of it; his full text exists only in his BnF cipher research report files. The excerpt state is kept.

## Source

This result is George Lasry's, obtained with ChatGPT Astra 6 and Anthropic Opus 5.5 and reported in "BnF cipher research" (10 October 2026), which he sent to Daniel Bourdeau on 13 October 2026 for publication here. The transcription, the key and the reading are his. This repository only spot-checked one sample against the Gallica image (below); it did not re-solve the cipher.

## His metadata

- Report status: 1/2 pages transcribed; Deciphered
- Ciphertext-only: No
- Sender: Filippo Sega
- Recipient: Cardinal Caetano
- Date: 9 January 1591
- Key: 29 plaintext codes and 1 null; published historical key 65.
- Ciphertext: 100 elements, 100 identified (100.0%): 99 plaintext codes and 1 null.
- Contents: A religious book, Navarre at Christmas Mass, and plans for an undertaking at Tours.
- Method category (our classification): read with known key; extent: complete

## His entry, as sent (excerpts and translations)

Quoted from the report; line breaks as extracted from the PDF.

```text
Français 3613 — Sega, ff148r–v
Contents: A religious book, Navarre at Christmas Mass, and plans for an undertaking at Tours.
1/2 pages transcribed; Deciphered
Ciphertext-only: No
Sender: Filippo Sega
Recipient: Cardinal Caetano
Year: 9 January 1591
Key: 29 plaintext codes and 1 null; published historical key 65.
Ciphertext: 100 elements, 100 identified (100.0%): 99 plaintext codes and 1 null.
Key elsewhere: Published historical key elsewhere: Meister, Die Geheimschrift im Dienste der
päpstlichen Kurie (1906), key 65, pp. 435–436.
Gallica — ff148r–v

Excerpt and Translation
Excerpt
f148v, complete enciphered passage and cleartext opening
Che Lignerac è stato inuiato d'ordine di Umena in Poitu et Bretagna a solecitar la impresa di Tours
per doue ua anco a questi efeto un religioso acciò se l uno fose impedito l altro pasi.
Translation
Lignerac has been sent by order of Umena to Poitou and Brittany to press the undertaking at Tours. A
religious man is also going there for this purpose, so that if one were prevented, the other might get through.
```

## Links

- <https://gallica.bnf.fr/ark:/12148/btv1b90582263/f157.item>
- <https://gallica.bnf.fr/ark:/12148/btv1b90582263/f158.item> — f148v, the cipher (canvas f158; the report links f157 = f148r, clear text)

## Images

- `lasry_p046_1.png`: George Lasry's image from the report (credit: George Lasry, BnF cipher research; manuscript © BnF via Gallica).
- Further images in the report, not copied here: p047_2.png, p048_3.png.

## Spot-check (13 Oct 2026)

- Batch A. Image checked: https://gallica.bnf.fr/ark:/12148/btv1b90582263/f158.item
- Folio matches the report: yes; cipher present: yes
- What we checked: f148v (canvas f158) after clear "Che Lignerac e stato inuiato di ordine di": "12 8.. omega 33 32+ 28 37 38 41 21 35 24 37 42 26 31 42" with Meister key 65 -> [Umena] in Poitu et Bretagna, matching his excerpt; f148r clear text (Navarre, Christmas mass at St Denis) matches contents
- Verdict: **confirmed** (method read with known key, extent complete). The check is a sample, not a re-solution.
- Notes: Key printed by Meister 1906 (key 65), so a published-key reading. Only 100 cipher elements. Cited link f157 is f148r (clear); cipher is on f148v = canvas f158.

## Notes and corrections

The cipher is on f148v, Gallica canvas f158. The report links f157, which is f148r (clear text).

## Verification 3, 23 Oct 2026

The v3 sweep flagged this entry at 0.59, scoring `lasry_entry.md` (his report pages: metadata, excerpt and English).
The enciphered passage alone, now `sega1591_reading.md`, scores **1.0 on explicit holes** (plain 0.33: the cipher
writes single consonants, *inuiato*, *efeto*, *fose*, *pasi*). Kept read; it is Lasry's reading with Meister's key 65.

## George Lasry's report PDF (24 Oct 2026)

Lasry sent his report on this item as a PDF, extracted with `research/reading_audit/lasry_pdf_extract.py` into `lasry/report/` (summary, key image, excerpt and translation, the full Readable text by folio). The page shows it at the top. Measured: whole text 0.971 (v10_relabel.measure), deciphered passages 1.0 (bare ? counted as unread). His status: 1/2 pages transcribed; Deciphered. Outcome: read.

## Dudout corrections, 29 Oct 2026
- A contemporary decipherment of Sega's letter of 9 Jan 1591 exists in AAV Segr. Stato Francia 32 (DECODE R5613, view 4, headed 'Decifrato'); the profile's 'plaintext: none known' needs revising. The legation key is Meister 1906 key no. 65; checked on R5621 f. 230 (decifrato of 21 Dec 1590) against ff. 228v, 231: 268/287 letters (0.93). Related Sega 1590 letters: R5612 (26 Nov 1590, 82/84 words), R5616 f. 71r-v (16 Jan 1591, 52/52 words) read with key 65, and R5618 (2 Jul 1591) in another system. Per his email, R5615 (duplicate, early Jan 1591) reads 95.1% on its first part only.
(Brice Dudout, research/dudout_2026-10-29/; his findings, not re-checked here.)
