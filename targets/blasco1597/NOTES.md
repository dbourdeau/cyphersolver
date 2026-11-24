# Juan Blasco de Aragon → Not established, 2 May 1597, BnF Français 23054 — Blasco, 2 May 1597

Status: no write-up of our own (result by George Lasry, presented on docs/blasco1597.html)

**24 Oct 2026, DECODE check** (Claude Opus 5.5): George Lasry's permission of 24 Oct 2026 covers his decryptions on DECODE. Searched the full DECODE record list (10,606 records, fetched 24 Oct 2026 with the project cookie) for this shelfmark (Français 23054 — Blasco, 2 May 1597): no record, so DECODE holds no decryption of it; his full text exists only in his BnF cipher research report files. The excerpt state is kept.

## Source

This result is George Lasry's, obtained with ChatGPT Astra 6 and Anthropic Opus 5.5 and reported in "BnF cipher research" (10 October 2026), which he sent to Daniel Bourdeau on 13 October 2026 for publication here. The transcription, the key and the reading are his. This repository only spot-checked one sample against the Gallica image (below); it did not re-solve the cipher.

## His metadata

- Report status: 3/4 pages transcribed; 1 more in part; 3/3 cipher pages deciphered
- Ciphertext-only: Yes
- Sender: Juan Blasco de Aragon
- Recipient: Not established
- Date: 2 May 1597
- Key: 16 codes, 16 letter values; 5 unidentified positions
- Ciphertext: 107 elements, 102 identified (95.3%)
- Contents: Juan Blasco reports court negotiations, the prospect of coming with the princess, and efforts to obtain royal favors. He discusses a gift for Don Cristóbal and the support of Don Juan, Chinchón and Miranda.
- Method category (our classification): key recovered from ciphertext-only; extent: complete

## His entry, as sent (excerpts and translations)

Quoted from the report; line breaks as extracted from the PDF.

```text
Français 23054 — Blasco, 2 May 1597
Contents: Juan Blasco reports court negotiations, the prospect of coming with the princess, and efforts to
obtain royal favors. He discusses a gift for Don Cristóbal and the support of Don Juan, Chinchón and
Miranda.
3/4 pages transcribed; 1 more in part; 3/3 cipher pages deciphered
Ciphertext-only: Yes
Sender: Juan Blasco de Aragon
Recipient: Not established
Year: 2 May 1597
Key: 16 codes, 16 letter values; 5 unidentified positions
Ciphertext: 107 elements, 102 identified (95.3%)
Gallica f71r
Excerpt and Translation
Excerpt
f72r
por fuerça [?] con el parecer de todos los amigos. No ay duda que lo de venir con la princesa como
dize V. E., siendo con las condiciones que V. E. apunta, seria lo que mejor estuviesse, pero hasta agora
no ay nada en esto, a lo menos no lo sabemos.
Translation
By force [?], with the opinion of all our friends. There is no doubt that coming with the princess, as Your
Excellency says, on the conditions Your Excellency specifies, would be best; but so far there is nothing in this,
at least as far as we know.

Excerpt
f72v
Estamos tratando con don Baltasar de hacer algun presente a don Christoual, que es el que mand[a]
todo, y no se perdera ocasion ninguna en que se ofrezca hacer el servicio de V. E. que no se haga.
Translation
We are discussing with Don Baltasar giving some present to Don Cristóbal, who commands everything; no
opportunity to serve Your Excellency will be left unused.
```

## Links

- <https://gallica.bnf.fr/ark:/12148/btv1b9063548f/f134.item>

## Images

- `lasry_p038_1.png`: George Lasry's image from the report (credit: George Lasry, BnF cipher research; manuscript © BnF via Gallica).
- Further images in the report, not copied here: p038_2.png, p039_3.png.

## Spot-check (13 Oct 2026)

- Batch A. Image checked: https://gallica.bnf.fr/ark:/12148/btv1b9063548f/f134.item
- Folio matches the report: yes; cipher present: yes
- What we checked: Gallica f71r = Spanish letter, clear "Señor" heading, Blasco hand; cipher check on his f72r crop: "13.7.20.8.14 2.29.20 9.3 10.14.8.20.2.7.18.3" = venir con la princesa, matching his excerpt
- Verdict: **confirmed** (method key recovered from ciphertext-only, extent complete). The check is a sample, not a re-solution.
- Notes: Only 107 cipher elements (numbers in clear Spanish text); 16-value key from a short sample, so mostly context-driven. f71r itself is clear text; f72 holds most cipher.

## Verification 4, 23 Oct 2026

The profile marks this document read, but its texts entry names no file. The reading is George Lasry's ("BnF cipher
research", 10 Oct 2026); the repository holds only his entry with one excerpt and its translation (`lasry_entry.md`), and
NOTES, README and the folder give no fuller text. His decryption is his to publish, so the entry stays an **external
pointer** to his decipherment, with a note saying so; it is not scored or reviewed here.

## George Lasry's report PDF (24 Oct 2026)

Lasry sent his report on this item as a PDF, extracted with `research/reading_audit/lasry_pdf_extract.py` into `lasry/report/` (summary, key image, excerpt and translation, the full Readable text by folio). The page shows it at the top. Measured: whole text 0.989 (v10_relabel.measure), deciphered passages 0.857 (bare ? counted as unread). His status: 3/4 pages transcribed; 1 more in part; 3/3 cipher pages deciphered. Outcome: read in part.

## Remaining gaps

- ff71r-72v: unread groups between the deciphered runs - blocker: no-key-material; left as George Lasry marks them; no other key or plaintext known; his decipherment is the only one
- the fourth page, transcribed in part: not transcribed or deciphered in full in Lasry's report - blocker: no-key-material; his report status says so; outside this project's work, no other key or plaintext known

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
His report status: 3/4 pages transcribed; 1 more in part; 3/3 cipher pages deciphered. Still open: the transcription of the cipher itself, which is not in the
PDF or in this folder; it has been requested from George Lasry (`research/reading_audit/TRANSCRIPTIONS_WANTED.md`).
