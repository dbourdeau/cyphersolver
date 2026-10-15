# Gramont to Montmorency, Rome, 11 October 1529 (BnF fr. 3091 no. 23; catalogue item 6, Gramont's cipher 1529)

BnF fr. 3091 no. 23, ff. 45r-47v (Gallica btv1b9060253s, canvases 49-52). Session of 18 Sept 2026.

**Split on 14 Oct 2026** under the one-key rule (George Lasry): catalogue item 6 grouped four letters to
Montmorency in four different keys. This folder keeps only the letter in **"Gramont's cipher (1529)"**. The others
are different ciphers, each with its own page:
- Langeac, Venice, 14 Jan 1529, fr. 3083 no. 8 ("Avranches' cipher 1"): `targets/langeac1529/`, `docs/langeac1529.html`.
- Gramont, Rome, 21 July 1530, fr. 3071 no. 7 ("Gramont's cipher (1530)"): `targets/gramont1530/`, `docs/gramont1530.html`.
- Mâcon, Rome, 11 Apr 1537, fr. 3071 no. 4 ("Mascon's cipher"): moved to `targets/rome1536/fr3071_no4/` with the
  cardinal's fr. 3053 letters in the same key (`docs/rome1536.html`); `macon_key.md` and `macon_decode.py` moved to
  `targets/rome1536/`.
Shared source material stays here: `GL.htm` and `francis.htm` (saved copies of Lasry's and Tomokiyo's pages), the
Gallica tools (`thumbs.py`, `full.py`, `crop.py`, `sheet.py`) and `AGENT_BRIEF.md`.

## The key

All four keys of item 6 were reconstructed by George Lasry in 2023 (tables dated 05/11/2023 on Tomokiyo's page
cryptiana.web.fc2.com/code/GL.htm). This letter's key is his "Gramont's cipher (1529)", built from the siblings
fr. 3040 f. 16 and Clair. 330 f. 53 (copies in `img/`). **Neither site gives any plaintext** ("only the decipherment
keys are displayed"), so the task was reading the letter, not breaking the cipher. Lasry also decoded the letter in
2023 when he reconstructed the key, but never published the decipherment (his correction of 21 Sept 2026).

fr. 3091 is the Raince volume, filmed as two-page openings, so canvas numbers do not follow folios.

## Result

* `fr3091_no23_gramont.md`: **read in full**. The letter runs to 171 cipher lines (ff. 45r-47v), each page 90-95 %
  confident, with per-page line tables in `f45r_transcription.md` … `f47v_transcription.md` and the glyph aliases in
  `aliases/f45r.txt` … `f47v.txt` (4,002 signs, 37 distinct alias characters, 12 `?` unidentified signs; measured
  14 Oct 2026). Year 1529 fixed by Clement VII's departure from Rome for Bologna, the bull of the four décimes, and
  Orange before Florence. Gramont vouches for the Pope's secret alignment with France. Clement dreads the general
  council and plans to grant it in principle and then stall it; he offers to feign illness on the road to wait for
  the Admiral Chabot; he fears soothsayers who foretell his deposition or death "du costé de" the Emperor, and had a
  dream before leaving Rome (enclosed). Orange is dealing to restore the Medici in Florence against Pisa and Livorno
  going to the Emperor. Code signs: heart = the King; several unlisted signs = the Emperor, the Florentines, the
  Pope/Medici (from context). `#` is A as often as M; the ♀-on-foot sign is a null.

Doubtful: single letters on each page (listed in the transcriptions), *fier ni a nui* (f. 45r), *en voi[e]*
(f. 45v), the first word of f. 47v l. 7, and the identity of the four code signs, inferred from context.

Prior art still to look at: B. Wirtz-Daviau's edition of Chabot's 1529 embassy (may quote Gramont's letters from a
contemporary decipherment).

## Assumptions for George's review

- His prior-solution credit on this entry rests on his note of 21 Sept 2026 that he decoded all four item-6 letters
  in 2023; it is kept on each of the four split entries, each for its own letter and key.
- The key-or-decipherment credit is for his "Gramont's cipher (1529)" table only; his other three item-6 tables are
  credited on langeac1529, gramont1530 and rome1536.

## Site

Written up as `docs/gramont1529.html` (18 Sept 2026; narrowed to this letter on 14 Oct 2026).

## Tools

`thumbs.py` (Gallica thumbnails), `sheet.py` (contact sheet), `full.py` (full-res canvases, 8 s spacing, back-off
on 429), `crop.py` (fractional crop + autocontrast), `decode.py` (Gramont 1529 alias decoder;
`python decode.py < aliases/f45r.txt`). f46r uses a few extra alias characters of its own, explained in
`f46r_transcription.md`. Raw images in `full/` are not tracked (main checkout only).
