# DECODE R1873 — Alvise Mocenigo, Rome, 25 April 1558 (ASVe Busta 30, catalogue 264)

Split on 14 Oct 2026 from `r1871` under the one-key rule (George Lasry, 14 Oct 2026). Catalogue 264 and the old
`r1871` entry joined this despatch with R1871, Sebastiano Foscarini's Paris despatch of 11 Sept 1680: a different
cipher 122 years later, with its own entry ([`targets/r1871/`](../r1871/NOTES.md), page `r1871.html`).

**Outcome: read from existing decipherment.** Paolo Bonavoglia ("Decifra dispacci veneziani",
crittologia.eu/critto/venezia_nomenclatore.html) gives the transcription and the full decipherment. Nothing about the
text is added here. Session 2026-09-22.

## The despatch

- Images `IMG_R1873_I8945`–`I8950` (6 PNG, login, not public domain, kept git-ignored in the main checkout's
  `targets/r1871/img/`). Folios 4–6. The Archivio di Stato di Venezia notice on DECODE allows publication only with
  the holder's permission, so no crop is published.
- Duplicate ("Duplicato") despatch of Alvise Mocenigo K., Venetian ambassador at Rome (the later Doge Alvise I
  Mocenigo), to Doge Lorenzo Priuli, "Di Roma alli 25 d'April 1558", signed. Clear Italian: Cardinal Carlo Carafa,
  the bishoprics of Cyprus and Brescia (Navagero, "mio precessor"), the Duke of Urbino's envoy.
- DECODE metadata: catalogued as "..." to unknown recipient, Non-decrypted; the sender, recipient and place are
  corrected in `decode_updates/queue.json`.

## The cipher

- Four cipher passages (pp. 3, 4, 5), 176 signs, 89 distinct (`r1873_ciphertext.txt`, Bonavoglia's transcription;
  measured with `docs/_check_profile.py --measure`), each a base letter with a superscript letter (a^n, c^a …); a
  nomenclator with letters, syllables and a word list. Bonavoglia puts it in the family of "Cifra n. 3" (1577),
  similar to the cipher Michel Surian used in England in 1557.

## The reading

- Bonavoglia's transcription and decipherment are saved in `r1873_bonavoglia.txt` from the Wayback snapshot of
  22 Jun 2025 (the live page returned HTTP 500 on 22 Sep 2026). It opens: "Sua Santità quando principiai parlare di
  questo lo uidi alquanto mutare nella facia …" and continues about the Carafa nephews and the bishopric of Brescia
  ("il uescouado di Bressa"): Mocenigo fears the Carafa will keep the Pope from hearing him soon.
- Not in CSP Venice vi (April 1558 prints only England-related despatches; checked `apr1558.txt`).
- The key was not rebuilt here, and the decipherment was not re-checked sign by sign against the images.

## Remaining gaps

None in the text: Bonavoglia's decipherment covers all four passages. The key (sign values) is not rebuilt here;
no sign-level alignment of his transcription with his decipherment has been made.

## Escalation

- [x] siblings: R1871, R1872 (Michiel, Brussels 1555), R1874, R1875 opened; none in this key.
- [x] clear-pages: the clear text of the despatch is interspersed; no decipherment on the record.
- [n/a] known-keys: not needed; the published decipherment covers the cipher.
- [x] print: CSP Venice vi April 1558 grepped: not calendared. Bonavoglia's page is the reading.
- [n/a] key-rebuild: not attempted; the text is complete without it.
- [n/a] retry: nothing unread to retry.

## Assumptions for George's review

- Extent "complete" (fraction 1.0) rests on Bonavoglia's decipherment covering all four passages; it was not
  measured sign by sign here.

## Steps

1. Fetched R1871/R1872/R1873 record pages and all images with the shared DECODE cookie.
2. Viewed all pages: identified sender, place and date from the clear text and signature.
3. Grepped CSP Venice vi, April 1558 (BHO): the Mocenigo despatch is not calendared.
4. Followed Tomokiyo's note on R1872 to Bonavoglia's page; recovered its archived copy with the R1873 decipherment.
5. 14 Oct 2026: split from `r1871` into its own entry.
