# Catherine de Médicis to Villeroy, Chenonceau 7–8 Feb 1581 (BnF fr. 15564 ff. 30–34; DECODE R4157)

Catalogue entry "Unknown sender (Villeroy) to unknown recipient, 5 Feb 1587". Session 2026-09-22.

Status: read. The one cipher block (f. 33r, 8 lines, 289 signs) is read in full: all 262 message signs read as
sense with Tomokiyo's reconstructed key, extended here by twelve values, and the other 27 signs are nulls or end
padding. The letter itself was already in print (1899). The cipher had been read at the time (margin decipherment)
and its key reconstructed by Tomokiyo, who could not read the end of the last line.

## Identification

- DECODE R4157 = BnF fr. 15564 ff. 30–34 (Gallica `ark:/12148/btv1b9064027v`, views 40–44; f. 33r = view 43 right).
  DECODE images P1–P4, P6, P7 are Gallica openings; P5 is a crop of the cipher block. P7 (f. 38) is a different
  letter ("Madame…", to Catherine), not part of this one.
- Docket (view 40 left): "Double de la lettre de la Royne mere du Roy à Mr de Villeroy du vııȷe febvrier 158[1]".
  **DECODE's "5 Feb 1587, unknown sender, unknown recipient" is wrong**: the sender is Catherine de Médicis, the
  recipient Nicolas de Neufville, seigneur de Villeroy, and the date is Chenonceau, 7 Feb 1581, with a postscript
  of 8 Feb and an autograph postscript by Catherine ("Je suys bien haybéye de set que ma dyst Beauvès-la-Nocque…").
- **In print:** *Lettres de Catherine de Médicis*, t. VII (1579–1581), ed. Baguenault de Puchesse (1899),
  pp. 349–353: "1581 — 7 et 8 février. Orig. Bibl. nat., fonds français 15564, f° 30. A Monsieur de Villeroy"
  (archive.org `lettresdecatheri07cathuoft`). Villeroy was in Guyenne with Anjou and Bellièvre, carrying out the peace
  of Fleix (Nov 1580). DECODE's 1587 comes from reading the docket's "1581" as "1587".
- The letter is in clear apart from one block of eight cipher lines on f. 33r. A second hand deciphered it at the
  time, in the left margin and on the three blank lines under the block. The edition prints that decipherment in
  place of the cipher, silently.
- **Tomokiyo** (cryptiana, "French ciphers during the reigns of Charles IX and Henry III", section BnF fr. 15564,
  "f.33"): "This letter, addressed to Villeroi, has several lines in cipher. The reconstructed cipher is as follows.
  (The last line cannot be read except for the first 'd.')" Key image saved as `lit/henryiii1.png`. He gives no
  plaintext and does not identify the letter. So the key existed before this session and a decipherment existed on
  the page. What was not done: a checked reading of every sign, the codes he left as "?", and the last line.

## Method

1. Found the letter in print by searching the Catherine volumes (t. IX first, from DECODE's 1587; then t. VII once
   the docket and the content, Anjou's sovereignty of the Low Countries and Condé's troops, pointed to 1581).
2. Transcribed the block from the Gallica native scan (4651 × 2118 crop of view 43), first pass `tokens_v1.txt`.
3. Without the key: a crib alignment against the printed text assuming one sign per letter with nulls (`em_align.py`,
   `sa_null.py`) failed (best 63 errors of 148). The printed text is only about half of the cipher: the rest of the
   decipherment is on the lines under the block, which I had first taken for the letter's clear continuation.
4. Found Tomokiyo's key. Mapping the first-pass labels onto it read the block at once. Then re-checked every
   disputed sign at 2× zoom and split merged labels: ψ forked = n vs ɣ curled = t; ᴀ filled = z vs Δ = f;
   ϖ = g vs ʊ-loop = s vs &-shape = z; ɦ = u vs б = e; small v = e vs large V = tout; ʒ bold = avec vs Ʒ barred = e;
   ɤ = ss; ıʔ is one sign (ɳ = r). The second pass is `tokens.txt`, the key `key.tsv`, and the reading `reading.txt`.

## Key (`key.tsv`)

Homophonic, one to three signs per letter, with a small nomenclator used even for syllables (*fi[de]lite*,
*[de]mourer*, *con[de]*, *[le]gation*). Values added to Tomokiyo's table: **18 = dict** (his "?"; *mon[dict]
filz*, *se [dict]*, *[le][dict] sieur*, *au[dict]*), **C̄σ = mais**, **ß̄ = la**, **ō = Angleterre** (M),
**4/b = nous** (he has "vous"; the text needs *que nous avez escript*, *mais nous ne laisserons*), ℬ = p, ꝏ = u,
ꝑ = t, ψ = n, ᴀ = z, & = z, F̣ = i, ϱ = l, d = x; nulls Ʒ+, ff, small raised hook, π̄.

## Reading (full text in `reading.txt`)

"…se dizant par deçà qu'il [the prince Dauphin] doibt aller en Flandres recevoir le serment de fidélité de ceulx des
Païs-Bas pour mon filz [Anjou], et qu'il y doibt demourer, et que le prince de Condé doibt mener les forces qui
s'assemblent, et faire tout ce qu'ilz pourront pour le service de mondict filz, qui se dict aussi y debvoir aller au
temps que nous avez escript, **et** non devant; mais nous ne laisserons **de** le nommer avec ledict sieur de
Montpensier audict pouvoir de la légation d'Angleterre."

The cipher differs from the printed text in three small places ("et non devant", "ne laisserons de le nommer",
"Monpensier"). It confirms the edition's wording otherwise.

## The tail of line 7

After "…legation d ō" come 20 signs: ꝛe Z7 ꝭ Ʒ+ ꝛ ꝭ ∂ ß ą̄ ꝛe Z7 π̄ ⊥ ꝭ ff Ʒ+ ne ꝭ Nz. They are end padding, for these reasons:
- the contemporary decipherer, who had the key, stops at "de la legation d'Ang[leter]re" and writes nothing more;
- f. 33v begins in clear with the next sentence, "Nous adviserons, aiant oy ledict La Fin…";
- the tail contains Tomokiyo's declared null Z7 twice, and the same Ʒ+, ff and small-hook signs that pad the start of
  the block before "doibt" (where the clear text has already written "qu'il");
- the signs in it that have letter values (a, l, mm, a, que) give no French.
Tomokiyo's "cannot be read except for the first d" is therefore right about the letters and wrong only in expecting
text: the "d" is the *d'* of *d'Angleterre*.

## Remaining gaps
- ō read as the code for "Angleterre" (it occurs once), graded M. It is required by the decipherer's "d'Ang…re" and
  by the edition. blocker: open-codes (single occurrence, no other key copy).
- "con[de]e": the latin e after the *de* code in *Condé* is either an e/é or a null. blocker: open-codes (single occurrence).
- "pouoi" at the end of line 6 lacks its r (an encipherer's omission, or the line-7 Z doing double duty).
  blocker: open-codes (single occurrence).

## Escalation
- [x] siblings: ff. 27, 78, 119, 142 (Guise → Mercœur) use a different key (Lasry); no other letter in this cipher found in fr. 15564.
- [x] clear-pages: the contemporary decipherment on the page (margin + three lines under the block) used as the check.
- [x] known-keys: Tomokiyo's reconstruction fits unchanged; 12 values added.
- [x] print: *Lettres de Catherine de Médicis* t. VII pp. 349–353 found and used.
- [x] key-rebuild: split merged labels at 2× zoom; every sign of the block has a value or a null role.
- [x] retry: last line re-read against the decipherment and f. 33v; tail explained as padding.
