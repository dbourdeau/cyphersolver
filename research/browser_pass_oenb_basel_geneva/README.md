# Browser pass: ÖNB, manuscripta.at, Basel Staatsarchiv, Archives d'Etat de Genève (2 Nov 2026)

Follow-up to the "Dead ends and blockers" in `research/swiss_austrian/README.md`. Retried in the built-in browser and in
Claude in Chrome. No check was solved or clicked by Claude. Everything is a lead, not a catalogue entry.

| Portal | Result | Route |
|---|---|---|
| **manuscripta.at** | **Blocked.** nginx 403 on `/` and `/hs_suche.php` in the built-in browser and in Chrome | Not swept. Needs another network or the ÖNB/HANNA route |
| **ÖNB Primo** (`search.onb.ac.at`) | **Blocked.** 403 in both browsers | Not swept |
| **ÖNB Digital** (`onb.digital`) | Opens in Chrome, but sits behind a cookie-consent gate ("Ich bin einverstanden") | **Not swept**: consent not accepted without the user's yes |
| **Basel Staatsarchiv** (`dls.staatsarchiv.bs.ch`, "agora") | Opens. An ALTCHA proof-of-work check clears itself in about 10 s in Chrome (built-in browser got a Nuxt 500). Cookie banner declined | `https://dls.staatsarchiv.bs.ch/search?page=1&page_size=100&query=<term>&advanced_query=false`; read `main.innerText` after 2.5 s. 12 terms |
| **Archives d'Etat de Genève** (Adhémar) | Opens in the built-in browser at `ge.ch/arvaegconsult/` (archives.ge.ch does not resolve) | Form is a POST, then a GET `ResultSet?...&w=NATIVE('(NMOCA ph any ''<w>'' OR MCCOM ... OR DESCRIP ph any ''<w>'') and ORIGINE = ''DOC'',''COLPHO''')`; same-origin `fetch` of that GET works; the clause on ORIGINE is required. 25 terms |

## Basel: terms and hits

Zero hits: Chiffrierschlüssel, chiffriert, Ziffernschrift, Zifferschrift, Geheimschlüssel, dechiffriert, Geheimsprache.
Hits (all other hits are modern noise: Scharlach "Chiffres", Eichenwald "Chiffren", Friends of the Earth, a Basel deanery "cifra"):

1. **PA 633c A 3.1.6, fasc. 8, "Chiffres pour correspondance secrette", 23 Sept 1795** (Peter Ochs papers). A cipher key or
   cipher sheet from the Basel peace-negotiation year. Detailed record, no scan seen on the record page. Key lead; look for
   the letters in the same Ochs series (PA 633c A 3.2.3, fasc. 84, Ochs to Bürgermeister und Rat, 3 Jan 1798, came up on the
   same query: possibly ciphered).
2. **PA 511a 604-10-02, "Korrespondenz betreffend die Sendung nach Paris, 1814/1815"** (hit on "Entzifferung"): Basel
   mission to Paris, correspondence; not opened.
3. PA 158 4 (1798-1828, personal papers) came up on "Geheimschrift"; PA 167 A 1 (1640-1889) likewise. Not opened.

## Geneva: terms and hits

Terms: chiffre, chiffres, chiffré/-ée/-és/-ées, chiffrer, déchiffrer, déchiffrement, cryptogramme, cryptographie, cifra,
cifre, chiffres secrets, écriture secrète, alphabet secret, correspondance secrète, clef du chiffre, secret, secrète(s),
clef, clé, énigme (348 distinct records seen). **No cipher document.** Only: P.H. 4927 and 4934 (1768-69), "cartons de
déchiffrement" for the election of auditeurs and syndics (a voting device, not a cipher), and 20th-century uses of
"chiffre". Caveat: the ORIGINE filter (DOC, COLPHO) is what the form itself applies; the "Manuscrits historiques" series
may be described in too little detail for a keyword to find.

## ÖNB Digital (swept after the user accepted the cookie notice)

Search box in Chrome, one term at a time (each search gets a session URL `onb.digital/search/<n>`, so there is no
scriptable query URL). Terms: Chiffre (32 hits), Geheimschrift (page returned the same 32, so the search may not have
refreshed), chiffriert (50), Ziffernschrift (50; identical list to chiffriert, so the engine looks fuzzy or fell back to a
default set). Date facet runs 1300-1925: this portal is the curated digitised subset, not the ÖNB manuscript holdings.
Manuscript hits are all medieval literature or theology (Roman de Troie, Eugen of Savoy's French codices, Hussite
Sammelhandschriften, a lectionary) plus "Werk über Stadtverteidigungsanlagen" (Murano 1597): **no cipher item**. The
real manuscript holdings (HAN catalogue, Primo) stay blocked; try them from another network.

## Next

- ÖNB Digital needs a yes to the cookie gate; ÖNB Primo and manuscripta.at need another network.
- Basel leads 1 and 2: open the Ochs and Paris-mission units on a scan-visible day (images may be on request only).
