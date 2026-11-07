# Méry de Vic → Henri IV, 28 August 1589, BnF Dupuy 61 — Méry de Vic, f43r

Status: in progress. Lasry's reading; the f. 43r cipher block decoded here 23 Oct 2026 with his key table, still below the reading bar.

**24 Oct 2026, DECODE check** (Claude Opus 5.5): George Lasry's permission of 24 Oct 2026 covers his decryptions on DECODE. Searched the full DECODE record list (10,606 records, fetched 24 Oct 2026 with the project cookie) for this shelfmark (Dupuy 61 — Méry de Vic, f43r): no record, so DECODE holds no decryption of it; his full text exists only in his BnF cipher research report files. The excerpt state is kept.

**23 Oct 2026, re-reading (REREAD_BRIEF, batch b30)**: Gallica views 85-100 opened (IIIF, openapi.bnf.fr): the letter is
ff. 40r-43v, all clear except one 16-line cipher block on f. 43r (view 95); no decipherment, gloss or clear copy nearby;
no DECODE record. The block decoded sign by sign with Lasry's table (`texts/f43r_cipher_decode.tsv`): both of his
excerpts reproduced; new: "qui a tousiours parle en … servit[e]ur de roy se change", "plusieurs qui soient ennemis de
la [?ligue] changent, qui prenent [?le] pretexte de la religion", "Ie [?les] contiens ce que ie puis", "… servira
beaucoup", "Et que les susdictz s'assemblent". The 13 Oct spot-check disagreement is two different passages, not an
error by Lasry. Partial reading `texts/f43r_reading.md` (English `f43r_en.md`, log `f43r_reread_log.md`): with the clear
text 0.667, the cipher passage alone 0.308 (holes-only 0.462): stays decoded, not read. 7 letters on look-alike
alternates; ꝗ = g and Ӿ = le(s) are sense-only, flagged for review.

**22 Oct 2026, reading audit** (George Lasry's test): both excerpts in lasry_entry.md have holes in every sentence and the report says "Partly deciphered": *decoded, not read* (excerpt only). Class already solved -> not read, method -> not solved; Lasry's ciphertext-only key recovery is recorded in method_basis; fraction_read 0.96 -> 0.

Earlier status (before the 22 Oct 2026 reading audit): no write-up of our own (result by George Lasry, presented on docs/meryvic1589.html)

## Source

This result is George Lasry's, obtained with ChatGPT Astra 6 and Anthropic Opus 5.5 and reported in "BnF cipher research" (10 October 2026), which he sent to Daniel Bourdeau on 13 October 2026 for publication here. The transcription, the key and the reading are his. This repository only spot-checked one sample against the Gallica image (below); it did not re-solve the cipher.

## His metadata

- Report status: 6/6 pages transcribed; Partly deciphered
- Ciphertext-only: Yes
- Sender: Méry de Vic
- Recipient: Henri IV
- Date: 28 August 1589
- Key: 81 symbols: 50 alphabet signs, 8 nomenclature signs, 3 nulls, 20 unidentified types
- Ciphertext: 545 elements, 523 identified (96.0%)
- Contents: Méry de Vic writes after the assassination of Henri III and the accession of Henri IV. The opening cleartext reports the arrival of the news and local allegiances. The cipher reports troops near Limoges and divided loyalties; later cleartext discusses expenses, elections, intercepted dispatches and cannon for rebel forts.
- Method category (our classification): key recovered from ciphertext-only; extent: partial

## His entry, as sent (excerpts and translations)

Quoted from the report; line breaks as extracted from the PDF.

```text
Dupuy 61 — Méry de Vic, f43r
Contents: Méry de Vic writes after the assassination of Henri III and the accession of Henri IV. The opening
cleartext reports the arrival of the news and local allegiances. The cipher reports troops near Limoges and
divided loyalties; later cleartext discusses expenses, elections, intercepted dispatches and cannon for rebel
forts.
6/6 pages transcribed; Partly deciphered
Ciphertext-only: Yes
Sender: Méry de Vic
Recipient: Henri IV
Year: 28 August 1589
Key: 81 symbols: 50 alphabet signs, 8 nomenclature signs, 3 nulls, 20 unidentified types
Ciphertext: 545 elements, 523 identified (96.0%)
Gallica f40r
Gallica f43r
Ciphertext-only

Excerpt and Translation
Excerpt
f43r
? assembler à huict lieues de ceste ville. Leur troupe ? au plus de douze cents hommes? de
pied? et deux cents chevaux et doivent meiner deux ou trois pieces.
Translation
? to assemble eight leagues from this town. Their force ? at most twelve hundred men? on foot? and two
hundred horsemen, and they must bring two or three guns.
Excerpt
f43r
? qui avoit tenu le feu Roy en esperance de le servir, s’est déclaré comme plusieurs du ? m’ont
asseuré. Il ? amas d’homes et se delibere de
Translation
?, who had kept the late King hoping to serve him, has declared himself, as several of ? have assured me. He
? a gathering of men and intends to
```

## Links

- <https://gallica.bnf.fr/ark:/12148/btv1b103164206/f89.item>
- <https://gallica.bnf.fr/ark:/12148/btv1b103164206/f95.item>

## Images

- `lasry_p004_1.png`: George Lasry's image from the report (credit: George Lasry, BnF cipher research; manuscript © BnF via Gallica).
- Further images in the report, not copied here: p005_2.png, p005_3.png.

## Spot-check (13 Oct 2026)

- Batch A. Image checked: https://gallica.bnf.fr/ark:/12148/btv1b103164206/f95.item
- Folio matches the report: yes; cipher present: yes
- What we checked: f43r: cleartext opening (Pompadour, Clermont Vertillac) + cipher block match his description; clear words between cipher runs read "...= roy q2 change come on ma asseure ... assemble aussi" whereas his excerpt gives "s est declare comme plusieurs du ? m ont asseure"; symbol-level decode not completed
- Verdict: **partly confirmed** (method key recovered from ciphertext-only, extent partial). The check is a sample, not a re-solution.
- Notes: Excerpt clear-text words do not exactly match the MS clear words (change come on ma asseure); 96% identified, status Partly deciphered; worth rechecking that excerpt line.

## Notes and corrections

One excerpt line disagrees with the manuscript. Lasry gives "s'est déclaré comme plusieurs du ? m'ont asseuré"; the clear words on f43r read "… roy q2 change come on ma asseure". The other clear words and the cipher block match. That line should be checked again.

## Remaining gaps

- f. 43r cipher: ~12 unread groups and 4 unidentified signs ([P], [A], [ʃ], [7]) - blocker: no-key-material; no value in Lasry's table (20 unidentified types); his full Readable text (report PDF, 24 Oct 2026) leaves them unread too. Decoded here 23 Oct 2026 (texts/f43r_cipher_decode.tsv).

## Escalation

- [x] siblings: not this project's reading; George Lasry's report covers the volume
- [x] clear-pages: ff. 40r-43v and neighbours opened 23 Oct 2026; the letter is clear apart from the f. 43r block; no decipherment
- [x] known-keys: Lasry's key is the key; his key table is not in the repository
- [x] print: Lasry's report (BnF cipher research, 10 Oct 2026) is the source
- [n/a] key-rebuild: not this project's work
- [x] retry: f. 43r block decoded sign by sign with Lasry's table (23 Oct 2026); next: ask Lasry for his decryption file
