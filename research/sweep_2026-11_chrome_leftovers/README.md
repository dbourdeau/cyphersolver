# Chrome leftovers (9 Nov 2026)

Result: **1 candidate row** (`candidates.json`, built by `make_candidates.py`) and `vetting_notes.json` for leads 2417-2420. One Chrome tab, created and closed by this sweep; no CAPTCHA or bot check appeared on any site.

## 1. Leads 2417-2420 (France departmental)
- **2419 confirmed.** AD Ardennes (archives.cd08.fr, Arkotheque free-text search "Turenne Anhalt 1592"): cote **1 J 252**, item 70 "Lettre partiellement chiffrée et déchiffrée d'Henri de la Tour d'Auvergne, Vicomte de Turenne, adressée au Prince d'Anhalt, relative à sa lutte contre les Ligueurs de Lorraine, 22 octobre 1592 (1 pièce avec signet). Notes de Georges Haumont (7 pièces)". So cipher is confirmed, but the notice says "chiffrée et déchiffrée": a decipherment (contemporary, or Haumont's notes) exists with the letter, so it is probably not an unread letter.
- **2417**: archives-aube.fr loads in Chrome (curl was blocked). The online inventory search indexes fonds level only; 8 J = Fonds Chandon de Briailles (1605-1953). "8 J 166" and "Brûlart de Léon" gave no result. Item text is in PDF inventories. Cipher wording unconfirmed.
- **2418**: archives.lenord.fr does not resolve; the live site is archivesdepartementales.lenord.fr. Its search is full-text over PDF inventories; "élection impériale" occurs only in Série B (Chambre des comptes, Lille) inventories. "Musée 205" not confirmed.
- **2420**: not found (EE is normally the communal-deposit series, so the cote may be wrong). Unconfirmed.
- Route note: Arkotheque sites (Aube, Ardennes) work in Chrome; the URL pattern with `arko_default_...--filtreGroupes` can be edited; the free-text filter works; the cote filter is "commence par".

## 2. Het Utrechts Archief
- Huis Amerongen 1001, inv. 3486, 3487, 3488 (Torck, 1730-33, 1734-37, 1738-42): each has the note **"Enkele in cijferschrift"**. "Bekijk gevonden bestanden (0)": no scans. Written up as one row (class B).
- Van der Muelen 57, inv. 359 (Godin letters 1672-73, "Sommige woorden in cijferschrift"): already in catalogue.json (Godin lead); no row.
- Recipe: `...&micode=<fonds>&miview=inv2`, click "Bekijk gevonden archiefstukken", click the item number for its NB field.

## 3. Landesarchiv NRW (archive.nrw.de) in Chrome
The sufservice API works from inside the Chrome page (same-origin `fetch`, status 200, no Anubis). 30 terms, 221 unique records (Ziffern phrases filtered by cipher words): Chiffre 18, Chiffren 11, Chiffrierte 9, chiffrierter Brief 2, Geheimschrift 12, Geheimzeichen 2, Chiffrenschlüssel 8, dechiffriert 5, Dechiffrierung 4, Chiffrierung 5, Chiffrierschlüssel 1, chiffriertes Schreiben 5, "in Ziffern" 131, "mit Ziffern" 132, "Ziffern Brief" 5, cifra 1, cifre 1; 0 for Geheimziffer, Ziffernschrift, Zifferschlüssel, Ziffernschlüssel, chiffr Schlüssel, Dechiffrier, chiffrierten Brief, Chiffrenbrief, Chiffreschreiben, chiffrirt, chiffré, Zifferbrief, Ziffernbrief. 24 pre-1860 cipher records: all already in the repo or earlier sweeps (Lucchesini V 061, Velen U 132, Cap.C.I Stein letters, Ber.A M 20, Hin.A.Ak 2344/2346, key L 77 A 7520) or not cipher (Lemgo U_0343, 1431, is a merchant mark; V 502 Nr. 379 closed). One item not in the repo, not made a row: V 105 Nr. 797 (Frederick II decrees to Vincke, Copenhagen 1768, scanned), "in Chiffre mit Klartext", i.e. plaintext supplied; possible crib set.
**Result: 0 new rows.**

## 4. Steiermärkisches Landesarchiv
egov.stmk.gv.at/archivinformationssystem (works in Chrome; submit by script): Geheimschrift 0, chiffriert 0, Chiffre 2 (an 1871 trade card, a 1961 poster), Chiffren 1 (the poster), Ziffer 3 (tarock card, price notes). The full-text database covers collections of images and cards, not correspondence. 0 rows.

## 5. NLI and UCD
catalogue.nli.ie loads in Chrome. 11 queries (cipher letter, cypher, in cipher, ciphers, decipher ...), 106 records, 26 pre-1850. All are microfilms of copies of originals elsewhere (BL, PRO, Vatican) and nearly all say "deciphered" or "with decipherings" (nuncio letters 1608-20, Gualterio 1700, d'Avaux 1689, Wentworth 1638-39, Wolsey 1528). No rows. Weak items not in the repo: BL Add MS 21,483 (letters in cipher to James II 1669-88 with a key to names, a mixed volume; NLI microfilm n.365) and Add MS 21,375 (Rosen dispatches, cipher not stated). UCD Archives not tried.

## 6. Royal Society, Leeds, Rylands
- Royal Society CalmView: two navigations bounced the tab back to the previous page; no results. Still blocked.
- Leeds Special Collections: loads; "cipher" gives 26 records, none an unread cipher letter (a 1734 "shorthand or cipher follows" verse index, the Raper cipher journal printed 1924, 20th-century items).
- Rylands ELGAR: page did not load.

## 7. dlib.si, hrcak
dlib.si: search URLs returned its 404 page and the home page threw "Runtime Error"; nothing searched. hrcak.srce.hr loads but is a journal-article portal (literature, not documents); not searched.

## Remains
Item texts for AD Aube 8 J / EE and AD Nord Musée 205 (PDF inventories); Royal Society; UCD; dlib.si; Rylands.
