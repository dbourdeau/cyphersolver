# Belgium: KBR, BnL, city archives, KU Leuven (9 Nov 2026)

Brief: `research/_nov9/BRIEF.md`. Follows `research/belgium_lux` (AGATHA catalogue level, ANLux). Result: 2 candidate rows
(`candidates.json`), 3 key leads (`key_leads.json`). Nothing viewed (`seen: catalogue`); no images online for either row.

## Routes

| Source | Result |
|---|---|
| KBR `opac.kbr.be` (Syracuse) | Answers 200 (it did not before). `/Library/search.aspx?QUERY=...` renders results by JavaScript only; curl gets an empty shell, Chrome gets them after ~8 s. But it is a catalogue of printed books, periodicals and TV listings: "chiffre lettres" 8,009 hits, all modern; "déchiffrement lettres 1600" 112 hits (TV5 guides, periodicals). Manuscripts are not searchable as items there. `/LIBRARY/doc/SYRACUSE/<id>` records exist but are only for the printed catalogues. Dead end for item-level cipher search. |
| KBR printed catalogue, Van den Gheyn, *Catalogue des manuscrits de la Bibliothèque royale* t. 1-13 | Full text from archive.org (`cataloguedesmanu01..13brusuoft_djvu.txt`, 13 volumes, ~19 MB), grepped for déchiffr*, cryptograph*, chiffrée, "en chiffre", clef, cijfer, geheim. Only two non-binding hits: a *Dictionnaire de cryptographie* (ms. II 1051, in a sermon book; a treatise, not a letter) and Ms. t. 7 p. 425-426, no. 33 in a 16th-c. miscellany: "Coppie de la lettre escripte en chiffre par le roy de France a ceulx de Tournay et destroussee sur l'ung de leur messaige", Amiens 19 Nov 1521 (a copy of an intercepted French letter; whether the cipher or the clear text is copied is not stated; a few leaves, Tournai 1521, worth a look only if someone already holds the volume; not made a row because it may be a plain copy). Bindings "chiffre couronné de Léopold" are noise. Van den Gheyn does not describe cipher letters; the modern KBR letter collections are not catalogued online by item. |
| KBR `belgica.kbr.be` | 301 to a Belgica (digitised documents) portal, same Syracuse engine; not searched beyond the landing page. |
| BnL `data.bnl.lu`, `eluxemburgensia.lu` | Answer 200; they serve newspapers and printed material (eluxemburgensia), not manuscript letters. No item-level route found for manuscripts. BnL not exhausted: no cipher manuscript is known to be catalogued online. |
| Archives de la Ville de Bruxelles `archives.bruxelles.be` | 200, a Drupal site pointing to inventories; no item search tried. |
| Felixarchief Antwerp | `felixarchief.antwerpen.be` 403 to curl; not tried through Chrome. Web searches for cipher letters there found nothing. |
| Ghent, Bruges city archives | `stadsarchief.gent.be`, `archief.brugge.be` did not connect. |
| KU Leuven (`limo.libis.be`, `bib.kuleuven.be`) | 200 for the landing pages only (Limo is a JS app); no search run. A web search for Leuven special-collections cipher letters found nothing. |
| `search.arch.be` | 302 to an end-of-life notice (as already noted in `belgium_lux`). Inventory PDFs under `search.arch.be/ead/pdf/...` are indexed by web search but the EAD files are the better source. |
| AGATHA EAD, second pass | The 649 EAD inventories downloaded by `belgium_lux` (in the main checkout, git-ignored) were searched again with `grep2.py`, a wider term list (gecodeerd, codé, décod*, "in code", lettres secrètes, geheime brieven, ontsleutel*, clef du chiffre, cipher, cryptographie, in cijfer*, schlüssel zu ...) over the full own text of each component, not only unittitle and scopecontent (the first pass missed notes in other elements). 6,964 raw hits, 6,090 of them "code" (legal codes, "gecodeerde" classification codes). The filtered 40 or so, read by hand, gave the two rows and the key leads below. `dump.py <eadid> <unitid>` prints a component with its ancestors. |

## Rows

1. Whyte/de Vicq(ue)/d'Albyville fonds, Rijksarchief Antwerpen, inv. 511 - Y21/004 no. 3: J. D'Uguarte, Brussels 1656-60, "deels in cijferschrift". Class B.
2. Merode Westerloo no. 9750: Ferdinand of Bavaria to Jean de Merode, 1640, cipher with the code attached. Class B.

## Key leads

Audience 405 (Halewijn/Boisschot to Requesens, key at f. 245; overlaps the existing England row), Audience 161/A-B (keys for Margaret of Parma), Audience 124 (Harneffe keys for Mary of Hungary/Granvelle).

## Excluded

- "Lettres secrètes de la duchesse Marguerite au roy" (Varia-bestanden 437/438): a 16th-c. title of a collection of copies of the troubles-of-the-Netherlands letters, not cipher.
- Audience 431-433 "correspondance secrète (agents secrets)" 1626-30: unsigned secret letters from France, no cipher stated.
- Cobenzl index "Correspondance secrète" 1766, Eupen Schlüssel, Namur "lettre secrète", Antwerp department "geheime briefwisseling" 1796-1800 (Napoleonic police), La Poste cryptographic material 1990, NGI 1928-46, tram telegram codes 1926-38: modern, administrative or not cipher.

## What remains

- KBR modern manuscript collections (Archives and Museum of Literature; Mss. 16xxx-20xxx): no item catalogue reachable; try the KBR "Catalogue des manuscrits" inventories as PDFs on kbr.be, or Belgica (digitised).
- BnL manuscripts, Felixarchief (needs Chrome past a 403), Ghent/Bruges/Brussels city archives (not reachable by script; Chrome untested), KU Leuven Limo (needs a JS session; `uurl.kbr.be/<id>` style permalinks answer 200).
- Whether the 1521 Tournai intercept copy (above) is worth a page request.

Chrome use: one tab, created for this sweep, only to render `opac.kbr.be` search results; it was closed afterwards.
