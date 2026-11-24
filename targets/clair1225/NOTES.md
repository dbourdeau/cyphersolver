# Paget? → Votre Excellence; identity unestablished, Genoa, 3 April and 28 August 1714, BnF Clairambault 1225

Status: no write-up of our own (result by George Lasry, presented on docs/clair1225.html)

**24 Oct 2026, DECODE check** (Claude Opus 5.5): George Lasry's permission of 24 Oct 2026 covers his decryptions on DECODE. Searched the full DECODE record list (10,606 records, fetched 24 Oct 2026 with the project cookie) for this shelfmark (Clairambault 1225): no record, so DECODE holds no decryption of it; his full text exists only in his BnF cipher research report files. The excerpt state is kept.

## Source

This result is George Lasry's, obtained with ChatGPT Astra 6 and Anthropic Opus 5.5 and reported in "BnF cipher research" (10 October 2026), which he sent to Daniel Bourdeau on 13 October 2026 for publication here. The transcription, the key and the reading are his. This repository only spot-checked one sample against the Gallica image (below); it did not re-solve the cipher.

## His metadata

- Report status: 13/13 pages transcribed; 7/7 cipher pages deciphered
- Ciphertext-only: No
- Sender: Paget?
- Recipient: Votre Excellence; identity unestablished
- Date: Genoa, 3 April and 28 August 1714
- Key: 113 codes, 20 letter codes, 89 in nomenclature, 4 unidentified
- Ciphertext: 495 elements, 487 identified (98.4%)
- Contents: Negotiations to sell the island of Tabarka, secret intelligence and a disputed Genoese inheritance; the princess of Parma’s marriage to the king of Spain and the Farnese succession.
- Method category (our classification): key recovered based on adjacent plaintext; extent: complete

## His entry, as sent (excerpts and translations)

Quoted from the report; line breaks as extracted from the PDF.

```text
Clairambault 1225
Contents: Negotiations to sell the island of Tabarka, secret intelligence and a disputed Genoese inheritance;
the princess of Parma’s marriage to the king of Spain and the Farnese succession.
13/13 pages transcribed; 7/7 cipher pages deciphered
Ciphertext-only: No
Sender: Paget?
Recipient: Votre Excellence; identity unestablished
Year: Genoa, 3 April and 28 August 1714
Key: 113 codes, 20 letter codes, 89 in nomenclature, 4 unidentified
Ciphertext: 495 elements, 487 identified (98.4%)
Interlinear plaintext: Interlinear plaintext on ff53r–54r, f57v and ff58r–59r.
Gallica Gallica — f53r

Excerpt and Translation
Excerpt
f58v
qualitez qu’on peut desirer. Elle achevera sa 22e année le 25 Octobre prochain, estant née le
mesme mois en mil 692. Elle est bien faite, blonde, le visage rond, les traits fins et assez reguliers,
et la taille belle, quoy que moyenne, beaucoup d’esprit et un air fort modeste.
Translation
Qualities one could wish for. She will complete her twenty-second year on 25 October next, having been born
in the same month in 1692. She is well formed and blonde, with a round face, fine and fairly regular features,
and a fine figure, though of medium size; much intelligence and a very modest manner.
```

## Links

- <https://gallica.bnf.fr/ark:/12148/btv1b9001034d/f60.item>

## Images

- `lasry_p075_1.png`: George Lasry's image from the report (credit: George Lasry, BnF cipher research; manuscript © BnF via Gallica).
- Further images in the report, not copied here: p076_2.png.

## Spot-check (13 Oct 2026)

- Batch A. Image checked: https://gallica.bnf.fr/ark:/12148/btv1b9001034d/f60.item
- Folio matches the report: yes; cipher present: yes
- What we checked: f53r "Monseigneur", "Excellence ... le 19 du mois dernier"; codes with interlinear: "145.31.67.148.186.147.176" = Labbe Lomelini, "244.176.221" = Venise, "147.46.146.87 / 232.66.45.204" = l Isle de Tabarque, consistent with his Tabarka contents; f58v excerpt (princess of Parma) not compared; his key table not applied
- Verdict: **partly confirmed** (method key recovered based on adjacent plaintext, extent complete). The check is a sample, not a re-solution.
- Notes: Interlinear decipherments on ff53r-54r, 57v, 58r-59r give most of the plaintext. Princess of Parma = Elisabeth Farnese (born Oct 1692, married Philip V 1714) - excerpt facts are historically right.

## Verification 4, 23 Oct 2026

The profile marks this document read, but its texts entry names no file. The reading is George Lasry's ("BnF cipher
research", 10 Oct 2026); the repository holds only his entry with one excerpt and its translation (`lasry_entry.md`), and
NOTES, README and the folder give no fuller text. His decryption is his to publish, so the entry stays an **external
pointer** to his decipherment, with a note saying so; it is not scored or reviewed here.

## George Lasry's report PDF (24 Oct 2026)

Lasry sent his report on this item as a PDF (`lasry/report/28_clairambault-1225.pdf`), extracted with
`research/reading_audit/lasry_pdf_extract.py` into `lasry/report/` (summary, key image, excerpt and translation, the
full Readable text by folio). The page now shows it at the top. Measured: whole text 0.993 (v10_relabel.measure),
deciphered passages 0.988. His status: 13/13 pages transcribed; 7/7 cipher pages deciphered. Outcome: read. He translates the excerpt only
(`lasry/report/translation_excerpt.md`).

## 14 Nov 2026: decryption listed in outcome.texts

The full-texts check (`docs/_texts.py`) reported "no decryption file" for George Lasry's entry: his Readable text by folio
(`lasry/report/readable.md`, extracted unedited from his report PDF of 24 Oct 2026; see `lasry/report/ATTRIBUTION.md`) was listed
only as the reading. It is now also listed as the entry's decryption. No text was changed and nothing was re-deciphered here.
His report status: 13/13 pages transcribed; 7/7 cipher pages deciphered. Still open: the transcription of the cipher itself, which is not in the
PDF or in this folder; it has been requested from George Lasry (`research/reading_audit/TRANSCRIPTIONS_WANTED.md`).
