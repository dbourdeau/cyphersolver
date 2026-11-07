# de Loménie Brienne → Servien, 10 January and 1 August 1653; letter B undated in selected cipher pages, BnF Français 5160

Status: no write-up of our own (result by George Lasry, presented on docs/brienne5160.html)

**24 Oct 2026, DECODE check** (Claude Opus 5.5): George Lasry's permission of 24 Oct 2026 covers his decryptions on DECODE. Searched the full DECODE record list (10,606 records, fetched 24 Oct 2026 with the project cookie) for this shelfmark (Français 5160): no record, so DECODE holds no decryption of it; his full text exists only in his BnF cipher research report files. The excerpt state is kept.

## Source

This result is George Lasry's, obtained with ChatGPT Astra 6 and Anthropic Opus 5.5 and reported in "BnF cipher research" (10 October 2026), which he sent to Daniel Bourdeau on 13 October 2026 for publication here. The transcription, the key and the reading are his. This repository only spot-checked one sample against the Gallica image (below); it did not re-solve the cipher.

## His metadata

- Report status: 14/14 pages transcribed; 13/13 cipher pages deciphered
- Ciphertext-only: No
- Sender: de Loménie Brienne
- Recipient: Servien
- Date: 10 January and 1 August 1653; letter B undated in selected cipher pages
- Key: 136 symbols/codes: 25 letter signs, 101 in nomenclature, 7 nulls ?, 3 unidentified
- Ciphertext: 1,356 elements, 1,308 identified (96.5%); 40 nulls ?, 3 unidentified, 5 cancelled
- Contents: Savoy’s policy toward Spain and the proposed marriage of the Infanta; the Duke of Mantua, Casale and the Monferrat dispute. Brienne also reports army news, the fall of Bordeaux and the succession to La Vieuville in financial administration.
- Method category (our classification): key recovered based on adjacent plaintext; extent: complete

## His entry, as sent (excerpts and translations)

Quoted from the report; line breaks as extracted from the PDF.

```text
Français 5160
Contents: Savoy’s policy toward Spain and the proposed marriage of the Infanta; the Duke of Mantua,
Casale and the Monferrat dispute. Brienne also reports army news, the fall of Bordeaux and the succession to
La Vieuville in financial administration.
14/14 pages transcribed; 13/13 cipher pages deciphered
Ciphertext-only: No
Sender: de Loménie Brienne
Recipient: Servien
Year: 10 January and 1 August 1653; letter B undated in selected cipher pages
Key: 136 symbols/codes: 25 letter signs, 101 in nomenclature, 7 nulls ?, 3 unidentified
Ciphertext: 1,356 elements, 1,308 identified (96.5%); 40 nulls ?, 3 unidentified, 5 cancelled
Plaintext in another folio of the same volume: Same volume: literal plaintext of letter B at f10r; literal
plaintext of letter C at ff17r–v. Letter A uses the same key. ·
Gallica ff1r–3r
Gallica ff9r–v
Gallica ff18r–21r

Excerpt and Translation
Excerpt
f18r
Les sages en jugent autrement je m’en remettray à leurs sentimens. Pour avoir droit de se plaindre du
duc de Mantoue des graces qu'il depart aux Espagnols, il faudroit l'en rechercher de semblables ou
de quipolentes, et sy il s'y rendoit difficile on pouroit avec justice luy reprocher sa conduitte. Mais de luy
imputer…
Translation
The wise judge otherwise; I will defer to their judgment. To complain about the Duke of Mantua’s favors to the
Spaniards, one would have to ask him for similar or equivalent favors; if he proved reluctant, one could then
justly reproach his conduct. But to impute to him…
```

## Links

- <https://gallica.bnf.fr/ark:/12148/btv1b9060495t/f24.item>
- <https://gallica.bnf.fr/ark:/12148/btv1b9060495t/f29.item>
- <https://gallica.bnf.fr/ark:/12148/btv1b9060495t/f8.item>
- <https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b9060495t/f24/full/1600,/0/default.jpg> — image checked in the spot-check

## Images

- `lasry_p095_1.png`: George Lasry's image from the report (credit: George Lasry, BnF cipher research; manuscript © BnF via Gallica).
- Further images in the report, not copied here: p096_2.png.

## Spot-check (13 Oct 2026)

- Batch B. Image checked: https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b9060495t/f24/full/1600,/0/default.jpg
- Folio matches the report: yes; cipher present: yes
- What we checked: f9r (canvas 24) after "ordres que vous avez receu": 36 60 33 n 39 x 21 , 6 28 ... -> de la co-n-du-i-te , que vo... = "de la conduite que vo(us)" with his table (36=de,60=la,33=co,39=du,21=te,6bar=que,28bar=vo); fits the f10r plaintext context. Excerpt f18r not imaged by me.
- Verdict: **confirmed** (method key recovered based on adjacent plaintext, extent complete). The check is a sample, not a re-solution.
- Notes: Clear copies of letters B and C in same volume (f10r, ff17r-v). 96.5% (1,308 of 1,356) excludes the 40 probable nulls, 3 unidentified and 5 cancelled elements; several nomenclator values marked ?. 1653 consistent (Bordeaux fell Jul/Aug 1653).

## Verification 4, 23 Oct 2026

The profile marks this document read, but its texts entry names no file. The reading is George Lasry's ("BnF cipher
research", 10 Oct 2026); the repository holds only his entry with one excerpt and its translation (`lasry_entry.md`), and
NOTES, README and the folder give no fuller text. His decryption is his to publish, so the entry stays an **external
pointer** to his decipherment, with a note saying so; it is not scored or reviewed here.

## George Lasry's report PDF (24 Oct 2026)

Lasry sent his report on this item as a PDF (`lasry/report/38_francais-5160.pdf`), extracted with
`research/reading_audit/lasry_pdf_extract.py` into `lasry/report/` (summary, key image, excerpt and translation, the
full Readable text by folio). The page now shows it at the top. Measured: whole text 0.981 (v10_relabel.measure),
deciphered passages 0.993. His status: 14/14 pages transcribed; 13/13 cipher pages deciphered. Outcome: read. He translates the excerpt only
(`lasry/report/translation_excerpt.md`).
