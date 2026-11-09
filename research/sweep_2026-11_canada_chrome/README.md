# canada_chrome sweep, 9 Nov 2026 (Chrome pass over the Canadian sources blocked to scripts in canada_provincial)

Result: **0 candidate rows**, no key leads. No New France / Acadia / Loyalist / 1812 / 1837 / Red River / fur-trade
letter with a cipher passage and no decipherment surfaced. One tab, no logins, no CAPTCHA touched.

## Routes
| Holder | Result in Chrome |
|---|---|
| **BAnQ Advitam** (`advitam.banq.qc.ca`, the archives catalogue that replaced pistard; no Radware check) | **Works.** A cookie dialog covers the page: "Personnaliser" > "Refuser" (all optional) > "Enregistrer", then the search box takes typed text + Enter (the form GET with `rechercheSimple=` does not run the search; type it). Hits: chiffre 567 (silver "au chiffre des Sulpiciens" monograms, statistics, court-file noise), chiffrée 51 (court sampling notes), "en chiffres" 36 (statistics), déchiffrer 22 (illegible handwriting), cipher 0, cypher 0, "écriture chiffrée" 0. One notarial/prévôté 1741 billet with "en chiffre entre deux barres" = numerals. Nothing cryptographic. |
| BAnQ numérique (`numerique.banq.qc.ca`) | Loads; form POST (`terme`) runs, but full-text over printed books/newspapers ("lettre chiffre" 156k noise). No manuscript route. |
| **McGill Archival Collections** (AtoM) | **Works by URL** `informationobject/browse?topLod=0&query=...`. cipher 5, cypher 1, combined (in cipher / cryptogram / secret writing / chiffre) 5. All five are false or off-scope: Penfield medal warrant, Baylis fonds MSG 399-1 (letters 1895/1899 from Ignatius Donnelly, Baconian cipher author, a printed-book matter, not a cipher text), Dawson-Harrington MG1022-6-126 (1892 business letters, probable "cypher" telegram mention), Osler items. Not opened further. |
| **Memory BC** (AtoM) | **Works by URL.** cipher 1 / "in cipher" 1 (Bell-Irving family fonds, City of Vancouver Archives; the word is not in the visible record, diaries 1889-1930, 20th c., not a cipher lead); cypher, cryptogram, "secret writing" 0. |
| **MemoryNS** (AtoM) | **Works by URL.** cipher 0, cypher 1 (Rebekah Lodge fonds 1949-2008), cryptogram/in cipher/secret writing/chiffre 1 (Télé-Clare video collection, noise). |
| Musée McCord Stewart | Site loads, collection search URL guessed wrong and redirected to a blog page; not searched. |
| Laval archives (`archives.ulaval.ca`) | Loads; institutional university records, no catalogue search tried (20th-c. administrative). |
| PANB `archives.gnb.ca` | Cloudflare "Just a moment" did not clear in about 18 s; skipped. |
| Archeion (Ontario) | "Verifying your browser" challenge did not clear in 10 s (twice); skipped. |
| UCalgary searcharchives (Glenbow) | "Verifying connection" check, skipped. |
| BC Archives `search-bcarchives.royalbcmuseum.bc.ca` | Chrome error page (same as scripts); skipped. |
| UdeM, Champlain Society / Canadiana, SLNSW | Not attempted (Canadiana covered in earlier sweeps; SLNSW shows Human Verification per oceania_chrome). |

Web searches (3: English cipher + Quebec/Acadia/NS/Upper Canada; 1837/Red River/fur trade; French lettre en chiffres Nouvelle-France/Louisbourg):
no named Canadian cipher item or edition found. Suggestions in the results (Pichon papers, Séminaire de Québec letters, ANOM Louisbourg dispatches) were not
cipher-specific.

## Remaining
PANB, Archeion, UCalgary/Glenbow (all bot checks that need a human to clear), McCord collection search (correct URL unknown), UdeM, Toronto
Baldwin collection. Advitam does not cover private fonds descriptions well for rare words, so item-level cipher mentions in finding aids could be missed.
Prior: Canadian holdings of pre-1900 manuscript cipher look sparse; the one real find remains AO F 47-1-2-47 (Simcoe cipher letters, sibling of #877).
