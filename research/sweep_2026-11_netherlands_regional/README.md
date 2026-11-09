# Netherlands regional archives and libraries (9 Nov 2026)

Brief: `research/_nov9/BRIEF.md`. Follows `nationaal_archief`, `sweep_2026-11_kb_netherlands`, `belgium_lux`,
`sweep_2026-11_belgium_kbr_arch`. **Result: 0 candidate rows, 0 key leads.** Nothing was found that meets the row bar; the
sweep was mostly a route survey.

## Routes

| Source | Result |
|---|---|
| Open Archives API `api.openarch.nl/1.0/records/search.json` | 200, but it indexes persons (genealogy). "cijfer" gives 843 surname hits (A. Cijfer, passenger lists). Useless for documents. |
| archieven.nl / Memorix `webservices8.memorix.nl/archives` (used by Archief Amsterdam, Zeeuws Archief etc.) | The item search needs an API key embedded in the page. Using that key from a script was declined by the tool's permission check, so the route was not used. Not tried again. |
| Het Utrechts Archief | Works in Chrome only (curl: 301/"Invalid key"; WebFetch 403). Global search URL: `https://hetutrechtsarchief.nl/onderzoek/resultaten/archieven?mivast=39&mizig=0&miadt=39&mizk_alle=<term>` lists archives (fonds) that contain the term; adding `micode=<fonds>&miview=inv2` and clicking "Bekijk gevonden archiefstukken" lists the item titles (JS, ~5 s). Item descriptions/links could not be read by script (`javascript_tool` blocked on link hrefs). |
| Zeeuws Archief, Erfgoed Leiden, Tresoar, Huygens Resources, NHA, Haags Gemeentearchief, BHIC, Amsterdam | Home pages answer 200, but archive search results render by JavaScript (or the guessed search URL 404s); no item-level text retrieved. Gelders Archief host unreachable (000). Leiden `digitalcollections.universiteitleiden.nl` search: no connection. |
| WebSearch for cipher letters in these archives | Nothing new: only Akkerman's Elizabeth Stuart work, the Brienne chest (Museum voor Communicatie), Gekaapte Brieven (not cipher). |

## Terms run (Het Utrechts Archief only)

- `cijferschrift`: 2 fonds hits, 1001 Huis Amerongen (3 items: inv. 3486-3488, Frederik Willem Torck letters from The Hague,
  Arnhem etc., 1730-1742) and 57 Familie Van der Muelen (not opened). The Torck letters are Dutch diplomatic/private
  correspondence; whether the cipher is a real cipher or a key, and whether they are scanned, was not established (Amerongen has
  1,571 digitised items). Not a row: no cipher text seen, no description of a cipher letter.
- `cijfer OR gecijferd OR cijfers OR chiffre OR geheimschrift`: 100 fonds hits (13 pages), dominated by modern "cijfers"
  (statistics); not worked through.

## What remains

1. Het Utrechts Archief: open Amerongen inv. 3486-3488 (Torck) and the Van der Muelen hit in a browser; check for cipher
   passages and scans. The Nationaal Archief README already names Huis Amerongen (Van Reede envoys) as the best regional lead.
2. A Chrome pass per regional archive (Tresoar 7-02..7-14 stadholder archives, Culemborg 0370, Gelre 0001, Bentinck 0613, Van
   Lynden 1030, KZGW Middelburg), each item list needs clicking, as in the Utrecht recipe above.
3. Leiden (UBL) and Huygens ING resources: not reached; Hugo de Groot/Huygens correspondence is printed (so not leads).
