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

## OeNB retry (leads 2832-2837), same day
onb.digital, data.onb.ac.at/dtl and digital.onb.ac.at all end at onb.digital (504 to curl, browser error page); viewer.onb.ac.at/DTL_<id> loads but its manifest API
(`api.onb.ac.at/iiif/presentation/v3/manifest/DTL_<id>`) answers 504 or "Fehler 500" for every id tried (4865249 and three others); iiif.onb.ac.at does not connect. Nothing was viewed.
P.Vindob. A.P. 11016 (lead 2832) is not in the ONB list of published Arabic papyri and no description exists beyond Karabacek's 1894 guide; the record calls it "unpubliziert". Lead 2832 stays a lead (retry when the ONB API is back).
Lead 2835 (Eugene of Savoy, Autogr. 14/61-15): the filed "Transskription" is taken as a decipherment, so the lead is closed `read` / decipherment_filed.
Bellievre papers fr. 15890-15911: Omont text only (see COVERAGE).
