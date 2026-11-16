# Brienne → Queen of Poland, Compiègne, 19 May 1646, BnF Clairambault 1067

Status: no write-up of our own (result by George Lasry, presented on docs/brienne1067.html)

**24 Oct 2026, DECODE check** (Claude Opus 5.5): George Lasry's permission of 24 Oct 2026 covers his decryptions on DECODE. Searched the full DECODE record list (10,606 records, fetched 24 Oct 2026 with the project cookie) for this shelfmark (Clairambault 1067): no record, so DECODE holds no decryption of it; his full text exists only in his BnF cipher research report files. The excerpt state is kept.

## Source

This result is George Lasry's, obtained with ChatGPT Astra 6 and Anthropic Opus 5.5 and reported in "BnF cipher research" (10 October 2026), which he sent to Daniel Bourdeau on 13 October 2026 for publication here. The transcription, the key and the reading are his. This repository only spot-checked one sample against the Gallica image (below); it did not re-solve the cipher.

## His metadata

- Report status: 6/6 pages transcribed; 4/4 cipher pages deciphered
- Ciphertext-only: No
- Sender: Brienne
- Recipient: Queen of Poland
- Date: Compiègne, 19 May 1646
- Key: 88 symbols/codes, 25 letter signs, 61 in nomenclature, 2 nulls
- Ciphertext: 350 elements, 349 identified (99.7%)
- Contents: Brienne advises delaying replies about the government of Nivernais, so continued possession may strengthen the claim. He also reports French and Dutch military preparations and Prince Thomas’s embarkation for an Italian expedition.
- Method category (our classification): key recovered based on adjacent plaintext; extent: complete

## His entry, as sent (excerpts and translations)

Quoted from the report; line breaks as extracted from the PDF.

```text
Clairambault 1067
Contents: Brienne advises delaying replies about the government of Nivernais, so continued possession may
strengthen the claim. He also reports French and Dutch military preparations and Prince Thomas’s
embarkation for an Italian expedition.
6/6 pages transcribed; 4/4 cipher pages deciphered
Ciphertext-only: No
Sender: Brienne
Recipient: Queen of Poland
Year: Compiègne, 19 May 1646
Key: 88 symbols/codes, 25 letter signs, 61 in nomenclature, 2 nulls
Ciphertext: 350 elements, 349 identified (99.7%)
Interlinear plaintext: Historical plaintext above cipher rows on PDF50–53, ff226–227 and continuation;
letter ends at PDF55.
Gallica Gallica — f226r

Excerpt and Translation
Excerpt
f226v
Le mien a esté qu’en la pluspart des affaires du monde le souverain conseil est de gaigner temps, et
que ce seroit assez tost respondre aux ministres de Monsieur de Mantoue quand ilz
renouvelleroient leurs instances; et peut estre qu’ayant presentement diverses choses à poursuivre
ilz pourront s’oublier de celle-là, et ainsi le titre du gouvernement de Nivernois se trouvera fortiffié
d’une possession maintenue depuis son absence du Royaume.
Translation
My view was that in most affairs of the world the wisest course is to gain time, and that it would be soon
enough to answer Monsieur de Mantua’s ministers when they renewed their requests. Perhaps, having
various matters to pursue at present, they will forget this one; thus the title to the government of Nivernois will
be strengthened by possession maintained since his departure from the kingdom.
```

## Links

- <https://gallica.bnf.fr/ark:/12148/btv1b90008551/f48.item>
- <https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b90008551/f48/full/1600,/0/default.jpg> — image checked in the spot-check

## Images

- `lasry_p099_1.png`: George Lasry's image from the report (credit: George Lasry, BnF cipher research; manuscript © BnF via Gallica).
- Further images in the report, not copied here: p100_2.png.

## Spot-check (13 Oct 2026)

- Batch B. Image checked: https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b90008551/f48/full/1600,/0/default.jpg
- Folio matches the report: yes; cipher present: yes
- What we checked: f226r: "Madame", clear text then cipher row with interlinear "que je communicasse sa despesche a la Reyne"; f226v show-through shows interlinear "...le souverain conseil est de gaigner temps..." as in his excerpt; codes not decoded independently
- Verdict: **confirmed** (method key recovered based on adjacent plaintext, extent complete). The check is a sample, not a re-solution.
- Notes: Fully interlined by a contemporary hand; 99.7% identified. Recipient Queen of Poland (Marie-Louise Gonzague) fits the Nevers/Mantua content.

## Verification 4, 23 Oct 2026

The profile marks this document read, but its texts entry names no file. The reading is George Lasry's ("BnF cipher
research", 10 Oct 2026); the repository holds only his entry with one excerpt and its translation (`lasry_entry.md`), and
NOTES, README and the folder give no fuller text. His decryption is his to publish, so the entry stays an **external
pointer** to his decipherment, with a note saying so; it is not scored or reviewed here.

## George Lasry's report PDF (24 Oct 2026)

Lasry sent his report on this item as a PDF (`lasry/report/40_clairambault-1067.pdf`), extracted with
`research/reading_audit/lasry_pdf_extract.py` into `lasry/report/` (summary, key image, excerpt and translation, the
full Readable text by folio). The page now shows it at the top. Measured: whole text 1.0 (v10_relabel.measure),
deciphered passages 1.0. His status: 6/6 pages transcribed; 4/4 cipher pages deciphered. Outcome: read. He translates the excerpt only
(`lasry/report/translation_excerpt.md`).

## 14 Nov 2026: decryption listed in outcome.texts

The full-texts check (`docs/_texts.py`) reported "no decryption file" for George Lasry's entry: his Readable text by folio
(`lasry/report/readable.md`, extracted unedited from his report PDF of 24 Oct 2026; see `lasry/report/ATTRIBUTION.md`) was listed
only as the reading. It is now also listed as the entry's decryption. No text was changed and nothing was re-deciphered here.
His report status: 6/6 pages transcribed; 4/4 cipher pages deciphered. Still open: the transcription of the cipher itself, which is not in the
PDF or in this folder; it has been requested from George Lasry (`research/reading_audit/TRANSCRIPTIONS_WANTED.md`).
