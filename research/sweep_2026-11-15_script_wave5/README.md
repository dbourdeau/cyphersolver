# Script wave 5 (15 Nov 2026): Omont Saint-Germain I/II, route probes

Result: **0 rows merged, 0 promoted.** No candidates.json (nothing met even the lead fields with an image seen).

## Routes found
- Omont Saint-Germain français (fr. 15370-20064) OCR is on archive.org as Google scans: `cataloguegnrald00manugoog` (tome I, 15370-17058, 1.7 MB)
  and `cataloguegnrald01manugoog` (tome II, 17059-18676); fetch with `curl -L archive.org/download/<id>/<id>_djvu.txt`.
  `p2catalogue01/02`, `p2catalogueg02/03` are the Ancien Supplement (fr. 6171-15369), already covered. NAF I (1-3060) has no archive.org item.
  `fz.py` is a fuzzy-OCR cipher-word extractor with nearest-heading attribution.
- Gallica ark from a shelfmark: Gallica SRU and texteBrut are 403 (Cloudflare) to curl; openapi.bnf.fr has no SRU. Manifests
  (`openapi.bnf.fr/iiif/presentation/v3/ark:/12148/<ark>/manifest.json`) answer at 3 s, label = shelfmark. ARK check character = NOID
  (alphabet 0123456789bcdfghjkmnpqrstvwxz, weights from 1, no prefix), so arks can be generated for a number but their order is
  not tied to shelfmarks (`mf.py A B` prints label for btv1b<A..B>). Mapped: fr. 15550-15565 = btv1b9064033k..9064026f (descending),
  15571 = 90618802, 15572 = 9061879d, 15573 = 90618780, 15597 = 9061877k, 15903/15904 = 9064052x/9064051h. fr. 15566-15570 not found.

## What Omont I/II show
Almost all "chiffre" mentions are key sheets ("Chiffres des depeches", Bellievre fr. 15912, 15999-16001; Maisse 16092; Cesy 16150;
Gueffier 16913), or "chiffrees, avec dechiffrement" (Revol, Du Val de Stors, fr. 16911-16912; Benlivoglio 18001-18019): not eligible.
Only undeciphered ciphertext mentions: Bellievre recueil fr. 15566 f. 50, 15567 ff. 24 and 158 ff., 15568 ff. 151 and 207 (Matignon,
Bellievre-Hautefort), 15571 f. 34 (Chasteauneuf), 15572 ff. 58, 115, 283 (Chasteauneuf), 15572 ff. 110, 123 (already catalogue 12).
Checked on the image: fr. 15571 view 38 (Omont f. 34) is plain French with a few marks; the cipher block is at views 41-42 (f. 37, Oct 1585,
sign cipher, no decipherment on or beside it). fr. 15572 views 63-66 and 121-124 (Omont ff. 58, 115) show clear text: Omont folios unreliable.
Not made into leads: arks for 15566-15568 unknown, prior art (Tomokiyo, Lasry Mayenne/Matignon keys, DECODE) not searched, Omont folios unconfirmed.
Next step for whoever has Chrome: SRU `dc.title all "Francais 15567"`, then page fr. 15566-15568, 15571 ff. 34-37, 15572 ff. 55-64, 280-295.

## Probed, no new route (curl from this network)
APE 403, Finna 403, DDB API 403, Archives Hub 403, Kalliope SRU no connection; Arkivportalen, Europeana demo key, TNA Discovery answer but were swept
(see `sweep_2026-11_malta_nordic_baltic`, `europeana`, `tna_discovery`); TNA WO 1/WO 32/FO 27/CO 5 are described by folio range, no cipher text to search.
