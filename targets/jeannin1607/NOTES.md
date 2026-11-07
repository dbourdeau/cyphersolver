# Villeroy; Henri IV → Pierre Jeannin and fellow envoys, 1607, BnF Français 3516 — Villeroy / royal cipher

Status: in progress (ff87v-88r, ff112v-116v still to transcribe and decipher with Lasry's 110-symbol key)

**24 Oct 2026, DECODE check** (Claude Opus 5.5): George Lasry's permission of 24 Oct 2026 covers his decryptions on DECODE. Searched the full DECODE record list (10,606 records, fetched 24 Oct 2026 with the project cookie) for this shelfmark (Français 3516 — Villeroy / royal cipher): no record, so DECODE holds no decryption of it; his full text exists only in his BnF cipher research report files. The excerpt state is kept.

## Source

This result is George Lasry's, obtained with ChatGPT Astra 6 and Anthropic Opus 5.5 and reported in "BnF cipher research" (10 October 2026), which he sent to Daniel Bourdeau on 13 October 2026 for publication here. The transcription, the key and the reading are his. This repository only spot-checked one sample against the Gallica image (below); it did not re-solve the cipher.

## His metadata

- Report status: 2/15 pages transcribed; 2 more in part; 2/15 pages deciphered; 2 more in part
- Ciphertext-only: No
- Sender: Villeroy; Henri IV
- Recipient: Pierre Jeannin and fellow envoys
- Date: 1607
- Key: 110 symbols: 35 letter signs, 74 in nomenclature, 1 repetition sign.
- Ciphertext: Transcribed passages: 1,145 elements, 1,099 identified
- Contents: Instructions on negotiations with England and the United Provinces, support for Prince Maurice, and the choice between peace and a truce with Spain.
- Method category (our classification): key recovered based on adjacent plaintext; extent: partial

## His entry, as sent (excerpts and translations)

Quoted from the report; line breaks as extracted from the PDF.

```text
Français 3516 — Villeroy / royal cipher
Contents: Instructions on negotiations with England and the United Provinces, support for Prince Maurice,
and the choice between peace and a truce with Spain.
2/15 pages transcribed; 2 more in part; 2/15 pages deciphered; 2 more in part
Ciphertext-only: No
Sender: Villeroy; Henri IV
Recipient: Pierre Jeannin and fellow envoys
Year: 1607
Key: 110 symbols: 35 letter signs, 74 in nomenclature, 1 repetition sign.
Ciphertext: Transcribed passages: 1,145 elements, 1,099 identified
Interlinear plaintext: Interlinear plaintext at ff86r–86v and112r.
Gallica ff86r–88r
Gallica ff112r–116v

Excerpt and Translation
Excerpt
f86r, cipher lines8–11
comme à tous ceux qui affectionnent ceste union, sans toutefois par trop vous fonder ou confier
aux belles parrolles de son agent, ny des autres qui penchent de son coste, car ilz sont tous
trompeurs. Mais si nous
Translation
as to all those who favour this union, without however relying too much on or trusting the fine words of his
agent or of the others who lean to his side, for they are all deceitful. But if we
```

## Links

- <https://gallica.bnf.fr/ark:/12148/btv1b9059630p/f148.item>
- <https://gallica.bnf.fr/ark:/12148/btv1b9059630p/f192.item>
- <https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b9059630p/f148/full/1600,/0/default.jpg> — image checked in the spot-check

## Images

- `lasry_p084_1.png`: George Lasry's image from the report (credit: George Lasry, BnF cipher research; manuscript © BnF via Gallica).
- Further images in the report, not copied here: p085_2.png.

## Spot-check (13 Oct 2026)

- Batch B. Image checked: https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b9059630p/f148/full/1600,/0/default.jpg
- Folio matches the report: yes; cipher present: yes
- What we checked: f86r cipher lines 8-11: contemporary interlinear reads "comme a tous ceux qui affectionnent ceste union sans toutesfois par trop vous fonder ou confier aux belles parolles de son agent ny des autres qui penchent de son coste car ilz sont tous trompeurs Mais si nous" = his excerpt; no own sign-by-sign decode (key table not checked)
- Verdict: **confirmed** (method key recovered based on adjacent plaintext, extent partial). The check is a sample, not a re-solution.
- Notes: Only 2/15 pages deciphered (+2 in part). Interlinear on ff86 and 112. Jeannin negotiations 1607 printed (Negociations du president Jeannin, 1656) - likely in print.

## Notes and corrections

Probably printed in Jeannin's Négociations (1656; 1875 edition); the two siblings in Fr. 3516 (berny1607, laboderie1608) are.

## George Lasry's report PDF (24 Oct 2026)

Lasry sent his report on this item as a PDF (`lasry/report/33_francais-3516-villeroy-royal-cipher.pdf`), extracted with
`research/reading_audit/lasry_pdf_extract.py` into `lasry/report/` (summary, key image, excerpt and translation, the
full Readable text by folio). The page now shows it at the top. Measured: whole text 0.986 (v10_relabel.measure),
deciphered passages 0.968. His status: 2/15 pages transcribed; 2 more in part; 2/15 pages deciphered; 2 more in part. Outcome: read in part. He translates the excerpt only
(`lasry/report/translation_excerpt.md`).

## Remaining gaps

- ff86r-87r, f112r: 10 unread groups, 3 doubtful words (1,099 of 1,145 elements identified) - blocker: no-key-material; interlinear plaintext only at ff86r-86v and 112r.
- ff87v-88r, ff112v-116v: not transcribed or deciphered in his report (11 of 15 pages) - blocker: not-attempted; his 110-symbol key exists, so these pages can be transcribed and deciphered here.

## Escalation

- [x] siblings: the volume belongs to Lasry's BnF survey; no sibling key on DECODE known (24 Oct 2026)
- [x] clear-pages: the plaintext beside the cipher is the one he used (see his summary); no further decipherment known
- [x] known-keys: Lasry's reconstructed key is the only key; shown on the page
- [x] print: the sampled passages are in the 1656, 1819 and 1875 editions of Jeannin's Négociations (see Passage verification and key additions; the 24 Oct 2026 entry here said no edition was known)
- [n/a] key-rebuild: the key reconstruction is George Lasry's, not this project's work
- [x] retry: his full Readable text (24 Oct 2026) read and measured; holes left as he marks them

## Passage verification and key additions

A sign-by-sign collation of selected passages adds six corroborated values to Lasry’s chart. On f. 87r the cipher and contemporary gloss preserve a negative omitted by the 1656, 1819 and 1875 editions. On f. 116v the cipher gives *leurs navires* where the checked editions print *les navires*. The proposed value of barred 90 remains provisional. The sampled wording on f. 113r matches the 1875 text. Contemporary glosses are also visible beyond the leaves identified in the original report.

See the [contribution note](CONTRIBUTION_NOTE.md), [cipher transcription](TRANSCRIPTION.txt), [French readings, alignments and English translations](PLAINTEXT.md), [key additions](key_additions.md), [source locations](SOURCES.md) and [Python verifier](verify.py). This evidence covers the listed passages and comparisons. The original report’s document-level coverage figures still refer to Lasry’s work.
