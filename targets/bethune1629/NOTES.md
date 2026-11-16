# Louis XIII → Philippe de Béthune, 30 June 1629, BnF Français 3675 — Louis XIII à Béthune, 30 juin 1629

Status: no write-up of our own (result by George Lasry, presented on docs/bethune1629.html)

**24 Oct 2026, DECODE check** (Claude Opus 5.5): George Lasry's permission of 24 Oct 2026 covers his decryptions on DECODE. Searched the full DECODE record list (10,606 records, fetched 24 Oct 2026 with the project cookie) for this shelfmark (Français 3675 — Louis XIII à Béthune, 30 juin 1629): no record, so DECODE holds no decryption of it; his full text exists only in his BnF cipher research report files. The excerpt state is kept.

## Source

This result is George Lasry's, obtained with ChatGPT Astra 6 and Anthropic Opus 5.5 and reported in "BnF cipher research" (10 October 2026), which he sent to Daniel Bourdeau on 13 October 2026 for publication here. The transcription, the key and the reading are his. This repository only spot-checked one sample against the Gallica image (below); it did not re-solve the cipher.

## His metadata

- Report status: 1/2 pages transcribed; 1 more in part; Partly deciphered
- Ciphertext-only: No
- Sender: Louis XIII
- Recipient: Philippe de Béthune
- Date: 30 June 1629
- Key: 59 mapped symbols; 11 unidentified.
- Ciphertext: 177 elements, 166 identified (93.8%).
- Contents: Louis XIII nominates the Archbishop of Lyon for a cardinal’s hat, citing the services of his brother Richelieu.
- Method category (our classification): key recovered based on adjacent plaintext; extent: partial

## His entry, as sent (excerpts and translations)

Quoted from the report; line breaks as extracted from the PDF.

```text
Français 3675 — Louis XIII à Béthune, 30 juin 1629
Contents: Louis XIII nominates the Archbishop of Lyon for a cardinal’s hat, citing the services of his brother
Richelieu.
1/2 pages transcribed; 1 more in part; Partly deciphered
Ciphertext-only: No
Sender: Louis XIII
Recipient: Philippe de Béthune
Year: 30 June 1629
Key: 59 mapped symbols; 11 unidentified.
Ciphertext: 177 elements, 166 identified (93.8%).
Interlinear plaintext: Interlinear plaintext on f53r; shared signs checked against interlinear passages
on f83r–v and f136r. ·
Gallica Gallica — f53r

Excerpt and Translation
Excerpt
f53r, three complete cipher-bearing rows and preceding cleartext
vous les fassiez valloir et peser à sa Saincteté y adjoustant de plus la recommandation des grands
services de mon cousin le cardinal de Richelieu son frere de qui le [passage rayé] la conduicte et
les actions sont
Translation
you should make these qualities count and carry weight with His Holiness, adding also the recommendation of
the great services of my cousin Cardinal Richelieu, his brother, whose [cancelled text] conduct and actions
are…
```

## Links

- <https://gallica.bnf.fr/ark:/12148/btv1b9059466m/f108.item>
- <https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b9059466m/f108/full/1600,/0/default.jpg> — image checked in the spot-check

## Images

- `lasry_p101_1.png`: George Lasry's image from the report (credit: George Lasry, BnF cipher research; manuscript © BnF via Gallica).
- Further images in the report, not copied here: p102_2.png.

## Spot-check (13 Oct 2026)

- Batch B. Image checked: https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b9059466m/f108/full/1600,/0/default.jpg
- Folio matches the report: yes; cipher present: yes
- What we checked: f53r: clear "vous les fassiez valloir et peser a sa Ste y adioustant de plus la recommandation des grands" + interlinear over cipher "services de mon cousin le cardinal de Richelieu son frere de qui la [struck] conduite et les actions" = his excerpt; next 4 cipher rows uninterlined (his own decipherment, not checked)
- Verdict: **confirmed** (method key recovered based on adjacent plaintext, extent partial). The check is a sample, not a re-solution.
- Notes: Addressed "Monsr de Bethune"; Archbishop of Lyon (Alphonse de Richelieu) cardinalate 1629 fits. 93.8%, partly deciphered.

## Verification 4, 23 Oct 2026

The profile marks this document read, but its texts entry names no file. The reading is George Lasry's ("BnF cipher
research", 10 Oct 2026); the repository holds only his entry with one excerpt and its translation (`lasry_entry.md`), and
NOTES, README and the folder give no fuller text. His decryption is his to publish, so the entry stays an **external
pointer** to his decipherment, with a note saying so; it is not scored or reviewed here.


## George Lasry's report PDF (24 Oct 2026)

Lasry sent his report on this item as a PDF (`lasry/report/41_francais-3675-louis-xiii-a-bethune-30-juin-1629.pdf`),
extracted with `research/reading_audit/lasry_pdf_extract.py` into `lasry/report/`. The page shows it at the top.
Measured: whole text 0.954 (v10_relabel.measure); every deciphered (bold) run gives sense. The report itself calls the
letter partly deciphered (59 mapped symbols, 11 unidentified; f53v transcribed in part), so the outcome is read in part.

## Remaining gaps

- f53r-f53v: about 11 unidentified sign types and the [?] groups in his readable text - blocker: no-key-material; the interlinear decipherment covers only part of f53r and his key gives these signs no value.

## Escalation

- [x] siblings: interlinear passages on f83r-v and f136r used by Lasry to check shared signs (his report)
- [x] clear-pages: the secretary's interlinear decipherment on f53r is the adjacent plaintext the key came from
- [x] known-keys: Lasry's reconstructed key is shown on the page
- [x] print: no printed decipherment found; DECODE has no record (24 Oct 2026)
- [n/a] key-rebuild: the key reconstruction is George Lasry's, not this project's work
- [x] retry: his full Readable text (24 Oct 2026) read and measured

## 14 Nov 2026: decryption listed in outcome.texts

The full-texts check (`docs/_texts.py`) reported "no decryption file" for George Lasry's entry: his Readable text by folio
(`lasry/report/readable.md`, extracted unedited from his report PDF of 24 Oct 2026; see `lasry/report/ATTRIBUTION.md`) was listed
only as the reading. It is now also listed as the entry's decryption. No text was changed and nothing was re-deciphered here.
His report status: 1/2 pages transcribed; 1 more in part; Partly deciphered. Still open: the transcription of the cipher itself, which is not in the
PDF or in this folder; it has been requested from George Lasry (`research/reading_audit/TRANSCRIPTIONS_WANTED.md`).
