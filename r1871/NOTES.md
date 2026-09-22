# DECODE R1871 + R1873 — two unrelated Venetian despatches in ASVe Busta 30 (catalogue 264)

Status: no write-up

**Verdict: both already read, by Paolo Bonavoglia** ("Decifra dispacci veneziani",
crittologia.eu/critto/venezia_nomenclatore.html). Nothing about the text is added here. Session 2026-09-22.

Catalogue 264 ("... (England?) to unknown recipient, 2 ciphertexts, 1555–1558") merges two records that belong to
different despatches, 122 years apart. Neither is from England. The "England?" region and the 1555 date come
from DECODE's R1871 metadata, which seems to have been copied from its neighbour R1872 (Giovanni Michiel,
Brussels, 19 Mar 1555, also in Bonavoglia's list).

## R1873: Alvise Mocenigo, Rome, 25 April 1558

- Images `IMG_R1873_I8945`–`I8950` (6 PNG, login, not public domain, kept git-ignored in `img/`). Folios 4–6.
- Duplicate ("Duplicato") despatch of Alvise Mocenigo K., Venetian ambassador at Rome, to Doge Lorenzo Priuli,
  "Di Roma alli 25 d'April 1558", signed. Clear Italian: Cardinal Carlo Carafa, the bishoprics of Cyprus and Brescia
  (Navagero, "mio precessor"), the Duke of Urbino's envoy.
- Four cipher passages (pp. 3, 4, 5), 176 signs, 89 distinct, each a base letter with a superscript letter
  (a^n, c^a …); a nomenclator with letters, syllables and a word list. Bonavoglia puts it in the family of "Cifra n. 3"
  (1577), similar to the cipher Michel Surian used in England in 1557.
- Bonavoglia gives the transcription and the full decipherment (saved in `r1873_bonavoglia.txt` from the Wayback
  snapshot of 22 Jun 2025). It opens: "Sua Santità quando principiai parlare di questo lo uidi alquanto mutare nella
  facia …" and continues about the Carafa nephews and the bishopric of Brescia ("il uescouado di Bressa").
- Not in CSP Venice vi (April 1558 prints only England-related despatches; checked `apr1558.txt`).

## R1871: Sebastiano Foscarini, Paris, 11 September 1680

- Images `IMG_R1871_I8939`–`I8940` (2 PNG). f. 4 (not 1555): one page of continuous digit cipher under
  "Ser.mo Principe", marked "#117 P.S. Sola", signed "Sebastian Foscarini Amb.r", dated "Parigi li … 1680"; the
  dorse is addressed to the Doge with the docket "11 Sett. 1680 … n.o 117".
- Bonavoglia's list includes "1680-09-11: Dispaccio di ambasciatore Sebastiano Foscarini", the same despatch.
  He says the Foscarini cipher was used at both Paris and Madrid and was "troppo regolare e ordinato".
- His decipherment could not be retrieved: the live page returns HTTP 500 (22 Sep 2026) and the Wayback snapshots
  show only the default (Mocenigo) despatch. Not read here; a later session can fetch it once the site is back.

## Steps

1. Fetched R1871/R1872/R1873 record pages and all 12 images with the shared DECODE cookie.
2. Viewed all pages: identified sender, place and date from the clear text, signature and dockets.
3. Grepped CSP Venice vi, April 1558 (BHO): the Mocenigo despatch is not calendared.
4. Followed Tomokiyo's note on R1872 to Bonavoglia's page; recovered its archived copy with the R1873 decipherment
   and the list naming the Foscarini 11 Sep 1680 despatch.
