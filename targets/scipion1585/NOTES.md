# Scipion de Gonzague (Français 4696); not established for Français 4698 → Duke of Nevers (Français 4696); not established for Français 4698, 1585–1589 (Français 4696); 1590 (Français 4698), BnF Français 4696 / 4698 — graphical cipher, ff5r/62r–v, ff30r– 31r and f104r

Status: no write-up of our own (result by George Lasry, presented on docs/scipion1585.html)

**24 Oct 2026, DECODE check** (Claude Opus 5.5): George Lasry's permission of 24 Oct 2026 covers his decryptions on DECODE. Searched the full DECODE record list (10,606 records, fetched 24 Oct 2026 with the project cookie) for this shelfmark (Français 4696 / 4698 — graphical cipher, ff5r/62r–v, ff30r–): no record, so DECODE holds no decryption of it; his full text exists only in his BnF cipher research report files. The excerpt state is kept.

22 Oct 2026, reading audit (George Lasry's test: can sentences be built and translated?): the repository holds only
his three-line excerpt of f62v, which reads with two `?` and has his translation (reviewed B in `profile.json`). His
37.3% of elements identified is key coverage, not a reading figure; his report says most of the letters are only
deciphered in part. `fraction_read` 0.373 -> about 0.02 (held text that reads, estimated). Nothing relabelled
decoded, not read: the rest of his decryption is not here to grade.

## Prior art (found 16 Nov 2026, issue #708)

Paolo Rosson's folder `gonzaga-1590` (<https://github.com/pangoleen/cipher-readings/tree/main/gonzaga-1590>, page
<https://pangoleen.github.io/cipher-readings/gonzaga-1590.html>; text CC BY 4.0, tables MIT; made by a model, no
palaeographer has checked it, by his own README) covers the same cipher for the Français 4698 letters. Brice Dudout
reported it in issue #708 on 16 Nov 2026. What it holds, as read in a clone here on 16 Nov 2026:

- Period decipherments by Nevers's clerk of 1590, in BnF fr. 4702 (Gallica `btv1b530546654`; his Credits name the clerk
  for three letters): ff. 94r-95r are the decipherment of fr. 4698 ff. 30r-31r (letter of 21 Jan 1590); f. 97r-v of
  f. 104r (the sheet sent with the letter of 16 Feb 1590); f. 108r of fr. 4698 f. 34r (aligned only, not transcribed).
  A further decipherment of f. 17r-v is on fr. 4698 f. 105r itself, in the same volume; his folder does not name its
  author and it is not in fr. 4702. He links them (his record: first found 3 Oct 2026), transcribes ff. 94r-95r and
  f. 97r-v (`decipherments_1590/`), and edits and translates two of them
  (`editions/edition_1590-01-21_f30.txt`, `editions/edition_1590-02-16_f104.txt`; 49 units where he preferred the
  cipher to the clerk's word, each needing a second reader).
- A rebuilt code: a one-part word code of two-digit figures in 14 lists told apart by marks (448 glossed values,
  `tables/lists_v4.tsv`), a symbol alphabet of about 45 signs and a verb sign.
- A test on fr. 4696 (the other volume of this folder, same cipher, Oct 1586 on), run with his earlier table of 378 values, built before that volume was seen: of 587 units transcribed, 463 have their word in the table, and for 452 of those (97.6%) the gloss on the page is the table's word (word and mark both agree for 408, 88.1%); a shuffled table gives 2 of 572. The 448-value table was built afterwards. "Agrees" here is agreement with the gloss written on the page, not independent confirmation of the reconstruction.
- The sender of the fr. 4698 letters: Cardinal Scipione Gonzaga, Rome, to Nevers (21 Jan, 16 and 19 Feb, 24 and 31 Mar
  1590), by his record. Lasry's report says "not established" for fr. 4698.

Dates: his git commits are dated 3-4 Oct 2026 (first commit `79a4d26`, 3 Oct 13:56 +0100). Git dates are the author's
own; the push dates could not be read (the GitHub API for his repository was not available to this session). The
project's own harvest `research/cryptoole/candidates.md`, headed 14 Oct 2026, already lists his page (row FR1586-3)
with "Already here" left blank: it was public by 14 Oct at the latest, and we did not match it to this folder then.
Lasry's report (10 Oct, received 13 Oct) does not cite Rosson or fr. 4702, so nothing in the record shows he used it; whether his models had seen Rosson's page is not known. His report itself names period material
for fr. 4698 ("worksheets on f26r/f93r and the f17v/f105 comparison"); whether that is the fr. 4702 / f. 105r material
Rosson aligns is not checked here. Lasry's report thus uses the f. 17v / f. 105 comparison, the same fr. 4698 gloss material Rosson starts from; readers should weigh that when judging independence.

Checked here, 16 Nov 2026 (model checks only, no person):

- `tables/lists_v4.tsv` has 448 data rows in 14 lists (A, BR, C, E, G, I, M, N, O, P, PT, Q, S, T).
- The fr. 4696 figure (with the 378-value table) adds up: 452 = 387 agree + 21 same word in another form + 44 word agrees, mark differs, from his
  `fr4696/agreement_table.md`. The shuffle test was not rerun.
- Gallica fr. 4702 f. 94r (IIIF via openapi.bnf.fr) is a clear Italian decipherment in a clerk's hand, with struck
  dictionary forms, and its first lines match his transcription.
- His edition of 21 Jan 1590 contains the run Lasry reads on f. 30v ("richiedermi ... che ... prieghi": "a richiedermi
  finalmente che io prieghi V.E."). One other run, Lasry's f. 30r "andava smar?end?", stands where the clerk has
  "andava spargendo"; the two differ in letters, so this is not an agreement, and it is not decided here.
- Image check from issue #708: fr. 4696 f. 5r (Gallica view 11) carries the interlinear period decipherment above the
  cipher.

Not checked: the unit-by-unit alignments (`alignment/`), the symbol alphabet and verb sign, the shuffle test, whether
Lasry's 24 nomenclature values are a subset of Rosson's lists, the fr. 4698 "Da Parigi" docket reading, whether Lasry's
f. 104r marked codes agree with the clerk's f. 97r-v, and the unread groups of fr. 4696 ff. 5r, 62r-v against his
fr. 4696 glosses. No cipher-words-only re-measure of the read share was made; the figures below stay Lasry's, as measured
on 24 Oct 2026.

What this changes here: this folder claims no decipherment of its own, so nothing is withdrawn. It presents Lasry's
report, which is now one of two readings of the fr. 4698 pages, the other being the clerk's of 1590 as edited by Rosson.
The statements corrected: "no other key or plaintext known", "his decipherment is the only one", "no edition found", and
the sender of fr. 4698 as not established.

## Source

This result is George Lasry's, obtained with ChatGPT Astra 6 and Anthropic Opus 5.5 and reported in "BnF cipher research" (10 October 2026), which he sent to Daniel Bourdeau on 13 October 2026 for publication here. The transcription, the key and the reading are his. This repository only spot-checked one sample against the Gallica image (below); it did not re-solve the cipher.

## His metadata

- Report status: 2/7 pages transcribed; 5 more in part; 7/7 pages deciphered in part
- Ciphertext-only: No
- Sender: Scipion de Gonzague (Français 4696); not established for Français 4698
- Recipient: Duke of Nevers (Français 4696); not established for Français 4698
- Date: 1585–1589 (Français 4696); 1590 (Français 4698)
- Key: 66 symbols/codes: 41 letter signs, 1 digraph, 24 in nomenclature
- Ciphertext: 3,078 recorded groups, 1,147 identified; 8 further groups with unresolved boundaries
- Contents: Confidential warnings and cavalry arrangements: horses, payments, dispatches and service in war. The Français 4698 fragment contains a request for an appeal or intercession; most of that letter remains unread. The Paris letter of16 February1590 discusses friendship, the King of Spain and a request; its substantial gaps remain unread. 2/7 pages transcribed; 5 more in part; 7/7 pages deciphered in
- Method category (our classification): key recovered based on adjacent plaintext; extent: partial

## His entry, as sent (excerpts and translations)

Quoted from the report; line breaks as extracted from the PDF.

```text
Français 4696 / 4698 — graphical cipher, ff5r/62r–v, ff30r–
31r and f104r
Contents: Confidential warnings and cavalry arrangements: horses, payments, dispatches and service in
war. The Français 4698 fragment contains a request for an appeal or intercession; most of that letter remains
unread. The Paris letter of16 February1590 discusses friendship, the King of Spain and a request; its
substantial gaps remain unread.
2/7 pages transcribed; 5 more in part; 7/7 pages deciphered in part
Ciphertext-only: No
Sender: Scipion de Gonzague (Français 4696); not established for Français 4698
Recipient: Duke of Nevers (Français 4696); not established for Français 4698
Year: 1585–1589 (Français 4696); 1590 (Français 4698)
Key: 66 symbols/codes: 41 letter signs, 1 digraph, 24 in nomenclature
Ciphertext: 3,078 recorded groups, 1,147 identified; 8 further groups with unresolved boundaries
Interlinear plaintext: Français 4696, f5r: interlinear plaintext for this cipher.
Interlinear plaintext: Français 4698: corresponding historical enciphering/plaintext worksheets on
f26r/f93r and the f17v/f105 comparison support the checked f104r marked codes.
Gallica Français 4696 f5r
Gallica Français 4696 ff62r–v

Excerpt and Translation
Excerpt
f62v, three complete body lines5–7
giudico ? il aiutarle. Quanto poi a la persona sva egli si ?ferisce prontisimo a servirla et
particolar[men]te in caso di difesa o vero di esaltatione di lei, fuor di questi ? solo de sua salute,
ri[gu]ardo al interesse
Translation
…helping you. As for his own person, he [offers?] himself very ready to serve you, especially in defending or
advancing your position. Apart from these matters, ? only his welfare, with regard to the interest…
```

## Links

- <https://gallica.bnf.fr/ark:/12148/btv1b9059540q/f11.item>
- <https://gallica.bnf.fr/ark:/12148/btv1b9059540q/f127.item>

## Images

- `lasry_p051_1.png`: George Lasry's image from the report (credit: George Lasry, BnF cipher research; manuscript © BnF via Gallica).
- Further images in the report, not copied here: p052_2.png.

## Spot-check (13 Oct 2026)

- Batch A. Image checked: https://gallica.bnf.fr/ark:/12148/btv1b9059540q/f127.item
- Folio matches the report: yes; cipher present: yes
- What we checked: Fr. 4696 f62r: Italian letter "Ill.mo et Ecc.mo S. mio" with clear text (Padre Toledo, Giulio Cesare, Pasqua) and Greek-like graphic cipher runs; excerpt is from f62v, not imaged here; sign-level decode with his table not completed (glyph forms at this scan only loosely match his crops)
- Verdict: **partly confirmed** (method key recovered based on adjacent plaintext, extent partial). The check is a sample, not a re-solution.
- Notes: Only 1147/3078 groups identified (37%); 4698 letter mostly unread. Interlinear on f5r gave the key. Two volumes/senders bundled in one entry.

## George Lasry's report PDF (24 Oct 2026)

Lasry sent his report on this item as a PDF, extracted with `research/reading_audit/lasry_pdf_extract.py` into `lasry/report/` (summary, key image, excerpt and translation, the full Readable text by folio). The page shows it at the top. Measured: whole text 0.849 (v10_relabel.measure), deciphered passages 0.689 (bare ? counted as unread). His status: 2/7 pages transcribed; 5 more in part; 7/7 pages deciphered in part. Outcome: read in part.

## Remaining gaps

- Français 4698 ff30r-31r, 104r: Lasry's unread groups between his deciphered runs - blocker: open-codes; the plain text exists (the clerk's decipherments, fr. 4702 ff. 94r-95r and f. 97r-v, edited by Rosson), but no unit-by-unit comparison of Lasry's Readable text with Rosson's alignment tables has been made here, so which of Lasry's holes the clerk's text fills is not recorded; for ff. 30r-31r the fr. 4702 text is also an independent reading of the same cipher
- Français 4696 ff5r, 62r-v: unread groups between Lasry's deciphered runs - blocker: open-codes; Rosson's table (448 values, 14 lists, tested on fr. 4696) has not been run against Lasry's holes here, and whether Lasry's 24 nomenclature values are a subset of it is not checked
- 5 of 7 pages transcribed in part, all 7 deciphered in part: not transcribed or deciphered in full in Lasry's report - blocker: no-key-material; the key sheet of the cipher is not known; Rosson's table is a reconstruction by a model, unchecked by a person, and his own README lists microfilm limits for fr. 4698

## Escalation

- [x] siblings: neighbours belong to George Lasry's BnF survey; the sibling letters of fr. 4698 (ff. 17r-v, 34r, 26v-27r, 36r-37r) and their period decipherments in fr. 4702 f. 108r and fr. 4698 f. 105r are Rosson's, listed in his README; not read here
- [x] clear-pages: the report's pages and the manuscript on Gallica checked against his text; the period decipherments of fr. 4698 ff. 30r-31r and f. 104r are in fr. 4702 ff. 94r-95r, 97r-v (found 16 Nov 2026, issue #708); f. 94r seen on Gallica
- [x] known-keys: Lasry's reconstructed key and Rosson's table of 448 values (a reconstruction by a model, not a period key sheet) are the keys known; Tomokiyo's Nevers key no. 35 (fr. 3995 f. 64) is the key the project's catalogue named for this volume, and Rosson reports it gives a value for 11 of 28 figures on fr. 4698 f. 17r and no Italian (his README, not re-tested here)
- [x] print: DECODE list searched (no record, 24 Oct 2026); Rosson's README (3 Oct 2026) reports no printed edition of these letters and says the printed BnF catalogue lists the fr. 4702 decipherments as letters of "un agent du duc de Nevers" without linking them (not checked here)
- [n/a] key-rebuild: the key reconstruction is George Lasry's and Paolo Rosson's, not this project's work
- [x] retry: his full Readable text (24 Oct 2026) read and measured; holes left as he marks them; not re-run against Rosson's tables
