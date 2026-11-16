# Arabic cipher sweep 2, part A: Spain, Portugal and the Maghreb (16 Nov 2026)

Run by Daniel Bourdeau; Claude Code session (Claude Opus 5.5), Arabic sweep 2 part A, cloud network, 16 Nov 2026,
about 05:40-07:00 UTC. Goal: unread enciphered texts in the Arabic language or script (aljamiado and Maghribi
included, any date to 1950), seen on images and vetted. Nothing solved, merged, promoted or committed. Rows:
`candidates_A.json` (**1 row, with a complete vetting block, verdict open**). Downloads and images are in the session
scratchpad, outside the repository.

Earlier passes this continues, and does not repeat: `research/sweep_2026-11_arabic/` (6 Nov),
`research/sweep_2026-11-15_arabic/` (parts A-D, 15 Nov; part C could not reach Spain) and
`research/sweep_2026-11-15_wave15_arabic2/` (15 Nov, which already read Colin 1927 in full; see below).

## Result in one paragraph

One new lead, and it is a good one: **Sacromonte Lead Book 17, *Ḥaqīqat al-Injīl*, the "Libro mudo"** (Granada, found
31 Dec 1597): five or six lead plates with 9-10 lines each of a cryptic script that its 2024 critical editors (van
Koningsveld and Wiegers, Brill, open access) call undeciphered. One plate (fol. 3b, 10 lines) is published as a
photograph in that edition and was viewed at its native 1,313 x 1,317 px; the rest are in the Sacromonte Abbey and the
Vatican photographs, not online. No Arabic-language **diplomatic** cipher letter was found in the area: PARES (Simancas,
ACA, AHN) blocked again (429, then a connection reset), as did the BNE digital library, Hispana, BVPB, the Ministry's
CCBAE pages, the RAH digital library, ANOM and the Moroccan national library. What could be reached was searched or
paged and is negative: the whole Torre do Tombo fonds of Arabic letters from the Moroccan *praças* (74 units, first
image of each viewed), the BNE catalogue's Arabic and aljamiado manuscripts (663 records), the BNP catalogue, the
Escorial, BNE, Granada and Junta catalogues on archive.org, and every volume of *Hespéris* 1921-1959.

## Routes that worked from this network

| Host | Route | Note |
|---|---|---|
| DigitArq (Torre do Tombo) | `GET /api/docs/search?query=<q>&archiveCode=ANTT` (10 rows; paging params `fromIndex`/`max` per `research/torre_do_tombo/README.md`); children `GET /api/docs/details/<id>?down=1&childrens=<id>&fromIndex=0&max=200`; scans `GET /api/rdigital/<doc id>?fromIndex=0&max=2000` then `GET /rdigital/dissemination?fileId=<id>` (images about 1,700 x 1,850 px) | Works with curl. `/api/docs/rdigital/<id>` and `/api/rdigital/files/<rep id>` answer "Unauthorized"; the route above (document id, not representation id) is the open one. About 245 requests used, 2.5 s apart. |
| BNE catalogue (Alma Primo VE) | `GET https://catalogo.bne.es/primaws/rest/pub/institution/34BNE_INST/guestJwt?isGuest=true&lang=es&viewId=34BNE_INST:CATALOGO` (the site's own anonymous guest token), then `GET /primaws/rest/pub/pnxs?...&q=<field,op,value[,AND;...]>&tab=LibraryCatalog&scope=MyInstitution&vid=34BNE_INST:CATALOGO` with `Authorization: Bearer <token>`. Field queries work: `lang,exact,ara`, `rtype,exact,manuscripts`, joined by `,AND;`. | **New route**: the BNE catalogue is reachable although bdh.bne.es / bdh-rd.bne.es / datos.bne.es / bnedigital.bne.es all return 403. Paging stops at offset 500 (401 beyond); re-sorting (`sort=title`, `date2`, `date`) recovers part of the rest. About 45 requests. |
| Europeana Record API | `api.europeana.eu/record/v2/search.json?wskey=api2demo` as in `research/bne_hispana/eu.py` | Works; carries only part of the BNE Arabic manuscripts. |
| BNP catalogue (Horizon ipac20) | as in `research/sweep_2026-11_bnp_portugal/README.md` | Works. |
| archive.org | `advancedsearch.php`, `metadata/<id>/files`, `download/<id>/<file>_djvu.txt` | Works. |
| Archives du Maroc (archivesdumaroc.ma) | WordPress site search `/ar/?s=<term>` | Answers, but it searches the institution's web pages, not a catalogue. |
| unglue.it / files.unglue.it | mirror of the open-access Brill PDF of the Sacromonte edition | Used after OAPEN answered 429. |
| DECODE | `research/sweep_2026-11-11_german/decode_search.py` | Works. |

## Blocked or unreachable

| Host | What happened |
|---|---|
| PARES (pares.cultura.gob.es) | 05:4x UTC: **429** on the first request (`catalogo/find?texto=cifra árabe`). Retry once at 05:55 UTC: **connection reset**. Stopped as instructed. `pares.mcu.es` answered 503. **Simancas, ACA and AHN were not searched live.** The cipher hit lists already harvested (`research/pares_ags/hits.jsonl`, 1,959 ids, and `sweep_2026-11_spain_nobility_aca/hits.jsonl`) were grepped offline for Arabic, Morisco, Moroccan, Algerian and Tunisian words: no Arabic-language cipher item (hits are Spanish letters about the Turk or Tunis, and "Carta del rey de Borneo a Tello escrita en árabe", PARES id 421205, which is Archivo General de Indias, out of scope, and not described as cipher). |
| mcu.es CCBAE (catalogue of the 2018 Simancas exhibition "Servicios secretos y escritura cifrada") | 429 |
| hispana.mcu.es, bvpb.mcu.es | 429 |
| bdh-rd.bne.es, bnedigital.bne.es, datos.bne.es | 403 (WAF page) |
| bibliotecadigital.rah.es (Real Academia de la Historia, Gayangos) | Anubis bot check |
| recherche-anom.culture.gouv.fr (ANOM, Algeria) | Anubis bot check |
| bnrm.ma (Bibliothèque nationale du Royaume du Maroc), simurg.bibliotecas.csic.es (CSIC, Tomás Navarro Tomás) | refused by the network proxy (no connection) |
| bibliotecadigital.aecid.es | connection reset |
| revistaseug.ugr.es (Granada journals) | Anubis bot check |
| jjournals.ju.edu.jo (the 2025 Fasi-pen article) | WAF "Request Rejected" |
| link.springer.com (Azizi 2019) | login redirect; Cryptologia papers paywalled |
| library.oapen.org | 429 twice; the same PDF was taken from the unglue.it mirror |
| brill.com | 403 |
| al-qantara.revistas.csic.es | TLS failure to curl, 503 to WebFetch |
| archives.nat.tn (Tunisia) | redirect only, not searched |

## Search terms and hit counts

**DigitArq, ANTT** (whole archive): "carta em arábico" 11; cifra arábico 1; cifra mouro 29; cifra Marrocos 0;
"em árabe" 335; "cartas árabes" 221; cifrada mouros 1; "em cifra" 308; "letra arábica" 6; cifra Arzila 5; cifra
Tânger 4; cifra Mazagão 3; cifra xarife 0; aljamia 4; "caracteres árabes" 31. The first ten rows of each were read
(the search is fuzzy; the earlier `research/torre_do_tombo/` sweep had run the plain cipher terms over the whole
archive). None joins Arabic and cipher. The hit that mattered is the fonds below.

**Torre do Tombo, PT/TT/CART/891.2, "Documentos em caracteres árabes provenientes dos lugares de África"** (1st half
of the 16th c.; letters of the Sharifs, the rulers of Fez, qaids and townsmen of Safi, Azemmour, Massa, Duccala; "contém
documentos em aljamia"): all 74 units listed and their full records read (descriptions almost empty), and the first
image of every unit viewed (74 of 194 images; for 891.2/08 and /48, whose first image is a wrapper, image 3 too), at
contact-sheet size and, for the two faded letters /55 and /66, at 1,400 px with contrast. **Every one is clear Maghribi
Arabic chancery or private script** (or, for /44 and /68-73, Persian, Indian and Ottoman chancery pieces and labels);
no cipher, no numeral or sign text. Not seen: images 2 and later of the 66 multi-image units (mostly versos,
addresses and Portuguese translations). PT/TT/CART/891.1 (the Oriental counterpart) was not paged. PT/TT/FRA/02.04/0090
("Fragmento com caracteres árabes", 2 images) was not opened (request budget).

**BNE catalogue (Primo)**: "cifra árabe" 8 (photographs, bindings); "escritura secreta" 7 (one modern cipher text of
1917-18 by Agustín Arce, Spanish); "alfabeto secreto" 0; "criptografía árabe" 0; "cifrado aljamiado" 0; "cifra
morisco" 0; "cifrada Marruecos" 0; "caracteres secretos" 0; "escritura cifrada" 61 (printed books, Trithemius, the
18th-c. "Reglas ... para descifrar sin contracifra", none Arabic); cifra AND manuscripts AND Marruecos 2 (20th-c.
French correspondence), Argel 0, Fez 0, Túnez 0, Orán 0, morisco 0, moros 0, arábigo 1 (an 18th-c. palaeographic
alphabet book), jerife 0. **All Arabic-language manuscripts** (`lang,exact,ara` + `rtype,exact,manuscripts`: 702
records, 639 harvested) and **all aljamiado manuscripts** (24): every display field, notes included, grepped for
cifr-, clave, secret-, criptog-, enigm-, alfabet-, abeced-, jerogl-, signos, caracteres raros/desconocidos, escritura
desconocida, guarismo, mu'amma, ta'miya, rumuz, talism-, cabalí-. The hits are foliation "en cifras arábigas",
"signos" of Qur'an vocalisation, a talismanic table book, a 17th-c. book of medical "secretos", magical figures, and
Hegyi's article on the Arabic alphabet among Muslim minorities. **No cipher.** 63 Arabic records beyond the offset cap
were not reached.

**Europeana**: BNE manuscripts with LANGUAGE:ar 0; BNE manuscripts "árabe" 38, "aljamiado" 2 (all read); Spain:
cifra AND (árabe OR arábigo OR arábiga OR morisco OR aljamía OR aljamiado) 5 (watches), cifrada AND (árabe OR arábigo
OR moro OR Marruecos OR Argel) 0, "caracteres arábigos" 9, "escritura secreta" 0, "alfabeto secreto" 0; all providers:
"carta en árabe" 2, "en caracteres árabes" AND carta 7, "cifra arábiga" 0, chiffre AND arabe AND lettre AND sultan 4.
Nothing.

**BNP**: arab* cifr* 0; arab* caracteres 40 (printed books, a Qur'an of 1612); arab* segredo 1 (modern book);
aljamia 3 (David Lopes, Textos em aljamia portuguesa); arab* chave 0; mouro* cifr* 1 (Tarouca papers, European).

**Archives du Maroc web search**: تشفير 0, مشفرة 0, الرموز السرية 0, chiffre 0.

**Catalogues on archive.org, grepped** (écriture secrète, chiffr-, cryptog-, caractères secrets/conventionnels/de
convention/inconnus, alphabet secret, écriture conventionnelle/inconnue, cifrad-, en cifra, descifr-, escritura
secreta/cifrada/desconocida, alfabeto secreto, caracteres secretos/desconocidos, criptogr-, ta'miya, mu'amma; for the
Spanish ones also clave, secret-, alfabet-, signos, caracteres): Derenbourg, *Les manuscrits arabes de l'Escurial* I
(two scans: `lesmanuscritsara01dereuoft`, `india.history.resource.89832`) and II.1 (`p1lesmanuscriarab02dereuoft`);
Guillén Robles, BNE Arabic catalogue 1889; *Catálogo de los manuscritos árabes ... Universidad de Granada* 1899; Ribera
and Asín, *Manuscritos árabes y aljamiados de la Junta* 1912 (only magical "signos cabalísticos" and a sun-degree
"clave"); Casiri, *Bibliotheca Arabico-Hispana Escurialensis* I-II with Latin terms (arcan-, occult-, cryptog-,
aenigm-, characteribus ...): the only relevant item is a mu'amma treatise of 995/1586 (Casiri I, from the Moroccan
royal library), not a lead. The 15 Nov part C had grepped Casiri, Derenbourg II.2, Guillén Robles and Ribera-Asín with
French terms; the new passes add Derenbourg I and II.1, Granada 1899 and the Spanish and Latin terms. No hit.
Not found as text: Derenbourg III (Lévi-Provençal 1928), Saavedra's *Índice general de la literatura aljamiada*
(1878; the Saavedra item found, `discursosledosa00saavgoog`, is a different discourse), Terés's RAH Gayangos
catalogue, Alarcón and García de Linares's ACA *Documentos árabes diplomáticos* (1940).

**Journals on archive.org, grepped**: *Hespéris* 1921-1959, every year (40 files): cryptogra-, écriture secrète,
caractères secrets/conventionnels, alphabet secret, lettres chiffrées, dépêches chiffrées, non déchiffré, langue
secrète, code secret. Hits: only Colin 1927 and later citations of it (1932, 1936, 1945, 1953: Anun "inventor of the
cryptographic system of the Second Bureau"), a Tuareg language game (1937), a Kabbalistic substitution (1953).
*Revue africaine* (Alger): the general table of 106 volumes and the 2 bibliometric theses: no article on cryptography
(only "Les chiffres arabes", 1872, numerals). *Archives marocaines* and *Revue tunisienne* were not grepped.

**Web searches (about 16)**: Azizi and Azizi on Moroccan cryptography (references taken from Crossref; papers not
opened); Tazi 1983 in Arabic; al-Manuni and Makhzen *ramz*; Nasrid cryptography; Morisco secret alphabets and the
Inquisition; Arabic cipher letters at Simancas; ACA Arabic letters and cipher; the Simancas exhibition catalogue; the
Rif war (Abd el-Krim) ciphers; Cryptiana and Morocco; then six for the Sacromonte lead (listed in its vetting block).
None named a digitised unread Arabic cipher letter.

## Finds

1. **Sacromonte Lead Book 17, *Ḥaqīqat al-Injīl*, "Libro mudo"** (found 31 Dec 1597; forged c. 1595-97). 16 lead
   plates; plates 2-6 (7?) carry 9-10 lines each of an engraved cryptic script, numbered in dots; plate 1a is a Seal
   of Solomon whose Arabic legend (read) calls the text "maqlūbat al-ʿallāma". Van Koningsveld and Wiegers 2024
   (ch. 6, pp. 113-115; edition entry p. 348): "a cryptic script ... that has baffled all scholars who have worked with
   these materials, including the experts of the seventeenth-century Vatican Commission"; "an undeciphered cryptic
   script"; they lean to pseudo-cryptography because the sign inventory is larger than the Arabic alphabet. Fol. 3b
   (fig. 14) viewed at 1,313 x 1,317 px: 10 ruled lines of angular signs in word-like groups with dot clusters; no
   reading. Sibling: one line of cryptic script in lp16, fol. 6a (fig. 29, p. 332). The Libro mudo is not in the
   repository, not on DECODE and not in Tomokiyo's list. **Vetted, open** (see the caveats below). Not before 1400, so
   no message to main.

   Caveats for the reviewer: (a) the published photograph is 1,313 px across, below the 1,500 px guide, though it is the
   native resolution of the only image online and covers a 74 mm plate (about 450 px per inch; signs and dots are
   distinct); (b) only one of the five or six cipher plates is online; (c) the editors think the script may be
   meaningless; (d) Hagerty 1980 and Barrios Aguilera 2011 were not opened; (e) the Lead Books are a famous affair,
   but the Libro mudo is not in `FAMOUS` in `docs/_check_writeup.py`.

## Closed or not a lead

- **Colin, "Note sur le système cryptographique du sultan Ahmad al-Mansur", Hespéris 7 (1927) 221-228**: re-read here
  (archive.org `hesperis-tamuda-1927_202511`). Confirms the 15 Nov wave-15 reading: a key (28 signs, Maghribi abjad
  order, partly torn) from the flyleaf of the "manuscrit Cerdeira", no ciphertext; the Anun note of 1009/1600-01 is
  described, not reproduced. Colin also cites the Almohad secretary Mallul ibn Ibrahim al-Sanhaji, who could write
  "Syriac" and cryptograms (Lévi-Provençal, *Documents inédits d'histoire almohade*, Paris 1927, text p. 39, as cited by Colin):
  a mention, no ciphertext.
- **Torre do Tombo CART 891.2** (74 Arabic letters from Morocco, 16th c.): first images all clear script; not cipher.
- **BNE Mss. of Morisco magic** ("Miscelánea de textos moriscos sobre magia y medicina", "Cuadros talismánicos",
  "Encantamientos", "Ensalmos y conjuros"; Junta MSS with "signos cabalísticos"): magical charakteres by description;
  not opened; excluded by the brief.
- **Casiri I, MS of 995/1586 from the Moroccan royal library**: a mu'amma (enigma) treatise; excluded.

## Key leads (no ciphertext)

- **Colin 1927 key** (Saadian, c. 1600): printed with plate, p. 224. Already noted by the 15 Nov wave-15 sweep.
- **Decourdemanche, table of the "système cryptographique utilisé par les Turcs des États barbaresques"**, *Journal
  asiatique* 9e série t. XIV (1899) p. 267, as cited by Colin 1927 p. 228. Ottoman Barbary (Algiers/Tunis) cipher
  alphabet. Not opened: the 1899 JA volume on archive.org (`journalasiatiqu79fragoog`) is not tome XIV, and the
  Indian DLI scans stop at tomes 9-11, 16, 17, 20. Would serve any Ottoman-Arabic cipher letter from the regencies.
- **Magical alphabets of Ibn Wahshiyya and al-Jildaki**: cited by van Koningsveld and Wiegers as the family nearest the
  Libro mudo script (the editors used a private manuscript of al-Jildaki's *Durrat al-ghawwas*).

## Side leads (Persian, Ottoman)

- PT/TT/CART/891.2/68-73 and 891.2/44: Ottoman/Persian divani pieces and Indian rulers' letters in clear; no cipher.
- Decourdemanche's Barbary Ottoman cipher table (above).

## What is left

- **Spain, live**: PARES (Simancas Estado, Guerra Antigua, Secretarías Provinciales; ACA Cancillería "Cartas árabes";
  AHN Inquisición Morisco processes) with the terms "cifra árabe", "en arábigo" + cifra, "caracteres", aljamiado,
  Marruecos/Fez/sultán/jarife + cifra, Argel/Túnez + cifra. Needs another network or a later hour. Hispana, BVPB,
  BDH, RAH digital (Gayangos), CSIC Simurg likewise.
- **BNE**: the 63 Arabic manuscripts beyond the Primo offset cap (try `sort=author` or a date split); Primo terms for
  "lengua arábiga", "letra arábiga" + cifra in archival collections.
- **Torre do Tombo**: images 2 and later of the 891.2 units; the whole of 891.1; PT/TT/FRA/02.04/0090; the Gavetas and
  Corpo Cronológico letters "em arábico" (the Portuguese cipher letters there are European-language and out of scope).
- **Sacromonte**: images of lp17 plates 2, 4-7 (Sacromonte Abbey or Vatican photographs iii, 1-16); Hagerty 1980;
  the two other lead books with a few words of the same script (lp16 fol. 6a seen; the third not identified).
- **Maghreb**: Tazi 1983 and the Azizi papers (paywalled/not online) for named Makhzen cipher letters; the Moroccan
  royal archives (no online catalogue found); ANOM (Anubis) for Abd el-Kader and the beylik correspondence; Tunisian
  national archives (not searched); *Archives marocaines*, *Revue tunisienne* full text; Decourdemanche 1899.
