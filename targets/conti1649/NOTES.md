# Prince de Conti's ciphered mémoires, 26–27 March 1649 (BnF fr. 3854 nos. 41–42)

Split on 14 Oct 2026 under the one-key rule (George Lasry, 14 Oct 2026). This entry used to hold nos. 41–43; no. 43,
Conti's mémoire for Laigue of 5 March 1649, is a numeric letter-and-syllable code with its own key and now has its
own entry: [`targets/laigue1649/`](../laigue1649/NOTES.md), page `laigue1649.html` ("a different cipher, with its own
page"). `READING43.md` and `n43/` moved there. The image list below still names canvases 245–251 (no. 43) because
the IIIF manifest and the git-ignored images stay in this folder in the main checkout.

Catalogue item 26. Worked 18 Sept 2026. **Status: read.** First deciphered by Lasry (2023). Re-deciphered independently here from my own transcription; see READING.md.

## Where the items are

Gallica ark `btv1b52520094g` (fr. 3854; the paper calls it "3584", a typo).

| Omont no. | Folio | Canvas | What it is |
|---|---|---|---|
| 41 | f. 113r–v | 237–238 | "A Paris ce 26 Mars 1649", letter cipher mixed with clear words |
| 42 | f. 115r | 241 | "A Paris ce 27 Mars 1649", same cipher, signed *Armand de Bourbon* |
| 43 | ff. 119ff. | 245–251 | three-digit figure code (e.g. 229, 375, 416, 347), deciphered letter by letter between the lines ("l'archiduc", "la paix", "le cardinal") |

## Verify-first answer: no, nos. 41–43 do not share a cipher

Nos. 41 and 42 are written in lower-case letters. No. 43 is a numeric code on three-digit figures. So no. 43's
decipherment is not a crib for 41–42. It did not need to be.

## Prior art

George Lasry, "Armand de Bourbon's Poly-Homophonic Cipher – 1649", *HistoCrypt 2023* (Linköping ECP),
<https://ecp.ep.liu.se/index.php/histocrypt/article/view/699>. The PDF is saved here as `lasry2023.pdf`. The
cipher was brought to light by Camille Desenclos (Lachenicht & Braun 2021, p. 87).

- He deciphered both letters in full; the text is printed in §4 with an English translation.
- The addressee is probably Noirmoutier (the letter opens "Affin que Monsieur Le Monsieur de Noirmo[u]stier sache…").
- The cipher has no nomenclator. It is homophonic for A (J/a), L (u/v) and R (d/o), and polyphonic for five signs:
  a = T/P/A/B, e = E/G, i = C/Z, m = S/D/X, n = M/Q.
- The key's second row spells *J'aime c'est un grand mal*, a Boesset air de cour of 1642.

## Checked here

- The images match the paper's Figures 1 and 8 sign for sign where compared (f. 115 lines 1–3, f. 113r opening).
- `check_key.py` runs the final key over my hand copy of Figure 8. **234 of 237** cipher/plain pairs fit the key.
  The three misses and four length mismatches are slips in my copy of the figure, not problems with the key.
- **Independent decipherment.** I transcribed all three pages from the images myself (`transcription.txt`) and decoded
  them with the key (`decode.py`, then word-level rescoring in `decode2.py` → `decoded.txt`). The normalized text is in
  `READING.md`. It agrees with Lasry's §4 throughout and adds small corrections: *ne* pouvant; *pour insister* à
  demander in no. 42; the B⟨l⟩etaigne slip. Details are in READING.md.
- "Monsieur de *Tenerande*" (f. 113r, ll. 16–17): the cipher is `a ẽ g ı ∂ J g m e`. In this hand `ı` is the E sign,
  so it reads TENERANDE, as Lasry has it. An earlier note of mine, "TENCRANDE", misread that sign and is withdrawn.
  The person is still unidentified.
- "dix(six?) mil hommes": m = S/D/X is genuinely ambiguous. The ciphertext cannot settle it.

## Files

- `check_key.py`: the key-consistency check.
- `lasry2023.pdf`: the paper.
- `manifest.json`: the Gallica IIIF manifest.
- The images are not in the repo (see `.gitignore`). To re-fetch full resolution, use
  `https://gallica.bnf.fr/iiif/ark:/12148/btv1b52520094g/f{237,238,241,245..251}/full/full/0/native.jpg`.

## No. 43

Moved to `targets/laigue1649/` on 14 Oct 2026 (different cipher).

## Measured (14 Oct 2026)

`measure_4142.py`: 1,692 cipher signs outside the clear words in `transcription.txt`, 3 illegible; 1,689 of 1,692
have a value under Lasry's key (99.8%).

## Assumptions for George's review

- Credit: George is credited with the prior solution of nos. 41–42 (HistoCrypt 2023: key and full text) and with the
  key applied here; nothing on no. 43, whose code is unrelated to his key.
- The addressee is taken as "probably Noirmoutier" from his paper; the page's recipient portrait is Louis II de La
  Trémoille, marquis de Noirmoutier, on that basis.
