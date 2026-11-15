# Omont leftovers on Gallica (15 Nov 2026, wave 6)

Brief: find the arks for BnF fr. 15566-15568 and look at the Omont leftover cipher folios named in `sweep_2026-11-15_script_wave5/README.md`.
**Result: 5 leads (2838-2842), all promoted (vetting blocks in `research/leads.json` -> `catalogue.json`).** `make_candidates.py` and `apply_vetting.py` rebuild them.

## Routes
- **Gallica SRU works in Chrome** from a tab on gallica.bnf.fr: `fetch('/SRU?operation=searchRetrieve&version=1.2&query=' + encodeURIComponent('gallica all "Français 15567" and dc.type all "manuscrit"'))`
  (plain `dc.title all "Francais 15567"` returns 0). Arks: fr. 15566 = btv1b9063929g, 15567 = btv1b90639282, 15568 = btv1b9063927n (15571 = 90618802, 15572 = 9061879d from wave 5).
- The images then come by curl from `openapi.bnf.fr/iiif/image/v3/ark:/12148/<ark>/f<view>/full/700,/0/default.jpg` (a view is a double-page spread; the right page carries the folio).
  View offsets: fr. 15566 view = f. + 11, fr. 15567 view = f. + 5 or 6, fr. 15568 view = f. + 8, fr. 15571 view = f. + 4.

## What the images and the prior art show
- **fr. 15566 f. 50** (Turin(?), 3 Oct 1582, one page of sign cipher with clear postscript): seen, but **already solved by Lasry** (GL.htm "A Letter in BnF fr.15566", preliminary solution, 2022). Not a lead; read from existing decipherment.
- **fr. 15567 f. 24, ff. 158-164; fr. 15568 ff. 151-152, 207-208; fr. 15571 f. 37**: seen, no full decipherment on or beside them. Tomokiyo's page (`henryiii.htm`) reconstructs the tables
  (Matignon's Cipher-1: fr. 15567 ff. 24, 54, fr. 15568 f. 151; Hautefort's Cipher: fr. 15567 ff. 158, 160, fr. 15568 f. 207; Chasteauneuf's Cipher: fr. 15571 ff. 34-36) but prints no reading of these texts. Leads 2838-2842, key_held = his table, untested.
- **fr. 15572 ff. 277-279**: three pages of cipher, but Tomokiyo and the repo (`matignon1586/NOTES.md`, Cipher-3) record ff. 277-278 as deciphered in ff. 279-280 (the clear letter at view 289-290). Not a lead.
- **fr. 15572 ff. 58, 115** (wave 5: clear text) and ff. 110, 123 (catalogue item 12): nothing new. fr. 15571 f. 34 is the Chasteauneuf letter deciphered in f. 36 (Tomokiyo).
- Writers and dates of 2840, 2841, 2842 were not read from the leaves (Omont and Tomokiyo attributions only).
