# Wave 16: Chrome pass over the sources wave 15 could not reach by script (15 Nov 2026)

One Chrome tab, one request at a time. Sources: KBR, Memoria digital de Canarias, Comunidad de Madrid, Sardinia and Sicily,
Nijmegen, PARES (if time). Rows: `candidates.json`. No CAPTCHA or human check was clicked anywhere.

## 1. KBR (Royal Library of Belgium), `opac.kbr.be`

**Route that works (Chrome only; scripts get a connection reset).** Open any search page, e.g.
`https://opac.kbr.be/Library/search.aspx?SC=DEFAULT&QUERY=chiffre`, then page the Syracuse search service from the page itself:

```
POST /Library/Portal/Recherche/Search.svc/Search   Content-Type: application/json
{"query":{"InitialSearch":true,"Page":0,"PageRange":3,"QueryString":"<term>","ResultSize":50,
          "ScenarioCode":"DEFAULT","SearchContext":0,"SearchLabel":""}}
```

The answer is JSON: `d.SearchInfo.NBResults`, `d.Results[].Resource.RscId` / `.Type`, `d.Results[].CustomResult` (HTML of the short
record), `d.FacetCollectionList` (facet 58 = "Type de document"). To filter by document type add
`"FacetFilter":"{\"_58\":\"Manuscrit\"}"` and `"InitialSearch":false`. One search takes about 10 s. A record is at
`https://opac.kbr.be/Library/doc/SYRACUSE/<RscId>` (drawn by script, about 10 s). `GetRecord` was refused ("Votre recherche a échoué").

The 9 Nov note that the OPAC holds no manuscripts is not right: it has the document types **Manuscrit** and **Correspondance**
("lettre autographe": Correspondance 5,312, Manuscrit 322), and a manuscript record carries a "Contient (note)" field keyed from the
card catalogue ("Fichebak"), which the search reads. The search is stemmed and accent-blind (chiffre = chiffré = chiffres).

`https://belgica.kbr.be/` (redirects to `/belgica/`) is the same Syracuse index (`/BELGICA/Portal/Recherche/Search.svc/Search`;
"chiffre" gives the same 18,596): no separate search was needed.

**Terms run, all types / Manuscrit / Correspondance** (55 terms; every Manuscrit and Correspondance hit read):
chiffre, chiffré, chiffres 18,596 / 1 / 0 (the one manuscript is ms. G 116, "le chiffre de leur population en 1709"); chiffrée 2,548 / 0 / 0;
"en chiffres", "en chiffre" 3,932 / 0 / 0; "lettre chiffrée", "lettres chiffrées" 1 (a printed book); "correspondance chiffrée" 1 (book);
"dépêche chiffrée" 25 (periodicals); "table de chiffre" 1; "clef du chiffre" 2 (Farago's book); déchiffrement 633, déchiffré 635,
déchiffrer 632 / 0 / 0; cijferschrift 15 (song books in number notation); geheimschrift 46 (novels, Singh); "geheim schrift" 12;
"in cijfers" 1,994; cijfers 13,980; cyfers 2 / 1 (ms. II 564, an arithmetic of 1624); cijffer 1; cyfer 31; cifra, cifre 109; "in cifra" 2;
"en cifra" 30; cifrado 5; cifrada 41; zifra 1; cipher 37 (printed; telegraph signal books); cryptographie 162 / 1 / 0; cryptogramme 17;
cryptogram 36; "écriture secrète" 25; "code secret" 154; "code télégraphique" 19; ziffern 21; Ziffer 121; chiffer 183; chifre 11;
steganographie 25; "caractères secrets" 32; "alphabet secret" 1; "lettres secrètes" 239; "langage convenu" 5; "écrit en chiffre" 3;
"chiffres diplomatiques" 1; polygraphie 400 / 0 / 1 (a photograph); "notes tironiennes" 9; "caractères inconnus" 5; "onbekend schrift" 259;
indéchiffrable 81 / 0 / 1 (a signature); "non déchiffré" 2; geheime brieven 806; and the word pairs "en chiffres" lettre, chiffre lettres
manuscrit, chiffre ambassadeur, secretaris cijfer, hiéroglyphes clef, "clef" chiffre: no Manuscrit or Correspondance record.

**Result: 0 rows.** One note for vetting, not a row: **Ms. II 4525** (record 10715130; 18th century, Dutch and French, paper): "Recueil de
poésies. Chansons à boire. Dialogue entre l'empereur et le Royaume ... de Sicilië. Occurence de la Campagne 1735", "Contient (note): Lettre
à Van Huffel, pasteur d'Uysen. cryptographie. Campagnes de Louis XV ...". The card says only "cryptographie": a treatise, a key or a cipher
text, not known. No digitisation linked. The KBR OPAC does not describe letters at a level where cipher is mentioned: the 5,312
"Correspondance" records are autograph letters and photographs with no content notes on cipher.

## 2. Memoria digital de Canarias (`mdc.ulpgc.es`)

**Route.** The Anubis page passes by itself in Chrome (no interaction asked). The site has moved from CONTENTdm to Omeka S: the old
`/digital/search/searchterm/<term>` address is now "Página no encontrada". Search: `https://mdc.ulpgc.es/s/mdc/busqueda?q=<term>&page=N`
(20 a page; the count is the "N fichas" line; same-origin `fetch` works). Items: `/s/mdc/item/<id>`. It searches record metadata, not the
full text of the scans.

Terms (hits): cifra 32, cifras 27, clave 113, criptografía 3, descifrar 2; cifrado, cifrada, cifradas, "en cifra", descifrado, "escritura
secreta", "carta cifrada", "lenguaje cifrado", "telegrama cifrado" 0. All titles of cifra and cifras read: journal articles (Pasos, Cartas
diferentes, Botánica macaronésica, Matematicalia) and 20 minute-book entries of the Heredad de aguas de Arucas y Firgas, 1884-1939 (sums of
money). "clave" is "palabras clave". **0 rows.** mdC holds journals, photographs, a water-company archive and printed texts; no diplomatic
or private letters described at item level.

Other Canarian portals: not searched. No item-level online catalogue address is known for the Archivos Históricos Provinciales of Las
Palmas and Santa Cruz de Tenerife or for El Museo Canario's Inquisition archive (wave 15 looked for one); Jable is a newspaper archive.

## 3. Madrid

### Comunidad de Madrid, Archivo Regional (AtoM): needs the owner

`https://gestiona.comunidad.madrid/archivos_atom/index.php/informationobject/browse?topLod=0&query=cifra` shows, in Chrome too, a
"Verificación de Seguridad" page with an ALTCHA box ("Por favor, resuelve el reto de seguridad para confirmar que eres humano. I'm not a
robot"). It asks for a click, so it was **not touched**. Not searched. Daniel has to tick it once in the tab; after that the AtoM browse
URL above should page as any AtoM does (`&page=N`, `&sort=relevance`).

### Memoria de Madrid (`www.memoriademadrid.es`)

**Route.** `buscador.php` is gone ("Access Denied" from Akamai, in Chrome as well). The site is new (2025): the home page
`https://www.memoriademadrid.es/` loads in Chrome, and the search is
`https://www.memoriademadrid.es/browse?q=must,any_exclude_fulltext,contains,<term>&limit=100` (same-origin `fetch`; the field
`any_exclude_fulltext` is "Cualquiera" without OCR; plain `any` adds the OCR of the newspapers and returns tens of thousands, e.g. cifra
50,841). A phrase is searched as its words (OR), so "escritura secreta" and "en clave" return noise. The result page carries every record
in full as JSON in its script (`var objects = [...]`: `_source.metadata.source` = shelfmark, `.description`, `.matiz_de_fecha`,
`_source.id`); a record is `https://www.memoriademadrid.es/view/<id>`, its scan `/viewer/<id>`.

Terms (records, without OCR): cifra 31, cifrado 9, cifrada 13, cifradas 0, "en cifra" 24, cifras 12, descifrado 7, clave 3,395
(not read: "palabra clave", calle del Clavel), criptografía, "escritura secreta", "carta cifrada", descifrar, desciframiento, cifrar:
only noise beyond the series below. The portal holds the Biblioteca Histórica Municipal, the Hemeroteca, the museums and a small part of
the Archivo de Villa; no Archivo de Villa record carries a cipher word.

**Nothing new: 0 rows.** The only cipher items are the reales cédulas of Philip III to Rodrigo Niño Laso, conde de Añover, 1610-11
(Biblioteca Histórica, I 242 and I 243), already catalogue entry 1988 / `targets/anover1610`. For that entry, the portal's own
descriptions settle which leaves have a decipherment filed (field "description"):

| Shelfmark | view id | Date | Decipherment in the description |
|---|---|---|---|
| I 242,29 | 424541 | 1610 (Lerma) | none (written up, anover1610) |
| I 242,35 | 424529 | 1610 | none |
| I 242,59 | 425639 | Lerma, 10 May 1610 | none |
| I 242,60 | 425637 | Lerma, 10 May 1610 | none; incipit quoted in cipher: "15 h032 ji 54 33 7520 fil 361573..."; "Triplicada" |
| I 242,33 | 424533 | 1610 | "+ 1 hoja con el texto descifrado" |
| I 242,39 | 424745 | Aranjuez, 27 Jan 1610 | deciphered |
| I 242,42 | 424739 | 1610 | deciphered |
| I 242,47 | 424869 | 1610 | deciphered |
| I 242,48 | 424867 | 1610 | deciphered |
| I 242,66 | 425625 | San Lorenzo, 23 Jul 1611 (keyed "16911") | deciphered |
| I 242,71 | 425615 | Madrid, 20 Feb 1611 | deciphered |
| I 243,18 | 425791 | Lerma, 30 Apr 1610 | "en parte cifrada", deciphered |

So the three open leaves of entry 1988 are I 242,35, I 242,59 and I 242,60 (as Brice Dudout named them). Images were not opened here.

## 4. Sardinia and Sicily: not reachable from this line, in Chrome either

Not a bot check: the hosts do not answer this machine at all. Chrome shows its own error page (`chrome-error://chromewebdata/`), with
nothing to click, for `https://archiviostatocagliari.org/`, `https://sias-archivi.cultura.gov.it/`, `https://asmessina.cultura.gov.it/`
and `http://sardegnaarchiviovirtuale.it/`. DNS and curl from the same machine (15 Nov):

| Host | DNS | HTTPS |
|---|---|---|
| archiviostatocagliari.org | 2.42.228.64 | no connection |
| sa-sardegna.cultura.gov.it | 2.42.228.47 | no connection |
| sias-archivi.cultura.gov.it | 2.42.229.112 | no connection |
| asmessina.cultura.gov.it | 2.42.229.31 | no connection |
| archiviodistatosiracusa.cultura.gov.it | 2.42.229.31 | no connection |
| archiviodistatotrapani.cultura.gov.it | 2.42.229.61 | no connection |
| sardegnaarchiviovirtuale.it | 195.130.213.74 | no connection |
| archiviodistatocagliari.cultura.gov.it, archiviodistatomessina..., archiviodistatocatania..., ascatania..., www.archiviodistatocagliari.it, www.sardegnaarchiviovirtuale.it | no DNS answer | |

Every resolving Ministry host sits in 2.42.228.0/23, the range that has reset this machine since the ASNa sweeps; the resolver here is
10.2.0.1, which looks like a VPN, and the Ministry network most likely drops that exit. **Needs another line (VPN off or another
network), not a click.** Nothing searched; 0 rows. No terms run.

## 5. Regionaal Archief Nijmegen (`studiezaal.nijmegen.nl`): 403 in Chrome too

`https://studiezaal.nijmegen.nl/` and `https://studiezaal.nijmegen.nl/ran/_resultaat.aspx?zoekterm=geheimschrift` both answer
"403 - Forbidden. U heeft geen toegang tot deze pagina." in the owner's Chrome, with no check to pass. An address block (the same
VPN exit, probably), not a bot check. The result address the archive's own site links to,
`https://studiezaal.nijmegen.nl/zoeken/groep=Archieven en archiefstukken/Vrij_zoeken=<term>`, is refused the same way.

**Part route: counts only.** The archive's main site answers (`https://regionaalarchiefnijmegen.nl/`), and its "Zoeken door alles" asks
the studiezaal on the server side: `https://regionaalarchiefnijmegen.nl/zoeken-door-alles?trefwoord=<term>&view=instance&instance=deventit&tmpl=raw`
returns the hit counts per group (Archieven, Beeldbank, Kranten, Bibliotheek ...), not the records. Archieven counts:
geheimschrift 0, cijferschrift 0, "in cijferschrift" 0, cijfercode 0, "in code" 0, codetelegram 0, ontcijferd 0, chiffre 0, cryptografie 0,
ontcijfering 1, "geheime code" 1 (word match, not a phrase), gecodeerd 3, "in cijfers" 31, "sleutel cijfer" 53, code 218, cijfer 222
(the last four are statistics, grades and building codes by every sign; not opened, the records are behind the 403).
Kranten (newspapers): geheimschrift 137, cijferschrift 120. **0 rows.** With the two exact cipher words at zero in the archive
descriptions, Nijmegen is very likely empty; the 1 "ontcijfering" and 3 "gecodeerd" records are the only ones worth opening from
another line.

## 6. PARES: 429 at the first request

`https://pares.cultura.gob.es/ParesBusquedas20/catalogo/find?nm=&texto=cifra&anio1=1400&anio2=1799` answered "429 Too Many Requests" in
Chrome on the first and only request of this wave (the IP-wide limit noted on 28-29 Oct and in the Arabic sweep). Stopped there, as
briefed. Nothing searched.

## Added along the way: Biblioteca Histórica Municipal de Madrid catalogue (AbsysNet)

`https://bibliotecasespecializadas.madrid.es/cgi-bin/historica?ACC=101` opens in Chrome (a session token is put in the path). The home
search box works; from a result page the same form can be re-posted from the page (`ACC=131, xsface=on, xsfind=1, START=1, subcat,
xsqf01=<words>`; pages are ISO-8859-1; words are ANDed). A direct POST from the home page form returned the form again, so the first
search was typed into the box. Records: `...?TITN=<n>`. The page template carries a reCAPTCHA key for the login form; the search asked for
no check and none was touched. This catalogue covers the library's manuscripts whether digitised or not.
Searches: cifrada 13; "cifra manuscrito" 12; "cifrado manuscrito" 3; "descifrado manuscrito" 7; "descifrada manuscrito" 1; "cifras
manuscrito" 12; "cifra carta" 3; "en cifra" 8; "clave manuscrito" 50 (music manuscripts, "clave" = harpsichord or clef); criptografía,
cifrar, descifrar, "caracteres secretos" with "manuscrito", nomenclator, contracifra, cifrario 0. Beyond the Añover cédulas: Comella's
opera "La cifra" (1799), a 1674-83 juro, "Papeles varios curiosos" (1775-1800; "cifras de las rentas provinciales"), printed books.
**Nothing new.** The library holds no cipher letter other than the Añover series, as far as its catalogue says.

## Result

`candidates.json` is `[]`: no new item qualifies. What this wave adds is routes and closures:

| Source | State after this wave |
|---|---|
| KBR OPAC / Belgica | swept (55 terms, Manuscrit and Correspondance types read); nothing; Ms. II 4525 "cryptographie" noted |
| Memoria digital de Canarias | swept (14 terms); nothing; other Canarian archives have no item catalogue online that we know of |
| Memoria de Madrid + Biblioteca Histórica catalogue | swept; only the Añover series (catalogue 1988), with the list of which leaves have a decipherment |
| Comunidad de Madrid AtoM | **needs Daniel**: ALTCHA "I'm not a robot" box |
| Sardinia, Sicily (Ministry hosts) | **needs another line**: no connection from this machine, Chrome included |
| Nijmegen studiezaal | **needs another line**: 403 in Chrome; counts through the main site say 0 for geheimschrift and cijferschrift |
| PARES | 429 on the first request; not searched |

Not seen or reached: any image (nothing new to look at); the three open Añover leaves (I 242,35, 59, 60) were not opened; KBR Ms. II 4525
was not seen and has no scan linked; the KBR types other than Manuscrit and Correspondance were read only for the small terms
(all printed matter, periodicals, music); the "Affaires étrangères" document type in the KBR OPAC (734 hits for "chiffre") was sampled
through three terms only and looked like the printed library of the Foreign Ministry (Farago, Langie), not archive files.

Chrome use: one tab at a time, created for this sweep (the first was closed after the Ministry hosts left it on an error page, a second
opened), closed at the end. The owner's APD tab was not touched.

