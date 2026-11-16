# OeNB Primo deep pass (15 Nov 2026)

Brief: a much deeper pass of the Austrian National Library catalogue (Primo, 403 to scripts, opens in Claude in Chrome with no check), then the
Tirol / Salzburg / Kaernten / Upper Austria archives. Own Chrome tab, one request per 4-5 s, no check clicked.
**Result: 6 rows in `candidates.json` (1 class A, 2 B, 3 weak C); nothing promoted.** `make_candidates.py` rebuilds the file.

## Routes

- Two scopes work. Korrespondenz facet: `https://search.onb.ac.at/primo-explore/search?query=any,contains,<term>&tab=default_tab&search_scope=ONB_gesamtbestand&vid=ONB&facet=rtype,include,Korrespondenz&lang=de_DE&offset=0`.
  **Whole manuscript holdings (HAN: codices, autographs, papers): `tab=onb_hanna&search_scope=ONB_hanna`, no facet**; this scope reaches the Handschrift and Sammelstueck records.
  `facet=rtype,include,Papyrus` gives the papyrus collection.
- Set "Ergebnisse pro Seite" to 50 once (it persists across navigations). The result list renders lazily: a page script that scrolls the page and
  reads each `prm-brief-result-container` collects all rows (about 8 s for 50). Opening a record (click `h3 a`, wait 2.6 s, read `Umfang` ... `Zitierlink`,
  `history.back()`) gives the extent line and the notes; the cipher information of the Autographensammlung is in the extent line ("Brief in Geheimschrift",
  "Text teilw. in Geheimschrift", "in Chiffern", "Begleitmaterial: Transskription").
- `javascript_tool` returns "[BLOCKED: Cookie/query string data]" for any string containing a URL; strip URLs before printing. A direct `fetch` of the Primo guest-JWT
  REST service was refused by the permission layer and not used.

## Terms and hits (Korrespondenz facet unless noted)

| Term | Hits | Result |
|---|---|---|
| Geheimschrift | 17 | 7 Autographen (Basta, Bragadin, Buquoy, Colloredo, Dampierre: already leads/catalogue; **Ferdinand II 1607 Autogr. 15/1-3 new**; Janos Zsigmond 1564: only the *address* is in Geheimschrift, dropped), Adelgunde of Bardi letters (known, 2816-2818), a Stammbuch (**new**), two Wittgenstein family letters (a family code word, edition exists: dropped) |
| chiffriert | 49 | all Schlik (28) and Dupont telegrams (21): known |
| Zahlencode | 21 | all Dupont: known |
| teilweise chiffriert | 16 | modern noise |
| Chiffre | 7 | all monogram signatures ("Mit Vermerk u. Chiffre von Kaunitz"): noise |
| Ziffern 10, verschluesselt 1 | | music letters (Berg), modern |
| Zifferschrift, Chiffrierschrift, Chiffrierschluessel, Zifern, cifra, cyphre, Dechiffrierung | 0 | - |
| HAN scope: chiffriert 51, chiffre 42, Ziffern 30, Geheimschriften 2, cifra 7, Entzifferung 13, cryptographia 1, Dechiffrierung 1, Chiffern 2, Schluessel (Korrespondenz) 28 | | Zane 25702 (known), Wassenaer Beilagen (part of the Schlik volume), Ottoman *siyaqat* number-writing manuscripts (accounting, not cipher), **Autogr. 15/28-1 and 14/61-15 ("in Chiffern") new**, **Cod. 9521 cryptography tract new**; Schluessel hits are literal keys; Dechiffrierung = a censor-office shorthand listing with its decipherment (closed) |
| Geheimschrift in the Papyrus facet | 5 | **P.Vindob. A. P. 11016, an Arabic letter in a secret script, Ihnas, 9th c.: new, the oldest item of the lead list**; Sator formula amulet and a magic tablet (not cipher) |
| Geheimschlüssel, Chiffrenschlüssel, Kryptographie, Zahlenschrift, Ziffernschrift | 0 | - |

## What did not open

- The ONB digital object of P.Vindob. A. P. 11016 (`data.onb.ac.at/dtl/4865249`) gave a browser error page in Chrome, so no image was seen; the record says "Digitalisierung und online".
  Nothing here was seen on an image, so no row meets the vetting bar (ciphertext seen) and none was promoted.
- manuscripta.at: 403 in Chrome (again). Kaernten KLAIS (`landesarchiv.ktn.gv.at/klais/`): the page never loads in Chrome either (error page). Tirol and Salzburg: no
  item-level finding-aid database was found in the earlier sweep and none here. Upper Austria went through findbuch in `sweep_2026-11-15_austria_swiss`.
