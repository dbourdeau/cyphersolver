# Ambrogio Bizozola (Bizzozero) to Maximilian Sforza, Bologna, 4 November 1529: BnF fr. 3034 f. 156 (DECODE R4224)

Status: read in part

Catalogue item 176 (class C). DECODE R4224, "Non-decrypted", 4 pp., Italian, dated 1520/1529.

## The document

- BnF, Français 3034, ff. 156r–157v, no. 69 of the volume: "Lettre, en chiffre, d'AMBROSIO BIZOZOLA… allo…
  principe… Maximiliano Sforza". Four pages, wholly in cipher except the salutation ("Ill.mo mio sig.or sempre
  cordiall.mo"), the closing ("D. V. Ill.ma Ex.tia … sig.ria") and the signature ("Humil.e Ser.or Ambrosio
  Bizozola"). Address on f. 158v ("Allo Ill.mo et Ex.mo Principe Il S. Maximiliano Sforza … patron suo osser.mo
  … In Franza … Ala Corte").
- Digitised on Gallica: ark `btv1b90600370` (the SRU search `dc.source adj "Français 3034"` finds it; the BnF
  archives catalogue does not link it). Views: 246 = f. 156r, 247 = f. 156v, 248 = f. 157r, 249 = f. 157v,
  251 = address. Full-resolution natives (4153 × 6091) fetched with a browser User-Agent; images are not committed.
- Maximilian Sforza lived in France from 1515 until his death in Paris in 1530; the letter reports from Italy
  ("per le mie ultime di Cremona") on the Emperor's council and the duchy of Milan under his brother Francesco II,
  so it falls between 1521 and 1529. The last cipher lines of f. 157v give the date: "Bologna, quattro del ...
  novembre". f. 156v ll. 11-16 say the Emperor is tonight at the Certosa a mile from the town, "domane sara
  l'intrata", and that the cardinals and ambassadors (Venice, Milan) went out to meet him: Charles V's entry into
  Bologna was on 5 November 1529. So the letter is of 4 November 1529 (inferred from content; the year is not
  written).

## Prior work

- Tomokiyo, cryptiana `GL.htm`, section "Ambrosio Bizozola–Maximilian Sforza Cipher: BnF fr.3034", shows a key
  table headed "BNF Francais 3034-156 Italian, George Lasry 05/11/2023": a simple substitution A–V with five
  unidentified signs. The image is at `https://cryptiana.web.fc2.com/code/GL/BnF_fr3034_f156.png`
  (saved here as `tomokiyo_key.png`). No plaintext is published there or on DECODE (status still
  "Non-decrypted"). So the key existed before this attempt and was used; the text had not been published.
- Not searched in print beyond this (no edition of Maximilian Sforza's French correspondence found).

## The system

Letter substitution, one sign per letter, words separated by spaces, with a few homophones (Lasry's table plus
what the text forces):

| letter | sign(s) | code in `codes.txt` |
|---|---|---|
| a | ʒ (also stands for u/v: "aolte" = volte, "altime" = ultime, "daca" = duca) | 3 |
| c | short 9 with descender | c |
| d | 1 | 1 |
| e | ꝗ; in the postscript also a small cross | q (+) |
| f / s | ʃ (long s; serves both: "fatti", "consiglio") | f |
| i | 8 | 8 |
| l | ʓ (2 with a bar) | z |
| m | ε (and a variant ꞓ) | e |
| n | Γ | n |
| o | 11 / barred 11 | o |
| p | tall cross | + |
| r | T-shaped J | J |
| s | ɗ (loop with ascender) | d |
| t | long-loop g (not in Lasry's table as drawn; forced by "molte", "intese", "rotta") | g |
| u/v | 5-shaped sign | 5 |
| h, g, b, q | 6, 2, 7, Ꝗ as Lasry | 6 2 7 Q |
| - | ꝏ (Lasry "unknown"): only at line ends ("al duca ꝏ / di Savoia", "il duc ꝏ / Francesco"), a line-end filler | w |
| ? | ρ-like signs (Lasry "unknown"), only in the dating line f. 157v ll. 9-10 (probably the numerals) | X |

## Work done (21 Sept 2026)

1. Found the Gallica copy, located ff. 156-158 by contact sheet, fetched natives.
2. Cut every line (seg.py projection; verso pages re-cropped at x 1000-4050) and transcribed all four pages
   (66 lines) into shape codes by eye (`codes.txt`). `decode.py` applies the key; output in `reading_raw.txt`.
3. Homophones and the ꝏ filler established from the text (table above). Date fixed from content.

## What the letter says (summary)

- f. 156r: news gathered since the writer's last from Cremona; an informant "degno di fede" says the Emperor's
  council has several times discussed dividing the state of Milan: to the Duke of Savoy, the Marquis of
  Monferrato, the Marquis of Mantua, the Duke of Ferrara, and Milan to a duke; the Archbishop of Bari spoke.
- f. 156v: whether Duke Francesco would have to be satisfied and what the brother (Maximilian) should have;
  the writer has written to the Pope; the Emperor is at the Certosa, the entry is tomorrow, the cardinals and the
  Venetian and Milanese ambassadors went out to meet him and spoke with him on horseback.
- f. 157r: dealings with "misere Iulio", negotiation together with the Venetians, waiting to see whether the
  duke will come; Trivulzio; "subito voi haverete il capello"; a report through Rosso; the council.
- f. 157v: hope that the matter of misere Iulio turns out well and passes into the Pope's power; ten thousand
  scudi of income a year; date line Bologna, 4 November; clear closing and signature; cipher postscript: many
  days without letters from the recipient.

## Remaining gaps

- f. 157v ll. 9-10, the ρ-like signs in the date line (probably the day/year numerals) - blocker: too-short; two or three occurrences, no second context to fix a value.
- f. 157r ll. 7-8 and f. 157v ll. 3-4, words not resolved in the transcription (graded M/I in reading_raw.txt) - blocker: illegible; cramped ligatured signs on the Gallica scan, sign forms ambiguous at this resolution, no better image online.
- f. 156r l. 4 ("sofinigoci") and l. 16 (name after "Milano al duca") - blocker: illegible; same sign ambiguity.

## Escalation

- [x] siblings: the neighbouring leaves (views 240-251: f. 152-155 clear and Visconti items, f. 158 address) seen on a contact sheet; per Tomokiyo f. 154 is Visconti's cipher and f. 160 a clear copy of another letter; no clear copy of this letter found.
- [x] clear-pages: the address leaf (view 251) and the clear closing checked; no decipherment on the leaves.
- [x] known-keys: Lasry's key for this letter (Tomokiyo GL.htm) used; it reads, so no other key was needed.
- [x] print: Tomokiyo GL.htm read; no printed decipherment found.
- [x] key-rebuild: homophones t, a/u, f/s, e-cross and the ꝏ filler added from the text.
- [x] retry: second pass on the doubtful lines of f. 156v with the corrected key (reading improved from "aolte"/"altime" to volte/ultime, ꝏ resolved).
- Next: a higher-resolution image or the BnF original for the doubtful lines; Sanuto's Diarii for Nov 1529 to confirm the date and the partition talk.
