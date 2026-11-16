# Vetting, Daniel Bourdeau (2026-11-15)

Run by Daniel Bourdeau with a Claude Code session (Claude Opus 5.5) on 15 Nov 2026, following `research/VET.md`.
The leads come from the Arabic sweep of the same day (`research/sweep_2026-11-15_arabic/`, parts B and C). No open
issue or pull request names any of these leads (searched by id, "Wetzstein", "Laud" and "Vat. ar").

## Leads

- **2887** (Berlin, diwan of as-Sukkari, 1705): unvetted. The volume is digitised (2026) but only on Orient-Digital/Qalamos, which this network cannot reach. Its shelfmark is **Wetzstein II 203**, not "Wetzstein I 203" (K10plus PPN 1982423900; Qalamos DE1Book_manuscript_00022629).
- **2888** (Berlin, Ms. or. oct. 1474, f. 1a): unvetted. The only image is Sellheim's printed strip, about 990 px long. The roughly 16 signs (stroke groups, loops, a hook) look like a numeral notation as much as a cipher, and they do not match his Greek-Coptic numerals (Abb. 46-47). Sellheim's entry is on printed p. 66, not p. 65.
- **2893** (Bodleian, Laud Or. 139, f. 101a): unvetted, access archive. Both Digital Bodleian manifests show only ff. 1a, 1b-2a, 1v-2r and 170a. Savage-Smith's "curious letter forms and undeciphered writing" does not show that this is a cipher.
- **2894** (Vatican, Vat. ar. 34, f. 288v): open, seen.kind "not online". The record is Graf's description in BAV OPAC 117402: "inscriptio cryptographica e notis numericis arabicis et copticis composita", with no reading, where the record transcribes the volume's other notes. Mai 1831 (Codices arabici XXXIV) is silent on it. There is no DigiVatLib copy. DECODE, Cryptiana/GL.htm and four web searches found nothing. Two sibling keys are untested: BnF Arabe 238 f. 384v and Vat. ar. 28. The length is unknown until an image is ordered.

## Routes

| Host | Result |
|---|---|
| sru.k10plus.de/opac-de-1 | **works** with the `pica.xsgb` (shelfmark) and `pica.xall` indexes; `recordSchema=picaxml` shows the holding (`209A`) and the digitisation platform (`220B` "IIIE Orient-Digital") |
| resolver.staatsbibliothek-berlin.de | answers, but redirects SBB00048A9700000000 to `werkansicht?PPN=NOTFOUND...` |
| content.staatsbibliothek-berlin.de | works for the VOHD volume (PPN1879940027 images 94, 462, 464-468; OCR and full-size JPG); no METS for the Orient-Digital manuscript |
| digital.staatsbibliothek-berlin.de | JavaScript shell to curl |
| qalamos.net, orient-digital.staatsbibliothek-berlin.de, mymssportal.dl.uni-leipzig.de | connection reset / no connection |
| deutsche-digitale-bibliothek.de | **bot check** (Anubis proof-of-work): left alone |
| iiif.bodleian.ox.ac.uk | works (manifests for both Laud Or. 139 objects) |
| raw.githubusercontent.com (fihrist-mss) | works (TEI for Laud Or. 139) |
| opac.vatlib.it | works (records 117402 and Vat.ar.28) |
| digi.vatlib.it | works; Vat.ar.34 is 404 (not digitised), while the Vat.ar.28 control returns 200 |
| archive.org | works (Ahlwardt vols 7 and 19 and Mai IV full text) |
| cryptiana.web.fc2.com | works (GL.htm) |

## What is left

- 2887: from another network, open Wetzstein II 203 on Orient-Digital/Qalamos; find the cipher passages and f. 103a, and test the key.
- 2888: view f. 1a of Ms. or. oct. 1474 at full size and compare it with rumi/Fasi and zimam numeral tables.
- 2893: order an image of f. 101a from the Bodleian.
- 2894: order an image of f. 288v from the BAV; open BnF Arabe 238 f. 384v and Vat. ar. 28 as keys; read Doresse (Coptic Encyclopedia) and Salah-Eldin 2013.
