# Canadian provincial / university archives sweep (9 Nov 2026)

Scope: Canadian holders beyond LAC (see research/canada_lac, research/canada_latam). Result: **0 candidates**,
1 weak key lead, 1 new access note for an existing catalogue entry. No Chrome, no BNE.

## Routes that worked (scripted, curl/urllib, 3 s between requests)

| Holder | Route | Terms and hits |
|---|---|---|
| Archives of Manitoba incl. HBCA | Minisis form POST (`pam.minisisinc.com/scripts/mwimain.dll/<sid>/1/0?SEARCH`, fields KEYWORDS/RESP_CENTRE; session id read from the DIRECTSEARCH page), `pam.py` | cipher 0, cypher 1 (HBC telegraph cypher books, 20th-c. commercial code), code 38 and "in code" 35 (court dockets, fur-sale code, noise), coded 6 (noise), secret/chiffre/cryptogram/secret writing/invisible ink/ciphers 0. No HBCA manuscript cipher. |
| Archives of Ontario (AIMS) | Minisis union search POST (`aims.archives.gov.on.ca`, KEYWORD_CLUSTER; action URL from the archival search page), `ao.py`, `ao_list.py` | cipher 1, cypher 2, cyphers 2, cryptogram 1, coded 40, code book 25, secret 101, decipher/deciphered/chiffre/"cipher key"/"secret code"/"secret writing" 0. Only real hit: F 47-1-2-47 (below). The rest are Mackenzie "mere cypher" rhetoric, Royal cyphers (monograms), code books for forestry/accounts, court noise. |
| Nova Scotia Archives | `/search/?q=` (digitised content) and `/library/catalogue/?Search=` | cipher 10 (all "difficult to decipher" gravestones), cypher/ciphered/chiffre/"secret writing"/"invisible ink" 0; library: Eliot diary "deciphered" shorthand, Thoyts palaeography. Archival Holdings (MemoryNS) not scriptable. |
| DalSpace (DSpace 7 REST) | `dal.py` | Theses and journal articles only; nothing archival. |
| Canadiana | `/search?q0.0=tx:"in cipher"` (548 results, mostly newspapers); earlier sweep covered the rest | no manuscript text. |

## Blocked (not bypassed)

BAnQ pistard.banq.qc.ca (Radware captcha, redirect to validate.perfdrive.com); Provincial Archives of New Brunswick
archives.gnb.ca (Cloudflare 403); McGill archivalcollections and McCord collections (HTTP 202 challenge shell, empty body);
BC Archives search-bcarchives.royalbcmuseum.bc.ca (connection error, not retried with TLS verification off); Memory BC (JS redirect);
Glenbow/UCalgary, Laval, Université de Montréal, Archeion, Archives Canada (JS-only or no search endpoint). LAC: see canada_lac.
UNB Loyalist collection `browse?search_api_fulltext=` ignores the query (returns all 699 titles).
Web searches (1812 Prevost/Brock, Fenian/McMicken, 1837 Patriotes, New France/Acadia lettre en chiffres, HBC, Loyalist cipher):
no named cipher item or edition found.

## Finding: sibling of catalogue #877 (Simcoe)

Archives of Ontario **F 47-1-2-47, "Cipher Letters Relating to North America", 1794-1795, 1 file**, part of F 47-1-2
Lieutenant-Governor of Upper Canada chronological files, correspondence (Simcoe papers); reached on self-service microfilm
**MS 1801**; record `aims.archives.gov.on.ca ... WEB_DESC_DET?SESSIONSEARCH&exp=sisn 249682`. This is the Archives of Ontario copy
(microfilm) of what catalogue #877 describes from the Devon Archives (1038 M/O/5/1-3, same title and years). Not entered
as a candidate (duplicate by title and date), but it gives #877 a film route and a second possible location, and a place to look for
whether the letters are in the Cruikshank edition, vols 3-4 (1794-95); only vol. 1 was found as full text on archive.org
(`correspondenceog0001brig`), so vols 3-4 were not searched. Suggest adding the AO shelfmark to #877's links/vetting.

## What remains

BAnQ (needs a normal browser), PANB, McGill, McCord, BC Archives, Memory BC, MemoryNS archival catalogue, Toronto Reference Library Baldwin
collection, Champlain Society volumes. Cruikshank Simcoe vols 3-4 full text for #877.

## Files
`pam.py`, `ao.py`, `ao_list.py`, `dal.py`, `ao_action.txt`, `candidates.json` (empty), `key_leads.json`.
