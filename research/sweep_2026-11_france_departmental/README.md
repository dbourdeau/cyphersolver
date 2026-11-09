# France departmental archives sweep (9 Nov 2026)

5 candidate rows (`candidates.json`, all `seen: catalogue`) and 5 key-only items (`key_leads.json`). Built by `make_candidates.py`.

## Routes
- **Worked: Daniel Tant, "Autres codes" (ARCSI, https://www.arcsi.fr/doc/Tant/420.pdf)**, a curated list of cipher items in French
  archives (cote, date, one-line summary). The best single source for departmental archives; four rows come from it, the fifth
  (AD Gironde G 919) was confirmed on its own Ligeo notice. `t_420.txt` is the extracted text.
  Entries not used: Indre 1595 (Henri IV to the Porte, printed by Berger de Xivrey), AD Bouches-du-Rhône 1 G 386 (34 coded documents
  on cloth, 1656-60, studied in Rev. d'hist. de l'Église de France 96), Yvelines 5 J 3 (copies, clear), Choiseul-Kau at AD Bas-Rhin
  C 644/645/589-57 (already in catalogue.json), Châlons FF 52 Delaval 1594 (already vetted and removed 2 Nov: part read by Tant),
  Besançon bishop's code, Haute-Vienne 2 JJ clergy register, Nantes diplomatic-archive codes (no cote), all 19th-20th c. telegram entries.
- **Worked: Ligeo Archives sites** (server-rendered): `archives.gironde.fr/archive/recherche/transversale/n:203?RECH_libre=<term>`
  (`lig.py`). Gironde: "lettre chiffrée" 2 hits (one real: G 919 art. 19), "en chiffre" 114 (all noise: plans, censuses), "Césy" 0.
  Hauts-de-Seine (also Ligeo): 0 for "lettre chiffrée" (search id guessed). Aveyron and Vosges are Ligeo too, not searched.
- **Worked: FranceArchives** (`fa.py`: JS redirect, then cookie jar). Already harvested in full by `../calames_biblissima`; spot checks only.
- **Blocked**: archives.cd08.fr (Ardennes), archives-aube.fr and about 20 other departmental hosts answer a 222- or 4110-byte JS/WAF
  shell to curl (`probe.py`); archives.lenord.fr, archives64.fr, archives-numerisees.paris.fr and the SHD site do not connect.
  Not tried in Chrome.
- Web search for the cotes finds nothing outside Tant, so every row's prior art reads "open as far as checked" and rests on one
  secondary list; cotes for Ardennes, Aube and Nord are unverified.

## Not done
SHD (Vincennes) and Archives diplomatiques finding-aid PDFs, Archives de Paris, Genève/Vaud; Institut/Mazarine/Sainte-Geneviève
are Calames and were swept. Arkotheque/Mnesys departmental portals are JS shells and were not harvested. A Chrome pass over
archives.cd08.fr and archives-aube.fr would confirm AD Ardennes 1 J 252 and AD Aube 8 J 166 / EE 1556.
