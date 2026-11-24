# Unidentified → Unidentified, Unestablished;1554/1555 remains a hypothesis, BnF Clairambault 1161

Status: no write-up of our own (result by George Lasry, presented on docs/clair1161.html)

**24 Oct 2026, DECODE check** (Claude Opus 5.5): George Lasry's permission of 24 Oct 2026 covers his decryptions on DECODE. Searched the full DECODE record list (10,606 records, fetched 24 Oct 2026 with the project cookie) for this shelfmark (Clairambault 1161): no record, so DECODE holds no decryption of it; his full text exists only in his BnF cipher research report files. The excerpt state is kept.

## Source

This result is George Lasry's, obtained with ChatGPT Astra 6 and Anthropic Opus 5.5 and reported in "BnF cipher research" (10 October 2026), which he sent to Daniel Bourdeau on 13 October 2026 for publication here. The transcription, the key and the reading are his. This repository only spot-checked one sample against the Gallica image (below); it did not re-solve the cipher.

## His metadata

- Report status: 6/6 pages transcribed; 2/6 pages deciphered; 4 more in part
- Ciphertext-only: No
- Sender: Unidentified
- Recipient: Unidentified
- Date: Unestablished;1554/1555 remains a hypothesis
- Key: 51 accepted forms: 38 letter signs, 11 nomenclature entries, 2 nulls, 39 provisional unidentified labels
- Ciphertext: 3,149 elements, 3,046 identified; 5 further wordlike groups not classified
- Contents: Political notices concerning England and Flanders: English arms and the Tower, religious policy, ships bound for Spain, Genoese lending, foreign courtiers, and a reported plan to force entry at Hampton Court.
- Method category (our classification): key recovered based on adjacent plaintext; extent: partial

## His entry, as sent (excerpts and translations)

Quoted from the report; line breaks as extracted from the PDF.

```text
Clairambault 1161
Contents: Political notices concerning England and Flanders: English arms and the Tower, religious policy,
ships bound for Spain, Genoese lending, foreign courtiers, and a reported plan to force entry at Hampton
Court.
6/6 pages transcribed; 2/6 pages deciphered; 4 more in part
Ciphertext-only: No
Sender: Unidentified
Recipient: Unidentified
Year: Unestablished;1554/1555 remains a hypothesis
Key: 51 accepted forms: 38 letter signs, 11 nomenclature entries, 2 nulls, 39 provisional unidentified labels
Ciphertext: 3,149 elements, 3,046 identified; 5 further wordlike groups not classified
Plaintext in the margin or below: Matching historical plaintext in the margin of f163r, in the same
volume; the other five cipher faces have no established matching plaintext.
Gallica Selected pages f162r–f164v

Excerpt and Translation
Excerpt
f163r — complete eight-line cipher paragraph
Ce Seigneur a par deulx fois escript et mandé à ceste royne qu’elle laissast passer en silence et
dissimulation beaucoup de choses quant au faict de la religion en ce royaume afin de regaigner
sa noblesse et peuple, et que son filz et elle y puissent regner et commander en plus grand
repos.
Translation
This lord has twice written and sent word to this queen that she should let many matters concerning
religion in this kingdom pass in silence and dissimulation, in order to win back her nobility and
people, so that her son and she may reign and command there in greater peace.
```

## Links

- <https://gallica.bnf.fr/ark:/12148/btv1b90010063/f186.item>

## Images

- `lasry_p073_1.png`: George Lasry's image from the report (credit: George Lasry, BnF cipher research; manuscript © BnF via Gallica).
- Further images in the report, not copied here: p074_2.png.

## Spot-check (13 Oct 2026)

- Batch A. Image checked: https://gallica.bnf.fr/ark:/12148/btv1b90010063/f186.item
- Folio matches the report: yes; cipher present: yes
- What we checked: f162r (canvas 186) and f163v-164r (canvas 188, "Aultres advis") are all-cipher pages with signs matching his table (+, #, w-forms, 77=de, 76=le, 84, 52, /// null); no run decoded symbol by symbol; the f163r margin plaintext he cites was not on the canvases I fetched
- Verdict: **partly confirmed** (method key recovered based on adjacent plaintext, extent partial). The check is a sample, not a re-solution.
- Notes: Cipher is bound next to an unrelated 1707 certificate copy (f161v), so date and context depend on content only; 1554/55 (Mary Tudor, Hampton Court) is his hypothesis. Only 2/6 pages fully deciphered; 39 provisional labels.

## Verification 4, 23 Oct 2026

The profile marks this document read, but its texts entry names no file. The reading is George Lasry's ("BnF cipher
research", 10 Oct 2026); the repository holds only his entry with one excerpt and its translation (`lasry_entry.md`), and
NOTES, README and the folder give no fuller text. His decryption is his to publish, so the entry stays an **external
pointer** to his decipherment, with a note saying so; it is not scored or reviewed here.

## George Lasry's report PDF (24 Oct 2026)

Lasry sent his report on this item as a PDF (`lasry/report/27_clairambault-1161.pdf`), extracted with
`research/reading_audit/lasry_pdf_extract.py` into `lasry/report/` (summary, key image, excerpt and translation, the
full Readable text by folio). The page now shows it at the top. Measured: whole text 0.992 (v10_relabel.measure),
deciphered passages 0.909. His status: 6/6 pages transcribed; 2/6 pages deciphered; 4 more in part. Outcome: read in part. He translates the excerpt only
(`lasry/report/translation_excerpt.md`).

## Remaining gaps

- ff162r-164v: about 56 unread groups and 22 doubtful words in the deciphered runs; 39 provisional sign labels without value - blocker: no-key-material; only f163r has matching margin plaintext; his status: 2/6 pages deciphered, 4 in part.

## Escalation

- [x] siblings: the volume belongs to Lasry's BnF survey; no sibling key on DECODE known (24 Oct 2026)
- [x] clear-pages: the plaintext beside the cipher is the one he used (see his summary); no further decipherment known
- [x] known-keys: Lasry's reconstructed key is the only key; shown on the page
- [x] print: no edition of the deciphered passages known to this project (24 Oct 2026)
- [n/a] key-rebuild: the key reconstruction is George Lasry's, not this project's work
- [x] retry: his full Readable text (24 Oct 2026) read and measured; holes left as he marks them

## 14 Nov 2026: decryption listed in outcome.texts

The full-texts check (`docs/_texts.py`) reported "no decryption file" for George Lasry's entry: his Readable text by folio
(`lasry/report/readable.md`, extracted unedited from his report PDF of 24 Oct 2026; see `lasry/report/ATTRIBUTION.md`) was listed
only as the reading. It is now also listed as the entry's decryption. No text was changed and nothing was re-deciphered here.
His report status: 6/6 pages transcribed; 2/6 pages deciphered; 4 more in part. Still open: the transcription of the cipher itself, which is not in the
PDF or in this folder; it has been requested from George Lasry (`research/reading_audit/TRANSCRIPTIONS_WANTED.md`).
