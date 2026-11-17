import json
def w(i, note, access, access_note):
    json.dump({"verdict": None, "confidence": "low", "note": note, "access": access, "access_note": access_note},
              open('parts/%s.json' % i, 'w', encoding='utf8'), ensure_ascii=False, indent=1)

RG = ("Blocker stands (no verdict): fgurgia.ru still serves the RGIA record only through JavaScript (curl 16 Nov 2026 returns the page shell, "
      "no description text); the 11 Nov cloud read of the record gives a file title only and no scans. Whether the leaves carry cipher groups, "
      "office decrypts or both cannot be told without an RGIA copy order. ")
w('1872', RG + "The held vetting block of 11 Nov (vetting_held) still describes the state; nothing new was findable by script.",
  "archive", "RGIA St Petersburg, F. 472 Op. 67 D. 639, 5 leaves; description on fgurgia.ru (JS-rendered), no scans.")
w('1873', RG + "The record's own note ('bol'shinstvo ne rasshifrovany', most not deciphered) implies some were deciphered; one bundle, no identified telegram.",
  "archive", "RGIA St Petersburg, F. 472 Op. 67 D. 640, 1 bundle; no scans.")
w('1874', RG + "196 leaves of cipher telegrams seized at the Helsingfors office; addressees and systems not named.",
  "archive", "RGIA St Petersburg, F. 472 Op. 67 D. 645, 196 leaves; no scans.")
w('1875', RG + "99 leaves of cipher telegrams seized at various offices; no sender, count or system given.",
  "archive", "RGIA St Petersburg, F. 472 Op. 67 D. 646, 99 leaves; no scans.")
w('1878', RG + "Bare file title 'Dvortsovaya politsiya. Shifrovannye telegrammy', 1917-1918 (not 1917 only); the keys in D. 1070-1071 make office decipherments likely, so 'open' would be a guess.",
  "archive", "RGIA St Petersburg, F. 508 Op. 3 D. 1072; no scans.")
w('2199', "Blocker stands (no verdict): Manus 685212 gives index titles only ('con li cifre a parte', 'un'altra in Cifra', cc. 242-253), no images; APUG's own catalogue (gate.unigre.it) is behind a bot check this week, and Susta vols 2-3 were not found online in the earlier pass. Needs APUG cc. 240-254.",
  "archive", "Rome, APUG, Concilio di Trento 588rec; no images.")
w('2200', "Blocker stands (no verdict): Manus 699266 lists 'Cifre di lettere del Concilio di Trento' and 'Cifra sopra il luogo del conte di Luna' (ff. 31r-43r) by title only; nothing shows whether these are cipher groups, decrypts or keys. APUG catalogue behind a bot check. Needs APUG ff. 28-44.",
  "archive", "Rome, APUG, Concilio di Trento 608rec; no images.")
w('2203', "Blocker stands (no verdict): Manus 588084 gives only 'Carteggio del Duca di Mantova con un suo invitato a Parigi in parte in cifra' (cc. 147r-197r) with no duke, envoy or year, so prior art cannot be searched; BNC Rome Gesuitico 204 is not digitised. Needs the volume opened.",
  "archive", "Rome, BNC, Gesuitico 204, cc. 147r-197r; no images.")
w('1513', "Blocker stands (no verdict): volume-level aggregate ('oficios, telegramas y criptogramas reservados y confidenciales', three volumes 1926-1940) with no identified item, count or image; Archivo Nacional de Chile search (sinarchile) blocked to scripts as of 11 Nov. Needs consultation of the volumes.",
  "archive", "Archivo Nacional de Chile, Intendencia de Antofagasta, Comunicaciones recibidas 1926-1940; not digitised.")
w('1297', "Blocker stands (no verdict): hollisarchives.lib.harvard.edu returns HTTP 403 to curl (16 Nov 2026, both the HTML record and its .json); a web search for 'Vincent E. Keegan' with the Schlesinger Library found nothing. Only the item title 'journal pages? (in code), 1919' is known; needs the folder looked at (Chrome or the Schlesinger Library).",
  "archive", "Schlesinger Library, Harvard, sch01461 item c0021; HOLLIS 403 to scripts.")
w('2906', "No verdict: the Saxon record (curl 16 Nov 2026, digitalisatExists false) reads 'Verhaftung des Captains von Loewenburg in Naumburg wegen seiner Verbindung zu Stanislaus Leszinski ... Enthaelt u. a.: Haftbedingungen.- Verhoerprotokoll.- Zettel mit Chiffren.' (Provenienz Geheime Kriegskanzlei, Rep. Bb, Loc. 39, No. 40). 'Zettel mit Chiffren' may be ciphertext slips or a key list, and the interrogation may give their plaintext; known.py, Tomokiyo, Lasry and a web search ('Loewenburg Naumburg 1724 Leszczynski Sonnenstein') found nothing. Too uncertain for 'open' without a scan.",
  "archive", "Saechsisches Hauptstaatsarchiv Dresden, 11237 Geheimes Kriegsratskollegium, Loc. 10922/01, 1724-1725; no digital copy.")
w('1678', "No verdict: the full Saxon record (curl and DDB Solr, 16 Nov 2026; no digital copy) is a topic list for Bruehl's letters to the Electoral Prince Friedrich Christian, dated 1739, 1746, 1748-1749, 1750, 1752 (not 1739-1745), formerly Geheimes Kabinett Loc. 30539/2: '... Warschauer Hofnachrichten.- Neuer polnischer Primas Komorowski.- Verwendung von Geheimschrift.- Jesuitenpater Breinl ...'. As one topic among a dozen, 'Verwendung von Geheimschrift' may mean letters that discuss using a cipher rather than ciphered text; needs scans.",
  "archive", "Saechsisches Hauptstaatsarchiv Dresden, 12527 Nachlass Friedrich Christian, Nr. 266; no digital copy.")
