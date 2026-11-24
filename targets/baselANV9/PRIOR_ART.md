# PRIOR_ART: baselANV9 (Basel UB, UBH AN V 9, enciphered Clavicula Salomonis and Septem sigilla planetarum)

Checked 24 Nov 2026, 21:59 to 22:10 Brisbane, before any transcription, key building or decode.
Track: adjacent plaintext (approved by Malcolm 22:3x per the brief). Outcome category if it works: key recovered from adjacent plaintext.

## Bottom line

- **No published reading, edition or study of the cipher found** [measured: searches below].
- **The volume holds its own key.** Steinmann's unprinted catalogue description (the library's PDF) says
  f. 99r is a pasted-in leaf "mit dem Schlüssel zu den Siglen der Geheimschrift sowie Erklärungen dazu auf Dänisch",
  and f. 98r is a pasted-in leaf "mit Erklärungen zu der Geheimschrift, deutsche Uebersetzung von 99r" [sourced].
  swisscollections adds: "Bl. 98 u. 99 sind zwei aufgeklebte, doppelt eingefaltete Zusatzblätter" [sourced].
- **The catalogue already identifies the plaintext.** ff. 101r-155r: "Gleicher Text wie 3r-96v, aber in normaler
  Schrift geschrieben"; ff. 166r-170r: "Gleicher Text wie 158r-162r, aber in normaler Schrift geschrieben" [sourced].
- So this is not keyless and its content is not new in principle. Nobody has published a decipherment, so it is
  not "read" in the hub's sense. Under the Cyphersolver vetting rule a key in the volume does not block a lead with no
  known decipherment (record it as `vetting.key_in_volume`).
- **Handling of the key leaf:** ff. 98-99 (canvases 199-206 in the manifest, the block between the last cipher page
  and the clear title f. 100r) are QUARANTINED: not fetched, not viewed, until FREEZE_KEY.txt exists. After the freeze
  they become an external check on the recovered key. (scripts/fetch.sh refuses canvases 199-206 until then.)

## Searches

| where | search | result |
|---|---|---|
| Hub issues | /home/claude/keyless/issues_index.tsv (931 lines) and issues_bodies.tsv (210 lines): `AN V 9`, `AN V9`, `ANV9`, `AN_V_9`, `clavicula`, `septem sigilla`, `sigilla planetarum`, `5353221`, `185551`, `e-manuscripta`, `Universitätsbibliothek Basel`, `UB Basel`, `Basel UB`, `UBH`, `Solomon`, `Salomon`, `grimoire`, `Key of Solomon`, `Basel` | 0 hits for every term except `Basel`: 3 hits in bodies, all the word "baseline" [measured] |
| Cyphersolver repo | /home/claude/cyphersolver catalogue.json, research/leads.json, research/COVERAGE.md; /home/claude/keyless/_cs and _cs_main: `AN V 9`, `Clavicula`, `Septem sigilla`, `5353221`, `e-manuscripta`, `Basel`, `Salomon`, `Solomon`, `grimoire` | no entry for this volume. `Basel` hits are a Patkul key note, Zofingen Pb 82 vetting text and a Fesch letter; `Salomon` is a Brazilian name; `Solomon` is a code name in an American letter [measured] |
| DECODE public search | tools/dsearch.py: `Clavicula`, `Salomonis`, `Solomon`, `Basel`, `sigilla`, `AN V 9`, `grimoire`, `Basel AN`, `Universitätsbibliothek Basel`, `Universitatsbibliothek Basel`, `Septem`, `magic`, `Salomon`, `planetarum`, `UBH` | no record for this volume. Hits: R2873 (Mellon MS 136), R2874 (Mellon MS 27), R3287 (a Basel postcard of 1898), and word-split noise for `AN V 9` and `Septem` [measured] |
| Web | `"AN V 9" Basel Clavicula Salomonis`; `Clavicula Salomonis verschlüsselt Basel Universitätsbibliothek Geheimschrift`; `e-manuscripta "Clavicula Salomonis" "Septem sigilla planetarum"`; `swisscollections "Clavicula Salomonis" Basel "AN V 9"`; `"Clavicula Salomonis" Basel Handschrift Geheimschrift "K IV 19" OR "AN V 9"`; `"Key of Solomon" manuscript written in cipher secret alphabet encrypted copy`; `"Salomons nøgle" OR "Clavicula Salomonis" dansk chiffer håndskrift Basel` | no page on this manuscript or its cipher. Results are general Clavicula material (Wikipedia, esotericarchives, Wellcome, Penn, Karlsruhe, Gal Sofer's Hebrew Clavicula article in HTR 119/2, 2026, checked: no Basel, no cipher copy) [measured] |
| Schmeh | Encrypted Book List (scienceblogs.de/klausis-krypto-kolumne/klaus-schmehs-list-of-encrypted-books/), read in two parts; web search Schmeh + Clavicula | no entry for Solomon, Salomonis, Clavicula, Basel or sigilla. Magic entries are Kassel, Heidelberg Cod. Pal. germ., Sloane 3822, the Cipher Manuscripts, the Triangular Book, Soyga, Steganographia [measured] |
| Clavicula literature | Skinner and Rankine, *The Veritable Key of Solomon* (2008); Boudet's Clavicula work (HAL halshs-03366136, his publication list); Mathers (1889) | web searches turned up no mention of a Basel cipher copy. The books themselves were not opened: Skinner/Rankine and Mathers are print; Boudet's manuscript census not read in full [unverified: absence in print not checked] |
| Library catalogue | Steinmann, unprinted description, PDF linked from the METS record: https://ub.unibas.ch/digi/a100/kataloge/mscr/mscr_div_gr/BAU_9972848358705504_cat.pdf (plain curl, HTTP 200, 2 pages; saved as work/steinmann_cat.pdf, rendered work/steinmann-1.png, -2.png) | contents quoted above; old shelfmark K IV 19; "In einer Art Geheimschrift geschrieben"; ff. 33r-55v drawings of pentacula on rectos, versos blank; 97r-97v two pentacula; 157r magic squares; 172r-177r astrological tables in several hands [sourced] |
| Library catalogue | swisscollections record 991171912544105501 (= 41SLSP_UBS 9972848358705504), read in Malcolm's cleared Chrome session at 22:08 (own tab, closed after) | adds the quire note on ff. 98-99 quoted above and "Moderne Bleistiftfoliierung: I.1-179"; no reading, no literature beyond Steinmann [sourced] |

## Bot checks met (not passed by me)

| URL | what it showed | what I did |
|---|---|---|
| https://swisscollections.ch/Record/991035022369705501 (plain curl) | Anubis "Making sure you're not a bot!" | stopped; later read the correct record in Malcolm's cleared Chrome session (coordinator message 22:06) |
| https://www.e-manuscripta.ch/bau/content/titleinfo/5353221 (plain curl) | "Verifying your browser" | stopped; not needed: the IIIF manifest https://www.e-manuscripta.ch/i3f/v20/5353221/manifest answered plain curl (JSON, 380 canvases) |

Page images: https://www.e-manuscripta.ch/i3f/v20/<page id>/full/2000,/0/default.jpg answer plain curl (FETCH_LOG.txt).
