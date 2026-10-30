# Napoleon III / Empress Eugénie (both directions) → Empress Eugénie / Napoleon III (both directions), June 1859, BnF NAF 11355 — Emperor–Empress code

Status: no write-up of our own (result by George Lasry, presented on docs/eugenie1859.html; his full report text extracted 24 Oct 2026)

**24 Oct 2026, DECODE check** (Claude Opus 5.5): George Lasry's permission of 24 Oct 2026 covers his decryptions on DECODE. Searched the full DECODE record list (10,606 records, fetched 24 Oct 2026 with the project cookie) for this shelfmark (NAF 11355 — Emperor–Empress code): no record, so DECODE holds no decryption of it; his full text exists only in his BnF cipher research report files. The excerpt state is kept.

**22 Oct 2026, reading audit** (George Lasry's test): the token table of ff. 9r, 15r, 17r, 18r, taken in order, builds French sentences, and the three report excerpts (ff. 19r, 35r, 27r) read; both are *excerpts* of Lasry's reading, whose full text is not in the repository. Krajcovic's corrections file is *not prose*. fraction_read 0.841 (Lasry's identified elements) -> about 0.31, what the repository shows.

Earlier status (before the 22 Oct 2026 reading audit): no write-up of our own (result by George Lasry, presented on docs/eugenie1859.html)

## Source

This result is George Lasry's, obtained with ChatGPT Astra 6 and Anthropic Opus 5.5 and reported in "BnF cipher research" (10 October 2026), which he sent to Daniel Bourdeau on 13 October 2026 for publication here. The transcription, the key and the reading are his. This repository only spot-checked one sample against the Gallica image (below); it did not re-solve the cipher.

## Verification by Jozef Krajčovič (issue #39, 16 Oct 2026)

Jozef Krajčovič (GitHub kjfriedo) re-read f9r, f15r, f17r and f18r by hand, then applied Lasry's key; he says
plainly this is not a ciphertext-only re-solution. Crib and control pages f19r, f27r, f29r, f30r, f35r; negative
control f21r-v (headed Emperor to the War Ministry: values above the Emperor-Empress range, no French under this
key, so a different nomenclator). Agreements, for example f15r 1155 1113 660 1244 199 *sans résistance*, f18r 195
1265 563 608 888 *Castiglione*, f27r/f30r 1333 30 785 1342 *va à merveille*.

Proposed corrections to the token transcription (not applied here; the transcription and key are Lasry's, and the
list goes to him): f9r 1143 -> 1193 (501 419 1193 = expr-[419]-sion, so 419 = es); f18r 1268 -> 1265 (1265 = ti,
also in fa-ti-gue); f15r 1115 -> 1155; f17r 839 -> 889 and 353 -> 355; provisional f9r 1200 = sort (*en sortant
avec le roi*). He would keep f17r 1325 = une. His package (token streams, a verification script, page locators) is
attached to the issue.

He also pointed out that the page said "Extent: complete" against 9 of 11 cipher pages deciphered; the profile class
was corrected to read in part on 21 Oct 2026.

## Lasry's answer to the proposed corrections (22 Oct 2026)

George Lasry checked each proposal against his final transcription and key (10 Oct 2026) and against the Gallica
images of f9r and f17r. No change to his transcription or key follows. His token streams for the four pages are in
`lasry_tokens_f9_f15_f17_f18.tsv` (code, value, confidence, as in his working files).

- Already in his transcription: f9r 1193 = sion, f18r 1265 = ti, f15r 1155 = sans, f17r 889 = ons and 355 = der.
  The values these were to replace (1143, 1268, 1115, 839, 353) are not in his transcription or his key.
- f9r *expr-es-sion* is 501 **459** 1193, not 419. The middle digit is the scribe's long ʃ-shaped 5, as in 515,
  54 and 598 on the same page. 459 = es also sits in the alphabetical run 453 er, 457 er, 459 es, 462 esp; 419
  would fall before 425 em.
- f9r *en sortant avec le roi* is 432 **1210** 85 126 708 1132; 1210 = sort is in his key. The image shows 1210
  twice, in the struck-out first line and in the clean line. Not 1200.
- f17r line 2 begins **151**, not 751: the first stroke is the hooked 1 of 1232 on the line, not the barred 7 of
  753 and 708. His key has 151 = bataille (between 142 bai and 160 bien), so the passage reads *nous espérons une
  bataille sur Chiese*. That keeps 1325 = une, as Krajčovič suggested, and removes the anomaly of *une main*.
- f17r ends 237 **868** (*Min-ci-o*), not 808 (808 = mon in his key).
- Other differences in the token streams: f9r line 4 (ink blot) has 751? 717? 515 in his reading against ?51 773
  518; f15r, in the unread tail, 925 and 656 against 935 and 616 (not re-checked against the image); the header
  numbers 753 (f15r) and 1098 (f17r) are outside his cipher streams; 329 is his marked code 329z.
- He agrees that f21r-v uses a different nomenclator.
- Checked here (22 Oct 2026) against his TSV: 1193, 1265, 1155, 889, 355, 459 = es, 1210 = sort, 151 = bataille and
  868 = o all occur on the folios he names; 1143, 1268, 1115, 839, 353, 419, 1200, 751 and 808 do not. The images
  were not re-checked here.

## His metadata

- Report status: 15/15 pages transcribed; 9/11 cipher pages deciphered; 2 more in part
- Ciphertext-only: Yes
- Sender: Napoleon III / Empress Eugénie (both directions)
- Recipient: Empress Eugénie / Napoleon III (both directions)
- Date: June 1859
- Key: 233 codes, 12 letter signs, 220 in nomenclature, 1 separator
- Ciphertext: 440 elements, 370 identified (84.1%); 4 assumed readings; 50 ?
- Contents: Napoleon III’s policy toward the Pope, his criticism of diplomatic speculation, and reports from the Italian campaign; private family news exchanged with Empress Eugénie.
- Method category (our classification): key recovered from ciphertext-only; extent: partial

## His entry, as sent (excerpts and translations)

Quoted from the report; line breaks as extracted from the PDF.

```text
NAF 11355 — Emperor–Empress code
Contents: Napoleon III’s policy toward the Pope, his criticism of diplomatic speculation, and reports from the
Italian campaign; private family news exchanged with Empress Eugénie.
15/15 pages transcribed; 9/11 cipher pages deciphered; 2 more in part
Ciphertext-only: Yes
Sender: Napoleon III / Empress Eugénie (both directions)
Recipient: Empress Eugénie / Napoleon III (both directions)
Year: June 1859
Key: 233 codes, 12 letter signs, 220 in nomenclature, 1 separator
Ciphertext: 440 elements, 370 identified (84.1%); 4 assumed readings; 50 ?
Literal plaintext: f35r: L’ennemi s’est retiré cette nuit. — One ciphered sentence only; fatigue passage not
printed. · L’Écho saumurois, 28 June 1859, p. 1 ·
Gallica ff3r–5r
Gallica f9r
Gallica ff14r–15r
Gallica ff17r–19r
Gallica f27r
Gallica ff29r–30r
Gallica ff32r–35r

Excerpt and Translation
Excerpt
f19r — the Pope and diplomacy
Je suis bien peiné au milieu de mes travaux d’avoir à répondre à toutes les sotte[s] suppositions de
la diplomatie. Je maintiens le pape à Rome avec mon armée. Je ne me mêle en rien du reste de
ses États.
Translation
I am very distressed, amid my work, to have to answer all the foolish suppositions of diplomacy. I keep the
Pope in Rome with my army. I do not interfere in any way with the rest of his States.

Excerpt
f35r — the battle and the Austrian emperor’s room
Impossible de donner des détails sur la bataille d’hier. Tout [le] monde était mort de fatigue. L’ennemi
s’est retiré cette nuit. J’ignore le nombre précis de canons, de drapeaux et de prisonniers. J’ai couché
cette nuit dans la chambre où l’Empereur d’Autriche a déjeuné hier matin. Niel est nommé Maréchal. La
bataille prendra le nom de Solférino.
Translation
It is impossible to give details of yesterday’s battle. Everyone was dead tired; the enemy withdrew during the
night. I do not know the exact number of cannon, flags and prisoners. I slept last night in the room where the
Emperor of Austria had breakfast yesterday morning. Niel has been appointed Marshal. The battle will be
named Solferino.

Excerpt
f27r — Eugénie’s message
Je suis désolée de vous avoir fait de la peine, ce n’était? pas mon intention. Ne vous inquiétez
pas du petit, il va à merveille. J’écris aujourd’hui par la poste.
Translation
I am sorry to have caused you sorrow; that was not? my intention. Do not worry about the little one; he is
doing wonderfully. I am writing today by post.
```

## Links

- <https://archives.ville-saumur.fr/_depot_amsaumur/_depot_arko/fonds/echo_saumurois/pdf/1859/FRAC049328_ECHSAU_1859_06_28.pdf>
- <https://gallica.bnf.fr/ark:/12148/btv1b52517729k/f11.item>
- <https://gallica.bnf.fr/ark:/12148/btv1b52517729k/f23.item>
- <https://gallica.bnf.fr/ark:/12148/btv1b52517729k/f33.item>
- <https://gallica.bnf.fr/ark:/12148/btv1b52517729k/f39.item>
- <https://gallica.bnf.fr/ark:/12148/btv1b52517729k/f57.item>
- <https://gallica.bnf.fr/ark:/12148/btv1b52517729k/f61.item>
- <https://gallica.bnf.fr/ark:/12148/btv1b52517729k/f67.item>

## Images

- `lasry_p027_2.png`: George Lasry's image from the report (credit: George Lasry, BnF cipher research; manuscript © BnF via Gallica).
- Further images in the report, not copied here: p026_1.png, p028_3.png, p029_4.png, p030_5.png.

## Spot-check (13 Oct 2026)

- Batch A. Image checked: https://gallica.bnf.fr/ark:/12148/btv1b52517729k/f67.item
- Folio matches the report: yes; cipher present: yes
- What we checked: f32r = Solferino telegram "Cavriana 24 juin 1859, Empereur a Imperatrice", clear text + code "941 325 274 1155 / 163 1142 1162"; his key gives 274=connais, 163=ble, 1142=s (fragmentary, no excerpt covers this run); f19r/f35r excerpts not image-checked
- Verdict: **partly confirmed** (method key recovered from ciphertext-only, extent partial). The check is a sample, not a re-solution.
- Notes: 84.1% identified, 50 ?; 2 cipher pages only in part. Telegrams of 1859 were partly printed in the press (he cites L Echo saumurois 28 June 1859) - external plaintext available for f35r.

## 23 Oct 2026: verification 3 (explicit-hole score)

The v3 sweep scored the Lasry-tokens entry on `lasry_tokens_f9_f15_f17_f18.tsv` itself (one value per row; 0.0): the
entry had no reading file. Lasry's values are now divided into words per folio in
`texts/eugenie1859_f9_f18_reading.md` (letters no value carries bracketed, his "?" tokens as [?]): 0.625 explicit-hole
(5/8 sentence windows), plain 0.5, the unknown words being the place names. ff. 9r, 17r, 18r and the first sentence
of 15r hold; the end of 15r is a run of tokens without values. Keeps read, barely.

## Verification 5, 23 Oct 2026

Plain-bar check (French 1859). `texts/eugenie1859_f9_f18_reading.md`: plain 0.5, explicit 0.625; two of the failing
windows fail only on place names (Chiese, Mincio, Lonato, Castiglion), the real hole is the unvalued run at the end of
f. 15r. Keeps read. The report-excerpt file had been scored with its English and page furniture (plain 0.488); the
French excerpts alone are now `texts/eugenie1859_lasry_excerpts_reading.md`, plain 1.0; keeps read.

## George Lasry's report PDF (24 Oct 2026)

Lasry sent his report on this item as a PDF, extracted with `research/reading_audit/lasry_pdf_extract.py` into `lasry/report/` (summary, key image, excerpt and translation, the full Readable text by folio). The page shows it at the top. Measured: whole text 0.982 (v10_relabel.measure), deciphered passages 0.948 (bare ? counted as unread). His status: 15/15 pages transcribed; 9/11 cipher pages deciphered; 2 more in part. Outcome: read in part.

## Lasry's update: f. 15r read, codebook revised (30 Oct 2026)

George Lasry sent a new version of his report, in French (`lasry/report/08_naf-11355-emperorempress-code_fr.pdf`,
made with the help of Claude Opus 5.5). It starts with the partial reconstruction of the codebook, then gives each
folio cropped to the telegram sheet, its decryption with the enciphered parts in bold, and a note on its context.

- f. 15r, the run left without values, now reads: 677 1074 310 925 357 381 708 81 1099 123 495 656 257 914 439 =
  *Je re-cueille partout des do-lé-ances relatives aux exact-ions commises par l'ennemi.* Each new value falls in
  the alphabetical order of the codebook between its neighbours (310 cueille between 297 cou and 318 dans, 925
  partout between 916 parait and 926 pas, 381 do between 379 dites and 398 du, 81 ances between 65 al and 85 ant,
  1099 relatives between 1094 regard and 1109 répond, 123 aux between 122 aut and 124 av, 495 exact between 494 ex
  and 501 expr, 656 ions between 649 intention and 660 is, 257 commises between 255 comment and 262 compensé).
- f. 15r: the group transcribed 981 is 381 on the image (981 would fall between 978 posi and 996 pre, where *do*
  cannot stand). `lasry_tokens_f9_f15_f17_f18.tsv` is updated.
- Eleven readings lose their question mark, each checked against the alphabetical order and the sense: 116 aura,
  151 bataille, 1232 sur, 233 402 1162 Chiese, 773 284 mécontents, 771 matérielle, 482 1074 étrangère, 357 886
  désolée, 1044 qui, 622 il a, and the marked codes 329z Autrichien and 1102z Sardaigne.
- Still uncertain: *dictature* in f. 19r needs 1216 = tu, which breaks the alphabetical order (1216 lies between
  1210 sort and 1226 sui); *Légations* and 980z *Piémont* in f. 19r; *officiers* in f. 29r.
- The multi-group header lines (f. 5r 865 442 163 824 204 543 225; 163 455, 163 723 on ff. 29r, 32r, 35r) are not
  deciphered: of the f. 5r line only 163 is in the codebook, and 163 opens all these lines, so they are probably a
  separate coded header.
- The codebook now has 242 groups (12 single letters). It is in `lasry_key.csv` (code, value; status read, uncertain
  or assumed) and, as a page image, in `lasry/report/images/key_1.png`. `lasry/report/readable.md` follows the new
  version; the first PDF is kept.

## Remaining gaps

- the cipher pages: unread groups between the deciphered runs - blocker: no-key-material; left as George Lasry marks them; no other key or plaintext known; his decipherment is the only one
- 2 of 11 cipher pages, deciphered in part: not transcribed or deciphered in full in Lasry's report - blocker: no-key-material; his report status says so; outside this project's work, no other key or plaintext known

## Escalation

- [x] siblings: neighbours belong to George Lasry's BnF survey; no sibling key found here
- [x] clear-pages: the report's pages and the manuscript on Gallica checked against his text; no further decipherment held
- [x] known-keys: Lasry's reconstructed key is the only key; shown on the page
- [x] print: no edition of the unread passages found
- [n/a] key-rebuild: the key reconstruction is George Lasry's, not this project's work
- [x] retry: his full Readable text (24 Oct 2026) read and measured; holes left as he marks them
