# DigiVatLib letter volumes without item descriptions, sweep of 11 Nov 2026 (cloud session)

Result: **0 candidate rows** (`candidates.json` is `[]`), no key leads. What the sweep adds is a map: which digitised
Barberini and Chigi letter volumes hold ciphertext, and that in every one of them the Roman decipherment (*decifrato*)
is bound next to the cipher sheet. Twelve digitised volumes of original cipher that are not on DECODE are listed below;
they are worked material (cipher with its plaintext), not unread letters.

## Routes from this network (11 Nov 2026)

- `digi.vatlib.it` and `opac.vatlib.it` answer curl/urllib with a browser User-Agent, cookie and Referer. No 429 or 403
  in this pass at one request every 2-3 s per host. Response time is the limit: 3 to 7 s per thumbnail for long
  stretches, so a 10-image sample of one volume takes about a minute and a page-by-page pass of 450 leaves about 40.
- **New, and the main shortcut: the fondo page lists every digitised shelfmark in one request.**
  `https://digi.vatlib.it/mss/Barb.lat` (also `/mss/Chig`, `/mss/Ott.lat`, `/mss/Urb.lat`, `/mss/Ross`, `/mss/Ferr`,
  `/mss/Cappon`, `/mss/Bonc`, `/mss/Patetta`, `/mss/Borg.lat`, `/mss/Reg.lat`) returns the full list of
  `/mss/edition/MSS_<Shelfmark>` links. No manifest probing is needed to learn what is digitised (the earlier 429 came
  from probing). Counts: Barb. lat. 2,440 (263 of them in 5600-9899), Chig. 1,282, Ott. lat. 4,760, Urb. lat. 3,190,
  Ross. 2,146, Ferr. 78, Cappon. 604, Bonc. 72, Patetta 128, Borg. lat. 174.
- The OPAC shelfmark page `opac.vatlib.it/mss/detail/<Shelfmark>` gives, for an undescribed volume, only its
  bibliography. The bibliography is still a usable handle: Pasture's inventory marks Low Countries material, Kraus
  marks Secretariat minutes, Platania marks the Polish papers, Tusor and Becker the Vienna nunciature.
- IIIF as before: manifest `https://digi.vatlib.it/iiif/MSS_<Shelfmark>/manifest.json`, image service id +
  `/full/<w>,/0/default.jpg`. Many Barberini volumes are microfilm scans ("Low Quality"), two pages to a frame; cipher
  digits are legible at 1300-1500 px.
- DECODE `RecordsList?search=...&cmd=search` answers curl (`decode_q.sh`). Searches run: `Barberini` (ASV Segr. Stato
  Francia 346 records only), `Barb. lat`, `Bibliotheca Apostolica` with 500 per page (99 records: Barb. lat. 6956 and
  6960 only, the Pallotto volumes already in `targets/pallotto1629`), `Mancini` (none), `Biblioteca Apostolica` (none).

## Scripts

`opacdet.py` (OPAC shelfmark pages to jsonl), `opac.py` (term harvest, copied from the 6 Nov sweep with a 3 s wait;
writes `hits.jsonl` here), `man.py` (manifests), `sheet.py` (thumbnails of every Nth canvas or N evenly spaced, and
contact sheets), `mksheet.py`, `combo.py` (stack several volumes' sheets), `leaf.py` (single leaves or the top strip
by canvas index), `decode_q.sh`, `run_g.sh` / `run_h.sh` / `run_i.sh` / `run_k.sh` (the queues). All images went to
scratch.

## What was looked at

OPAC bibliography read for all 263 digitised Barb. lat. 5626-9860. Dropped unseen: the avvisi (6338-6428, 9828-9837),
Lincei, Holste, Ughelli and other scholarly letter-books (6456-6517), inquisition and curial volumes. Sampled on
contact sheets (10 to 40 frames each, cipher-looking frames then opened at 1000-1500 px):

| Volumes | What they are (seen) | Cipher |
|---|---|---|
| Barb. lat. 6929, 6930, 6939, 6943, 6944, 6964, 6985, 6986, 7017, 7025, 7045, 7046, 7053 | Germania: nuncios' clear letters (Graz, Carafa, Pallotto 1630, Baglioni, Mattei) | none in sample; 6939's dark slips are avvisi |
| Barb. lat. 6946 | Carafa, Vienna: decifrati only | plaintext only |
| **Barb. lat. 6948** | Carlo Carafa, Vienna 1625 (f. 86 "Di Vienna dal Vesc.o d'Aversa li 21 di Maggio 1625. Decifrato a 25 d.") | cifre + decifrati |
| **Barb. lat. 7004, 7005, 7006, 7007** | Malatesta Baglioni, Vienna and Pressburg, Nov 1637 - spring 1638 (7004 f. 26 "Di Vienna da Mons. Nun. li 14 di Novembre 1637. Decifrato li 3 di Decembre"; f. 87 cipher "Posonia 4 Xbre 1637", 14 lines of run-on digits; f. 111 "Posonia 11 Xbre 1637", 20 lines) | cifre + decifrati |
| **Barb. lat. 7029** | Germania series, cipher sheets (f. 14: 9 lines of digits, a date of 164[?] in the margin), decifrati and some Latin letters; correspondent not read | cifre + decifrati |
| **Barb. lat. 7050** | P. Alessandro d'Ales, Vienna 1634 (f. 88 "Di Vienna dal P. Aless.o d'Ales li 26 d'Agosto 1634, decif. li 14 di Sett."; f. 186 a memorandum in mixed clear and digit cipher) | cifre + decifrati |
| Barb. lat. 7060, 7063 | registers of minutes | none |
| **Barb. lat. 8105** | France nunciature, 1634 (Richelieu, Epernon and the archbishop of Bordeaux in the decifrati): 124 frames viewed one by one | cifre + decifrati |
| Barb. lat. 8106 | France, clear letters | none in sample |
| **Barb. lat. 8175, 8178** | France nunciature: 8175 f. 14 "... da Mons. Nun.o di Francia delli 8 Gennaro 1638. Deciferato li 21" with the cipher sheet facing it (15 lines of digits); 8178 f. 60 a full sheet of run-on digits | cifre + decifrati |
| Barb. lat. 8268, 8458, 8463, 8464, 8483, 8535, 8536, 8563, 8578 | Spain, Catalonia 1642-43 and others: clear letters and prints | none in sample |
| **Barb. lat. 8404** | cipher sheets and decifrati (shelved with the Spain series; correspondent not read); ff. 27v-28r are two full pages of digits, about 28 lines each | cifre + decifrati |
| Barb. lat. 8615, 8616, 8618, 8625, 8626 | England: royal letters, clear | none in sample |
| Barb. lat. 6563-6565, 6649-6654 | Carlo Barberini's Polish papers, clear | none in sample |
| Barb. lat. 9848 | Francesco Mancini, Madrid 1654: frames 30-179 (ff. 14r-88v) of 448 viewed one by one | cifre + decifrati (below) |
| Chig. A.I.23, A.II.27, 28, 33, 34, 35, 38, 44, 47 | Fabio Chigi's Cologne and Münster papers: registers, van der Veken's Latin letters, Barberini's signed letters | none in sample |

Chig. A.I.35-60: none is digitised (fondo list). Digitised in Chig. A are A.I.4, 6, 7, 8, 20-23, 25, A.II.27-30, 33-35,
38, 44, 47 and scattered A.IV-A.VIII volumes.

## Why there are no rows

- **Barb. lat. 9848** (Mancini to Card. Francesco Barberini, Madrid, Aug-Sept 1654). Ff. 14r-88v viewed one by one.
  The cipher is run-on digits. Each despatch is there as original, duplicate and triplicate (ff. 29r, 34r, 38r all
  begin `2321 26 23 29 65 65 39 ...`, "Madrid 12 Agosto 1654"), and the Roman clerk's sheet "Madrid 12 Agosto 1654.
  Decifrato del S.r Mancini" is at f. 27r. Letters with cipher passages inside clear text (ff. 81r, 85r "Dupp.to",
  87r "Triplicato") have their decifrato at f. 83r ("Con lettera del S.r Mancini delli 16 Sett. 1654", the same opening
  sentence in clear). Nothing unpaired found in those leaves. Ff. 1-13 and 89-216 (and 9849, 9860) were not viewed: image speed.
- **Barb. lat. 8105** (all 124 frames): every run of cipher sheets follows a sheet headed "Di ... Decifrato li ...".
  No cipher run without a decifrato before it was seen at thumbnail size; dates were not matched one by one.
- The other volumes in bold show the same layout on every sampled frame: decifrato, then the cipher sheet, with the
  ink of one showing through the other.
- Print: Carafa 1621-28, Pallotto 1628-30, Rocci, Baglioni 1634-35 and d'Ales 1634-35 are in *Nuntiaturberichte aus
  Deutschland*, IV. Abteilung (a web search confirms Bd. 7, Becker 2004, ends in 1635). Baglioni 1637-38 (Barb. lat.
  7004-7007) falls after the printed volumes; the decifrati in the volume are the reading, and the British Library holds
  Baglioni's own letter-books with "Registro delle Cifre" (web search result, catalogue not opened).

So these are not unread ciphers. They are, like Barb. lat. 6956/6960 (`targets/pallotto1629`), long digit ciphertexts
with their plaintext alongside, online, and absent from DECODE: usable for a key recovery from adjacent plaintext or as
a DECODE addition, if the project wants that kind of target. A letter left without its decifrato could still exist in
them; finding one takes a date-by-date match of every sheet, which was done for no volume.

## OPAC terms run (on top of the two 6 Nov sweeps)

`dispacci` 12, `registro di lettere` 24, `lettere di nunzi` 15, `nunzio` 297, `ambasciatore` 290, `lettere cifrate` 2,
`decifrati` 35. Nothing new for Ott. lat., Urb. lat., Ross., Ferr., Cappon., Bonc., Patetta: the Urb. lat. hits are
avvisi and register copies already read on 6 Nov; `decifrati` returns only the Barberini agents' series already
described (9848-9884) and Zacchia (7633-7636, undigitised); Borg. lat. 898 ("Cifrario farmacologico") was closed by
the vatican_rome sweep.

## What remains

- Page-by-page date matching of cifra against decifrato in Barb. lat. 6948, 7004-7007, 7029, 7050, 8105, 8175, 8178,
  8404, and the rest of 9848, 9849, 9860 (the only route to an orphan cipher sheet).
- Digitised Barb. lat. letter volumes not sampled: 7196-7428, 7789-8015, 8586, 8600, 8725-8979, 9192-9746 (all
  "Shelfmark only" in the OPAC), and the queue in `run_k.sh` as far as it did not finish (see the end of this file).
- Ott. lat., Ross., Ferr., Reg. lat. letter volumes: still no handle. The fondo lists give the digitised shelfmarks, but
  nothing says which are letters; the handwritten Sala Cons. inventories were not read.
- Undigitised: Chig. A.I.35-60, and the Barberini France, Spain and Germania cifre volumes between the digitised ones.
