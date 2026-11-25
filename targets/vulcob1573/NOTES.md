# Charles IX → Jean de Vulcob, 7 March 1573, BnF Français 3318

Status: no write-up of our own (result by George Lasry, presented on docs/vulcob1573.html)

**24 Oct 2026, DECODE check** (Claude Opus 5.5): George Lasry's permission of 24 Oct 2026 covers his decryptions on DECODE. Searched the full DECODE record list (10,606 records, fetched 24 Oct 2026 with the project cookie) for this shelfmark (Français 3318): no record, so DECODE holds no decryption of it; his full text exists only in his BnF cipher research report files. The excerpt state is kept.

## Source

This result is George Lasry's, obtained with ChatGPT Astra 6 and Anthropic Opus 5.5 and reported in "BnF cipher research" (10 October 2026), which he sent to Daniel Bourdeau on 13 October 2026 for publication here. The transcription, the key and the reading are his. This repository only spot-checked one sample against the Gallica image (below); it did not re-solve the cipher.

## His metadata

- Report status: Transcribed; Deciphered
- Ciphertext-only: No
- Sender: Charles IX
- Recipient: Jean de Vulcob
- Date: 7 March 1573
- Key: 43 identified symbols, 39 letter signs, 4 in nomenclature
- Ciphertext: 754 elements, 746 identified; 4 groups with unresolved boundaries and 19 null-marked groups
- Contents: Instructions about the Polish royal election discuss Anjou, Archduke Ernest, rival candidates and reports from the Duke of Lorraine’s court.
- Method category (our classification): key recovered based on adjacent plaintext; extent: complete

## His entry, as sent (excerpts and translations)

Quoted from the report; line breaks as extracted from the PDF.

```text
Français 3318
Contents: Instructions about the Polish royal election discuss Anjou, Archduke Ernest, rival candidates and
reports from the Duke of Lorraine’s court.
Transcribed; Deciphered
Ciphertext-only: No
Sender: Charles IX
Recipient: Jean de Vulcob
Year: 7 March 1573
Key: 43 identified symbols, 39 letter signs, 4 in nomenclature
Ciphertext: 754 elements, 746 identified; 4 groups with unresolved boundaries and 19 null-marked groups
not included in these counts
Interlinear plaintext: Interlinear plaintext on the same page, f32r. ·
Key elsewhere: Comparison key in a different volume: Colbert 398; 14 shared letter forms.
Gallica Gallica source

Excerpt and Translation
Excerpt
f32r, complete cipher lines 13–15
…election l'archiduc Erneste, sont semblables a ceu? que le sieur de Tanneberg a tenuz a la
court de mon frere le duc de Lorraine sur ce fait et pourroit bien estre ?
Translation
…election, Archduke Ernest, resemble what the sieur de Tanneberg has said on this matter at the court of my
brother, the Duke of Lorraine, and it could well be ?.
```

## Links

- Related cipher: Ancel's letters of Oct-Dec 1577 in Colbert 398, in Tomokiyo's Vulcob-Ancel cipher (1575-1584), contributed by Harumi-Matsuba (issue #53), have their own folder and page: [`targets/ancel1577/`](../ancel1577/NOTES.md), `ancel1577.html`. Whether the 1573 cipher is the same was not established.

- <https://gallica.bnf.fr/ark:/12148/btv1b9060207j/f33.item>

## Images

- `lasry_p065_2.png`: George Lasry's image from the report (credit: George Lasry, BnF cipher research; manuscript © BnF via Gallica).
- Further images in the report, not copied here: p065_1.png, p066_3.png.

## Spot-check (13 Oct 2026)

- Batch A. Image checked: https://gallica.bnf.fr/ark:/12148/btv1b9060207j/f33.item
- Folio matches the report: yes; cipher present: yes
- What we checked: f32r "Monsr de Vulcob", cipher block with contemporary interlinear; the interlinear over the excerpt lines reads "election larchiduc ernestes ont semblables a ceux que ...", matching his "election l archiduc Erneste, sont semblables a ceu? que"; symbols not re-decoded independently
- Verdict: **confirmed** (method key recovered based on adjacent plaintext, extent complete). The check is a sample, not a re-solution.
- Notes: Interlinear decipherment on the same page covers the cipher, so this largely restates an existing decipherment. Dorsal on facing page "du Roy ... May" docket.

## George Lasry's report PDF (24 Oct 2026)

Lasry sent his report on this item as a PDF (`lasry/report/23_francais-3318.pdf`), extracted with
`research/reading_audit/lasry_pdf_extract.py` into `lasry/report/` (summary, key image, excerpt and translation, the
full Readable text by folio). The page now shows it at the top. Measured: whole text 0.957 (v10_relabel.measure),
deciphered passages 0.974. His status: Transcribed; Deciphered. Outcome: read. He translates the excerpt only
(`lasry/report/translation_excerpt.md`).

## Read share over cipher words only (16 Nov 2026)

README Conventions now count the read share over the words written in cipher. Lasry's Readable text (`lasry/report/readable.md`) marks the deciphered passages in bold and leaves the letter's clear text in plain type, so the bold words are the cipher words and the entry declares `cipher_markup: **`. Counted by hand over the bold text, with `v10_relabel.py` (dry run) as a cross-check of the holes: **181 cipher words (177 bold words plus the 4 bare `[?]` marks), 13 holes** (the four bare `[?]` marks after "longueur", "qui", "ont" and "estre", pro[?]z, and the words with bracketed or doubtful letters parei[l], l[e?], uou[d?], q[u]alite, Emp[ereur], ceu[x], escriue[z], sui[s]); each hole is one word, the bare marks being of unknown extent. Share 168/181 = **0.928**, under 0.95. (The tool's 189 is a count of letter-run tokens, which splits the nine bracketed words into pieces and each elision such as d'auoir in two, and gives 1 - 13/(189 + 13) = 0.936; the word count by the README rules is the one kept.): **read -> read in part**. Before: 0.957 over the whole text (clear included, not the measure) and 0.974 over the deciphered passages with only the 5 unread groups counted (the bracketed letters were not counted). Emp[ereur] is counted as a hole because the files do not show whether it expands a written abbreviation. The result is George Lasry's; nothing was re-deciphered here, and the class change rests on his own marks.

## Remaining gaps

- the four bare `[?]` marks and pro[?]z in Lasry's readable text and the eight words with bracketed or doubtful letters (parei[l], l[e?], uou[d?], q[u]alite, Emp[ereur], ceu[x], escriue[z], sui[s]) - blocker: not-attempted; this is Lasry's decipherment, not re-deciphered here, and the holes have not been tried against the Gallica image or the interlinear plaintext

## Escalation

- [n/a] siblings: not worked here; the result is Lasry's and the project did not re-decipher it
- [n/a] clear-pages: the letter's own clear text is the plain type of the readable text; no separate clear copy is recorded
- [n/a] known-keys: Lasry notes a comparison key in Colbert 398 sharing 14 letter forms; not tried here
- [n/a] print: not searched in this recount
- [n/a] key-rebuild: the key is Lasry's (43 identified symbols); not rebuilt here
- [n/a] retry: the holes were not retried here

