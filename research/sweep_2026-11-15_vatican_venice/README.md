# Vatican and Venice sweep, 15 Nov 2026

Result: **0 candidate rows** (`candidates.json` is `[]`), 4 minor key leads (`key_leads.json`). Every route requested was run or
re-checked; each is either already saturated by an earlier sweep or has no item-level text. No Chrome was needed except one
failed attempt (below). Nothing edited outside this folder.

## 1. Archivio Apostolico Vaticano
- `www.archivioapostolicovaticano.va` answers curl with a browser User-Agent (the root is 200; the old /content/archivioapostolicovaticano path is 404).
  The site has no inventory search, no "atlante"/Mensa interface and no inventory PDFs. The only finding aid is
  `/content/dam/aav/documenti/Indice dei Fondi e relativi mezzi di descrizione e di ricerca.pdf` (3.2 MB, 106 pp., downloaded to
  `dl/aav_indice.pdf`, text in `dl/aav_indice.txt`). It is fonds level: grep for cifr/decifr gives only the fonds
  "Ufficio Cifra" (Segreteria di Stato). No Nunziature item list, no "in cifra" notes.
- archive.org advanced search for "indice nunziature": 0 titles. A web search for item-level inventories with cipher notes returned
  only the Nunziatura in Italia 1929-58 inventories (Collectanea Archivi Vaticani), 20th century, not cipher listings.
- Conclusion: no item-level online route for AAV cipher letters; DECODE remains the only index (see `research/vat_vatican`).

## 2. BAV OPAC (opac.vatlib.it/mss/search), letter volumes
- Route as in `sweep_2026-11_vatlib_letters` (browser UA + cookie + Referer, 1.1 s pacing, no 429). `opac.py`, `items.py`, `probe.py` copied here.
- 16 new terms/wildcards: `decifrat*` 39, `decifrazion*` 2, `cifrat*` 5, `cifrar*` 6, `cifr* lettere` / `lettere cifr*` 73, `cifra nunzio` 4,
  `cifra Barberini` 6, `cifre Spagna` 35, `cifre Francia` 19, `cifre* decifr*` 33, `dispacci cifr*` 0, `avvisi cifra` 0, `cifra Germania` 0,
  `zifr*` 0. Harvest in `hits.jsonl`. **Every shelfmark returned was already in the shelfmark sets of `sweep_2026-11_digivatlib` and
  `sweep_2026-11_vatlib_letters` (426 shelfmarks): zero new volumes.** The OPAC route is closed for volumes with item-level notes.
- Re-read the 119 stored item records for Barb./Chig./Ott./Urb./Ross./Ferr./Cappon./Borg. entries mentioning cifra but not decifr/interpretazione.
  All are existing rows (Barb. 9863, 9885-86, 9892; Borg. 587) or already closed (Cappon. 164, Urb. lat. 1704 = lead 1918); the rest are
  mentions (Barb. 9845 f. 50r asks for the diplomatic cipher; Barb. 9812 f. 76r returns cipher instructions; Cappon. 281 f. 117r letter about a cipher), see `key_leads.json`.
- Digitisation probe (3 s pacing, GET manifest): **Chig. A.I.35-60 are not digitised** (404 for all 26; `chig_probe.txt`). Chig. A.I.4, 6, 7, 8, 20-23, 25
  were digitised and sampled in the earlier sweep (clear text).
- Not reached (unchanged): Barb. lat. 6000-9800 volumes without item descriptions (about 3,800 manifests at 3 s = 3+ hours, then contact sheets);
  Ott./Urb. avvisi/ambassador volumes, Ross., Ferr.: no OPAC handle, so no shelfmark list to probe. These need the Sala Cons. Mss. inventories.

## 3. Venice
- ASVe moreveneto GraphQL (route of `research/venice_archives`): 11 further terms (`lettera cifrata` 0, `lettere cifrate` 0, `dispacci cifrati` 1, `chiave di cifra` 1,
  `cifrato` 1, `zifrato`/`zifrate`/`ciffra`/`decifrar`/`cifrare` 0, `scontro` 43). Only hits: the known Senato *Deciferazioni* series and the Dieci *Cifre, chiavi e
  scontri di cifra* series (already key leads). `scontro` = skirmish or ledger reconciliation (Scuole grandi, Miscellanea documenti turchi 1334 of 1626, 701 of 1552, 158 of 1504: all noise).
  Item-level description of the Dieci Cifre series is still absent (restricted access).
- Marciana: Manus Online lists two Marciana records for the cifra terms (Gozzi 9.9, 12.3, folio-number "cifra"): noise. A web search for Marciana Ital. cl. VII cipher
  codices found nothing; the Marciana catalogue is not in Manus for the diplomatic codices, so no handle.

## 4. Manus Online: Ambrosiana, Trivulziana, Estense, Casanatense, other libraries
- `manus.py` ran 23 queries (AND mode, combined with dispacci, carteggio, ambasciatore, nunzio, lettere, lettere cifrate, cifrario, decifrazione, library and fondo names):
  328 distinct records (`dl/manus_all.json`). The detail JSON route `GET /o/manus-api/title?id=<id>` works (the HTML detail URL does not; Chrome tab was tried and closed).
  Read 34 detail records of the early-modern, letter-type survivors (Redi 214/215, Corsini 188/190/193, Riccardiano 3811/3814, Sessoriano 341, Vitt. Em. 598/1680,
  ex-Vind. Lat. 72, Aldrovandi 38/2, Ambrosiana G 119 inf., Casanatense 935/1108/1122/1161/1186/1211/1212/1830, Alessandrina, Angelica, Trivulzio 324, Padova 272,
  Marciana Gozzi): every hit is "cifra" = a sum, a numeral, a shelfmark digit, the post "segretario della Cifra" (Alamanni, Clement XI) or "decifrazione" = handwriting.
- All the real hits (APUG Concilio di Trento 242rec/588rec/608rec, Marsili 75/C, Bigazzi 303, Casanatense 1309, Vitt. Em. 1680, Gal. 12, Ambrosiana G 275 inf.) were already in
  `sweep_2026-11_manus_italian_libs` and `sweep_2026-11_B_unswept_south`. Estense Lat. hits are the same foliation noise.
- Dedupe: `known.py` on all candidates' shelfmarks. No new row survived.

## Notes for next time
- COVERAGE: AAV has no item route (Indice dei Fondi PDF only); Chig. A.I.35-60 not digitised; OPAC term harvest saturated (16 new terms, 0 new volumes).
- Remaining unswept work is image-level: Barb. lat. 6000-9800 manifest probe plus contact sheets, and Internet Culturale full text via Chrome (see COVERAGE).
