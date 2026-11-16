# Darnétal (catalogue attribution for manuscript p103; not every unsigned letter established) → Unestablished for the checked selections, Bordeaux, 8 September 1650 for p103; dates of the other selected letters unestablished, BnF Clairambault 460 — reciprocal alphabet

Status: no write-up of our own (result by George Lasry, presented on docs/clair460alpha.html)

**24 Oct 2026, DECODE check** (Claude Opus 5.5): George Lasry's permission of 24 Oct 2026 covers his decryptions on DECODE. Searched the full DECODE record list (10,606 records, fetched 24 Oct 2026 with the project cookie) for this shelfmark (Clairambault 460 — reciprocal alphabet): no record, so DECODE holds no decryption of it; his full text exists only in his BnF cipher research report files. The excerpt state is kept.

## Source

This result is George Lasry's, obtained with ChatGPT Astra 6 and Anthropic Opus 5.5 and reported in "BnF cipher research" (10 October 2026), which he sent to Daniel Bourdeau on 13 October 2026 for publication here. The transcription, the key and the reading are his. This repository only spot-checked one sample against the Gallica image (below); it did not re-solve the cipher.

## His metadata

- Report status: 5/5 pages transcribed; 5/5 pages deciphered
- Ciphertext-only: No
- Sender: Darnétal (catalogue attribution for manuscript p103; not every unsigned letter established)
- Recipient: Unestablished for the checked selections
- Date: Bordeaux, 8 September 1650 for p103; dates of the other selected letters unestablished
- Key: 22 symbols, 22 letter signs
- Ciphertext: 888 visible elements, 887 identified; additional ciphertext hidden in the binding
- Contents: Reports on the Princes’ liberty, Nemours leaving Paris, Spanish concern over Bordeaux, Turenne’s negotiations, Chevreuse’s mediation, and Sfondrati’s advance with six hundred horsemen.
- Method category (our classification): key recovered based on adjacent plaintext; extent: complete

## His entry, as sent (excerpts and translations)

Quoted from the report; line breaks as extracted from the PDF.

```text
Clairambault 460 — reciprocal alphabet
Contents: Reports on the Princes’ liberty, Nemours leaving Paris, Spanish concern over Bordeaux, Turenne’s
negotiations, Chevreuse’s mediation, and Sfondrati’s advance with six hundred horsemen.
5/5 pages transcribed; 5/5 pages deciphered
Ciphertext-only: No
Sender: Darnétal (catalogue attribution for manuscript p103; not every unsigned letter established)
Recipient: Unestablished for the checked selections
Year: Bordeaux, 8 September 1650 for p103; dates of the other selected letters unestablished
Key: 22 symbols, 22 letter signs
Ciphertext: 888 visible elements, 887 identified; additional ciphertext hidden in the binding
Interlinear plaintext: Interlinear historical decipherments on selected PDF50/59/61 passages.
Plaintext in the margin or below: Some glosses are displaced above earlier lines or at the bottom of
the facing page.
Plaintext in another folio of the same volume: Facing manuscript p106 supplies gloss context for
selected p107 (PDF61).

Excerpt and Translation
Excerpt
p107 — complete cipher paragraph
jusques à Neufchastel Mais au lieu de le faire passer la riviere, les Espagnolz luy ont envoyé six
cens chevaux, parce qu'il avoit (disent ils) peu de cavalerie et luy ont faict demeurer. Ce qui fait
croire qu'ils ont tousiours la pensée de faire quelque siege.
Translation
as far as Neufchâtel But instead of making him cross the river, the Spaniards sent him six hundred
horsemen because, they say, he had little cavalry, and they made him remain there. This suggests that
they still intend to undertake a siege.
```

## Links

- No link in the report.

## Images

- `lasry_p067_1.png`: George Lasry's image from the report (credit: George Lasry, BnF cipher research; manuscript © BnF via Gallica).
- Further images in the report, not copied here: p068_2.png.

## Spot-check (13 Oct 2026)

- Batch A. Image checked: none (no Gallica link in entry; Clairambault 460 checked only via his p107 crop)
- Folio matches the report: unclear; cipher present: yes
- What we checked: p107 crop: "h l e e h b g p h b 9 g n K i t l g t t" with his reciprocal alphabet (h=o, l=n, e=t, b=u, g=s, p=i, 9=r, n=l, K=a) = "ont tousiours la pensee", matching interlinear and his excerpt
- Verdict: **partly confirmed** (method key recovered based on adjacent plaintext, extent complete). The check is a sample, not a re-solution.
- Notes: Folio identity not checked on Gallica. Simple reciprocal monoalphabet; interlinear decipherments on the page. Same volume as bouillon1650 (pp53-55) - overlap of volume, different cipher.

## Verification 4, 23 Oct 2026

The profile marks this document read, but its texts entry names no file. The reading is George Lasry's ("BnF cipher
research", 10 Oct 2026); the repository holds only his entry with one excerpt and its translation (`lasry_entry.md`), and
NOTES, README and the folder give no fuller text. His decryption is his to publish, so the entry stays an **external
pointer** to his decipherment, with a note saying so; it is not scored or reviewed here.

## George Lasry's report PDF (24 Oct 2026)

Lasry sent his report on this item as a PDF (`lasry/report/24_clairambault-460-reciprocal-alphabet.pdf`), extracted with
`research/reading_audit/lasry_pdf_extract.py` into `lasry/report/` (summary, key image, excerpt and translation, the
full Readable text by folio). The page now shows it at the top. Measured: whole text 1.0 (v10_relabel.measure),
deciphered passages 0.995. His status: 5/5 pages transcribed; 5/5 pages deciphered. Outcome: read. He translates the excerpt only
(`lasry/report/translation_excerpt.md`).

## 14 Nov 2026: decryption listed in outcome.texts

The full-texts check (`docs/_texts.py`) reported "no decryption file" for George Lasry's entry: his Readable text by folio
(`lasry/report/readable.md`, extracted unedited from his report PDF of 24 Oct 2026; see `lasry/report/ATTRIBUTION.md`) was listed
only as the reading. It is now also listed as the entry's decryption. No text was changed and nothing was re-deciphered here.
His report status: 5/5 pages transcribed; 5/5 pages deciphered. Still open: the transcription of the cipher itself, which is not in the
PDF or in this folder; it has been requested from George Lasry (`research/reading_audit/TRANSCRIPTIONS_WANTED.md`).
