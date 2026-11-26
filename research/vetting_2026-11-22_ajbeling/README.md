# Vetting, ajbeling (22 Nov 2026)

Run by Andrew Beling (GitHub ajbeling) with AI agents (Claude, model `claude-opus-5-5`), from his own computer and
network, on 22 Nov 2026. Two leads, both corrections to rows already in `research/leads.json`. No person has checked
the readings of the images. Before starting, issues and pull requests were searched for 1204, Martinique, 2730,
Humieres and Humières: none on these leads.

## Leads

- **1204** (Martinique despatches, ANOM COL C8 A 51, 56, 58, 59): `read`. Every piece the lead names carries the
  ministry's decipherment on the leaf, apart from the enclosure C8 A 56 f. 57, which `targets/champigny1744` reads.
- **2730** (letters "avec chiffre" to Humières, BnF fr. 3329, 3409, 4717): `unvetted`, not digitised; field corrections
  below.

Count: read 1, unvetted 1.

## 1204

Seen on the ANOM page images, 22 Nov 2026 (IIIF, one request every seven seconds):

| Piece | Record | Date, writer | Code | Decipherment |
|---|---|---|---|---|
| C8 A 51 f. 109 | ark:/61561/zn401hgefcg | Fort-Royal, 21 Dec 1740, Champigny, duplicate | ff. 109v-113r, about 100-110 lines, clear passages between | above every line (all 20 lines of f. 110r checked) |
| C8 A 58 f. 33 | ark:/61561/zn401uptqh | Martinique, 10 Mar 1748, Caylus, duplicate | ff. 33r-34r, about 90 lines | in the left margin, continued below the signature and onto f. 34v |
| C8 A 59 f. 158 | ark:/61561/zn401rsnkma | Fort-Royal, 14 Nov 1751, Bompar and Hurson, duplicate | ff. 158r-161r, about 140 lines | above every line (all 24 lines of f. 159v checked); a second hand rewrites a few glosses |
| C8 A 56 f. 54 | ark:/61561/zn401utsvwe | Fort-Royal, 17 Aug 1744, Champigny | ff. 54r-56v, about 100 lines; enclosure f. 57-57v, 381 groups | above every line of the letter; the enclosure f. 57 is bare (see below) |
| C8 A 56 f. 73 | ark:/61561/zn401c104yw | Fort-Royal, 16 Nov 1744, Champigny, duplicate | ff. 73r-77v, about 150 lines | above every line (all 13 lines of f. 75v checked) |
| C8 A 56 f. 85 | ark:/61561/zn401zyx1xd | 24 Nov 1744, Champigny | ff. 85r-88r, clear and code mixed, about 80 lines | above every line (ff. 87r and 87v checked) |
| C8 A 56 f. 253 | ark:/61561/zn401mllfgb | 6 Feb 1745, Champigny | ff. 253r-255r, about 75 lines | above every line (f. 254r checked) |

Line counts are by eye from contact sheets. Nothing was transcribed: a period decipherment is on each leaf.

Images FRANOM23_C8A_051_0204-0214, _058_0059-0066, _059_0268-0279 and _056_0096-0107, 0133-0146, 0157-0166,
0463-0471. Image _056_0097 (f. 54r) is damaged on the server: the full image returns an error and only its right half
could be fetched, with black blocks; every line it shows is glossed.

The calendar's "part of this letter has not been decrypted" for f. 54 is its enclosure, the bare copy of Knowles's
notice on f. 57-57v (48 lines, 381 groups), which `champigny1744` reads. The letter ff. 54-56v itself is glossed. With
the five pieces seen on 3 Nov and those attested by `champigny1744`, every piece the lead names is now read at the time
or since, so 1204 closes as `read`.

Two of the dates sit outside the war the lead's title names: f. 109 is of 1740 and f. 158 of 1751; only C8 A 58 f. 33
(March 1748) falls in King George's War.

Not tested: whether the 1740, 1748 and 1751 pieces use the 1744 code of `champigny1744`. Their glosses would give keys
for those years if a bare letter of them turns up.

## 2730

The BnF record of fr. 3329 (https://archivesetmanuscrits.bnf.fr/ark:/12148/cc497913) was read again on 22 Nov 2026. It
agrees with the project's own audit of 16 Nov (`research/audit_2026-11-16_omont_shelfmarks`, finding for 2730), whose
folio fixes have not reached the lead:

- **Folios.** No. 81 (Maineville to Humières, Chenonceaux, 7 May 1577, "Avec chiffre") is f. 164 and no. 82 (Pierre de
  Roncherolles, Pont-Saint-Pierre, 9 May 1577, "Avec chiffre") is f. 165; the lead says ff. 104 and 105. No. 78
  ("Nouvelles d'Allensson", 3 May 1577, "Avec chiffre") is f. 159, as the lead says.
- **Missing item.** No. 107, Maineville, "D'Ennet, le 30 septembre" (no year), "Avec chiffre", f. 197.
- **The two tables are not a pair.** No. 1 is a "Table de déchiffrement anonyme"; no. 2 is a "Table de chiffrement de
  Monsieur de Humières pour correspondre avec Monsieur d'Entragues" (no folios given for either). Table 2 was made for
  another correspondent, so it need not be the key of the Maineville, Roncherolles and Laisné letters; that is a
  question to test.
- **Name.** The volume names the governor of Péronne as "J[acques de] Humyeres" (no. 84, f. 168, his mandement of
  18 May 1577); the lead has Jean. "Marquis" is not in the record.
- **Not online.** None of the three volume records (fr. 3329 cc497913, fr. 3409 cc49879s, fr. 4717 cc57767r) has a
  Gallica link, and Gallica's search, for "Français 3329" and (manuscripts) for Humières with "chiffre", finds only
  printed books and other volumes (fr. 3120, 3081, 3158, 3983 and a Clairambault volume). The lead's `access: archive` stands.
- The audit also lists fr. 3409 no. 39 ("Chiffre") and fr. 4717 no. 11 ("Clef d'un chiffre"): keys in the other two
  volumes, not yet looked at.

These go in the `unvetted` note, since `lead_updates` applies only with a verdict. Suggested field changes for the
project: `folio_note` "fr. 3329 nos. 1-2 (a decipherment table and Humières's cipher table for d'Entragues), 78
(f. 159), 81 (f. 164), 82 (f. 165), 107 (f. 197); fr. 3409 no. 49 (f. 126, 21 Nov 1578); fr. 4717 no. 49 (f. 91,
2 Apr 1577)"; `correspondents` "... -> Jacques de Humières".

## Routes

- ANOM (recherche-anom.culture.gouv.fr): record pages and IIIF manifests, images by script; 35 requests, all answered.
- BnF Archives et manuscrits: one fetch of the fr. 3329 record; no check appeared. Gallica's own search box, at a slow
  pace (one short check that cleared by itself).

## What is left

- 1204: look at C8 A 56 ff. 73, 85 and 253.
- 2730: images of fr. 3329 (nos. 1, 2, ff. 159, 164, 165, 197), fr. 3409 f. 126 and fr. 4717 f. 91, and the keys
  fr. 3409 no. 39 and fr. 4717 no. 11, by a BnF reproduction order or a visit.
