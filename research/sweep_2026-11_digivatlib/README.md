# DigiVatLib / BAV manuscripts OPAC sweep, 6 Nov 2026

Result: **6 rows** in `candidates.json` (2 seen bare on DigiVatLib images, 4 undigitised and scored from the OPAC
record), **8 key and treatise items** in `keys.json`, and vetting evidence that closes all four existing BAV leads
from the 2 Nov sweep (see "Existing leads" below). About 2 hours, roughly one request a second, no browser.

## Routes (plain curl / urllib from this network, 6 Nov 2026)

- `https://digi.vatlib.it/` answers 200. COVERAGE's "connection reset in Chrome, TLS error in curl" no longer holds here.
- **DigiVatLib search** `https://digi.vatlib.it/search?k_f=0&k_v=<term>&r=100&p=<n>` returns 403 to a bare curl, but
  200 with a browser User-Agent, the cookie set by `https://digi.vatlib.it/` and `Referer: https://digi.vatlib.it/`.
  It indexes digitised volumes only (34 records for `cifra`).
- **BAV manuscripts OPAC** (the better index): `https://opac.vatlib.it/mss/search?k_f=0&k_v=<term>&r=100&p=<n>`, same
  headers, cookie from `https://opac.vatlib.it/mss/`. It covers digitised and undigitised volumes (49 records for
  `cifra`, 20 of them undigitised), **accepts `*` wildcards**, and has a Digitized / Not Digitized facet. Result blocks
  give the shelfmark, a not-digitised flag and the matching items with their numeric ids.
- **Item records** `https://opac.vatlib.it/mss/detail/<numeric id>` hold the Summary and General note, where the cipher
  word sits ("Cifre e decifrati", "In cifra", "Testo cifr. con interpretazione"). The shelfmark page
  `https://opac.vatlib.it/mss/detail/<Shelfmark>` lists the items without those notes.
- **IIIF**: manifests `https://digi.vatlib.it/iiif/MSS_<Shelfmark>/manifest.json` (Presentation 2; 404 = not
  digitised; canvas labels are folio numbers such as `298r`, with suffixes like `105r.[01.mn.0000]` for inserted slips).
  Images: the canvas service id + `/full/1600,/0/default.jpg` (a bottom copyright bar is composited in; region requests
  `/<x>,<y>,<w>,<h>/2000,/0/default.jpg` work on the full-size grid).
- **Printed catalogues on archive.org** (OCR `_djvu.txt`, grepped): `bavcodicesvaticanilatini9852` (Vat. lat.
  9852-10300, 1914), `bavcodicesvaticanilatini10301` (10301-10700, 1920), `codicesurbinates02bibluoft` and
  `codicesurbinates03bibluoft` (Urb. lat. 501-1779). No Barberini, Ottoboni or Chigi catalogue is on archive.org.
- Scripts: `opac.py` (term harvest), `items.py` (item records), `img.py` (IIIF image by folio label);
  `opac_items.jsonl` keeps the 119 item records whose notes really mention a cipher.

## Terms and hits (OPAC)

`cifra` 41, `cifr*` 185, `in cifra` 28, `decifr*`/`decif*` 42, `chiffr*` 133 (almost all Arabic manuscripts, the
French "chiffres" of folio counts), `ziffer*` 10 (a scholar named Ziffer), `cryptograph*` 9, `decipher*` 5,
`scrittura segreta` 4, `contrasegn*` 2, `dechiffr*` 2; zero for `zifr*`, `ziffr*`, `cifer*`, `zifer*`, `ciffr*`,
`dicifr*`, `deciffr*`, `cypher*`, `cifrad*`, `contracifr*`, `steganograph*`, `cyfr*`, `ciphr*`, `alfabeto segreto`.
`chiave*`, `alfabet*`, `nomenclat*`, `interpretazione` and `occult*` were tried and are noise.
356 shelfmarks; after dropping the oriental, Greek and bibliography-only hits, 228 item records were read, of which 119
mention a cipher. Most `cifr*` hits are foliation notes ("cifre arabiche") or musical and numeric uses.

In the printed catalogues: Vat. lat. 10409, 10421, 10440, 9955; Urb. lat. 839, 868, 879, 882, 948, 949, 998, 1035.

## Rows (candidates.json)

| Shelfmark | Folios | Date | Who | State |
|---|---|---|---|---|
| Vat. lat. 8214 | 298r-v | 1524 | Mantuan informant -> Federico II Gonzaga | seen, bare (A) |
| Borgh. 239 | 16r margin | codex s. XIV | unknown, about 26 signs | seen, bare (B) |
| Barb. lat. 9892 | 313r | 5 Feb 1641 | Luis Revelo -> Card. Francesco Barberini | "In cifra", not digitised (B) |
| Borg. lat. 587 | 37r-231r, key 141r | 1665-66 | Domenico Giannuzzi -> nuncio Marco Gallio, Cologne | partly cipher + enclosed key, not digitised (B) |
| Barb. lat. 9885-9886 | 1r-152r | 1701-04 | G. B. Facini (Madrid) -> Urbano Barberini, G. Valuta | "Cifre" (no "decifrati"), not digitised (B) |
| Barb. lat. 9863 | 479r, 505r-507r | Nov 1669 | D. Millanta <-> nuncio Federico Borromeo, Madrid | "Cifra"/"Cifre", not digitised (C) |

known.py, catalogue.json and research/leads.json: no hit for any of these shelfmarks or correspondents.

## Not rows: glossed, deciphered or studied

- **Barberini agents in Madrid, "Cifre e decifrati"** (OPAC general note on every volume): Francesco Mancini 1644-55
  (Barb. lat. 9848-9849, digitised; 9849 f. 107r opened, clear), letters to Attilio Marcellini (9850-9852), Nicolò
  Ricci 1654-68 (9853-9855; 9853 f. 73r "Lettera decifrata"), Domenico Millanta 1666-79 (9859-9875; 9871 has "Cifre
  ai ff. 249r-270r e decifrati"), Martin Perez Costes (9877), Nicolò Arpe 1682-99 (9878-9882), Facini 1698-1700
  (9883-9884). All undigitised except 9848-9849. These are the key source for the Facini row; individual letters whose
  decipherment is missing could still turn up on a page-by-page pass of 9848-9849.
- Barb. lat. 9846 (Egidio Sforzini 1642, "Testo in cifra e decifrato"; f. 75r is a minute about the cipher
  correspondence for the Castro war), Barb. lat. 9866 f. 47r and 249r-255v, 9867 ff. 492r-499v, 9868 ff. 335r-337r,
  9876 (Genoa, to Maffeo Barberini): all "cifra e decifrato".
- Barb. lat. 7633-7636: "Lettere, decifrati" of the nuncio Laudivio Zacchia, 1621-23 (clear texts).
- Vat. lat. 10421: 58 letters to G. B. Bernardi 1690-92, "in cifra, con interpretazione" (Vattasso-Carusi: an
  explanatio follows each; some "decifrata dal Sr Abbate Blasi").
- Vat. lat. 10440 (digitised): letters from Rome to the nuncio Scipione d'Elci 1652-58. ff. 1r, 45r, 99r opened:
  all are clear decipherments headed "Decifrata a dì ...". Not cipher.
- Vat. lat. 10409 (digitised): an Urbino register of 1661-62 with entries "Al Sr Card. Chigi, cifra" (register copies).
- Urb. lat. 839, 882, 1035: 1560s registers; "appartato in cifra" and "foglio in cifra" are clear copies or mentions.
- Vat. lat. 14673 ff. 85v-104r: copies of eleven letters "inviate in cifra" to the nuncio Ascanio Gesualdo, 1618
  (Piazzoni-Vian p. 7, "Copie"); sibling of lead 2201 (ff. 122r-129v, Ubaldini 1606). Not digitised; register copies,
  so probably clear.
- Medieval secret scripts already studied: Reg. lat. 2024 (a poem in secret script, Coletti 1977), Borgh. 46, 54, 173
  (Olivi codices with Guillem Negre's glosses, Troncarelli 2003), Barb. lat. 721 (Colker 1971), Vat. lat. 266 f. Ir
  (9th-c. cryptographic alphabet), Vat. lat. 2392 f. 72v (a bird-catching recipe in cipher with its explanation).
- Name-only hits: "segretario della cifra" (Vat. lat. 8338, 10285, 12564, Borg. lat. 240), Vat. lat. 12531 (a
  political text "Cifra della Corte di Roma"), Vat. lat. 12934 (the chrismon), Urb. lat. 868 f. 196r (a text "venute
  colle cifre", clear).

## Existing leads (vetting evidence; leads.json not edited)

- **1917, Cappon. 164 ff. 292r-299r**: f. 292r is headed "Cifra del Nuntio di Spagna de ultimo di Febraro 1584" and
  f. 298r "Cifra del N.o di Sp.a", both in clear Italian: register copies of the decipherments. OPAC dates the five
  letters 29 Feb - 30 Jun 1584 (the lead says 1587-1592). Close as deciphered.
- **1918, Urb. lat. 1704 f. 237r**: OPAC: "Nel codice: solo la parte in cifra, da 'Sono rimasto col [...]' a '[...]
  iusta ira di N.S.'", with Luciano Serrano as external author: a clear copy of the cipher part, printed by Serrano.
  The page (canvas label `237`) is clear Italian. Close.
- **1919, Vat. lat. 13153 ff. 38v-40v**: OPAC: "In gran parte cifrata, con decifrazione interlineare", printed by Gérin
  (Revue des questions historiques 39, 1886, pp. 117-118); f. 40r-v (Jaigel to Du Vernay, 22 Sept 1682) also
  interlinear, printed by De Bojani, Innocent XI, III (1912). Close.
- **1920, Vat. lat. 9684 ff. 23r-26r**: deciphered by Domenico Morosini in 1822 (Cicognara's letter, ff. 137r-138r);
  decipherments in the volume at f. 140r (Cancellieri) and ff. 144r-146v (Morosini). Close as read from an existing
  decipherment.
- **2201, Vat. lat. 14673**: OPAC confirms "Copie"; manifest 404 (not digitised).

## Not reached

- Volumes the OPAC describes without item-level notes: most Barb. lat. (6000-10000), Ottob. lat. and Chigi letter
  volumes have no IAM description, so a cipher in them is invisible to keyword search. The handwritten inventories
  (Sala Cons. Mss., digitised on DigiVatLib as images) were not read.
- Page-by-page passes over the digitised glossed volumes (Barb. lat. 9848-9849) for letters left without decipherment.
- Printed catalogues of Vat. lat. 10701+ and of the Barberini, Ottoboni and Chigi fondi are not on archive.org.
- AAV (Archivio Apostolico Vaticano) is a separate institution with no online images; untouched here.

## COVERAGE

The DigiVatLib row in `research/COVERAGE.md` ("Connection reset in Chrome, TLS error in curl; needs another network")
can be lifted: DigiVatLib, its search (with UA + cookie + Referer) and the BAV OPAC all answer to scripts from this
network on 6 Nov 2026. What remains unswept is the undescribed Barberini/Ottoboni/Chigi letter volumes (inventory images
only), which belongs in COVERAGE as its own row. (This file was not edited by this sweep.)
