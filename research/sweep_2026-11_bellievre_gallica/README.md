# Bellièvre papers (BnF fr. 15890-15911), Gallica screen, 9 Nov 2026 - partial, 0 candidates

## What is on Gallica (found 9 Nov 2026)
Gallica SRU is 403 to curl/WebFetch but works in Chrome (one tab):
`gallica.bnf.fr/SRU?operation=searchRetrieve&version=1.2&maximumRecords=50&query=(gallica all "Papiers et correspondance de Pompone Ier de Bellièvre") and dc.type all "manuscrit"`
gave 21 records. IIIF manifests via `openapi.bnf.fr/iiif/presentation/v3/ark:/12148/<ark>/manifest.json` work with curl
(saved `m_*.json`). Images via `openapi.bnf.fr/iiif/image/v3/ark:/12148/<ark>/f<n>/full/500,/0/default.jpg` work with curl,
about 3 s per image (`fetch.py`). Each canvas is a microfilm two-page opening; canvases 1-4 are target frames and cover.

| fr. | vol. | ark(s) (btv1b...) | canvases | note |
|---|---|---|---|---|
| 15890 | I 1566-77 | 105073513 | 988 | not screened |
| 15894 | V 1598-1606 | 525216318 | 1168 | not screened |
| 15897 | VIII 1599-1606 prelates, princes | 9057357p | 580 | not screened |
| 15898 | IX parlements | 90643252 / 9064324n | 422 / 412 | not screened |
| 15902 | XIII 1572-73 | 9063602s | 627 | not screened |
| 15903 | XIV 1574-75 | 10501677p / 9064052x | 858 / 436 | not screened |
| 15904 | XV 1576-77 | 9064051h | 480 | not screened |
| 15905 | XVI 1578-80 (Anjou in the Netherlands) | 90638227 / 9063808z | 341 / 363 | first ark canvases 1-60 viewed |
| 15911 | XXII 1590, 1597-99 | 52521582d | 907 | not screened |

Not on Gallica (absent from the SRU title query): fr. 15892 (III), 15893 (IV), 15895 (VI), 15896 (VII), 15899 (X),
15900 (2), 15901 (XII), 15907-15910 (XVIII-XXI). That removes the Henri IV-era ambassador letters (15896 king, queen and
secretaries 1599-1606; 15899 ambassadors, consuls 1599-1607) from an online sweep; they need BnF photos.
Fonds notice: archivesetmanuscrits.bnf.fr/ark:/12148/cc461166 (opens in Chrome; the item-level links did not open on click,
so no item inventories were retrieved for these volumes, and no "déchiffré" flags checked).

## Screen
Fr. 15905, first ark, canvases 1-60 (5x3 sheets, 250 px tiles, `sheets.py`): Henri III / Anjou / Netherlands letters,
no cipher block seen. Stopped there: at 250-300 px a microfilm opening is too small to tell a cipher block from dense
script reliably, and the 5 Nov sweep used 800-px sheets and agent readers for 2,643 canvases. About 6,000 canvases remain.

## What remains
Screen at 800 px (method of `../gallica_sweep/NOTES.md`, `SCREEN_BRIEF.md`), priority 15905, 15911, 15904, 15894, 15903,
15902. Rows with seen:'scan' have not been written because no cipher leaf was seen.
