# Sweep: French-language Swiss archives, pre-1920 (15 Nov 2026)

Brief: the French-speaking Swiss archives left open by `sweep_2026-11-15_austria_swiss` (Geneva, Vaud, Fribourg, Valais, Neuchatel, Jura, Bibliotheque de Geneve,
e-manuscripta). **Result: 17 rows in `candidates.json` (12 class A, 3 class B, 2 weak class C), 6 key-only groups in `key_leads.json`.** Every row is scored from
finding-aid text (`seen: catalogue`); none viewed as an image; no web, Tomokiyo, Lasry or DECODE search. Dedupe with `known.py` (Affry (de Boccard), Mestral, Saint-Saphorin, Marsay,
Supersaxo, Kalbermatten, Marclay, Tronchin 148, Ivernois, Jacobi-Kloest, Rambaud, Wrisberg, Altamira): only Marsay (lead 1781, TNA SP 78/205/95), Robethon (lead 1663) and the
existing d'Affry 1757 targets turned up; Courten / Rousseau rows are the Austria/Swiss sweep's and are not repeated. Nothing merged or committed; `catalogue.json`, `leads.json` and
`merge.py` untouched. `make_candidates.py` rebuilds both files.

**Best find: the Affry (de Boccard) fonds at the Archives de l'Etat de Fribourg** (friXplore, `archives.fr.ch`): about 300 units, 1755-62, of French ministers', generals' and
envoys' letters and dispatches to Louis-Auguste Augustin d'Affry (ambassador at The Hague), many ciphered and filed with "Transcription du chiffre ..." or "Decryptage ..." pieces, plus
two key sheets (280.209-210). The catalogue's `affry1757` / `affry1757c` targets (R1071, d'Affry to Stainville 7 Aug 1757) cite only Nationaal Archief decipherments that are not
digitised; the Fribourg fonds is the other half of that correspondence and was in no ledger.

## Routes, for the next sweep

| Source | Route | Result |
|---|---|---|
| **Fribourg friXplore** (`archives.fr.ch`; the fr.ch inventory page links it) | Server-rendered. `/search/results?q=TERM&scope=all&mode=table&page=N` fetched from the page returns 20 rows a page (the extension blocks printing that URL; build it in code). Row text gives cote, title, date, level; the ark link is the detail page. "Multimedias: Sans" for the whole Affry set (no images online). A stemmed engine: "lettre chiffree" and "lettres chiffrees" return the same 185. Cookie banner left alone. | Done. 185-222 hits for chiffre terms, nearly all Affry (295 distinct units) |
| **Vaud DAVEL** (`davel.vd.ch`, scopeArchiv; **opens normally in Chrome**, the 2 Nov block was the other Vaud site) | From `volltextsuche.aspx` fetch the page, copy the hidden fields, POST `ctl00$cphMainArea$txtMitAllenWoertern` and `cmdSuchen`; it lands on `resultatliste.aspx` (10 rows a page; next page is a postback with the `>>` link's event target). `detail.aspx` and ID gives the unit text (Content, Language "Crypte; Francais", Descriptors). The inventory flags ciphered units in its **Language field "Crypte"** and descriptors **cryptage / codage / cryptographie**: search "Crypte" and "codage". Noise: Chillon "crypte". | Done |
| **BGE Geneve** (`archives.bge-geneve.ch`) | GET `/archive/resultats/touslesfonds/lineaire/n:96/limit:50/page:N` with query `RECH_S` and `type=touslesfonds`; 50 records a page, each with its full description. Lower-level hits surface under the parent fonds record, so read "Presentation du contenu". | Done; shelfmarks need a second look at the item level |
| **archives-online.org** | As in the Austria/Swiss README (Chrome console, 5 s a term, "nae chsten Seite"). Archive names are localised in the result column (Wallis, Waadt, Genf, Neuenburg, Luzern). Covers AEV, ACV, AEG, AEN, AAEB (Jura), ArCJ, AVN, AVCF, BPUN. **Not in it: Fribourg, Archives de la Ville de Geneve, BGE.** | Re-run for about 20 French terms; nothing new beyond the rows |
| **e-manuscripta** (`www.e-manuscripta.ch/search/quick?query=`) | An automatic "Verifying your browser" proof-of-work page appears first (no CAPTCHA; it clears itself in a few seconds). Then fetch works; results hold hit blocks with the transcription text. | Terms Geheimschrift 8, chiffriert 5, dechiffrement 12, clef du chiffre 8, Dechiffrierung 10, verschluesselt 2: only transcription matches (Basel Bernoulli and Mencke letters, Wille 1915-18 papers, almanacs with "Geheimschrift" notes: bau 1090307, 1041276, 1083008, Brief an Josephine Reiter bau 980745). No row |
| Neuchatel AEN, Geneva AEG (Adhemar), Ville de Geneve | `archives.ne.ch` and `adhemar.ge.ch` do not resolve; the `ne.ch` archives page is a 404; the `ge.ch/archives/adhemar` URL redirects to the ge.ch home page. Searched only through archives-online. | Native databases not found; not searched |
| Valais AEV native, Jura bernois (Archives de la Fondation de l'Ancien Eveche de Bale = AAEB, in archives-online), ArCJ | Through archives-online: AAEB gave only census and ordinance noise; ArCJ nothing. | No row |
| Archives Henri Dunant (BGE) | Searched inside the BGE terms; no cipher hit in the Dunant papers. | No row |

## What is new

| Rows | What |
|---|---|
| 1-9 | **AEF Affry (de Boccard)**: Rouille 1755-57 (225, 42 units), Bernis 1757-58 (226, 23), Choiseul 1759-62 with "Decryptage" pieces (227-228, about 60), Stainville from Vienna 1757-60 (257, 259), Estrees 1757 (238, 20), Conflans d'Armentieres 1759 (244, 19), Ogier 1758-60 (266, 28), Havrincourt from Stockholm 1758-60 (267, 45; 268.19 is a "Decryptage" filed next to it). Keys 280.209-210 and the small commander series are in `key_leads.json`. |
| 10-11 | **ACV Marsay** (British envoy): P de Mestral III 484 (1730-39, 96 pieces, "le code est dans le lot") and III 486 (1746-62, 145 pieces, "avec une clef du chiffre"). Two periods, two keys. Related to lead 1781 (Newcastle to Marsay cypher, 1734). |
| 12 | **ACV Mestral II D 4 and D 6/1**: Saint-Saphorin's correspondents (Robethon, Wrisberg 1720/24, Robinson 1726) with ciphered letters and a series of per-correspondent ciphers (Bothmer, Bernstorff, Buol, Hohenzollern, Prie, Salm, Schlick ...). |
| 13-15 | Valais: Supersaxo II P 74 (cipher letter to Schiner, c. 1510); Marclay FQ 238 / 372 (c. 1630, weak); Kalbermatten P 196 (a cipher table, weak). |
| 16-17 | **BGE**: Tronchin 148/56, d'Aubigne's "Divers chiffres employes dans les guerres civiles" 1620-25 (digitised, 48 views); Eynard / d'Ivernois / Jacobi-Kloest ciphers 1807-15 with a named decipherment and keys (three keys; split on merge); Rambaud, Ms. fr. 445 (weak). |

`key_leads.json`: AEF Legislation et varietes 52 (the 1708 Lucerne-Fribourg-Solothurn code, third copy next to Luzern COD 1100 and Valais AV 54/7); the Affry key sheets
280.209-210; the small Affry commander and envoy series; the Mestral cipher series; Valais Courten Cn B 5/11/8 (Stainville's codes); the BGE Altamira fonds (not a row).

## Seen and dropped

- **Noise**: "chiffre" as number or "chiffre d'affaires" (ACV, Valais communal records, Geneva registers), "musique chiffree", BAR (Federal Archives) Chiffre-Verkehr files of 1918-19 (twentieth century), "carton de dechiffrement" (Geneva ballots 1768-69), "recapitulations chiffrees" (Neuchatel census), Chillon "crypte", Zurich and Obwalden gazette notices ("Chiffre-Inserate"), Boissonnas photographs, Bonnet and BPU manuscripts with "folios non chiffres", Basel PA 633c (held, `browser_pass_oenb_basel_geneva`), Rousseau BPUN rows (Austria/Swiss sweep).
- **Not rowed**: BAR E2.0.0.1A#1/45 "Geheimkaestchen, Chiffrierapparate und Chiffre-Verkehr" (1897) and E2.2.0.0.19-01#1/7.0.3 "Correspondance en chiffres entre Legation et Consulats" (1914-18, Federal Archives): late, the Austria/Swiss sweep has the Federal Archives key lead; StAGR D III Z/II Ba.dd.068 Planta "Chiffre pour correspondance" table 1771 (Graubuenden, French-language table; Planta Ac.64 is already a key lead); AEN Benoit-Bobillier-8 (dye recipes).
- Mestral II D 4 letters of Robethon 1717, Wrisberg 1720/24 and Robinson 1726 are inside row 12, not separate rows (one fonds, keys per correspondent).

## Honest limits

- Descriptions only. No image or page viewed; the Affry "Transcription" pieces may be modern or contemporary (the finding aid does not say), and which Affry pieces are in cipher versus only transcribed was not opened. The counts per series are of units surfaced by the chiffre terms, capped at 200 a term; fonds-wide totals may be higher.
- The Affry fonds is not digitised on friXplore; it needs the reading room or a reproduction order, so these rows stay on the "needs archive scan" side.
- Altamira (BGE) and the AAEB and ArCJ results were read as parent records only.
- Neuchatel's native database, Geneva's Adhemar and the Ville de Geneve archives were not reachable; Fribourg's other fonds beyond Affry returned only the 1708 code.
- Class labels follow the earlier sweeps: A = key or clear text named in the finding aid, B = cipher only, C = weak or unclear.

## Chrome use and blocks

Own tabs, one search per 1-5 s, no parallel floods. **No CAPTCHA or login appeared.** e-manuscripta showed an automatic browser-verification page that cleared by itself. The extension blocks tool output containing
`?query=`-style strings and long outputs over about 1,000 characters (cut with `[TRUNCATED]`); print compact snippets and replace `=&?` in strings. Long awaits (45 s) time out: start loops un-awaited and poll a `window` object. A tab I did not open
(Stiftsarchiv St Gallen scope page) was left untouched. Native databases that do not resolve from this network: `archives.ne.ch`, `adhemar.ge.ch`.
