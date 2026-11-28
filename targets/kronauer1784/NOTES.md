# kronauer1784 — Kronauer's Masonic album, OeNB Cod. Ser. n. 4832

Lead: catalogue 2836 (Daniel Bourdeau, OeNB deep sweep). Album ('Stammbuch für einen Freimaurer', Johann Georg Kronauer), Vienna 1783-91, II+82+1 leaves, 110 x 166 mm; contributors include Mozart (fol. 41r), Gemmingen, Born, Alxinger, Blumauer, Ratschky (Nettl 1957).

## Images
ONB IIIF manifest https://api.onb.ac.at/iiif/presentation/v3/manifest/1004802B (188 canvases, about 1050 px wide). Canvas index (0-based) 64 = fol. 28r; 56 = fol. 24r; 70 = fol. 31r; the member register = canvases 160-169 (written across the page). The manifest has no rights statement (attribution to the ONB only), so no image is copied here.

## fol. 28r — this target
A German text of 75 words with heading, place/date and signature, written in invented letters that look like Georgian Mkhedruli. The Georgian sound values are not used: it is a plain substitution.

Glyph inventory (codes of transcription_f28r.txt; '+X' = the enlarged capital form):
| code | shape | letter |
|---|---|---|
| U | small cup | e |
| J | short stroke curling left below the line | i |
| N | arch with hooked left foot | n |
| A | plain arch | d |
| R | small double loop (omega) | r |
| S | '3' with a descending loop | s |
| Z | '3' with a top flourish | z |
| Y | '5'-like | z (zur, zu) |
| H | plain figure 8 | h |
| T | figure 8 with a top-right flourish | t |
| E | schwa | a |
| O | small round o | u |
| Q | small loop with a tail | o |
| B | '6' | b and p |
| L | tall '(' | l |
| C | reversed c | c |
| K | lambda-like | k |
| G | cup with a long descending loop | g |
| M | cup with a short tail | m |
| V | tall round 0 | v |
| W | flat oval | w |
| F | looped l | f |
| y | like S | y (freye) |
| +D +E +N +P +M +K +G +F +T +R +S +W +Q | enlarged capitals | D A N P M K G F T R S W O |

Spelling: ä ö ü = ae oe ue; no q ('bekuem'); 'Pallast', 'Republick', 'Thun', 'freye'.

## Method and checks
- Pass A: transcription and hand solve by word patterns ('Kinder sind Kinder', 'Mutter ist Mutter', -er endings, 'sich', 'macht'), then the key read the whole page.
- Pass B, blind: a separate agent with only the image and crops, no hint on language or content, built its own glyph table and reached the same key and text. Differences: seinen/einen (line 7), gehöret/gehört (line 6), first word of the signature not read; arbitrated on the image as in reading_f28r.md.
- No pre-registered held-out test: about 400 signs, the only text in this system in the album, and the key was built on the whole page. 75 words of continuous German lie far beyond the unicity distance of a simple substitution (about 30 letters). validation.tsv (418 tokens, 37 types, model de-1740s) is ready for docs/_validate.py; not run by the contributor (no numpy).
- Prior art: catalogue 2836 vetting (DECODE, Tomokiyo, Lasry, Nettl, Mozart documents) and this repository: no reading of the cipher entries.

## Other cipher entries in the album (not read)
- fol. 31r (25 Sep 1784): 'Hier liegt der Hund begraben … Seinem Freund und B.: gewidmet von' + a name of 5 + 7 square signs (pigpen family with inner strokes, not the dotted standard pigpen) + 'L.: M.: der ☐ …, K.K. Börse u. Wechsel Censal'.
- fol. 24r: three short vertical lines of angle, triangle, circle-dot, cross and division signs, beside a drawing of an obelisk.
- fol. 37r, 51r (Epstein von Ankersberg's signature), 78v: not yet located among the canvases.
