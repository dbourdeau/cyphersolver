# Screen log (canvas = one microfilm opening unless noted). Detector hits = det.py score >= 20, each viewed as a native-scale crop.

## fr. 15905, second ark btv1b9063808z (363 canvases, ff. c. 330-680, 1579-80)
- Page sheets (pagesheets.py) read for canvases 5-87: all clear.
- Detector: 363 scored, 76 hits viewed (crop sheets), all clear French/Italian/Latin text (italic and small dense hands,
  microfilm targets c0002, c0362). c0023 left: pen trials on an address panel, not cipher. c0198 (f. 520v-521): clear letter, Nov 1579.
- Result: no cipher seen.

## fr. 15905, first ark btv1b90638227 (341 canvases, ff. 1-c. 330, 1578-79)
- Detector: 341 scored, 25 hits viewed, all clear (italic hands, Italian letter c0238, autograph postscripts, film targets).
- Result: no cipher seen.

## fr. 15911, btv1b52521582d (907 canvases, colour, one page per canvas, ff. 1-c. 450; 1590, 1597-99)
- Detector at scale 0.5 (rank.py <dir> 24 0.5; first 136 canvases at threshold 16): 907 scored, 254 hits viewed as crops.
- Contact sheets (sheets.py, 8x4, 195 px) read for canvases 470-693 (ff. 233-343, the Vervins correspondence, Feb-May 1598).
- CIPHER FOUND, three originals of Henri IV (signed Henry, countersigned de Neufville) to Bellièvre and Sillery at Vervins,
  passages in a figure-letter-sign cipher (two-digit numbers 61-99, letters, +, #, dotted signs), no interlinear or marginal
  decipherment (the margin notes are a later hand's summaries of the clear text):
  - c0483-c0491 (ff. 238-242): cipher on c0489 (f. 241r, c. 5 lines) and c0490 (f. 241v, 4 lines). Letter of 14 March 1598.
  - c0569-c0577 (ff. 281-285): cipher on c0572 (f. 282v, c. 5 lines), c0575 (f. 284r, c. 9 lines), c0576 (f. 284v, c. 5 lines),
    c0577 (f. 285r, c. 6 lines). Letter of 9 April 1598 (Angers).
  - c0611-c0615 (ff. 302-304): cipher on c0611 (f. 302r, c. 14 lines), c0612 (f. 302v, nearly the whole page, c. 30 lines),
    c0615 (f. 304r, 10 lines). Letter of 14 April 1598 (Nantes).
  All three are PRINTED IN CLEAR from the Court's copies: Mémoires et correspondance de Duplessis-Mornay, t. VIII (1824),
  archive.org mmoiresetcorresp08morn (14 March: pp. 162-175, the enciphered passage on the château d'If is on p. 173-174;
  9 April: pp. 290-304; 14 April: pp. 317-320). So they are not open: known-plaintext material, listed in not_candidates.json.
- Everything else viewed is clear (French, Italian, Spanish, Latin, German-hand letters; Spanish intercepts c0071-c0087 in clear).

## fr. 15904, btv1b9064051h (480 canvases, microfilm openings, ff. 1-463; 1576-77)
- Detector: 480 scored, 63 hits viewed, all clear (French, Latin, one Italian notarial act c0450; Casimir/Condé affair).
- Result: no cipher seen.
